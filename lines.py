import sys

def main():
    i = 0
    try:
        check_argv()
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        count = 0
        for line in lines:
            if remove_things(line) == False:
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File not found ")






def check_argv():
    if len(sys.argv) > 2:
        sys.exit("Too many commands line arguments ")

    elif len(sys.argv) <= 1:
        sys.exit("Too few commands line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file. ")

def remove_things(word):
    if word.isspace():
        return True
    elif word.lstrip().startswith("#"):
        return True
    else:
        return False

      
if __name__ == "__main__":
    main()
