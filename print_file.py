import pypdf

def print_pdf(file_path):
    # prints the saved gpx file to a PDF
        pdf_writer = pypdf.PdfWriter()
        pdf_reader = pypdf.PdfReader(file_path)

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        output_path = file_path.replace('.gpx', '.pdf').replace('.xml', '.pdf')
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"GPX file has been printed to PDF: {output_path}")

def print_gpx(gpx_to_print):
  
    # Print the contents of a GPX file to the console.
    print(gpx_to_print)
    print("\nEnd of file.")