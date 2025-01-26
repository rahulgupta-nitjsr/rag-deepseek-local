from fpdf import FPDF

# Create a sample PDF file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is a test PDF file.", ln=True)
pdf.cell(200, 10, txt="It contains multiple lines of text.", ln=True)
pdf.output("test_sample.pdf")

# Test the extract_text_from_pdf function
file_path = "test_sample.pdf"
extracted_text = extract_text_from_pdf(file_path)
print(extracted_text)
