# -*- coding: utf-8 -*-
"""Araçlar & Yardımcılar · Bilim & Akademik

Not: kaynak yer imlerindeki tek tek Vikipedi makaleleri (kisisel okuma listesi)
bilerek disarida birakildi; burada yalnizca baskasinin da kullanabilecegi
kaynaklar var.
"""


def load(add):
    # ============================================================ ARAÇLAR & YARDIMCILAR
    T = 'araclar'
    add('https://excalidraw.com/', 'Excalidraw', ['açık-kaynak', 'diyagram', 'tarayıcı-içi'],
        'El çizimi görünümlü beyaz tahta. Kasıtlı olarak kaba durması bir üslup tercihi değil işlevsel: '
        'taslak aşamasındaki bir mimarinin bitmiş sanılmasını engelliyor.',
        'A hand-drawn-style whiteboard. Looking deliberately rough is functional rather than stylistic — '
        'it stops a draft architecture being mistaken for a finished one.', T)
    add('https://www.drawio.com/', 'draw.io', ['açık-kaynak', 'diyagram', 'ücretsiz'],
        'Ağ, UML ve AWS şekil kütüphaneleriyle gelen genel amaçlı diyagram aracı. '
        'Dosyayı yerel diske ya da kendi Drive’ına kaydediyor; sunucuya bir şey göndermiyor.',
        'General-purpose diagramming with network, UML and AWS shape libraries. It saves to local disk or your own '
        'Drive and sends nothing to a server.', T)
    add('https://mermaid.live/edit', 'Mermaid Live Editor', ['ücretsiz', 'diyagram', 'metin'],
        'Metinden diyagram üretiyor; sonuç düz metin olduğu için sürüm kontrolüne giriyor ve '
        'diff’i okunabiliyor. GitHub ve GitLab Mermaid’i doğrudan render ediyor.',
        'Generates diagrams from text, so the source lives in version control with a readable diff. '
        'GitHub and GitLab render Mermaid natively.', T)
    add('https://moqups.com/', 'Moqups', ['saas', 'freemium', 'tel-kafes'],
        'Tarayıcıda tel kafes ve prototip; Figma’nın tasarım derinliği yok ama '
        'hızlı bir akış şeması ya da ekran taslağı için yeterli ve daha hafif.',
        'Browser wireframing and prototyping. It lacks Figma’s design depth but is lighter and sufficient for '
        'a quick flow or screen sketch.', T)
    add('https://www.figma.com/', 'Figma', ['saas', 'freemium', 'tasarım'],
        'Arayüz tasarımının fiilî standardı; eşzamanlı düzenleme masaüstü araçların sonunu getirdi. '
        'Dev Mode ile geliştiriciye ölçü ve token aktarımı yapıyor.',
        'The de facto standard for interface design, whose multiplayer editing ended the desktop tools. '
        'Dev Mode hands measurements and tokens to developers.', T)
    add('https://transform.tools/', 'Transform', ['ücretsiz', 'dönüştürücü', 'açık-kaynak'],
        'Biçimler arası dönüştürücü koleksiyonu: JSON’dan TypeScript tipine, HTML’den JSX’e, '
        'SVG’den React bileşenine. Her biri için ayrı site aramaya son veriyor.',
        'A collection of format converters — JSON to TypeScript types, HTML to JSX, SVG to a React component. '
        'It ends hunting a separate site for each.', T)
    add('https://regex101.com/', 'regex101', ['ücretsiz', 'regex', 'araç'],
        'İfadeyi jeton jeton açıklıyor ve hata ayıklayıcısıyla eşleşmenin nerede koptuğunu gösteriyor. '
        'PCRE, JavaScript ve Python lehçeleri arasında geçiş yapabiliyorsun.',
        'Explains an expression token by token and its debugger shows exactly where a match breaks down, '
        'with switching between the PCRE, JavaScript and Python flavours.', T)
    add('https://godbolt.org/', 'Compiler Explorer', ['açık-kaynak', 'derleyici', 'assembly'],
        'Kaynak kodun yanına ürettiği assembly’i koyuyor; optimizasyon seviyesini ve derleyici sürümünü '
        'değiştirip farkı anında görüyorsun. Performans tartışmalarını fikirden ölçüme taşıyor.',
        'Puts the generated assembly beside your source, with optimisation level and compiler version switchable so '
        'you see the difference immediately. It moves performance arguments from opinion to measurement.', T)
    add('https://carbon.now.sh/', 'Carbon', ['ücretsiz', 'görsel', 'kod'],
        'Kod parçasından paylaşılabilir görsel üretiyor; tema, pencere süsü ve satır numarası ayarlanabiliyor. '
        'Ekran görüntüsünden farkı, sonucun tekrar edilebilir ve okunaklı olması.',
        'Turns a snippet into a shareable image with theme, window chrome and line numbers under your control. '
        'Unlike a screenshot the result is reproducible and legible.', T)
    add('https://www.ilovepdf.com/', 'iLovePDF', ['saas', 'freemium', 'pdf'],
        'Birleştirme, bölme, sıkıştırma ve dönüştürme; kurulum istemiyor. '
        'Hassas belgeler için dikkat: dosya sunucuya yükleniyor, yerel araç daha uygun olabilir.',
        'Merge, split, compress and convert with no installation. Be careful with sensitive documents — '
        'the file is uploaded to a server, and a local tool may be the better call.', T)
    add('https://www.textise.net/', 'Textise', ['ücretsiz', 'erişilebilirlik', 'araç'],
        'Sayfayı yalnızca metne indiriyor. Reklam ve düzen gürültüsünü kaldırmasının yanında, '
        'ekran okuyucunun sayfayı nasıl gördüğünü kabaca test etmeye de yarıyor.',
        'Strips a page to text only. Besides removing ads and layout noise, it roughly approximates what a screen '
        'reader sees.', T)
    add('https://alternativeto.net/', 'AlternativeTo', ['ücretsiz', 'dizin', 'topluluk'],
        'Bir yazılıma alternatif bulmanın standart yolu; lisansa, platforma ve '
        '“açık kaynak olsun” filtresine göre daraltabiliyorsun. Sıralama kullanıcı oylarıyla.',
        'The standard way to find an alternative to a piece of software, narrowable by licence, platform and an '
        'open-source-only filter, ranked by user votes.', T)
    add('https://free-for.dev/', 'Free for Developers', ['ücretsiz', 'awesome-liste'],
        'Ücretsiz katmanı olan geliştirici servisleri; kotalar tabloda yazılı olduğu için '
        'sınırın nerede olduğunu önden görüyorsun.',
        'Developer services with free tiers, with the quotas written into the table so you see where the ceiling '
        'sits before you commit.', T)
    add('https://same.energy/', 'Same Energy', ['ücretsiz', 'arama', 'görsel'],
        'Anahtar kelimeyle değil görsel benzerlikle arıyor; bir görsel verip “buna benzeyenler” diyorsun. '
        'Estetik üzerinden keşif, metin araması için sözcük bulmayı gerektirmiyor.',
        'Searches by visual similarity rather than keywords — you hand it an image and ask for more like it. '
        'Discovery through aesthetics, with no need to find the word first.', T)
    add('https://feedly.com/', 'Feedly', ['saas', 'freemium', 'rss'],
        'RSS okuyucu. Algoritmik akışların aksine ne okuyacağına kaynak düzeyinde sen karar veriyorsun; '
        'okumadığın şey de kaybolmuyor.',
        'An RSS reader where you decide what you read at the source level, unlike algorithmic feeds — '
        'and nothing you have not read disappears.', T)
    add('https://www.parse.bot/', 'Parse', ['saas', 'freemium', 'kazıma', 'api'],
        'Web sayfasından API üretiyor; seçicileri sen tanımlamıyorsun, sayfayı gösteriyorsun. '
        'API’si olmayan bir kaynaktan yapılandırılmış veri almanın kısa yolu.',
        'Turns a web page into an API without you writing selectors — you point at the page. '
        'A short route to structured data from a source with no API.', T)
    add('https://www.audionotes.app/', 'AudioNotes', ['saas', 'freemium', 'stt', 'not'],
        'Sesli notu ham döküm yerine yapılandırılmış metne çeviriyor: özet, madde listesi, yapılacaklar. '
        'Yürürken düşünüp sonra düzenlemek isteyenler için.',
        'Turns a voice note into structured text — summary, bullets, action items — rather than a raw transcript. '
        'For thinking aloud on the move and organising afterwards.', T)
    add('https://www.macrodroid.com/', 'MacroDroid', ['android', 'freemium', 'otomasyon'],
        'Android’de tetikleyici-eylem kuralları kuruyorsun: konuma girince Wi-Fi aç, '
        'şarj olurken sessize al. Tasker kadar güçlü değil ama arayüzü kat kat anlaşılır.',
        'Builds trigger-action rules on Android — Wi-Fi on when you reach a location, silent while charging. '
        'Less powerful than Tasker and vastly more comprehensible.', T)
    add('https://sxp.studio/apps/applist', 'AppList', ['ios', 'ücretsiz', 'minimalizm'],
        'iPhone için metin listesi biçiminde uygulama başlatıcı. '
        'Simge ızgarasının dikkat çekiciliğini kaldırıyor; dijital minimalizm tarafında bilinçli bir sürtünme.',
        'A text-list app launcher for iPhone, removing the pull of an icon grid — deliberate friction on the '
        'digital minimalism side.', T)
    add('https://codewiki.google/', 'CodeWiki', ['ücretsiz', 'kod', 'dokümantasyon'],
        'Kod tabanları için otomatik üretilmiş dokümantasyon; bir depoya ilk baktığında '
        'yapıyı ve giriş noktalarını çıkarmaya yarıyor.',
        'Automatically generated documentation for codebases, useful for extracting structure and entry points '
        'the first time you open a repository.', T)
    add('https://codescene.com/', 'CodeScene', ['saas', 'ücretli', 'analiz', 'teknik-borç'],
        'Kodu değişim geçmişiyle birlikte analiz ediyor: en çok değişen, en karmaşık ve '
        'tek kişiye bağımlı dosyaları çıkarıyor. Statik çözümleyicilerin göremediği boyut zaman.',
        'Analyses code alongside its change history, surfacing the files that churn most, carry most complexity or '
        'depend on one person. The dimension static analysers miss is time.', T)
    add('https://labs.google/', 'Google Labs', ['ücretsiz', 'deneysel'],
        'Google’ın henüz ürünleşmemiş denemelerinin vitrini. '
        'Buradaki çoğu şey kapanıyor, ama şirketin hangi yöne baktığını erken gösteriyor.',
        'A showcase of Google experiments that have not become products. Most of it gets shut down, '
        'but it shows early where the company is looking.', T)
    add('https://github.com/HQarroum/docker-android', 'Docker Android', ['açık-kaynak', 'github', 'docker', 'test'],
        'Kapsayıcı içinde Android emülatörü çalıştırıyor; VNC ile ekranına bakabiliyorsun. '
        'CI hattında cihaz çiftliği kurmadan otomatik test çalıştırmak için.',
        'Runs an Android emulator in a container with VNC access to the screen — for running automated tests in CI '
        'without standing up a device farm.', T)
    add('https://github.com/Augani/openreel-video', 'OpenReel Video', ['açık-kaynak', 'github', 'video', 'tarayıcı-içi'],
        'Tarayıcıda çalışan video düzenleyici; görüntü cihazdan çıkmıyor. '
        'Kurulum istemeyen ve bulut servisine yüklemeyen bir alternatif.',
        'A video editor running in the browser with the footage staying on device — an alternative that needs no '
        'installation and no upload to a cloud service.', T)
    add('https://github.com/getagentseal/codeburn', 'CodeBurn', ['açık-kaynak', 'github', 'analiz'],
        'Kod tabanındaki ölü kodu ve kullanılmayan bağımlılıkları çıkarıyor. '
        'Uzun süredir yaşayan projelerde ne kadar birikinti olduğunu görmek şaşırtıcı olabiliyor.',
        'Surfaces dead code and unused dependencies in a codebase. On a long-lived project the amount of accumulated '
        'debris can be surprising.', T)
    add('https://github.com/punitarani/fli', 'fli', ['açık-kaynak', 'github', 'cli'],
        'Uçuş aramayı komut satırına taşıyor; sonuçlar betiklenebilir olduğu için '
        'fiyat takibini bir cron işine bağlayabiliyorsun.',
        'Brings flight search to the command line, and because results are scriptable you can hang price tracking '
        'off a cron job.', T)
    add('https://github.com/ZeoRexDevs/Udeler_GUI', 'Udeler GUI', ['açık-kaynak', 'github', 'araç'],
        'Satın aldığın Udemy kurslarını çevrimdışı izlemek için indiriyor. '
        'Erişimin olan içeriği arşivleme aracı; kurs erişimi kaldırıldığında elinde kalıyor.',
        'Downloads Udemy courses you own for offline viewing — an archiving tool for content you already have '
        'access to, which survives if that access is withdrawn.', T)
    add('https://keepnote.org/', 'KeepNote', ['açık-kaynak', 'not', 'masaüstü'],
        'Basit ve taşınabilir not defteri; notları düz dosya olarak diskte tutuyor. '
        'Bulut not uygulamalarının kapanma riskine karşı sade bir sigorta.',
        'A simple, portable notebook keeping notes as plain files on disk — a modest hedge against cloud note apps '
        'shutting down.', T)
    add('https://appsgolem.com/en/cut-youtube-video/', 'YouTube Video Kesici', ['ücretsiz', 'video', 'araç'],
        'Videodan belirli bir aralığı kesip indiriyor. Tamamını indirip düzenlemeye göre '
        'hem hızlı hem disk dostu.',
        'Cuts and downloads a specific range from a video — faster and kinder to disk than downloading the whole '
        'thing and trimming.', T)
    add('https://dynomapper.com/blog/inventory-content/how-to-download-a-website-for-offline-viewing/', 'Siteyi Çevrimdışı İndirme', ['ücretsiz', 'rehber', 'arşiv'],
        'Bir siteyi çevrimdışı arşivleme yöntemlerini karşılaştıran rehber (wget, HTTrack ve diğerleri). '
        'Kaybolma riski olan dokümantasyon için pratik bir hazırlık.',
        'A guide comparing methods for archiving a site offline — wget, HTTrack and the rest. '
        'Practical preparation for documentation at risk of vanishing.', T)
    add('https://www.technopat.net/sosyal/indir/', 'Technopat İndirilenler', ['ücretsiz', 'türkçe', 'topluluk'],
        'Türkçe yazılım arşivi ve tartışma alanı; yerel kullanıcı deneyimleri ve '
        'donanım uyumluluk notları bir arada.',
        'A Turkish software archive and discussion area, gathering local user experience and hardware compatibility notes.', T)
    add('https://sourceforge.net/projects/embarcadero-devcpp/files/v6.3/', 'Embarcadero Dev-C++', ['ücretsiz', 'ide', 'c++', 'windows'],
        'Hafif C/C++ geliştirme ortamı. Modern IDE’lerin gerisinde ama düşük donanımda çalışıyor ve '
        'Türkiye’deki üniversite laboratuvarlarında hâlâ standart kurulum.',
        'A lightweight C/C++ IDE. Behind modern ones, yet it runs on weak hardware and remains the standard install '
        'in many Turkish university labs.', T)
    add('https://www.youtube.com/watch?v=rbu7Zu5X1zI', 'Geliştirici Araçları (video)', ['video', 'ücretsiz'],
        'Geliştirici araç zinciri üzerine anlatım; yazılı dokümana alternatif olarak izleyerek öğrenmek için.',
        'A walkthrough of developer tooling, for learning by watching rather than reading.', T)
    add('https://www.youtube.com/watch?v=uOPl7ZzuXf8&list=PLi2GhhsPL-RrapHA_Z8c1GG_qM3Nzdd0j&index=2', 'Araç Serisi (oynatma listesi)', ['video', 'ücretsiz'],
        'Araç ve iş akışı üzerine çok bölümlü seri; tek videodan farkı konuyu adım adım derinleştirmesi.',
        'A multi-part series on tooling and workflow, deepening the subject step by step rather than in one pass.', T)
    # trend & istatistik
    add('https://www.tiobe.com/tiobe-index/', 'TIOBE Index', ['ücretsiz', 'istatistik'],
        'Programlama dili popülerlik endeksi. Yöntemi (arama motoru sonucu sayısı) haklı olarak eleştiriliyor; '
        'yine de yirmi yıllık tutarlı seri olduğu için eğilim okumada kullanılıyor.',
        'A programming language popularity index whose methodology — counting search engine results — is rightly '
        'criticised, yet which is read for trends because the series has been consistent for twenty years.', T)
    add('https://octotrends.com/', 'OctoTrends', ['ücretsiz', 'github', 'istatistik'],
        'GitHub depolarının yıldız kazanma hızını gösteriyor. Toplam yıldız eski projeleri kayırır; '
        'ivmeye bakmak yeni çıkanı görmenin daha iyi yolu.',
        'Shows how fast GitHub repositories gain stars. Total stars favour old projects, so looking at momentum '
        'is the better way to see what is new.', T)
    add('https://gitstar-ranking.com/repositories', 'GitStar Ranking', ['ücretsiz', 'github', 'istatistik'],
        'Depo ve kullanıcıların yıldız sıralaması; bir alanda neyin baskın olduğunu hızla gösteriyor. '
        'Yıldız kalite ölçüsü değil, görünürlük ölçüsü — o gözle okumak gerekiyor.',
        'Star rankings for repositories and users, quickly showing what dominates a field. '
        'Stars measure visibility rather than quality, and should be read that way.', T)
    add('https://trendshift.io/', 'Trendshift', ['ücretsiz', 'github', 'istatistik'],
        'Yükselen açık kaynak projeleri izleyen pano; olgunlaşmış listelerin kaçırdığı '
        'yeni çıkanları öne alıyor.',
        'A dashboard tracking rising open-source projects, foregrounding the new arrivals established lists miss.', T)
    add('https://www.visualcapitalist.com/', 'Visual Capitalist', ['ücretsiz', 'veri-görselleştirme'],
        'Ekonomi ve teknoloji verisini bilgi grafiğine çeviren yayın. Ham veri kaynağı değil; '
        'büyüklükleri karşılaştırılabilir kılması asıl katkısı.',
        'A publication turning economic and technology data into infographics. Not a raw data source — '
        'its contribution is making magnitudes comparable.', T)

    # ============================================================ BİLİM & AKADEMİK
    B = 'bilim'
    add('https://arxiv.org/', 'arXiv', ['ücretsiz', 'ön-baskı', 'akademik'],
        'Fizik, matematik ve bilgisayar biliminin ön baskı arşivi. Hakem sürecinden önce yayımlandığı için '
        'alanın en güncel hâli burada — ama denetimden geçmediğini akılda tutmak gerekiyor.',
        'The preprint archive for physics, maths and computer science. Publishing before peer review is why the '
        'field’s newest work appears here — and why it needs reading with that caveat.', B)
    add('https://www.semanticscholar.org/', 'Semantic Scholar', ['ücretsiz', 'akademik', 'arama'],
        'Atıfların bağlamını çözümleyip “bu makale destekleniyor mu eleştiriliyor mu” sorusuna cevap veriyor. '
        'Google Scholar sayı verir, bu yönü söyler.',
        'Analyses citation context to answer whether a paper is being supported or criticised. '
        'Google Scholar gives you a count; this gives you a direction.', B)
    add('https://www.connectedpapers.com/', 'Connected Papers', ['freemium', 'akademik', 'graf'],
        'Bir makalenin etrafındaki literatürü benzerlik grafiği olarak çiziyor; öncüller ve '
        'türevler ayrı gösteriliyor. Yeni bir alana girerken haritayı hızlı çıkarıyor.',
        'Draws the literature around a paper as a similarity graph with prior and derivative work separated — '
        'a fast map when entering an unfamiliar field.', B)
    add('https://www.doi.org/', 'DOI', ['ücretsiz', 'standart', 'akademik'],
        'Akademik yayınların kalıcı tanımlayıcı sistemi. Dergi sitesi taşınsa da DOI çalışmaya devam ediyor; '
        'atıflarda bağlantı çürümesine karşı tek sağlam çözüm.',
        'The persistent identifier system for scholarly work. A DOI keeps resolving when a journal site moves — '
        'the only solid answer to link rot in citations.', B)
    add('https://academic.oup.com/', 'Oxford Academic', ['ücretli', 'akademik', 'dergi'],
        'Oxford University Press dergi platformu. Büyük yayıncı arşivlerinden biri; '
        'içeriğin çoğu abonelik arkasında, açık erişim makaleler ayrıca işaretli.',
        'Oxford University Press’s journal platform, one of the major publisher archives. '
        'Most content sits behind subscription, with open-access articles separately marked.', B)
    add('https://dergipark.org.tr/tr/', 'DergiPark', ['ücretsiz', 'türkçe', 'akademik'],
        'Türkiye akademik dergilerinin açık erişim platformu; binin üzerinde dergi barındırıyor. '
        'Türkçe literatür taraması için birincil kaynak, başka yerde toplu bulunmuyor.',
        'The open-access platform for Turkish academic journals, hosting over a thousand titles — '
        'the primary source for Turkish literature, not aggregated anywhere else.', B)
    add('https://aperta.ulakbim.gov.tr/', 'Aperta', ['ücretsiz', 'türkçe', 'veri', 'akademik'],
        'TÜBİTAK’ın açık arşivi; yayının yanında araştırma verisini de barındırıyor. '
        'Veri paylaşımı Türkiye’de henüz yaygın değil, bu yüzden dikkate değer.',
        'TÜBİTAK’s open archive, hosting research data alongside publications. '
        'Data sharing is not yet common in Turkey, which makes it notable.', B)
    add('https://harman.ulakbim.gov.tr/index', 'Harman', ['ücretsiz', 'türkçe', 'akademik'],
        'Türkiye’deki kurumsal akademik arşivleri tek noktadan aratan toplayıcı. '
        'Üniversite üniversite tez ve makale aramanın yerini alıyor.',
        'A harvester searching Turkey’s institutional academic archives from one place, '
        'replacing the university-by-university hunt for theses and articles.', B)
    add('https://www.wolframalpha.com/', 'Wolfram Alpha', ['freemium', 'hesaplama', 'matematik'],
        'Hesaplamalı bilgi motoru: integral alıyor, birim çeviriyor, veri karşılaştırıyor. '
        'Arama motoru cevabı bulur, bu hesaplar — ücretli katmanda adım adım çözümü de gösteriyor.',
        'A computational knowledge engine that integrates, converts units and compares data. A search engine finds '
        'the answer; this computes it, showing the working step by step in the paid tier.', B)
    add('https://www.nist.gov/pml/owm/metric-si-prefixes', 'SI Ön Ekleri (NIST)', ['ücretsiz', 'referans', 'standart'],
        'Ölçü birimi ön eklerinin resmî tablosu; ronna ve quetta gibi yeni eklenenler dahil. '
        'Birim dönüşümünde otoriter kaynak.',
        'The official table of unit prefixes, including recent additions like ronna and quetta — '
        'the authoritative reference for unit conversion.', B)
    add('https://stellarium-web.org/', 'Stellarium Web', ['açık-kaynak', 'astronomi', 'tarayıcı-içi'],
        'Bulunduğun konumun gerçek gökyüzünü tarayıcıda gösteriyor; zamanı ileri sarıp '
        'gezegen konumlarını görebiliyorsun. Kurulum gerektirmiyor.',
        'Shows the real sky for your location in the browser, with time you can wind forward to see planetary '
        'positions. No installation.', B)
    add('https://skyviewer.app/explorer', 'SkyViewer', ['ücretsiz', 'astronomi', 'veri'],
        'Gökyüzü tarama verilerini konuma göre gezdiriyor; teleskop görüntülerini üst üste '
        'bindirip farklı dalga boylarında karşılaştırabiliyorsun.',
        'Browses sky survey data by position, letting you overlay telescope imagery and compare across wavelengths.', B)
    add('https://www.inaturalist.org/', 'iNaturalist', ['ücretsiz', 'biyoloji', 'vatandaş-bilimi'],
        'Doğa gözlemlerini paylaşıp tür tespiti yaptırıyorsun; topluluk doğruladığında kayıt '
        'araştırma kalitesinde sayılıp GBIF’e aktarılıyor. Hobinin gerçek veriye dönüştüğü nadir örnek.',
        'Share nature observations and get species identified; once the community confirms one, the record becomes '
        'research-grade and flows into GBIF. A rare case of a hobby producing real data.', B)
    add('https://www.usap.gov/', 'ABD Antarktika Programı', ['ücretsiz', 'bilim', 'kurum'],
        'Antarktika araştırma programının resmî portalı; saha lojistiği ve istasyon operasyonları '
        'üzerine belgeler var. Aşırı koşullarda çalışan sistemler için ilginç bir kaynak.',
        'The official portal of the Antarctic research programme, with material on field logistics and station '
        'operations — an interesting source on systems that work in extreme conditions.', B)
    add('https://skybrary.aero/', 'SKYbrary', ['ücretsiz', 'havacılık', 'güvenlik'],
        'Havacılık emniyeti bilgi tabanı; kaza analizleri, insan faktörleri ve emniyet yönetim sistemleri. '
        'Yüksek güvenilirlikli sistem tasarımı üzerine düşünen herkes için kullanılabilir bir arşiv.',
        'An aviation safety knowledge base of accident analyses, human factors and safety management systems — '
        'a usable archive for anyone thinking about high-reliability system design.', B)
    add('https://commons.wikimedia.org/wiki/Main_Page', 'Wikimedia Commons', ['ücretsiz', 'medya', 'arşiv'],
        'Serbestçe kullanılabilir görsel ve medya arşivi; lisans her dosyada açıkça yazılı. '
        'Sunum ya da yayın için görsel ararken hukuki belirsizliği ortadan kaldırıyor.',
        'An archive of freely usable images and media with the licence stated explicitly on every file, '
        'which removes the legal ambiguity when sourcing visuals for a talk or publication.', B)
    add('https://en.wikipedia.org/wiki/Wikipedia:Contents/Portals', 'Vikipedi Portalları', ['ücretsiz', 'referans'],
        'Vikipedi’nin konu portalleri dizini; rastgele arama yerine bir alana yapılandırılmış giriş. '
        'Yeni bir konuya haritasız girmemek için.',
        'An index of Wikipedia’s topic portals — a structured way into a field instead of random search, '
        'and a way not to enter a new subject without a map.', B)
    add('https://blinpete.github.io/wiki-graph/', 'Wiki Graph', ['açık-kaynak', 'görselleştirme', 'graf'],
        'Vikipedi maddelerinin bağlantı ağını graf olarak gezdiriyor. '
        'Kavramlar arası uzaklığı metin okumadan görmek, bir alanın yapısını hızlı çıkarıyor.',
        'Explores Wikipedia’s link network as a graph. Seeing conceptual distance without reading the text '
        'sketches a field’s structure quickly.', B)
    add('https://learn-anything.xyz/', 'Learn Anything', ['ücretsiz', 'graf', 'öğrenme'],
        'Konuları ve aralarındaki bağı haritalayan öğrenme platformu; '
        'doğrusal müfredatın gizlediği komşulukları görünür kılıyor.',
        'A learning platform mapping topics and their connections, making visible the adjacencies a linear '
        'curriculum hides.', B)
    add('https://www.transkribus.org/models/ottoman-turkish-print', 'Transkribus · Osmanlıca', ['freemium', 'türkçe', 'ocr', 'arşiv'],
        'Osmanlı Türkçesi matbu metinler için eğitilmiş metin tanıma modeli. '
        'Genel OCR araçları Arap harfli Türkçeyi okuyamıyor; arşiv araştırmasında bu boşluk kritik.',
        'A text-recognition model trained on printed Ottoman Turkish. General OCR cannot read Arabic-script Turkish, '
        'and that gap is critical in archive research.', B)
    add('https://www.devletarsivleri.gov.tr/', 'Devlet Arşivleri', ['ücretsiz', 'türkçe', 'arşiv'],
        'Türkiye’nin resmî arşiv kurumu; Osmanlı ve Cumhuriyet dönemi belgelerinin katalog ve '
        'dijital kopyalarına erişim kapısı.',
        'Turkey’s official archive institution and the gateway to catalogues and digital copies of Ottoman and '
        'Republican-era documents.', B)
    add('https://nek.istanbul.edu.tr/ekos/GAZETE/', 'İÜ Gazete Arşivi', ['ücretsiz', 'türkçe', 'arşiv'],
        'İstanbul Üniversitesi’nin taranmış tarihî gazete koleksiyonu. '
        'Dönem araştırmasında birincil kaynak; ikincil literatürün atladığı ayrıntılar burada çıkıyor.',
        'Istanbul University’s scanned historical newspaper collection — primary sources for period research, '
        'where the details secondary literature skips turn up.', B)
    add('https://www.davidrumsey.com/', 'David Rumsey Harita Koleksiyonu', ['ücretsiz', 'harita', 'arşiv'],
        'Yüksek çözünürlüklü tarihî harita arşivi; haritaları modern coğrafyaya bindirip '
        'karşılaştırabiliyorsun. Yer adı ve sınır değişimlerini izlemek için güçlü bir araç.',
        'A high-resolution historical map archive that lets you georeference maps onto modern geography — '
        'a strong tool for tracking place-name and border change.', B)
    add('https://archeprojesi.com/', 'Arkhe Projesi', ['ücretsiz', 'türkçe', 'bilim'],
        'Türkçe bilim ve felsefe yazıları; popüler bilimin yüzeyselliği ile akademik dilin '
        'kapalılığı arasında bir yer tutuyor.',
        'Turkish science and philosophy writing that sits between the shallowness of popular science and the '
        'opacity of academic register.', B)
    add('https://onculanalitikfelsefe.com/unlu-dusunce-deneyleri-metaforlar-ve-paradokslar-bolum-1-zihin-felsefesi-ibrahim-yesua-ozcelik-hasan-alparslan-bayrak/', 'Düşünce Deneyleri ve Paradokslar', ['ücretsiz', 'türkçe', 'felsefe'],
        'Zihin felsefesindeki ünlü düşünce deneylerinin Türkçe derlemesi: Çin Odası, '
        'zombiler, Mary’nin odası. Yapay zeka tartışmalarının felsefi arka planı burada.',
        'A Turkish compilation of famous thought experiments in philosophy of mind — the Chinese Room, zombies, '
        'Mary’s room. The philosophical backdrop to current AI arguments.', B)
    add('https://www.etimolojiturkce.com/', 'Etimoloji Türkçe', ['ücretsiz', 'türkçe', 'sözlük'],
        'Türkçe sözcüklerin kökenini kaynak göstererek veren sözlük; hangi dilden ne zaman '
        'geçtiğini ve ilk kaydını gösteriyor. Nişanyan’ın çalışmasına dayanıyor.',
        'An etymological dictionary of Turkish citing its sources, showing which language each word came from, '
        'when, and its earliest attestation. Built on Nişanyan’s work.', B)
    add('https://www.nisanyanyeradlari.com/', 'Nişanyan Yeradları', ['ücretsiz', 'türkçe', 'coğrafya'],
        'Türkiye ve çevresindeki yerleşim adlarının tarihsel envanteri; ad değişikliklerini '
        'tarih ve kaynağıyla belgeliyor. Başka hiçbir yerde bu sistematiklikte derlenmemiş.',
        'A historical inventory of settlement names in and around Turkey, documenting each change with date and '
        'source. Nothing else compiles this systematically.', B)
    add('https://www.ethnologue.com/', 'Ethnologue', ['ücretli', 'dilbilim', 'referans'],
        'Dünya dillerinin standart kataloğu; konuşan sayısı ve canlılık derecesi sistematik veriliyor. '
        'ISO 639-3 dil kodlarının kayıt otoritesi de bu.',
        'The standard catalogue of world languages with systematic speaker counts and vitality ratings. '
        'It is also the registration authority for ISO 639-3 language codes.', B)
    add('https://search.language-archives.org/', 'Open Language Archives (arama)', ['ücretsiz', 'dilbilim', 'arşiv'],
        'Dil kaynaklarını dağınık kurum arşivlerinden tek noktada aratıyor; '
        'özellikle belgelenmemiş ve tehlike altındaki diller için materyal bulmaya yarıyor.',
        'Searches language resources across scattered institutional archives from one place, '
        'particularly useful for material on under-documented and endangered languages.', B)
