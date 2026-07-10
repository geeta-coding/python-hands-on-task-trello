import sre_parse

# # print("File Name : ",sys.argv[0]) 
# # print("Nmae : ",sys.argv[1])
# if len(sys.argv) < 2 :
#     print("please provide a arguments for that")
# else:
#     print("Name : ",sys.argv[1])
# parser = argparse.ArgumentParser(
#     description="Simple greeting program"
# )

parser.add_argument(
    "name",
    help="Enter your name"
)

parser.add_argument(
    "--age",
    help="Enter your age"
)

args = parser.parse_args()

print(args.name)

import argparse

parser = argparse.ArgumentParser(
    description="Simple Calculator"
)

parser.add_argument(
    "num1",
    type=float,
    help="First number"
)

parser.add_argument(
    "operator",
    help="Operator (+ - * /)"
)

parser.add_argument(
    "num2",
    type=float,
    help="Second number"
)

args = parser.parse_args()

if args.operator == "+":
    print(args.num1 + args.num2)

elif args.operator == "-":
    print(args.num1 - args.num2)

elif args.operator == "*":
    print(args.num1 * args.num2)

elif args.operator == "/":
    print(args.num1 / args.num2)

else:
    print("Invalid operator")