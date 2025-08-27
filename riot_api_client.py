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

def get_match_ids(puuid: str, count: int = 100) -> list[str]:
    url = f"{BASE_URL}/lol/match/v5/matches/by-puuid/{puuid}/ids"
    headers = {"X-Riot-Token": API_KEY}
    params = {"count": count}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return(resp.json())

get_match_ids(get_puuid('brownbuddyguy', '3619'))