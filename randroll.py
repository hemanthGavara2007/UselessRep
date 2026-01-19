#given 60 roll no , divide each into 5 groups by random ways
import random

roll = [x for x in  range(501,561)]
teams = []

while roll:
    team = []
    while len(team) < 5:
        x = random.randint(0,len(roll)-1)
        team.append(roll.pop(x))

    teams = teams + [team]

print(teams)
