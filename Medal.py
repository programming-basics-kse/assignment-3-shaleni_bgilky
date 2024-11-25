import csv

#how should NOC be done, it doesn't correspond to countries properly
def medal_sort(filepath,country,year):

    gold = []
    silver = []
    bronze = []
    just_participants = []

    with open(filepath) as file :
        is_in_data = False
        reader = csv.DictReader(file,delimiter="\t")
        for line in reader :
            line: dict
            if country in line["Team"] and line["Year"] == year: #line["Team"] == country
                is_in_data = True
                if line["Medal"] == "Gold":
                    gold.append([line["Name"],line["Event"]])
                elif line["Medal"] == "Silver":
                    silver.append([line["Name"],line["Event"]])
                elif line["Medal"] == "Bronze":
                    bronze.append([line["Name"],line["Event"]])
                else :
                    just_participants.append([line["Name"],line["Event"]])

        if is_in_data and (gold or silver or bronze or just_participants) :
            return {"gold":gold,"silver":silver,"bronze":bronze,"N/A":just_participants}
        else:
            return is_in_data

def medal_print(medalists:dict):
    if type(medalists) == bool :
        if medalists:
            print("Unfortunately this country didn't win anything that year")
        else:
            print("Please, make sure you entered real country and there was in fact olympic games that year")
    else:
        for medal in medalists:
            print(len(medalists[medal] + " - " + medal))

        n_of_people = sum([len(medalists[medal]) for medal in medalists])
        n_just_participants = medalists["N/A"]
        print(round((n_just_participants / n_of_people) * 100) + "%" + " - just participated")
        all_medalists = medalists["gold"] + medalists["silver"] + medalists["bronze"]
        count = 0
        while count < 10 and count < len(all_medalists):
            print(f"{count + 1}. {all_medalists[0]} - {all_medalists[1]} - {all_medalists[2]}")
            count += 1


def medal_make_csv(medalists):
    with open("medal.csv","w") as file:
        writer = csv.DictWriter(file,fieldnames=["medal","name","event"])
        writer.writeheader()
        for medal in medalists:
            for person,event in medalists[medal]:
                writer.writerow({"medal":medal,"name":person,"event":event})


medal_make_csv(medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","2016"))
for i in medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","2016"):
    print(i,medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","2016")[i])
    print(len(medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","2016")[i]))
# def medal_results(medalists):
#
#     medalists : list[[],[],[]] or bool
#
#     if type(medalists) == bool :
#         if medalists:
#             return "Unfortunately this country didn't win anything that year"
#         else:
#             return "Please, make sure you entered real country and there was in fact olympic games that year"
#     else:
#         result = ""
#
#         result += f"{len(medalists[0])} - gold\n"
#         result += f"{len(medalists[1])} - silver\n"
#         result += f"{len(medalists[2])} - bronze\n"
#
#         all_medalists = []
#         for i in medalists:
#             all_medalists += i
#         count = 0
#         while count < 10 and count < len(all_medalists):
#             result += f"{count + 1}. "
#             for i in range(3):
#                 result += all_medalists[count][i]
#                 if i != 2:
#                     result += " - "
#             result += "\n"
#             count += 1
#
#         return  result
# maybe hte info in result could be stored some other way
# for i in medal_results(medal_sort("Olympic Athletes - athlete_events.tsv","Ukraine","1996")).split("\t"):
#    print(i)

# def medal_sort(filepath,country,year):
#     gold = []
#     silver = []
#     bronze = []
#     #just_participants = []
#     with open(f"{filepath}") as file :
#         is_in_data = False
#         reader = csv.DictReader(file,delimiter="\t")
#         for line in reader :
#             line: dict
#             if country in line["Team"] and line["Year"] == year: #line["Team"] == country
#                 is_in_data = True
#                 if line["Medal"] == "Gold":
#                     gold.append([line["Name"],line["Event"],line["Medal"]])
#                 elif line["Medal"] == "Silver":
#                     silver.append([line["Name"],line["Event"],line["Medal"]])
#                 elif line["Medal"] == "Bronze":
#                     bronze.append([line["Name"],line["Event"],line["Medal"]])
#                 #else :
#                     #just_participants.append([line["Name"],line["Event"]])
#                     #need to rewrite logic a lot if make participants
#         if is_in_data and (gold or silver or bronze) :
#             return gold,silver,bronze
#         else:
#             return is_in_data

# def medal_print(medalists):
#
#     medalists : list[[],[],[]] or bool
#
#     if type(medalists) == bool :
#         if medalists:
#             print("Unfortunately this country didn't win anything that year")
#         else:
#             print("Please, make sure you entered real country and there was in fact olympic games that year")
#     else:
#         print(f"{len(medalists[0])} - gold")
#         print(f"{len(medalists[1])} - silver")
#         print(f"{len(medalists[2])} - bronze")
#
#         all_medalists = medalists[0] + medalists[1] + medalists[2]
#         count = 0
#         while count < 10 and count < len(all_medalists):
#             print(f"{count + 1}. {all_medalists[0]} - {all_medalists[1]} - {all_medalists[2]}")
#             count += 1
