from argparse import ArgumentParser
import os
from Interactive import interactive, valid_choice
from Medal import medal_sort, medal_print, medal_results, medal_make_csv
from Overall import overall_print, overall_result
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

file_tsv = args.filepath.strip()

if not os.path.exists(file_tsv):
    raise Exception("Can't find tsv file")

if "tsv" not in file_tsv:
    raise Exception("This file is not a tsv, if you file is a tsv it must have a '.tsv' ending")


o_file = args.output.strip()
if o_file :
    if not os.path.exists(o_file) :
        raise Exception("Can't find file for output")


if args.medals :

    country = args.medals[0]
    country = country.title()
    year = args.medals[1]

    if not year.isdecimal():
        raise Exception("After medal first argument is country and second is year. Year must be an integer.")

    medals_dict = medal_sort(file_tsv,country,year)
    medal_print(medals_dict,country, year)


if args.total:

    year = args.total

    total_dict = total_sort(file_tsv,year)

    total_print(total_dict)


if args.overall:
    overall_print(file_tsv,args.overall)


if args.interactive:
    while True:
        country = input('\nEnter a country to get statistics about: ')
        print(interactive(file_tsv, country),'\n')
        answer = valid_choice(input("Do you want to continue?(Yes or No)\n>>> "))
        if not answer:
            break


if o_file:
    if args.medals :
        medal_results(medals_dict,o_file)
        if medals_dict:
            medal_make_csv(medals_dict)
            print("There is an additional 'medal.csv' file for further use")

    if args.total :
        total_results(total_dict,o_file)
        if total_dict:
            total_make_csv(total_dict)
            print("There is an additional 'total.csv' file for further use")

    if args.overall :
        overall_result(file_tsv,args.overall,o_file)

    if args.total or args.overall:
        print("will be rewritten with fresh info every usage")



congrats()















