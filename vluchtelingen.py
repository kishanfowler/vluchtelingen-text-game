def vraag1():
    antwoord = input("er is oorlog. Vlucht je? ja of nee? " )
    if antwoord == "ja":
        vraag2()
    elif antwoord == "nee":
        print("je vlucht niet en gaat dood. DEAD ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")

def vraag2():
    antwoord2 = input("je vlucht uit je huis en laat je ouders achter, waar ga je naartoe? a = een dichtbij gelegen stad b = een taliban stad c = naar Pakistan ")
    if antwoord2 == "a":
        vraag3()
    elif antwoord2 == "b":
        ("je gaat naar een stad die door de taliban wordt beheerst. Ze zien dat je alleen bent. ze vragen of jij je wilt aansluiten bij de taliban")

def vraag3():
    antwoord3 = input("je stapt de auto in en rijd naar een stad waar de taliban nog niet is. daar wordt het nu ook gevaarlijk. Wat doe je nu? A = naar europa rijden B = blijven C= naar Pakistan ")
    if antwoord3 == "a":
        vraag4()

def vraag4():
    antwoord4 = input("je komt aan in europa. stad wat wil je doen? a = je vlucht naar nederland b = je blijft of c = je sluit je aan bij de taliban ")
    if antwoord4 == "a":
        print("je bent veilig naar nederland gegaan. GOOD ENDING")

def vraag5():
    antwoord5 = input("je gaat naar een stad die door de taliban wordt beheerst. Ze zien dat je alleen bent. ze vragen of jij je wilt aansluiten bij de taliban. a = aansluiten b = niet aansluiten ")
    if antwoord5 == "a":
        print("je sluit je aan bij de taliban. BAD ENDING")
    elif antwoord5 == "b":
        vraag6()

def vraag6():
    antwoord6 = input("je zegt dat je niet bij ze aansluit, ren je weg of ren je een huis in? a = wegrennen b= huis in rennen ")
    if antwoord6 == "a":
        print("je rent weg van ze en wordt neergeschoten. DEAD ENDING")





vraag1()
