'''
 A example of defining class -

 In java :
    class CricketPlayer {
        String name;
        int age;

        CricketPlayer(String name, int age){
            this.name = name;
            this.age = age;
        }
    }
  So the init in Python is constructor just like in Java.
2. Why the double underscores __
    Methods like __init__ are called dunder methods (double underscore methods).
    They are special methods built into Python that have predefined meaning.

    Examples:

    Method	Purpose
    __init__	Initialize object
    __str__	String representation
    __len__	Length of object
    __eq__	Equality comparison

    class CricketPlayer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

        p = CricketPlayer("Virat")
        print(p)   # calls __str__()

'''
import datetime


class CricketPlayer:
    def __init__(self, fname,lname, age):
        self.first_name = fname
        self.last_name =lname
        self.age = age
        self.team = ''
        self.scores = []

    # Like toString in java
    def __str__(self):
         return self.first_name + ' ' + self.last_name + ' year =' + str(self.age) +" Age=" + str(self.get_age())

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.age

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def add_score(self, score):
        self.scores.append(score)

    # Operation overloading we can overload < or > operators.

    def __lt__(self, other):
        object1_score = self.get_average_score()
        object2_score = other.get_average_score()
        return object1_score < object2_score

    def __gt__(self, other):
        object1_score = self.get_average_score()
        object2_score = other.get_average_score()
        return object1_score > object2_score
    

virat = CricketPlayer('Virat','Kohli',35)
virat.add_score(90)
virat.add_score(35)
# both works but better use method
virat.scores.append(136)

Rohith = CricketPlayer('Rohith','Sharma',37)
Rohith.add_score(90)
Rohith.add_score(45)
Rohith.add_score(67)


David = CricketPlayer('David','Warner',40)
David.add_score(45)
David.add_score(56)
David.add_score(125)

print('Virat='+ str(virat)  +" Average Score="+ str(virat.get_average_score()))
print('Rohith='+str(Rohith)+" Average Score="+ str(Rohith.get_average_score()))
print('David='+str(David)+" Average Score="+ str(David.get_average_score()))

if(virat.get_average_score() > David.get_average_score()):
        print("Kohli is better than David")
else :
    print("Kohli not greater than David")


# Look  how we can use > or < on actual objects...
if (virat >David):
    print("Kohli is better than David.Checked using operator overloading")
else:
    print("Kohli not greater than David.Checked using operator overloading")


