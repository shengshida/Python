import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name",type=str,default="阿达")
parser.add_argument("--message",type=str,default="早上好")

argv = parser.parse_args()

print(argv.name + argv.message)
#argpares 未接入到参数时使用默认参数
#.py --command 1