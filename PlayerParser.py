import json
from typing import Dict, List

from Classes import Player, UUID, PlayerStats


def parse_players(json_file_paths: List[str]) -> Dict[str, Player]:
    unique_games: Dict[str, Dict] = {}

    for json_file_path in json_file_paths:
        with open(json_file_path, 'r') as file:
            games: List[Dict] = json.load(file)

        for game in games:
            exact_date = game["exact_date"]["$date"]
            if isinstance(exact_date, dict):
                exact_date = exact_date["$numberLong"]

            if exact_date not in unique_games:
                unique_games[exact_date] = game

    print("Unique games: ", len(unique_games))

    players: Dict[str, Player] = {}

    valid_games = 0

    for game in unique_games.values():
        if not "winner" in game or not "counted" in game or "game_mode" not in game:
            continue
        if not game["counted"] or game["game_mode"] != "CAPTURE_THE_FLAG":
            continue
        if abs(game["blue_points"] - game["red_points"]) > 550:  # TODO feature flags
            continue

        valid_game = True

        for team in ["RED", "BLUE"]:
            # Normalize the team key to uppercase for case-insensitive lookup
            team_key = next((key for key in game["players"] if key.upper() == team.upper()), None)

            if not team_key:  # If the team key doesn't exist in any case
                valid_game = False
                break

            for player_stats in game["players"][team_key]:
                # Normalize the UUID format
                if isinstance(player_stats["uuid"], str):
                    # If UUID is a string, convert it to the $binary format
                    uuid_data = {
                        "$binary": {
                            "base64": player_stats["uuid"],
                            "subType": "04"  # Assuming subType is always "04" for UUIDs
                        }
                    }
                else:
                    # If UUID is already in the $binary format, use it as-is
                    uuid_data = player_stats["uuid"]

                uuid = uuid_data["$binary"]["base64"]

                if uuid not in players:
                    players[uuid] = Player(
                        uuid=UUID(
                            base64=uuid_data["$binary"]["base64"],
                            subType=uuid_data["$binary"]["subType"]
                        ),
                        name=player_stats["name"]
                    )

                # Normalize the winner team for case-insensitive comparison
                winner_team = game["winner"].upper()
                players[uuid].add_game_stats(player_stats, winner_team == team.upper())

        if valid_game:
            valid_games += 1

    print("Valid games: ", valid_games)

    return players


def parse_game_players(json_file_paths: List[str]) -> Dict[int, List[PlayerStats]]:
    unique_games: Dict[str, Dict] = {}

    for json_file_path in json_file_paths:
        with open(json_file_path, 'r') as file:
            games: List[Dict] = json.load(file)

        for game in games:
            exact_date = game["exact_date"]["$date"]
            if exact_date not in unique_games:
                unique_games[exact_date] = game

    players: Dict[int, List[PlayerStats]] = {
        1: [],
        0: []
    }

    for game in unique_games.values():
        if not "winner" in game or not "counted" in game:
            continue
        if not game["counted"]:
            continue

        winner = game["winner"]
        for team in ["RED", "BLUE"]:
            for player_stats in game["players"][team]:
                if winner == team:
                    players[1].append(player_stats)
                else:
                    players[0].append(player_stats)
    return players
