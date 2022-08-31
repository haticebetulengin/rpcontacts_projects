print("hello")
# Sanal çalışma alanı - virtual environment : Python orijinal kurulum yerinde değil de kopyasında çalışıyoruz.
# oyun - bir yerde 
# yapay zeka - bir yerde 
# web - bir yerde 
# böylece birbirlerine karışmıyor. 

# pip install virtualenv 
# python -m venv .venv   # ile python kopyası oluştu diyebiliriz. 
# .venv\Scripts\active   # kodunu terminale yazdık.
# Hata verdi :
# .venv\Scripts\activate : File D:\rpcontacts_projects\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.  
# For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
# At line:1 char:1
# + .venv\Scripts\activate
# + ~~~~~~~~~~~~~~~~~~~~~~
#    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
#    + FullyQualifiedErrorId : UnauthorizedAccess

# Bunu düzeltmek için; Windows PowerShell'i yönetici olarak çalıştırıp şu kodu çalıştırdık.
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
# Ctrl+Shift+P ile Select Interpreter dan .venv kısmını seçiyoruz. 
# ardından 
# pip install PyQt5 
# PyQt - görsel bir tasarım arayüzü var. 
# pip install PyQt5designer   #kur

# designer.exe yi çalıştır. 
# orada istediğin tasarımda oluşturabilirsin. sonra bunu proje dosyasına kaydet. 
# Form -> Preview bas, tasarımı görürsün.
# Yaptığın tasarımı python kodunu görmek için: Form -> View PythonCode a bas. kodları alıp projeye ekleyebilirsin.
