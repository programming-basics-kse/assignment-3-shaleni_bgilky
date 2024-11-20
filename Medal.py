import csv

#how should NOC be done, it doesn't correspond to countries properly
def medal_sort(filepath,country,year):
    gold = []
    silver = []
    bronze = []
    #maybe for some extra part of assignment
    #just participants
    #participants = []
    with open(f"{filepath}") as file :
        is_in_data = False
        reader = csv.DictReader(file,delimiter="\t")
        for line in reader :
            line: dict
            if country in line["Team"] and line["Year"] == year: #line["Team"] == country
                is_in_data = True
                if line["Medal"] == "Gold":
                    gold.append([line["Name"],line["Event"],line["Medal"]])
                elif line["Medal"] == "Silver":
                    silver.append([line["Name"],line["Event"],line["Medal"]])
                elif line["Medal"] == "Bronze":
                    bronze.append([line["Name"],line["Event"],line["Medal"]])
                # else :
                #     participants.append([line["Name"],line["Event"])
        if is_in_data and (gold or silver or bronze) :
            return gold,silver,bronze
        else:
            return is_in_data


def medal_results(medalists):

    medalists : list[[],[],[]] or bool

    if type(medalists) == bool :
        if medalists:
            return "Unfortunately this country didn't win anything that year"
        else:
            return "Please, make sure you entered real country and there was in fact olympic games that year"
    else:
        result = ""

        result += f"{len(medalists[0])} - gold\t"
        result += f"{len(medalists[1])} - silver\t"
        result += f"{len(medalists[2])} - bronze\t"

        all_medalists = []
        for i in medalists:
            all_medalists += i
        count = 0
        while count < 10 and count < len(all_medalists):
            result += f"{count + 1}. "
            for i in range(3):
                result += all_medalists[count][i]
                if i != 2:
                    result += " - "
            result += "\t"
            count += 1

        return  result
# maybe hte info in result could be stored some other way
# for i in medal_results(medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","1996")).split("\t"):
#    print(i)



