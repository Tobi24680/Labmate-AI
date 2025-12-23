import subprocess
import os

# Optional: full path to Ollama executable if not in PATH
OLLAMA_CLI = r"C:\Users\SRIMATHI\AppData\Local\Programs\Ollama\ollama.exe"  # or r"C:\Users\YourUser\ollama.exe"

OLLAMA_MODEL = "qwen2.5:1.5b"  # your model

def lab_ai_response(prompt: str) -> str:
    try:
        result = subprocess.run(
            [OLLAMA_CLI, "run", OLLAMA_MODEL, prompt],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            return f"❌ Ollama error: {result.stderr.strip() or 'Unknown error'}"

        return result.stdout.strip() or "⚠️ Ollama returned no response."

    except FileNotFoundError:
        return "❌ Ollama CLI not found. Make sure it's installed and in PATH."
    except subprocess.TimeoutExpired:
        return "⚠️ AI took too long to respond."
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
