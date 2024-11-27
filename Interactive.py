import csv
from Overall import country_medals
from Overall import best_nd_worst
from math import ceil

def valid_choice(choice):
    choice = choice.lower()
    while True:
        if choice == "no":
            return False
        elif choice == "yes":
            return True
        choice = input("(Yes or No)Try again\n>>> ")

def find_venue(filepath,games):
    with open(f"{filepath}", 'r') as file:
        reader = csv.DictReader(file, delimiter="\t")
        for line in reader:
            if line['Games'] == games:
                return line['City']

def find_average(games_dict):
    golds, silvers, bronzes = 0, 0, 0  # to find average medals amount
    for key in games_dict:
        golds += games_dict[key][0]
        silvers += games_dict[key][1]
        bronzes += games_dict[key][2]
    golds = ceil(golds / len(games_dict))  # average for each type of medal
    silvers = ceil(silvers / len(games_dict))
    bronzes = ceil(bronzes / len(games_dict))
    return golds,silvers,bronzes

def find_first_games(games_dict):
    # sorts medals by participation time, winter is before summer if year is the same
    for_sort = ['Winter', 'Summer']
    country_medals_sort = dict(
        sorted(games_dict.items(), key=lambda x: int(x[0].split()[0]) + for_sort.index(x[0].split()[1])))
    first_games = list(country_medals_sort.keys())[0] # the first games in format '2012 Summer'
    return first_games

def interactive(filepath, country):
    medals = country_medals(filepath, country, 'Games')
    if medals:
        country = country.title().strip()

        first_games = find_first_games(medals)

        venue = find_venue(filepath,first_games)

        extremes = best_nd_worst(medals)  # best and worst results dictionaries by amounts of medals in tuple
        '''don't print year if there are same results???'''
        best_games = [i for i in extremes[0]][0]# get the games
        best_res = extremes[0][best_games][3] # get the total result
        worst_games = [i for i in extremes[1]][0]
        worst_res = extremes[1][worst_games][3]

        golds, silvers, bronzes = find_average(medals)

        ans = f'Country: {country}\nFirst olympics: {first_games}, {venue}\nBest score: {best_games}, '\
        f'medals: {best_res}\nWorst score: {worst_games}, medals: {worst_res}\n'\
        f'Average medals: Gold: {golds}, Silver: {silvers}, Bronze: {bronzes}'

    else:
        ans = f'Country {country} not found. Make sure you entered correct country/team, and it participated in the olympics.'
    with open ('interactive_answer.tsv', 'w') as ans_file: #writing function output into a file
        ans_file.write(str(ans))
    return ans
