import sys

def main():
    print('Adaptive Command Line Interface - v.0.0.1')
    args = sys.argv[1:]
    for arg in args:
        print('passed argument :: {}'.format(arg))
    print('count of args :: {}'.format(len(args))) 

if __name__ == '__main__':
    main()