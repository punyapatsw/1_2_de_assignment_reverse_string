from reverse_string import reverse_string
import sys

def main(argv):
    print(reverse_string(list((argv[0]))))
    print(reverse_string(['a','b','c']))
    print(reverse_string(['1','2','3','4']))
    print(reverse_string(['a','b','c','d']))

if __name__=='__main__':
    main(sys.argv[1:])

