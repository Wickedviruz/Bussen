import os
import csv

#klass fr bussen Bussen 
class buss:
    print("Välkommen till bussen by Johan")
    passangers=[]
    quantity=0

    #Clear för att rensa konsolen.
    def clear(self):
        os.system('cls')

    #användar menyn
    def menu(self):
        while True:
            print("************************")
            print("*********Bussen*********")
            print("************************")
            print("1. Lägg till passagerare")
            print("2. Se alla passagerare")
            print("3. Se total ålder")
            print("4. Se totalvikt av bagaget!\n")
            print("5. Avsluta programmet!")

            #Meny vals hantering
            try:
                option=int(input("Väl ett alternativ i menyn: "))

                if option == 1:
                    b.add_passanger()
                elif option == 2:
                    b.showbuss()
                elif option == 3:
                    b.total_age()
                elif option == 4:
                    b.total_weight()
                else:
                    b.clear()
                    print("Tack för att du använde bussprogrammet by Johan")
                    input("Programmet avslutas")
                    break

            except:
                b.clear()
                input("Felaktig inmanting")
                self.menu()

    #Skapa passagerare.
    def add_passanger(self):
        try:
            firstname=str(input("Vilket förnamn har passageraren? "))
            lastname=str(input("Vilktet efternamn har passageraren? "))
            age=int(input("Hur gammal är ", firstname, " ? "))
            logweight=int(input("Hur mycket väger bagaget? "))

            if b.quantity <= 25:
                b.passangers.insert
                b.quantity += 1

            else:
                input("Bussen är full!")

        except:
            b.clear()
            input("Felaktig inmatning")


    #skriv ut alla passagerare
    def showbuss(self):
        pass

    #Se total ålder eller medel ålder

    #Se total vikt av bagage (annan fil?)

#Call emot klassen och menyn.
b = buss()
b.menu()