import requests
import os
import pandas as pd


# seqid
# label
# locations
# haplogroup
# verbose_haplogroup
# variant_cnt
# variants


# Uploads the fasta sequences to Mitomaster API and returns the data in Pandas DataFrame format
def do_all(filename):
    data = upload_fasta(filename)  # Gets data from Mitomaster uploading the sequences in fasta format
    data = convert_list(data)  # Converts data from text to list of lists
    data = convert_dataframe(data)  # Converts the response data from string to python dictionary format
    return data


def upload_fasta(filename):
    if os.path.exists(filename):
        try:
            _response = requests.post("https://mitomap.org/mitomaster/websrvc.cgi",
                                      files={"file": open(filename), 'fileType': ('', 'sequences'),
                                             'output': ('', 'summary')})  # detail, summary and hsd
            return str(_response.content, 'utf-8')
        except requests.exceptions.HTTPError as err:
            print("HTTP error: " + err)
            pass
        except:
            print("Error with getting data from Mitomaster")
            pass
    else:
        print("The file does not exist")


def convert_list(response):
    data = list()  # Creates a list of lists
    long = response.split('\n')  # Splits the response by lines
    for short in long:
        if not (short == ""):  # If the line is not empty
            data.append(list(short.split('\t')))  # Splits the lines by tabs and saves into the dara
        else:
            pass
    return data


def get_labels(data):
    labels = list()  # Creates a list of labels
    for label in data:
        labels.append(label[1])  # Gets the labels from the data
    return labels


def convert_dictionary(data):
    del data[0]  # Removes the headers
    labels = get_labels(data)  # Gets the labels of the data
    return dict(zip(labels, data))


# Gets the text response from Mitomaster and return a Dataframe labeled with index and columns
def convert_dataframe(data):
    headers = data[0].copy()  # Creates a copy of the headers
    del data[0]  # Removes the headers from the data
    labels = get_labels(data)  # Gets the labels of the data
    return pd.DataFrame(data, index=labels, columns=headers)


def convert_group(data):
    ordered = []
    for i in range(0, 7):
        ordered.append(list())

    for long in data:
        index = 0
        for short in long:
            if not (short == ""):
                ordered[index].append(short)
                index += 1
            else:
                pass
