from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class UUID:
    base64: str
    subType: str


@dataclass
class PlayerStats:
    uuid: UUID
    name: str
    spec: str
    skill_boost: str
    seconds_in_combat: int
    seconds_in_respawn: int
    flag_captures: int
    flag_returns: int
    total_damage_on_carrier: int
    total_healing_on_carrier: int
    damage_on_carrier: List[int]
    healing_on_carrier: List[int]
    blocks_travelled: int
    x_locations: str
    z_locations: str
    total_kills: int
    total_assists: int
    total_deaths: int
    total_damage: int
    total_healing: int
    total_absorbed: int
    kills: List[int]
    assists: List[int]
    deaths: List[int]
    damage: List[int]
    healing: List[int]
    absorbed: List[int]
    experience_earned_spec: int
    experience_earned_universal: int


@dataclass
class Players:
    RED: List[PlayerStats]
    BLUE: List[PlayerStats]


@dataclass
class GameDetails:
    _id: Dict[str, str]
    time_left: int
    winner: str
    blue_points: int
    red_points: int
    players: Players
    exact_date: Dict[str, str]
    date: str
    map: str
    game_mode: str
    game_addons: List[str]
    counted: bool
    _class: str


@dataclass
class Player:
    uuid: UUID
    name: str
    plays: int = 0
    wins: int = 0
    spec: List[str] = field(default_factory=list)
    skill_boost: List[str] = field(default_factory=list)

    seconds_in_combat: List[int] = field(default_factory=list)
    seconds_in_respawn: List[int] = field(default_factory=list)
    blocks_travelled: List[int] = field(default_factory=list)

    flag_captures: List[int] = field(default_factory=list)
    flag_returns: List[int] = field(default_factory=list)

    total_damage_on_carrier: List[int] = field(default_factory=list)
    total_healing_on_carrier: List[int] = field(default_factory=list)

    damage_on_carrier: List[List[int]] = field(default_factory=list)
    healing_on_carrier: List[List[int]] = field(default_factory=list)

    total_kills: List[int] = field(default_factory=list)
    total_assists: List[int] = field(default_factory=list)
    total_deaths: List[int] = field(default_factory=list)
    total_damage: List[int] = field(default_factory=list)
    total_healing: List[int] = field(default_factory=list)
    total_absorbed: List[int] = field(default_factory=list)

    kills: List[List[int]] = field(default_factory=list)
    assists: List[List[int]] = field(default_factory=list)
    deaths: List[List[int]] = field(default_factory=list)
    damage: List[List[int]] = field(default_factory=list)
    healing: List[List[int]] = field(default_factory=list)
    absorbed: List[List[int]] = field(default_factory=list)

    def add_game_stats(self, stats: Dict, winner: bool):

        def extract_value(value):
            """Extract value from {$numberLong: "value"} format or return the value directly."""
            if isinstance(value, dict) and "$numberLong" in value:
                return int(value["$numberLong"])
            return value

        def extract_list(data):
            """Extract list of values from a list of {$numberLong: "value"} dictionaries or return the list directly."""
            if isinstance(data, list):
                return [extract_value(item) for item in data]
            return data

        self.plays += 1
        if winner:
            self.wins += 1

        for attr_name, value in stats.items():
            if attr_name in ["uuid", "name", "spec", "skill_boost"]:
                continue  # Skip non-stat attributes

            if not hasattr(self, attr_name):
                continue  # Skip if the attribute does not exist in the class

            attr_value = getattr(self, attr_name)

            # Handle single integer values
            if isinstance(value, (int, dict)):
                extracted_value = extract_value(value)
                if isinstance(extracted_value, int):
                    attr_value.append(extracted_value)
                else:
                    raise TypeError(f"{attr_name} must be an integer, got {type(extracted_value)}")

            # Handle flat lists
            elif isinstance(value, list) and not any(isinstance(item, list) for item in value):
                extracted_list = extract_list(value)
                if all(isinstance(item, int) for item in extracted_list):
                    attr_value.extend(extracted_list)
                else:
                    raise TypeError(f"{attr_name} must be a list of integers, got {type(extracted_list)}")

            # Handle nested lists
            elif isinstance(value, list) and any(isinstance(item, list) for item in value):
                extracted_list = extract_list(value)
                if all(isinstance(item, list) for item in extracted_list):
                    attr_value.extend(extracted_list)
                else:
                    raise TypeError(f"{attr_name} must be a list of lists of integers, got {type(extracted_list)}")

            else:
                raise TypeError(f"{attr_name} has an unsupported type: {type(value)}")

    def get_player_stats(self):
        """Returns a dictionary of statistics for the player."""
        stats = {}
        for attr_name, attr_value in self.__dict__.items():
            if attr_name in ["uuid", "name", "spec", "skill_boost"]:
                continue

            if isinstance(attr_value, list):
                if all(isinstance(item, list) for item in attr_value):
                    # Handle nested lists
                    flat_list = [item for sublist in attr_value for item in sublist]
                    total = sum(flat_list)
                    average = total / len(flat_list) if flat_list else 0
                else:
                    # Handle flat lists
                    total = sum(attr_value)
                    average = total / len(attr_value) if attr_value else 0

                # stats[f"{attr_name}_total"] = total
                stats[f"{attr_name}_average"] = average
            else:
                stats[attr_name] = attr_value

        return stats


@dataclass
class GamePlayer:
    # spec: str
    # skill_boost: str
    seconds_in_combat: int
    seconds_in_respawn: int
    flag_captures: int
    flag_returns: int
    total_damage_on_carrier: int
    total_healing_on_carrier: int
    damage_on_carrier: List[int]
    healing_on_carrier: List[int]
    blocks_travelled: int
    total_kills: int
    total_assists: int
    total_deaths: int
    total_damage: int
    total_healing: int
    total_absorbed: int
    kills: List[int]
    assists: List[int]
    deaths: List[int]
    damage: List[int]
    healing: List[int]
    absorbed: List[int]
