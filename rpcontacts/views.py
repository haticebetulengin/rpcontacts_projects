# Görselde ne olacak tanımlamaları yapılıyor.
from PyQt5.QtCore import Qt # Kişi Ekle iletişim kutusunu oluşturmak için
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QAbstractItemView, #tablo görünümü seçim davranışı ilkesine erişim sağlamak için
    QDialog, #Kişi Ekle iletişim kutusunu kodlamak için.GUI uygulamaları için diyaloglar oluşturur.
    QDialogButtonBox, # Kişi Ekle iletişim kutusunu oluşturmak için
    QFormLayout, # Kişi Ekle iletişim kutusunu oluşturmak için
    QHBoxLayout,
    QLineEdit, # Kişi Ekle iletişim kutusunu oluşturmak için
    QMainWindow,
    QMessageBox, # Kişi Ekle iletişim kutusunu oluşturmak için
    QPushButton, #Buton eklemek için
    QTableView, #Tablo görünümü için
    QVBoxLayout, #butonların alt alta eklenmesi için
    QWidget,
)
from .model import ContactsModel
class Window(QMainWindow):
    #"""Main Window."""
    def __init__(self, parent=None):
        #"""Initializer."""
        super().__init__(parent) #QMainWindow özelliklerini bizim sınıfa aktarıyoruz.
        self.setWindowTitle("RP Contacts") #Pencerenin başlığı
        self.resize(550, 250) #pencerenin boyutu
        self.centralWidget = QWidget() #Ana gruplandırıcı
        self.setCentralWidget(self.centralWidget) #setCentralWidget ile nesnenin içine aktarıyoruz. küçük nesneleri büyük nesneye bağlar.
        self.layout = QHBoxLayout() #Layout tanımlanıyor. Main layout tutucu.
        self.centralWidget.setLayout(self.layout) #central'a QHBoxLayout'u da ekliyor. 
        #Buraya kadar yapılanlar, boş bir pencere oluşturmak içindir. 
        self.contactsModel = ContactsModel() #bize gerilen verileri alacak bir model tanımlanıyor.
        self.setupUI()

    def setupUI(self):
        #"""Setup the main window's GUI."""
        # Tablo nesnesi oluşturuluyor. nesne ismi table'dır.
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model) #tabloya, tanımlanan modeli bağlıyoruz. 
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents() #içeriğe göre hücre boyutunu otomatik olarak büyütüp/küçültmeyi sağlar.
        # Buton ekleme. Nesne ismi Button'dur. 
        self.addButton = QPushButton("Ekle...")
        # Ekle düğmesinin .clicked()sinyalini yeni oluşturulan yuvaya bağlar.düğmeye bir tıklama otomatik olarak yuvayı arayacaktır .openAddDialog()
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Sil")
        self.deleteButton.clicked.connect(self.deleteContact) #Sil düğmesi click ile yuvaya bağlanır.
        self.clearAllButton = QPushButton("Tümünü Seç")
        self.clearAllButton.clicked.connect(self.clearContacts) #Tümünü seç düğmesi için click ile bağlama yapıyoruz.
        # Lay out'lara bağlama yapıyoruz. 
        layout_button = QVBoxLayout()
        layout_button.addWidget(self.addButton) # Ekle butonunu ekledi
        layout_button.addWidget(self.deleteButton) # Sil butonunu ekledi
        layout_button.addStretch() # Araya boşluk ekliyor. 
        layout_button.addWidget(self.clearAllButton) # Tümünü seç butonunu ekledi
        
        #Hazırlanan butonları ve tabloyu main layout'a ekliyoruz. 
        self.layout.addWidget(self.table) #sınıfın asıl layout'u
        self.layout.addLayout(layout_button) #widgetların layout'u
    
    def openAddDialog(self):
        dialog = AddDialog(self) #Örnek oluşur.
        if dialog.exec() == QDialog.Accepted: #iletişim kutusunun kabul edilip edilmediği kontrolü
            self.contactsModel.addContact(dialog.data) #Eğer kabul edildiyse 59.satır argüman olarak addContact() ile veri modelini çağırır.
            self.table.resizeColumnsToContents() # Tablo görünümü yeniden boyutlandırılır. 

    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Uyarı!",
            "Seçili kişiyi kaldırmak istiyor musunuz?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)

    def clearContacts(self): #Tümünü seçerek silme 
        messageBox = QMessageBox.warning(
            self,
            "Uyarı!",
            "Tüm kişilerinizi silmek istiyor musunuz?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.clearContacts()


class AddDialog(QDialog): #QDialog'dan miras alan yeni bir sınıf tanımlanıyor. 
    #84-91 arası sınıf başlatıcısını tanımlar. 
    # Bu durumda, en uygun ekleme .data, kullanıcılarınızın sağladığı verileri tutmak için kullanacağınız bir örnek niteliğidir.
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Kişi Ekle")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        # veri alanları için satır düzenlemeleri oluşturma
        self.nameField = QLineEdit() 
        self.nameField.setObjectName("İsim") #Eklenecek kişinin adı girdisi
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Meslek") #Eklenecek kişinin işi girdisi
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email") #Eklenecek kişinin mail adresi girdisi
        
        # Veri alanlarını düzenleme, satır düzenlemelerini yapıyoruz.
        layout = QFormLayout()
        layout.addRow("İsim:", self.nameField)
        layout.addRow("Meslek:", self.jobField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        
        # İki tane standart düğme sağlayan nesne ekliyoruz. Ok ve Cancel
        # Tamam düğmesi kullanıcının girişini kabul eder ve İptal düğmesi onu reddeder.
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        # 131 ve 132. satırlar, iletişim kutusunun yerleşik .accepted() ve .rejected() sinyallerini sırasıyla .accept() ve reject() yuvalarına bağlar.
        # Bu durumda, diyalog kutusunun girdiyi işlemeden kapatan yerleşik .reject() yuvasına güveneceksiniz. Bunun dışında .accept() yuvasını kodlamanız yeterlidir.
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    # İletişim kutusunun yuvasını kodlarken, doğru ve güvenliliğinden emin olmak için 
    # herhangi bir kullanıcı girişinin onaylanması .accept() gerektiğini düşünmek gerekir .
    def accept(self):
        self.data = [] #Boş bir listeyle başlar. Bu liste kullanıcının giriş verilerini saklayacak.
        # İletişim kutusundaki üç satır düzenlemesi veya alan üzerinde yineleme yapan bir for döngüsü tanımlanır.
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Hata!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return
            # 141 - 148 arasında kullanıcının iletişim kutusundaki her alan için veri sağlayıp sağlamadığını kontrol eder.
            # Değilse, iletişim kutusu, kullanıcıyı eksik veriler hakkında uyaran bir hata mesajı gösterir.
            self.data.append(field.text()) # her alan için kullanıcının girdisini ekler

        if not self.data:
            return

        #kullanıcı Tamam'ı tıklattıktan sonra iletişim kutusunu kapatan standart davranışı sağlamak için üst sınıfın .accept() yuvasını çağırır.
        super().accept()