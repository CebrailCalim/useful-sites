# GitHub'a Yükleme — Adım Adım

Depo yerelde hazır ve commit'lenmiş durumda. Yapılacak tek şey onu GitHub'a
göndermek ve Pages'i açmak. Aşağıdaki adımların hepsi bir defalık.

---

## 1. GitHub'da Boş Bir Depo Aç

[github.com/new](https://github.com/new) adresine git.

| Alan | Ne yazmalı |
|---|---|
| Repository name | `teknoloji-baglantilari` (istediğin adı verebilirsin) |
| Description | `Yazılım, yapay zeka ve güvenlik üzerine açıklamalı bağlantı dizini` |
| Public / Private | **Public** — Pages'in ücretsiz çalışması için gerekli |
| Add a README | **İşaretleme.** Bizde zaten var, çakışır |
| .gitignore | **None** |
| License | **None** — bizde `LICENSE` dosyası var |

**Create repository**'ye bas. Açılan sayfadaki `git@github.com:...` adresini kopyala.

---

## 2. Depo Adresini Ayarla

`site` klasöründe terminal aç ve adresi kendi kullanıcı adınla değiştirerek çalıştır:

```bash
git remote add origin git@github.com:KULLANICI/teknoloji-baglantilari.git
```

SSH anahtarın yoksa HTTPS de olur:

```bash
git remote add origin https://github.com/KULLANICI/teknoloji-baglantilari.git
```

Doğru ayarlandığını gör:

```bash
git remote -v
```

---

## 3. Altbilgideki Depo Adresini Düzelt

`index.html` içinde `REPO` diye bir sabit var, şu an yer tutucu:

```js
var REPO = "https://github.com/KULLANICI/teknoloji-baglantilari";
```

Altbilgideki "bildir" bağlantısı buraya gidiyor. Kendi adresinle değiştir,
sonra commit'le:

```bash
git add index.html
git commit -m "depo adresini ayarla"
```

---

## 4. Gönder

```bash
git push -u origin main
```

Dosyaların GitHub'da göründüğünü kontrol et.

---

## 5. Pages'i Aç

Deponun **Settings → Pages** sekmesine git:

- **Source:** `Deploy from a branch`
- **Branch:** `main`, klasör `/ (root)`
- **Save**

Bir iki dakika sonra site şurada yayında olur:

```
https://KULLANICI.github.io/teknoloji-baglantilari/
```

`.nojekyll` dosyası zaten var, Jekyll işlemesi atlanıyor.

---

## 6. Otomatik Bakımı Aç

Depoda `.github/workflows/link-check.yml` var; her pazartesi bütün bağlantıları
tarıyor. İlk çalışmadan önce iki ayar gerekiyor:

**a) Actions'a yazma izni**

Settings → Actions → General → **Workflow permissions** →
`Read and write permissions` seç, kaydet.

Bu izin `verified.json` dosyasını geri yazabilmesi için gerekli — site her
kayıtta "son doğrulama" tarihi gösteriyor, o dosyadan geliyor.

**b) Elle bir kez çalıştır**

Actions sekmesi → `Bağlantı ve depo sağlığı` → **Run workflow**.

İlk tarama 700+ bağlantıyı geziyor, birkaç dakika sürüyor. Bitince ölü bağlantı
bulduysa bir issue açar. Sonraki haftalarda yeni issue açmaz, aynısını günceller.

---

## 7. Depoyu Tanıtılabilir Hâle Getir

Ana sayfada sağ üstteki **About** çarkına bas:

- **Description:** yukarıdaki açıklamanın aynısı
- **Website:** Pages adresini yapıştır
- **Topics:** `bookmarks`, `awesome-list`, `directory`, `turkish`, `developer-tools`

Topic eklemek arama görünürlüğünü belirgin artırıyor.

---

## Sonrasında

Bağlantı eklemek için `data/part_*.py` içine not yaz, `python data/build.py`
çalıştır, commit'le, push'la. Pages birkaç saniye içinde güncellenir.

Ayrıntı için [README.md](README.md).

## Takılırsan

| Sorun | Sebebi |
|---|---|
| Push'ta `Permission denied (publickey)` | SSH anahtarı yok. HTTPS adresini kullan |
| Pages 404 veriyor | Branch/folder ayarı yanlış ya da henüz yayına alınmadı, 2 dk bekle |
| Sayfa boş açılıyor | `links.js` push edilmemiş olabilir; `git status` ile kontrol et |
| Workflow hata veriyor | Adım 6a'daki yazma izni verilmemiştir |
