import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

class HTMLTableParser:
    
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #table_div = soup.find('div' , {'class': 'field__items'})
        a = soup.find_all('table')
        a = self.parse_html_table(a)
        #a = [self.parse_html_table(table) for table in soup.find('table')]
        print(a)
        exit()
        return a
        #return [(table['id'],self.parse_html_table(table)) for table in soup.find('table')]  

    def parse_html_table(self, table):
        #print(table)
        names = []
        marks = []
        for row in table[0].find_all('tr'):
            #print(row)
            td_tags = row.find_all('td')
            name_td = td_tags[0]
            marks_td = td_tags[1]
            names.append(name_td.get_text())
            marks.append(marks_td.get_text())
        
        names = np.array(names, dtype='str')
        marks = np.array(marks, dtype='str')
        #print(names)
        #print(marks)
        df = pd.DataFrame(list(zip(names,marks)))
        return df[1:]

        
if __name__ == '__main__':
    hp = HTMLTableParser()
    table = hp.parse_url("https://pk.cs.msu.ru/node/297")[0][1] # Grabbing the table from the tuple
    table.head()