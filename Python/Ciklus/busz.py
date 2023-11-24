ora = 8
perc = 0

print(f"0{ora}:0{perc}")
while ora < 18:
    perc += 25
    if perc >= 60:
        ora += 1
        perc -= 60
    if perc < 10 and ora < 10:
        print(f"0{ora}:0{perc}")
    elif perc < 10:
        print(f"{ora}:0{perc}")
    elif ora < 10:
        print(f"0{ora}:{perc}")
    else:
        print(f"{ora}:{perc}")
        
        
    
        
    