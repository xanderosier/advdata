import urllib2, requests
from bs4 import BeautifulSoup

########## YOUR CODE GOES HERE ##########

def get_html(ward):

    url = 'http://www.chicagoelections.com/en/pctlevel3.asp?Ward=1&elec_code=9&race_number=10'

      # Put the correct URL here

    html = requests.get(url).content

    return html # Leave this line here. Just be sure to call your variable html.

def get_table(html):
    
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('tbody', {'id': 'AutoNumber1'})
    row_list = table.find_all('tr')

    for row in row_list:

        cell_list = row.find_all('tr')

        data = [cell.text for cell in cell_list]

        print data

 # Write your code here

    return table # Leave this line here. Just be sure to call your variable table.