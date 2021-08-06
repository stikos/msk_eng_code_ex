# Engineering Coding Exercise
## Papaemmanuil Lab - Memorial Sloan Kettering, Aug 2021.
### Gene Info Viewer

A simple CLI that prompts the user to input a gene name, then executes the
necessary API calls and prints the required information in the appropriate
format. The main assumption here is that the user knows beforehand exactly
the name of the gene they're looking information for. GeneNetwork API does
not provide a way to retrieve a full list of all 50K+ genes available,
in order for the user to be able to locally parse them and select. A more
complex solution, for example involving a scraper (Scrapy) could display the
available choices online, as the user would be typing (would also
ideally require a GUI).

#### Execution instructions:
The user simply needs to execute the `main.py` module (*Python3.7*). The
 only non-native python package required is `requests`. The necessary
  `requirements.txt` file is available in the repo, hence the usual `pip
   install -r requirements.txt` would install the one and only dependency.
 
#### Public access:
In order to make the tool available to a broader audience, a Github repo was
 created including all the necessary files.

#####  Author: Konstantinos Liosis

