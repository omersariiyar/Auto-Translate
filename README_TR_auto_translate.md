# Auto Translate - Gerçek Zamanlı Çeviri Aracı

## 📋 Genel Bakış

**Auto Translate**, yazdığınız metni otomatik olarak çeviren güçlü bir Python tabanlı araçtır. Bilgisayarınızın herhangi bir yerinde cümle yazın, noktalama işaretiyle bitirin (`.`, `!`, `?`, vb.) ve anında hedef dilinize çevrilmesini izleyin!

## ✨ Özellikler

- 🌍 **Evrensel Çeviri**: Tarayıcılar, metin editörleri, sohbet uygulamaları gibi her uygulamada çalışır
- 🚀 **Gerçek Zamanlı İşleme**: Yazmayı bitirdiğinizde anında çeviri
- 🎯 **Akıllı Algılama**: Kaynak dili otomatik olarak algılar
- 📝 **Çoklu Noktalama Desteği**: `.`, `!`, `?`, `:`, `;` işaretlerini cümle sonu olarak tanır
- 💾 **Pano Güvenliği**: Orijinal pano içeriğinizi korur
- 🔤 **Otomatik Büyük Harf**: Çevirinin ilk harfinin büyük olmasını sağlar
- 📏 **Akıllı Boşluk**: Cümleler arasına otomatik boşluk ekler
- 🐛 **Debug Modu**: Sorun giderme için yerleşik hata ayıklama

## 🛠️ Kurulum

### Gereksinimler

- Python 3.7 veya üzeri
- pip (Python paket yöneticisi)

### Gerekli Kütüphaneler

Tüm bağımlılıkları tek komutla yükleyin:

```bash
pip install deep-translator pynput pyperclip
```

Ya da tek tek yükleyin:

```bash
pip install deep-translator
pip install pynput
pip install pyperclip
```

### Kütüphane Detayları

- **deep-translator**: Google Translate API üzerinden çeviri işlemlerini yönetir (API anahtarı gerekmez!)
- **pynput**: Klavye girişini global olarak yakalar
- **pyperclip**: Pano işlemlerini yönetir

> **Not**: `deep-translator`, API anahtarı gerektirmeden Google Translate'e ücretsiz erişim sağlar. Resmi olmayan web arayüzünü kullanır.

## 🚀 Kullanım

### Uygulamayı Başlatma

#### Yöntem 1: Komut Satırı Kullanarak

1. Terminal/komut istemcisini açın
2. Script dizinine gidin:
   ```bash
   cd "C:\Program Files\Auto_Translate"
   ```
3. Script'i çalıştırın:
   ```bash
   python auto_translate.py
   ```

#### Yöntem 2: Batch Dosyası Kullanarak (Hızlı Başlatma)

Daha hızlı erişim için dahil edilen `auto_translate.bat` dosyasını kullanın:

1. `auto_translate.bat` dosyasını bir metin editöründe açın
2. Script konumunuza göre yolu güncelleyin:
   ```batch
   @echo off
   cd C:\Program Files\Auto_Translate
   python auto_translate.py
   pause
   ```
3. Dosyayı kaydedin
4. Çalıştırmak için `auto_translate.bat` dosyasına çift tıklayın

> **İpucu**: Anında erişim için masaüstünüze `auto_translate.bat` kısayolu oluşturun!

### Yapılandırma

Uygulamayı başlattığınızda şunu göreceksiniz:

```
============================================================
Auto Translate Listener
============================================================
Target language: EN
Usage:
  • Type anywhere
  • End your sentence with a period (.), exclamation (!), question mark (?), etc.
  • It will automatically translate and replace
  • Press ESC to exit
============================================================

Would you like to change the target language? (en/tr/de/fr/es/az etc.)
Default: en (English)
Target language code (Enter = default):
```

**Desteklenen Dil Kodları:**
- `en` - İngilizce
- `tr` - Türkçe
- `de` - Almanca
- `fr` - Fransızca
- `es` - İspanyolca
- `az` - Azerice
- `ru` - Rusça
- `ja` - Japonca
- `zh` - Çince
- Ve daha fazlası...

### Nasıl Çalışır

1. **Cümlenizi Yazın**: Herhangi bir uygulamada yazmaya başlayın
2. **Noktalama ile Bitirin**: `.`, `!`, `?`, `:` veya `;` ile sonlandırın
3. **Sihri İzleyin**: Cümleniz otomatik olarak çevrilir ve değiştirilir
4. **Yazmaya Devam Edin**: Bir sonraki cümle uygun boşlukla gelecektir

### Örnek

**Girdi:** `Hello world.`  
**Çıktı:** `Merhaba dünya.`

**Girdi:** `Merhaba dünya. How are you?`  
**Çıktı:** `Merhaba dünya. Nasılsın?`

## ⚙️ Teknik Detaylar

### Mimari

Uygulama çok iş parçacıklı bir mimari kullanır:

1. **Ana İş Parçacığı**: Klavye dinleyicisini çalıştırır
2. **Çeviri İş Parçacığı**: API çağrılarını girişi engellemeden yönetir
3. **Değiştirme İş Parçacığı**: Metin değiştirme işlemlerini yönetir

### Temel Bileşenler

#### 1. Klavye Dinleyici (`on_press`)
- Tüm tuş vuruşlarını global olarak yakalar
- Noktalama algılanana kadar karakterleri tamponlar
- Özel tuşları işler (Boşluk, Enter, Backspace, ESC)

#### 2. Çeviri Motoru (`translate_text`)
- `deep-translator` üzerinden Google Translate kullanır
- Otomatik kaynak dil algılama
- Orijinal metne geri dönüşlü hata yönetimi

#### 3. Metin Değiştirme (`replace_sentence_with_translation`)
- Shift+Sol Ok kullanarak yazılan metni seçer
- Orijinal cümleyi siler
- Çevrilmiş metni uygun formatlama ile yapıştırır
- Pano içeriğini korur

#### 4. Cümle İşleme (`process_sentence`)
- Çeviriden önce boşluk gerekip gerekmediğini belirler
- Tampon yaşam döngüsünü yönetir
- Çeviri ve değiştirmeyi koordine eder

### Detaylı Özellikler

#### Akıllı Boşluk
Araç, cümlenizin boşlukla başlayıp başlamadığını algılar:
- **İlk cümle**: Başta boşluk yok
- **Sonraki cümleler**: Otomatik olarak boşluk ekler

#### Büyük Harf Kullanımı
Her çevrilmiş cümle büyük harfle başlar, doğru dilbilgisi sağlar.

#### Noktalama Koruma
Orijinal noktalama işaretleri korunur:
- Girdi: `Hello!` → Çıktı: `Merhaba!`
- Girdi: `How are you?` → Çıktı: `Nasılsın?`

## 🐛 Debug Modu

Uygulama, sorun giderme için debug çıktısı içerir:

```
Debug: Buffer length=5, Punctuation='.', Total to delete=6, Space needed=False
✓ 'hello' → 'Hello.'
```

Bu şunları gösterir:
- Tamponda bulunan karakterler
- Kullanılan noktalama işareti
- Silinecek karakter sayısı
- Boşluk gerekip gerekmediği
- Orijinal ve çevrilmiş metin

## ⚠️ Sınırlamalar

1. **Hız Sınırı**: Çok sık çeviri yaparsanız Google Translate istekleri sınırlayabilir
2. **Karakter Sınırı**: Çeviri başına ~5000 karakter
3. **İnternet Gerekli**: Aktif internet bağlantısı gerektirir
4. **API Bağımlılığı**: Resmi olmayan Google Translate erişimine dayanır

## 🔧 Sorun Giderme

### Çeviri Çalışmıyor
- İnternet bağlantısını kontrol edin
- `deep-translator` kütüphanesinin doğru yüklendiğini doğrulayın
- Çeviri sıklığını azaltmayı deneyin

### Metin Seçim Sorunları
- Koddaki zamanlama gecikmelerini artırın (`time.sleep()` değerlerini ayarlayın)
- Uygulamanızın pano işlemlerini destekleyip desteklemediğini kontrol edin

### Klavye Girişi Algılanmıyor
- Script'i yönetici yetkileriyle çalıştırın
- `pynput` kütüphanesinin gerekli izinlere sahip olduğundan emin olun

## 📝 Yapılandırma Seçenekleri

### Zamanlama Ayarlama

Çeviriler çok hızlı/yavaşsa, koddaki bu değerleri değiştirin:

```python
time.sleep(0.003)  # Seçim hızı
time.sleep(0.05)   # Silme işlemi
time.sleep(0.1)    # Değiştirme işlemi
```

### Cümle Sonu Ekleme

`sentence_end_chars` listesini düzenleyin:

```python
sentence_end_chars = ['.', '!', '?', ':', ';', '…']  # Daha fazla ekleyin
```

## 🔒 Gizlilik ve Güvenlik

- Tüm çeviriler Google Translate sunucuları üzerinden işlenir
- Bu uygulama tarafından yerel olarak hiçbir veri saklanmaz
- Pano içeriği her işlemden sonra geri yüklenir
- Klavye girişi yalnızca izlenir, günlüğe kaydedilmez

## 👨‍💻 Geliştirici Bilgileri

- **Yazar**: omre (RedStains)
- **Website**: redstains.com
- **Lisans**: Lisans detayları için repository'yi kontrol edin

## 🆘 Destek

Sorunlar, sorular veya katkılar için:
1. Hatalar için debug çıktısını kontrol edin
2. Tüm bağımlılıkların yüklü olduğunu doğrulayın
3. En son sürüme sahip olduğunuzdan emin olun

## 📜 Sürüm Geçmişi

- **v1.0**: Temel çeviri ile ilk sürüm
- **v1.1**: Akıllı boşluk ve büyük harf eklendi
- **v1.2**: Geliştirilmiş pano yönetimi
- **v1.3**: Debug modu ve hata yönetimi

---

**RedStains tarafından ❤️ ile yapıldı**  
*Her yerde yazarken çevir!*