import pandas as pd
from fpdf import FPDF


def footer(x):
    pdf.ln(x)

    pdf.set_font(family="Times", size=24, style="I")

    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


def line():
    for i in range(27):
        pdf.cell(w=0, h=10, txt="", ln=1, border="B")


data = pd.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24)
    pdf.set_fill_color(209, 224, 224)
    pdf.set_text_color(153, 102, 255)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=0, border=1, fill=True)
    line()
    footer(5)

    for page in range(row['Pages'] - 1):
        pdf.add_page()
        line()
        footer(5)

pdf.output("output.pdf")
