#Reviewing ultramsg
import requests
import json

######################
#  ENVÍO DE MENSAJES #
######################

url = "https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

payload = "token={TOKEN}&to=&body=WhatsApp API on UltraMsg.com works good"

# Siempre encode con base64 o utf-8

payload = payload.encode('utf8').decode('iso-8859-1') 

headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# CON JSON

payload = json.dumps({
    "token": "{TOKEN}",
    "to": "",
    "body": "Un texto de ejemplo para el chat"
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)