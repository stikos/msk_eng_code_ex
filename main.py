#!/usr/bin/python3
"""
File:       main.py
Desc:       Main gene search tool component, entry point

A simple CLI that prompts the user to input a gene name, then executes the
necessary API calls and prints the required information in the appropriate
format. The main assumption here is that the user knows beforehand exactly
the name of the gene they're looking information for. GeneNetwork API does
not provide a way to retrieve a full list of all 50K+ genes available,
in order for the user to be able to locally parse them and select. A more
complex solution, for example involving a scraper (Scrapy) could display the
available choices online, as the user would be typing (would also
ideally require a GUI).

- Potential improvements:
    - Configparser: for additional code modularization and better
    organization. API endpoints and various parameters could be defined in a
    config file.
"""
__author__ = "Konstantinos Liosis"
__copyright__ = "Copyright 2021"
__credits__ = "Konstantinos Liosis"
__license__ = None
__version__ = "1.0.0"
__maintainer__ = "Konstantinos Liosis"
__email__ = "konstantinos.liosis@ucalgary.ca"
__status__ = "Development"

from utilities import *


if __name__ == "__main__":
    print("--- Gene Info Viewer ---")

    # An infinite loop for continuous gene searches. Ctrl+C will
    # terminate the program.
    while True:
        # Gene Network endpoint URL generation
        gene_name = input("Please type the name of a gene (Ctrl+C to exit): ")
        gene_network_endpoint = f'https://www.genenetwork.nl/api/v1/gene/' \
                                f'{gene_name}'
        gene_net_req = exec_req(gene_network_endpoint)
        if gene_net_req is None:
            continue
        else:
            # ENSEMBL API endpoint URL generation
            ensembl_id = gene_net_req["gene"]["id"]
            ensembl_endpoint = f'https://rest.ensembl.org/lookup/id/' \
                               f'{ensembl_id}?content-type=application/' \
                               f'json;expand=1'
            ensembl_req = exec_req(ensembl_endpoint)
            if ensembl_req is None:
                continue
            else:
                # Print the information in exact accordance to the problem
                # description
                transcripts = get_transcripts(ensembl_req["Transcript"])
                print(f'Gene Name: {gene_name}\n'
                      f'Ensembl ID: {ensembl_id}\n'
                      f'Species: '
                      f'{ensembl_req["species"].replace("_", " ").title()}\n'
                      f'Assembly: {ensembl_req["assembly_name"]}\n'
                      f'Sequence Region Name: '
                      f'{ensembl_req["seq_region_name"]}\n'
                      f'Description: {ensembl_req["description"]}\n'
                      f'Transcripts:\n')

                # A for loop necessary to properly format the transcript info
                for trans in transcripts:
                    if trans[2] == 1:
                        trans[1] = str(trans[1]) + " <--"
                    print("\t\t" + trans[0] + "\t " + str(trans[1]) + "\n")
