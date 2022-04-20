from PyPDF2 import PdfFileWriter, PdfFileReader
#--- Tomado a : https://es.acervolima.com/encriptar-y-desencriptar-pdf-usando-pypdf2/


out = PdfFileWriter() 
  
file = PdfFileReader("./src/tuto1.pdf") 
  
num = file.numPages 
  
for idx in range(num): 
    
    
    page = file.getPage(idx) 
      
    
    out.addPage(page) 
  
  
password = "pass"
  
out.encrypt(password) 
  
with open("./src/myfile_encrypted.pdf", "wb") as f: 
    
    
    out.write(f)