import flet as ft

def main(page: ft.Page):
    page.title = "Мой мессенджер"
    
    messages = ft.Column()
    user_input = ft.TextField(label="Ваше имя")
    msg_input = ft.TextField(label="Сообщение", multiline=True)
    
    def send_click(e):
        if user_input.value and msg_input.value:
            messages.controls.append(
                ft.Text(f"{user_input.value}: {msg_input.value}")
            )
            msg_input.value = ""
            page.update()
    
    page.add(
        user_input,
        msg_input,
        ft.ElevatedButton("Отправить", on_click=send_click),
        messages
    )

ft.app(target=main)
