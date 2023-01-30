from bs4 import BeautifulSoup
import requests
from csv import writer
from multiprocessing import Pool
import tqdm

def multi_process():
  html_text = requests.get('https://www.brickeconomy.com/sets/retiring-soon').text
  soup = BeautifulSoup(html_text, 'lxml')
  sets = soup.find_all("td", class_ = 'ctlsets-left')
  results = []
  for set in sets:
    results.append(set.find('a')['href'])

  if __name__ == '__main__':
    print("Extracting Data...")
    all_info = []
    with Pool(processes=4) as pool, tqdm.tqdm(total=len(results)) as pbar:
      all_data = []
      for data in pool.imap_unordered(get_data, results): 
        all_data.append(data)
        pbar.update()

    with open('retiring.csv', 'w', encoding='utf8', newline='') as f:
      fileWriter = writer(f)
      header = ['Set number', 'Name', 'Theme', 'Subtheme', 'Released', 'Market price', 'Retail price', 'Retirement', 'Retirement pop', 'Annual growth (first year)', 'Annual growth (second year']
      fileWriter.writerow(header)
      for info in all_data:
        fileWriter.writerow(info)
    print("Saved Data To CSV!")

def single_process():
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
    print("Extracting Data...")
    with tqdm.tqdm(total=len(results)) as pbar:
      for result in results:
        info = get_data(result)
        fileWriter.writerow(info)
        pbar.update()
  print("Saved Data To CSV!")


def get_data(result):
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
    return info

def main():
  multi_process()
  # single_process()

main()

