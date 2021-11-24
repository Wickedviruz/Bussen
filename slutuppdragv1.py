import os
import json

#klass fr bussen Bussen 
class buss:
    passangers=dict()
    quantity=0
    id=0
    filecreate=False

    #Clear för att rensa konsolen.
    def clear(self):
        os.system('cls')

    #användar menyn
    def menu(self):
        while True:
            b.clear()
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
        b.clear()

        try:
            firstname=str(input("Vilket förnamn har passageraren? "))
            lastname=str(input("Vilktet efternamn har passageraren? "))
            age=int(input("Hur gammal är passageraren? "))
            logweight=int(input("Hur mycket väger bagaget? "))

            if b.quantity <= 25:
                b.filecreate=True
                b.quantity += 1
                b.id += 1
                b.passangers.update({'ID':b.id, 'Firstname':firstname, 'Lastname':lastname, 'Age':age, 'Bagagevikt':logweight,})

            else:
                print("Bussen är full!")

        except:
            b.clear()
            print("Felaktig inmatning")
            self.add_passanger()

    def json_create(self):
        while True:
            print("creating json object!")
            if b.filecreate==True:

            try:
                with open("data.json" "w") as json_file:
                    json.dumps(b.passangers, json_file, indent="4")

    #skriv ut alla passagerare
    def showbuss(self):
        input("all data")
        

    #Se total ålder eller medel ålder
    def total_age(self):
        pass

    #Se total vikt av bagage (annan fil?)
    def total_weight(self):
        pass

#Call emot klassen och menyn.
b = buss()
b.menu()