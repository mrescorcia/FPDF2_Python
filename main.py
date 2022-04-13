from fpdf import FPDF


def run():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, "Hello World!")
    pdf.multi_cell(0,5,"Habia un dia: En el documento de entga de proyecto."+
    "El decia mucho eso. El historial de avance. Para ver esa linea de tiempo."+ 
    "Para tener la experiencia en Campo.")
    pdf.output("tuto1.pdf")

if __name__ == '__main__':
    run()