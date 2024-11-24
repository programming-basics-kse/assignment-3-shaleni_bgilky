import csv
from argparse import ArgumentParser
def country_medals(filepath, country: str, key):
    country = country.title().strip() #makes 1 letter capital and others lower, skips symbols
    country_exists = False

    with open(f"{filepath}") as file:
        reader = csv.DictReader(file, delimiter="\t")
        country_medals : dict[str:list[int]]
        country_medals={}

        for line in reader:

            if line['Team']==country:

                country_exists = True
                if not line[key] in country_medals: # line['GAmes'] contains Year and Season
                    country_medals[line[key]]= [0] * 4

                if line["Medal"] == "Gold":
                    country_medals[line[key]][0] += 1
                elif line["Medal"] == "Silver":
                    country_medals[line[key]][1] += 1
                elif line["Medal"] == "Bronze":
                    country_medals[line[key]][2] += 1
                country_medals[line[key]][3]=sum(country_medals[line[key]][:-1])

        if not country_exists:
            return False

        #sort country_medals by year
        #country_medals_sort = dict(sorted(country_medals.items(), key=lambda x: int(x[0]), reverse=True))
        return country_medals #dict

def best_nd_worst(country: str, country_medals: dict[str:list[int]]):
    country = country.title()
    if not country_medals:
        return False
    best_rezult, total_medals =0,0
    least_rezult = 100000
    least_score, best_score,  = {}, {}

    for games in country_medals: #year is str type
        #year = games.split()[0]
        total_medals += country_medals[games][3] # to find if there has been none medals at all

        if country_medals[games][3]>best_rezult:
            best_score= {games : country_medals[games]}
            best_rezult = best_score[games][3]

        if country_medals[games][3]<least_rezult:
            least_score={games : country_medals[games]}
            least_rezult = least_score[games][3]

    if not total_medals:
        return False

    return (best_score, least_score)

if __name__=='__main__':

    var = ArgumentParser('Olympics')
    var.add_argument('filepath', help='Filepath to the data.tsv')
    var.add_argument('-o', '--overall', nargs='*', help='Info on coutry\'s/team\'s medals for specific olympics.')
    args = var.parse_args(['Olympic Athletes - athlete_events.tsv', '--overall', 'Ukraine'])
    filepath = args.filepath

    if args.overall:
        for country in args.overall:
            a = country_medals(filepath, country, 'Year')
            print(f'Your dict is: {a} \n')
            if not a:
                print(f'Make sure you entered correct country/team, and it participated in the olympics.')
                continue
            b = best_nd_worst(country, a)
            if not b:
                print(f'{country} gained no medals.')
            else:
                print(b[0])


