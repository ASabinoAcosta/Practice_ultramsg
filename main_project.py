"""
Un pequeño programa en el cual se podrán visualizar los mensajes enviados y recibidos.
Enviar y recibir imágenes. Ver estado de los mensajes.
"""

import requests
import sqlite3

instance = input("Instancia: ")
token = input("Token: ")
to = input("Número de teléfono (ej. +1...): ")

url = f"https://api.ultramsg.com/{instance}/messages/chat"

headers_post = {'content-type': 'application/x-www-form-urlencoded'}

payload = "token={TOKEN}&to=&body=WhatsApp API on UltraMsg.com works good"
payload = payload.encode('utf8').decode('iso-8859-1')
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


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
    pass

# Encontrar un orden para realizar las funciones sin problemas