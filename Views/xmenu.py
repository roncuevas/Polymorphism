import sys
from Controllers import xpersistency
from Utils import xutils


def main():
    while True:
        xutils.clear()
        menu()


if __name__ == "__main__":
    main()


def get_response(text, type_expected):
    answer = input(text + ": ")
    try:
        answer = type_expected(answer)
        return answer
    except ValueError:
        print("\tInvalid answer")
        get_response(text, type_expected)


def menu():
    print("------------ MENU -----------------")
    print("1. Mitomaster")
    print("2. FASTA polymorfism")
    print("3. dbSNP")
    print("4. Exit")
    answer = get_response("Select an option", int)
    if answer == 1:
        mitomaster()
    elif answer == 2:
        fasta()
    elif answer == 3:
        dbsnp()
    elif answer == 4:
        sys.exit()
    else:
        print("Invalid option")
        menu()


def mitomaster():
    index = 0
    print("------------ WELCOME TO MITOMASTER -----------------")
    haplo = xhaplo.Haplo()  # Creates an instance of Haplo class
    try:
        answer = get_response("Enter FASTA path or write exit to retun menu", str)
        if answer == "exit":
            return
        data = haplo.get_data(answer)  # Gets data from mitomaster uploading the sequences in fasta format
        print("------------------------------------- DATA -------------------------------------")
        print(data)
        data = haplo.convert_list(data)  # Converts data from text to list of lists
        mito_cvs(data)
    except:
        mitomaster()


def mito_cvs(data):
    print("------------------------------------- SAVE -------------------------------------")
    print("1. Save in csv")
    print("2. Dont save")
    answer = get_response("Select an option", int)
    if answer == 1:
        filename = get_response("Enter filename", str)
        xpersistency.write_csv(data, filename + ".csv")  # Writes data to csv file
    else:
        pass


def fasta():
    print("------------ WELCOME TO FASTA -----------------")



def dbsnp():
    pass
