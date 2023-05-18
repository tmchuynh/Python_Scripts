from fpdf import FPDF
Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("result.pdf", "F")