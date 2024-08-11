import webbrowser
import os

# Path to the PDF file
pdf_path = r'TensorFlowGraph-VAST.pdf'

# Convert the file path to a file URL
file_url = 'file://' + os.path.abspath(pdf_path)

# Open the PDF file in the default web browser (Chrome if set as default)
webbrowser.open(file_url)
