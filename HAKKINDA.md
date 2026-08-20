# Hakkında

Bu dizin yıllarca biriken bir tarayıcı yer imi arşivinden çıktı.

İki bin küsur yer imi vardı. Çoğu bir daha açılmamıştı, bir kısmı çoktan ölmüştü,
hangisinin ne olduğunu anlamak için hepsini tek tek açmak gerekiyordu. Klasör
adları da yardımcı olmuyordu: "Araçlar" klasöründe otuz link varsa hangisinin ne
yaptığını hatırlamak mümkün değil.

Sorun yer imlerinin dağınıklığı değildi aslında. Sorun şuydu: bir bağlantının
**adı ve URL'si onun ne olduğunu söylemiyor.** `regex101.com` yazan bir satır
sana o siteyi açtırmadan hiçbir şey anlatmıyor. Oysa şunu bilsen açman gerekip
gerekmediğine hemen karar verirdin:

> Düzenli ifadeyi jeton jeton açıklıyor ve hata ayıklayıcısıyla eşleşmenin
> nerede koptuğunu gösteriyor.

Dizindeki her kayıtta bu var. İki şey yazıyor: **ne işe yaradığı** ve
**benzerlerinden nerede ayrıldığı.** İkincisi asıl mesele. Aynı işi yapan beş
araç arasından birini seçerken lazım olan şey özellik listesi değil, aralarındaki
farkın nerede olduğu.

## Nasıl Ayıklandı

Ham arşivde 2294 yer imi vardı. Teknolojiyle ilgili olanlar 634 taneydi.
Bunlardan:

- Hesaba bağlı paneller çıkarıldı — bir AWS konsolu bağlantısı kimseye yaramaz
- Google arama sorguları çıkarıldı
- Kişisel dosya paylaşımları çıkarıldı
- Ölü bağlantılar taranıp ayıklandı

Kalanlara dışarıdan bir derleme eklendi. Bunlar ayrı işaretli, çünkü aynı
titizlikte değiller — kendi arşivimden gelen kayıtları tek tek gözden geçirdim,
dışarıdan gelenler için aynı şeyi iddia edemem.

## Neyi İddia Etmiyor

Bu bir "en iyi araçlar" listesi değil. Kategori başına iki üç kayıt "başlangıç
noktası" olarak işaretli ama bu "en iyisi" demek değil, "bu alana ilk giriyorsan
buradan bak" demek.

Açıklamalardaki karşılaştırmalı yargılar da bana ait. Projelerin kendi
belgelerine bakarak yazdım ama "X, Y'den hızlı" gibi bir cümle sonuçta bir görüş.
Katılmıyorsan söyle.

## Çürümeye Karşı

Bağlantı listelerinin ortak kaderi çürümek. Bir süre sonra yarısı açılmaz olur
ve liste değerini kaybeder.

Buna karşı haftalık bir tarama var: bütün bağlantılar denetleniyor, ölenler tek
bir issue'da toplanıyor. Ayrıca GitHub depoları ayrıca kontrol ediliyor — çünkü
bir depo 404 döndürmeden de ölebilir. Nitekim bu dizindeki bir kayıt tam olarak
öyle: 76 bin yıldızlı bir derleme, sayfası hâlâ açılıyor ama Kasım 2025'te
arşivlenmiş. Bağlantı taraması bunu göremez, depo denetimi görür.

## Katkı

Eklenmesini istediğin bir kaynak varsa ya da hatalı bir kayıt gördüysen issue aç.
Yeni bağlantı şablonunda "benzerlerinden farkı ne" diye bir alan var ve zorunlu.
Bilmiyorsan "bilmiyorum" yaz, araştırırım — ama boş bırakılırsa kayıt dizinin
değerini taşımıyor demektir.

---

*Teknik ayrıntılar, derleme betikleri ve bağlantı ekleme yöntemi için
[data/README.md](data/README.md).*
