from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image(
            name="./src/img/logoJamar.png",
            x=10,
            y=8,
            w=33
            )
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", 1, 0, "C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")


# Instantiation of inherited class
pdf = PDF()

'''alias_nb_pages() metodo que se encarga de darnos la cantiad total de paginas para 
usar el valor especial {nb}'''
pdf.alias_nb_pages()

pdf.add_page()
pdf.set_font(family="Times", size=12)
for i in range(1, 100):
    pdf.cell(w=0, h=10, txt=f"Printing line number {i}", border=0, ln=1)
pdf.output("./src/tuto2.pdf")
