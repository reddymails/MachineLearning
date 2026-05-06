#################
#
#  An example  to show class inheritance.
#
##############
import datetime


class Player:
    def _init__(self,fname,lname,birthday):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday

    def get_age(self):
        return datetime.datetime.today().year - self.birthday


#inherting parent class.
class CricketPlayer(Player):
    def __init__(self,fname,lname, birthday,team):
        Player.__init__(fname,lname,birthday)
        self.team = team
        self.scores = []

    def add_score(self,score):
        self.scores.append(score)

    def  get_average_score(self):
        return sum(self.scores)/len(self.scores)

class TennisPlayer(Player):
    def __init__(self,fname,lname, birthday, gwinner):
        super().__init__(fname,lname,birthday)
        self.grand_slam_winner = gwinner
        self.aces = []

    def add_ace(self,ace):
        self.aces.append(ace)

    def get_average_score(self):
        return sum(self.aces)/len(self.aces)

virat = CricketPlayer('Virat','Kohli',1985, 'India')
virat.add_score(90)
virat.add_score(35)
#Both works but better use method
virat.scores.append(136)

print(virat.get_average_score())

federrer = TennisPlayer('Roger','Federrer',1981,28)
federrer.add_ace(90)
federrer.add_ace(35)
federrer.add_ace(136)

print(federrer)
print(federrer.get_average_score())
