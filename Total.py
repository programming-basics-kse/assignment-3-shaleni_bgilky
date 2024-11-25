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


def total_make_csv(countries:dict):
    with open("total.csv","w") as file:
        writer = csv.DictWriter(file, fieldnames=["country", "gold", "silver", "bronze"])
        writer.writeheader()
        for country in countries.keys():
            writer.writerow({"country":country,
                             "gold":countries[country][0],
                             "silver":countries[country][1],
                             "bronze":countries[country][2]})


def total_print(countries:dict):

    if not countries:
        print("Are you sure there were olympic games that year?")
    else:
        for country in countries.keys():
            print(country + ": "
                  +"gold - " + str(countries[country][0]) + ",  "
                  +"silver - " + str(countries[country][1]) + ", "
                  +"bronze - " + str(countries[country][2]) + ".")
    print("\n",end="")


def total_results(countries: dict,filepath:str):
    with open(filepath,"at") as file:
        file.write("total function results:\n")
        if not countries:
            file.write("Are you sure there were olympic games that year?\n")
        else:
            for country in countries.keys():
                file.write(country + ": "
                      + "gold - " + str(countries[country][0]) + ",  "
                      + "silver - " + str(countries[country][1]) + ", "
                      + "bronze - " + str(countries[country][2]) + "."
                           +"\n")
        file.write("\n")

