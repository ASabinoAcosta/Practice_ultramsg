"""
Un pequeño programa en el cual se podrán visualizar los mensajes enviados y recibidos.
Enviar y recibir imágenes. Ver estado de los mensajes.
"""

import requests
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('ultramsg.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatId TEXT NOT NULL,
    fecha TEXT NOT NULL,
    body TEXT NOT NULL,
    status TEXT NOT NULL,
    remitente TEXT NOT NULL
    ''')

def get_chatid(token):
    pass

def screen(token, chatId):
    """
    Función para mostrar los mensajes de un chat específico.
    Se conecta a la base de datos 'ultramsg.db' y obtiene todos los mensajes
    asociados al chatId proporcionado. Los mensajes se devuelven como una lista de tuplas,
    donde cada tupla representa un mensaje con sus detalles.
    """

    cursor.execute("SELECT * FROM messages WHERE chatId = ?", (chatId,))
    messages = cursor.fetchall()
    
    return messages

def get_messages(token, chatId):
    """
    
    """
    pass

def sent(instance, token, to):
    """
    Tomar los datos y enviar el mensaje.

    Si quiere enviar un archivo usar sent_doc.
    Si quiere enviar una imagen usar sent_img.
    """

    def sent_img(instance, token, to):
        url_img = f"https://api.ultramsg.com/{instance}/messages/image"
        
        img_url = input("URL de la imagen: ")
        
        caption = input("Pie de foto (opcional): ")
        
        payload_img = f"token={token}&to={to}&image={img_url}&caption={caption}"
        
        payload_img = payload_img.encode('utf8')
        
        response = requests.request("POST", url_img, data=payload_img, headers=headers_post)
        
        return response.text
    
    def sent_doc(instance, token, to):
        url_doc = f"https://api.ultramsg.com/{instance}/messages/document"
        
        doc_url = input("URL del archivo: ")
        
        filename = input("Nombre del archivo (con extensión): ")

        caption = input("Pie de documento (opcional): ")
        
        payload_doc = f"token={token}&to={to}&filename={filename}&document={doc_url}&caption={caption}"
        
        payload_doc = payload_doc.encode('utf8')
        
        response = requests.request("POST", url_doc, data=payload_doc, headers=headers_post)
        
        return response.text

    user_input = input("¿Qué vas a enviar? Imagen, archivo o mensaje: ")
    if user_input.lower() == "imagen":
        sent_img(instance, token, to)
    elif user_input.lower() == "archivo":
        sent_doc(instance, token, to)
    else:
        body = input("Mensaje: ")
        payload = f"token={token}&to={to}&body={body}"
        payload = payload.encode('utf8')
        response = requests.request("POST", url, data=payload, headers=headers_post)
        print(response.text)

instance = input("Instancia: ")
token = input("Token: ")
to = input("Número de teléfono (ej. +1...): ")

url = f"https://api.ultramsg.com/{instance}/messages/chat"

headers_post = {'content-type': 'application/x-www-form-urlencoded'}

sent(instance, token, to)

# Encontrar un orden para realizar las funciones sin problemas

conn.close()