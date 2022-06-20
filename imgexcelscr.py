import requests, shutil, xlsxwriter, os, glob
from bs4 import BeautifulSoup
import pandas as pd
#returns link to the first image in search results for book_to_find in indigo website
def generate_link(book_to_find):
    url = (f'https://www.chapters.indigo.ca/en-ca/home/search/?keywords={book_to_find}')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    imagefind = soup.find('img')
    link = imagefind['src']
    return link
#downloads image to 'book1.jpg' in users\riley
def download_image(link_to_image, index):
    r = requests.get(link_to_image, stream=True) #Get request on link_to_image
    with open(f"C:\\Users\\riley\\Documents\\Pyth\\ScrapeBin\\book{index}.jpg", 'wb') as f:
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
      f.close()
#extracts data from excel - arguments are excel file, column name
def get_excel_data(fileobj, column_name):
    data = pd.read_excel(f"{fileobj}")
    df = pd.DataFrame(data)
    coldata = df[column_name]
    return coldata
#file to extract
#usage example, takes 'article title' column from file below and extracts it to file1
file1 = get_excel_data(r'C:\Users\riley\example.xlsx', 'ARTICLE TITLE')


# generates workbook and calls above functions to create an author's info in 1st row,
# and an image of the cover of the book
def wbgen(book_data, filename):
    workbook = xlsxwriter.Workbook(f'C:\\Users\\riley\\{filename}.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 30)
    #main for loop to grab name from author data, download the corresponding image, and put in author + image into excel
    for i in range(1, len(book_data) +1):
        download_image(generate_link(book_data[i-1]), i)
        worksheet.write(f'A{i}', f'{book_data[i-1]}:') #writes the book data to excel file
        worksheet.insert_image(f'B{i}', f'C:\\Users\\riley\\Documents\\Pyth\\ScrapeBin\\book{i}.jpg') #writes the corresponding images it excel file
    workbook.close()
    #removes downloaded files from directory
    path = r"C:\Users\riley\Documents\Pyth\ScrapeBin"
    files = glob.glob(path + '/*.jpg')
    for f in files:
        os.remove(f)
#final function call to write data from file1 into new excel file 'EcoWarriors_images'
wbgen(file1, 'Example_Output')
