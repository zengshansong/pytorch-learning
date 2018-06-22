import argparse
import torch as th
parser = argparse.ArgumentParser()
parser.add_argument('--lr', type=float, default=0.0001, help='learning rate')
args = parser.parse_args()

def main():
    lr = args.lr
    x = th.randn(1, 10) 
    print x
if __name__ == "__main__":
    main()
