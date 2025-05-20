print("Ahoj! Jak se jmenuješ?")
jmeno = input()
 
print("Kolik vrstev má mít tvůj dort?")
vrstvy = int(input())
 
print("Kolik různých příchutí chceš použít?")
pocet_prichuti = int(input())
 
prichute = []
i = 0
while i < pocet_prichuti:
    print("Zadej příchuť číslo", i + 1)
    p = input()
    prichute.append(p)
    i = i + 1

i = 0
while i < vrstvy:
    print("Vrstva", i + 1, ":", prichute[i % pocet_prichuti])
    i = i + 1
 

print(jmeno, "vytvořil dort s", vrstvy, "vrstvami a příchutěmi:", ", ".join(prichute))
 
print("Chceš dort ozdobit? (napiš ozdoby, odděluj čárkami)")
ozdoby = input()
print("Tvůj dort je ozdobený:", ozdoby)