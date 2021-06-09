import argparse

runtimeDesc = 'Adaptive CLI --v.0.0.2--'
messDesc = 'will eventually send message'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=runtimeDesc)
    parser.add_argument('-m', '--message', help=messDesc)
    args = parser.parse_args()
