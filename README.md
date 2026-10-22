# Mustafa Mert Demir · Özgeçmiş

Türkçe ve İngilizce, mobil uyumlu ve A4 baskıya hazırlanmış HTML özgeçmişler. Framework, derleme veya dış kaynak bağlantısı gerektirmez; fontlar HTML içine gömülüdür.

Tasarım, kullanıcının paylaştığı CV’deki mavi sol sütun ve beyaz içerik alanından esinlenir. İletişim, teknik yetkinlikler ve dil bilgisi sol sütunda; isim, profil, deneyim, projeler ve eğitim sağda yer alır. Lacivert başlıklar ve kırmızı vurgular her iki dilde de kullanılır. Mobil ekranlarda sütunlar alt alta sıralanır.

## Sürümler

- `index.html`: Türkçe CV; referanssız ve referanslı PDF seçenekleri.
- `cv-en.html`: Avrupa iş başvurularına yönelik, tamamen İngilizce CV. Standart bölüm başlıkları, ters kronolojik tarih düzeni, uluslararası telefon numarası ve CEFR dil seviyesi içerir. Doğum tarihi, medeni durum, askerlik ve referans kişilerin iletişim bilgileri bu sürümde yer almaz. Bu sürüm resmî Europass şablonu değildir.

Sayfalardaki TR / EN bağlantıları ile dil değiştirilebilir. İngilizce PDF: `downloads/Mustafa-Mert-Demir-CV-European-EN.pdf`.

## Kullanım

`index.html` dosyasını tarayıcıda açın veya depo dizininden `python3 -m http.server 8000 --bind 127.0.0.1` komutuyla yerel olarak sunun.

- **PDF indir:** Hazırlanmış bir sayfalık PDF’yi indirir.
- **PDF’ye referans sayfasını da ekle:** İndirme ve yazdırma için iki sayfalık sürümü seçer.
- **Yazdır:** Tarayıcının yazdırma penceresini açar. PDF olarak kaydederken A4, %100 ölçek, kenar boşluğu yok ve üst/alt bilgiler kapalı ayarlarını kullanın.

`downloads/` klasöründe referanslı ve referanssız PDF sürümleri bulunur. HTML içeriğini değiştirdiğinizde indirme dosyalarını da yeniden üretin. Tüm klasörü birlikte taşıyın; HTML kendi başına açılır ve yazdırılabilir, PDF indirme bağlantıları `downloads/` klasörünü gerektirir.

## PDF’leri yeniden üretme

Python 3, Playwright Python paketi ve Chromium gerekir. Bu bulut ortamında hazırdır:

```sh
python3 scripts/export_pdf.py
```

Betik `/usr/bin/chromium` kullanır. Başka bir sistemde bu yolu kendi Chromium kurulumunuza göre değiştirin. PDF’ler HTML’nin gerçek baskı görünümünden üretilir; metin seçilebilir, bağlantılar tıklanabilir.

## İçerik

İçerik, kullanıcının sağladığı özgün CV’den düzenlenmiştir. Proje başarısı, metrik, çalışma süresi veya yeni bir yetkinlik eklenmemiştir. Türkçe sürümde iletişim ve kişisel bilgiler korunmuştur. Referansların adları ve görevleri sol sütundadır; ayrıntılı iletişim bilgileri isteğe bağlı ikinci sayfaya eklenir. İngilizce sürümde eğitim devam ediyor olarak belirtilir; B2 dil seviyesi için sınav veya sertifika iddiası eklenmez. Web sitesi için barındırma veya dağıtım ayarı yapılmamıştır.
