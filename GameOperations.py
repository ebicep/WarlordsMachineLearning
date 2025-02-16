from enum import Enum


class PostOperation(Enum):
    DO_NOTHING = 0
    CONTINUE = 1


def no_mercy(game: dict) -> PostOperation:
    if abs(game["blue_points"] - game["red_points"]) > 550:
        return PostOperation.CONTINUE
    return PostOperation.DO_NOTHING


class GameOperation(Enum):
    NO_MERCY = no_mercy
