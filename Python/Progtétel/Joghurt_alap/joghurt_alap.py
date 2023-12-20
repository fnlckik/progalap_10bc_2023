napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
epres = [30, 20, 12, 27, 29, 23]
barackos = [18, 25, 19, 22, 21, 12]

n = len(napok)
# F1
print("1. Bevétel epres joghurtokból a hét egyes napjain:")
for i in range(n):
    ar = 189 * epres[i]
    print(f"   - {napok[i]}: {ar} Ft")

# F2
# Megszámolás
db = 0
for i in range(n):
    if epres[i] > barackos[i]:
        db += 1
print("2. Ennyi napon fogyott több epres, mint barackos:", db)

# F3
epresOsszeg = 0
osszeg = 0
for i in range(n):
    epresOsszeg += epres[i]
    osszeg += epres[i] + barackos[i]
szazalek = epresOsszeg / osszeg * 100
print(f"3. A vásárolt joghurtok {round(szazalek, 2)}%-a volt epres!")

# F4
mine = abs(epres[0] - barackos[0])
for i in range(1, n):
    elteres = abs(epres[i] - barackos[i])
    if elteres < mine:
        mine = elteres
print("4. Legkisebb eltérés az epres és barackos joghurtok mennyiségében:", mine)
