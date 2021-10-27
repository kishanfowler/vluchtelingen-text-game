def vraag1():
    antwoord = input("er is oorlog. Vlucht je? ja of nee? " )
    if antwoord == "ja":
        vraag2()
    elif antwoord == "nee":
        print("je vlucht niet en gaat dood. DEAD ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag1()

def vraag2():
    antwoord2 = input("je vlucht uit je huis en laat je ouders achter, waar ga je naartoe? \n a = een dichtbij gelegen stad \n b = een taliban stad \n c = naar Pakistan ")
    if antwoord2 == "a":
        vraag3()
    elif antwoord2 == "b":
        vraag5()
    elif antwoord2 == "c":
        print("je gaat naar pakistan maar wordt weer uitgeleverd aan de taliban. PRISON ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag2()

def vraag3():
    antwoord3 = input("je stapt de auto in en rijd naar een stad waar de taliban nog niet is. daar wordt het nu ook gevaarlijk. Wat doe je nu? \n a = naar europa rijden \n b = blijven \n c = naar Pakistan ")
    if antwoord3 == "a":
        vraag4()
    elif antwoord3 == "b":
        vraag15()
    elif antwoord3 == "c":
        print("je gaat naar pakistan maar wordt weer uitgeleverd aan de taliban. PRISON ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag3()

def vraag4():
    antwoord4 = input("je komt aan in europa. wat wil je doen? \n a = je vlucht naar nederland \n b = je gaat naar belgië \n c = je gaat naar duitsland ")
    if antwoord4 == "a":
        vraag10()
    if antwoord4 == "b":
        vraag13()
    if antwoord4 == "c":
        vraag14()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag4()

def vraag5():
    antwoord5 = input("je gaat naar een stad die door de taliban wordt beheerst. Ze zien dat je alleen bent. ze vragen of jij je wilt aansluiten bij de taliban. \n a = aansluiten \n b = niet aansluiten ")
    if antwoord5 == "a":
        print("je sluit je aan bij de taliban. BAD ENDING")
    elif antwoord5 == "b":
        vraag6()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag5()

def vraag6():
    antwoord6 = input("je zegt dat je niet bij ze aansluit, ren je weg of ren je een huis in? \n a = wegrennen \n b= huis in rennen ")
    if antwoord6 == "a":
        print("je rent weg van ze en wordt neergeschoten. DEAD ENDING")
    elif antwoord6 == "b":
        vraag7()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag6()

def vraag7():
    antwoord7 = input("je rent een huis in en de familie daar schrikt ren je het huis uit of blijf je daar schuilen? \n a = wegrennen \n b = schuilen ")
    if antwoord7 == "a":
        vraag8()
    elif antwoord7 == "b":
        vraag9()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag7()

def vraag8():
    antwoord8 = input("je rent weg en word niet gezien door de taliban. vlucht je nu naar het buiteland of naar een andere stad? \n a = buitenland \n b = andere stad ")
    if antwoord8 == "a":
        vraag11()
    elif antwoord8 == "b":
        vraag12()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag8()

def vraag9():
    antwoord9 = input("waar wil je schuilen \n a = een kast \n b = onder een bed \n c = de kelder ")
    if antwoord9 == "a":
        print("ze vinden je in de kast en je wordt gevangn genomen. PRISON ENDING")
    elif antwoord9 == "b":
        print("ze vinden je onder het bed en je wordt gevangn genomen. PRISON ENDING")
    elif antwoord9 == "c":
        print("ze vinden je in de kelder en je wordt gevangn genomen. PRISON ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag9()

def vraag10():
    antwoord10 = input("je bent veilig naar nederland gegaan. wil je jouw familie ook naar nederland laten komen? ja of nee ")
    if antwoord10 == "ja":
        print("je familie komt ook naar nederland. GOOD ENDING")
    elif antwoord10 == "nee":
        print("je familie komt niet naar nederland en gaan dood in afghanistan. DEVIL'S ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag10()

def vraag11():
    antwoord11 = input("naar welk land vlucht je? \n a = pakistan \n b = turkmenistan \n c = iran \n d = tajikistan")
    if antwoord11 == "a":
        print("je gaat naar pakistan maar wordt weer uitgeleverd aan afghanistan. PRISON ENDING")
    elif antwoord11 == "b":
        print("je gaat naar turkmenistan maar wordt weer uitgeleverd aan afghanistan. PRISON ENDING")
    elif antwoord11 == "c":
        vraag16()
    elif antwoord11 == "a":
        print("je gaat naar tajikistan en leeft daar je leven uit. TAJIKISTAN ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag11()

def vraag12():
    antwoord12 = input("je gaat naar een andere stad wil je hier blijven of naar europa gaan? \n a = blijven \n b = naar europa")
    if antwoord12 == "a":
        vraag15()
    elif antwoord12 == "b":
        vraag4()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag12()

def vraag13():
    antwoord13 = input("waar wil je wonen in belgië? \n a = naar brussel gaan \n b = naar antwerpen")
    if antwoord13 == "a":
        vraag17()
    elif antwoord13 == "b":
        vraag18()
    elif antwoord13 == "c":
        vraag21()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag13()

def vraag14():
    antwoord14a = input("waar in duitsland wil je wonen? \n a = wenen \n b = keulen \n c = berlijn")
    if antwoord14a == "a":
        antwoord14b = input("dat ligt niet eens in duitsland, wil je naar ooostenrijk? ja of nee")
        if antwoord14b == "ja":
            print("je gaat naar wenen in oosterijk en leeft daar de rest van je leven")
            vraag19()
        elif antwoord14b == "nee":
            vraag14()
    elif antwoord14a == "b":
        vraag20()
    elif antwoord14a == "c":
        vraag19()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag14()

def vraag15():
    antwoord15 = input("de taliban komt aan in de stad. Ze zien dat je alleen bent. ze vragen of jij je wilt aansluiten bij de taliban. \n a = aansluiten \n b = niet aansluiten ")
    if antwoord15 == "a":
        print("je sluit je aan bij de taliban. BAD ENDING")
    elif antwoord15 == "b":
        vraag6()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag15()

def vraag16():
    antwoord16 = input("je bent in iran maar je moet verder naar europa hoe wil je er naartoe? \n a = vliegtuig \n b = lopen \n c = een auto stelen")
    if antwoord16 == "a":
        vraag4()
    elif antwoord16 == "b":
        print("je loopt te lang zonder eten en drinken daardoor ga je dood. DEAD ENDING")
    elif antwoord16 == "c":
        print("je steelt een auto maar wordt gepakt door de politie. PRISON ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag16()

def vraag17():
    antwoord17 = input("wil je hier echt wonen? ja of nee")
    if antwoord17 == "ja":
        print("je bent in brussel gaan wonen maar je woont er illegaal dus word je terug gestuurd. SENT BACK ENDING")
    elif antwoord17 == "nee":
        vraag13()

def vraag18():
    antwoord18 = input("wil je hier echt wonen? ja of nee")
    if antwoord18 == "ja":
        print("je bent in antwerpen gaan wonen maar je woont er illegaal dus word je terug gestuurd. SENT BACK ENDING")
    elif antwoord18 == "nee":
        vraag13()


def vraag19():
    antwoord19 = input("je bent veilig angekomen. wil je jouw familie ook naar hier laten komen? ja of nee ")
    if antwoord19 == "ja":
        print("je familie komt ook hier naartoe. GOOD ENDING")
    elif antwoord19 == "nee":
        print("je familie komt niet hier en gaan dood in afghanistan. DEVIL'S ENDING")
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag19()

def vraag20():
    antwoord20 = input("wil je hier echt wonen? ja of nee")
    if antwoord20 == "nee":
        vraag21()
    elif antwoord20 == "ja":
        vraag19()

def vraag21():
    antwoord21 = input("waar wil je dan wonen? \n a = nederland \n b = belgië \n c = duitsland ")
    if antwoord21 == "a":
        vraag10()
    if antwoord21 == "b":
        vraag13()
    if antwoord21 == "c":
        vraag14()
    else:
        print("het ingevulde antwoord is niet geldig")
        vraag21()   
vraag1()
