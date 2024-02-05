import reportlab  # Replace with your chosen library
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

# Create a PDF document object
pdf = reportlab.pdfgen.canvas.Canvas("invoice.pdf")

# Set fonts, font sizes, and colors
# pdf.setFont("Helvetica", 12)
# Set fonts and font sizes
pdf.setFont("Helvetica-Bold", 20)  # Font for company name
# pdf.setFont("Helvetica", 10)  # Font for address and contact details


# - Header (company logo, name, address, contact details)
# Add company logo
logo_path = "test_images/logo.png"  # Replace with your logo's path
logo_width = 2 * inch  # Adjust width as needed
logo_height = inch  # Adjust height as needed
pdf.drawImage(logo_path, 1 * inch, 9.5 * inch, width=logo_width, height=logo_height)

# Add company name
pdf.drawString(3 * inch + logo_width, 10.5 * inch, "Grow Fitness")
pdf.setFont("Helvetica", 10)  # Font for address and contact details
# Add company address
address1 = "Sai Sastha Crystal Building, Tembhipada Road,"
address2 = "Market Tembhipada, Bhandup West, Mumbai"
pdf.drawString(3 * inch + logo_width, 10 * inch, address1)
pdf.drawString(3 * inch + logo_width, 9.8 * inch, address2)

# Add contact details
phone = "Phone: +919619053019"
email = "Email: info@yourcompany.com"
pdf.drawString(3 * inch + logo_width, 9 * inch, phone)
pdf.drawString(3 * inch + logo_width, 8.8 * inch, email)
# --- Add a horizontal line to visually separate the header ---
pdf.line(0.5 * inch, 8.5 * inch, 7.5 * inch, 8.5 * inch) 


# - Invoice number, issue date, due date
pdf.setFont("Helvetica-Bold", 12)  # Font for invoice number
pdf.drawString(1 * inch, 8 * inch, "Invoice No.: INV-2023-12345")  # Replace with actual invoice number

pdf.setFont("Helvetica", 10)  # Font for dates
pdf.drawString(6 * inch, 8 * inch, "Issue Date: 2023-12-29")  # Replace with actual issue date
pdf.drawString(6 * inch, 7.8 * inch, "Due Date: 2024-01-12")  # Replace with actual due date

# --- Customer information (name, address) ---
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1 * inch, 7.5 * inch, "Bill To:")
pdf.setFont("Helvetica", 10)
customer_name = "John Doe"  # Replace with actual customer name
customer_address = "456 Elm Street"
pdf.drawString(1 * inch, 7.2 * inch, customer_name)
pdf.drawString(1 * inch, 7 * inch, customer_address)
# --- Visual cue (optional) ---
# pdf.line(1 * inch, 3 * inch, 7.5 * inch, 3 * inch)


# - Table of items (description, price, quantity, total)
items = [
    ["Description", "Price"],
    ["Subscription Plan", "$10.00"],
    ["Personal Trainer", "$5.50"],
    ["Total", "$12.00"],
]

# Table style (adjust as needed)
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header row background
    ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),             # Align price, quantity, total to the right
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),          # Vertically center text
    ('GRID', (0, 0), (-1, -1), 1, colors.black),       # Grid lines
])

# Create the table
table = Table(items, colWidths=[4 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
table.setStyle(table_style)

# Position the table on the PDF
table.wrapOn(pdf, 6 * inch, 5 * inch)  # Adjust width and height as needed
table.drawOn(pdf, 1 * inch, 5 * inch)

# --- Total amount paid ---
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1 * inch, 4.5 * inch, "Total Amount Paid:")
total_amount_paid = 48.50
pdf.setFont("Helvetica", 12)
pdf.drawString(6 * inch, 4.5 * inch, f"${total_amount_paid:.2f}")

# --- Total payment balance ---
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1 * inch, 4.25 * inch, "Total Amount Balance:")
total_amount_bal = 48.50
pdf.setFont("Helvetica", 12)
pdf.drawString(6 * inch, 4.25 * inch, f"${total_amount_bal:.2f}")

# --- Payment Mode ---
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1 * inch, 4 * inch, "Payment Mode:")
payment_mode = "Cash"
pdf.setFont("Helvetica", 12)
pdf.drawString(6 * inch, 4 * inch, f"{payment_mode}")


pdf.line(1 * inch, 1 * inch, 7.5 * inch, 1 * inch)

# - Payment information (bank account details, payment methods)
# - Footer (terms and conditions, contact information)
pdf.setFont("Helvetica", 10)  # Font for footer content

# --- Copyright notice (optional) ---
copyright_text = "Copyright © 2024 Grow Fitness. All rights reserved."
text_width = pdf.stringWidth(copyright_text, "Helvetica", 8)  # Measure text width
start_x = (pdf._pagesize[0] - text_width) / 2  # Calculate center position
pdf.drawString(start_x, 0.5 * inch, copyright_text)

# Save the PDF
pdf.save()