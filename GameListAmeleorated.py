#list of games
TotalGameName = []

#edit list of games


#Sorts the list
TotalGameName.sort()

#Number of games
TotalGamesNum = len(TotalGameName)

#print number of games
print(f"Total games: {TotalGamesNum}")

#print list of games
for game in TotalGameName:
	print(f"\t{game.title()}")
print("------------------")

