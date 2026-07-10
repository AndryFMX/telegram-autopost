import os
import time
import requests

TOKEN = "8926173750:AAEl_wflDiJPtY6aDQwbOG-yOqqZyfHhBos"
CHAT_ID = "@lauramendosaf777"

TEXT = """
AMOR AQUÍ EL RETO 🚫‼️🔴
🤤🌶️🔥🙈👇🏻
https://miraelretoenvivo.short.gy/laura

SI NO LES FUNCIONA EL LINK ENTREN AQUÍ
👇🏻🙈🔥💕
https://miraelretoenvivo.short.gy/laura
"""

LAST_ID_FILE = "last_message.txt"

# Cargar el último message_id si existe
last_message_id = None
if os.path.exists(LAST_ID_FILE):
    with open(LAST_ID_FILE, "r") as f:
        contenido = f.read().strip()
        if contenido:
            last_message_id = int(contenido)

while True:

    # Eliminar el último mensaje si existe
    if last_message_id:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/deleteMessage",
            data={
                "chat_id": CHAT_ID,
                "message_id": last_message_id
            }
        )

    # Enviar el nuevo mensaje
    r = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": TEXT,
            "disable_web_page_preview": False
        }
    )

    data = r.json()

    if data.get("ok"):
        last_message_id = data["result"]["message_id"]

        # Guardar el último message_id
        with open(LAST_ID_FILE, "w") as f:
            f.write(str(last_message_id))

        print("Mensaje enviado:", last_message_id)
    else:
        print("Error:", data)

    time.sleep(60)
