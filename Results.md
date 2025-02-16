# Normalization More Data

Mean Squared Error (MSE): 0.0323
R-squared (R2): -0.3617

Coefficients:

- seconds_in_combat_average: 0.1071
- seconds_in_respawn_average: 0.0092
- blocks_travelled_average: 0.0956
- flag_captures_average: 0.0184
- flag_returns_average: 0.0877
- total_damage_on_carrier_average: 0.1945
- total_healing_on_carrier_average: -0.0848
- damage_on_carrier_average: -0.1899
- healing_on_carrier_average: 0.0233
- total_kills_average: 0.1187
- total_assists_average: -0.0313
- total_deaths_average: -0.1311
- total_damage_average: -0.1048
- total_healing_average: -0.0113
- total_absorbed_average: -0.0603

Intercept: 0.5194

# Normalization Feature Removal

- Mean Squared Error (MSE): 0.0319
- R-squared (R2): -0.3465

- Coefficients (sorted by absolute value):
    - total_deaths_average: -0.1980
    - seconds_in_combat_average: 0.1296
    - total_kills_average: 0.1279
    - seconds_in_respawn_average: 0.1079
    - blocks_travelled_average: 0.1012
    - total_absorbed_average: -0.0916
    - total_damage_average: -0.0504
    - total_damage_on_carrier_average: 0.0495
    - total_healing_on_carrier_average: -0.0421
    - flag_captures_average: 0.0355
    - total_assists_average: -0.0208
    - total_healing_average: 0.0182
- Intercept: 0.5107

--- 

- Mean Squared Error (MSE): 0.0319
- R-squared (R2): -0.3448
    - Coefficients (sorted by absolute value):
    - total_deaths_average: -0.2503
    - seconds_in_respawn_average: 0.1969
    - total_kills_average: 0.1295
    - total_healing_on_carrier_average: -0.0731
    - total_healing_average: 0.0674
    - total_absorbed_average: -0.0590
    - flag_captures_average: 0.0478
    - seconds_in_combat_average: 0.0391
    - total_damage_average: -0.0270
    - total_assists_average: -0.0163
    - total_damage_on_carrier_average: 0.0153
- Intercept: 0.5143

# Normalization Feature Removal + Transform

Mean Squared Error (MSE): 0.0345
R-squared (R2): -0.4527

Coefficients (sorted by absolute value):

- total_kills_average: 0.1334
- total_healing_on_carrier_average: -0.0769
- total_healing_average: 0.0696
- total_absorbed_average: -0.0562
- total_deaths_average: -0.0556
- flag_captures_average: 0.0493
- seconds_in_combat_average: 0.0380
- total_damage_average: -0.0276
- average_respawn_time: -0.0274
- total_assists_average: -0.0233
- total_damage_on_carrier_average: 0.0146

Intercept: 0.5136

# Normalization More Data Feature Removal + Transform

Mean Squared Error (MSE): 0.0184
R-squared (R2): -0.1013

Coefficients (sorted by absolute value):

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

Intercept: 0.4840

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

# Normalization More Data Feature Removal + Transform + Removed mercies

---

drop_correlated + average_respawn_time:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0109 (±0.0024)
- 5-Fold Cross-Validation R-squared (R2): -0.3578 (±0.3352)

Test Set Performance:

- Mean Squared Error (MSE): 0.0096
- R-squared (R2): -0.0424

- Coefficients (sorted by absolute value):
    - total_kills_average: 0.0334
    - total_damage_average: -0.0209
    - total_healing_average: 0.0200
    - flag_captures_average: 0.0105
    - total_assists_average: 0.0090
    - total_healing_on_carrier_average: 0.0057
    - average_respawn_time: 0.0046
    - total_damage_on_carrier_average: -0.0040
    - seconds_in_combat_average: -0.0024
    - total_absorbed_average: 0.0007
- Intercept: 0.4963

---

drop_correlated + average_respawn_time + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0102 (±0.0020)
- 5-Fold Cross-Validation R-squared (R2): -0.2656 (±0.2328)

Test Set Performance:

- Mean Squared Error (MSE): 0.0089
- R-squared (R2): 0.0287

- Coefficients (sorted by absolute value):
    - average_dhp: 0.0157
    - total_kills_average: 0.0117
    - total_healing_on_carrier_average: 0.0116
    - flag_captures_average: 0.0106
    - total_damage_on_carrier_average: -0.0104
    - seconds_in_combat_average: -0.0047
    - total_assists_average: 0.0014
    - average_respawn_time: -0.0002
- Intercept: 0.4954

---

drop_correlated + average_respawn_time_kda + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0099 (±0.0019)
- 5-Fold Cross-Validation R-squared (R2): -0.2365 (±0.2688)

Test Set Performance:

- Mean Squared Error (MSE): 0.0082
- R-squared (R2): 0.1045

- Coefficients (sorted by absolute value):
    - kda: 0.0133
    - average_dhp: 0.0122
    - flag_captures_average: 0.0102
    - total_healing_on_carrier_average: 0.0075
    - total_damage_on_carrier_average: -0.0073
    - average_respawn_time: -0.0019
    - seconds_in_combat_average: -0.0011
- Intercept: 0.4954

---

drop_correlated + average_respawn_time + average_dhp + ka:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0101 (±0.0021)
- 5-Fold Cross-Validation R-squared (R2): -0.2522 (±0.2486)

Test Set Performance:

- Mean Squared Error (MSE): 0.0089
- R-squared (R2): 0.0335

- Coefficients (sorted by absolute value):
    - average_dhp: 0.0163
    - flag_captures_average: 0.0115
    - ka: 0.0110
    - total_healing_on_carrier_average: 0.0105
    - total_damage_on_carrier_average: -0.0080
    - seconds_in_combat_average: -0.0047
    - average_respawn_time: 0.0011
- Intercept: 0.4952

# Normalization More Data Feature Removal + Transform + Removed mercies + Polynomial Features

---

drop_correlated + average_respawn_time:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.5603 (±0.6473)
- 5-Fold Cross-Validation R-squared (R2): -79.8613 (±108.1811)

Test Set Performance:

- Mean Squared Error (MSE): 0.2539
- R-squared (R2): -26.6440

- Coefficients (sorted by absolute value):
    - seconds_in_combat_average total_healing_average: 0.2834
    - total_damage_average total_healing_average: -0.2274
    - total_damage_average total_absorbed_average: -0.2027
    - total_assists_average total_absorbed_average: 0.1896
    - seconds_in_combat_average total_damage_average: 0.1386
    - total_damage_on_carrier_average total_assists_average: 0.1243
    - total_healing_average: 0.1170
    - seconds_in_combat_average total_kills_average: -0.1153
    - total_damage_on_carrier_average average_respawn_time: 0.1146
    - seconds_in_combat_average^2: -0.1089
    - total_kills_average total_healing_average: 0.1026
    - flag_captures_average total_assists_average: -0.1025
    - total_healing_average^2: -0.1017
    - flag_captures_average total_damage_average: 0.0958
    - total_damage_on_carrier_average total_damage_average: -0.0911
    - total_absorbed_average average_respawn_time: 0.0853
    - total_damage_on_carrier_average total_healing_average: 0.0849
    - total_healing_on_carrier_average total_assists_average: -0.0809
    - total_damage_on_carrier_average total_kills_average: -0.0807
    - seconds_in_combat_average total_assists_average: 0.0797
    - total_kills_average^2: 0.0751
    - flag_captures_average total_damage_on_carrier_average: -0.0730
    - total_kills_average total_absorbed_average: 0.0725
    - total_assists_average total_damage_average: -0.0710
    - seconds_in_combat_average flag_captures_average: 0.0691
    - total_healing_on_carrier_average total_healing_average: -0.0682
    - total_assists_average average_respawn_time: 0.0671
    - flag_captures_average total_absorbed_average: -0.0667
    - total_assists_average^2: 0.0616
    - total_healing_on_carrier_average total_kills_average: 0.0562
    - flag_captures_average average_respawn_time: -0.0559
    - seconds_in_combat_average: -0.0523
    - total_assists_average total_healing_average: 0.0517
    - total_absorbed_average: 0.0394
    - total_kills_average total_assists_average: -0.0388
    - flag_captures_average^2: 0.0384
    - seconds_in_combat_average total_absorbed_average: 0.0350
    - average_respawn_time: 0.0319
    - total_damage_average average_respawn_time: -0.0318
    - total_healing_on_carrier_average total_absorbed_average: 0.0298
    - total_damage_on_carrier_average total_absorbed_average: 0.0286
    - total_absorbed_average^2: -0.0285
    - flag_captures_average total_healing_on_carrier_average: -0.0243
    - total_healing_average total_absorbed_average: -0.0224
    - total_damage_on_carrier_average total_healing_on_carrier_average: 0.0215
    - total_healing_on_carrier_average: 0.0213
    - flag_captures_average: 0.0210
    - total_healing_on_carrier_average average_respawn_time: -0.0189
    - seconds_in_combat_average average_respawn_time: 0.0173
    - total_kills_average average_respawn_time: 0.0166
    - total_healing_on_carrier_average^2: 0.0155
    - average_respawn_time^2: 0.0153
    - flag_captures_average total_healing_average: 0.0142
    - total_assists_average: -0.0127
    - total_damage_average: 0.0125
    - total_damage_average^2: -0.0125
    - total_healing_on_carrier_average total_damage_average: -0.0113
    - seconds_in_combat_average total_damage_on_carrier_average: 0.0093
    - total_kills_average: -0.0087
    - total_healing_average average_respawn_time: 0.0085
    - flag_captures_average total_kills_average: -0.0059
    - total_damage_on_carrier_average^2: -0.0047
    - total_kills_average total_damage_average: -0.0028
    - total_damage_on_carrier_average: 0.0020
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0011
    - 1: 0.0000
- Intercept: 0.4993

---

drop_correlated + average_respawn_time + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0636 (±0.0418)
- 5-Fold Cross-Validation R-squared (R2): -6.1967 (±3.1966)

Test Set Performance:

- Mean Squared Error (MSE): 0.0359
- R-squared (R2): -2.9051

- Coefficients (sorted by absolute value):
    - seconds_in_combat_average average_dhp: 0.1167
    - total_healing_on_carrier_average average_dhp: -0.1148
    - seconds_in_combat_average total_assists_average: 0.0944
    - seconds_in_combat_average total_kills_average: -0.0700
    - total_damage_on_carrier_average total_kills_average: -0.0623
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0548
    - seconds_in_combat_average^2: -0.0537
    - total_kills_average average_dhp: 0.0496
    - total_healing_on_carrier_average total_kills_average: 0.0487
    - average_dhp^2: -0.0473
    - total_kills_average average_respawn_time: 0.0457
    - total_damage_on_carrier_average total_assists_average: 0.0406
    - total_assists_average average_dhp: -0.0371
    - flag_captures_average average_dhp: 0.0310
    - seconds_in_combat_average average_respawn_time: 0.0243
    - total_kills_average total_assists_average: -0.0216
    - total_assists_average: 0.0209
    - average_respawn_time average_dhp: -0.0194
    - total_assists_average average_respawn_time: -0.0148
    - flag_captures_average total_kills_average: -0.0147
    - average_respawn_time: 0.0146
    - flag_captures_average total_damage_on_carrier_average: 0.0133
    - total_kills_average: -0.0123
    - total_damage_on_carrier_average average_dhp: 0.0117
    - total_assists_average^2: 0.0111
    - total_damage_on_carrier_average average_respawn_time: 0.0101
    - flag_captures_average: 0.0099
    - total_healing_on_carrier_average total_assists_average: 0.0098
    - flag_captures_average average_respawn_time: -0.0094
    - flag_captures_average^2: 0.0093
    - total_healing_on_carrier_average^2: 0.0086
    - flag_captures_average total_healing_on_carrier_average: 0.0083
    - total_healing_on_carrier_average average_respawn_time: 0.0075
    - total_damage_on_carrier_average: 0.0073
    - total_damage_on_carrier_average^2: -0.0073
    - seconds_in_combat_average total_damage_on_carrier_average: 0.0072
    - total_healing_on_carrier_average: 0.0063
    - total_kills_average^2: 0.0051
    - average_respawn_time^2: 0.0050
    - total_damage_on_carrier_average total_healing_on_carrier_average: 0.0044
    - seconds_in_combat_average: 0.0043
    - seconds_in_combat_average flag_captures_average: -0.0031
    - flag_captures_average total_assists_average: -0.0018
    - average_dhp: 0.0011
    - 1: 0.0000
- Intercept: 0.4888

---

drop_correlated + average_respawn_time_kda + average_dhp:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0278 (±0.0130)
- 5-Fold Cross-Validation R-squared (R2): -2.6359 (±2.0898)

Test Set Performance:

- Mean Squared Error (MSE): 0.0101
- R-squared (R2): -0.0963

- Coefficients (sorted by absolute value):
    - seconds_in_combat_average average_dhp: 0.0751
    - average_respawn_time kda: 0.0559
    - total_damage_on_carrier_average kda: -0.0481
    - total_healing_on_carrier_average average_dhp: -0.0440
    - average_respawn_time average_dhp: -0.0422
    - total_damage_on_carrier_average average_dhp: 0.0388
    - total_damage_on_carrier_average average_respawn_time: 0.0378
    - seconds_in_combat_average^2: -0.0365
    - total_damage_on_carrier_average total_healing_on_carrier_average: 0.0357
    - total_damage_on_carrier_average^2: -0.0352
    - flag_captures_average kda: -0.0307
    - total_damage_on_carrier_average: 0.0293
    - kda: 0.0263
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0243
    - total_healing_on_carrier_average kda: 0.0227
    - flag_captures_average average_dhp: 0.0220
    - average_respawn_time^2: -0.0214
    - flag_captures_average^2: 0.0194
    - kda average_dhp: -0.0190
    - seconds_in_combat_average average_respawn_time: -0.0190
    - flag_captures_average total_healing_on_carrier_average: -0.0172
    - flag_captures_average average_respawn_time: -0.0163
    - total_healing_on_carrier_average average_respawn_time: -0.0142
    - average_dhp^2: -0.0113
    - total_healing_on_carrier_average^2: 0.0111
    - seconds_in_combat_average kda: -0.0084
    - total_healing_on_carrier_average: -0.0083
    - average_dhp: -0.0073
    - flag_captures_average total_damage_on_carrier_average: 0.0063
    - flag_captures_average: -0.0058
    - seconds_in_combat_average total_damage_on_carrier_average: -0.0050
    - seconds_in_combat_average flag_captures_average: 0.0032
    - average_respawn_time: -0.0025
    - kda^2: 0.0024
    - seconds_in_combat_average: 0.0001
    - 1: -0.0000
- Intercept: 0.5030

---

drop_correlated + average_respawn_time + average_dhp + ka:

- 5-Fold Cross-Validation Mean Squared Error (MSE): 0.0571 (±0.0490)
- 5-Fold Cross-Validation R-squared (R2): -7.1099 (±8.3082)

Test Set Performance:

- Mean Squared Error (MSE): 0.0135
- R-squared (R2): -0.4706

- Coefficients (sorted by absolute value):
    - average_respawn_time ka: 0.0664
    - total_healing_on_carrier_average average_dhp: -0.0586
    - ka: 0.0423
    - total_healing_on_carrier_average: 0.0376
    - average_respawn_time average_dhp: -0.0364
    - seconds_in_combat_average total_healing_on_carrier_average: 0.0344
    - seconds_in_combat_average average_dhp: 0.0314
    - total_damage_on_carrier_average^2: -0.0304
    - total_damage_on_carrier_average ka: -0.0299
    - average_dhp: -0.0285
    - total_healing_on_carrier_average ka: 0.0266
    - total_damage_on_carrier_average total_healing_on_carrier_average: 0.0263
    - total_damage_on_carrier_average average_respawn_time: 0.0221
    - seconds_in_combat_average^2: -0.0183
    - average_respawn_time: 0.0177
    - flag_captures_average average_dhp: 0.0163
    - seconds_in_combat_average total_damage_on_carrier_average: -0.0159
    - ka^2: 0.0141
    - seconds_in_combat_average ka: 0.0105
    - total_damage_on_carrier_average average_dhp: 0.0104
    - flag_captures_average total_healing_on_carrier_average: 0.0082
    - flag_captures_average^2: 0.0063
    - total_healing_on_carrier_average^2: 0.0045
    - seconds_in_combat_average: -0.0040
    - average_dhp ka: -0.0038
    - flag_captures_average total_damage_on_carrier_average: -0.0037
    - average_respawn_time^2: 0.0036
    - total_healing_on_carrier_average average_respawn_time: -0.0033
    - seconds_in_combat_average average_respawn_time: 0.0030
    - total_damage_on_carrier_average: -0.0029
    - flag_captures_average ka: -0.0028
    - flag_captures_average average_respawn_time: -0.0025
    - seconds_in_combat_average flag_captures_average: -0.0015
    - flag_captures_average: -0.0008
    - average_dhp^2: 0.0003
    - 1: 0.0000
- Intercept: 0.4952


