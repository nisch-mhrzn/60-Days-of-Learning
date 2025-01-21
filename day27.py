import pikepdf
from pikepdf import Page
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Open the original PDF
old_pdf = pikepdf.Pdf.open("licence.pdf")

# Reverse the pages in the PDF
old_pdf.pages.reverse()
old_pdf.save("rev_new.pdf")
# Replace the 5th page with the 1st page
old_pdf.pages[4] = old_pdf.pages[0]
old_pdf.save("replace_pnew.pdf")

# Delete specific pages (2nd and 3rd pages)
del old_pdf.pages[1:3]
old_pdf.save("del_new.pdf")


# Add a blank page at the end
blank_page = Page.new(width=old_pdf.pages[0].mediabox[2], height=old_pdf.pages[0].mediabox[3])
old_pdf.pages.append(blank_page)
old_pdf.save("add_blank_page.pdf")

# Open another PDF to merge
another_pdf = pikepdf.Pdf.open("Machine learning.pdf")

# Append all pages from another PDF
for page in another_pdf.pages:
    old_pdf.pages.append(page)

old_pdf.save("merged.pdf")

