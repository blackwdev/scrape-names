import requests
from bs4 import BeautifulSoup
import xlsxwriter

root = "https://museum.wa.gov.au"
website = f'{root}/welcomewalls/names'
max_row = 1

def scrape(i, website):
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    tbody_a = soup.find('tbody').find_all('a', href=True)    

    for row_num, data in enumerate(tbody_a):
        worksheet.write_row(row_num + i, 0, data.get_text().split(","))
    return len(tbody_a)

with xlsxwriter.Workbook('result.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, ['First name', 'Surname'])

    max_row += scrape(max_row, website)
    for page_num in range(1, 3):
        website = f'{root}/welcomewalls/names?page={page_num}'
        max_row += scrape(max_row, website)