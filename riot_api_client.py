# src/riot_api_client.py
import os
import requests
from dotenv import load_dotenv

# Load variables from .env and override anything set globally
load_dotenv(override=True)

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

def get_match_details(match_id: str) -> dict:
    url = f"{BASE_URL}/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": API_KEY}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()
    
def extract_player_from_match(match_json, puuid):
    """Return only the participant dict for the given puuid."""
    for p in match_json["info"]["participants"]:
        if p["puuid"] == puuid:
            return p
    return None  # should not happen if the match IDs came from this puuid

puuid = get_puuid('brownbuddyguy', '3619')
match_ids = get_match_ids(puuid, count=1)

for mid in match_ids:
    m = get_match_details(mid)
    me = extract_player_from_match(m, puuid)
    # quick sanity check output:
    print(mid, me)