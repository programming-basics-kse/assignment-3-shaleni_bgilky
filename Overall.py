import csv


def is_noc(country : str): # to check if user entered NOC
    if len(country)!=3 or not country.isalpha():
        return False
    return True


def country_medals(filepath, country: str, key):
    # returns a dictionary with keys all games/years of the country
    # values are medals list with sum as 4ht element
    # medals =  sth like {'1998 Summer':[2, 5, 2, 9], '2016 Winter': [2, 6, 4, 12], ...}

    country_exists = False
    country = country.strip()

    if is_noc(country): # in case the user entered NOC as country
        country = country.upper() # NOC to upper
        filter = 'NOC'
    else:
        country = country.title()
        filter = 'Team' # just filter by country

    with open(f"{filepath}") as file:
        reader = csv.DictReader(file, delimiter="\t")
        medals_dict={}

        for line in reader:

            if country == line[filter]: # filter is 'Team' or 'NOC'

                country_exists = True
                if not line[key] in medals_dict: # line['Games'] contains Year and Season
                    medals_dict[line[key]]= [0] * 4

                if line["Medal"] == "Gold":
                    medals_dict[line[key]][0] += 1
                elif line["Medal"] == "Silver":
                    medals_dict[line[key]][1] += 1
                elif line["Medal"] == "Bronze":
                    medals_dict[line[key]][2] += 1
                medals_dict[line[key]][3]=sum(medals_dict[line[key]][:-1])#maybe you don't need to recount it every cycle

        if not country_exists:
            return False

        return medals_dict


def best_nd_worst(medals_dict): # returns two dict - best and worst results
    if not medals_dict:
        return False
    best_result, total_medals =0,0
    least_result = 100000
    least_score, best_score,  = {}, {}

    for games in medals_dict:
        total_medals += medals_dict[games][3] # to find if there has been none medals at all

        if medals_dict[games][3]>best_result:
            best_score= {games : medals_dict[games]} #e.g. {'2012 Winter' : [3, 2, 5, 10]}
            best_result = best_score[games][3] # the total amount of medals for this result

        if medals_dict[games][3]<least_result:
            least_score={games : medals_dict[games]}
            least_result = least_score[games][3]

    if not total_medals:
        return False # no medals

    return (best_score, least_score)


def overall_print(filepath,countries):
    for country in countries:
        a = country_medals(filepath, country, 'Year')
        country = country.strip().title()
        if not a:
            print(
                f'{country} not in data. Make sure you entered correct country/team, and it participated in the olympics.')
            continue

        b = best_nd_worst(a)
        if not b:
            print(f'{country} gained no medals.')
        else:
            best_result = b[0]
            for year in best_result:
                print(f"{country}'s best result was in {year}")
                print(
                    f"{best_result[year][0]} - gold, {best_result[year][1]} - silver, {best_result[year][2]} - bronze")


def overall_result(filepath,countries,output_filepath):
    with open(output_filepath,"at") as file:
        file.write("Overall function results: \n")
        for country in countries:
            a = country_medals(filepath, country, 'Year')
            country = country.strip().title()
            if not a:
                file.write(f'{country} not in data. Make sure you entered correct country/team, and it participated in the olympics.\n')
                continue

            b = best_nd_worst(a)
            if not b:
                file.write(f'{country} gained no medals.\n')
            else:
                best_result = b[0]
                for year in best_result:
                    file.write(f"{country}'s best result was in {year}\n")
                    file.write(f"{best_result[year][0]} - gold, {best_result[year][1]} - silver, {best_result[year][2]} - bronze\n")

        file.write("\n")