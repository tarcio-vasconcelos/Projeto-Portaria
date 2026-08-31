import os, shutil
from pypdf import PdfReader

def buscar_assinatura(pypdf, os, shutil):
    caminho = "./Arquivos/"
    lista = ler_pdfs(caminho, os)

    quant_arquivos = range(len(lista))
    for i in quant_arquivos:
        texto = ""
        caminho += lista[i]
        reader = PdfReader(caminho)
        for page in range(len(reader.pages)):
            texto += reader.pages[page].extract_text()
        if "Documento assinado eletronicamente" in texto:
            destino = "./Finalizados/Assinados"
            shutil.move(caminho, destino)
            caminho = "./Arquivos/"
        else:
            destino = "./Finalizados/Não Assinados"
            shutil.move(caminho, destino)
            caminho = "./Arquivos/"

def ler_pdfs(arquivo ,os):
    lista = os.listdir(arquivo)
    return lista

def agrupar_pdfs(os, PDF):
    caminho = "./Finalizados/Assinados"
    lista = ler_pdfs(caminho ,os)
    print(lista)




agrupar_pdfs(os, PdfReader)