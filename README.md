# PDF-Merger

## Overview
This project is a PDF merger Python script that allows users to merge multiple PDF files into a single PDF. 
It provides a graphical user interface (GUI) for easy interaction and file selection.

## Features

- **Merge Multiple PDFs**: Select up to three PDF files and merge them into a single output file.
- **GUI**: A user-friendly interface for selecting files and merging them.
- **Error Handling**: Handles common errors such as file not found and permission errors.

## Usage

### GUI Instructions

1. **Select PDF Files**: Click on the `Browse` button to select up to three PDF files.
2. **Specify Output File**: Click on the `Browse` button to specify the output file location and name.
3. **Merge PDFs**: Click on the `Merge PDFs` button to merge the selected files.
4. **Exit**: The application will continue running until you manually close the window.

### Example
```plaintext
Selected PDFs: ['file1.pdf', 'file2.pdf', 'file3.pdf']
Processing: file1.pdf
Processing: file2.pdf
Processing: file3.pdf
Total pages added: 15
PDF Merge Completed Successfully.
```
## Installation
1. **Clone the repository**.
   ```sh
   git clone https://github.com/Dosobella/PDF-Merger.git
2. **Navigate to the project directory**.
   ```sh
   cd PDF_merger
3. **Install required dependencies**.
   ```sh
   pip install PyPDF2
## Run the script
```sh
pip PDF_merger.py

