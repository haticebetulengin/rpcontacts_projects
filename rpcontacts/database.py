from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery() #tablo oluşturacağız.
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(databaseName): #veritabanı oluşturuyoruz. bir dosya veriyoruz. 
    #"""Create and open a database connection."""
   
     #Eğer gönderdiğimiz isimde veritabanı dosyası yoksa dosya oluşturuyor. 
     #Varsa dosyaya bağlanıyor.
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    #Bağlantı sağlanmıyorsa, hata gösterir. 
    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createContactsTable()
    return True