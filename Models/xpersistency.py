import pickle
import os
import csv


def save_data(obj, filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")


def remove_directory(dirname):
    if os.path.exists(dirname):
        os.rmdir(dirname)
    else:
        print("The directory does not exist")


def write_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def read_csv(filename):
    data = list()
    with open(filename) as file_in:
        reader = csv.reader(file_in)
        for row in reader:
            data.append(row)
    return data


def read_lines(filename):
    with open(filename) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    return lines


def read_nolines(filename):
    with open(filename) as file_in:
        lines = file_in.read().splitlines()
    return lines


def read_fasta(filename):
    data = read_nolines(filename)
    sequences = list()
    index = -1
    for line in data:
        if line.startswith(">"):
            index += 1
            sequences.append([line, ""])
        else:
            sequences[index][1] += line
    return sequences


def read_line(filename, line):
    with open(filename) as file_in:
        for i in range(line):
            file_in.readline()
            if i == line - 1:
                return file_in.readline()
