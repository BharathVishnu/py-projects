import PyPDF2

def merge_pdfs(input_paths, output_path):
    merger = PyPDF2.PdfFileMerger()

    for path in input_paths:
        with open(path, 'rb') as pdf_file:
            merger.append(pdf_file)

    with open(output_path, 'wb') as merged_pdf:
        merger.write(merged_pdf)

if __name__ == "__main__":

    input_pdf_paths = input('Enter input file paths:').split()

    output_pdf_path = input('Enter output file path: ')

    merge_pdfs(input_pdf_paths, output_pdf_path)

    print("PDFs merged successfully!")
