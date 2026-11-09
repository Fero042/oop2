# -------------------------------------------------
# encapsulation nedir?
# melumatlari ve methodlari bir yerde saxlamaq ve xarice gizli saxlamaq prinsipi ile isleyir.
# melumatlari yalniz xususi methodlarla(feddter/setterle) elde edilir.

# class BankHesabi:
#     def __init__(self,hesab_nomresi,sahibi,ilkin_balans):
#         self.__hesab_nomresi=hesab_nomresi
#         self.__sahibi=sahibi
#         self.__balans=ilkin_balans
#         self._emeliyyat_sayi=0
#         self.__emeliyyatlar=[]
#         print(f'Hesab yaradildi: {self.__hesab_nomresi}')
#     # GETTER methodlar
#     def get_balans(self):
#         return self.__balans
#     def get_hesab_nomresi(self):
#         return self.__hesab_nomresi
#     def get_sahibi(self):
#         return self.__sahibi
#     # SETTER methodlar
#     def pul_yatir(self,mebleg):
#         # bu method pul yatirmaq methodudur ve args olmasinin sebebi mebleg= Yaradilacaq meblege beraber olmasidir
#         if mebleg>0:
#             self.__balans+=mebleg
#             self._emeliyyat_sayi+=1
#             self.__emeliyyatlar.append(f'[self.emeliyyat_sayi] Pul yatirildi:{mebleg}')
#             print(f'{mebleg} AZN yatirildi. Yeni balans:{self.__balans} AZN')
#             return True
#         else:
#             print("Sehv mebleg. Musbet mebleg daxil edin.")
#             return False

#     def pul_cixart(self,mebleg):
#         # pul cixartmaq methodu ucun iki esas prinsip var burada:
#         # 1)mebleg musbet olmalidir
#         # 2)balansda kifayet qeder pul olmalidir
#         if mebleg<=0:
#             print('sehv mebleg')
#             return False
#         if mebleg>self.__balans:
#             print(f'Kifayet qeder balans yoxdur. Movcud balans: {self.__balans} AZN')
#             return False
#         self.__balans-=mebleg
#         self._emeliyyat_sayi-=1
#         self.__emeliyyatlar.append(f'[{self.__balans}]-{mebleg} AZN cixarildi')
#         print(f'{mebleg} AZN pul cixarildi. Qalan balans: {self.__balans} AZN')

#     def pul_kocurt(self,diger_hesab,mebleg):
#         # basqa hesaba pul kocurtmek ucun
#         # esas iki emeliyyat var:
#         # 1)bu hesabdan pulu cixartmaq
#         # 2)diger hesaba pulu yatirmaq
#         if self.pul_cixart(mebleg):
#             if diger_hesab.pul_yatir(mebleg):
#                 print(f'{mebleg} AZN kocuruldu => {diger_hesab.get_hesab()}')
#                 return True
#         return False

#     def emeliyyatlari_goster(self):
#         # emeliyyat tarixcesini gostermek ucun
#         print(f'Hesab: {self.__hesab_nomresi} | Sahib:{self.__sahibi}')
#         if self.__emeliyyatlar:
#             for emeliyyat in self.__emeliyyatlar:
#                 print(emeliyyat)
#         else:
#             print("Hesabda emeliyyat yoxdur")

# hesab1=BankHesabi('AZ001','Ramin Hidayetov',3000)
# hesab2=BankHesabi('AZ002','Orxan Allahyarov',7000)

# print(f'{hesab1.get_sahibi()} Balans:{hesab1.get_balans()} AZN')
# print(f'{hesab2.get_sahibi()} Balans:{hesab2.get_balans()} AZN')

# # hesab1.pul_yatir(1000)
# # hesab2.pul_yatir(2000)

# # hesab1.pul_cixart(300)
# hesab2.pul_kocurt(hesab1,200)
# print(f'{hesab1.get_sahibi()} Balans: {hesab2.get_balans()} AZN')

    # ---------------------------------------

# class Isci:
#     # isci sinifi
#     sirket_ad='compar academy'


#     def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi):
#         self.ad=ad
#         self.soyad=soyad
#         self.iscinin_id=iscinin_id
#         self.ise_qebul_tarixi=iscinin_ise_qebul_tarixi
#         self.aktiv=True
#         print(f'isci yaradildi:{self.tam_ad()}')

#     def tam_ad(self):
#         # iscinin tam adini qaytarir
#         return f'{self.ad}{self.soyad}'

#     def ise_basla(self):
#         print(f'{self.tam_ad()} ise basladi.')

#     def ise_son_ver(self):
#         print(f'{self.tam_ad()} isden cixdi.')

#     def melumatlari_goster(self):
#         # iscinin melumatlarini gosterir
#         print(f'isci id: {self.iscinin_id}')
#         print(f'ad soyad: {self.tam_ad()}')
#         print(f'ise qebul tarixi: {self.ise_qebul_tarixi}')
#         print(f'sirket: {self.sirket_ad}')
#         print(f'aktivlik: {'aktiv' if self.aktiv else 'deaktiv'}')

# class Proqramci(Isci):
#     def __init__(self, ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi,proqramlasdirma_dilleri,tecrube_ili):
#         super().__init__(ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi)
#         self.proqramlasdirma_dilleri=proqramlasdirma_dilleri
#         self.tecrube_ili=tecrube_ili
#         self.proyektler=[]

#     def kod_yaz(self,proyekt_adi):
#         print(f'{self.tam_ad()} {proyekt_adi} proyektinde yazir.')
#         self.proyektler.append(proyekt_adi)

#     def melumatlari_goster(self):
#         super().melumatlari_goster()
#         print(f'vezife:proqramci')
#         print(f'diller:{','.join(self.proqramlasdirma_dilleri)}')
#         print(f'tecrube ili: {self.tecrube_ili}')
#         print(f'proyektler: {len(self.proyektler)} eded')

# class Manager(Isci):
#     def __init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi,komanda_hecmi):
#         super().__init__(self,ad,soyad,iscinin_id,iscinin_ise_qebul_tarixi)
#         self.komanda_hecmi=komanda_hecmi
#         self.komanda=[]

#     def komandaya_isci_elave_et(self,isci):
#         if(len(self.komanda)<self.komanda_hecmi):
#             self.komanda.append(isci)
#             print(f'{isci.tam_ad()} menecerin komandasina elave edildi.')
#             print(f'Manager: {self.tam_ad()}')
#         else:
#             print(f'komanda hecmi doludur. max hecmi: {self.komanda_hecmi}')

#     def gorus_teskil_et(self):
#         print(f'{self.tam_ad()} gorus teskil edir.')
#         print(f'istirakcilar: {len(self.komanda)} nefer')
#         for isci in self.komanda:
#             print(f'{isci.tam_ad()}')

#     def melumatlari_goster(self):
#         super().melumatlari_goster()
#         print(f'vezife:menecer')
#         print(f'komanda hecmi:{self.komanda_hecmi}')
#         print(f'komanda: {len(self.komanda)} eded')

# proqramci1=Proqramci('Ramin','Hidayetov','C001','2020-05-10',['Python','Javascript'],3)
# proqramci2=Proqramci('Orxan','Allahyarov','C002','2019-03-15',['Java','C#'],3)
# meneger=Manager('Aysel','Mammadova','M001','2018-01-20',5)

# proqramci1.kod_yaz('E-commerce sayti')
# proqramci2.kod_yaz('Mobil tetbiq')
# meneger.komandaya_isci_elave_et(proqramci1)
# meneger.komandaya_isci_elave_et(proqramci2)

# meneger.gorus_teskil_et()
# proqramci1.melumatlari_goster()
# meneger.melumatlari_goster()

# ----------------------------------------------------------------
# polymorphism nedir?
# eyni metodun ferqli sinifler ucun ferqli sekilde islemesi demekdir.

# from abc import ABC, abstractmethod
# import math

# class OdenisYontemi(ABC):
#     def __init__(self,sahibi):
#         self.sahibi=sahibi
#     @abstractmethod
#     def odeme_et(self,mebleg):
#         pass
#     def qebz_cap_et(self,mebleg):
#         print(f'Qebz: {self.sahibi} - {mebleg} AZN odendi.')

# class KrediKarti(OdenisYontemi):
#     def __init__(self,sahibi,kart_nomresi,son_istifade_tarixi,cvv):
#         super().__init__(sahibi)
#         self.kart_nomresi=kart_nomresi
#         self.son_istifade_tarixi=son_istifade_tarixi
#         self.__cvv=cvv # private - tehlukesizlik ucun

#     def odeme_et(self, mebleg):
#         print(f'Kredit karti ile odenis')
#         print(f'Kart: **** **** **** {self.kart_nomresi[-4:]}')
#         print("odenis ugurlu oldu")
#         self.qebz_cap_et(mebleg)
#         return True

# class Nagdpul(OdenisYontemi):
#     def odeme_et(self, mebleg):
#         print('nagd pul ile odenis')
#         print(f'Mebleg: {mebleg} AZN')
#         print('odenis ugurlu oldu')
#         self.qebz_cap_et(mebleg)
#         return True
# class MobilOdenis(OdenisYontemi):
#     def __init__(self, sahibi,telefon_nomresi,operator):
#         super().__init__(sahibi)
#         self.telefon_nomresi=telefon_nomresi
#         self.operator=operator

#     def odeme_et(self, mebleg):
#         print('mobil odenis ile odenis')
#         print(f'Operator: {self.operator}')
#         print(f'Telefon: {self.telefon_nomresi}')
#         print(f'Mebleg: {mebleg} AZN')
#         print('odenis ugurlu oldu')
#         self.qebz_cap_et(mebleg)
#         return True


# class KriptoValyuta(OdenisYontemi):
#     def __init__(self,sahibi,wallet_adres,crypto_type):
#         super().__init__(sahibi)
#         self.wallet_adres=wallet_adres
#         self.crypto_type=crypto_type

#     def odeme_et(self,mebleg):
#         print('Kripto valyuta ile odenis')
#         print(f'Valyuta: {self.crypto_type}')
#         print(f'Walet: {self.wallet_adres}')
#         print(f'Mebleg: {mebleg} AZN')
#         print('odenis ugurlu oldu')
#         self.qebz_cap_et(mebleg)
#         return True

# def odemeni_proses_et(odenis_yontemi,mebleg):
#     print('odenis prosesi baslayir...')
#     print(f'Musteri: {odenis_yontemi.sahibi}')
#     return odenis_yontemi.odeme_et(mebleg)
    
# kart=KrediKarti("Ramin Hidayetov","12345674367556763","12/25","123")
# negd=Nagdpul("Orxan Alahyarov")
# mobil=MobilOdenis("Aysel Mammadova","+9942673637378","Azercell")
# kripto=KriptoValyuta("Leyla Quliyeva","1632465679800874624","Bitcoin")

# odemeni_proses_et(kart,150)
# odemeni_proses_et(negd,75)
# odemeni_proses_et(mobil,200)
# odemeni_proses_et(kripto,500)
# print("----")

# --------------------------------------------------
# super ve MRO - method resolution order nedir?
# class Heyvan:
#     def __init__(self,ad):
#         self.ad=ad
#     def ye(self):
#         print(f'{self.ad} yemek yeyir.')

# class it(Heyvan):
#     def __init__(self,ad,cins):
#         super().__init__(ad)
#         self.cins=cins
#     def ye(self):
#         super().ye()
#         print(f'{self.ad} quyrugunu terpedir')

# It=it('Linda','Doberman')
# It.ye()

# class Ana:
#     def melumat(self):
#         print('Ana: yemek hazir edir')

# class Ata:
#     def melumat(self):
#         print('Ata: pul verdim usaqa')

# class Usaq(Ana,Ata): #2 sinifdende miras alib 
#     pass #salamla metodu yoxdur

# usaq=Usaq()
# usaq.melumat()

# class Ana:
#     def __init__(self,ad):
#         self.ad=ad

# class Usaq(Ana):
#     def __init__(self, ad,yas):
#         super().__init__(ad)
#         self.yas=yas

# print(Usaq.__mro__)

from abc import ABC, abstractmethod
class IckiAparati(ABC):
    """
    Abstraction
    musteri gorur: icki_hazirla()
    musteri gormur: daxili_prosesleri
    """
    def __init__(self,ad):
        self.ad=ad
        print(f'{ad} aparati hazirdir')
    # Daxili metodlar - musterinin gormediyi
    @abstractmethod
    def _mehsul_hazirla(self):
        pass

    @abstractmethod
    def _bisir(self):
        #bisirme, demlemek
        pass

    @abstractmethod
    def _fincan_doldur(self):
        pass

    # --------------------------------Public metod

    def icki_hazirla(self,boyuk_olsun=False):
        olcu="Boyuk" if boyuk_olsun else "Kicik"
        print(f'{olcu} {self.ad} hazirlanir')

    #daxili prosesler

        self._mehsul_hazirla()
        self._bisir()
        self._fincan_doldur()
        print(f'{self.ad} hazirdir nus olsun')

class KofeAparati(IckiAparati):
    def _mehsul_hazirla(self):
        print('kofe denleri uyudur')
    def _bisir(self):
        print('kofe demlenir')
    def _fincan_doldur(self):
        print('fincana tokulur')


class CayAparati(IckiAparati):
    def _mehsul_hazirla(self):
        print('cay denleri uyudur')
    def _bisir(self):
        print('cay demlenir')
    def _fincan_doldur(self):
        print('fincana tokulur')

class KakaoAparati(IckiAparati):
    def _mehsul_hazirla(self):
        print('kakao denleri uyudur')
    def _bisir(self):
        print('kakao demlenir')
    def _fincan_doldur(self):
        print('fincana tokulur')


kofe_aparati=KofeAparati('ekspresso')
cay_aparati=CayAparati("early grey")
kakao_aparati=KakaoAparati('hot chocolate')

kofe_aparati.icki_hazirla(boyuk_olsun=True)
cay_aparati.icki_hazirla()
kakao_aparati.icki_hazirla()


        
        


