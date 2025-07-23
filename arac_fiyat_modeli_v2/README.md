# 🚗 İkinci El Araç Fiyat Tahmin Uygulaması



Bu proje, ikinci el araçların çeşitli özelliklerine göre fiyat tahmini yapan bir makine öğrenmesi uygulamasıdır. Kaggle’dan alınan temizlenmiş veri seti kullanılarak model eğitilmiş, kategorik değişkenler için gömülü katmanlar (embedding) içeren bir derin öğrenme modeli (Keras ile) geliştirilmiştir. Tahmin arayüzü ise kullanıcı dostu bir şekilde Streamlit ile oluşturulmuştur.
Uygulama arayüzünde, kullanıcının girdiği özelliklere en çok benzeyen araçlar filtrelenerek, bu araçların ortalama fiyatı da ayrı bir referans olarak kullanıcıya sunulmaktadır.



## 🔧 Kullanılan Teknolojiler



- **Python**

- **TensorFlow / Keras** – Gömülü katmanlı model

- **Pandas \& NumPy** – Veri işleme

- **Scikit-learn** – Ölçekleme, encoding

- **Streamlit** – Web arayüzü

- **Kaggle Veri Seti** – \[Used Cars Dataset - Cardekho](https://www.kaggle.com/datasets/sukritchatterjee/used-cars-dataset-cardekho)





## 📂 Proje Yapısı



arac_fiyat_tahmin_v2

├── streamlit_app.py # Streamlit arayüz dosyası

├── trained_model.keras # Eğitilmiş model

├── scaler.pkl # Sayısal veriler için scaler

├── encoder.pkl # Kategorik veriler için encoder

├── data # Veri dosyaları 

├── requirements.txt # Gerekli Python paketleri

└── README.md # Bu tanıtım dosyası







## 🚀 Uygulama Nasıl Çalıştırılır?



1. Gerekli ortamı oluşturun ve bağımlılıkları kurun:

  ```bash

  pip install -r requirements.txt

Uygulamayı başlatın:



2.Uygulamayı başlatın:

streamlit run streamlit_app.py



3.Tarayıcıda açılan arayüz üzerinden araç bilgilerini girerek fiyat tahmini alın.





🧠 Model Bilgisi

Girdi Değişkenleri: Marka (OEM), model, üretim yılı, kilometre, yakıt türü, vites tipi, kasa tipi, sahibi sayısı vb.



Model Yapısı: Gömülü (embedding) katmanlar kullanılarak derin öğrenme modeli kurulmuştur.



Çıktı: Log dönüşümlü fiyat tahmini; ardından log dönüşüm ters çevrilerek gerçek fiyat değeri hesaplanır.









## 📸 Uygulama Görselleri





([streamlit_screenshot1.png](streamlit_screenshot1.png))



---



([streamlit_screenshot2.png](streamlit_screenshot2.png))











## 👩‍💻 Geliştirici



**Zeynep Cengiz**  

Hacettepe Üniversitesi, İstatistik (3. Sınıf)  

📧 zeyneppcengiz14@gmail.com  

📎 [LinkedIn][https://www.linkedin.com/in/zeynep-cengiz-61b7b4253](https://www.linkedin.com/in/zeynep-cengiz-61b7b4253)





📝 Notlar

Bu proje bireysel olarak geliştirilmiş ve veri bilimi portföyüne eklenmek üzere hazırlanmıştır.

Model, kendi bilgisayarınızda çalışacak şekilde optimize edilmiştir.

Proje, ikinci el araç sektöründe veri analitiği ve fiyat tahmini uygulamaları için temel bir örnek teşkil etmektedir.

