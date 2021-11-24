#Bussen av Johan Ivarsson
#Importerar rätt modul/moduler
import os

#Klassen "buss"
class buss:

    #Init som lägger grund för filen
    #Börjar med att kolla om "quantity.txt" finns
    #Gör den det läses den till variablen "quantity"
    def __init__(self):
        if os.path.exists("quantity.txt"):
            with open('quantity.txt') as file:
                self.id = self.quantity = int(file.read())
            
        #Finns ej filen så skapas den och det skrivs ett värde till den.
        else:
            file=open("quantity.txt", mode="a")
            file.write(str(0))
            file.close
            with open("quantity.txt") as file:
                self.id = self.quantity = int(file.read())

    #Clear för att rensa konsolen.
    #Och håll UI rent och lätt att använda
    def clear(self):
        os.system('cls')

    #Metod för huvudmenyn
    #Skriver ut flera rader text för att illustrera en meny
    #efterfrågar sedan input ifrån användaren iform av siffror.
    #för att sedan köra en IF sats som avgör vad som skall hända.
    def menu(self):
        while True:
            b.clear()
            print("************************")
            print("*********Bussen*********")
            print("************************")
            print("1. Hantera passagerare")
            print("2. Visa alla passagerare")
            print("3. Visa ålders data")
            print("4. Se totalvikt av bagaget!\n")
            print("5. Avsluta programmet!\n")

            #Meny valhantering
            try:
                option=int(input("Välj ett alternativ i menyn: "))

                if option == 1:
                    b.clear()
                    print("1. Lägg till passagerare")
                    print("2. Ta bort alla passagerare\n")

                    #Submeny vid val 1 i huvudmeny.
                    try:
                        suboption=int(input("Välj ett alternativ i menyn: "))
                        if suboption == 1:
                            b.add_passanger()
                        elif suboption == 2:
                            b.remove_passanger()

                    #Felhantering av submenyn
                    except:
                        b.clear()
                        input("Felaktig inmanting1")
                     
                elif option == 2:
                    b.print_file()
                elif option == 3:
                    b.clear()
                    print("1. Visa yngsta passageraren")
                    print("2. Visa äldsta passageraren")
                    print("3. Visa medelåldern\n")

                    #Submeny vid val 1 i huvudmeny.
                    try:
                        suboption1=int(input("Välj ett alternativ i menyn: "))
                        if suboption1 == 1:
                            print("Den yngsta passageraren på bussen är: ", self.youngest(), "år gammal\n")
                            input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")
                        elif suboption1 == 2:
                            print("Den äldsta passageraren på bussen är:", self.oldest(), "år gammal!\n")
                            input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")
                        elif suboption1 == 3:
                            print("Medel åldern på alla passagerare är:",self.awg_age(),"år\n")
                            input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

                    #Felhantering av submenyn
                    except:
                        b.clear()
                        input("Felaktig inmanting1")

                elif option == 4:
                    b.totalweight()
                
                #Vid val av nummer 5 eller annat nummer så skrivs tack meddelande
                #Och användaren blir ombedd att trycka ENTER för att avsluta.
                #Efter det break för att avsluta.
                else:
                    b.clear()
                    print("Tack för att du använde bussprogrammet by Johan")
                    input("Tryck ENTER för att avsluta programmet")
                    break

            #Felhantering vid felaktig inmatning i menyn.
            except:
                b.clear()
                input("Felaktig inmanting")

    #Metod för att lägg till passagerare.
    #Kollar om variablen quantity är likamed eller mindre än 25. är den det fortsätt denna if statement
    #Där användaren får fylla i några variabler och de omvandlas till rätt datatyp
    def add_passanger(self):
        if self.quantity <=25:
            b.clear()
            b.__init__()
            firstname=str(input("Vilket förnamn har passageraren? "))
            lastname=str(input("Vilktet efternamn har passageraren? "))
            age=int(input("Hur gammal är passageraren? "))
            logweight=int(input("Hur mycket väger bagaget? "))
            self.quantity += 1
            self.id += 1
            yn=input("Spara till fil? ja/nej \n")

            #Efter input får man välja om man vill spara till fil.
            #Öppnar filerna den skall skriva till och skriver sagd information med rätt datatyp.
            #Sedan stänger vi alla filer och ränsar menyn. och visar användaren att allt sparades rätt.
            if yn=="ja":
                file=open("quantity.txt",mode="w")
                file.write(str(self.quantity))
                file=open("name.txt",mode="a")
                file.write("ID " + str(b.id) + " || " "Förnamn: " + firstname + " || " "Efternamn: " + lastname + "\n")
                file=open("age.txt", mode="a")
                file.write(str(age) + "\n")
                file=open("weight.txt", mode="a")
                file.write(str(logweight) + "\n")
                file.close
                b.clear()
                input("tillagd i systemet! Tryck 'ENTER' för att komma tillaka till huvudmenyn")

            #Vid nej sparas ingenting och man bilr tillbaka visad till menyn
            elif yn=="nej":
                print("Sparar ej till fil.")
                input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

            #Vid ogiltiga svar, skrivs felmeddelande och man blir skickad tillbaka till menyn.
            else:
                b.clear()
                input("Ogiltigt svar. inget skrivs.")

        #ifall variablen quantity är större än 25
        #Så är bussen full så bilr man tillbakavisad till menyn.   
        else:
            b.clear()
            input("Bussen är full!")
            self.menu()

    #Metod för att ta bort passagerare som är sparade i filer och rensar quantity.
    #Metoden kör en if statement för att se om filen "name.txt" finns.
    #Finns den filen så tas de andra filerna också bort, sedan rensas UI.
    def remove_passanger(self):
        if os.path.exists("name.txt"):
            os.remove("name.txt")
            os.remove("weight.txt")
            os.remove("age.txt")
            os.remove("quantity.txt")
            b.clear()
            input("All passagerar-data är borttagen.")

        #Finns ej filerna så får användaren ett felmeddelande och blir skickade tillbaka till menyn.
        else:
            b.clear()
            input("Det finns ingen sparad passagerare-data.")


    #Metod för att skriva ut vilka passagerare som är med.
    #Börjar med att rensa menyn, sendan kör en if statemen för att se om filen"name.txt" finns
    #Finns fieln så öppnar den i läge "r" för read, sedan skriver filens innehåll till variablen namn
    #Efter det stängs filen och sedan skrivs variablen namn ut.
    def print_file(self):
        b.clear()
        if os.path.exists("name.txt"):
            f = open('name.txt', 'r')
            namn = f.read()
            f.close()
            print(namn)
            input("Tryck ENTER för att komma tillbaka till menyn")

        #Error hantering om fil ej finns.
        #Och blir tillbakavisad till huvudmenyn.
        else:
            b.clear()
            input("Det finns ingen användardata sparad.")

    #Läser in filen "age.txt" och beräknar totala värdet av den
    #och skriver sedan ut den
    def youngest(self):
        b.clear()
        try:
            with open('age.txt') as f:
                data = [int(line.rstrip()) for line in f]
                youngest = min(data)
                return youngest

        except:
            b.clear()
            print("Det finns ingen data sparad")
            input("Tryck ENTER för att komma tillbaka till menyn")

    #Metod för att skriva ut äldsta passageraren
    def oldest(self):
        b.clear()
        try:
            with open('age.txt') as f:
                data = [int(line.rstrip()) for line in f]
                oldest = max(data)
                return oldest

        except:
            b.clear()
            print("Det finns ingen data sparad")
            input("Tryck ENTER för att komma tillbaka till menyn")


    #Metod för att beräka medelåldern
    def awg_age(self):
        b.clear()
        try:
            with open('age.txt') as f:
                data = [int(line.rstrip()) for line in f]
                return (sum(data)/len(data))

        except:
            b.clear()
            print("Det finns ingen data sparad")
            input("Tryck ENTER för att komma tillbaka till menyn")

    #Metod för att beräkna totalvikten på allt bagage
    #Gör en try för att öppna filen weight.txt och läsa den
    #Kör sedan en forloop för att skriva ut summan.
    #Finns ej filen körs en except och meddelar det för användaren.
    def totalweight(self):
        b.clear()
        try:
            sum = 0
            with open('weight.txt', 'r') as f:
                for line in f:
                    line =line.strip()
                    sum = sum + int(line)
                        
            print("Den totala vikten av allt bagage är:", sum,"KG\n")
            input("Tryck ENTER för att komma tillbaka till menyn")
                

        except:
            b.clear()
            print("Det finns ingen data sparad för allt bagage!\n")
            input("Tryck ENTER för att komma tillbaka till menyn")
    
b=buss()
b.menu()