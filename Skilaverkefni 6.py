Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Sölvi geir Björnsson

#Allir liðir eru í einnu lykkju til að notandi getur valið hvaða lið hann vill gera.
lykkja = 0
while lykkja == 0:
    print("1. Kennitala")
    print("2. Búa til nýtt orð")
    print("3. Sneið af streng")
    print("4. Hætta")
    lidur = input("Hvaða lið viltu gera? ")

    #Liður 1
    #Forritið biður um kennitölu frá notanda og passar að hún er rétt slegin inn.
    #Ef kennitalan er ekki rétt inn slegin er notandinn beðinn um að skrifa hana aftur þangað til að hún er rétt.
    if lidur == '1':
        rett = 0
        while rett == 0:
            kennitala = input("Sláðu inn kennitöluna þína ")
            #Passar að kennitalan er í réttri lengd
            if 10 == len(kennitala):
                dags = kennitala [0:2]
                man = kennitala [2:4]
                ar = kennitala [4:6]
                dags = int(dags)
                man = int(man)
                ar = int(ar)

                #Fyrstu tvær tölurnar geta bara verið dagar og meiga ekki vera yfir 32
                if dags <= 32:
                    #Tölur 3 og 4 geta bara verið mánaðarnúmer og meiga ekki vera yfir 12
                    if man <= 12:
                        #Tölur 5 og 6 geta bara verið fæðingarár og notandi má ekki vera eldri en 90
                        if ar <= 16 or ar >= 26 and ar <= 99:
                            print("Vel gert þú slóst inn rétta kennitölu", kennitala)
                            rett += 1
                        else:
                            print("Vitlaus kennitala, reyndu aftur")
                    else:
                        print("Vitlaus kennitala, reyndu aftur")
                else:
                    print("Vitlaus kennitala, reyndu aftur")
            else:
                print("Vitlaus kennitala, reyndu aftur")

    #Liður 2
    #Forritið tekur inn streng frá notanda og býr til nýjan streng úr fyrstu 2 og seinustu 2 stökunum í upphafsstrengnum
    #Ef strengurinn er minni en 5 stafir er notandi beðinn um að slá inn strenginn aftur þangað til að strengurinn er amk 5 stafa langur
    elif lidur == '2':
        lengd = 0
        while lengd == 0:
            strengur = input("Sláðu inn orð ")
            if len(strengur) >= 5:
                print(strengur)
                fyrriHluti = strengur [0:2]
                senniHluti = strengur [-2:]
                nyrStrengur = fyrriHluti + senniHluti
                #Prentar út nýja strenginn
                print(nyrStrengur)
                #Prentar út nýja strenginn í hástöfum
                print(nyrStrengur.upper())
                #Prentar út nýja strenginn í lágstöfum
                print(nyrStrengur.lower())
                lengd += 1
            else:
                print("Strengurinn er minni en 5 stafir, reyndu aftur")

    #Liður 3
    #Forritið biður um nafn frá notanda
    #Forritið tekur sneið úr nafninu og prentar fyrst út allt nafnið síðan allt nema first bókstafinn o.s.fvr
    elif lidur == '3':
        teljari = 0
        nafn = input("Sláðu inn nafn ")
        for i in nafn:
            print(nafn[teljari:])
            teljari += 1

    #Liður 4
    #Hætta
    elif lidur == '4':
        break
