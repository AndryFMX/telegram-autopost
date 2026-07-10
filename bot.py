import requests

TOKEN="8926173750:AAEl_wflDiJPtY6aDQwbOG-yOqqZyfHhBos"

CHAT_ID="@lauramendosaf777"

TEXT="""
AMOR AQUÍ EL RETO 🚫‼️🔴
🤤🌶️🔥🙈👇🏻
https://miraelretoenvivo.short.gy/laura

SI NO LES FUNCIONA EL LINK ENTREN AQUÍ
👇🏻🙈🔥💕
https://miraelretoenvivo.short.gy/laura
"""

url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url,data={
"chat_id":CHAT_ID,
"text":TEXT
})
