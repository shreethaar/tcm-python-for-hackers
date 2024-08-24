import argparse
parser=argparse.ArgumentParser(description="Example Python CLI")
parser.add_argument("hacker_name",help="Enter the hacker name", type=str)
parser.add_argument("hacker_power",help="Enter the hacker power",type=int)
parser.add_argument("-bh","--blackhat",default=False,action="store_true")
#parser.add_argument("-bh","--blackhat",required=True,default=False,action="store_true")
parser.add_argument("-wh","--whitehat",default=True,action="store_false")
parser.add_argument("-ht","--hackertype",choices=["whitehat","blackhat","greyhat"])

args=parser.parse_args()
print(args)

print(args.hacker_name)

if args.blackhat:
    hacker_type="blackhat"
elif args.whitehat:
    hacker_type="whitehat"
else:
    hacker_type="unknown"

print("{} is a {} type of hacker".format(args.hacker_name,hacker_type))


