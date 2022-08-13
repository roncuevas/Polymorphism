from Controllers import xfasta, xpersistency, xmitomaster, xncbi
from Models import Polymorphism
from Models.Variant import Variant
from Models import *

fasta_filename = "diabetes.fasta"
filename = "haplo.csv"


def main():
    # data = xmitomaster.upload_fasta(fasta_filename)
    # data = xmitomaster.convert_list(data)
    # xpersistency.save_data(data, "datos.cc")
    data = xpersistency.load_data("datos.cc")
    data = xmitomaster.convert_dataframe(data)
    for index, row in data.iterrows():
        print(row.to_list())


def do_all():
    data = xmitomaster.do_all(
        fasta_filename)  # Uploads the fasta sequences to Mitomaster API and returns the data in Pandas DataFrame format
    xpersistency.write_pandas_to_csv(data, filename)  # Saves the data in csv format
    df = xpersistency.read_pandas_from_cvs(filename)
    sequencias = xfasta.do_all(fasta_filename)  # Reads a fasta file and returns a Pandas Dataframe with ID and sequence
    df = df.join(sequencias)
    xpersistency.write_pandas_to_csv(df, filename)
    print(df.describe())
    for index, row in df.iterrows():
        print(index)
        locations = xfasta.get_positions_from_string(row["locations"])
        data = xfasta.align(row["secuencias"],
                            locations)  # Aligns the sequence with the reference sequence and returns the data [position, reference, sequence]
        data = xfasta.polymorphism(data)
        print(data)
        for location in data:
            xncbi.ncbi(location)


if __name__ == '__main__':
    main()
