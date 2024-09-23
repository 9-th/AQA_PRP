import requests
import pytest
import os
from dotenv import load_dotenv

host = "https://api.pokemonbattle.ru"
TOKEN = os.getenv("TOKEN")
TRAINER_ID = 6812


def test_status_code():
    response= requests.get(host + "/v2/trainers")
    assert response.status_code == 200

def test_name():
    response = requests.get(host + "/v2/trainers", params={"trainer_id": TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == "9iNtH"