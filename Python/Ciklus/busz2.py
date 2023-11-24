# 08:00 => 8*60 = 480
# 18:00 => 18*60 = 1080

for idopont in range(480, 1081, 25):
    ora = idopont // 60
    perc = idopont % 60
    if ora < 10:
        ora = "0" + str(ora)
    if perc < 10:
        perc = "0" + str(perc)
    print(ora, perc, sep=":")
