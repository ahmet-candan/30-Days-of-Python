from argparse import ArgumentParser

parser = ArgumentParser(prog="hungry")
parser.add_argument('--user_id', type = int)

arg = parser.parse_args()

print(arg)
for i in range(1,5):
    print(arg.user_id)
    print(arg.user_id)
