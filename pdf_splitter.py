from PyPDF2 import PdfFileReader, PdfFileWriter

# function for extraction pdfs information. Not currently used, due to some
# pdfs using metadata streams insted of docinfo dictionaries resulting in title = None

def extract_information(pdf_path):

    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        page_number = pdf.getNumPages()
        info = pdf.getDocumentInfo()

        information = {
            'title' : info.title,
            'number_of_pages' : page_number
        }

    print(information)
    return information



def split_pages(path, title):

    try:
        pdf = PdfFileReader(path)

        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            output = f'{title}{page}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
    
    except:
        print("Unfortunately, there is something wrong with the path.")

if __name__ == "__main__":
    paths = []
    titles = []
    add_path = True
    while add_path:
        print('Please add the path to which doucument that you would like to split.')
        path = input("Path: ")
        title = input("Please give your new documents a title: ")
        cont = input('Write "yes" for adding another document: ')
        paths.append(path)
        titles.append(title)

        if cont.upper() != "YES":
            add_path = False

    for path in paths:
        split_pages(path,titles[paths.index(path)])
    






