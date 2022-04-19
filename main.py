from unittest.mock import patch
from fpdf import FPDF


def run():
    pdf = FPDF(
        orientation="P",
        unit="mm",
        format="A4"
        )

    pdf.add_page()

    pdf.set_margins(
        left=5,
        right=5,
        top=5)   

    pdf.set_font(
        family="helvetica",
        style="B",
        size=16
        )

    pdf.cell(
        w=40,
        h=10,
        txt="Hello World!"
        )

    pdf.cell(
        w=40,
        h=10,
        txt="Hello World!"
        )

    pdf.cell(60, 10, 'Powered by FPDF.', align='C')

    pdf.ln(h=None)#-- Salto de linea h es altura None acomoda de forma automatica
    

    pdf.multi_cell(
        w=0,
        h=5,
        txt="Habia un dia: En el documento de entrega de proyecto."+
    "El decía mucho eso. El historial de avance. Para ver esa linea de tiempo."+ 
    "Para tener la experiencia en Campo."+
    "Lo siguiente es para ver como trabaja la nueva implementacion de la ruta y "+
    "nombre de archivo por separado."
    )

    pdf.add_page()

    pdf.set_margins(
        left=5,
        right=5,
        top=5)   

    pdf.set_font(
        family="helvetica",
        style="B",
        size=16
        )

    pdf.cell(
        w=40,
        h=10,
        txt="Hello World!"
        )

    pdf.cell(
        w=40,
        h=10,
        txt="Hello World!"
        )

    pdf.cell(60, 10, 'Powered by FPDF.', align='C')

    
    patch:str = "./src/"
    fileName: str = "tuto1.pdf"
    pdf.output(name=f"{patch}{fileName}")

if __name__ == '__main__':
    run()