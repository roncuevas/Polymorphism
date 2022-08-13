import time
from Controllers import xconection, xparse


def ncbi(variant_location):
    variant_location = str(variant_location)
    data = xconection.do_all(variant_location)  # Data in xml format by a polymorphism found in ___ position

    data = xparse.convert_xml(data)  # Converts data from xml to python dictionary format

    # Prints SNPs IDs
    snps = xparse.get_snp_list(data)  # List of SNPs IDs from the response in python dictionary format
    snp = xparse.get_snp_last(snps)  # Selects the first SNP ID from dbSNP
    print(snp)  # Prints the first SNP ID from dbSNP
    time.sleep(4)