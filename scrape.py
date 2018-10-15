from bs4 import BeautifulSoup

import requests
import json


class ScrapRecord(object):
    """
    It's scrap the record from ico data webside.
    """
    def __init__(self):
        super(ScrapRecord, self).__init__()
        self.url = 'https://www.icodata.io/ICO/ended'
        self.content_parser = 'html.parser'

    def http_request(self, url):
        response  = requests.get(url)
        return self.parse_html_data(response)

    def parse_html_data(self, response):
        html_content = BeautifulSoup(response.content,  'html.parser')        
        return html_content

    def scrap_records(self):
        return self.prepare_json_data(self.http_request(self.url))


    def prepare_json_data(self, html_content):
        # It's get elements record from html dom element and return the json response.
        tr_elements = html_content.select('table#table tbody tr')

        record = []
        for element in tr_elements[0::]:
            td_element = element.select('td')
            
            record.append({
                'name' : element.select('td a').pop().text.strip(),
                'usd_raised' : td_element[2].text.strip(),
                'end_of_ico' : td_element[3].text.strip(),
                'token_sale_price' : td_element[4].text.strip(),
                'current_price' : td_element[5].text.strip(),
                'telegram' : td_element[6].text.strip(),
                'hype' : td_element[7].text.strip(),
                'returns' : td_element[8].text.strip(),
                'rating' : td_element[9].text.strip()
                })

        return(json.dumps(record))

def main():
    scrap_record = ScrapRecord()
    data = scrap_record.scrap_records()
    print(data)



if __name__ == '__main__':
    main()