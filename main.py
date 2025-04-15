import requests

adresa = 'https://discord.com/api/webhooks/1361603716519690240/8hPuNNcvwmr2KfBa093uCFXqOUzDHuroZvV6WkQAbhpNmcuQ9yg1Yf0_odH2-ODW2fal'

text = {
    "content": "Ahoj z pythonu"
}

response = requests.post(adresa, json=text)