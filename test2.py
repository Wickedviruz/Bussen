import os


class jsoncreater:
    passangers=dict()
    quantity=0
    id=0

    def clear(self):
        os.system('cls')

        #Skapa passagerare.
    def add_passanger(self):
        
        try:
            firstname=str(input("Vilket förnamn har passageraren? "))
            lastname=str(input("Vilktet efternamn har passageraren? "))
            age=int(input("Hur gammal är passageraren? "))
            logweight=int(input("Hur mycket väger bagaget? "))

            if jsoncreater.quantity <= 25:
                jsoncreater.passangers.update({'ID':b.id, 'Firstname':firstname, 'Lastname':lastname, 'Age':age, 'Bagagevikt':logweight,})
                jsoncreater.quantity += 1
                jsoncreater.id += 1

            else:
                print("Bussen är full!")

        except:
            b.clear()
            print("Felaktig inmatning")
            self.add_passanger()
