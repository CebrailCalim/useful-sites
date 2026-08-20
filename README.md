# Teknoloji Bağlantıları / Technology Links

Yazılım, yapay zeka, güvenlik, donanım ve bilim üzerine elle derlenmiş bir bağlantı
dizini. Her kayıtta bağlantının **ne işe yaradığı** ve **benzerlerinden nerede
ayrıldığı** yazılı. Türkçe ve İngilizce.

A hand-curated directory of links on software, AI, security, hardware and science.
Every entry says what the thing is for and where it differs from its neighbours.
Turkish and English.

---

## Neden / Why

Bağlantı listeleri genelde bir yığın URL'dir; hangisinin ne olduğunu anlamak için
hepsini tek tek açmak gerekir. Buradaki her kayıt kısa bir açıklama ve etiket
taşıyor, böylece açmadan önce ne olduğunu biliyorsun.

Most link lists are a pile of URLs — you have to open each one to find out what it
is. Here every entry carries a short description and tags, so you know before you
click.

## Özellikler / Features

- Anlık arama (isim, açıklama, etiket, alan adı) — Türkçe karakter duyarsız
- Kategori ve etiketle filtreleme, birleştirilebilir
- TR / EN dil değiştirici
- Açık / koyu tema
- Klavye: `/` arama, `Esc` temizle
- Tek sayfa, sıfır bağımlılık, dış istek yok (font/analitik/CDN yok)

## Yapı / Structure

```
index.html    tüm arayüz — CSS ve JS gömülü
links.js      veri (window.LINKS)
data/         derleme betikleri, ham çıktılar
```

`links.js` düz bir JavaScript dosyası olduğu için site **dosya olarak da açılır**;
sunucu gerekmez (`fetch` ile JSON okusaydı `file://` üzerinde CORS'a takılırdı).

## Yayınlama / Publishing

GitHub Pages için:

```bash
git init && git add -A && git commit -m "ilk sürüm"
git branch -M main
git remote add origin git@github.com:KULLANICI/REPO.git
git push -u origin main
```

Sonra repo ayarlarında **Settings → Pages → Source: main / root**.
`.nojekyll` dosyası zaten var, Jekyll işlemesi atlanır.

## Bağlantı eklemek / Adding a link

`links.js` içine yeni bir kayıt ekle:

```js
{
  url: "https://ornek.com/",
  name: "Örnek",
  cat: "araclar",
  tags: ["ücretsiz", "açık kaynak"],
  tr: "Ne işe yaradığı ve benzerlerinden farkı.",
  en: "What it does and how it differs."
}
```

`cat` değerleri `links.js` başındaki kategori listesinde tanımlı.

## Derleme betikleri / Build scripts

`data/` altındakiler tek seferlik derleme içindir, siteyi çalıştırmak için gerekmez:

| Betik | İş |
|---|---|
| `extract.py` | Tarayıcı yer imi dosyasından teknoloji bağlantılarını çıkarır, ayıklar |
| `check.py` | Bağlantıların canlı olup olmadığını kontrol eder |
| `fetchmeta.py` | Her sitenin başlık/açıklama meta verisini çeker (GitHub için API) |
| `build.py` | Küratör notlarını meta veriyle birleştirip `links.js` üretir |

## Lisans / License

Derleme ve açıklama metinleri CC BY 4.0. Bağlantı verilen sitelerin kendi
lisansları kendilerine aittir.
