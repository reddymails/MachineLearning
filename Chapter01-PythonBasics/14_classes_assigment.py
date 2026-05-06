'''
1. Avengers is a Marvel’s American Superheroes team, and if you are a fan of avengers, recently you have learned about classes and objects in your python course. Now you want to showcase your programming skills by representing the Avengers team using classes. Create a class called Avenger and create these six superheroes using this class.

super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
Your Avenger class should have these properties:

Name
Age
Gender
Super Power
Weapon

2. Captain America has Super strength, Iron Man has Technology, Black Widow is superhuman, Hulk has Unlimited Strength, Thor has super Energy and Hawkeye has fighting skills as superpowers.
Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and Arrows
3. Create methods to get the information about each superhero
4. Create a method is_leader() which will tell if the superhero is a leader or not.

'''


class Avenger:

    def __init__(self, fullName,age,gender,power,wpn):
        self.Name =fullName
        self.Age =age
        self.Gender =gender
        self.Super_Power =power
        self.Weapon =wpn

    def is_leader(self):
        if(self.Name == 'Captain America'):
            return True
        else:
            return False

    def __str__(self):
        return self.Name +"," + str(self.Age) + "," + str(self.Gender) + "," + str(self.Super_Power)

captain_america = Avenger('Captain America',100,'male','Super strength','shield')
iron_man = Avenger('Iron Man', 45, 'male', 'Technology', 'Armor')
black_widow = Avenger('Black Widow', 35, 'female', 'Superhuman', 'Batons')
hulk = Avenger('Hulk', 40, 'male', 'Unlimited Strength', 'No Weapon')
thor = Avenger('Thor', 1500, 'male', 'Super Energy', 'Mjolnir')
hawkeye = Avenger('Hawkeye', 38, 'male', 'Fighting Skills', 'Bow and Arrows')

print(captain_america)
print(iron_man)
print(black_widow)
print(hulk)
print(thor)
print(hawkeye)

print(captain_america.is_leader())
print(hawkeye.is_leader())