from fpdf import FPDF
from datetime import datetime

def generate_report(patient_info, result):
    pdf = FPDF()
    pdf.add_page()
    # Add report content
    return pdf.output(dest='S').encode('latin1')