bolha = int(input("Bolha: "))

print(bolha, end=" -> ")
while bolha != 0:
    bolha *= -1
    maradek = bolha % 10
    if maradek == 0:
        maradek = 10
    
    if bolha < 0:
        bolha += maradek
    elif bolha > 0:
        bolha -= maradek
        
    if bolha != 0:
        print(bolha, end=" -> ")
    else:
        print(bolha)
        