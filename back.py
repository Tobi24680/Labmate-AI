"""
Local-only backend for LabMate using HuggingFace models.
Safe for Flet apps (lazy loading + CPU/GPU aware).
"""

_GENERATOR = None


def _get_generator():
    global _GENERATOR
    if _GENERATOR is not None:
        return _GENERATOR

    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
        import torch
    except Exception as e:
        return e

    model_name = "google/flan-t5-base"

    try:
        device = 0 if torch.cuda.is_available() else -1

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == 0 else torch.float32,
        )

        _GENERATOR = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            device=device,
            max_new_tokens=256,
            do_sample=False,      # IMPORTANT for lab accuracy
        )

        return _GENERATOR

    except Exception as e:
        return e


def lab_ai_response(user_query: str):
    """
    Generate CS Lab–only responses using a local HuggingFace model.
    """

    prompt = (
        "You are an AI Lab Assistant for Computer Science students.\n"
        "Answer ONLY computer science LAB experiments, programs, algorithms, "
        "viva questions, and lab doubts.\n\n"
        f"Question: {user_query}\n"
        "Answer:"
    )

    gen = _get_generator()

    if gen is None:
        return (
            "❌ Local AI not available.\n"
            "Install dependencies:\n"
            "pip install transformers torch accelerate"
        )

    if isinstance(gen, Exception):
        return f"❌ Model load failed:\n{str(gen)}"

    try:
        out = gen(prompt)

        if isinstance(out, list) and len(out) > 0:
            return out[0].get("generated_text") or out[0].get("text", "")

        return str(out)

    except Exception as e:
        return f"❌ AI inference error:\n{str(e)}"
