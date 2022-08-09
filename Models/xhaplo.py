import requests
import os


# seqid	label	locations	haplogroup	verbose_haplogroup	variant_cnt	variants

class Haplo:
    _response = None

    def __init__(self):
        pass

    # Data in list of list format
    def do_all(self, filename):
        data = self.get_haplo(filename) # Gets data from mitomaster uploading the sequences in fasta format
        data = self.convert_list(data)  # Converts data from text to list of lists
        return data


    def get_haplo(self, filename):
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


    def convert_list(self, response):
        data = list()  # Creates a list of lists
        long = response.split('\n')  # Splits the response by lines
        for short in long:
            if not (short == ""):  # If the line is not empty
                data.append(list(short.split('\t')))  # Splits the lines by tabs and saves into the dara
            else:
                pass
        return data

    def get_labels(self, data):
        labels = list()  # Creates a list of labels
        for label in data:
            labels.append(label[1])  # Gets the labels from the data
        return labels

    def convert_dictionary(self, data):
        del data[0]  # Removes the headers
        labels = self.get_labels(data)  # Gets the labels of the data
        return dict(zip(labels, data))

    def convert_group(self, data):
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
