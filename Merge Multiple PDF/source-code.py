from PyPDF4 import PdfFileMerger
import os

# Inicializa el objeto PdfFileMerger
merger = PdfFileMerger()

# Lista para almacenar nombres de archivos PDF
pdf_files = []

# Itera sobre los archivos en el directorio actual
for file_name in os.listdir():
    # Comprueba si el archivo termina en .pdf
    if file_name.endswith('.pdf'):
        pdf_files.append(file_name)
        merger.append(file_name)

# Escribe el archivo PDF combinado
try:
    merger.write("Final_pdf.pdf")
except Exception as e:
    print(f"Error al escribir el archivo combinado: {e}")
finally:
    merger.close()

# Elimina los archivos PDF originales, excepto el archivo combinado
for file_name in pdf_files:
    if file_name != 'Final_pdf.pdf':
        try:
            os.remove(file_name)
        except Exception as e:
            print(f"Error al eliminar {file_name}: {e}")

