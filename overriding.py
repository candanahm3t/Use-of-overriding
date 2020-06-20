class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çlaışan Fonksiyonun init fonksiyonu")

        self.isim = isim
        self.maaş =maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan Fonksiyonun Bilgileri")
        print("İsim: {}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maaş,self.departman))
        
    def departman_degis(self,yeni_departman):
        self.departman = yeni_departman

class Yönetici(Çalışan):

    def __init__(self,isim,maaş,departman,kişi_sayısı):
        print("Yöneticinin init foksiyonu")
        self.isim = isim
        self.maaş =maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı


    def zam_yap(self,zam_miktarı):
        self.maaş+=zam_miktarı

yönetici= Yönetici("Orhan Candan",4000,"Bilişim",10)
