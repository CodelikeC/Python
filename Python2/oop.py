#this is OOP 
#Nguyen Duc Tri 
#Location : Ha Noi 
class people () : 
    def _init_(self, name,age) :

        self.name = name  
        self.age = age 

    def greet(self) : 

        print ("greetings", self.name)
        print ("The age of that person is:", self.age)
        
        person_1 = people(name = "Iron Man", age = 35)
        person_2 = people(name = "Tony Stark")

        person_1.greet()
        person_2.greet()

        print ("The person_1 name is:", person_1.name)
        print ("The second person name is :", person_2.name)

