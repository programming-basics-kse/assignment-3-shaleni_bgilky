# var.add_argument('--interactive', type=str, help ='Statistics of a given country (the first and the most successful olympics)')
import csv
from argparse import ArgumentParser
#from Medal import medal_sort
var = ArgumentParser('Olympics')
var.add_argument('filepath', help ='Filepath to the data.tsv')
var.add_argument('-o','--overall', nargs='*',help ='Info on coutry\'s/team\'s medals for specific olympics.')
args = var.parse_args(['Olympic Athletes - athlete_events.tsv', '--overall', 'West Germany'])
filepath = args.filepath

def overall(filepath, country):

    country_exists = False
    with open(f"{filepath}") as file:
        reader = csv.DictReader(file, delimiter="\t")
        country_medals : dict[str:list[int]]
        country_medals={}

        for line in reader:

            if line['Team']==country:

                country_exists = True
                if not line['Year'] in country_medals:
                    country_medals[line['Year']]= [0] * 4

                if line["Medal"] == "Gold":
                    country_medals[line['Year']][0] += 1
                elif line["Medal"] == "Silver":
                    country_medals[line['Year']][1] += 1
                elif line["Medal"] == "Bronze":
                    country_medals[line['Year']][2] += 1
                country_medals[line['Year']][3]=sum(country_medals[line['Year']][:-1])
        if not country_exists:
            return f'Make sure you entered correct country/team and it participated in the olympics.'

        best_score =0
        total_medals=0
        for year in country_medals: # str type
            total_medals += country_medals[year][3] # to find if there has been none medals at all
            if country_medals[year][3]>best_score:
                best_score=country_medals[year][3] # best sum of medals
                ans = country_medals[year]
                best_year=year
        if not total_medals:
            return f'{country} gained no medals.'

    return f'{country} gained the most medals in {best_year}: {ans[3]} ({ans[0]} gold, {ans[1]} silver and {ans[2]} bronze).'


if args.overall:
    for country in args.overall:
        print(overall(filepath,country))
'''years_dict = {}
with open(f"{filepath}") as file :
    reader = csv.DictReader(file,delimiter="\t")
    for line in reader :
        if line['Year'] not in years_dict:
            years_dict[line['Year']]={}
    for line in reader:
        if line['Team'] not in years_dict[line['Year']]:
            years_dict[line['Year']]+={line['Team'] : [medal_sort(filepath, line['Team'], line['Year'])]}
print(years_dict)'''


