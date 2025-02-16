---

drop_correlated + average_respawn_time:
- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0116 (±0.0039)
- 5-Fold Cross-Validation R-squared (R2): -0.0421 (±0.1936)

Test Set Performance:
- Mean Squared Error (MSE): 0.0191
- R-squared (R2): -0.1425

- Coefficients (sorted by absolute value):
  - total_assists_average: 0.0355
  - total_absorbed_average: -0.0326
  - total_kills_average: 0.0320
  - total_healing_on_carrier_average: -0.0288
  - total_damage_on_carrier_average: 0.0268
  - total_damage_average: -0.0266
  - flag_captures_average: 0.0238
  - seconds_in_combat_average: 0.0149
  - total_healing_average: 0.0064
  - average_respawn_time: 0.0021
- Intercept: 0.4854

---

drop_correlated + average_respawn_time + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0119 (±0.0036)
- 5-Fold Cross-Validation R-squared (R2): -0.0738 (±0.2305)

Test Set Performance:

- Mean Squared Error (MSE): 0.0185
- R-squared (R2): -0.1037

- Coefficients (sorted by absolute value):
    - total_damage_on_carrier_average: 0.0287
    - total_assists_average: 0.0231
    - total_healing_on_carrier_average: -0.0175
    - flag_captures_average: 0.0125
    - total_kills_average: 0.0071
    - average_dhp: 0.0069
    - average_respawn_time: -0.0025
    - seconds_in_combat_average: 0.0003
- Intercept: 0.4854

---

drop_correlated + average_respawn_time_kda + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0106 (±0.0047)
- 5-Fold Cross-Validation R-squared (R2): 0.0748 (±0.2100)

Test Set Performance:

- Mean Squared Error (MSE): 0.0198
- R-squared (R2): -0.1850

- Coefficients (sorted by absolute value):
    - kda: 0.0477
    - total_healing_on_carrier_average: -0.0354
    - total_damage_on_carrier_average: 0.0320
    - seconds_in_combat_average: 0.0059
    - average_respawn_time: -0.0034
    - flag_captures_average: 0.0029
    - average_dhp: 0.0007
- Intercept: 0.4830

---

drop_correlated + average_respawn_time + average_dhp + ka:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0119 (±0.0036)
- 5-Fold Cross-Validation R-squared (R2): -0.0765 (±0.2319)

Test Set Performance:

- Mean Squared Error (MSE): 0.0184
- R-squared (R2): -0.0966

- Coefficients (sorted by absolute value):
    - ka: 0.0280
    - total_damage_on_carrier_average: 0.0278
    - total_healing_on_carrier_average: -0.0173
    - flag_captures_average: 0.0122
    - average_dhp: 0.0064
    - average_respawn_time: -0.0025
    - seconds_in_combat_average: 0.0006
- Intercept: 0.4855

---

drop_correlated + average_respawn_time:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.1821 (±0.1647)
- 5-Fold Cross-Validation R-squared (R2): -17.7129 (±17.3977)

Test Set Performance:

- Mean Squared Error (MSE): 0.0899
- R-squared (R2): -4.3652

- Coefficients (sorted by absolute value):
    - total_healing_on_carrier_average total_healing_average: -0.1314
    - total_damage_average average_respawn_time: -0.1164
    - total_damage_on_carrier_average total_healing_average: 0.1125
    - total_damage_on_carrier_average total_healing_on_carrier_average: -0.1110
    - flag_captures_average total_damage_average: 0.1039
    - total_damage_on_carrier_average total_damage_average: -0.1036
    - seconds_in_combat_average total_healing_on_carrier_average: 0.1031
    - total_damage_on_carrier_average total_kills_average: 0.0930
    - flag_captures_average total_assists_average: -0.0860
    - flag_captures_average total_kills_average: -0.0834
    - total_healing_on_carrier_average total_absorbed_average: -0.0826
    - total_kills_average average_respawn_time: 0.0822
    - total_healing_on_carrier_average total_damage_average: 0.0794
    - total_damage_average^2: 0.0763
    - flag_captures_average total_healing_on_carrier_average: 0.0757
    - flag_captures_average total_damage_on_carrier_average: -0.0698
    - total_damage_average total_absorbed_average: -0.0687
    - total_damage_on_carrier_average: 0.0591
    - total_kills_average total_absorbed_average: 0.0551
    - total_kills_average total_assists_average: 0.0503
    - total_assists_average total_healing_average: -0.0480
    - total_kills_average total_damage_average: -0.0454
    - total_kills_average total_healing_average: -0.0438
    - flag_captures_average total_healing_average: -0.0421
    - seconds_in_combat_average total_absorbed_average: 0.0413
    - total_healing_on_carrier_average average_respawn_time: -0.0404
    - seconds_in_combat_average total_damage_on_carrier_average: -0.0382
    - total_damage_on_carrier_average total_absorbed_average: 0.0371
    - total_absorbed_average: 0.0365
    - seconds_in_combat_average total_assists_average: 0.0364
    - total_absorbed_average average_respawn_time: -0.0349
    - total_damage_average: -0.0337
    - seconds_in_combat_average total_kills_average: -0.0307
    - total_healing_average: 0.0304
    - total_damage_on_carrier_average average_respawn_time: 0.0295
    - total_healing_on_carrier_average^2: 0.0287
    - total_healing_average total_absorbed_average: 0.0269
    - total_assists_average^2: -0.0263
    - total_healing_on_carrier_average: -0.0262
    - total_assists_average total_damage_average: -0.0259
    - flag_captures_average total_absorbed_average: 0.0258
    - seconds_in_combat_average average_respawn_time: 0.0248
    - total_damage_on_carrier_average^2: 0.0228
    - total_damage_on_carrier_average total_assists_average: -0.0207
    - total_kills_average^2: -0.0191
    - total_healing_on_carrier_average total_kills_average: -0.0189
    - seconds_in_combat_average total_damage_average: 0.0183
    - total_healing_average average_respawn_time: 0.0183
    - seconds_in_combat_average: 0.0181
    - total_assists_average: 0.0162
    - total_healing_average^2: -0.0157
    - total_healing_on_carrier_average total_assists_average: -0.0151
    - total_assists_average total_absorbed_average: 0.0136
    - average_respawn_time^2: 0.0134
    - flag_captures_average average_respawn_time: -0.0121
    - seconds_in_combat_average^2: -0.0098
    - seconds_in_combat_average flag_captures_average: 0.0090
    - seconds_in_combat_average total_healing_average: 0.0085
    - average_respawn_time: 0.0081
    - total_damage_average total_healing_average: 0.0070
    - flag_captures_average: 0.0034
    - total_assists_average average_respawn_time: 0.0026
    - total_kills_average: 0.0026
    - total_absorbed_average^2: -0.0019
    - flag_captures_average^2: 0.0006
    - 1: 0.0000
- Intercept: 0.4753

---

drop_correlated + average_respawn_time + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0534 (±0.0565)
- 5-Fold Cross-Validation R-squared (R2): -4.2775 (±5.9508)

Test Set Performance:

- Mean Squared Error (MSE): 0.0319
- R-squared (R2): -0.9019

- Coefficients (sorted by absolute value):
    - seconds_in_combat_average average_dhp: 0.0860
    - total_healing_on_carrier_average total_assists_average: 0.0547
    - total_healing_on_carrier_average average_dhp: -0.0540
    - flag_captures_average total_healing_on_carrier_average: 0.0528
    - total_damage_on_carrier_average average_dhp: 0.0461
    - total_damage_on_carrier_average: 0.0439
    - seconds_in_combat_average total_kills_average: -0.0437
    - total_damage_on_carrier_average total_assists_average: -0.0433
    - total_healing_on_carrier_average: -0.0422
    - flag_captures_average total_assists_average: -0.0399
    - seconds_in_combat_average^2: -0.0398
    - total_kills_average total_assists_average: 0.0382
    - seconds_in_combat_average average_respawn_time: -0.0373
    - seconds_in_combat_average: 0.0326
    - seconds_in_combat_average total_damage_on_carrier_average: 0.0275
    - average_dhp^2: -0.0254
    - flag_captures_average total_kills_average: 0.0234
    - flag_captures_average total_damage_on_carrier_average: -0.0195
    - total_healing_on_carrier_average total_kills_average: -0.0185
    - seconds_in_combat_average total_assists_average: 0.0168
    - total_damage_on_carrier_average^2: -0.0164
    - total_assists_average average_respawn_time: 0.0161
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0160
    - total_kills_average^2: -0.0153
    - total_assists_average: 0.0142
    - average_respawn_time average_dhp: -0.0141
    - total_assists_average^2: -0.0141
    - total_healing_on_carrier_average^2: 0.0134
    - flag_captures_average: -0.0108
    - flag_captures_average^2: 0.0103
    - flag_captures_average average_respawn_time: -0.0088
    - total_assists_average average_dhp: 0.0083
    - total_damage_on_carrier_average average_respawn_time: 0.0081
    - total_kills_average average_dhp: -0.0065
    - total_damage_on_carrier_average total_kills_average: -0.0051
    - flag_captures_average average_dhp: 0.0050
    - average_respawn_time^2: -0.0046
    - seconds_in_combat_average flag_captures_average: 0.0042
    - average_respawn_time: -0.0033
    - total_kills_average average_respawn_time: 0.0030
    - average_dhp: -0.0023
    - total_kills_average: 0.0013
    - total_damage_on_carrier_average total_healing_on_carrier_average: -0.0009
    - total_healing_on_carrier_average average_respawn_time: 0.0007
    - 1: 0.0000
- Intercept: 0.4897

---

drop_correlated + average_respawn_time_kda + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0336 (±0.0162)
- 5-Fold Cross-Validation R-squared (R2): -2.3511 (±1.9216)

Test Set Performance:

- Mean Squared Error (MSE): 0.0243
- R-squared (R2): -0.4501

- Coefficients (sorted by absolute value):
    - seconds_in_combat_average average_dhp: 0.0856
    - flag_captures_average kda: -0.0557
    - total_healing_on_carrier_average average_dhp: -0.0538
    - seconds_in_combat_average^2: -0.0513
    - flag_captures_average total_healing_on_carrier_average: 0.0510
    - total_damage_on_carrier_average: 0.0496
    - average_respawn_time average_dhp: -0.0473
    - average_respawn_time kda: 0.0420
    - flag_captures_average^2: 0.0378
    - seconds_in_combat_average total_damage_on_carrier_average: 0.0356
    - flag_captures_average average_respawn_time: -0.0339
    - flag_captures_average average_dhp: 0.0300
    - total_healing_on_carrier_average kda: 0.0296
    - average_dhp^2: -0.0281
    - total_healing_on_carrier_average: -0.0273
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0254
    - total_damage_on_carrier_average average_respawn_time: 0.0252
    - total_damage_on_carrier_average total_healing_on_carrier_average: 0.0249
    - seconds_in_combat_average flag_captures_average: -0.0205
    - kda average_dhp: 0.0201
    - seconds_in_combat_average kda: -0.0194
    - flag_captures_average total_damage_on_carrier_average: -0.0189
    - total_damage_on_carrier_average^2: -0.0188
    - seconds_in_combat_average average_respawn_time: -0.0168
    - flag_captures_average: -0.0152
    - kda: 0.0138
    - total_damage_on_carrier_average average_dhp: -0.0136
    - seconds_in_combat_average: 0.0113
    - total_healing_on_carrier_average^2: -0.0095
    - average_respawn_time: -0.0093
    - total_damage_on_carrier_average kda: -0.0073
    - average_dhp: 0.0064
    - kda^2: -0.0054
    - total_healing_on_carrier_average average_respawn_time: -0.0049
    - average_respawn_time^2: -0.0008
    - 1: -0.0000
- Intercept: 0.4792

---

drop_correlated + average_respawn_time + average_dhp + ka:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0510 (±0.0581)
- 5-Fold Cross-Validation R-squared (R2): -4.1399 (±6.0918)

Test Set Performance:

- Mean Squared Error (MSE): 0.0229
- R-squared (R2): -0.3678

- Coefficients (sorted by absolute value):
    - total_healing_on_carrier_average average_dhp: -0.0532
    - total_damage_on_carrier_average ka: -0.0487
    - seconds_in_combat_average average_dhp: 0.0454
    - total_healing_on_carrier_average ka: 0.0417
    - flag_captures_average total_healing_on_carrier_average: 0.0401
    - total_damage_on_carrier_average average_dhp: 0.0355
    - flag_captures_average ka: -0.0348
    - total_damage_on_carrier_average: 0.0342
    - average_respawn_time average_dhp: -0.0324
    - total_healing_on_carrier_average: -0.0301
    - seconds_in_combat_average^2: -0.0288
    - seconds_in_combat_average total_damage_on_carrier_average: 0.0256
    - seconds_in_combat_average average_respawn_time: -0.0247
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0241
    - average_respawn_time ka: 0.0237
    - flag_captures_average total_damage_on_carrier_average: -0.0234
    - flag_captures_average average_respawn_time: -0.0204
    - total_damage_on_carrier_average^2: -0.0203
    - seconds_in_combat_average: 0.0172
    - total_healing_on_carrier_average^2: 0.0159
    - average_dhp: 0.0150
    - flag_captures_average average_dhp: 0.0132
    - total_damage_on_carrier_average average_respawn_time: 0.0123
    - flag_captures_average^2: 0.0114
    - average_dhp ka: -0.0094
    - ka^2: 0.0079
    - total_damage_on_carrier_average total_healing_on_carrier_average: -0.0079
    - average_respawn_time: -0.0076
    - average_dhp^2: -0.0063
    - ka: 0.0063
    - average_respawn_time^2: -0.0057
    - flag_captures_average: 0.0011
    - total_healing_on_carrier_average average_respawn_time: 0.0006
    - seconds_in_combat_average ka: -0.0006
    - seconds_in_combat_average flag_captures_average: -0.0000
    - 1: -0.0000
- Intercept: 0.4856

