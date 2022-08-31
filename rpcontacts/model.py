from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ContactsModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        #"""Create and set up the model."""
        tableModel = QSqlTableModel() #tablo modeli oluştur.
        tableModel.setTable("contacts") #tabloya bağlanıyoruz.
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange) #tabloda değişiklik yapabilmeyi sağlıyoruz.
        tableModel.select() 
        headers = ("ID", "İsim", "Meslek", "Email") #tablonun başlıklarını alıyor.
        for columnIndex, header in enumerate(headers): #aldığı başlıkların altına gelecek şekilde hücreleri birbirine eşitliyor.
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
        rows = self.model.rowCount() #veri modelindeki geçerli satır sayısını alır.
        self.model.insertRows(rows, 1) #veri modelinin sonuna yeni bir satır ekler.
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field) #her öğeyi veri modelindeki karşılık gelen hücreye ekler.
        self.model.submitAll() #modelde .submitAll()'ı çağırarak değişiklikleri veritabanına gönderir.
        self.model.select() # veritabanındaki verileri modele yeniden yükler.

    def deleteContact(self, row): #Veri tabanından kişiyi kaldırmak için. 
        self.model.removeRow(row) #Seçili olanı kaldırmak için
        self.model.submitAll() #Değişiklik veri tabanına gönderilir.
        self.model.select() #Veritabanındaki veriler modele yeniden yüklenir.

    def clearContacts(self):
        # Veri tabanındaki tüm kişileri kaldırmak için. 
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit) #veri modelinin .editStrategy özelliğini QSqlTableModel.OnManualSubmit olarak ayarlar.
        # .submitAll() öğesini çağırana kadar tüm değişiklikleri önbelleğe almanıza olanak tanır.
        self.model.removeRows(0, self.model.rowCount()) #tüm satırları modelden kaldırır.
        self.model.submitAll() #değişiklikleri veritabanına kaydeder.
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange) #modelin .editStrategy özelliğini orijinal değeri olan QSqlTableModel.OnFieldChange'e sıfırlar.
        # orijinal değerine sıfırlamazsanız, kişileri doğrudan tablo görünümünde güncelleyemezsiniz.
        self.model.select() #verileri modele yeniden yükler.