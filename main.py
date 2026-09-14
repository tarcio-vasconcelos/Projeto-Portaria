from pypdf import PdfReader
import utils

def iniciar():
    trig = utils.buscar_pdfs()
    if not trig:
        print("A lista está vazia!")
    else:
        ...
        #print(trig)
iniciar()