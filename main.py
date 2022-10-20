from bs4 import BeautifulSoup
import requests
from csv import writer

html_text = requests.get('https://www.brickeconomy.com/sets/retiring-soon').text
soup = BeautifulSoup(html_text, 'lxml')
sets = soup.find_all("td", class_ = 'ctlsets-left')
results = []
for set in sets:
  results.append(set.find('a')['href'])

with open('retiring.csv', 'w', encoding='utf8', newline='') as f:
  fileWriter = writer(f)
  header = ['Set number', 'Name', 'Theme', 'Subtheme', 'Released', 'Market price', 'Retail price', 'Retirement', 'Retirement pop', 'Annual growth (first year)', 'Annual growth (second year']
  fileWriter.writerow(header)

  for result in results:
    html_text2 = requests.get('https://www.brickeconomy.com' + result).text
    soup = BeautifulSoup(html_text2, 'lxml')
    try:
      set_number = soup.find('div', text= 'Set number').next_sibling.text
    except:
      set_number = "unknown"
    try:
      set_name = soup.find('div', text= 'Name').next_sibling.text
    except:
      set_name = "unknown"
    try:
      set_theme = soup.find('div', text= 'Theme').next_sibling.text
    except:
      set_theme = "unknown"
    try:
      set_subtheme = soup.find('div', text= 'Subtheme').next_sibling.text
    except:
      set_subtheme = "unknown"
    try:
      set_release = soup.find('div', text= 'Released').next_sibling.text
    except:
      set_release = "unknown"
    try:
      set_market = soup.find('div', text= 'Market price').next_sibling.text
    except:
      set_market = "unknown"
    try:
      set_retail = soup.find('div', text= 'Retail price').next_sibling.text
    except:
      set_retail = "unknown"
    try:
      set_retirement = soup.find('div', text= 'Retirement').next_sibling.text
    except:
      set_retirement = "unknown"
    try:
      set_retirementpop = soup.find('div', text= 'Retirement pop').next_sibling.text
    except:
      set_retirementpop = "unknown"
    try:
      set_annual_growth1 = soup.find('div', text= 'Annual growth').next_sibling.next_element.text.replace('\xa0\xa0(first year)', '')
    except:
      set_annual_growth1 = "unknown"

    try:
      set_annual_growth2 = soup.find('div', text= 'Annual growth').next_sibling.next_element.next_sibling.text.replace('\xa0\xa0(second year)', '')
    except:
      set_annual_growth2 = "unknown"
    
    info = [set_number, set_name, set_theme, set_subtheme, set_release, set_market, set_retail, set_retirement, set_retirementpop, set_annual_growth1, set_annual_growth2]
    fileWriter.writerow(info)
    print(set_number)
    # print(set_name)
    # print(set_theme)
    # print(set_subtheme)
    # print(set_release)
    # print(set_retail)
    # print(set_market)
    # print(set_retirement)
    # print(set_retirementpop)
    # print(set_annual_growth1)
    # print(set_annual_growth2)
  print("All Done")

