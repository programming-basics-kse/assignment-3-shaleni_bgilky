import csv
from argparse import ArgumentParser
from Overall import country_medals
from Overall import best_nd_worst
from math import ceil

def interactive(filepath, country):
    '''finish validation'''
    medals = country_medals(filepath, country, 'Games') # dict off all games of the country with years keys, values are medals numbers
    if medals:
        country = country.title().strip()
        # sorts medals by participation time, winter is before summer if year is the same
        for_sort = ['Winter', 'Summer']
        country_medals_sort = dict(sorted(medals.items(), key=lambda x: int(x[0].split()[0]) + for_sort.index(x[0].split()[1])))
        first_games = list(country_medals_sort.keys())[0] # the first games in format '2012 Summer'

        venue = ''
        with open (f"{filepath}", 'r') as file:
            reader = csv.DictReader(file, delimiter="\t")
            for line in reader:
                if line['Games']==first_games:
                    venue+=line['City']
                    break

        extremes = best_nd_worst(country, medals)# best and worst results dictionaries by amounts of medals in tuple
        '''don't print year if there are same results???'''
        best_games = [i for i in extremes[0]][0] # get the games
        best_res = extremes[0][best_games][3] # get the total result
        worst_games = [i for i in extremes[1]][0]
        worst_res = extremes[1][worst_games][3]

        golds, silvers, bronzes =0,0,0 # to find average medals amount
        for key in medals:
            golds+=medals[key][0]
            silvers += medals[key][1]
            bronzes += medals[key][2]
        golds=ceil(golds/len(medals)) # average for each type of medal
        silvers = ceil(silvers / len(medals))
        bronzes = ceil(bronzes / len(medals))

        ans = f'Country: {country}\nFirst olympics: {first_games}, {venue}\nBest score: {best_games}, '\
        f'medals: {best_res}\nWorst score: {worst_games}, medals: {worst_res}\n'\
        f'Average medals: Gold: {golds}, Silver: {silvers}, Bronze: {bronzes}'

    else:
        ans = f'Country {country} not found. Make sure you entered correct country/team, and it participated in the olympics.'
    with open ('interactive_answer.tsv', 'w') as ans_file: #writing function output into a file
        ans_file.write(str(ans))
    return ans

var = ArgumentParser('Olympics')
var.add_argument('filepath', help ='Filepath to the data.tsv')
var.add_argument('-i','--interactive', action = 'store_true',
                 help ='Info on country\'s/team\'s medals for specific olympics.') #False if the argument is not specified, true otherwise
args = var.parse_args(['Olympic Athletes - athlete_events.tsv', '--interactive'])
filepath = args.filepath
if args.interactive:
    while True:
        country = input('\nEnter a country to get statistics about: ')
        print(interactive(filepath, country),'\n')
        '''how to stop this command when the user enters another like --medals?'''
print(args)