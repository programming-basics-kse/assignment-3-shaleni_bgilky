#Part of the code for taking in argument

from argparse import ArgumentParser
import os


var = ArgumentParser(prog='Olympics_dataset_analyzer')
var.add_argument('filepath', help ='Filepath to the data.tsv')
var.add_argument('-m','--medals',nargs=2, help ='Input two arguments: country and year. Shows top 10 medalists and total of each kind of medals(gold,silver,bronze)')
var.add_argument('-o','--output', metavar='filepath', help='Name of the file to save results to')

args = var.parse_args()

filepath = args.filepath
if args.medals :
    country = args.medals[0]
    country = country[0].upper()
    year = args.medals[1]
    if not year.isdecimal():
        raise Exception("After medal first argument is country and second is year. Year must be an integer.")

if not os.path.exists(filepath):
    raise Exception("Can't find this file")

if "tsv" not in filepath:
    raise Exception("This file is not a tsv, if you file is a tsv it must have a '.tsv' ending")












