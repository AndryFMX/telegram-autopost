import requests

TOKEN="8926173750:AAEl_wflDiJPtY6aDQwbOG-yOqqZyfHhBos"

CHAT_ID="@lauramendosaf777"

TEXT="""
Hola 👋

Este mensaje fue enviado automáticamente.
"""

url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url,data={
"chat_id":CHAT_ID,
"text":TEXT
})
