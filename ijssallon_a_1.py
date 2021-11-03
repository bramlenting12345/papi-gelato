
#----------------------------------------------------------import functies-------------------------------------------------

import os
import time

#----------------------------------------------------------variable voor programma-----------------------------------------

verpakking_bolletjes = "geen"
verpakking_bolletjes = "geen"
aantal_bolletjes = 0
totaal_bolletjes = 0
totaal_bakjes = 0
totaal_hoorntjes = 0       
totaal_topping_slagroom = 0
totaal_topping_sprinkels = 0 
totaal_topping_caramel_saus = 0  

eenheid = "geen"
       
#-----------------------------------------------------------variabelen voor bon ---------------------------------------------

Gekozen_smaken = []


prijs_bolletjes = 1.10
prijs_bakje =  0.75
prijs_hoorntje = 1.25
prijs_slagroom = 0.50
prijs_sprinkels = 0.30
prijs_caramel_saus = 0.90  
prijs_liters = 9.80



#-----------------------------------------------------------kies topping verhaaltje ----------------------------------------

kies_p_z = """-------------------------------------------------------------------------------------------------------------

kies of u parteculier of zakelijk wilt bestellen 

a = particulier 
b = zakelijk

----------------------------------------------------------------------------------------------------------------------------
"""
 
kies_topping = """-----------------------------------------------------------------------------------------------------------

welke topping wilt u kies uit 

a = Geen              € 0 
b = Slagroom          € 0,50
c = Sprinkels         € 0,30
d = Caramel saus      € 0,90


"""

#-------------------------------------------------------------kies topping verhaaltje---------------------------------------

kies_smaken = """------------------------------------------------------------------------------------------------------------

kies u smaak u kunt kiezen uit de volgende smaken

A = Aardbei
C = Chocolade
M = Munt
V = Vanilie

------------------------------------------------------------------------------------------------------------------------------
"""
#-----------------------------------------------------------def clear screen--------------------------------------------------
def clear_screen():
    os.system("cls")

#-----------------------------------------------------------def sleep timer---------------------------------------------------

def timer_5():
    time.sleep(5)

#----------------------------------------------------------- def welkom / komt alles in---------------------------------------

def welkom(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):
                                                                      
    clear_screen()
    print("Welkom bij Papi Gelato kies uit de volgende smaken .") 
    timer_5()
    clear_screen()
    type_klant(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)    

    

#---------------------------------------------------------------def type klant-------------------------------------------------    
def type_klant(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):
    print(kies_p_z)
    vraag_p_z = input("vul hier u antwoord in : ")
    if vraag_p_z=="a":
        eenheid="bolletjes"
        bestelling_bolletjes(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    elif vraag_p_z =="b":
        eenheid="liters" 
        bestelling_bolletjes(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    else:
        print("Sorry dat is geen optie die we aanbieden...” ") 
        type_klant(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus) 

# ------------------------------------------------------stap 1 / def bestelling bolletjes -------------------------------------------------------------------------------------

    
def bestelling_bolletjes(eenheid,verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):                                                                          # def besteling bolletjes
    aantal_bolletjes= int(input("hoeveel " + eenheid + " wilt u ? : "))
    totaal_bolletjes=aantal_bolletjes+totaal_bolletjes
    smaken(aantal_bolletjes,eenheid)
    
    
    topings(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    


    
             
# ------------------------------------------------------stap 2 / def vraag hoorntje bakje ---------------------------------------------------------------------------------------


def vraag_hoorntje_bakje(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):
    
                                                   
    verpakking_bolletjes=input("wilt u deze  " + str(aantal_bolletjes) + " bolletejes in een : A = bakje  B = hoorntje " + ":  maak u keuze " )
    if verpakking_bolletjes=="a":
        totaal_bakjes = totaal_bakjes + 1
        print("u heeft gekozen voor een bakje ")
        verpakking_bolletjes = "bakje"

        goede_bestelling(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    elif verpakking_bolletjes=="b":
        totaal_hoorntjes = totaal_hoorntjes + 1
        print("u heeft gekozen voor een hoorntje") 
        verpakking_bolletjes="hoorntje"

        goede_bestelling(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    else:
        print(" Sorry dat is geen optie die we aanbieden...” ") 
        
        vraag_hoorntje_bakje(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    
        
   

#------------------------------------------------------tussen stap voor grote bestelling  --------------------------------------------------------------------------------------    
def grote_bestelling(aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):                                                            # def foute bestelling
   verpakking_bolletjes="bakje"
   totaal_bakjes = totaal_bakjes + 1
   goede_bestelling(aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)     
   


    


#--------------------------------------------------------stap 3 / goede bestelling ---------------------------------------------------------------------------------------------
def goede_bestelling(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):                                         # def foute bestelling
    complete_bestelling = input("hier is uw " + str(verpakking_bolletjes) + " met uw " + str (aantal_bolletjes) + " bolletjes" + "wilt u nog meer bestellen : Y / N " + " maak u keuze ")
    if complete_bestelling=="Y":
    
        welkom(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    elif complete_bestelling=="N":
        print("bedankt en tot ziens")    
        bon(totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)


    else:
        print("Sorry dat is geen optie die we aanbieden...”") + goede_bestelling(verpakking_bolletjes,aantal_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom)
    


#---------------------------------------------------------def smaken -----------------------------------------------------------------------------------------------------------

def smaken(aantal_bolletjes,eenheid):
   
    print(kies_smaken)
    for i in range (aantal_bolletjes):
        smaak_keuze = input("maak u keuze voor "+ eenheid + str(i + 1) + " : " )
        if smaak_keuze=="a":
            Gekozen_smaken.append("Aardbei")
        elif smaak_keuze=="c":
            Gekozen_smaken.append("chocolade")
        elif smaak_keuze=="m":
            Gekozen_smaken.append("Munt")
        elif smaak_keuze=="v":
            Gekozen_smaken.append("Vanilie")
        else:
            print("Sorry dat is geen optie die we aanbieden.. ") + smaken()                    

    print("u heeft de volgende smaken gekozen: ")

    for i in range(aantal_bolletjes):
        print( eenheid + str(i+1) + "= " + Gekozen_smaken[i])


    check_vraag =input ("klopt dit ? (j / n ) : ")
    if check_vraag=="j":
        print ("ziet er lekker uit goede combinatie  ")
        if eenheid=="liters":
            zakelijke_bon(aantal_bolletjes)    

    elif check_vraag=="n":
        smaken(aantal_bolletjes)  
    else:
        ("Sorry dat is geen optie die we aanbieden...") + smaken(aantal_bolletjes)



#---------------------------------------------------------------------def toppings----------------------------------------------------------------------------------

def topings(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):

    print(kies_topping)
    vraag_topping = input("kies u topping uit ")
    if vraag_topping=="a":
        print ("u heeft gekozen voor geen topping  ")
        print(" ")


    elif vraag_topping == "b":
        print("u heeft gekozen voor de slagroom topping " )
        print(" ")
        totaal_topping_slagroom=totaal_topping_slagroom +1 
     
        
      
    elif vraag_topping =="c":
       print("u heeft gekozen voor de sprinkels topping ")
       print(" ")
       totaal_topping_sprinkels = totaal_topping_sprinkels + 1

    elif vraag_topping =="d":
       print("u heeft gekozen voor de topping caramel saus")
       print(" ")
       totaal_topping_caramel_saus = totaal_topping_caramel_saus + 1     

    else:
        print("Sorry dat is geen optie die we aanbieden...” ")
        print(" ")
        topings(totaal_topping_slagroom)

    if int (aantal_bolletjes) > 0 and int(aantal_bolletjes) < 4:    
        vraag_hoorntje_bakje(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    elif int (aantal_bolletjes) > 3 and int (aantal_bolletjes) < 9:
        grote_bestelling(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    else:
        print("sorry zukke grote bakken hebben we niet ") + bestelling_bolletjes(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus)
    

#-------------------------------------------------------------------- def bon----------------------------------------------------------------------------------------------------------------                                      
def bon(totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_slagroom,totaal_topping_sprinkels,totaal_topping_caramel_saus):
    print("------------------Papi Gelato----------------")
    print(" ")
    print("bolletjes      " + str(totaal_bolletjes) + " " + "x" + " " + "€ 1,10" + " " + " " + " " + "= " + "€ " + (str(format(totaal_bolletjes*prijs_bolletjes,'.2f'))))
    print("Horentje       " + str(totaal_hoorntjes) + " " + "x" + " " + "€ 1.25" + " " + " " + " " + "= " + "€ " + (str(format(totaal_hoorntjes*prijs_hoorntje,'.2f'))))
    print("bakjes         " + str(totaal_bakjes)    + " " + "x" + " " + "€ 1.25" + " " + "" + " " +" = " + "€ "  +  (str(format(totaal_bakjes*prijs_bakje,'.2f')))) 
    print("toppings       " + str(totaal_topping_slagroom+totaal_topping_caramel_saus+totaal_topping_sprinkels)    + " stuks      = € " + (str(format(totaal_topping_sprinkels*prijs_sprinkels + totaal_topping_slagroom*prijs_slagroom +  totaal_topping_caramel_saus*prijs_caramel_saus,'.2f'))))
   
    
    
    print("                       " + "-------- + ")
    print("totaal " + "                " + "= " + "€ " + (str(format((totaal_bolletjes*prijs_bolletjes)+(totaal_hoorntjes*prijs_hoorntje)+(totaal_bakjes*prijs_bakje)+(totaal_topping_sprinkels*prijs_sprinkels + totaal_topping_slagroom*prijs_slagroom +  totaal_topping_caramel_saus*prijs_caramel_saus),'.2f'))))

#=============================================================================================================================================================================================

#---------------------------------------------------------------------def bon zakelijk of particulier-----------------------------------------------------------------------------------------
def zakelijke_bon(aantal_bolletjes):
    print("====================Papi gelato=================")
    print(" ")
    print("liters" + "   x " + str(aantal_bolletjes) +  " €"+ str(format(prijs_liters,'.2f')) + "     =  €" + (str(format(aantal_bolletjes*prijs_liters,'.2f'))))
    print("                      -------- +")
    print(" ")
    print("totaal " + "               = " + " €" + str(format(aantal_bolletjes*prijs_liters,'.2f')))
    print("BTW (9%) " + "             =   €" + str(format(aantal_bolletjes*prijs_liters/100*9,'.2f')))
    print(" ")
    print("=================================================")
    exit()


#========================================================================= def welkom aanroep heel het programma==================================================================================

welkom(eenheid,aantal_bolletjes,verpakking_bolletjes,totaal_bolletjes,totaal_bakjes,totaal_hoorntjes,totaal_topping_caramel_saus,totaal_topping_slagroom,totaal_topping_sprinkels)
