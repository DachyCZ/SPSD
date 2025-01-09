import random
text = {
    "text01": "Hi there!",
    "text02": "I've generated a random 4-digit number for you.",
    "text03": "Let's play a bulls and cows game.",
    "text04": "Enter a number: ",
    "error": "Invalid input! Enter a 4-digit number with unique digits.",
    "vyhra": "Correct, you've guessed the right number in {typ} guesses!"
}
carky = "\n" + "-" * 50 + "\n"

def ZadaneCisla(num):
    return [int(x) for x in str(num)]
def VsechnaCisla(num):
    cisla2 = ZadaneCisla(num)
    return len(cisla2) == len(set(cisla2))
def VygenerovaneCislo():
    while True:
        cislo = random.randint(1000, 9999)
        if VsechnaCisla(cislo):
            return cislo
def BullsCows(secret, typ):
    bulls = sum(1 for s, g in zip(secret, typ) if s == g)
    cows = sum(1 for g in typ if g in secret) - bulls
    return bulls, cows

# Zacatek hry
print(text["text01"] + carky + text["text02"] + carky + text["text03"] + carky)
skryte_number = ZadaneCisla(VygenerovaneCislo())
typ_pocet = 0
while True:
    try:
        user_input = input(text["text04"])
        if not user_input.isdigit() or len(user_input) != 4 or not VsechnaCisla(int(user_input)):
            print(text["error"])
            continue
        hrace_typ = ZadaneCisla(int(user_input))
        typ_pocet += 1
        bulls, cows = BullsCows(skryte_number, hrace_typ)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        if bulls == 4:
            print(text["vyhra"].format(typ=typ_pocet))
            break
    except ValueError:
        print(text["error"])
