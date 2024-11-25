from argparse import ArgumentParser
import os

from Interactive import interactive, valid_choice
#from Medal import medal_results, medal_sort
from Overall import best_nd_worst, country_medals
from Total import total_results, total_sort, total_print, total_make_csv
from congrats import congrats

var = ArgumentParser(prog='Olympics_dataset_analyzer')
var.add_argument('filepath', help ='Filepath to the data.tsv')
var.add_argument('-m','--medals',nargs=2, help ='Input two arguments: country and year. Shows top 10 medalists and total of each kind of medals(gold,silver,bronze)')
var.add_argument('-t','--total', type=int, metavar='year', help = 'Year of some olympic games')
var.add_argument('-oa', '--overall', nargs='*', help='Info on coutry\'s/team\'s medals for specific olympics.')
var.add_argument('-i','--interactive', action = 'store_true',help ='Info on country\'s/team\'s medals for specific olympics.')
var.add_argument('-o','--output', metavar='filepath', help='Name of the file to save results to')

args = var.parse_args()

file_tsv = args.filepath

if not os.path.exists(file_tsv):
    raise Exception("Can't find tsv file")

if "tsv" not in file_tsv:
    raise Exception("This file is not a tsv, if you file is a tsv it must have a '.tsv' ending")


o_file = args.output
if o_file :
    if not os.path.exists(o_file) :
        raise Exception("Can't find file for output")


# if args.medals :
#
#     country = args.medals[0]
#     country = country[0].upper()
#     year = args.medals[1]
#
#     if not year.isdecimal():
#         raise Exception("After medal first argument is country and second is year. Year must be an integer.")
#
#     medal = medal_results(medal_sort(file_tsv,country,year))
#     print(medal)


if args.total:

    year = args.total

    total_dict = total_sort(file_tsv,year)

    total_print(total_dict)


if args.overall:
    for country in args.overall:
        a = country_medals(file_tsv, country, 'Year')
        country = country.strip().title()
        if not a:
            print(f'{country} not in data. Make sure you entered correct country/team, and it participated in the olympics.')
            continue

        b = best_nd_worst(country, a)
        if not b:
            print(f'{country} gained no medals.')
        else:
            best_result = b[0]
            for year in best_result:
                print(f"{country}'s best result was in {year}")
                print(f"{best_result[year][0]} - gold, {best_result[year][1]} - silver, {best_result[year][2]} - bronze")


if args.interactive:
    while True:
        country = input('\nEnter a country to get statistics about: ')
        print(interactive(file_tsv, country),'\n')
        answer = valid_choice(input("Do you want to continue?(Yes or No)\n>>> "))
        if not answer:
            break


if o_file:
    with open(o_file,"w") as file:

        # if args.medals :
        #     file.write("medal function results:\n\n")
        #     file.write(medal+"\n")

        if args.total :
            total_results(total_dict,o_file)
            if total_dict:
                total_make_csv(total_dict)
                print("There is an additional 'total.csv' file for further use\nit will be rewritten with fresh info every usage")


congrats()















