import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class OgrenciNotAnalizSistemi:

    def __init__(self, dosya_yolu):
        self.dosya_yolu = dosya_yolu
        self.df = None

    def veriyi_oku(self):

        try:
            self.df = pd.read_csv(self.dosya_yolu)

            if self.df.empty:
                raise ValueError("csv dosyası boş")
            
            gerekli_sutunlar = {"isim", "yas", "bolum", "not"}

            if not gerekli_sutunlar.issubset(self.df.columns):
                raise ValueError(
                    f"csv dosyasında gerekli sütunlar eksik"
                    f"Gerekli sütunlar: {gerekli_sutunlar}"
                )
            
            self.df["not"] = pd.to_numeric(self.df["not"], errors = "raise")

            print("Veri başarıyla okundu")
            print(self.df)
        except FileNotFoundError:
            print(f"hata: {self.dosya_yolu} bulunamadı")
        except pd.errors.EmptyDataError:
            print("csv dosyası boş")
        except ValueError as error:
            print(f"hata: {error}")
        except Exception as e:
            print(f"Beklenmeyen hata: {e}")

    def numpy_ile_hesaplama(self):

        try:

            if self.df is None: 
                raise ValueError("önce veri yüklenmeli")
            
            notlar = self.df["not"].to_numpy()

            print(f"Ortalama {np.mean(notlar)}")
            print(f"En yüksek not {np.max(notlar)}")
            print(f"En düşük not {np.min(notlar)}")
            print(f"Standart sapma {np.std(notlar)}")
        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu. {e}")

    def pandas_ile_filtreleme(self):

        try:
            if self.df is None:
                raise ValueError("Önce veri okunmalıdır")
            
            print("Pandas ile filtreleme sonuçları")

            yuksek_notlular = self.df[self.df["not"] > 80]
            print(f"Notu 80 den büyük olan öğrenciler: \n{yuksek_notlular}")

            yapay_zeka_ogrencileri = self.df[self.df["bolum"] == "Yapay Zeka"]
            print(f"Bölümü yapay zeka olanlar: \n{yapay_zeka_ogrencileri}")

            yasi_buyuk_olanlar = self.df[self.df["yas"] > 22]
            print(f"22 yaşından büyük olanlar: \n{yasi_buyuk_olanlar}")

        except ValueError as hata:
            print(f"hata: {hata}")
        except Exception as e:
            print(f"BBeklenmeyen bir hata: {e}")

    def grafik_ciz(self):

        try:
            if self.df is None:
                raise ValueError("önce veri okunmalı")
            
            plt.figure(figsize=(10, 5))

            plt.bar(self.df["isim"], self.df["not"])
            plt.title("Öğrenci Not Grafiği")
            plt.xlabel("Öğrenci İsimleri")
            plt.ylabel("Notlar")

            plt.tight_layout() 

            plt.show()

        except Exception as e:
            print(f"hata: {e}")

    def tum_analizi_calistir(self):

        self.veriyi_oku()

        if self.df is None:
            print("analiz durduruldu")
            return
        
        self.numpy_ile_hesaplama()

        self.pandas_ile_filtreleme()

        self.grafik_ciz()

if __name__ == "__main__":
    
    dosya_yolu = "ogrenci_notlari.csv"
    sistem = OgrenciNotAnalizSistemi(dosya_yolu)

    sistem.tum_analizi_calistir()