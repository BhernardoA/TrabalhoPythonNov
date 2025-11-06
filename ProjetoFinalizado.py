import requests as rq
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):
    reader = PyPDF2.PdfReader(in_PdfFile) 
    return reader.pages[0].extract_text()

def api():
    url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

    payload = {}
    headers= {
        'accept': 'application/json',
        'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJ'
        }

    response = rq.request("GET", url, headers=headers, data=payload)
    return response.text

def arquivo(texto_widget):
    arquivo = filedialog.askopenfilename(title="Escolha um arquivo")
    if arquivo:
        texto_pdf = Get_text_from_PDFfiles_usingPyPDF2(arquivo)
        datas=texto_pdf.split("\n")
        feriado = api()
        for data in datas:
            if data.strip() in feriado:
                texto_widget.insert(tk.END, data + "\n")
                print(data)

        print(arquivo)
        

def Interface():
    root = tk.Tk()
    root.title("Programinha :D")
    root.geometry("600x400")

    texto = tk.Text(root, wrap="word", height=30, width = 60)
    texto.pack(pady=20)
    
    Botao = tk.Button(root, text="escolha_o_arquivo", command=lambda: arquivo(texto))
    Botao.pack(pady=20)
    
    tk.mainloop()


if __name__ == '__main__':
    Interface()
    
