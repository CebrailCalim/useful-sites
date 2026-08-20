# GitHub'a Yükleme — Adım Adım

Depo: **https://github.com/CebrailCalim/useful-sites**
Yayın adresi (Pages açılınca): **https://cebrailcalim.github.io/useful-sites/**

Hazırlık bitti. Aşağıda önce yapılmış olanlar, sonra kalanlar var.

---

## Yapılmış olanlar

| # | İş | Durum |
|---|---|---|
| 1 | GitHub'da boş depo açıldı | ✅ |
| 2 | Dal adı `master` → `main` çevrildi | ✅ |
| 3 | `origin` HTTPS adresine ayarlandı | ✅ |
| 4 | `index.html` içindeki `REPO` sabiti gerçek adrese çevrildi | ✅ |

**Neden HTTPS, neden SSH değil:** bilgisayarda `~/.ssh/id_ed25519.pub` anahtarı var
ama GitHub hesabına tanıtılmamış — bağlanmayı denedim, `Permission denied (publickey)`
döndü. SSH'yi sonra kurmak istersen anahtarı
[github.com/settings/keys](https://github.com/settings/keys) sayfasına ekleyip
adresi geri çevirebilirsin. Şimdilik gereksiz.

---

## 4. Gönder

`site` klasöründe:

```bash
git push -u origin main
```

**İlk push'ta tarayıcı açılır** ve GitHub girişi ister (Git Credential Manager).
Bir kez onaylarsın, sonraki push'larda sormaz.

Bittiğinde depo sayfasını yenile, 62 dosyanın göründüğünü gör.

---

## 5. Pages'i Aç

Settings → Pages:

- **Source:** `Deploy from a branch`
- **Branch:** `main`, klasör `/ (root)`
- **Save**

İki dakika sonra site şurada yayında:

```
https://cebrailcalim.github.io/useful-sites/
```

`.nojekyll` dosyası zaten depoda, Jekyll işlemesi atlanıyor.

---

## 6. Otomatik Bakımı Aç

`.github/workflows/link-check.yml` her pazartesi bütün bağlantıları tarıyor.
İlk çalışmadan önce iki ayar gerekiyor.

**a) Actions'a yazma izni — bunu atlama**

Settings → Actions → General → **Workflow permissions** →
`Read and write permissions` seç, kaydet.

Bu izin olmadan tarama `data/verified.json` dosyasını geri yazamaz. O dosya
sitedeki "son doğrulama" tarihlerini besliyor; izin verilmezse tarihler donar
ve dizin taze görünmeyi bırakır.

**b) Elle bir kez çalıştır**

Actions sekmesi → `Bağlantı ve depo sağlığı` → **Run workflow**.

İlk tarama 700+ bağlantıyı geziyor, birkaç dakika sürer. Ölü bağlantı bulursa
`link-check` etiketli bir issue açar. Sonraki haftalarda yeni issue açmaz,
aynısını günceller — böylece issue listesi şişmez.

---

## 7. Depoyu Tanıtılabilir Hâle Getir

Ana sayfada sağ üstteki **About** çarkı:

- **Description:** `Yazılım, yapay zeka ve güvenlik üzerine açıklamalı bağlantı dizini`
- **Website:** `https://cebrailcalim.github.io/useful-sites/`
- **Topics:** `bookmarks`, `awesome-list`, `directory`, `turkish`, `developer-tools`

Topic eklemek GitHub aramasında görünürlüğü belirgin artırıyor.

---

## Sonrasında bağlantı eklemek

1. `data/part_*.py` içine notu yaz
2. `python data/build.py` çalıştır
3. `git add -A && git commit -m "..." && git push`

Pages birkaç saniye içinde güncellenir. Ayrıntı için [data/README.md](data/README.md).

**Not:** `data/meta.json` ve `data/ext_meta.json` depoya dâhil değil (`.gitignore`).
Bunlar ham toplama çıktıları; `build.py` senin bilgisayarında çalışır, sunucuda
değil. Yayınlanan şey `links.js` — o takipte ve güncel.

---

## Takılırsan

| Sorun | Sebebi ve çözümü |
|---|---|
| Push'ta tarayıcı açılıp kapanıyor, yine soruyor | Windows Kimlik Bilgileri Yöneticisi'nden `git:https://github.com` kaydını silip tekrar dene |
| `Permission denied (publickey)` | Adres SSH'ye dönmüş. `git remote set-url origin https://github.com/CebrailCalim/useful-sites.git` |
| Push reddedildi, `fetch first` diyor | Depoda README açılmış. `git pull --rebase origin main` sonra tekrar push |
| Pages 404 veriyor | Branch/folder ayarı yanlış ya da henüz yayına alınmadı — 2 dk bekle |
| Site açılıyor ama boş | `links.js` push edilmemiş. `git status` ile kontrol et |
| Workflow kırmızı | Büyük ihtimalle adım 6a'daki yazma izni verilmemiş |
