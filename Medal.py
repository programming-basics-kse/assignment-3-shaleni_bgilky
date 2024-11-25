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
            return {"gold":gold,"silver":silver,"bronze":bronze,"NA":just_participants}
        else:
            return is_in_data

def medal_print(medalists:dict):
    if type(medalists) == bool :
        if medalists:
            print("Unfortunately this country didn't win anything that year")
        else:
            print("Please, make sure you entered real country and there was in fact olympic games that year")
    else:
        print(f"{len(medalists["gold"])} - gold")
        print(f"{len(medalists["silver"])} - silver")
        print(f"{len(medalists["bronze"])} - bronze")
        print(f"{len(medalists["NA"])} - just participated")

        n_of_people = sum([len(medalists[medal]) for medal in medalists])
        n_just_participants = len(medalists["NA"])
        print(str(round((n_just_participants / n_of_people) * 100)) + "%" + " - just participated")

        all_medalists = medalists["gold"] + medalists["silver"] + medalists["bronze"]
        count = 0
        while count < 10 and count < len(all_medalists):
            print(f"{count + 1}.",end="")
            print(*all_medalists[count])
            count += 1
        print("\n",end="")


def medal_make_csv(medalists):
    with open("medal.csv","w") as file:
        writer = csv.DictWriter(file,fieldnames=["medal","name","event"])
        writer.writeheader()
        for medal in medalists:
            for person,event in medalists[medal]:
                writer.writerow({"medal":medal,"name":person,"event":event})


def medal_results(medalists, filepath):
    with open(filepath,"at") as file:
        file.write("medal function results:\n")
        if type(medalists) == bool :
            if medalists:
                file.write("Unfortunately this country didn't win anything that year")
            else:
                file.write("Please, make sure you entered real country and there was in fact olympic games that year")
        else:
            file.write(f"{len(medalists["gold"])} - gold"+"\n")
            file.write(f"{len(medalists["silver"])} - silver"+"\n")
            file.write(f"{len(medalists["bronze"])} - bronze"+"\n")
            file.write(f"{len(medalists["NA"])} - just participated"+"\n")

            n_of_people = sum([len(medalists[medal]) for medal in medalists])
            n_just_participants = len(medalists["NA"])
            file.write(str(round((n_just_participants / n_of_people) * 100)) + "%" + " - just participated"+"\n")

            all_medalists = medalists["gold"] + medalists["silver"] + medalists["bronze"]
            count = 0
            while count < 10 and count < len(all_medalists):
                file.write(f"{count + 1}. ",)
                file.write(f"{all_medalists[count][0]} - {all_medalists[count][1]}")
                file.write("\n")
                count += 1
            file.write("\n")
