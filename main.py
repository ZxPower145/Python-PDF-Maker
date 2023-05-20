import pandas as pd
from fpdf import FPDF

data = pd.read_csv("topics.csv", sep=",")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24)
    pdf.set_fill_color(209, 224, 224)
    pdf.set_text_color(153, 102, 255)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1, border=1, fill=True)
    for page in range(row['Pages'] - 1):
        pdf.add_page()

pdf.output("output.pdf")
