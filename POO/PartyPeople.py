class PartyPeople:
    
    #In python there aren't private attributes or methods, an underscore is used to indicate this attribute shouldn't be accessed
    _persons = 0
    
    def party(self):
        self._persons = self._persons + 1
        print("So far ",self._persons," persons.")
    
    #Two underscores places the name of the class before the method or attribute to avoid overwriting 
    def __hello_people(self):
        print("Hello people!")
        
    #Constructor
    def __init__(self, persons):
        print("The object was created.")
        self._persons = persons
    
    #Destructor
    def __del__(self):
        print("The object was destructed")
        
    #To-String
    def __repr__(self):
    	return "The party is rocking. There are {} persons.".format(self._persons)
    	

#Inheritance
class PartyGirls(PartyPeople):
    
    girls_percentage = 0
    girls = 0
    
    def __hello_people(self):
        print("Hello girls!")
    
    def party(self):
        
        self._persons = self._persons + 1
        self.girls = self.girls_percentage * self._persons
        
        print("So far ",self._persons," persons. And ",self.girls," girls.")
        is_whole(self.girls)
    
    def __init__(self,girls_percentage,persons):
        
        self._persons = persons
        self.girls_percentage = girls_percentage
        
        if girls_percentage > 1 or girls_percentage < 0:
            print("Oh goodness, the percentage of girls go beyond boundaries.")
            quit()
        else:
            if girls_percentage > 0.5:
                print("This party is wild!")
            else:
                print("This party sucks!")
            self.girls = girls_percentage * self._persons
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

print(party1)
print(party3)

party3._PartyPeople__hello_people()
party3._PartyGirls__hello_people()

print(dir(party2))
print(dir(party3))

