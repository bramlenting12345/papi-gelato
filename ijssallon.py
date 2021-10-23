
import os
import time



def clear_screen():
    os.system("cls")

def timer_5():
    time.sleep(5)



def welkom():
    clear_screen()
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.") 
    timer_5()
    clear_screen()
    bestelling_bolletjes()
    

# ------------------------------------------------------stap 1--------------------------------------------------------------------------------------


    

def bestelling_bolletjes():
    aantal_bolletjes= int(input("hoeveel bolletjes wilt u ? : "))
    if int (aantal_bolletjes) > 0 and int(aantal_bolletjes) < 4:    
        vraag_hoorntje_bakje(aantal_bolletjes)
    elif int (aantal_bolletjes) > 3 and int (aantal_bolletjes) < 9:
        foute_bestelling(aantal_bolletjes)
    else:
        print("sorry zukke grote bakken hebben we niet ") + bestelling_bolletjes()
    
             
# ------------------------------------------------------stap 2--------------------------------------------------------------------------------------------


def vraag_hoorntje_bakje(aantal_bolletjes):
    
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
        print(" u kunt allen kiezen tussen a of b  : ") + vraag_hoorntje_bakje()
    
        
   

#------------------------------------------------------foute bestellng --------------------------------------------------------------------------------------    
def foute_bestelling(aantal_bolletjes): 
   uw_bestelling=("dan krijgt u van mij een bakje  met  " + str(aantal_bolletjes) + " bolletjes ")  
   print (uw_bestelling)
    


#--------------------------------------------------------stap 3---------------------------------------------------------------------------------------------
def goede_bestelling(verpakking_bolletjes,aantal_bolletjes):
    complete_bestelling = input("hier is uw " + verpakking_bolletjes + " met uw " + str (aantal_bolletjes) + " bolletjes" + "wilt u nog meer bestellen : Y / N " + " maak u keuze ")
    if complete_bestelling=="Y":
        welkom()
    elif complete_bestelling=="N":
        print("bedankt en tot ziens")    
    else:
        print("Sorry dat snap ik niet") + goede_bestelling(verpakking_bolletjes,aantal_bolletjes)
  
welkom()   
    
    




  

















