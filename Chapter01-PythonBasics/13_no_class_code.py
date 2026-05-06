####################
# A demo to show code without classes. Its a pain.
############
import datetime

virat = {
    'first_name': 'Virat',
    'last_name': 'Kohli',
    'birth_year':'1990',
    'scores' : []
}

virat['scores'].append(100)
virat['scores'].append(85)
virat['scores'].append(54)

def get_average_score(player):
    total_score = player['scores']
    average_score = sum(total_score)/len(total_score)
    return average_score

def get_age(player):
    birth_year = player['birth_year']
    now = datetime.datetime.now()
    return  now.year - int(birth_year)


print(get_average_score(virat))
print(get_age(virat))


