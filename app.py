import flet as ft
import asyncio
from datetime import datetime
from back import lab_ai_response

chat_history = []

def setup_drawer(page: ft.Page):
    
    def nav_home(e):
        home(page)
        page.drawer.open=False
        page.update()

    def nav_history(e):
        history_screen(page)
        page.drawer.open=False
        page.update()

    def nav_contact(e):
        contact_screen(page)
        page.drawer.open=False
        page.update()

    def nav_about(e):
        about_screen(page)
        page.drawer.open=False
        page.update()

    
    page.drawer=ft.NavigationDrawer(
        controls=[
            ft.Text("AI LabMate...", size=25, weight="bold"),
            ft.Divider(),
            ft.ListTile(title=ft.Text("New Chat"), leading=ft.Icon(ft.Icons.MESSAGE, color=ft.Colors.BLUE),
                        on_click=nav_home),
            ft.ListTile(title=ft.Text("Chat History"), leading=ft.Icon(ft.Icons.HISTORY, color=ft.Colors.GREEN),
                        on_click=nav_history),
            ft.ListTile(title=ft.Text("Contact Us"), leading=ft.Icon(ft.Icons.CONTACT_PAGE, color=ft.Colors.ORANGE),
                        on_click=nav_contact),
            ft.ListTile(title=ft.Text("About App"), leading=ft.Icon(ft.Icons.INFO_OUTLINE, color=ft.Colors.PURPLE),
                        on_click=nav_about),
        ]
    )

def splash(page: ft.Page):
    page.controls.clear()
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Container(
                        width=120,
                        height=120,
                        border_radius=60,
                        bgcolor=ft.Colors.BLUE,
                        alignment=ft.alignment.center,
                        content=ft.Icon(ft.Icons.CHAT, size=64, color=ft.Colors.WHITE),
                    ),
                    ft.Text("LAB MATE", size=26, weight=ft.FontWeight.BOLD),
                    ft.Text("Powered by AI", size=12, color=ft.Colors.BLUE_GREY),
                    ft.ProgressRing(),
                ],
            ),
        )
    )
    page.update()

def about_screen(page: ft.Page):
    setup_drawer(page)
    page.controls.clear()
    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("AI LabMate", size=26, weight="bold"),
                    ft.Text("Your Smart Offline AI Lab Assistant Here."),
                    ft.Divider(),

                    ft.Text("📌 App Usage", weight="bold"),
                    ft.Text(
                        "AI LabMate helps students understand and complete "
                        "Computer Science students lab experiments, programs, algorithms, "
                        "and viva questions using AI-powered explanations ect..."
                    ),

                    ft.Text("✨ Features", weight="bold"),
                    ft.Text("• Lab experiment guidance"),
                    ft.Text("• AI-based doubt solving"),
                    ft.Text("• Chat history"),
                    ft.Text("• Drawing / rough work canvas"),
                    ft.Text("• Simple & student-friendly UI"),
                    ft.Text("• Offline App"),

                    ft.Divider(),
                    ft.Text("👨‍💻 Developer", weight="bold"),
                    ft.Text("Name: SHREERAM M K"),
                    ft.Text("Tech Stack: Python, Flet, LLM"),
                ],
            ),
        )
    )
    page.update()


def contact_screen(page):
    setup_drawer(page)
    page.controls.clear()
    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("Contact & Help", size=26, weight="bold"),
                    ft.Text("We're here to help students get the most from AI LabMate."),
                    ft.Divider(),

                    ft.Text("📧 Email", weight="bold"),
                    ft.Text("For bug reports or detailed queries: sumathidevan2006@gmail.com"),

                    ft.Text("💬 Social", weight="bold"),
                    ft.Text("Follow for updates: GITHUB: Tobi24680 | X: @ailabmate"),

                    ft.Text("❓ Help & FAQ", weight="bold"),
                    ft.Text(
                        "If the AI gives an incorrect answer, try rephrasing your question or "
                        "asking for step-by-step clarification. For local model issues, install the"
                        " required packages listed in the app README."
                    ),

                    ft.Text("🛠️ Developed by", weight="bold"),
                    ft.Text("Name: Tobi24680"),
                    ft.Text("Tech Stack: Python, Flet, HuggingFace / OpenAI (optional)"),

                    ft.Divider(),
                    ft.Row(
                        controls=[
                            ft.Button("Report a Bug", on_click=lambda e: page.launch_url("sumathidevan2006@gmail.com")),
                            ft.Button("Project Repo", on_click=lambda e: page.launch_url("https://github.com/Tobi24680")),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
            ),
        )
    )
    page.update()


def history_screen(page):
    setup_drawer(page)
    page.controls.clear()

    items = []
    for h in chat_history:
        items.append(
            ft.ListTile(
                leading=ft.Icon(ft.Icons.QUESTION_ANSWER, color=ft.Colors.BLUE),
                title=ft.Text(h["question"]),
                subtitle=ft.Text(h["time"]),
            )
        )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Text("Chat History", size=22, weight="bold"),
                ft.Divider(),
                ft.Column(items, scroll="adaptive"),
            ],
        )
    )
    page.update()


def help_screen(page: ft.Page):
    setup_drawer(page)
    page.controls.clear()
    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("Help & Guide", size=26, weight="bold"),
                    ft.Text("Get started with AI LabMate - your offline AI lab assistant."),
                    ft.Divider(),

                    ft.Text("🚀 Step-by-Step Guide", weight="bold"),
                    ft.Text("1. Launch the App: Open AI LabMate on your device."),
                    ft.Text("2. Start Chatting: Type your lab question in the input field at the bottom."),
                    ft.Text("3. Get AI Response: Wait for the AI to provide explanations or guidance."),
                    ft.Text("4. Access History: Tap the menu icon to view your chat history."),
                    ft.Text("5. Explore Features: Use the navigation bar to switch between Home, About, and Help."),
                    ft.Text("6. Contact Support: For issues, use the Contact Us section in the drawer."),

                    ft.Text("💡 Tips", weight="bold"),
                    ft.Text("• Ask clear, specific questions for better answers."),
                    ft.Text("• Rephrase if the response isn't helpful."),
                    ft.Text("• The app works offline for privacy."),

                    ft.Divider(),
                    ft.Text("📧 Feedback", weight="bold"),
                    ft.Text("We value your feedback! Share your thoughts or report issues."),
                    ft.Row(
                        controls=[
                            ft.Button("Send Feedback", on_click=lambda e: page.launch_url("mailto:sumathidevan2006@gmail.com?subject=AI LabMate Feedback")),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
            ),
        )
    )
    page.update()

def home(page: ft.Page):
    setup_drawer(page)
    page.controls.clear()
    page.title = "AI LABMATE"
    page.theme_mode = ft.ThemeMode.LIGHT

    async def type_anim(text, msg):
        msg.value = ""
        for ch in text:
            msg.value += ch
            page.update()
            await asyncio.sleep(0.02)

    async def send(e):
        if not user_input.value.strip():
            return

        user_query = user_input.value
        quote.visible = False

        chat.controls.append(
            ft.Row(
                [ft.Container(expand=True),
                 ft.Container(
                     content=ft.Text(user_input.value, color="white"),
                     bgcolor="#6366F1",
                     padding=10,
                     border_radius=12,
                 )]
            )
        )

        bot_text = ft.Text()
        thinking_indicator = ft.Container(
            content=ft.Text("Thinking...", size=10, color=ft.Colors.GREY),
            bgcolor="#F3F4F6",
            padding=10,
            border_radius=12,
        )
        thinking_row = ft.Row([thinking_indicator, ft.Container(expand=True)])
        chat.controls.append(thinking_row)

        user_input.value = ""

        page.update()

        ai_response = None

        try:
            ai_response = await asyncio.to_thread(lab_ai_response, user_query)
            thinking_indicator.content = bot_text
            await type_anim(ai_response, bot_text)
        except Exception as error:
            ai_response = f"Error: {str(error)}"
            thinking_indicator.content = bot_text
            await type_anim(ai_response, bot_text)

        chat_history.append({
            "question": user_query,
            "response": ai_response,
            "time": datetime.now().strftime("%H:%M")
        })

    quote = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.LIGHTBULB, size=50, color="#6366F1"),
                ft.Text("Learning becomes easy with the right guide.", italic=True),
            ],
            horizontal_alignment="center",
        ),
        alignment=ft.alignment.center,
        visible=True,
    )

    chat = ft.Column(scroll="adaptive", spacing=10)

    user_input = ft.TextField(hint_text="Ask your lab question...", expand=True, on_submit=lambda e: page.run_task(send, e))
    send_btn = ft.IconButton(
        icon=ft.Icons.ARROW_FORWARD,
        on_click=lambda e: page.run_task(send, e)
    )

    quote.visible = len(chat_history) == 0

    if chat_history:
        for h in chat_history:
            chat.controls.append(
                ft.Row(
                    [ft.Container(expand=True),
                     ft.Container(
                         content=ft.Text(h["question"], color="white"),
                         bgcolor="#6366F1",
                         padding=10,
                         border_radius=12,
                     )]
                )
            )
            bot_text = ft.Text(h["response"])
            chat.controls.append(
                ft.Row(
                    [ft.Container(
                         content=bot_text,
                         bgcolor="#F3F4F6",
                         padding=10,
                         border_radius=12,
                     ), ft.Container(expand=True)]
                )
            )

    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.MENU,
            on_click=lambda e: (setattr(page.drawer, "open", True), page.update())
        ),
        title=ft.Text("AI LabMate"),
        center_title=True,
    )

    def nav_change(e):
        if e.control.selected_index == 0:
            home(page)
        elif e.control.selected_index == 1:
            about_screen(page)
        elif e.control.selected_index == 2:
            help_screen(page)
        page.navigation_bar.selected_index = e.control.selected_index
        page.update()

    page.navigation_bar = ft.NavigationBar(
        on_change=nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.INFO, label="About"),
            ft.NavigationBarDestination(icon=ft.Icons.HELP, label="Help"),
        ],
    )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                quote,
                ft.Column(expand=True, controls=[chat], scroll="adaptive"),
                ft.Divider(height=1),
                ft.Row([user_input, send_btn], spacing=8),
            ],
        )
    )

    page.update()

async def app(page: ft.Page):
    splash(page)
    await asyncio.sleep(3)
    home(page)


def main(page: ft.Page):
    page.run_task(app, page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
