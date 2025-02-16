# Goal

- Find how each feature affects the win rate of a game.

# Data

- 1818 Comp Games that took place on the Warlords 2 server.

# Features

- seconds_in_combat
- seconds_in_respawn
- flag_captures
- flag_returns
- total_damage_on_carrier
- total_healing_on_carrier
- damage_on_carrier
- healing_on_carrier
- total_kills
- total_assists
- total_deaths
- total_damage
- total_healing
- total_absorbed
- kills
- assists
- deaths
- damage
- healing
- absorbed

# Transformed Features

- average_respawn_time
- average_dhp

# Target

- Win Rate

# Results

- Mean Squared Error (MSE): 0.0184
- R-squared (R2): -0.1013


- total_assists_average: 0.0474
- total_healing_on_carrier_average: -0.0355
- total_deaths_average: -0.0328
- total_kills_average: 0.0295
- total_damage_on_carrier_average: 0.0290
- total_damage_average: -0.0286
- total_absorbed_average: -0.0238
- seconds_in_combat_average: 0.0181
- flag_captures_average: 0.0138
- total_healing_average: -0.0006
- average_respawn_time: 0.0004

