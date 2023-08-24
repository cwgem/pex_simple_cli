import argparse

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--integer1", type=int, help="First Integer")
    parser.add_argument("--integer2", type=int, help="Second Integer")
    args = parser.parse_args()
    print(args.integer1 + args.integer2)