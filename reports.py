import webbrowser
import os
class Pdfreport:
    """
    Creates a PDF which contain data about the flatmates  such as their name there due amount and period of bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2, bill):
        from fpdf import FPDF

        fm1 = str(round(flatmate1.pays(bill, flatmate2),3))
        fm2 = str(round(flatmate2.pays(bill, flatmate1), 3))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w =30, h=30)

        pdf.set_font('Times', 'B', 24)
        pdf.cell(w = 0, h= 80, txt = 'Flatmates Bill', border =1, align = 'C', ln=1)

        pdf.cell(w = 100, h= 40, txt = 'Period:', border =1)
        pdf.cell(w=150, h=40, txt= bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt= flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt= fm1, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt= fm2, border=1, ln=1)

        file_path =  os.path.join("files", self.filename)
        pdf.output(file_path)
        webbrowser.get('safari').open('file://'+os.path.realpath(file_path))


