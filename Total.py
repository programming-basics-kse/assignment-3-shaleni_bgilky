import csv

def total_sort(filepath,year:int):

    countries = {}

    with open(f"{filepath}") as file:
        reader = csv.DictReader(file, delimiter="\t")

        for line in reader:
            line: dict

            if line["Year"] == f"{year}" :

                if line["Team"] in countries : #different countries named USA-1 USA-2 should be counted as one?
                    gold = countries[line['Team']][0]
                    silver = countries[line['Team']][1]
                    bronze = countries[line['Team']][2]
                else :
                    gold = 0
                    silver = 0
                    bronze = 0

                if line["Medal"] == "Gold":
                    gold += 1
                elif line["Medal"] == "Silver":
                    silver += 1
                elif line["Medal"] == "Bronze":
                    bronze += 1

                if sum([gold,silver,bronze]):
                    countries[line['Team']] = [gold,silver,bronze]

    return countries


def total_results(countries:dict):

    if not countries:
        result = "Are you sure there were olympic games that year?"
    else:
        result = ""
        for country in countries.keys():
            result += country + ": "
            result += "gold - " + str(countries[country][0]) + ",  "
            result += "silver - " + str(countries[country][1]) + ", "
            result += "bronze - " + str(countries[country][2]) + "."
            result += "\n"

    return result

#print(total_results(total_sort("Olympic Athletes - athlete_events.tsv","1900")))

