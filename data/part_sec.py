# -*- coding: utf-8 -*-
"""Güvenlik & Gizlilik, Kuantum, Referans"""


def load(add):
    # ============================================================ GÜVENLİK & GİZLİLİK
    G = 'guvenlik'
    add('https://tryhackme.com/', 'TryHackMe', ['freemium', 'güvenlik', 'interaktif'],
        'Rehberli güvenlik laboratuvarları; Hack The Box’tan farkı, elinden tutup adım adım ilerletmesi — yeni başlayan için daha uygun.',
        'Guided security labs; unlike Hack The Box it walks you through step by step, which suits beginners better.', G)
    add('https://www.hackthebox.com/', 'Hack The Box', ['freemium', 'güvenlik', 'interaktif'],
        'Gerçekçi sızma testi laboratuvarları; ipucu vermemesiyle TryHackMe’den ayrılır, araştırma yükünü sana bırakır.',
        'Realistic penetration testing labs; it withholds hints, unlike TryHackMe, leaving the research to you.', G)
    add('https://overthewire.org/wargames/', 'OverTheWire Wargames', ['ücretsiz', 'güvenlik', 'ctf'],
        'SSH üzerinden oynanan klasik güvenlik savaş oyunları; kayıt ve arayüz olmadan doğrudan kabuğa düşürmesi ayırt edici.',
        'Classic security wargames played over SSH — dropping you straight into a shell with no signup or UI is its distinction.', G)
    add('https://cyberexam.io/', 'CyberExam', ['freemium', 'güvenlik', 'sınav'],
        'Güvenlik sertifikalarına yönelik pratik laboratuvar ve sınav ortamı; teorik soru bankalarına karşı uygulamalı hazırlık.',
        'Practical labs and exam environment for security certifications — hands-on prep against theory-only question banks.', G)
    add('https://www.hackerone.com/', 'HackerOne', ['ücretsiz', 'güvenlik', 'ödül'],
        'Hata ödül programı platformu; laboratuvarların aksine gerçek sistemlerde yasal olarak test yapma imkânı verir.',
        'Bug bounty platform — unlike labs it lets you legally test real production systems.', G)
    add('https://siberguvenlik.gov.tr/', 'Siber Güvenlik Başkanlığı', ['ücretsiz', 'türkçe', 'resmî'],
        'Türkiye’nin resmî siber güvenlik kurumu; ulusal uyarılar ve mevzuat için birincil kaynak.',
        'Turkey’s official cyber security authority — the primary source for national advisories and regulation.', G)
    add('https://github.com/farhanashrafdev/90DaysOfCyberSecurity', '90 Days of Cyber Security', ['ücretsiz', 'github', 'müfredat'],
        'Doksan günlük güvenlik çalışma planı; dağınık kaynak listelerine karşı takvimli bir program sunar.',
        'A 90-day security study plan — a dated schedule against the usual scattered resource lists.', G)
    add('https://github.com/LuNiZz/siber-guvenlik-sss', 'Siber Güvenlik SSS', ['ücretsiz', 'türkçe', 'github'],
        'Türkçe siber güvenlik sıkça sorulan sorular derlemesi; alana giriş yapanların kariyer sorularını da kapsaması ayırt edici.',
        'A Turkish cyber security FAQ, distinguished by also covering the career questions newcomers actually ask.', G)
    add('https://www.cybernotes.tech/', 'CyberNotes', ['ücretsiz', 'güvenlik', 'not'],
        'Güvenlik konularının derli toplu not arşivi; sınav ve laboratuvar sırasında hızlı başvuru için.',
        'A tidy note archive of security topics, for quick reference during labs and exams.', G)
    add('https://osintframework.com/', 'OSINT Framework', ['ücretsiz', 'osint', 'dizin'],
        'Açık kaynak istihbarat araçlarını ağaç yapısında toplayan dizin; ne aradığına göre araca inmen için tasarlanmış.',
        'A tree-structured directory of open-source intelligence tools, designed so you descend to a tool by what you are looking for.', G)
    add('https://start.me/p/DPYPMz/the-ultimate-osint-collection', 'The Ultimate OSINT Collection', ['ücretsiz', 'osint', 'koleksiyon'],
        'Kategorilere ayrılmış geniş OSINT bağlantı panosu; framework’e göre daha güncel tutulan bir alternatif.',
        'A broad categorised OSINT link board — a more frequently updated alternative to the framework.', G)
    add('https://github.com/apurvsinghgautam/robin', 'Robin', ['açık kaynak', 'github', 'osint'],
        'Karanlık ağ araştırması için yapay zeka destekli OSINT aracı; elle arama yapmaya karşı otomatik tarama sunar.',
        'AI-assisted OSINT tool for dark web research, offering automated sweeps instead of manual searching.', G)
    add('https://github.com/redhuntlabs/Awesome-Asset-Discovery', 'Awesome Asset Discovery', ['ücretsiz', 'github', 'koleksiyon'],
        'Varlık keşfi araç ve yöntemlerinin listesi; sızma testinin ilk aşaması için toplu başvuru.',
        'A list of asset discovery tools and methods — a single reference for the first phase of a penetration test.', G)
    add('https://github.com/jivoi/awesome-ml-for-cybersecurity', 'Awesome ML for Cybersecurity', ['ücretsiz', 'github', 'koleksiyon'],
        'Güvenlikte makine öğrenmesi kaynakları listesi; veri kümeleri ve makaleleri bir arada vermesi ayırt edici.',
        'A list of machine learning resources for security, distinguished by gathering datasets and papers together.', G)
    add('https://github.com/wtsxDev/Machine-Learning-for-Cyber-Security', 'ML for Cyber Security', ['ücretsiz', 'github', 'koleksiyon'],
        'Güvenlik alanında ML çalışmalarının bir başka derlemesi; araç ve kurs tarafı daha ağır basıyor.',
        'Another compilation of ML work in security, leaning more towards tools and courses.', G)
    add('https://github.com/WKL-Sec/Illicit-Services-Enum-Script', 'Illicit Services Enum', ['açık kaynak', 'github', 'güvenlik'],
        'Servis numaralandırma betiği; keşif aşamasını otomatikleştiren dar kapsamlı bir araç.',
        'A service enumeration script — a narrow tool automating the reconnaissance phase.', G)
    add('https://github.com/lauriewired/ghidramcp', 'GhidraMCP', ['açık kaynak', 'github', 'tersine mühendislik', 'mcp'],
        'Ghidra tersine mühendislik aracını yapay zeka asistanına bağlayan MCP sunucusu; ikili çözümlemede asistan kullanmayı mümkün kılıyor.',
        'MCP server connecting the Ghidra reverse-engineering tool to an AI assistant, enabling assistant-driven binary analysis.', G)
    add('https://www.youtube.com/watch?v=iCbOV8p6tD4', 'Siber Güvenlik Anlatımı', ['ücretsiz', 'video', 'güvenlik'],
        'Güvenlik kavramlarına video giriş; okumadan önce alanın haritasını görmek için.',
        'A video introduction to security concepts, for mapping the field before reading.', G)
    add('https://www.youtube.com/watch?v=p3vaaD9pn9I', 'Güvenlik Uygulaması', ['ücretsiz', 'video', 'güvenlik'],
        'Uygulamalı güvenlik anlatımı; teorik dersin ardından tekniği çalışırken görmek için.',
        'A hands-on security walkthrough, for seeing a technique in action after the theory.', G)
    add('https://www.turkhackteam.org/konular/access-point-ve-monitor-mod-destekli-wifi-kartini-nereden-bulabilirim.2051107/', 'Monitör Mod Wi-Fi Kartı', ['ücretsiz', 'türkçe', 'donanım'],
        'Monitör modu destekleyen Wi-Fi kartı seçimi üzerine Türkçe tartışma; kablosuz güvenlik testine başlarken donanım sorusunu çözer.',
        'A Turkish discussion on picking a monitor-mode Wi-Fi adapter — it answers the hardware question before wireless testing.', G)
    # gizlilik
    add('https://bitwarden.com/', 'Bitwarden', ['freemium', 'açık kaynak', 'gizlilik'],
        'Açık kaynak parola yöneticisi; rakiplerinden farkı, kodunun denetlenebilir olması ve kendi sunucunda çalıştırılabilmesi.',
        'Open-source password manager; unlike rivals its code is auditable and it can be self-hosted.', G)
    add('https://privnote.com/', 'Privnote', ['ücretsiz', 'gizlilik'],
        'Okunduktan sonra kendini silen not gönderme aracı; hesap gerektirmemesi tek seferlik sır paylaşımını kolaylaştırıyor.',
        'Sends notes that self-destruct after reading; needing no account makes one-off secret sharing easy.', G)
    add('https://silent.link/#generic_price_table', 'Silent Link', ['ücretli', 'gizlilik', 'mobil'],
        'Kimlik istemeyen eSIM veri hattı; kripto ile ödenebilmesi ve isim istememesi ayırt edici yanı.',
        'An eSIM data plan requiring no identity; paying with crypto and giving no name is what sets it apart.', G)
    add('https://5sim.net/', '5SIM', ['ücretli', 'gizlilik'],
        'SMS doğrulaması için geçici numara servisi; kişisel numaranı vermeden hesap açmak için kullanılıyor.',
        'Temporary number service for SMS verification, used to sign up without giving out your own number.', G)
    add('https://privacy.com/', 'Privacy.com', ['freemium', 'gizlilik', 'ödeme'],
        'Tek kullanımlık sanal kart üreten servis; abonelik iptallerini kart tarafında kesebilmesi pratik avantajı.',
        'Generates single-use virtual cards; being able to kill a subscription at the card level is its practical advantage.', G)
    add('https://guvenlik.oyd.org.tr/', 'Özgür Yazılım Güvenlik Rehberi', ['ücretsiz', 'türkçe', 'gizlilik'],
        'Dijital güvenlik ve mahremiyetin Türkçe rehberi; ürün tanıtımı değil, tehdit modeline göre yöntem anlatması ayırt edici.',
        'A Turkish guide to digital security and privacy, distinguished by teaching method by threat model rather than promoting products.', G)
    add('https://guvenlik.oyd.org.tr/yazisma_guvenligi/mailvelope.html', 'Mailvelope ile E-posta Şifreleme', ['ücretsiz', 'türkçe', 'rehber'],
        'Tarayıcıdan PGP ile e-posta şifrelemenin Türkçe adım adım anlatımı; kavramı en somut hâliyle gösteriyor.',
        'A step-by-step Turkish walkthrough of PGP email encryption in the browser — the concept at its most concrete.', G)
    # şifreleme & bulmaca
    add('https://en.wikipedia.org/wiki/List_of_ciphertexts', 'Çözülmemiş Şifreli Metinler', ['ücretsiz', 'referans', 'kriptografi'],
        'Tarihte çözülmüş ve çözülmemiş şifreli metinlerin listesi; kriptanaliz pratiği için gerçek malzeme.',
        'A list of solved and unsolved historical ciphertexts — real material for cryptanalysis practice.', G)
    add('https://en.wikipedia.org/wiki/Category:Undeciphered_historical_codes_and_ciphers', 'Çözülmemiş Tarihî Şifreler', ['ücretsiz', 'referans'],
        'Hâlâ çözülememiş tarihî şifrelerin kategorisi; her biri açık bir problem olarak duruyor.',
        'The category of still-unbroken historical ciphers, each standing as an open problem.', G)
    add('https://blog.wolfram.com/2021/03/24/the-solution-of-the-zodiac-killers-340-character-cipher/', 'Zodiac 340 Şifresinin Çözümü', ['ücretsiz', 'kriptografi', 'vaka'],
        'Elli yıl çözülemeyen şifrenin nasıl kırıldığının teknik anlatımı; kriptanaliz sürecinin gerçek bir örneği.',
        'A technical account of how a cipher unsolved for fifty years was broken — a real worked example of cryptanalysis.', G)
    add('https://www.boxentriq.com/guides/cicada-3301-first-puzzle-walkthrough', 'Cicada 3301 Çözüm Rehberi', ['ücretsiz', 'kriptografi', 'bulmaca'],
        'Ünlü internet bulmacasının adım adım çözümü; steganografi ve klasik şifrelerin bir arada kullanımına örnek.',
        'A step-by-step solution of the famous internet puzzle — an example of steganography and classical ciphers combined.', G)

    # ============================================================ KUANTUM BİLİŞİM
    K = 'kuantum'
    add('https://quantum.cloud.ibm.com/docs/en/guides', 'IBM Quantum', ['ücretsiz', 'dokümantasyon'],
        'Gerçek kuantum donanımına erişim veren platformun rehberleri; simülatörle sınırlı kalmayıp fiziksel cihazda çalıştırabilmesi ayırt edici.',
        'Guides for a platform giving access to real quantum hardware — running on a physical device, not just a simulator, is its distinction.', K)
    add('https://quantum.microsoft.com/en-us/vision/quantum-roadmap', 'Microsoft Kuantum Yol Haritası', ['ücretsiz', 'referans'],
        'Kuantum hesaplamanın aşamalarını ve beklenen zaman çizelgesini anlatan yol haritası; alanın nerede olduğunu tartmak için.',
        'A roadmap of quantum computing’s stages and expected timeline — useful for gauging where the field actually is.', K)
    add('https://quantum.microsoft.com/en-us/insights/blogs/qsharp/why-do-we-need-q', 'Neden Q#?', ['ücretsiz', 'makale'],
        'Kuantum için ayrı bir programlama diline neden ihtiyaç duyulduğunu anlatan yazı; dile başlamadan önce gerekçeyi verir.',
        'An article on why quantum needs its own programming language — the rationale before you start the language.', K)
    add('https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk', 'Q# Geliştirme Kiti Kurulumu', ['dokümantasyon', 'kurulum'],
        'Q# ve kuantum geliştirme kitinin kurulum rehberi; yerel simülatörle başlamanın en kısa yolu.',
        'Setup guide for Q# and the Quantum Development Kit — the shortest path to starting with a local simulator.', K)
    add('https://github.com/microsoft/qdk', 'Microsoft QDK', ['açık kaynak', 'github', 'kuantum'],
        'Q# dili ve kuantum geliştirme kitinin kaynak kodu; derleyici ve simülatörün nasıl çalıştığını görmek için.',
        'Source for the Q# language and Quantum Development Kit, for seeing how the compiler and simulator work.', K)
    add('https://azure.microsoft.com/tr-tr/resources/training-and-certifications/quantum-computing', 'Kuantum Öğrenme Kaynakları', ['ücretsiz', 'türkçe', 'kurs'],
        'Kuantum hesaplama eğitim kaynaklarının Türkçe derlemesi; alana giriş için sıralı bir başlangıç noktası.',
        'A Turkish compilation of quantum computing learning resources — an ordered entry point into the field.', K)
    add('https://stationq.github.io/Liquid/getting-started/', 'LIQUi|>', ['ücretsiz', 'araştırma'],
        'Microsoft’un erken dönem kuantum simülasyon platformu; artık tarihî değeri olan bir kaynak, güncel iş için Q# tercih edilmeli.',
        'Microsoft’s early quantum simulation platform — now of historical interest; use Q# for current work.', K)
    add('https://www.tensorflow.org/quantum', 'TensorFlow Quantum', ['açık kaynak', 'ml'],
        'Kuantum devrelerini makine öğrenmesi modellerine gömen kütüphane; hibrit klasik-kuantum modeller için.',
        'Library embedding quantum circuits into machine learning models, for hybrid classical-quantum architectures.', K)

    # ============================================================ REFERANS & KOLEKSİYONLAR
    R = 'referans'
    add('https://devdocs.io/', 'DevDocs', ['ücretsiz', 'açık kaynak', 'dokümantasyon'],
        'Onlarca teknolojinin dokümantasyonunu tek arayüzde toplayan araç; çevrimdışı çalışabilmesi ve tek tuşla arama sunması ayırt edici.',
        'Gathers documentation for dozens of technologies in one interface; offline support and single-key search are what set it apart.', R)
    add('https://quickref.me/index.html', 'QuickRef', ['ücretsiz', 'kopya kâğıdı'],
        'Dil ve araçlar için tek sayfalık hızlı başvuru kâğıtları; tam dokümantasyona karşı sık kullanılanı öne çıkarır.',
        'One-page cheat sheets for languages and tools, surfacing the common cases instead of full documentation.', R)
    add('https://learnxinyminutes.com/', 'Learn X in Y Minutes', ['ücretsiz', 'kopya kâğıdı'],
        'Bir dili tek yorumlu kod dosyasıyla tanıtan derleme; başka dil bilenler için en hızlı geçiş yolu.',
        'Introduces a language through a single annotated code file — the fastest crossover route if you already know another language.', R)
    add('https://www.w3schools.com/', 'W3Schools', ['ücretsiz', 'referans', 'başlangıç'],
        'Web teknolojilerinin denenebilir örnekli referansı; MDN kadar kesin değil ama örnekleri tarayıcıda çalıştırabilmesiyle başlangıçta daha erişilebilir.',
        'A reference with runnable examples for web technologies — less rigorous than MDN, but more approachable for beginners.', R)
    add('https://www.w3schools.com/c/ref_math_sqrt.php', 'W3Schools C Referansı', ['ücretsiz', 'c', 'referans'],
        'C standart kütüphane fonksiyonlarının örnekli referansı; hızlı kullanım örneği aradığında kılavuzdan pratik.',
        'An example-driven reference for C standard library functions — handier than the manual for a quick usage example.', R)
    add('https://natureofcode.com/', 'The Nature of Code', ['ücretsiz', 'kitap', 'simülasyon'],
        'Doğal sistemleri kodla simüle etmeyi anlatan ücretsiz kitap; matematiği görsel ve etkileşimli örneklerle vermesi ayırt edici.',
        'A free book on simulating natural systems in code, distinguished by delivering the maths through visual, interactive examples.', R)
    add('https://free-for.dev/#/', 'Free for Developers', ['ücretsiz', 'koleksiyon'],
        'Geliştiriciler için ücretsiz katman sunan servislerin listesi; yan proje kurarken maliyeti sıfıra yakın tutmak için.',
        'A list of services with free tiers for developers — for keeping a side project’s cost near zero.', R)
    add('https://github.com/ripienaar/free-for-dev', 'free-for-dev (kaynak)', ['ücretsiz', 'github', 'koleksiyon'],
        'Free for Developers listesinin kaynak deposu; katkı yapmak veya değişiklik geçmişini görmek için.',
        'The source repository behind the Free for Developers list, for contributing or reading its change history.', R)
    add('https://github.com/sdmg15/Best-websites-a-programmer-should-visit', 'Programcının Ziyaret Etmesi Gereken Siteler', ['ücretsiz', 'github', 'koleksiyon'],
        'Geliştiriciler için genel amaçlı bağlantı derlemesi; konuya değil kullanıma göre gruplanması ayırt edici.',
        'A general-purpose link collection for developers, grouped by use rather than by topic.', R)
    add('https://github.com/exercism/problem-specifications', 'Exercism Problem Şartnameleri', ['açık kaynak', 'github', 'alıştırma'],
        'Exercism alıştırmalarının dilden bağımsız tanımları; kendi alıştırma setini kurmak isteyenler için hazır malzeme.',
        'Language-independent definitions of Exercism’s exercises — ready material if you want to build your own practice set.', R)
    add('https://github.com/abhigyanpatwari/GitNexus', 'GitNexus', ['açık kaynak', 'github', 'araç'],
        'Depo içeriğini gezilebilir hâle getiren araç; büyük kod tabanına ilk kez bakarken yön bulmayı kolaylaştırıyor.',
        'Makes repository content navigable, easing orientation when you first face a large codebase.', R)
    add('https://education.github.com/pack', 'GitHub Student Pack', ['ücretsiz', 'öğrenci'],
        'Öğrencilere ücretsiz geliştirici araç ve kredileri veren paket; tek tek başvurmaya karşı toplu erişim sağlıyor.',
        'A bundle of free developer tools and credits for students — bulk access instead of applying to each separately.', R)
    add('https://en.wikipedia.org/wiki/Portal:Computer_programming', 'Programlama Portalı (Vikipedi)', ['ücretsiz', 'referans'],
        'Programlama konularının Vikipedi giriş kapısı; kavram haritası çıkarmak için tarafsız bir başlangıç.',
        'Wikipedia’s entry point for programming topics — a neutral start for mapping concepts.', R)
    add('https://tr.wikipedia.org/wiki/DjVu', 'DjVu', ['ücretsiz', 'türkçe', 'format'],
        'Taranmış belgeler için PDF alternatifi biçimin tanıtımı; arşiv dosyalarıyla uğraşırken formatın ne olduğunu açıklar.',
        'An introduction to the scanned-document format that competes with PDF — useful when you meet one in an archive.', R)
    add('https://shipx.substack.com/', 'ShipX', ['ücretsiz', 'bülten'],
        'Teknoloji ve ürün üzerine bülten; günlük haber akışına karşı seçilmiş ve yorumlanmış içerik sunar.',
        'A newsletter on technology and product — curated and interpreted content against the daily news feed.', R)
    add('https://engineering.teknasyon.com/androidler-neden-elektrikli-koyun-d%C3%BC%C5%9Fleyemez-dab0ee1e85be', 'Androidler Neden Elektrikli Koyun Düşleyemez', ['ücretsiz', 'türkçe', 'makale'],
        'Türkçe mühendislik blogundan teknik bir yazı; yerel dilde derinlikli teknik içeriğin az bulunduğu bir alanda örnek.',
        'A technical piece from a Turkish engineering blog — an example in an area short of in-depth local-language content.', R)
    add('https://www.btkakademi.gov.tr/portal/public/terimlersozlugu', 'BTK Terimler Sözlüğü', ['ücretsiz', 'türkçe', 'sözlük'],
        'Bilişim terimlerinin resmî Türkçe karşılıkları; belge ve sunum yazarken terim tutarlılığı için.',
        'Official Turkish equivalents for computing terms — for keeping terminology consistent in documents and talks.', R)
    add('https://github.com/LuNiZz?tab=repositories', 'LuNiZz Depoları', ['ücretsiz', 'github', 'türkçe'],
        'Türkçe güvenlik ve bilişim içerikleri üreten bir geliştiricinin depoları; yerel kaynak arayanlar için toplu giriş.',
        'The repositories of a developer producing Turkish security and IT content — a single entry point for local resources.', R)
