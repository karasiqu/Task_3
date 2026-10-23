import random
import string
import requests
from urls import API_REGISTER, API_USER


def generate_random_email():
    random_str = "".join(random.choices(string.ascii_lowercase, k=8))
    return f"test_{random_str}@yandex.ru"


def register_user(email, password, name):
    payload = {"email": email, "password": password, "name": name}
    return requests.post(API_REGISTER, json=payload, timeout=15)


def delete_user(token):
    return requests.delete(API_USER, headers={"Authorization": token}, timeout=15)
