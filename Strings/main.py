#Part 1

scorer_0 = "Ruud Gullit"  
scorer_1 = "Marco van Basten"  


goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(scorers)

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'

print(report)

#Part 2

player = "Frank Rijkaard"

first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[player.find(' '):]) - 1
print(last_name_len)

name_short = player[:player.find(' ')].upper()[:1] + '.' + player[player.find(' '):]
print(name_short)

chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')])).strip()
print(chant)

good_chant = chant[-1:] != ' '
print(good_chant)
