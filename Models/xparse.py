from Required import xmltodict


# Converts XML to python Dictionary
def convert_xml(data_xml):
    return xmltodict.parse(data_xml)


# Gets list of SNPs IDs from the data response dictionary to a python list format
def get_snp_list(data):
    if data["eSearchResult"]["IdList"]['Id']:  # If there are SNPs
        return data["eSearchResult"]["IdList"]['Id']
    else:
        print("No SNPs found")
        return None


# Gets the first search (last in the list) SNP IDs from a list of SNPs IDs in python list format
def get_snp_last(list):
    length = len(list)
    if length == 0:
        print("No SNPs found")
        return None
    elif type(list) == str or type(list) == int:
        return list
    else:
        return list[length - 1]
