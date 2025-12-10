# GNN ve Pekiştirmeli Öğrenme ile Otonom Kod Analizi (Auto-Code Explorer)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)
![GNN](https://img.shields.io/badge/Architecture-GNN%20%2B%20PPO-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Proje Hakkında

Bu proje, Python kaynak kodlarını analiz ederek yapılarını öğrenen ve bu kodlar üzerinde otonom olarak gezinen bir **Yapay Zeka Ajanı** geliştirilmesini amaçlar.

Sistem, ham Python kodunu **Kontrol Akış Grafiklerine (Control Flow Graph - CFG)** dönüştürür ve **Graf Sinir Ağları (Graph Neural Networks - GNN)** ile güçlendirilmiş bir **PPO (Proximal Policy Optimization)** ajanı kullanarak kodun tüm dallarını (code coverage) keşfetmeye çalışır. Bu, yazılım test süreçlerinde otonom test senaryosu üretimi ve kod analizi için deneysel bir yaklaşımdır.

## 🎯 Amaç

Projenin temel amacı, bir yapay zeka ajanının, kodun ne işe yaradığını bilmeden sadece **yapısal özelliklerine (topoloji)** bakarak:
1.  Kodun akışını anlamasını,
2.  Mantıksal dallanmaları (If/Else, Loops) çözmesini,
3.  Ziyaret edilmemiş kod satırlarına ulaşmak için strateji geliştirmesini sağlamaktır.

## ⚙️ Teknik Mimari ve Çalışma Mantığı

Sistem 3 ana aşamadan oluşur:

### 1. Statik Analiz (AST'den CFG'ye)
Python'un `ast` modülü kullanılarak kaynak kodlar analiz edilir. `ControlFlowVisitor` sınıfı, kodun **Soyut Sözdizimi Ağacını (AST)** çıkarır ve bunu yönlendirilmiş bir grafa (CFG) dönüştürür.
* **Düğümler (Nodes):** Kod bloklarını temsil eder (Fonksiyon tanımları, döngüler, koşul ifadeleri).
* **Kenarlar (Edges):** Kodun akış yönünü gösterir.

### 2. Graf Ortamı (RL Environment)
Özel olarak geliştirilen `GrafOrtami`, ajan için bir oyun alanı görevi görür.
* **Durum (State):** Grafın o anki yapısı + Hangi düğümlerin ziyaret edildiğini gösteren bir maske vektörü.
* **Ödül Mekanizması:**
    * `+20 Puan`: Yeni bir düğüm keşfedildiğinde.
    * `+200 Puan`: Kodun tamamı (%100) keşfedildiğinde.
    * Ceza: Tekrar eden hareketler veya geçersiz adımlar için.

### 3. Ajan Modeli (Actor-Critic GNN)
Model, graf verilerini işlemek için **PyTorch Geometric** kullanır.
* **GCN Katmanları:** Kodun topolojik yapısını öğrenir.
* **Actor:** Hangi kod bloğuna gidileceğine karar verir.
* **Critic:** Mevcut durumun ne kadar değerli olduğunu tahmin eder.

## 📊 Test Sonuçları

Eğitilen model, basit matematiksel işlemlerden karmaşık desen yazdırma algoritmalarına kadar **66 farklı Python dosyası** üzerinde test edilmiştir.

| Metrik | Değer |
| :--- | :--- |
| **Toplam Test Edilen Dosya** | 66 |
| **Tamamen Çözülen (%100 Keşif)** | 16 |
| **Genel Başarı Oranı** | **%24.24** |
| **Ortalama Adım (Başarılı)** | 5.25 |
| **Ortalama Ödül (Başarılı)** | 305.00 |

### ✅ Başarıyla Çözülen Algoritmalar
Ajanın %100 kapsama oranına ulaştığı bazı dosya türleri:
* `factorial_analysis.py` (Faktöriyel Hesabı)
* `find_divisors.py` (Bölenleri Bulma)
* `sort_words_alphabetically.py` (Sıralama Algoritmaları)
* `reverse_string.py` (Metin Ters Çevirme)
* `odd_even_analysis.py` (Tek/Çift Sayı Analizi)
* `mean_analysis.py` (Ortalama Hesaplama)

*Not: Ajan, doğrusal ve basit dallanmalara sahip algoritmalarda mükemmel performans gösterirken, çok katmanlı iç içe döngüler içeren karmaşık desen (pattern printing) kodlarında henüz gelişim aşamasındadır.*

## 🛠️ Kurulum ve Kullanım

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install torch torchvision torchaudio
    pip install torch_geometric
    pip install graphviz
    # Linux kullanıcıları için ayrıca: sudo apt-get install graphviz libgraphviz-dev
    ```

2.  **Veri Setini Hazırlayın:**
    Analiz edilecek `.py` dosyalarınızı bir klasöre yerleştirin.

3.  **Eğitim (Training):**
    Notebook içerisindeki `ana_egitim_dongusu_genel()` fonksiyonunu çalıştırarak ajanı eğitebilirsiniz.

4.  **Test (Testing):**
    Eğitilen modeli değerlendirmek için:
    ```python
    test_genel_ajan()
    ```
---
*Bu proje, kod analizi ve yapay zeka alanındaki deneysel bir çalışmadır.*
