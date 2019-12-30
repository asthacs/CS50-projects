from cs50 import get_string
from sys import argv




def main():

    # TODO
    if len(argv)!=2:
        print("Usage: python bleep.py dictionary")
        exit(1)
    infile=argv[1]

    file= open(infile, "r")
    words=[]
    for line in file:
        words.append(line.rstrip ("\n"))
    file.close()

    s = get_string("What message would you like to censor?\n")


    arr=s.split()
    output=""
    j=0
    for eachword in arr:
        for i in range(len(words)):
            j=0
            if eachword.lower()==words[i]:
                x=len(eachword)
                output+= '*'*x + " "
                j=1
                break
        if j==0:
            output+= eachword + " "



    print(output)








if __name__ == "__main__":
    main()
