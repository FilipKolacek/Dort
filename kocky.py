
while True:
    vaha = float(input("Zadej váhu kočky: "))
    krmivo = vaha * 30 + 70
    print(f"Kočka by měla dostat {krmivo} g krmiva denně.")
    dalsi = input("Chceš zadat další kočku? (ano/ne): ")
    if dalsi == "ne":
        break