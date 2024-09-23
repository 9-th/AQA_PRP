import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Загрузка переменных из файла .env

host = "https://api.pokemonbattle.ru"
TOKEN = os.getenv("TOKEN")

def post_pokemons():
    payload = {
        "name": "Raven",
        "photo_id": 823
    }

    headers = {
        "Content-Type": "application/json",
        "trainer_token": TOKEN
    }

    response = requests.post(host + "/v2/pokemons", json=payload, headers=headers)
    pokemon_id = response.json()["id"]
    print(f"{response.status_code}\n {response.text}\n pokemon_id: {pokemon_id}")

    return pokemon_id


def put_pokemons(pokemon_id):
    payload = {
        "pokemon_id": f"{pokemon_id}",
        "name": "RAVEN",
        "photo_id": 823
    }

    headers = {
        "Content-Type": "application/json",
        "trainer_token": TOKEN
    }

    response = requests.put(host + f"/v2/pokemons", json=payload, headers=headers)
    pokemon_id = response.json()["id"]
    print(f"{response.status_code}\n {response.text}")

    return pokemon_id


def post_trainers_add_pokeball(pokemon_id):
    payload = {
        "pokemon_id": f"{pokemon_id}"
    }

    headers = {
        "Content-Type": "application/json",
        "trainer_token": TOKEN
    }

    response = requests.post(host + "/v2/trainers/add_pokeball", json=payload, headers=headers)
    print(f"{response.status_code}\n {response.text}\n")


# Основной блок: вызов функций с использованием одного pokemon_id
pokemon_id = post_pokemons()
put_pokemons(pokemon_id)
post_trainers_add_pokeball(pokemon_id)
