#given 60 roll no , divide each into 5 groups by random ways
import random
m = int(input("Enter starting roll no: "))
n = int(input("Enter ending roll no: "))
i = int(input("Enter no of persons in each group:  "))

roll = [x for x in  range(m,n+1)]
teams = []

while roll:
    team = []
    while len(team) < i and len(roll) > 0:
        x = random.randint(0,len(roll)-1)
        team.append(roll.pop(x))

    teams = teams + [team]

print(teams)
