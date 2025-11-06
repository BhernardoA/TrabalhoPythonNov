import requests as rq
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())

def api():
    url = "https://date.nager.at/api/v3/PublicHolidays/2025-2026/BR"

    payload = {}
    headers= {
        'accept': 'applicantion/json',
        'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJ'
        }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

def arquivo():
    arquivo = filedialog.askopenfilename(title="Escolha um arquivo")
    if arquivo:
        print(arquivo)
        

def Interface():
    root = tk.Tk()
    root.title("Titulo da janela")
    root.geometry("600x400")
    Botao = tk.Button(root, text="escolha_o_arquivo", command=arquivo)
    Botao.pack(pady=20)
    tk.mainloop()


if __name__ == '__main__':
    Interface()
    
