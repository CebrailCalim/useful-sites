# -*- coding: utf-8 -*-
"""Records surfaced by the cdcruz.com useful-sites collection.

Of its 407 entries, the ones inside this directory's scope were taken --
development, privacy, self-hosting, utilities and the creative tools that
developers actually reach for. Left out: anime clothing shops, wellness
apps, travel planners and a "Pirate Life" section.

Two of the source's URLs pointed at the wrong site (its FreeTube entry links
to signal.org, its MKVToolNix entry to MediaInfo) and were dropped rather than
guessed at. Descriptions here were rewritten, not copied.

These carry src='cdcruz'.
"""

S = 'cdcruz'


def load(add):
    def a(url, name, tags, tr, en, cat):
        add(url, name, tags, tr, en, cat, S)

    # ============================================================ DEVELOPMENT
    a('https://vscodium.com/', 'VSCodium', ['açık-kaynak', 'masaüstü'],
      'VS Code’un Microsoft telemetrisi ve markası çıkarılmış topluluk derlemesi. Aynı editör, '
      'aynı eklenti API’si; farkı, varsayılan eklenti marketinin Microsoft’unki değil Open VSX '
      'olması — bazı kapalı eklentiler burada bulunmuyor.',
      'A community build of VS Code with Microsoft’s telemetry and branding stripped out. Same '
      'editor, same extension API; the difference is that the default marketplace is Open VSX '
      'rather than Microsoft’s, so some proprietary extensions are simply absent.',
      'araclar')
    a('https://www.warp.dev/', 'Warp', ['masaüstü', 'cli', 'llm'],
      'Rust ile yazılmış terminal; komutları ve çıktılarını metin akışı yerine ayrı "blok"lar '
      'hâlinde tutuyor, böylece bir komutun çıktısını tek tıkla kopyalayabiliyorsun. iTerm veya '
      'Windows Terminal’dan ayrıldığı yer bu blok modeli ve gömülü YZ komut önerisi.',
      'A terminal written in Rust that keeps each command and its output as a separate block '
      'instead of one scrolling stream, so you can copy a single command’s output in one click. '
      'That block model and the built-in AI command suggestions are what set it apart.',
      'araclar')
    a('https://notepad-plus-plus.org/', 'Notepad++', ['açık-kaynak', 'masaüstü'],
      'Windows için hafif kaynak kodu editörü; sözdizimi renklendirme, çok dosyada arama-değiştir '
      've makro kaydı var. VS Code’a karşı tercih sebebi hız: dev bir günlük dosyasını saniyeler '
      'içinde açıyor, dil sunucusu beklemiyor.',
      'A lightweight source editor for Windows with syntax highlighting, multi-file search and '
      'replace, and macro recording. The reason to reach for it over VS Code is speed: it opens '
      'a huge log file in seconds without waiting on a language server.',
      'araclar')
    a('https://it-tools.tech/', 'IT Tools', ['açık-kaynak', 'tarayıcı-içi', 'self-hosted'],
      'Seksen küsur geliştirici aracı tek sayfada: hash, JWT çözücü, cron ifadesi, UUID, renk '
      'dönüştürücü. Tek tek araç sitelerinden farkı hepsinin tarayıcıda çalışması ve Docker ile '
      'kendi sunucuna kurulabilmesi — veri dışarı çıkmıyor.',
      'Eighty-odd developer utilities on one page: hashes, JWT decoding, cron expressions, UUIDs, '
      'colour conversion. Unlike the one-tool-per-site alternatives, everything runs in the '
      'browser and the whole thing self-hosts with Docker, so nothing leaves your machine.',
      'araclar')
    a('https://www.convex.dev/', 'Convex', ['backend', 'veritabanı', 'açık-kaynak'],
      'Veritabanı, sunucu işlevleri ve gerçek zamanlı abonelikleri tek üründe toplayan backend '
      'platformu. Firebase’den farkı sorguların TypeScript fonksiyonu olarak yazılması ve işlem '
      '(transaction) garantisi vermesi — döküman veritabanı esnekliğiyle ilişkisel tutarlılık.',
      'A backend platform folding the database, server functions and real-time subscriptions into '
      'one product. Where Firebase has you write rules, here queries are TypeScript functions with '
      'real transactional guarantees — document flexibility without giving up consistency.',
      'backend')
    a('https://turso.tech/', 'Turso', ['veritabanı', 'sql', 'açık-kaynak'],
      'SQLite çatallaması libSQL üzerine kurulu veritabanı platformu; veritabanını kullanıcının '
      'yakınındaki uç düğümlere kopyalıyor. Planetscale gibi merkezî hizmetlerden farkı, okuma '
      'gecikmesini ağ mesafesi yerine yerel dosya erişimine indirmesi.',
      'A database platform built on libSQL, a SQLite fork, that replicates the database to edge '
      'nodes near the user. Unlike centralised services such as PlanetScale, read latency becomes '
      'local file access rather than a network round trip.',
      'veritabani')
    a('https://porkbun.com/', 'Porkbun', ['sunucu'],
      'ICANN akreditasyonlu alan adı kayıt şirketi; WHOIS gizliliği, SSL ve e-posta yönlendirme '
      'ücretsiz geliyor. GoDaddy tarzı kayıtçılardan farkı yenileme fiyatının ilk yıl fiyatına '
      'yakın kalması — cazip giriş fiyatı sonra üç katına çıkmıyor.',
      'An ICANN-accredited domain registrar where WHOIS privacy, SSL and email forwarding are '
      'included rather than upsold. What separates it from the GoDaddy school is that renewal '
      'prices stay close to the first-year price instead of tripling.',
      'backend')
    a('https://caniuse.com/', 'Can I Use', ['referans', 'frontend', 'ücretsiz'],
      'Bir web özelliğinin hangi tarayıcının hangi sürümünde çalıştığını gösteren tablo; kullanım '
      'oranlarıyla birlikte. MDN’den farkı, "destekleniyor mu" sorusuna sürüm ve pazar payı '
      'düzeyinde cevap vermesi — polyfill gerekip gerekmediğine buradan karar veriyorsun.',
      'A table of which browser version supports which web feature, weighted by usage share. Where '
      'MDN explains the feature, this answers "can I ship it" at version and market-share level — '
      'it is where you decide whether a polyfill is needed.',
      'web')
    a('https://www.freepublicapis.com/', 'Free Public APIs', ['api', 'referans', 'ücretsiz'],
      'Üç yüzden fazla ücretsiz genel API’nin dizini; her biri için canlılık durumu ve son kontrol '
      'tarihi tutuluyor. Eski awesome-list derlemelerinden farkı bu: listedeki API’lerin hâlâ '
      'yanıt verip vermediğini düzenli olarak tarıyor.',
      'A directory of over three hundred free public APIs, each carrying a liveness status and a '
      'last-checked date. That is what separates it from the old awesome-list compilations: it '
      'actually keeps scanning whether the APIs still answer.',
      'backend')
    a('https://splidejs.com/', 'Splide', ['açık-kaynak', 'javascript', 'frontend'],
      'Bağımlılığı olmayan, erişilebilirlik odaklı kaydırıcı/karusel kütüphanesi. Swiper’a göre '
      'çok daha küçük (sıkıştırılmış ~12 KB) ve klavye gezinme ile ARIA rollerini varsayılan '
      'olarak doğru kuruyor — karusel erişilebilirliğinin klasik zayıf noktası.',
      'A dependency-free, accessibility-first slider and carousel library. It is markedly smaller '
      'than Swiper (~12KB gzipped) and gets keyboard navigation and ARIA roles right by default — '
      'the usual weak spot of carousels.',
      'web')
    a('https://howlerjs.com/', 'Howler.js', ['açık-kaynak', 'javascript', 'ses'],
      'Tarayıcılar arası ses oynatma kütüphanesi; Web Audio API’yi kullanıyor, olmadığı yerde '
      'HTML5 Audio’ya düşüyor. Ham Web Audio ile uğraşmaktan farkı ses sprite’ları, havuzlama ve '
      'mobil otomatik oynatma kilidini kendisi çözmesi.',
      'A cross-browser audio library that uses the Web Audio API and falls back to HTML5 Audio. '
      'Against hand-rolling Web Audio, it handles audio sprites, pooling and the mobile autoplay '
      'lock for you — the three things that always bite.',
      'web')
    a('https://easingwizard.com/', 'Easing Wizard', ['tarayıcı-içi', 'frontend', 'ücretsiz'],
      'CSS yumuşatma (easing) eğrilerini görsel olarak kuran araç; cubic-bezier’in yanında linear() '
      'ile yay ve sıçrama eğrilerini de üretiyor. cubic-bezier.com’dan farkı bu modern linear() '
      'desteği — CSS’te yay animasyonu artık kütüphane gerektirmiyor.',
      'A visual builder for CSS easing curves that covers not just cubic-bezier but linear() spring '
      'and bounce curves. That linear() support is what dates it past cubic-bezier.com: spring '
      'animation in CSS no longer needs a library.',
      'web')
    a('https://wakamaifondue.com/', 'Wakamai Fondue', ['tarayıcı-içi', 'frontend', 'ücretsiz'],
      'Bir font dosyasını sürükleyince içindeki her şeyi döküyor: karakter kümesi, OpenType '
      'özellikleri, değişken eksenler ve bunları açan hazır CSS. Font önizleyicilerinden farkı '
      'çıktının doğrudan kullanılabilir CSS olması.',
      'Drop in a font file and it reports everything inside: character set, OpenType features, '
      'variable axes — plus the CSS that switches each of them on. Unlike a font previewer, the '
      'output is code you can paste.',
      'web')
    a('https://webaim.org/', 'WebAIM', ['referans', 'ücretsiz', 'frontend'],
      'Utah State Üniversitesi bünyesindeki erişilebilirlik merkezi; kontrast denetleyicisi, WAVE '
      'aracı ve yıllık "Million" taraması buradan çıkıyor. WCAG belgesinin kendisinden farkı, '
      'kuralı değil kuralın pratikte nasıl uygulandığını anlatması.',
      'The accessibility centre at Utah State University — the contrast checker, the WAVE tool and '
      'the annual "Million" survey all come from here. Where the WCAG spec states the rule, WebAIM '
      'shows what applying it actually looks like.',
      'web')
    a('https://www.checklist.design/', 'Checklist Design', ['referans', 'frontend', 'ücretsiz'],
      'Buton, form, tablo gibi arayüz parçaları için tek tek kontrol listeleri: hangi durumlar '
      'çizilmeli, hangi erişilebilirlik ayrıntısı atlanır. Tasarım sistemi belgelerinden farkı '
      'bileşen kütüphanesi dayatmaması — kendi bileşenini denetlemek için liste veriyor.',
      'Per-component checklists for buttons, forms, tables and the rest: which states to draw, '
      'which accessibility detail everyone forgets. Unlike a design-system doc it imposes no '
      'component library — it hands you a list to audit your own against.',
      'web')
    a('https://www.30secondsofcode.org/', '30 Seconds of Code', ['referans', 'javascript', 'ücretsiz'],
      'Otuz saniyede okunup anlaşılacak uzunlukta kod parçacıkları; JavaScript, Python, React ve '
      'CSS için. Stack Overflow’dan farkı her parçacığın açıklamalı, test edilmiş ve konu başlığına '
      'göre düzenlenmiş olması — arama değil, gezinme.',
      'Code snippets short enough to read and understand in thirty seconds, for JavaScript, Python, '
      'React and CSS. Against Stack Overflow, each one is explained, tested and filed by topic — '
      'you browse it rather than search it.',
      'web')
    a('https://uiverse.io/', 'Uiverse', ['açık-kaynak', 'frontend', 'ücretsiz'],
      'Topluluğun katkı verdiği açık kaynak arayüz bileşeni galerisi: buton, kart, yükleyici, '
      'anahtar. CodePen’den farkı her parçanın MIT lisanslı, kopyala-yapıştır hazır ve saf '
      'CSS/Tailwind olarak sunulması — çatı bağımlılığı yok.',
      'A community-contributed gallery of open-source UI elements: buttons, cards, loaders, '
      'toggles. Unlike CodePen, everything is MIT-licensed, copy-paste ready and offered as plain '
      'CSS or Tailwind, with no framework attached.',
      'web')
    a('https://www.accessibility-developer-guide.com/', 'Accessibility Developer Guide',
      ['referans', 'dokümantasyon', 'frontend'],
      'Erişilebilir arayüzü kod düzeyinde anlatan rehber; her örnekte önce yanlış yaklaşımı sonra '
      'doğrusunu gösteriyor. WCAG’ın soyut ölçütlerinden farkı, ekran okuyucunun ne duyduğunu '
      'somut örnekle göstermesi.',
      'A guide to accessible interfaces at the code level, showing the wrong approach before the '
      'right one in every example. Where WCAG states abstract criteria, this demonstrates what a '
      'screen reader actually announces.',
      'referans')
    a('https://developer.apple.com/design/human-interface-guidelines/', 'Apple Human Interface Guidelines',
      ['referans', 'dokümantasyon', 'masaüstü'],
      'Apple’ın tüm platformları için arayüz tasarım kuralları: dokunma hedefi boyutları, gezinme '
      'kalıpları, hareket ve tipografi. Material Design’dan farkı, öneri değil App Store '
      'incelemesinde fiilen uygulanan bir ölçüt olması.',
      'Apple’s interface rules across all its platforms: touch target sizes, navigation patterns, '
      'motion and typography. Unlike Material Design, this is not advice — it is the yardstick App '
      'Store review actually applies.',
      'referans')
    a('https://lawsofux.com/', 'Laws of UX', ['referans', 'ücretsiz', 'frontend'],
      'Fitts, Hick, Jakob gibi arayüz tasarımını yöneten psikoloji yasalarının kısa ve görsel '
      'derlemesi. Akademik kaynaklardan farkı her yasayı tek ekranda örnekle anlatması — '
      'tasarım tartışmasında ortak dil kurmak için.',
      'A short, visual collection of the psychological laws that govern interface design — Fitts, '
      'Hick, Jakob and the rest. Unlike the academic sources, each law fits on one screen with an '
      'example, which makes it a shared vocabulary for design arguments.',
      'referans')

    # ============================================================ GAME & APP ENGINES
    a('https://godotengine.org/', 'Godot', ['açık-kaynak', 'masaüstü', 'interaktif'],
      'MIT lisanslı oyun motoru; 2B ve 3B için ayrı ayrı olgun boru hatları var. Unity ve Unreal’dan '
      'ayrıldığı yer lisans: gelir payı, koltuk ücreti ya da kurulum başına ücret yok, motorun '
      'tamamı senin.',
      'An MIT-licensed game engine with separately mature 2D and 3D pipelines. Where it parts ways '
      'with Unity and Unreal is the licence: no revenue share, no seat fee, no per-install charge — '
      'the whole engine is yours.',
      'mobil')
    a('https://unity.com/', 'Unity', ['masaüstü', 'ücretli', 'interaktif'],
      'C# ile yazılan, mobilden konsola on beşten fazla platforma çıkış alan oyun motoru. Unreal’a '
      'göre daha hafif ve mobil tarafında baskın; bağımsız oyunların çoğunluğu buradan çıkıyor. '
      'Lisans koşulları 2023’te tartışma yarattı, sözleşmeyi okumakta fayda var.',
      'A game engine scripted in C# that exports to more than fifteen platforms, from mobile to '
      'console. Lighter than Unreal and dominant on mobile — most indie games come out of it. Its '
      'licensing terms caused a public fight in 2023, so read the agreement.',
      'mobil')
    a('https://www.unrealengine.com/en-US/', 'Unreal Engine', ['masaüstü', 'c-ailesi', 'interaktif'],
      'AAA yapımların motoru; Nanite ve Lumen ile gerçek zamanlı yüksek çözünürlüklü geometri ve '
      'küresel aydınlatma sunuyor. Unity’den farkı görsel üst sınırı ve Blueprint görsel betikleme — '
      'karşılığında daha ağır bir proje ve daha dik bir öğrenme eğrisi.',
      'The engine behind AAA productions, offering real-time high-density geometry and global '
      'illumination through Nanite and Lumen. Against Unity it wins on visual ceiling and Blueprint '
      'visual scripting, and pays for it with heavier projects and a steeper climb.',
      'mobil')
    a('https://o3de.org/', 'Open 3D Engine', ['açık-kaynak', 'c-ailesi', 'interaktif'],
      'Amazon Lumberyard’ın Linux Foundation’a devredilmiş hâli; Apache 2.0 lisanslı, modüler 3B '
      'motor. Godot’ya göre daha ağır ama AAA ölçeğine yakın bir render hattı sunuyor; kurumsal '
      'destek arayan takımlar için açık kaynak seçeneği.',
      'Amazon’s Lumberyard, handed to the Linux Foundation as an Apache 2.0 modular 3D engine. '
      'Heavier than Godot, but with a rendering pipeline closer to AAA scale — the open-source '
      'option for teams that want corporate backing.',
      'mobil')
    a('https://microstudio.dev/', 'microStudio', ['tarayıcı-içi', 'ücretsiz', 'interaktif'],
      'Tarayıcıda çalışan tam oyun geliştirme ortamı: kod editörü, sprite çizimi, harita editörü ve '
      'ses üretimi bir arada. Godot veya Unity’den farkı kurulum gerektirmemesi — Chromebook’ta bile '
      'oyun yazılabiliyor, öğretim için elverişli.',
      'A complete game development environment in the browser: code editor, sprite drawing, map '
      'editor and sound generation together. Unlike Godot or Unity it installs nothing, so it works '
      'on a Chromebook — which makes it good for teaching.',
      'mobil')
    a('https://www.programmingfonts.org/', 'Programming Fonts', ['referans', 'ücretsiz', 'tarayıcı-içi'],
      'Kodlama için tasarlanmış tek aralıklı fontları gerçek kod örneği üzerinde yan yana deneme '
      'sitesi. Font indirme sitelerinden farkı, ligatürleri ve 0/O, 1/l/I ayrımını doğrudan kod '
      'bağlamında görmen — asıl önemli olan da bu.',
      'A place to try monospaced coding fonts side by side on real code. Unlike a font download '
      'site, you see the ligatures and the 0/O and 1/l/I distinctions in the context that actually '
      'matters.',
      'araclar')

    # ============================================================ PRIVACY & SELF-HOSTING
    a('https://tailscale.com/', 'Tailscale', ['ağ', 'güvenlik', 'freemium'],
      'WireGuard üzerine kurulu örgü VPN; cihazlarını NAT ve güvenlik duvarı arkasında olsalar bile '
      'doğrudan birbirine bağlıyor. Klasik VPN sunucusundan farkı merkezî bir çıkış düğümü '
      'olmaması — trafik cihazdan cihaza gidiyor, koordinasyon sunucusu yalnızca anahtar dağıtıyor.',
      'A mesh VPN on top of WireGuard that connects your devices directly even behind NAT and '
      'firewalls. Unlike a classic VPN server there is no central exit hop: traffic goes device to '
      'device and the coordination server only hands out keys.',
      'ag')
    a('https://pi-hole.net/', 'Pi-hole', ['açık-kaynak', 'self-hosted', 'ağ', 'gizlilik'],
      'Ağ geneli reklam engelleyici: DNS sunucusu olarak çalışıp reklam ve izleyici alan adlarını '
      'boşa düşürüyor. Tarayıcı eklentisinden farkı akıllı televizyon, telefon uygulaması ve IoT '
      'cihazlarını da kapsaması — eklenti kurulamayan her şeyi.',
      'A network-wide ad blocker that runs as your DNS server and sinkholes ad and tracker domains. '
      'Unlike a browser extension it also covers smart TVs, phone apps and IoT devices — everything '
      'you cannot install an extension on.',
      'ag')
    a('https://adguard.com/en/adguard-home/overview.html', 'AdGuard Home',
      ['açık-kaynak', 'self-hosted', 'ağ', 'gizlilik'],
      'Pi-hole ile aynı işi yapan ağ geneli engelleyici; farkı DNS-over-HTTPS ve DNS-over-TLS '
      'sunucusunu kendi içinde barındırması ve istemci başına ayrı kural yazmaya izin vermesi. '
      'Tek ikili dosya, ek bağımlılık yok.',
      'A network-wide blocker doing the same job as Pi-hole; what differs is that it ships its own '
      'DNS-over-HTTPS and DNS-over-TLS server and lets you write per-client rules. One binary, no '
      'extra dependencies.',
      'ag')
    a('https://mullvad.net/en', 'Mullvad VPN', ['gizlilik', 'güvenlik', 'ücretli'],
      'İsveç merkezli VPN; hesap açarken e-posta bile istemiyor, rastgele bir numara veriyor ve '
      'nakit ödeme kabul ediyor. Diğer VPN’lerden farkı bu kimliksizlik ve bağımsız denetim '
      'raporlarını yayımlaması — abonelik süresi arttıkça indirim de yapmıyor, tek fiyat.',
      'A Swedish VPN that asks for no email at signup — it hands you a random account number and '
      'takes cash. What separates it is that anonymity plus published independent audits, and a '
      'flat price with no long-subscription discount games.',
      'guvenlik')
    a('https://www.privacyguides.org/en/', 'Privacy Guides', ['referans', 'gizlilik', 'ücretsiz'],
      'Gizlilik araçlarını ölçüt bazlı değerlendiren, kâr amacı gütmeyen gönüllü topluluk. '
      '"En iyi VPN" listelerinden farkı ortaklık geliri almaması ve her tavsiyenin karşılamak '
      'zorunda olduğu koşulları açıkça yazması — tavsiyeyi tartışabiliyorsun.',
      'A non-profit, volunteer-run evaluation of privacy tools against stated criteria. Unlike the '
      '"best VPN" listicles it takes no affiliate money and publishes the conditions each '
      'recommendation must meet, so the recommendation is arguable.',
      'guvenlik')
    a('https://simplelogin.io/', 'SimpleLogin', ['açık-kaynak', 'gizlilik', 'freemium'],
      'E-posta takma adı hizmeti: her siteye ayrı adres verip gelen postayı asıl kutuna '
      'yönlendiriyor. "Apple ile giriş yap" gizli adresinden farkı açık kaynak ve kendi sunucuna '
      'kurulabilir olması; takma adı silince spam da kesiliyor ve kimin sattığı belli oluyor.',
      'An email aliasing service: a separate address per site, forwarded to your real inbox. Unlike '
      'Apple’s hide-my-email it is open source and self-hostable, and killing an alias both stops '
      'the spam and tells you who sold your address.',
      'guvenlik')
    a('https://simplex.chat/', 'SimpleX Chat', ['açık-kaynak', 'gizlilik', 'güvenlik'],
      'Kullanıcı kimliği kavramı olmayan mesajlaşma: telefon numarası, kullanıcı adı, hatta kalıcı '
      'bir ID yok. Signal’dan farkı bu — Signal numaranı biliyor, SimpleX sunucularında bağlanacak '
      'bir kimlik hiç oluşmuyor, dolayısıyla ilişki grafiği de çıkarılamıyor.',
      'Messaging with no notion of a user identity: no phone number, no username, not even a '
      'persistent ID. That is the break from Signal — Signal knows your number, whereas SimpleX '
      'servers never hold an identifier to correlate, so no social graph can be derived.',
      'guvenlik')
    a('https://tuta.com/', 'Tuta', ['gizlilik', 'güvenlik', 'freemium'],
      'Uçtan uca şifreli e-posta ve takvim; posta kutusunun tamamını, konu satırları ve adres '
      'defteri dahil şifreliyor. ProtonMail’den farkı IMAP yerine kendi istemcisini şart koşması — '
      'karşılığında meta verinin daha azı açıkta kalıyor.',
      'End-to-end encrypted email and calendar that encrypts the whole mailbox, subject lines and '
      'address book included. Against ProtonMail it insists on its own client rather than IMAP, and '
      'in exchange leaves less metadata exposed.',
      'guvenlik')
    a('https://www.thunderbird.net/en-US/', 'Thunderbird', ['açık-kaynak', 'masaüstü', 'gizlilik'],
      'Mozilla çatısı altındaki masaüstü e-posta istemcisi; IMAP, takvim, kişiler ve OpenPGP '
      'imzalama bir arada. Web arayüzlerinden farkı postanın yerelde durması ve sağlayıcıyı '
      'değiştirdiğinde arşivinin seninle kalması.',
      'A desktop mail client under the Mozilla umbrella, with IMAP, calendar, contacts and OpenPGP '
      'signing in one place. Against webmail, the archive lives on your disk and stays yours when '
      'you change provider.',
      'araclar')
    a('https://tails.net/', 'Tails', ['açık-kaynak', 'gizlilik', 'güvenlik'],
      'USB’den çalışan, tüm trafiği Tor üzerinden geçiren canlı Linux dağıtımı. Tor Browser '
      'kullanmaktan farkı, sistemin tamamının unutkan olması: kapattığında diskte hiçbir iz '
      'kalmıyor, bilerek kalıcı bölüm açmadıysan.',
      'A live Linux distribution that runs from USB and routes everything through Tor. Unlike just '
      'using Tor Browser, the whole system is amnesic: shut it down and nothing remains on disk '
      'unless you deliberately made a persistent volume.',
      'guvenlik')
    a('https://privatebin.info/', 'PrivateBin', ['açık-kaynak', 'self-hosted', 'gizlilik'],
      'Sunucunun içeriği hiç bilmediği pastebin: metin tarayıcıda şifreleniyor, anahtar URL '
      'parçasında kalıyor ve sunucuya gitmiyor. Pastebin.com’dan farkı bu sıfır bilgi tasarımı ve '
      'okununca yok olma seçeneği.',
      'A pastebin the server cannot read: the text is encrypted in the browser and the key lives in '
      'the URL fragment, which is never sent. That zero-knowledge design and burn-after-reading are '
      'the break from pastebin.com.',
      'guvenlik')
    a('https://github.com/jvoisin/mat2', 'mat2', ['açık-kaynak', 'gizlilik', 'python', 'cli'],
      'Dosyalardaki meta veriyi temizleyen araç: fotoğrafın GPS koordinatı, PDF’in yazar alanı, '
      'ofis belgesinin düzenleme geçmişi. exiftool’dan farkı varsayılanın silmek olması — '
      'hangi alanın kaldığını tek tek düşünmen gerekmiyor.',
      'A tool that strips metadata from files: GPS coordinates in a photo, the author field in a '
      'PDF, the revision history in an office document. Unlike exiftool the default is removal, so '
      'you are not left reasoning about which field survived.',
      'guvenlik')
    a('https://libredirect.codeberg.page/', 'LibRedirect', ['açık-kaynak', 'gizlilik', 'eklenti'],
      'YouTube, Twitter, Reddit, Instagram bağlantılarını otomatik olarak gizlilik dostu ön yüzlere '
      '(Invidious, Nitter, Redlib) yönlendiren tarayıcı eklentisi. Elle ön yüz aramaktan farkı, '
      'çalışmayan örnekleri atlayıp çalışanı seçmesi.',
      'A browser extension that redirects YouTube, Twitter, Reddit and Instagram links to '
      'privacy-respecting frontends such as Invidious, Nitter and Redlib. Against hunting for a '
      'frontend yourself, it skips the dead instances and picks a working one.',
      'guvenlik')
    a('https://www.rocket.chat/', 'Rocket.Chat', ['açık-kaynak', 'self-hosted', 'sunucu'],
      'Kendi sunucuna kurulabilen takım mesajlaşma platformu; kanal, tez (thread), sesli görüşme ve '
      'köprüler (bridge) var. Slack’ten farkı verinin senin altyapında kalması ve mesaj geçmişinin '
      'ücretli plan arkasına kilitlenmemesi.',
      'A self-hostable team messaging platform with channels, threads, voice and bridges. Against '
      'Slack, the data stays on your infrastructure and message history is not locked behind a paid '
      'tier.',
      'araclar')
    a('https://element.io/', 'Element', ['açık-kaynak', 'gizlilik', 'self-hosted'],
      'Matrix protokolü üzerine kurulu mesajlaşma istemcisi; uçtan uca şifreleme ve sunucular arası '
      'federasyon var. Slack ya da Discord’dan farkı bu federasyon: farklı sunucudaki iki kişi tek '
      'bir şirkete bağlı olmadan aynı odada konuşabiliyor.',
      'A messaging client on the Matrix protocol, with end-to-end encryption and federation between '
      'servers. That federation is the break from Slack or Discord: two people on different servers '
      'share a room without a single company in the middle.',
      'araclar')
    a('https://syncthing.net/', 'Syncthing', ['açık-kaynak', 'self-hosted', 'gizlilik'],
      'Cihazlar arası sürekli dosya eşitleme; merkezî sunucu yok, cihazlar doğrudan konuşuyor. '
      'Dropbox’tan farkı buluta hiç kopya çıkmaması — depolama kotası da yok, diskin kadar yer var.',
      'Continuous file synchronisation between devices with no central server: the devices talk '
      'directly. Unlike Dropbox no copy ever reaches a cloud, and there is no storage quota — you '
      'have as much room as you have disk.',
      'araclar')
    a('https://nextcloud.com/', 'Nextcloud', ['açık-kaynak', 'self-hosted', 'sunucu'],
      'Kendi sunucunda çalışan dosya senkronizasyonu ve iş birliği paketi: takvim, kişiler, '
      'belge düzenleme, sohbet. Syncthing’den farkı web arayüzü ve paylaşım bağlantıları sunması — '
      'eşitleme değil, Google Workspace’in yerini almaya çalışıyor.',
      'A self-hosted file sync and collaboration suite: calendar, contacts, document editing, chat. '
      'Where Syncthing only syncs, this adds a web interface and share links — it is aiming at '
      'Google Workspace rather than at Dropbox.',
      'araclar')
    a('https://immich.app/', 'Immich', ['açık-kaynak', 'self-hosted', 'gizlilik'],
      'Google Photos’un kendi sunucunda çalışan karşılığı: telefondan otomatik yükleme, yüz tanıma, '
      'harita ve zaman çizelgesi. Diğer öz-barındırılan galerilerden farkı mobil uygulamanın '
      'gerçekten arka planda yedekleme yapması — çoğu bunu beceremiyor.',
      'A self-hosted answer to Google Photos: background upload from the phone, face recognition, '
      'map and timeline. What separates it from other self-hosted galleries is that the mobile app '
      'actually backs up in the background, which most of them never manage.',
      'araclar')
    a('https://www.audiobookshelf.org/', 'Audiobookshelf', ['açık-kaynak', 'self-hosted', 'ses'],
      'Sesli kitap ve podcast koleksiyonunu kendi sunucunda yönetip yayınlayan uygulama; ilerleme '
      'cihazlar arasında eşitleniyor. Plex ya da Jellyfin’den farkı sesli kitaba özgü olması — '
      'bölüm işaretleri, hız ayarı ve seri takibi doğru çalışıyor.',
      'A self-hosted server for managing and streaming your audiobook and podcast collection, with '
      'progress synced across devices. Unlike Plex or Jellyfin it is built for audiobooks '
      'specifically, so chapter marks, playback speed and series tracking behave properly.',
      'araclar')
    a('https://github.com/Freika/dawarich', 'Dawarich', ['açık-kaynak', 'self-hosted', 'gizlilik'],
      'Konum geçmişini kendi sunucunda tutan ve haritada gösteren uygulama; Google Location History '
      'dışa aktarımını içe alabiliyor. Google’ın kendi hizmetinden farkı verinin sende kalması ve '
      'kapatıldığında kaybolmaması.',
      'Self-hosted location history with a map view, able to import a Google Location History '
      'export. The difference from Google’s own service is that the data stays with you — and does '
      'not vanish when the product is discontinued.',
      'araclar')
    a('https://asahilinux.org/', 'Asahi Linux', ['açık-kaynak', 'ağ', 'donanım'],
      'Apple Silicon Mac’lere ana hat Linux getiren proje; GPU sürücüsünü ve güç yönetimini tersine '
      'mühendislikle yazıyor. Sanal makineden farkı donanımda doğrudan çalışması — M serisi '
      'yongadan tam performans alınıyor.',
      'A project bringing mainline Linux to Apple Silicon Macs, reverse-engineering the GPU driver '
      'and power management. Unlike a virtual machine it runs on the metal, so you get the M-series '
      'chip’s full performance.',
      'ag')
    a('https://ladybird.org/', 'Ladybird', ['açık-kaynak', 'frontend'],
      'Sıfırdan yazılan bağımsız tarayıcı motoru; Chromium, WebKit ya da Gecko’dan türetilmemiş. '
      'Diğer "alternatif" tarayıcılardan farkı tam olarak bu — ötekiler Chromium kabuğu, bu kendi '
      'motorunu yazıyor. Henüz günlük kullanıma hazır değil.',
      'An independent browser engine written from scratch, derived from neither Chromium, WebKit '
      'nor Gecko. That is precisely what separates it from the other "alternative" browsers, which '
      'are Chromium shells. Not yet ready for daily use.',
      'web')
    a('https://organicmaps.app/', 'Organic Maps', ['açık-kaynak', 'gizlilik', 'ücretsiz'],
      'OpenStreetMap verisiyle çalışan çevrimdışı harita ve navigasyon uygulaması; izleyici ve '
      'reklam yok. Maps.me’den farkı onun ticarileşmesinin ardından çatallanmış olması — eski '
      'reklamsız hâlin devamı.',
      'An offline map and navigation app on OpenStreetMap data, with no trackers and no ads. It is '
      'the fork Maps.me spawned when that went commercial — the continuation of the version people '
      'actually liked.',
      'araclar')

    # ============================================================ UTILITIES
    a('https://www.voidtools.com/', 'Everything', ['ücretsiz', 'masaüstü'],
      'Windows’ta dosya adına göre anlık arama; NTFS ana dosya tablosunu okuyarak indeks kuruyor. '
      'Windows Search’ten farkı bu: içerik indekslemediği için ilk taraması saniyeler sürüyor ve '
      'sonuçlar yazarken anında geliyor.',
      'Instant filename search on Windows, built by reading the NTFS master file table directly. '
      'That is the trick against Windows Search: it does not index content, so the first scan takes '
      'seconds and results appear as you type.',
      'araclar')
    a('https://getsharex.com/', 'ShareX', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Windows için ekran görüntüsü ve kayıt aracı; kaydettikten sonra yükleme, kısaltma, OCR gibi '
      'adımları zincirleyebiliyorsun. Snipping Tool’dan farkı bu iş akışı otomasyonu — görüntü alıp '
      'panoya bağlantı koymayı tek kısayola indiriyor.',
      'A screenshot and recording tool for Windows that chains post-capture steps: upload, shorten, '
      'OCR. What separates it from Snipping Tool is that workflow automation — capture and '
      'link-on-clipboard becomes one shortcut.',
      'araclar')
    a('https://squoosh.app/', 'Squoosh', ['açık-kaynak', 'tarayıcı-içi', 'ücretsiz'],
      'Görsel sıkıştırmayı iki bölmede karşılaştırmalı gösteren araç; MozJPEG, WebP, AVIF '
      'kodlayıcılarını WebAssembly ile tarayıcıda çalıştırıyor. TinyPNG’den farkı dosyanın hiç '
      'yüklenmemesi ve her kodlayıcının ayarını elle kurcalayabilmen.',
      'Image compression with a side-by-side comparison, running MozJPEG, WebP and AVIF encoders in '
      'the browser through WebAssembly. Unlike TinyPNG nothing is uploaded, and every encoder '
      'setting is yours to tune.',
      'araclar')
    a('https://tinypng.com/', 'TinyPNG', ['ücretsiz', 'tarayıcı-içi'],
      'PNG ve JPEG dosyalarını seçici nicemleme ile küçülten servis; sürükle bırak, ayar yok. '
      'Squoosh’tan farkı toplu işlem ve API sunması — tek görsel için Squoosh, yüz görsel için bu.',
      'Shrinks PNG and JPEG files through selective quantisation: drag, drop, no settings. Against '
      'Squoosh it offers batch processing and an API — Squoosh for one image, this for a hundred.',
      'araclar')
    a('https://www.xnview.com/en/xnconvert/', 'XnConvert', ['ücretsiz', 'masaüstü'],
      'Toplu görsel dönüştürme ve işleme aracı; 500’den fazla biçimi okuyup 70 kadarına yazıyor, '
      'yeniden boyutlandırma ve filigran zincirlenebiliyor. Çevrimiçi dönüştürücülerden farkı '
      'binlerce dosyayı yerelde, boyut sınırı olmadan işlemesi.',
      'Batch image conversion and processing that reads over 500 formats and writes around 70, with '
      'resize and watermark steps chained together. Unlike online converters it handles thousands '
      'of files locally with no size cap.',
      'araclar')
    a('https://snapdrop.net/', 'Snapdrop', ['açık-kaynak', 'tarayıcı-içi', 'ücretsiz'],
      'Aynı ağdaki cihazlar arasında tarayıcıdan dosya aktarımı; WebRTC ile doğrudan bağlanıyor. '
      'AirDrop’tan farkı işletim sistemi gözetmemesi — Android ile Mac arasında da çalışıyor, '
      'kurulum ve hesap istemiyor.',
      'Browser-to-browser file transfer between devices on the same network, connected directly over '
      'WebRTC. Unlike AirDrop it does not care about the operating system — Android to Mac works — '
      'and needs no install or account.',
      'araclar')
    a('https://rufus.ie/en/', 'Rufus', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Önyüklenebilir USB hazırlayan Windows aracı; ISO’yu yazarken UEFI/BIOS ve bölümleme '
      'ayrıntılarını kendisi çözüyor. Diğer yazıcılardan farkı Windows 11 kurulumundaki TPM ve '
      'hesap zorunluluğunu kaldıran seçenekleri sunması.',
      'A Windows tool for writing bootable USB drives that works out the UEFI/BIOS and partitioning '
      'details itself. What sets it apart from other writers is the option to strip the TPM and '
      'account requirements out of a Windows 11 install.',
      'araclar')
    a('https://learn.microsoft.com/en-us/windows/powertoys/', 'Microsoft PowerToys',
      ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Windows’a eksik özellikleri ekleyen resmi araç seti: pencere yerleşimi (FancyZones), toplu '
      'yeniden adlandırma, renk seçici, metin çıkarma. Üçüncü parti araçlardan farkı Microsoft’un '
      'kendi geliştirip açık kaynak tutması — güncellemelerle uyumu bozulmuyor.',
      'The official set of tools that adds what Windows lacks: window layouts (FancyZones), bulk '
      'rename, colour picker, text extraction. Unlike third-party equivalents it is built and kept '
      'open source by Microsoft, so updates do not break it.',
      'araclar')
    a('https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns', 'Autoruns',
      ['ücretsiz', 'masaüstü', 'güvenlik'],
      'Windows’ta açılışta çalışan her şeyi listeleyen Sysinternals aracı: hizmetler, zamanlanmış '
      'görevler, kabuk uzantıları, sürücüler. Görev Yöneticisi’nin başlangıç sekmesinden farkı '
      'kötü amaçlı yazılımın saklandığı otuz küsur kayıt defteri noktasını da göstermesi.',
      'The Sysinternals tool that lists everything Windows runs at startup: services, scheduled '
      'tasks, shell extensions, drivers. Against Task Manager’s startup tab it also covers the '
      'thirty-odd registry locations malware actually hides in.',
      'araclar')
    a('https://www.ntop.org/', 'ntop', ['açık-kaynak', 'ağ', 'gözlemlenebilirlik'],
      'Ağ trafiğini gerçek zamanlı izleyen araç ailesi; hangi cihazın hangi protokolle ne kadar '
      'veri geçirdiğini gösteriyor. Wireshark’tan farkı paket paket inceleme değil sürekli akış '
      'izleme — sorunu yakalamak için değil, olağandışıyı fark etmek için.',
      'A family of tools for real-time network traffic monitoring, showing which device moves how '
      'much over which protocol. Where Wireshark inspects packet by packet, this watches the flow '
      'continuously — for noticing the anomaly rather than dissecting it.',
      'ag')
    a('https://openspeedtest.com/', 'OpenSpeedTest', ['açık-kaynak', 'self-hosted', 'ağ'],
      'Tarayıcıda çalışan hız testi; Flash ya da uygulama gerektirmiyor, kendi sunucuna da '
      'kurulabiliyor. Speedtest.net’ten farkı bu öz-barındırma — yerel ağının gerçek hızını dış '
      'bağlantıya bağlı kalmadan ölçebiliyorsun.',
      'A browser-based speed test needing no Flash and no app, and self-hostable on your own '
      'server. That self-hosting is the difference from Speedtest.net: you can measure your LAN’s '
      'real throughput without an internet hop.',
      'ag')
    a('https://canyouseeme.org/', 'CanYouSeeMe', ['ücretsiz', 'ağ'],
      'Belirli bir portun dışarıdan açık olup olmadığını kontrol eden basit araç. Yerel port '
      'taramasından farkı dışarıdan bakması — yönlendirici port yönlendirmesinin gerçekten '
      'çalışıp çalışmadığı ancak böyle anlaşılıyor.',
      'A minimal check for whether a given port is reachable from outside. Unlike scanning locally '
      'it looks in from the internet, which is the only way to tell whether router port forwarding '
      'actually works.',
      'ag')
    a('https://mediaarea.net/en/MediaInfo', 'MediaInfo', ['açık-kaynak', 'ücretsiz'],
      'Video ve ses dosyalarının teknik künyesini döken araç: kodek, bit hızı, kare hızı, renk '
      'uzayı, kapsayıcı ayrıntıları. Oynatıcıların "özellikler" ekranından farkı akış düzeyinde '
      'ayrıntıya inmesi — sorun ayıklarken tek gerçek kaynak.',
      'Dumps the technical identity of a video or audio file: codec, bitrate, frame rate, colour '
      'space, container details. Unlike a player’s properties dialog it goes to stream level, which '
      'makes it the source of truth when something will not play.',
      'araclar')
    a('https://github.com/mifi/lossless-cut', 'LosslessCut', ['açık-kaynak', 'masaüstü', 'video'],
      'Videoyu yeniden kodlamadan kesip birleştiren araç; anahtar kare sınırlarında çalışıyor. '
      'Klasik video editörlerinden farkı işlemin saniyeler sürmesi ve kalite kaybı olmaması — '
      'bir saatlik kaydın başını sonunu almak için editör açmaya gerek yok.',
      'Cuts and joins video without re-encoding, working on keyframe boundaries. Against a normal '
      'editor the operation takes seconds and loses no quality — trimming the head and tail off an '
      'hour of footage no longer means opening a timeline.',
      'araclar')
    a('https://www.shutterencoder.com/', 'Shutter Encoder', ['açık-kaynak', 'ücretsiz', 'video'],
      'FFmpeg’i arayüzle saran dönüştürücü; video editörlerinin ihtiyaç duyduğu ara kodekleri ve '
      'toplu işlemleri hazır sunuyor. HandBrake’ten farkı yayın/kurgu odaklı olması — ProRes, DNxHD '
      've altyazı gömme gibi işler menüde duruyor.',
      'A converter wrapping FFmpeg with a UI, offering the intermediate codecs and batch jobs '
      'editors need. Against HandBrake it is aimed at post-production — ProRes, DNxHD and subtitle '
      'burn-in sit in the menu rather than in a command line.',
      'araclar')
    a('https://github.com/SubtitleEdit/subtitleedit', 'Subtitle Edit',
      ['açık-kaynak', 'masaüstü', 'ücretsiz'],
      'Altyapı olarak dalga formu ve ses spektrumu gösteren altyazı editörü; 200’den fazla biçim '
      'okuyor, zamanlama kaydırma ve OCR ile gömülü altyazı çıkarma yapıyor. Basit altyazı '
      'düzenleyicilerden farkı bu senkronizasyon araçları.',
      'A subtitle editor that shows a waveform and spectrogram underneath, reads over 200 formats, '
      'shifts timings and extracts burned-in subtitles by OCR. Those synchronisation tools are what '
      'separate it from simple subtitle editors.',
      'araclar')
    a('https://subtitle-editor.org/', 'Subtitle Editor Online', ['tarayıcı-içi', 'ücretsiz'],
      'Tarayıcıda çalışan altyazı düzenleyici; .srt ve .vtt dosyalarını açıp zamanlama ve metin '
      'düzeltmeye yarıyor. Subtitle Edit gibi masaüstü araçlardan farkı kurulum istememesi — '
      'başkasının bilgisayarında hızlı bir düzeltme için.',
      'A subtitle editor in the browser for opening .srt and .vtt files and fixing timings and '
      'text. Against desktop tools like Subtitle Edit it installs nothing, which is what you want '
      'for a quick fix on someone else’s machine.',
      'araclar')
    a('https://github.com/k4yt3x/video2x', 'Video2X', ['açık-kaynak', 'python', 'video'],
      'Videoyu kare kare sinir ağıyla büyüten çerçeve; waifu2x, Real-ESRGAN ve Anime4K gibi '
      'modelleri arkasında çalıştırıyor. Tek görsel büyütücülerden farkı zamansal tutarlılığı ve '
      'video boru hattını üstlenmesi.',
      'A framework that upscales video frame by frame with neural models, driving waifu2x, '
      'Real-ESRGAN and Anime4K behind the scenes. Against single-image upscalers it takes on the '
      'video pipeline and temporal consistency.',
      'yz_arac')
    a('https://github.com/fccview/cronmaster', 'Cronmaster', ['açık-kaynak', 'self-hosted', 'devops'],
      'Cron görevlerini web arayüzünden yöneten öz-barındırılan uygulama; ifadeleri okunur hâlde '
      'gösteriyor ve çalıştırma günlüğü tutuyor. crontab -e’den farkı bir sonraki çalışma zamanını '
      've son çıktıyı göstermesi — sessizce başarısız olan görevler görünür oluyor.',
      'A self-hosted web interface for cron jobs that renders expressions in readable form and '
      'keeps a run log. Against `crontab -e` it shows the next run time and the last output, which '
      'makes silently failing jobs visible.',
      'devops')
    a('https://logseq.com/', 'Logseq', ['açık-kaynak', 'masaüstü', 'ücretsiz'],
      'Madde temelli, çift yönlü bağlantı kuran not uygulaması; notları düz Markdown dosyası olarak '
      'diskte tutuyor. Notion’dan farkı verinin senin klasöründe olması, Obsidian’dan farkı ana '
      'birimin sayfa değil madde olması — günlük tutmaya daha uygun.',
      'An outliner with bi-directional links that keeps every note as a plain Markdown file on '
      'disk. Against Notion the data is in your folder; against Obsidian the primary unit is the '
      'block rather than the page, which suits daily journalling better.',
      'araclar')
    a('https://www.libreoffice.org/', 'LibreOffice', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Yazı, hesap tablosu, sunum ve veritabanı içeren ofis paketi; varsayılan biçimi açık standart '
      'ODF. Microsoft Office ile farkı lisans ve veri sahipliği; karşılığında karmaşık .docx '
      'düzenlerinde ufak kaymalar görebiliyorsun.',
      'An office suite of writer, spreadsheet, presentation and database, defaulting to the open ODF '
      'standard. The difference from Microsoft Office is licensing and data ownership; the price is '
      'occasional layout drift on complex .docx files.',
      'araclar')

    # ============================================================ CREATIVE TOOLS
    a('https://www.blender.org/', 'Blender', ['açık-kaynak', 'ücretsiz', '3b'],
      'Modelleme, kaplama, kuşatma (rigging), simülasyon, render ve video kurgu tek pakette. '
      'Maya ya da 3ds Max’ten farkı tamamen ücretsiz olması ve bu boru hattının tümünü tek '
      'programda tutması — dosya aktarımı kaybı yok.',
      'Modelling, texturing, rigging, simulation, rendering and video editing in one package. '
      'Against Maya or 3ds Max it is free, and it keeps the entire pipeline in a single program so '
      'nothing is lost in file handoffs.',
      'araclar')
    a('https://krita.org/en/', 'Krita', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Dijital resim ve konsept sanat için çizim programı; fırça motoru ve kare kare animasyon '
      'desteği güçlü. GIMP’ten farkı fotoğraf düzenleme değil çizim için tasarlanmış olması — '
      'fırça gecikmesi ve stabilizasyon buna göre ayarlanmış.',
      'A painting program for digital art and concept work, with a strong brush engine and '
      'frame-by-frame animation. Unlike GIMP it was built for drawing rather than photo editing, '
      'and brush latency and stabilisation are tuned accordingly.',
      'araclar')
    a('https://inkscape.org/', 'Inkscape', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'SVG’yi yerel biçimi olarak kullanan vektör çizim programı. Illustrator’dan farkı dosyanın '
      'doğrudan web’e gidebilecek temiz SVG olması — ara dışa aktarma adımı yok, kaynağı elle '
      'düzenleyebiliyorsun.',
      'A vector editor that uses SVG as its native format. Against Illustrator, the file is clean '
      'SVG ready for the web — no export step in between, and you can hand-edit the source.',
      'araclar')
    a('https://www.photopea.com/', 'Photopea', ['tarayıcı-içi', 'ücretsiz'],
      'Tarayıcıda çalışan görsel editör; PSD, XCF, Sketch ve XD dosyalarını katmanlarıyla açıyor. '
      'GIMP’ten farkı kurulum gerektirmemesi ve PSD uyumluluğunun gerçekten iyi olması — başkasının '
      'gönderdiği PSD’yi açmak için en kısa yol.',
      'An image editor in the browser that opens PSD, XCF, Sketch and XD files with their layers '
      'intact. Against GIMP it installs nothing and its PSD compatibility is genuinely good, which '
      'makes it the shortest path to opening a file someone sent you.',
      'araclar')
    a('https://www.aseprite.org/', 'Aseprite', ['ücretli', 'masaüstü', 'interaktif'],
      'Piksel sanatı ve animasyon için tasarlanmış editör; soğan zarı, kare zaman çizelgesi ve '
      'sprite sayfası dışa aktarımı var. Genel amaçlı çizim programlarından farkı her aracın piksel '
      'ızgarasına oturması — yumuşatma (anti-aliasing) istemediğin yerde olmuyor.',
      'An editor built for pixel art and animation, with onion skinning, a frame timeline and sprite '
      'sheet export. Unlike a general painting program every tool snaps to the pixel grid, so '
      'anti-aliasing never appears where you did not ask for it.',
      'araclar')
    a('https://www.piskelapp.com/', 'Piskel', ['açık-kaynak', 'tarayıcı-içi', 'ücretsiz'],
      'Tarayıcıda çalışan piksel sanatı ve sprite animasyon editörü. Aseprite’tan farkı ücretsiz ve '
      'kurulumsuz olması; karşılığında katman ve fırça araçları daha sınırlı — ilk sprite’ını '
      'çizmek için yeterli.',
      'A pixel art and sprite animation editor in the browser. Against Aseprite it is free and needs '
      'no install; in exchange the layer and brush tools are thinner — enough for your first sprite.',
      'araclar')
    a('https://fontforge.org/en-US/', 'FontForge', ['açık-kaynak', 'ücretsiz', 'masaüstü'],
      'Font oluşturma ve düzenleme programı; TTF, OTF, WOFF arasında dönüştürüyor ve glif '
      'ipuçlarını (hinting) düzenlemeye izin veriyor. Çevrimiçi font dönüştürücülerden farkı '
      'gliflerin kendisine müdahale edebilmen.',
      'A font creation and editing program that converts between TTF, OTF and WOFF and lets you '
      'work on glyph hinting. Unlike an online font converter, you can get at the glyphs themselves.',
      'araclar')
    a('https://vectormagic.com/', 'Vector Magic', ['ücretli', 'tarayıcı-içi'],
      'Bitmap görseli vektöre çeviren araç. Illustrator’ın izleme (trace) işlevinden farkı kenar '
      'tespitinin belirgin daha temiz olması — logoyu düşük çözünürlüklü bir PNG’den geri kazanmak '
      'için en iyi sonucu veren yol.',
      'Converts a bitmap image into vector art. Against Illustrator’s trace, its edge detection is '
      'noticeably cleaner — it is the best route to recovering a logo from a low-resolution PNG.',
      'araclar')
    a('https://lucide.dev/', 'Lucide', ['açık-kaynak', 'frontend', 'ücretsiz'],
      '1600’den fazla SVG ikon içeren kütüphane; React, Vue, Svelte için hazır paketleri var. '
      'Feather’ın topluluk çatallaması olarak devam ediyor — farkı, Feather bakımsız kalırken '
      'bunun aktif olarak büyümesi ve tek tek ikon içe aktarmaya (tree-shaking) uygun olması.',
      'An icon library of over 1,600 SVG icons with ready packages for React, Vue and Svelte. It is '
      'the community fork of Feather, and the difference is that it kept growing while Feather went '
      'quiet — and that it tree-shakes down to the icons you import.',
      'web')
    a('https://thenounproject.com/', 'The Noun Project', ['freemium', 'ücretsiz'],
      'Milyonlarca ikon ve sembolün arandığı arşiv; her kavram için birden çok üslup bulunuyor. '
      'İkon kütüphanelerinden farkı tutarlı bir set değil kavram sözlüğü olması — çok özel bir '
      'nesnenin ikonunu ancak burada bulursun.',
      'A searchable archive of millions of icons and symbols, with several visual takes on each '
      'concept. Unlike an icon library it is not a consistent set but a dictionary of concepts — '
      'the place where an icon for one very specific object actually exists.',
      'araclar')
    a('https://cc0textures.com/', 'ambientCG', ['ücretsiz', '3b'],
      'CC0 lisanslı PBR doku ve malzeme arşivi; renk, normal, pürüzlülük ve yer değiştirme '
      'haritaları birlikte geliyor. Doku sitelerinin çoğundan farkı lisansın gerçekten CC0 '
      'olması — atıf bile gerekmiyor, ticari kullanım serbest.',
      'An archive of CC0-licensed PBR textures and materials, shipping colour, normal, roughness '
      'and displacement maps together. Unlike most texture sites the licence really is CC0 — no '
      'attribution needed, commercial use fine.',
      'araclar')
    a('https://3dassets.one/', '3Dassets.one', ['ücretsiz', '3b'],
      'Farklı 3B varlık sitelerini tek aramada birleştiren arama motoru; lisans ve fiyata göre '
      'süzülüyor. Tek tek siteleri gezmekten farkı lisans süzgeci — ticari kullanıma uygun '
      'olanları doğrudan ayırabiliyorsun.',
      'A search engine that consolidates several 3D asset sites into one query, filterable by '
      'licence and price. Against visiting each site, the licence filter is the point — you can '
      'isolate what is actually usable commercially.',
      'araclar')
    a('https://www.thingiverse.com/', 'Thingiverse', ['ücretsiz'],
      '3B baskı modellerinin topluluk arşivi; çoğu Creative Commons lisanslı ve baskı ayarlarıyla '
      'birlikte paylaşılıyor. Printables ve MakerWorld’den farkı en eski ve en büyük arşiv olması — '
      'niş bir parça arıyorsan hâlâ ilk bakılacak yer.',
      'The community archive of 3D printing models, mostly Creative Commons licensed and shared '
      'with print settings. Against Printables and MakerWorld it is the oldest and largest — still '
      'the first place to look for a niche part.',
      'donanim')
    a('https://www.freecad.org/', 'FreeCAD', ['açık-kaynak', 'ücretsiz', 'cad'],
      'Parametrik 3B CAD modelleyici; tasarım ağacını düzenleyerek geçmişe dönüp ölçü '
      'değiştirebiliyorsun. Blender’dan farkı bu parametrik yaklaşım — Blender çokgen biçimlendirir, '
      'bu üretilebilir parça tasarlar.',
      'A parametric 3D CAD modeller where you go back up the design tree and change a dimension. '
      'That parametric approach is the split from Blender: Blender sculpts polygons, this designs '
      'a manufacturable part.',
      'donanim')
    a('https://www.kicad.org/', 'KiCad', ['açık-kaynak', 'ücretsiz', 'cad', 'donanım'],
      'Şematik çizimden PCB yerleşimine kadar tüm elektronik tasarım akışını kapsayan açık kaynak '
      'paket. Eagle ve Altium’dan farkı katman veya kart boyutu sınırı olmaması — ücretsiz sürüm '
      'kısıtı diye bir şey yok.',
      'An open-source suite covering the whole electronics design flow from schematic to PCB '
      'layout. Against Eagle and Altium there is no layer count or board size limit — no free-tier '
      'ceiling at all.',
      'donanim')
    a('https://land-book.com/', 'Land-book', ['ücretsiz', 'frontend'],
      'İyi tasarlanmış web sitelerinin küratörlü galerisi; sektöre, üsluba ve renge göre '
      'süzülebiliyor. Awwwards gibi ödül sitelerinden farkı gösterişli deneysel işler yerine '
      'gerçekten yayında olan ürün sitelerini toplaması.',
      'A curated gallery of well-designed websites, filterable by industry, style and colour. '
      'Unlike award sites such as Awwwards it collects real shipping product sites rather than '
      'showpiece experiments.',
      'web')

    # ============================================================ AI / TRANSLATION
    a('https://libretranslate.com/', 'LibreTranslate', ['açık-kaynak', 'self-hosted', 'api'],
      'Kendi sunucuna kurulabilen makine çevirisi API’si; Argos Translate modellerini kullanıyor. '
      'Google Translate API’sinden farkı çevrilen metnin hiç dışarı çıkmaması ve istek başına '
      'ücret olmaması — kalite daha düşük, gizlilik daha yüksek.',
      'A self-hostable machine translation API running Argos Translate models. Against the Google '
      'Translate API the text never leaves your server and there is no per-request charge — lower '
      'quality, higher privacy.',
      'yz_arac')
    a('https://github.com/ggml-org/whisper.cpp', 'whisper.cpp',
      ['açık-kaynak', 'c-ailesi', 'ses', 'llm'],
      'OpenAI Whisper konuşma tanıma modelinin bağımlılıksız C/C++ uyarlaması; CPU’da bile makul '
      'hızda çalışıyor. Python sürümünden farkı kurulum yükünün olmaması ve tek ikili dosyaya '
      'derlenebilmesi — gömülü cihaza bile giriyor.',
      'A dependency-free C/C++ port of OpenAI’s Whisper speech recognition model that runs at a '
      'reasonable pace even on CPU. Against the Python original there is no install burden and it '
      'compiles to a single binary — small enough for embedded targets.',
      'yz_altyapi')
