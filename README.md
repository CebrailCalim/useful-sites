# Teknoloji Bağlantıları / Technology Links

Yazılım, yapay zeka, güvenlik, donanım ve bilim üzerine derlenmiş **717
bağlantılık** bir dizin. Her kayıtta bağlantının **ne yaptığı** ve
**benzerlerinden nerede ayrıldığı** yazılı. Türkçe ve İngilizce.

A directory of 717 links on software, AI, security, hardware and science.
Every entry states what the thing does and where it parts ways with its
neighbours. Turkish and English.

---

## Neden / Why

Bağlantı listeleri genelde bir yığın URL'dir; hangisinin ne olduğunu anlamak
için hepsini tek tek açman gerekir. Buradaki her kayıt bir açıklama ve
kanonik etiketler taşıyor, böylece tıklamadan önce ne olduğunu biliyorsun.

Most link lists are a pile of URLs — you have to open each one to find out what
it is. Here every entry carries a description and canonical tags, so you know
before you click.

## Özellikler / Features

- Anlık arama — isim, açıklama, etiket ve alan adında, Türkçe karakter duyarsız
- 63 kanonik etiket ve 20 kategoriyle birleştirilebilir filtre
- **Kaynak ayrımı** — kendi arşivinden gelen kayıtlar ile dış listelerden
  alınanlar ayrı işaretli ve ayrı süzülebiliyor
- **Kategori giriş metinleri** — her başlıkta neye bakılacağını anlatan iki cümle
- **İlgili kayıtlar** — her satırda etiket örtüşmesine göre üç komşu bağlantı
- **Kayıt bazında son doğrulama tarihi** (rozetin üstüne gelince)
- Sıralama: kategori · A→Z · önce yeni eklenen
- **Başlangıç noktaları** — kategori başına 2-3 kayıt işaretli, tek düğmeyle süzülüyor
- **Durum URL'de** — filtrelediğin görünüm paylaşılabilir, tarayıcı geri tuşu çalışır
- Satır başına iki bağlantı, kategori başına 20'lik sayfalama
- TR / EN — İngilizce açıklamalar ayrı dosyada, sadece gerekince yükleniyor
- Açık / koyu tema, `prefers-reduced-motion` desteği
- Klavye: `/` ara · `r` rastgele bağlantı aç · `Esc` temizle
- Sıfır bağımlılık, sıfır dış istek (font, CDN, analitik yok)

## Yapı / Structure

```
index.html          tüm arayüz — CSS ve JS gömülü, ~26 KB
links.js            çekirdek veri + Türkçe açıklamalar  (ilk yükleme)
links.en.js         İngilizce açıklamalar               (dil değişince)
data/               derleme betikleri ve ham çıktılar
.github/            haftalık bağlantı kontrolü + issue şablonları
```

`links.js` düz bir JavaScript dosyası olduğu için site **dosya olarak da
açılır**; sunucu gerekmez. (`fetch` ile JSON okusaydı `file://` üzerinde CORS'a
takılırdı.)

## Yayınlama / Publishing

```bash
git remote add origin git@github.com:KULLANICI/REPO.git
git push -u origin main
```

Sonra **Settings → Pages → Source: main / root**. `.nojekyll` zaten var.

Yayınladıktan sonra `index.html` içindeki `REPO` sabitini kendi depo adresinle
değiştir — altbilgideki "bildir" bağlantısı oraya gidiyor.

## Bakım / Maintenance

### Haftalık bağlantı kontrolü

`.github/workflows/link-check.yml` her pazartesi bütün bağlantıları tarıyor.
Ölü bulursa **tek bir issue** açıyor ve sonraki haftalarda aynı issue'yu
güncelliyor — her hafta yeni issue yığılmıyor.

Rapor iki başlığa ayrılıyor:

| Başlık | Anlamı |
|---|---|
| **Ölü** | 404/410 döndü ya da hiç yanıt vermedi — değiştir veya çıkar |
| **Şüpheli** | 403/429/503 — muhtemelen bot engeli, tarayıcıda açılıyor olabilir |
| **Arşivlenmiş** | GitHub deposu salt okunur — sayfa 200 döner ama bakım bitmiş |
| **Bayat** | 2+ yıldır itme yok — terk edilmiş olabilir |

Son iki satır ayrı bir denetim (`ci_github.py`). Bir kaynak 404 döndürmeden de
ölebilir: 76 bin yıldızlı `Best-websites-a-programmer-should-visit` deposu
1 Kasım 2025'te arşivlendi ve bağlantı taraması bunu göremez.

Elle çalıştırmak için: `python data/ci_check.py`

### Katkı

İki issue şablonu var: **yeni bağlantı öner** ve **hatalı/ölü kayıt bildir**.
Yeni bağlantı şablonu "ne işe yarıyor" ve "benzerlerinden farkı ne" alanlarını
zorunlu tutuyor — dizinin tek gerçek değeri o ikinci alan.

## Bağlantı eklemek / Adding a link

Kalıcı yol, `data/part_*.py` içine not yazıp yeniden derlemek:

```python
add('https://ornek.com/', 'Örnek', ['açık-kaynak', 'python'],
    'Ne yaptığı ve komşularından nerede ayrıldığı.',
    'What it does and where it differs.',
    'araclar')
```

Sonra `python data/build.py`. Etiketler `data/tags.py` içindeki 63 kanonik
etiketten seçilir; eşleşmeyen etiket `ALIAS` tablosuna eklenerek kanonik bir
karşılığa bağlanır, bağlanmazsa düşer.

Bir kaydı başlangıç noktası yapmak için URL'sini `data/picks.py` içine ekle.

Hızlı bir düzeltme için doğrudan `links.js` de düzenlenebilir, ama bir sonraki
derlemede kaybolur.

## Derleme betikleri / Build scripts

`data/` altındakiler tek seferlik derleme içindir, siteyi çalıştırmak için
gerekmez:

| Betik | İş |
|---|---|
| `extract.py` | Tarayıcı yer imi dosyasından teknoloji bağlantılarını çıkarır, ayıklar |
| `check.py` | Bağlantıların canlı olup olmadığını kontrol eder |
| `fetchmeta.py` | Her sitenin başlık/açıklama meta verisini çeker (GitHub için API) |
| `notes.py` + `part_*.py` | Küratör notları — asıl içerik burada |
| `tags.py` | 357 serbest etiketi 63 kanonik etikete indiren sözlük |
| `picks.py` | Kategori başına başlangıç noktası olarak işaretlenen kayıtlar |
| `ci_github.py` | GitHub depolarının arşiv / bayatlık denetimi |
| `sources.py` | Kayıt kökenleri (kendi arşivi / dış liste) |
| `intros.py` | Kategori giriş metinleri |
| `verified.json` | Kayıt bazında son doğrulama tarihi — CI her hafta tazeliyor |
| `build.py` | Hepsini birleştirip `links.js` ve `links.en.js` üretir |
| `ci_check.py` | GitHub Actions için bağlantı taraması ve rapor |

## Kayıt kökenleri / Provenance

Dizindeki her kaydın nereden geldiği işaretli, çünkü hepsi aynı titizlikte değil:

| Kaynak | Adet | Ne demek |
|---|---|---|
| **Kedi** | 612 | Derleyenin kendi yer imi arşivi; tek tek gözden geçirilmiş, açıklamalar projenin kendi belgelerine bakılarak yazılmış |
| **Dış liste** | 105 | [Best-websites-a-programmer-should-visit](https://github.com/sdmg15/Best-websites-a-programmer-should-visit) derlemesinden alındı; 702 bağlantıdan canlı, tekrarsız ve kapsama giren ~105'i seçildi |

Dış listeden alınanların açıklamaları da elle yazıldı ama karşılaştırmalı yargı
daha az; okuyucunun bu ayrımı görebilmesi için rozet ve süzgeç var.

## Lisans / License

Derleme, kategoriler ve açıklama metinleri **CC BY 4.0**. Bağlantı verilen
sitelerin içeriği kendi sahiplerine ve kendi lisanslarına aittir.
