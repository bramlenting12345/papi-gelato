
import os
import time

Gekozen_smaken=[]
verpakking_bolletjes = "geen"
aantal_bolletjes = 0
totaal_bolletjes = 0
totaal_bakjes = 0
totaal_hoorntjes = 0

kies_smaken = """------------------------------------------------------------------------------------------------------------

kies u smaak u kunt kiezen uit de volgende smaken

A = Aardbei
C = Chocolade
M = Munt
V = Vanilie

------------------------------------------------------------------------------------------------------------------------------
"""

def clear_screen():
    os.system("cls")

def timer_5():
    time.sleep(5)



def welkom(verpakking_bolletjes,aantal_bolletjes):                                                                                       # def welom 
    clear_screen()
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.") 
    timer_5()
    clear_screen()
    bestelling_bolletjes(aantal_bolletjes,verpakking_bolletjes)
    


# ------------------------------------------------------stap 1--------------------------------------------------------------------------------------

    
def bestelling_bolletjes(verpakking_bolletjes,aantal_bolletjes):                                                                          # def besteling bolletjes
    aantal_bolletjes= int(input("hoeveel bolletjes wilt u ? : "))
    smaken(aantal_bolletjes)
    if int (aantal_bolletjes) > 0 and int(aantal_bolletjes) < 4:    
        vraag_hoorntje_bakje(aantal_bolletjes,verpakking_bolletjes)
    elif int (aantal_bolletjes) > 3 and int (aantal_bolletjes) < 9:
        grote_bestelling(aantal_bolletjes,verpakking_bolletjes)
    else:
        print("sorry zukke grote bakken hebben we niet ") + bestelling_bolletjes(verpakking_bolletjes,aantal_bolletjes)
    
             
# ------------------------------------------------------stap 2----------------------------------------------------------------------------------------


def vraag_hoorntje_bakje(aantal_bolletjes,verpakking_bolletjes):                                                             # def vraag hoorntje bakje
    
    verpakking_bolletjes=input("wilt u deze  " + str(aantal_bolletjes) + " bolletejes in een : A = bakje  B = hoorntje " + ":  maak u keuze " )
    if verpakking_bolletjes=="a":
        print("u heeft gekozen voor een bakje ")
        verpakking_bolletjes = "bakje"

        goede_bestelling(verpakking_bolletjes,aantal_bolletjes)
    elif verpakking_bolletjes=="b":
        print("u heeft gekozen voor een hoorntje") 
        verpakking_bolletjes="hoorntje"

        goede_bestelling(verpakking_bolletjes,aantal_bolletjes)
    else:
        print(" u kunt allen kiezen tussen a of b  : ") + vraag_hoorntje_bakje(verpakking_bolletjes,aantal_bolletjes)
    
        
   

#------------------------------------------------------grote bestellng --------------------------------------------------------------------------------------    
def grote_bestelling(aantal_bolletjes,verpakking_bolletjes):                                                            # def foute bestelling
   verpakking_bolletjes="bakje"
   goede_bestelling(aantal_bolletjes,verpakking_bolletjes)
   


    


#--------------------------------------------------------stap 3---------------------------------------------------------------------------------------------
def goede_bestelling(verpakking_bolletjes,aantal_bolletjes):                                         # def foute bestelling
    complete_bestelling = input("hier is uw " + str(verpakking_bolletjes) + " met uw " + str (aantal_bolletjes) + " bolletjes" + "wilt u nog meer bestellen : Y / N " + " maak u keuze ")
    if complete_bestelling=="Y":
        welkom(verpakking_bolletjes,aantal_bolletjes)
    elif complete_bestelling=="N":
        print("bedankt en tot ziens")    
    else:
        print("Sorry dat snap ik niet") + goede_bestelling(verpakking_bolletjes,aantal_bolletjes)
  




def smaken(aantal_bolletjes):
   
    print(kies_smaken)
    for i in range (aantal_bolletjes):
        smaak_keuze = input("maak u keuze voor bolletje "+ str(i + 1) + " : " )
        if smaak_keuze=="a":
            Gekozen_smaken.append("Aardbei")
        elif smaak_keuze=="c":
            Gekozen_smaken.append("chocolade")
        elif smaak_keuze=="m":
            Gekozen_smaken.append("Munt")
        elif smaak_keuze=="v":
            Gekozen_smaken.append("Vanilie")
        else:
            print("sorry dat snap ik niet ") + smaken()                    

    print("u heeft de volgende smaken gekozen: ")

    for i in range(aantal_bolletjes):
        print("Bolletje " + str(i+1) + "= " + Gekozen_smaken[i])


    check_vraag =input ("klopt dit ? (j / n ) : ")
    if check_vraag=="j":
        print ("ziet er lekker uit goede combinatie  ")
    elif check_vraag=="n":
        smaken(aantal_bolletjes)  
    else:
        ("sorry antwoord met j / n ") + smaken(aantal_bolletjes)

welkom(verpakking_bolletjes,aantal_bolletjes)












# Bolletjes (ongeacht de smaak) zijn €1,10 per stuk
# Horrentjes zijn €1,25 per stuk
# Bakjes zijn €0,75 per stuk















  
# Na het kiezen van een aantal bolletjes komt voor ieder bolletje de vraag: “Welke smaak wilt u voor bolletje nummer {X}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?”

# Bij een andere keuze dan A, C, M of V krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt de
















