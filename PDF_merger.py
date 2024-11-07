# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:16:58 2024

@author: Dosobella
"""
import PyPDF2  # Import the PyPDF2 library for PDF operations
import tkinter as tk  # Import the Tkinter library for GUI creation
# Import filedialog module for file selection dialogs
from tkinter import filedialog


def merge_pdf(file_paths, output_file):
    """Merges multiple PDF files into a single PDF.

    Args:
        file_paths (list): A list of file paths to the PDF files to be merged.
        output_file (str): The path to the output PDF file.

    Returns:
        bool: True if the merge is successful, False otherwise.
    """

    try:
        # Create a PDF writer object to store merged pages
        pdf_writer = PyPDF2.PdfWriter()

        for file_path in file_paths:

            if file_path:

                print("\nProcessing:", file_path)

                # Create a PDF reader object for the current file
                pdf_reader = PyPDF2.PdfReader(file_path)

                i = 0
                # Iterate over each page in the PDF
                for page in pdf_reader.pages:

                    # Add the page to the writer object
                    pdf_writer.add_page(page)

                    i += 1

        print(f"\nTotal pages added:", len(pdf_writer.pages))

        # Write the merged PDF to the specified output file
        with open(output_file, 'wb') as fh:

            pdf_writer.write(fh)

            print("\nPDF Merge Completed Succesfully.")

            return True

    except FileNotFoundError:

        print(f"Error: Input file not found.")

#   except PyPDF2.PdfReadError:

#       print(f"Error: Invalid or corrupted PDF file.")

    except PermissionError:

        print(f"Error: Insufficient permissions.")

    except Exception as e:

        print(f"Error: {e}")


def browse_file1():
    filename = filedialog.askopenfilename(title="Select PDF File 1")
    entry1.delete(0, tk.END)
    entry1.insert(0, filename)


def browse_file2():
    filename = filedialog.askopenfilename(title="Select PDF File 2")
    entry2.delete(0, tk.END)
    entry2.insert(0, filename)


def browse_file3():
    filename = filedialog.askopenfilename(title="Select PDF File 3")
    entry3.delete(0, tk.END)
    entry3.insert(0, filename)


def browse_ouput_file():
    filename = filedialog.asksaveasfilename(
        title="Saved Merged PDF", defaultextension=".pdf", filetypes=[("PDF Files", ".pdf")])
    entry4.delete(0, tk.END)
    entry4.insert(0, filename)


def start_merge():
    file_paths = [entry1.get(), entry2.get(), entry3.get()]
    print("\nSelected PDFs:", file_paths)
    output_file = entry4.get() + ".pdf"
    if merge_pdf(file_paths, output_file):
        label5.config(text="PDFs merged successfully!", fg="green")

    else:
        label5.config(
            text="Error merging PDFs. Check console for details.", fg='red')


root = tk.Tk()
root.title("PDF Merger")

label1 = tk.Label(root, text="PDF File 1:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=1, padx=5, pady=5)

button1 = tk.Button(root, text="Browse", command=browse_file1)
button1.grid(row=0, column=2, padx=5, pady=5)

label2 = tk.Label(root, text="PDF File 2:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=1, padx=5, pady=5)

button2 = tk.Button(root, text="Browse", command=browse_file2)
button2.grid(row=1, column=2, padx=5, pady=5)

label3 = tk.Label(root, text="PDF File 3:")
label3.grid(row=2, column=0, padx=5, pady=5)

entry3 = tk.Entry(root, width=50)
entry3.grid(row=2, column=1, padx=5, pady=5)

button3 = tk.Button(root, text="Browse", command=browse_file3)
button3.grid(row=2, column=2, padx=5, pady=5)

label4 = tk.Label(root, text="Output File:")
label4.grid(row=3, column=0, padx=5, pady=5)

entry4 = tk.Entry(root, width=50)
entry4.grid(row=3, column=1, padx=5, pady=5)

button4 = tk.Button(root, text="Browse", command=browse_ouput_file)
button4.grid(row=3, column=2, padx=5, pady=5)

button5 = tk.Button(root, text="Merge PDFs", command=start_merge)
button5.grid(row=4, column=1, padx=5, pady=5)

label5 = tk.Label(root, text="Message")
label5.grid(row=5, column=1, padx=5, pady=5)


root.mainloop()

if __name__ == '__main__':

    root.mainloop()
