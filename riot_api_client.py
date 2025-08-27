# src/riot_api_client.py
import os
import requests

API_KEY = os.environ["RIOT_API_KEY"]
BASE_URL = "https://americas.api.riotgames.com"  # or the appropriate region


def get_puuid(game_name: str, tag_line: str) -> str:
    url = f"{BASE_URL}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}" # Game name refers to the summoner name
    headers = {"X-Riot-Token": API_KEY}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()["puuid"]

get_puuid('brownbuddyguy', '3619')