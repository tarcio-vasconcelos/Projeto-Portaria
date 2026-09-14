from pathlib import Path
from pypdf import PdfReader
from docxtpl import DocxTemplate, RichText
import shutil


def buscar_pdfs():
    caminho = Path("Novos")
    arquivos = puxar_lista(caminho)
    
    mapa = {
    "aplicar_penalidade": "",
    "autorizar_o_afastamento": "",
    "conceder_a_gratificação_de_risco_em_regime_de_plantão": "",
    "conceder_a_permanência_no_regime_de_trabalho_de_dedicação_exclusiva": "",
    "conceder_gratificação_de_dedicação_exclusiva": "",
    "conceder_gratificação_de_incentivo_à_titulação_docente": "",
    "concender_gratificação_de_risco_vida": "",
    "conceder_licença_sem_vencimentos": "",
    "declarar_vacância": "",
    "designar_substituir": "",
    "designar": "",
    "dispensar": "",
    "distribuir_carga_horária": "",
    "e r r a t a": "",
    "exonerar": "",
    "extrato_de_contrato": "",
    "homologar": "",
    "instaurar_comissão": "",
    "interromper": "",
    "migração_de_regime_de_trabalho_de_dedicação_exclusiva": "",
    "nomear": "",
    "progredir_por_elevação_de_nível_profissional": "",
    "promover": "",
    "reconhecer_direito_à_licença_prêmio": "",
    "reconhecer_o_direito_ao_abono_de_permanência": "",
    "remanejar": "",
    "remover": "",
    "rescindir": "",
    "suspender": "",
    "tornar_sem_efeito": "",
    "prorrogar": "",
    "retificar": "",
    "retornar_do_afastamento": "",
    }
    
    if not arquivos:
        return arquivos
    
    for arquivo in arquivos:
        texto = extrair_texto(arquivo)
        if "Documento assinado eletronicamente" in texto:
            mapa = classificar(texto, mapa)
            
    preencher_texto(mapa)
    return mapa

def puxar_lista(caminho): 
    pdfs = list(caminho.glob("*.pdf"))
    return pdfs

def extrair_texto(caminho):
    reader = PdfReader(caminho)
    texto = ""
    paginas = reader.pages
    for pagina in paginas:
        texto_bruto = pagina.extract_text() or ""
        texto += texto_bruto
    return texto

def classificar(texto, mapa):
    texto_lista = texto.split("R  E  I  T  O  R A")
    for item in mapa:
        item_interavel = item.replace("_", " ")
        if item_interavel.lower() in texto_lista[0].lower():
            rt = RichText()
            rt.add(texto_lista[0])
            mapa[item] = rt
            return mapa
    return mapa

def preencher_texto(mapa):
    doc = DocxTemplate("Template/BOLETIM OFICIAL - MODELO EM BRANCO.docx")
    doc.render(mapa)
    doc.save("Finalizar/BOLETIM.docx")