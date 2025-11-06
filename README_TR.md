# Azerbaycan Türkçesi Otomatik Düzeltme Aracı

Hem manuel karakter ekleme hem de Türkçe/ASCII transkripsiyon metinlerinden ə karakteri ile doğru Azerbaycan Türkçesi formlarına akıllı otomatik kelime düzeltmesi sağlayan güçlü bir sistem çapında klavye otomasyon aracı.

## 🚀 Özellikler

- **🎯 Manuel Kısayol**: Her yerde anında `ə` karakteri eklemek için `Ctrl + Sol Shift` tuşuna basın
- **🔄 Akıllı Otomatik Düzeltme**: Yazmayı bitirdiğinizde (boşluk/enter) Türkçe/ASCII kelimeleri otomatik olarak doğru Azerbaycan Türkçesi karşılıkları ile değiştirir
- **📚 Kapsamlı Sözlük**: Türkçe'den Azerbaycan Türkçesi'ne özenle hazırlanmış 300+ kelime eşleşmesi
- **🔤 Büyük/Küçük Harf Zekası**: Orijinal büyük/küçük harf yazımınızı korur (BÜYÜK, Başlık, küçük)
- **📝 Çok Kelimeli İfadeler**: "eleştiriliyor" → "tənqid olunur" gibi tam ifadeleri işler
- **🇹🇷 Türkçe Karakter Desteği**: Türkçe karakterler için tam destek (ç, ğ, ı, ö, ş, ü)
- **🌐 Evrensel Uyumluluk**: TÜM uygulamalarda sorunsuz çalışır (Word, tarayıcılar, sohbet uygulamaları, IDE'ler, vb.)
- **⚡ Gerçek Zamanlı İşleme**: Fark edilir gecikme olmadan anında değiştirmeler

## 📋 Ön Koşullar

- **İşletim Sistemi**: Windows 10/11
- **Python**: Sürüm 3.7 veya üzeri
- **Yetkiler**: Standart kullanıcı (yönetici yetkisi gerekmez)

## ⚙️ Kurulum

### Adım 1: Dosyaları İndirme
```bash
# Aşağıdaki dosyaları aynı klasöre indirin:
# - auto_reverse_e.py (ana program)
# - mapping.json (kelime sözlüğü)
# Örnek: C:\AutoReverse\
```

### Adım 2: Bağımlılıkları Yükleyin
```bash
pip install pynput pyperclip
```

### Adım 3: Aracı Çalıştırın
```bash
python C:\auto_reverse_e.py
```

## 💡 Kullanım Kılavuzu

### Manuel Karakter Girişi
- **Kısayol**: `Ctrl + Sol Shift` → anında `ə` yazar
- Sisteminizdeki herhangi bir metin alanında çalışır

### Otomatik Kelime Düzeltme
Türkçe kelimeleri doğal olarak yazın ve `Boşluk` veya `Enter` tuşuna basın:

```
Yazın: "aziz" + Boşluk → Sonuç: "əziz "
Yazın: "eleştiriliyor" + Boşluk → Sonuç: "tənqid olunur "
Yazın: "meseleler" + Enter → Sonuç: "məsələlər "
Yazın: "HASTA" + Boşluk → Sonuç: "XƏSTƏ "
Yazın: "Gazete" + Boşluk → Sonuç: "Qəzet "
```

### 📖 Popüler Eşleşmeler

| Türkçe/ASCII | Azerbaycan Türkçesi | Anlamı |
|---------------|---------------------|--------|
| aziz | əziz | sevgili |
| evvel | əvvəl | ilk/önce |
| eleştiriliyor | tənqid olunur | eleştiriliyor |
| meseleler | məsələlər | sorunlar |
| hasta | xəstə | hasta |
| gazete | qəzet | gazete |
| öğretmen | müəllim | öğretmen |
| sabah | səhər | sabah |
| bilgi | məlumat | bilgi |
| değil | deyil | değil |

## 🔧 Nasıl Çalışır

### Mimari
1. **📂 Sözlük Yükleme**: Program başlangıcında `mapping.json` dosyasından kelime eşleşmelerini yükler
2. **🎧 Global Dinleyici**: `pynput` kullanarak sistem çapında klavye girişini izler
3. **📝 Kelime Tamponlama**: Kelime sınırlarına kadar karakterleri akıllıca biriktirir
4. **🔍 Sözlük Araması**: Yazılan kelimeleri JSON dosyasından yüklenen eşleşme veritabanına karşı kontrol eder
5. **✨ Akıllı Değiştirme**: Eşleşme bulunduğunda:
   - Backspace simülasyonu ile orijinal kelimeyi hassas şekilde siler
   - Güvenilir Unicode karakter ekleme için panoya kullanır
   - Orijinal büyük/küçük harf desenini korur
   - Uygun boşluk ekler

### Teknik Yığın
- **JSON**: Kelime eşleşmelerini kolayca düzenlenebilir formatta saklar
- **pynput**: Çapraz platform klavye olay işleme
- **pyperclip**: Unicode desteği için güvenilir pano işlemleri
- **threading**: Engelleyici olmayan değiştirme işlemleri
- **Unicode**: Azerbaycan Türkçesi karakter seti için tam destek

## 🛠️ Gelişmiş Yapılandırma

### Özel Eşleşmeler Ekleme
`mapping.json` dosyasını düzenleyerek yeni kelime eşleşmeleri ekleyebilirsiniz:

```json
{
    "turkce_kelimeniz": "azerbaycan_karsiligi",
    "merhaba": "salam",
    "teşekkürler": "təşəkkürlər",
    "yeni_kelime": "yeni_əməliyyat"
}
```

**Not**: JSON dosyasını düzenledikten sonra programı yeniden başlatmanız gerekir.

### Performans Ayarlama
- **Bellek kullanımı**: ~10-20 MB (çok hafif)
- **CPU etkisi**: Önemsiz arka plan işlemi
- **Yanıt süresi**: Çoğu değiştirme için < 50ms
- **Sözlük boyutu**: 626+ kelime eşleşmesi (JSON dosyasından otomatik yüklenir)

## ❗ Sorun Giderme

### Yaygın Sorunlar ve Çözümler

| Sorun | Çözüm |
|-------|-------|
| Betik yanıt vermiyor | Gerekirse yükseltilmiş yetkilerle çalıştırın |
| Karakterler yanlış görünüyor | Hedef uygulamanın Unicode desteklediğinden emin olun |
| İçe aktarma hataları | `pip install pynput pyperclip` |
| Değiştirme çalışmıyor | Kelimenin eşleşme sözlüğünde var olup olmadığını kontrol edin |
| Performans sorunları | Gereksiz arka plan uygulamalarını kapatın |

### Aracı Durdurma
- **Nazik çıkış**: `ESC` tuşuna basın
- **Zorla çıkış**: Terminalde `Ctrl+C`
- **Görev Yöneticisi**: Donmuşsa python.exe işlemini sonlandırın

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Şu şekillerde yardımcı olabilirsiniz:
- 📝 Yeni Türkçe → Azerbaycan Türkçesi kelime eşleşmeleri ekleme
- 🐛 Hataları ve sorunları bildirme
- ⚡ Performans optimizasyonları
- 🌐 Diğer diller için destek ekleme
- 📚 Dokümantasyonu iyileştirme

## 📄 Lisans

Bu proje açık kaynaklıdır ve **MIT Lisansı** altında sunulmaktadır.

## 🖥️ Sistem Gereksinimleri

| Bileşen | Gereksinim |
|---------|------------|
| **İS** | Windows 10/11 (64-bit önerilir) |
| **Python** | 3.7+ |
| **RAM** | 50MB kullanılabilir bellek |
| **Depolama** | 5MB disk alanı |
| **Ağ** | Gerekli değil (çevrimdışı çalışır) |

## 🔥 Profesyonel İpuçları

- **Başlangıç**: Otomatik başlatma için Windows başlangıcına ekleyin
- **Verimlilik**: Daha hızlı yazım için yaygın eşleşmeleri öğrenin
- **Yedekleme**: Özel eşleşmelerinizi yedekli tutun
- **Güncellemeler**: Kelime sözlüğünü düzenli olarak güncelleyin
- **Entegrasyon**: Otomatik tamamlama ve yazım denetleyicileri ile mükemmel çalışır

## 🏷️ Sürüm Bilgisi

- **Mevcut Sürüm**: 2.0
- **Son Güncelleme**: Kasım 2024
- **Uyumluluk**: Windows 10/11, Python 3.7+
- **Durum**: Aktif olarak sürdürülmektedir

---

*Türkçe yazımınızı mükemmel Azerbaycan Türkçesi'ne zahmetsizce dönüştürün!*
