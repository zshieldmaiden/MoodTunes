# MoodTunes Light

🎵 Ruh haline göre Spotify çalma listesi öneren, tamamen mock veriyle çalışan Streamlit demo uygulaması.

## Özellikler
- Tek dosyada (app.py) çalışır
- 10'dan fazla mood için öneri
- Sidebar ve modern arayüz
- API anahtarı gerekmez, tüm veriler hardcoded
- Sonuçlarda fake Spotify playlist linkleri

## Kurulum
1. Depoyu klonlayın veya dosyaları indirin.
2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```
3. Uygulamayı başlatın:
   ```
   streamlit run app.py
   ```

## Kullanım
- Ana ekranda ruh halinizi yazın (ör: "mutluyum", "üzgünüm", "enerjikim" ...)
- "Müzik Öner!" butonuna tıklayın
- Size uygun Spotify playlist önerilerini ve linklerini görün

## Notlar
- Uygulama tamamen demo amaçlıdır, gerçek Spotify API'si kullanılmaz.
- Playlistler ve mood eşleşmeleri sabittir.

## Geliştirici
upschool_project 