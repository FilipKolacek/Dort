with open ("textkparsovani.txt","r", encoding="utf-8") as soubor:
    text = soubor.read()
    print(text)


staryZnak1 = "("
novyZnak1 = ""
staryZnak2 = ")"
novyZnak2 = ""

for znak in text:
    if znak == staryZnak1:
        text = text.replace(staryZnak1, novyZnak1, 1)
    elif znak == staryZnak2:
        text = text.replace(staryZnak2, novyZnak2, 1)

print(text)

with open("hotovo.txt", "w", encoding="utf-8") as soubor:
    soubor.write(text)