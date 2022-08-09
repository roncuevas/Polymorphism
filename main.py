from Models import xconection, xhaplo, xparse, xpersistency, xfasta

from Views import xmenu
fastafilename = "diabetes.fasta"

def main():
    final = {}
    haplo = xhaplo.Haplo()  # Creates an instance of Haplo class
    haplo_data = haplo.do_all(fastafilename)  # Data in list of list format
    xpersistency.write_csv(haplo_data, "haplo.csv")  # Writes data in csv format
    haplo_data = haplo.convert_dictionary(haplo_data)  # Converts data from list of list format to dictionary format
    positions = [] # List of positions
    for key in haplo_data:
        positions.append(get_positions(haplo_data, key))
    print(positions)
    fasta_data = xpersistency.read_fasta(fastafilename)
    print(fasta_data)
    fasta_data = xfasta.fasta_to_dictionary(fasta_data)
    print(fasta_data)
    final = haplo_data.copy()
    for key in final:
        print(key)
        final[key].append(fasta_data[key])
        print(final[key])
        print(type(final[key]))



    #secuencia = xfasta.get_sequence(diabetes[0])

    # # xmenu.main()
    # diabetes = xpersistency.read_fasta("diabetes.fasta")
    # print(diabetes)
    # secuencia = xfasta.get_sequence(diabetes[0])
    # print(len(secuencia))
    # haplo = xhaplo.Haplo()
    # # data = haplo.get_data("diabetes.fasta")
    # # data = haplo.convert_list(data)
    #
    # # xpersistency.save_data(data, "datos.cc")  # Saves data in a file
    #
    # # data = xpersistency.load_data("datos.cc")  # Loads data from a file
    # # print(data)
    # # data = haplo.convert_list(data)  # Converts data from text to list of lists
    # # print(data)
    # # # xpersistency.write_csv(data, "datos.csv")  # Writes data to csv file
    # data = xpersistency.read_csv("datos.csv")  # Reads data from csv file
    # data = haplo.convert_dictionary(data)  # Converts the response data from string to python dictionary format
    # positions = get_positions(data, "JF717097.1")  # Gets the positions of the polymorphisms from the dictionary key
    # print(positions)
    # data = xfasta.align(secuencia, positions)  # Aligns the sequence with the reference sequence and returns the data [position, reference, sequence]
    # # print("ALINEAMIGNTO: "+ str(data))
    # xd = xfasta.polymorphism(data)
    # print(xd)



def get_positions(dictionary, key):
    positions = []
    value = ""
    for char in dictionary[key][2]:
        if char != "-" and char != ";":
            value += char
        elif char == "-":
            positions.append([int(value), ""])
            value = ""
        elif char == ";":
            positions[len(positions) - 1][1] = int(value)
            value = ""
        else:
            print("Foreign character")
    return positions



def ncbi():
    data = xconection.do_all("16093")  # Data in xml format by a polymorphism found in ___ position

    data = xparse.convert_xml(data)  # Converts data from xml to python dictionary format

    # Prints SNPs IDs
    snps = xparse.get_snp_list(data)  # List of SNPs IDs from the response in python dictionary format
    snp = xparse.get_snp_last(snps)  # Selects the first SNP ID from dbSNP
    print(snp)  # Prints the first SNP ID from dbSNP


if __name__ == '__main__':
    main()
