import sys #sistem ile ilgili argümanlar
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window  #Görsel dosyası içe aktarılıyor.

def main(): #Fonksiyon tanımlanıyor.
    """RP Contacts main function."""
    # Create the application
    app = QApplication(sys.argv) #Widgetları oluşturmak için kullanılan sınıf.
    if not createConnection("contacts.sqlite"): #veritabanı adı contacts olacak. sqlite da bu adda dosya yoksa oluşturacak, varsa açacak.
        sys.exit(1)
    # Create the main window
    win = Window() #Bizim sınıfımızdan bir tane nesne oluşturuyoruz.
    win.show() # Nesneyi göstermenisini istiyoruz.
    # Run the event loop
    sys.exit(app.exec()) #Ekranda sürekli durmasını, programın ekrandaki akışını sağlıyor. 
