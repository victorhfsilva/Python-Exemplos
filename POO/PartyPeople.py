class PartyPeople:
    
    persons = 0
    
    def party(self):
        self.persons = self.persons + 1
        print("So far ",self.persons," persons.")

    #Constructor
    def __init__(self, persons):
        print("The object was created.")
        self.persons = persons
    
    #Destructor
    def __del__(self):
        print("The object was destructed")
        
    #To-String
    def __repr__(self):
    	return "The party is rocking. There are {} persons.".format(self.persons)
    	

#Inheritance
class PartyGirls(PartyPeople):
    
    girls_percentage = 0
    girls = 0
    
    def party(self):
        
        self.persons = self.persons + 1
        self.girls = self.girls_percentage * self.persons
        
        print("So far ",self.persons," persons. And ",self.girls," girls.")
        is_whole(self.girls)
    
    def __init__(self,girls_percentage,persons):
        
        self.persons = persons
        self.girls_percentage = girls_percentage
        
        if girls_percentage > 1 or girls_percentage < 0:
            print("Oh goodness, the percentage of girls go beyond boundaries.")
            quit()
        else:
            if girls_percentage > 0.5:
                print("This party is wild!")
            else:
                print("This party sucks!")
            self.girls = girls_percentage * self.persons
            print("So far ",self.girls," girls.")
            is_whole(self.girls)

def is_whole(girls):
    if not girls.is_integer():
        print("Fuck! Some girl is not whole.")
        
party1 = PartyPeople(2)
party2 = PartyPeople(5)

party1.party()
party1.party()

party2.party()

party3 = PartyGirls(0.72,10)
party3.party()
print(party3.girls)

print(dir(party2))
print(dir(party3))

