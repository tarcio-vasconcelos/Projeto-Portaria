from pypdf import PdfReader

read = PdfReader("Finalizados/Não Assinados/SEI_GOVPE - 85122747 - UPE - Portaria Reitor - DESIGNAR.pdf")
texto = ""

path = read.pages[0]
texto = path.extract_text()

print(texto)