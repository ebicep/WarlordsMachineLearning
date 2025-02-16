from enum import Enum

from pandas import DataFrame


def drop_correlated(df: DataFrame) -> DataFrame:
    df = df.copy()
    df.drop(
        columns=[
            "kills_average", "kills_average", "assists_average", "deaths_average", "damage_average", "healing_average", "absorbed_average", "damage_on_carrier_average",
            "healing_on_carrier_average", "flag_returns_average", "blocks_travelled_average"
        ],
        inplace=True
    )
    return df


def average_respawn_time(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["average_respawn_time"] = df["total_deaths_average"] / df["seconds_in_respawn_average"]
    df.drop(
        columns=["total_deaths_average", "seconds_in_respawn_average"],
        inplace=True
    )
    return df


def average_dhp(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["average_dhp"] = (df["total_damage_average"] + df["total_absorbed_average"] + df["total_healing_average"]) / 3
    df.drop(
        columns=["total_damage_average", "total_absorbed_average", "total_healing_average"], inplace=True
    )
    return df


def average_respawn_time_kda(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["average_respawn_time"] = df["total_deaths_average"] / df["seconds_in_respawn_average"]
    df["kda"] = (df["total_kills_average"] + df["total_assists_average"]) / df["total_deaths_average"]
    df.drop(
        columns=["seconds_in_respawn_average", "total_kills_average", "total_assists_average", "total_deaths_average"], inplace=True
    )
    return df


def kda(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["kda"] = (df["total_kills_average"] + df["total_assists_average"]) / df["total_deaths_average"]
    df.drop(
        columns=["total_kills_average", "total_assists_average", "total_deaths_average"], inplace=True
    )
    return df


def ka(df: DataFrame) -> DataFrame:
    df = df.copy()
    df["ka"] = df["total_kills_average"] + df["total_assists_average"]
    df.drop(
        columns=["total_kills_average", "total_assists_average"], inplace=True
    )
    return df


class DataFrameOperation(Enum):
    DROP_CORRELATED = drop_correlated
    AVERAGE_RESPAWN_TIME = average_respawn_time
    AVERAGE_DHP = average_dhp
    AVERAGE_RESPAWN_TIME_KDA = average_respawn_time_kda
    KDA = kda
    KA = ka
