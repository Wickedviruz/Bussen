import os
import test2


class menu:

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
                    m.clear()
                    test2.add_passenger()
                elif option == 2:
                    b.showbuss()
                elif option == 3:
                    b.total_age()
                elif option == 4:
                    b.total_weight()
                else:
                    m.clear()
                    print("Tack för att du använde bussprogrammet by Johan")
                    input("Programmet avslutas")
                    break

            except:
                m.clear()
                input("Felaktig inmanting!")
                self.menu()

m=menu()
m.menu()