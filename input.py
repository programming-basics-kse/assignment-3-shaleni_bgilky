from argparse import ArgumentParser
import os
from Medal import medal_results, medal_sort

var = ArgumentParser(prog='Olympics_dataset_analyzer')
var.add_argument('filepath', help ='Filepath to the data.tsv')
var.add_argument('-m','--medals',nargs=2, help ='Input two arguments: country and year. Shows top 10 medalists and total of each kind of medals(gold,silver,bronze)')
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


if args.medals :

    country = args.medals[0]
    country = country[0].upper()
    year = args.medals[1]

    if not year.isdecimal():
        raise Exception("After medal first argument is country and second is year. Year must be an integer.")

    medal = medal_results(medal_sort(file_tsv,country,year))

    print(medal)


if o_file:
    with open(o_file,"w") as file:
        if args.medals :
            file.write(medal)
















