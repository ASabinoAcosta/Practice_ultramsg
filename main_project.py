"""
Un pequeño programa en el cual se podrán visualizar los mensajes enviados y recibidos.
Enviar y recibir imágenes. Ver estado de los mensajes.
"""

import requests
import sqlite3

instance = input("Instancia: ")
token = input("Token: ")

url = f"https://api.ultramsg.com/{instance}/messages/chat"

headers_post = {'content-type': 'application/x-www-form-urlencoded'}

to = input("tel. number: ")


def get_chatid(token):
    pass

def screen(token, chatId):
    pass

def sent(to):
    """
    Tomar los datos y enviar el mensaje.

    Si quiere enviar un archivo usar sent_doc.
    Si quiere enviar una imagen usar sent_img.
    """
    user = input("""
    1. send text 2. send docs 3. send images
    """)

    if user == "1":
        body = input("escribe tu texto: ")

    payload = f"token={token}&to={to}&body={body}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    
    response = requests.request("POST", url, data=payload, headers=headers_post)

    response.raise_for_status()

    print(response.text)
    
