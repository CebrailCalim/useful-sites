# -*- coding: utf-8 -*-
"""Araçlar & Yardımcılar · Bilim & Akademik

Not: kaynak yer imlerindeki tek tek Vikipedi makaleleri (kisisel okuma)
bilerek disarida birakildi; burada yalnizca baskasinin da kullanabilecegi
kaynaklar var.
"""


def load(add):
    # ============================================================ ARAÇLAR & YARDIMCILAR
    T = 'araclar'
    add('https://excalidraw.com/', 'Excalidraw', ['ücretsiz', 'açık kaynak', 'diyagram'],
        'El çizimi görünümlü beyaz tahta; kasıtlı olarak kaba görünmesi, taslak aşamasında tasarımın bitmiş sanılmasını engelliyor.',
        'A hand-drawn-style whiteboard; looking deliberately rough stops people mistaking a sketch for a finished design.', T)
    add('https://www.drawio.com/', 'draw.io', ['ücretsiz', 'açık kaynak', 'diyagram'],
        'Genel amaçlı diyagram aracı; Excalidraw’dan farkı, ağ ve UML gibi standart şekil kütüphaneleriyle gelmesi.',
        'General-purpose diagramming; unlike Excalidraw it ships standard shape libraries for network and UML work.', T)
    add('https://mermaid.live/edit', 'Mermaid Live Editor', ['ücretsiz', 'diyagram', 'metin'],
        'Metinden diyagram üreten editör; grafik araçlardan farkı, diyagramın sürüm kontrolüne girebilen düz metin olması.',
        'Text-to-diagram editor; unlike graphical tools the diagram is plain text that can live in version control.', T)
    add('https://moqups.com/', 'Moqups', ['freemium', 'tasarım', 'prototip'],
        'Tarayıcıda tel kafes ve prototip aracı; Figma’ya göre daha hafif, hızlı taslak için yeterli.',
        'Browser wireframing and prototyping — lighter than Figma and sufficient for quick drafts.', T)
    add('https://www.figma.com/', 'Figma', ['freemium', 'tasarım'],
        'Arayüz tasarımının fiilî standardı; eşzamanlı çok kişili düzenleme onu masaüstü araçların önüne geçirdi.',
        'The de facto standard for interface design; real-time multiplayer editing is what put it ahead of desktop tools.', T)
    add('https://transform.tools/', 'Transform', ['ücretsiz', 'dönüştürücü'],
        'Biçimler arası dönüştürücü koleksiyonu (JSON→TypeScript, CSS→JS vb.); tek tek araç aramaya karşı toplu çözüm.',
        'A collection of format converters (JSON→TypeScript, CSS→JS and so on) — one place instead of hunting a tool per conversion.', T)
    add('https://regex101.com/', 'regex101', ['ücretsiz', 'araç', 'regex'],
        'Düzenli ifade test ve açıklama aracı; ifadeyi parça parça açıklaması ve hata ayıklayıcısı ayırt edici yanı.',
        'Regex tester whose distinguishing features are the token-by-token explanation and the debugger.', T)
    add('https://godbolt.org/', 'Compiler Explorer', ['ücretsiz', 'açık kaynak', 'derleyici'],
        'Kaynak kodun ürettiği makine kodunu yan yana gösteren araç; optimizasyon tartışmalarını fikirden ölçüme taşır.',
        'Shows source code beside the machine code it produces, moving optimisation debates from opinion to evidence.', T)
    add('https://carbon.now.sh/', 'Carbon', ['ücretsiz', 'görsel', 'kod'],
        'Kod parçasından paylaşılabilir görsel üreten araç; ekran görüntüsünden farkı, tema ve satır numarasını denetleyebilmen.',
        'Turns a code snippet into a shareable image; unlike a screenshot you control theme and line numbers.', T)
    add('https://www.ilovepdf.com/', 'iLovePDF', ['freemium', 'pdf', 'araç'],
        'Birleştirme, bölme, sıkıştırma gibi PDF işlemleri; kurulum gerektirmemesi tek seferlik işler için avantaj.',
        'PDF merge, split and compress operations; needing no installation is the advantage for one-off jobs.', T)
    add('https://www.textise.net/', 'Textise', ['ücretsiz', 'araç', 'erişilebilirlik'],
        'Bir sayfayı yalnızca metne indirgeyen araç; reklam ve düzen gürültüsünü kaldırıp okunabilirlik ve erişilebilirlik testi sağlıyor.',
        'Reduces a page to text only, stripping ads and layout noise for readability and accessibility checks.', T)
    add('https://alternativeto.net/', 'AlternativeTo', ['ücretsiz', 'dizin'],
        'Bir yazılıma alternatif bulmanın standart yolu; kullanıcı oylarıyla sıralaması ve lisansa göre filtrelemesi ayırt edici.',
        'The standard way to find an alternative to a piece of software, ranked by user votes and filterable by licence.', T)
    add('https://free-for.dev/', 'Free for Developers', ['ücretsiz', 'koleksiyon'],
        'Ücretsiz katman sunan geliştirici servislerinin listesi; yan proje maliyetini sıfıra yakın tutmak için.',
        'A list of developer services with free tiers — for keeping a side project’s cost near zero.', T)
    add('https://same.energy/', 'Same Energy', ['ücretsiz', 'arama', 'görsel'],
        'Görsel benzerliğe göre arama motoru; anahtar kelime yerine estetik üzerinden keşif sunması ayırt edici.',
        'A search engine driven by visual similarity, offering discovery through aesthetics rather than keywords.', T)
    add('https://feedly.com/', 'Feedly', ['freemium', 'rss'],
        'RSS okuyucu; algoritmik akışların aksine ne okuyacağına kaynak düzeyinde sen karar verirsin.',
        'RSS reader — unlike algorithmic feeds you decide what you read at the source level.', T)
    add('https://www.parse.bot/', 'Parse', ['freemium', 'veri', 'kazıma'],
        'Herhangi bir web sayfasından API üreten araç; kazıyıcı kodu yazmadan yapılandırılmış veri almayı hedefliyor.',
        'Creates an API from any web page, aimed at getting structured data without writing a scraper.', T)
    add('https://www.audionotes.app/', 'AudioNotes', ['freemium', 'ses', 'not'],
        'Sesli notu yapılandırılmış metne çeviren uygulama; ham döküm yerine özet ve madde çıkarması ayırt edici.',
        'Turns voice notes into structured text, producing summaries and bullet points rather than a raw transcript.', T)
    add('https://www.macrodroid.com/', 'MacroDroid', ['freemium', 'android', 'otomasyon'],
        'Android’de cihaz otomasyonu; Tasker’a göre çok daha erişilebilir bir arayüzle aynı işi yapmayı hedefliyor.',
        'Device automation on Android, aiming at Tasker’s capability through a far more approachable interface.', T)
    add('https://sxp.studio/apps/applist', 'AppList', ['ücretsiz', 'ios', 'minimalizm'],
        'iPhone için sade uygulama başlatıcı; simge ızgarasının dikkat dağıtıcılığına karşı metin listesi sunuyor.',
        'A minimal app launcher for iPhone, offering a text list against the distraction of an icon grid.', T)
    add('https://codewiki.google/', 'CodeWiki', ['ücretsiz', 'google', 'kod'],
        'Kod tabanları için otomatik üretilmiş dokümantasyon; depoya ilk bakışta yapıyı kavramak için.',
        'Automatically generated documentation for codebases, for grasping structure at first contact with a repo.', T)
    add('https://codescene.com/', 'CodeScene', ['ücretli', 'analiz', 'teknik borç'],
        'Kod tabanını değişim geçmişiyle birlikte analiz eden araç; statik çözümleyicilerden farkı, en çok değişen ve en riskli dosyaları öne çıkarması.',
        'Analyses a codebase alongside its change history; unlike static analysers it surfaces the files that churn most and carry most risk.', T)
    add('https://labs.google/', 'Google Labs', ['ücretsiz', 'deneysel'],
        'Google’ın deneysel ürünlerinin vitrini; yayımlanmadan önce araçları denemek için.',
        'A showcase of Google’s experimental products, for trying tools before general release.', T)
    add('https://github.com/HQarroum/docker-android', 'Docker Android', ['açık kaynak', 'github', 'docker'],
        'Kapsayıcı içinde Android çalıştıran imaj; test otomasyonunu fiziksel cihaz ve emülatör kurulumundan kurtarıyor.',
        'An image running Android inside a container, freeing test automation from physical devices and emulator setup.', T)
    add('https://github.com/Augani/openreel-video', 'OpenReel Video', ['açık kaynak', 'github', 'video'],
        'Tarayıcıda çalışan açık kaynak video düzenleyici; kurulum gerektirmeyen ve verinin cihazda kaldığı bir alternatif.',
        'Open-source video editor running in the browser — an alternative with no install where the footage stays on device.', T)
    add('https://github.com/getagentseal/codeburn', 'CodeBurn', ['açık kaynak', 'github', 'araç'],
        'Kod tabanı üzerinde çalışan analiz aracı; ölü kod ve gereksiz bağımlılıkları temizlemeye yönelik.',
        'Analysis tool for a codebase, aimed at clearing dead code and unnecessary dependencies.', T)
    add('https://github.com/punitarani/fli', 'fli', ['açık kaynak', 'github', 'cli'],
        'Uçuş arama için komut satırı aracı; tarayıcı arayüzlerinin aksine sonuçları betiklenebilir hâle getiriyor.',
        'A command-line flight search tool, making results scriptable unlike browser interfaces.', T)
    add('https://github.com/ZeoRexDevs/Udeler_GUI', 'Udeler GUI', ['açık kaynak', 'github', 'araç'],
        'Satın alınan Udemy kurslarını çevrimdışı izlemek için indirici; erişimi olan içerik için arşivleme aracı.',
        'A downloader for offline viewing of purchased Udemy courses — an archiving tool for content you already have access to.', T)
    add('https://keepnote.org/', 'KeepNote', ['açık kaynak', 'not'],
        'Basit ve taşınabilir not defteri uygulaması; bulut hizmetlerine karşı dosyaların diskte kalmasını isteyenler için.',
        'A simple, portable note-taking app for people who want their files on disk rather than in a cloud service.', T)
    add('https://appsgolem.com/en/cut-youtube-video/', 'YouTube Video Kesici', ['ücretsiz', 'video', 'araç'],
        'Bir videodan belirli aralığı kesip indiren araç; tamamını indirip düzenlemeye karşı hızlı çözüm.',
        'Cuts and downloads a specific range from a video — quicker than downloading the whole thing and editing.', T)
    add('https://dynomapper.com/blog/inventory-content/how-to-download-a-website-for-offline-viewing/', 'Siteyi Çevrimdışı İndirme', ['ücretsiz', 'rehber', 'arşiv'],
        'Bir web sitesini çevrimdışı arşivlemenin yöntemlerini karşılaştıran rehber; kaybolma riski olan kaynaklar için.',
        'A guide comparing methods for archiving a website offline — for resources at risk of disappearing.', T)
    add('https://www.technopat.net/sosyal/indir/', 'Technopat İndirilenler', ['ücretsiz', 'türkçe', 'yazılım'],
        'Türkçe yazılım indirme ve tartışma arşivi; yerel kullanıcı deneyimlerinin bir arada bulunduğu bir kaynak.',
        'A Turkish software download and discussion archive, gathering local user experience in one place.', T)
    add('https://sourceforge.net/projects/embarcadero-devcpp/files/v6.3/', 'Embarcadero Dev-C++', ['ücretsiz', 'ide', 'c++'],
        'Hafif C/C++ geliştirme ortamı; modern IDE’lere göre eski ama düşük donanımda ve eğitim ortamlarında hâlâ kullanılıyor.',
        'A lightweight C/C++ IDE — dated next to modern ones, but still used on low-spec machines and in teaching.', T)
    add('https://www.youtube.com/watch?v=rbu7Zu5X1zI', 'Araç Kullanımı (video)', ['ücretsiz', 'video'],
        'Geliştirici araçları üzerine anlatım videosu; yazılı dokümana alternatif olarak izleyerek öğrenmek için.',
        'A walkthrough video on developer tooling, for those who would rather watch than read the docs.', T)
    add('https://www.youtube.com/watch?v=uOPl7ZzuXf8&list=PLi2GhhsPL-RrapHA_Z8c1GG_qM3Nzdd0j&index=2', 'Araç Serisi (oynatma listesi)', ['ücretsiz', 'video'],
        'Araç ve iş akışı üzerine video serisi; tek videodan farkı, konuyu adım adım derinleştirmesi.',
        'A video series on tooling and workflow; unlike a single video it deepens the topic step by step.', T)
    # trend & istatistik
    add('https://www.tiobe.com/tiobe-index/', 'TIOBE Index', ['ücretsiz', 'istatistik'],
        'Programlama dillerinin popülerlik endeksi; yöntemi tartışmalı ama uzun zaman serisi sunması sebebiyle eğilim izlemekte kullanılıyor.',
        'A popularity index of programming languages — its methodology is debated, but the long time series makes it useful for trends.', T)
    add('https://octotrends.com/', 'OctoTrends', ['ücretsiz', 'github', 'istatistik'],
        'GitHub depolarının büyüme eğilimini gösteren araç; anlık yıldız sayısından farkı, ivmeyi göstermesi.',
        'Shows growth trends for GitHub repositories; unlike a raw star count it reveals momentum.', T)
    add('https://gitstar-ranking.com/repositories', 'GitStar Ranking', ['ücretsiz', 'github', 'istatistik'],
        'GitHub depo ve kullanıcılarının yıldız sıralaması; bir alanda neyin baskın olduğunu hızlıca görmek için.',
        'Star rankings for GitHub repos and users — a fast way to see what dominates a field.', T)
    add('https://trendshift.io/', 'Trendshift', ['ücretsiz', 'github', 'istatistik'],
        'Yükselen açık kaynak projeleri izleyen pano; olgunlaşmış listelerden farkı, yeni çıkanları öne alması.',
        'A dashboard tracking rising open-source projects, favouring new arrivals over established lists.', T)
    add('https://www.visualcapitalist.com/', 'Visual Capitalist', ['ücretsiz', 'veri görselleştirme'],
        'Ekonomi ve teknoloji verisini bilgi grafiklerine çeviren yayın; ham veri kaynağı değil, bağlam ve karşılaştırma sunar.',
        'A publication turning economic and technology data into infographics — context and comparison rather than raw data.', T)

    # ============================================================ BİLİM & AKADEMİK
    B = 'bilim'
    add('https://arxiv.org/', 'arXiv', ['ücretsiz', 'akademik', 'ön baskı'],
        'Fizik, matematik ve bilgisayar biliminin ön baskı arşivi; hakem sürecinden önce yayımlanması sayesinde alanın en güncel hâli burada.',
        'The preprint archive for physics, maths and computer science — publishing before peer review is why the field’s latest work appears here first.', B)
    add('https://www.semanticscholar.org/', 'Semantic Scholar', ['ücretsiz', 'akademik', 'arama'],
        'Yapay zeka destekli akademik arama; Google Scholar’dan farkı, atıfların bağlamını ve etkisini çözümlemesi.',
        'AI-powered academic search; unlike Google Scholar it analyses the context and influence of citations.', B)
    add('https://www.connectedpapers.com/', 'Connected Papers', ['freemium', 'akademik', 'görselleştirme'],
        'Bir makalenin etrafındaki literatür ağını haritalayan araç; kaynakça takibine karşı alanı görsel olarak keşfettirir.',
        'Maps the literature network around a paper, letting you explore a field visually instead of chasing bibliographies.', B)
    add('https://www.doi.org/', 'DOI', ['ücretsiz', 'akademik', 'standart'],
        'Akademik yayınların kalıcı tanımlayıcı sistemi; bağlantı çürümesine karşı atıfların uzun ömürlü kalmasını sağlar.',
        'The persistent identifier system for scholarly work, keeping citations durable against link rot.', B)
    add('https://academic.oup.com/', 'Oxford Academic', ['ücretli', 'akademik', 'yayın'],
        'Oxford University Press dergi platformu; büyük yayıncı arşivlerinden biri, çoğu içerik abonelik gerektiriyor.',
        'Oxford University Press’s journal platform — one of the major publisher archives, mostly subscription-gated.', B)
    add('https://dergipark.org.tr/tr/', 'DergiPark', ['ücretsiz', 'türkçe', 'akademik'],
        'Türkiye akademik dergilerinin açık erişim platformu; Türkçe literatür taraması için birincil kaynak.',
        'Open-access platform for Turkish academic journals — the primary source for surveying Turkish-language literature.', B)
    add('https://aperta.ulakbim.gov.tr/', 'Aperta', ['ücretsiz', 'türkçe', 'veri'],
        'TÜBİTAK’ın açık arşivi; yayınların yanında araştırma verisini de barındırması ayırt edici yanı.',
        'TÜBİTAK’s open archive, distinguished by hosting research data alongside publications.', B)
    add('https://harman.ulakbim.gov.tr/index', 'Harman', ['ücretsiz', 'türkçe', 'akademik'],
        'Türkiye’deki kurumsal akademik arşivleri tek noktadan aratan toplayıcı; üniversite üniversite gezmeye alternatif.',
        'A harvester searching Turkey’s institutional academic archives from one point, instead of visiting each university.', B)
    add('https://www.wolframalpha.com/', 'Wolfram Alpha', ['freemium', 'hesaplama'],
        'Hesaplamalı bilgi motoru; arama motorlarından farkı, sonucu bulmak yerine adım adım hesaplaması.',
        'A computational knowledge engine; unlike search engines it computes the answer step by step rather than finding it.', B)
    add('https://www.nist.gov/pml/owm/metric-si-prefixes', 'SI Ön Ekleri (NIST)', ['ücretsiz', 'referans', 'standart'],
        'Ölçü birimi ön eklerinin resmî tablosu; birim dönüşümlerinde otoriter kaynak.',
        'The official table of unit prefixes — the authoritative source for unit conversions.', B)
    add('https://stellarium-web.org/', 'Stellarium Web', ['ücretsiz', 'açık kaynak', 'astronomi'],
        'Tarayıcıda çalışan gökyüzü haritası; kurulum gerektirmeden bulunduğun konumun gerçek gökyüzünü gösteriyor.',
        'A sky map in the browser, showing the real sky for your location with no installation.', B)
    add('https://skyviewer.app/explorer', 'SkyViewer', ['ücretsiz', 'astronomi'],
        'Gökyüzü gözlem verilerini gezmek için görsel arayüz; teleskop görüntülerini konuma göre keşfetmeye yarıyor.',
        'A visual interface for exploring sky survey data, letting you browse telescope imagery by position.', B)
    add('https://www.inaturalist.org/', 'iNaturalist', ['ücretsiz', 'biyoloji', 'topluluk'],
        'Doğa gözlemlerini paylaşıp tür tespiti yaptıran platform; kayıtların bilimsel veri olarak kullanılması ayırt edici yanı.',
        'A platform for sharing nature observations and getting species identified; its records feeding real scientific datasets is what sets it apart.', B)
    add('https://www.usap.gov/', 'ABD Antarktika Programı', ['ücretsiz', 'bilim', 'kurum'],
        'Antarktika araştırma programının resmî portalı; kutup bilimi ve saha lojistiği üzerine birincil kaynak.',
        'The official portal of the Antarctic research programme — a primary source on polar science and field logistics.', B)
    add('https://skybrary.aero/', 'SKYbrary', ['ücretsiz', 'havacılık', 'referans'],
        'Havacılık emniyeti bilgi tabanı; kaza analizleri ve insan faktörleri konusunda güvenlik mühendisliğine de örnek teşkil eder.',
        'An aviation safety knowledge base whose accident analyses and human-factors material double as safety engineering case studies.', B)
    add('https://commons.wikimedia.org/wiki/Main_Page', 'Wikimedia Commons', ['ücretsiz', 'medya', 'arşiv'],
        'Serbestçe kullanılabilir görsel ve medya arşivi; lisans durumunun her dosyada açıkça belirtilmesi ayırt edici yanı.',
        'An archive of freely usable images and media, distinguished by stating the licence explicitly on every file.', B)
    add('https://en.wikipedia.org/wiki/Wikipedia:Contents/Portals', 'Vikipedi Portalları', ['ücretsiz', 'referans'],
        'Vikipedi’nin konu portallerinin dizini; rastgele arama yerine bir alana yapılandırılmış giriş sunar.',
        'An index of Wikipedia’s topic portals, offering a structured entry into a field instead of random search.', B)
    add('https://blinpete.github.io/wiki-graph/', 'Wiki Graph', ['ücretsiz', 'açık kaynak', 'görselleştirme'],
        'Vikipedi maddelerinin bağlantı ağını graf olarak gezdiren araç; kavramlar arası ilişkiyi metin okumadan görmek için.',
        'Explores Wikipedia’s link network as a graph, showing relationships between concepts without reading the text.', B)
    add('https://learn-anything.xyz/', 'Learn Anything', ['ücretsiz', 'harita', 'öğrenme'],
        'Konuları ve aralarındaki bağlantıyı haritalayan öğrenme platformu; doğrusal müfredatın gizlediği komşulukları görünür kılar.',
        'A learning platform mapping topics and their connections, revealing the adjacencies a linear curriculum hides.', B)
    add('https://www.transkribus.org/models/ottoman-turkish-print', 'Transkribus · Osmanlıca', ['freemium', 'türkçe', 'ocr'],
        'Osmanlı Türkçesi matbu metinleri için el yazısı/metin tanıma modeli; genel OCR araçlarının okuyamadığı arşiv belgelerini çözer.',
        'A text-recognition model for printed Ottoman Turkish, handling archive documents general OCR tools cannot read.', B)
    add('https://www.devletarsivleri.gov.tr/', 'Devlet Arşivleri', ['ücretsiz', 'türkçe', 'arşiv'],
        'Türkiye’nin resmî arşiv kurumu; Osmanlı ve Cumhuriyet dönemi belgelerine erişim için birincil kapı.',
        'Turkey’s official archive institution — the primary gateway to Ottoman and Republican-era documents.', B)
    add('https://nek.istanbul.edu.tr/ekos/GAZETE/', 'İÜ Gazete Arşivi', ['ücretsiz', 'türkçe', 'arşiv'],
        'İstanbul Üniversitesi’nin tarihî gazete koleksiyonu; dönem araştırması için taranmış birincil kaynak.',
        'Istanbul University’s historical newspaper collection — scanned primary sources for period research.', B)
    add('https://www.davidrumsey.com/', 'David Rumsey Harita Koleksiyonu', ['ücretsiz', 'harita', 'arşiv'],
        'Yüksek çözünürlüklü tarihî harita arşivi; haritaları modern coğrafyaya bindirebilmesi ayırt edici yanı.',
        'A high-resolution historical map archive, distinguished by letting you overlay maps onto modern geography.', B)
    add('https://archeprojesi.com/', 'Arkhe Projesi', ['ücretsiz', 'türkçe', 'bilim'],
        'Türkçe bilim ve felsefe yazıları üreten proje; popüler bilim ile akademik dil arasında bir yer tutuyor.',
        'A project publishing Turkish science and philosophy writing, sitting between popular science and academic register.', B)
    add('https://onculanalitikfelsefe.com/unlu-dusunce-deneyleri-metaforlar-ve-paradokslar-bolum-1-zihin-felsefesi-ibrahim-yesua-ozcelik-hasan-alparslan-bayrak/', 'Düşünce Deneyleri ve Paradokslar', ['ücretsiz', 'türkçe', 'felsefe'],
        'Zihin felsefesindeki ünlü düşünce deneylerinin Türkçe derlemesi; kavramları örnek üzerinden anlatması ayırt edici.',
        'A Turkish compilation of famous thought experiments in philosophy of mind, teaching concepts through examples.', B)
    add('https://www.etimolojiturkce.com/', 'Etimoloji Türkçe', ['ücretsiz', 'türkçe', 'sözlük'],
        'Türkçe sözcüklerin kökenini veren etimoloji sözlüğü; sözcüğün hangi dilden ne zaman geldiğini göstermesi ayırt edici.',
        'An etymological dictionary of Turkish, showing which language each word came from and when.', B)
    add('https://www.nisanyanyeradlari.com/', 'Nişanyan Yeradları', ['ücretsiz', 'türkçe', 'coğrafya'],
        'Türkiye ve çevresindeki yerleşim adlarının tarihsel envanteri; ad değişikliklerini kaynağıyla belgelemesi ayırt edici yanı.',
        'A historical inventory of settlement names in and around Turkey, documenting name changes with sources.', B)
    add('https://www.ethnologue.com/', 'Ethnologue', ['ücretli', 'dilbilim', 'referans'],
        'Dünya dillerinin standart kataloğu; konuşan sayısı ve canlılık durumunu sistematik vermesiyle referans kabul edilir.',
        'The standard catalogue of world languages, treated as a reference for its systematic speaker counts and vitality status.', B)
    add('https://search.language-archives.org/', 'Open Language Archives', ['ücretsiz', 'dilbilim', 'arşiv'],
        'Dil kaynaklarını tek noktadan arayan toplayıcı; özellikle belgelenmemiş diller üzerine materyal için.',
        'A harvester searching language resources from one point, especially for material on under-documented languages.', B)
