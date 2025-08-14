"""
Un pequeño programa en el cual se podrán visualizar los mensajes enviados y recibidos.
Enviar y recibir imágenes o documentos. Ver estado de los mensajes.
"""

import requests
import sqlite3
import base64

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
    )''')
conn.commit()

def get_chatid(token):
    """
    Para obtener el chatId del usuario.
    """
    pass

def screen(token, chatId):
    """
    Para mostrar los mensajes de un chat específico.
    Se conecta a la base de datos 'ultramsg.db' y obtiene todos los mensajes
    asociados al chatId proporcionado. Los mensajes se devuelven como una lista de tuplas,
    donde cada tupla representa un mensaje con sus detalles.
    """

    cursor.execute("SELECT * FROM messages WHERE chatId = ?", (chatId,))
    messages = cursor.fetchall()
    
    return messages

def get_messages(token, chatId):
    """
    Para obtener los mensajes de un chat específico.
    """
    pass

def sent(instance, token, to):
    """
    Tomar los datos y enviar el mensaje.

    Si quiere enviar un archivo usar sent_doc.
    Si quiere enviar una imagen usar sent_img.
    """

    def sent_img(instance, token, to):
        """
        Para enviar imágenes.
        """
        url_img = f"https://api.ultramsg.com/{instance}/messages/image"
        
        img_url = input("URL de la imagen: ")
        
        headers_post = {'content-type': 'application/x-www-form-urlencoded'}
        
        caption = input("Pie de foto (opcional): ")
        
        payload_img = f"token={token}&to={to}&image={img_url}&caption={caption}"
        
        payload_img = payload_img.encode('utf8')
        
        response = requests.request("POST", url_img, data=payload_img, headers=headers_post)

        print(response.text)

    
    def sent_doc(instance, token, to):
        """
        Para enviar documentos.
        """
        url_doc = f"https://api.ultramsg.com/{instance}/messages/document"

        user = input("Local o URL: ")

        if user.lower() == "local":
            file_path = input("Ruta del archivo local: ")
            with open(file_path, "rb") as f:
                doc_data = f.read()
            doc_url = f"data:application/octet-stream;base64,{base64.b64encode(doc_data).decode()}" #para tomar el archivo local sin necesidad de url

        else:
            doc_url = input("URL del archivo: ")
        
        headers_post = {'content-type': 'application/x-www-form-urlencoded'}
        
        filename = input("Nombre del archivo (con extensión): ")

        caption = input("Pie de documento (opcional): ")
        
        payload_doc = f"token={token}&to={to}&filename={filename}&document={doc_url}&caption={caption}"
        
        payload_doc = payload_doc.encode('utf8')
        
        response = requests.request("POST", url_doc, data=payload_doc, headers=headers_post)

        print(response.text)

    
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


#El programa empieza aquí

instance = input("Instancia: ")
token = input("Token: ")
to = input("Número de teléfono (ej. +1...): ")

url = f"https://api.ultramsg.com/{instance}/messages/chat"

headers_post = {'content-type': 'application/x-www-form-urlencoded'}

sent(instance, token, to)


conn.close()