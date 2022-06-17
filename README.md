# BookTitletoImage
Takes a list of book titles, goes to indigo.com and scrapes the image found by searching the title. Takes that image and creates a new excel file with titles and images

Functions:
generate_link(book_to_find): #returns link to the first image in search results for book_to_find in indigo website
download_image(link_to_image, index):#downloads image to 'book{index}.jpg' in cwd
get_excel_data(fileobj, column_name): #extracts data from excel - arguments are excel file, column name
wbgen(book_data, filename): generates workbook and calls above functions to create an author's info in 1st row, and an image of the cover of the book retrieved in download_image
