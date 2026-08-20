# -*- coding: utf-8 -*-
"""Güvenlik & Gizlilik · Kuantum Bilişim · Referans & Koleksiyonlar"""


def load(add):
    # ============================================================ GÜVENLİK & GİZLİLİK
    G = 'guvenlik'
    add('https://tryhackme.com/', 'TryHackMe', ['freemium', 'lab', 'sızma-testi'],
        'Rehberli laboratuvarlar; her odada hangi aracı neden kullandığın anlatılıyor. '
        'Hack The Box’a göre elinden tutuyor, o yüzden ilk sızma testi deneyimi için daha uygun.',
        'Guided labs that explain which tool you are using and why in each room. It holds your hand more than '
        'Hack The Box, which makes it the better first exposure to penetration testing.', G)
    add('https://www.hackthebox.com/', 'Hack The Box', ['freemium', 'lab', 'sızma-testi'],
        'Gerçekçi makineler; ipucu vermiyor, keşif ve araştırma yükü tamamen sende. '
        'OSCP hazırlığında sık kullanılmasının sebebi bu zorluk seviyesi.',
        'Realistic machines with no hints — reconnaissance and research are entirely on you. '
        'That difficulty is why it turns up so often in OSCP preparation.', G)
    add('https://overthewire.org/wargames/', 'OverTheWire Wargames', ['ücretsiz', 'ctf', 'linux'],
        'SSH ile bağlanıp seviye seviye ilerlediğin klasik savaş oyunları. '
        'Bandit serisi Linux komut satırını öğretmenin en sert ama en kalıcı yolu.',
        'Classic wargames you play by SSH, advancing level by level. The Bandit series is the harshest and '
        'most durable way to learn the Linux command line.', G)
    add('https://cyberexam.io/', 'CyberExam', ['freemium', 'lab', 'sertifika'],
        'Güvenlik sertifikalarına yönelik uygulamalı laboratuvar ve deneme sınavları. '
        'Soru bankası ezberlemeye karşı, aracı gerçekten çalıştırarak hazırlanma yolu.',
        'Hands-on labs and mock exams for security certifications — preparation by actually running the tools '
        'rather than memorising a question bank.', G)
    add('https://www.hackerone.com/', 'HackerOne', ['ücretsiz', 'ödül-programı', 'sızma-testi'],
        'Hata ödül platformu; şirketlerin kapsam tanımladığı gerçek sistemlerde yasal olarak test yapıyorsun. '
        'Yayımlanan raporlar (hacktivity) laboratuvarlardan daha öğretici bir arşiv.',
        'A bug bounty platform where you legally test real systems within a company-defined scope. '
        'The published reports (hacktivity) form an archive more instructive than any lab.', G)
    add('https://siberguvenlik.gov.tr/', 'Siber Güvenlik Başkanlığı', ['ücretsiz', 'türkçe', 'resmî'],
        'Türkiye’nin siber güvenlik otoritesi; ulusal uyarılar, mevzuat ve kritik altyapı '
        'rehberleri buradan yayımlanıyor.',
        'Turkey’s cyber security authority, publishing national advisories, regulation and critical-infrastructure guidance.', G)
    add('https://github.com/farhanashrafdev/90DaysOfCyberSecurity', '90 Days of Cyber Security', ['github', 'müfredat', 'ücretsiz'],
        'Doksan güne bölünmüş çalışma planı: ağ temelleri, Linux, Python, ardından saldırı ve savunma. '
        'Dağınık kaynak listelerine karşı takvimli bir program.',
        'A study plan split across ninety days — networking, Linux, Python, then offence and defence. '
        'A dated schedule against the usual scattered resource list.', G)
    add('https://github.com/LuNiZz/siber-guvenlik-sss', 'Siber Güvenlik SSS', ['github', 'türkçe', 'kariyer'],
        'Türkçe siber güvenlik sıkça sorulan sorular derlemesi; teknik konular kadar '
        '“nereden başlanır, hangi sertifika” gibi kariyer sorularını da kapsıyor.',
        'A Turkish cyber security FAQ covering career questions — where to start, which certification — '
        'as much as technical ones.', G)
    add('https://www.cybernotes.tech/', 'CyberNotes', ['ücretsiz', 'not', 'referans'],
        'Güvenlik konularının derli toplu not arşivi; laboratuvar sırasında komut ve yöntem '
        'hatırlamak için hızlı başvuru.',
        'A tidy note archive of security topics, for recalling a command or method mid-lab.', G)
    add('https://osintframework.com/', 'OSINT Framework', ['ücretsiz', 'osint', 'dizin'],
        'Açık kaynak istihbarat araçlarını ağaç yapısında topluyor: e-posta, kullanıcı adı, alan adı, '
        'görüntü. Ne aradığından başlayıp araca iniyorsun, ters yönde değil.',
        'A tree of open-source intelligence tools organised by target — email, username, domain, image. '
        'You start from what you are looking for and descend to the tool, not the other way round.', G)
    add('https://start.me/p/DPYPMz/the-ultimate-osint-collection', 'The Ultimate OSINT Collection', ['ücretsiz', 'osint', 'koleksiyon'],
        'Kategorilere ayrılmış geniş OSINT bağlantı panosu; framework’e göre daha sık güncelleniyor, '
        'ölü araç oranı düşük.',
        'A broad categorised OSINT link board, updated more frequently than the framework so fewer of its tools are dead.', G)
    add('https://github.com/apurvsinghgautam/robin', 'Robin', ['açık-kaynak', 'github', 'osint', 'llm'],
        'Karanlık ağ araştırmasında sorguyu genişletip sonuçları özetleyen yapay zeka destekli araç. '
        'Elle arama yapmanın zaman aldığı bir alanda tarama adımını otomatikleştiriyor.',
        'An AI-assisted tool that expands queries and summarises results in dark web research, '
        'automating the sweep in an area where manual searching is slow.', G)
    add('https://github.com/redhuntlabs/Awesome-Asset-Discovery', 'Awesome Asset Discovery', ['github', 'awesome-liste', 'keşif'],
        'Varlık keşfi araç ve yöntemleri listesi: alt alan adı numaralandırma, sertifika şeffaflığı, '
        'ASN sorgulama. Sızma testinin ilk ve en belirleyici aşaması.',
        'A list of asset discovery tools and methods — subdomain enumeration, certificate transparency, ASN lookups. '
        'The first and most decisive phase of a penetration test.', G)
    add('https://github.com/jivoi/awesome-ml-for-cybersecurity', 'Awesome ML for Cybersecurity', ['github', 'awesome-liste', 'ml'],
        'Güvenlikte makine öğrenmesi kaynakları; veri kümeleri ve akademik makaleleri bir arada veriyor. '
        'Bu alanda en zor bulunan şey etiketli veri, listede o kısım güçlü.',
        'Machine learning resources for security, gathering datasets and academic papers together. '
        'Labelled data is the hardest thing to find in this field, and that part of the list is strong.', G)
    add('https://github.com/wtsxDev/Machine-Learning-for-Cyber-Security', 'ML for Cyber Security', ['github', 'awesome-liste', 'ml'],
        'Aynı alanda ikinci bir derleme; araç, kurs ve konuşma tarafı daha ağır basıyor.',
        'A second compilation in the same field, weighted more towards tools, courses and conference talks.', G)
    add('https://github.com/WKL-Sec/Illicit-Services-Enum-Script', 'Illicit Services Enum', ['açık-kaynak', 'github', 'keşif'],
        'Servis numaralandırma betiği; keşif aşamasında elle çalıştırılan komut dizisini otomatikleştiriyor.',
        'A service enumeration script automating the command sequence you would otherwise run by hand during reconnaissance.', G)
    add('https://github.com/lauriewired/ghidramcp', 'GhidraMCP', ['açık-kaynak', 'github', 'mcp', 'tersine-mühendislik'],
        'Ghidra’yı MCP üzerinden bir asistana açıyor; sökülmüş kodu okuma ve fonksiyon adlandırma '
        'gibi yorucu adımları devredebiliyorsun. İkili çözümlemede yeni bir iş akışı.',
        'Exposes Ghidra to an assistant over MCP, letting you delegate the tedious parts — reading disassembly, '
        'naming functions. A genuinely new workflow in binary analysis.', G)
    add('https://www.youtube.com/watch?v=iCbOV8p6tD4', 'Siber Güvenlik Anlatımı', ['video', 'ücretsiz', 'giriş'],
        'Güvenlik kavramlarına video giriş; alanın hangi dallara ayrıldığını görmek için.',
        'A video introduction to security concepts, useful for seeing how the field branches.', G)
    add('https://www.youtube.com/watch?v=p3vaaD9pn9I', 'Uygulamalı Güvenlik', ['video', 'ücretsiz'],
        'Bir tekniği çalışırken gösteren uygulamalı anlatım; teorik dersin ardından izlenmeli.',
        'A hands-on walkthrough showing a technique in operation — best watched after the theory.', G)
    add('https://www.turkhackteam.org/konular/access-point-ve-monitor-mod-destekli-wifi-kartini-nereden-bulabilirim.2051107/', 'Monitör Mod Wi-Fi Kartı', ['türkçe', 'donanım', 'kablosuz'],
        'Monitör modu ve paket enjeksiyonu destekleyen Wi-Fi yonga setleri üzerine Türkçe tartışma. '
        'Kablosuz güvenlik testine başlamadan çözülmesi gereken donanım sorusu bu.',
        'A Turkish discussion of Wi-Fi chipsets supporting monitor mode and packet injection — '
        'the hardware question that has to be settled before any wireless testing.', G)
    # gizlilik
    add('https://bitwarden.com/', 'Bitwarden', ['açık-kaynak', 'freemium', 'gizlilik', 'self-hosted'],
        'Kaynak kodu açık ve bağımsız denetimden geçmiş parola yöneticisi. '
        'Ücretsiz katmanda sınırsız parola var; istersen Vaultwarden ile kendi sunucunda çalıştırılıyor.',
        'A password manager with open source and independent audits behind it. The free tier holds unlimited '
        'passwords, and Vaultwarden lets you self-host the whole thing.', G)
    add('https://privnote.com/', 'Privnote', ['ücretsiz', 'gizlilik'],
        'Okunduktan sonra kendini silen not; hesap gerektirmiyor. '
        'Tek seferlik bir parolayı sohbet geçmişinde bırakmadan iletmek için pratik.',
        'A note that destroys itself after reading, with no account required — practical for handing over '
        'a one-time password without leaving it in a chat log.', G)
    add('https://silent.link/#generic_price_table', 'Silent Link', ['ücretli', 'gizlilik', 'esim'],
        'Kimlik istemeyen eSIM veri hattı; kripto ile ödeniyor, isim ya da belge sorulmuyor. '
        'Seyahatte telefon numarasını kimliğine bağlamadan veri almanın yolu.',
        'An eSIM data plan requiring no identity — paid in crypto, no name or document. '
        'A way to get data abroad without tying a number to your identity.', G)
    add('https://5sim.net/', '5SIM', ['ücretli', 'gizlilik', 'sms'],
        'SMS doğrulaması için geçici numara kiralama. Kendi numaranı vermeden hesap açmayı sağlıyor; '
        'kalıcı hesaplarda kurtarma sorunu doğurabileceği için dikkatli kullanılmalı.',
        'Rents temporary numbers for SMS verification so you can sign up without your own. '
        'Use carefully on accounts you intend to keep — recovery becomes a problem.', G)
    add('https://privacy.com/', 'Privacy.com', ['freemium', 'gizlilik', 'ödeme'],
        'Tek kullanımlık ve harcama limitli sanal kart üretiyor. '
        'Aboneliği iptal edemediğinde kartı kapatmak, satıcıyla uğraşmaktan hızlı bir çıkış. Yalnızca ABD.',
        'Issues single-use virtual cards with spend limits. Killing the card is a faster exit than arguing with '
        'a merchant you cannot unsubscribe from. US only.', G)
    add('https://guvenlik.oyd.org.tr/', 'Özgür Yazılım Güvenlik Rehberi', ['ücretsiz', 'türkçe', 'gizlilik'],
        'Dijital güvenliğin Türkçe rehberi; ürün tanıtmıyor, tehdit modeline göre yöntem anlatıyor. '
        '“Kimden korunuyorsun” sorusuyla başlaması onu araç listelerinden ayırıyor.',
        'A Turkish guide to digital security that recommends method by threat model rather than promoting products. '
        'Starting from “who are you protecting against” is what separates it from tool lists.', G)
    add('https://guvenlik.oyd.org.tr/yazisma_guvenligi/mailvelope.html', 'Mailvelope ile E-posta Şifreleme', ['ücretsiz', 'türkçe', 'pgp'],
        'Tarayıcı eklentisiyle PGP kullanmayı adım adım anlatan Türkçe rehber. '
        'Anahtar üretme ve paylaşma kısmı, kavramın en somut hâliyle görüldüğü yer.',
        'A step-by-step Turkish walkthrough of using PGP through a browser extension. '
        'The key generation and exchange section is where the concept becomes concrete.', G)
    # şifreleme & bulmaca
    add('https://en.wikipedia.org/wiki/List_of_ciphertexts', 'Çözülmemiş Şifreli Metinler', ['ücretsiz', 'kriptografi', 'referans'],
        'Tarihte çözülmüş ve çözülememiş şifreli metinlerin listesi. '
        'Kriptanaliz pratiği için sentetik alıştırma yerine gerçek malzeme.',
        'A list of solved and unsolved historical ciphertexts — real material for cryptanalysis practice '
        'instead of synthetic exercises.', G)
    add('https://en.wikipedia.org/wiki/Category:Undeciphered_historical_codes_and_ciphers', 'Çözülmemiş Tarihî Şifreler', ['ücretsiz', 'kriptografi'],
        'Hâlâ kırılamamış şifrelerin kategorisi; Voynich el yazması ve Beale şifreleri dahil. '
        'Her biri açık bir problem olarak duruyor.',
        'The category of ciphers still unbroken, the Voynich manuscript and Beale ciphers among them. '
        'Each stands as an open problem.', G)
    add('https://blog.wolfram.com/2021/03/24/the-solution-of-the-zodiac-killers-340-character-cipher/', 'Zodiac 340 Şifresinin Çözümü', ['ücretsiz', 'kriptografi', 'vaka'],
        'Elli bir yıl çözülemeyen homofonik yerine koyma şifresinin nasıl kırıldığının teknik anlatımı. '
        'Hipotez kurma ve eleme sürecinin gerçek bir örneği.',
        'A technical account of how a homophonic substitution cipher unsolved for fifty-one years was broken — '
        'a real worked example of hypothesis and elimination.', G)
    add('https://www.boxentriq.com/guides/cicada-3301-first-puzzle-walkthrough', 'Cicada 3301 Çözüm Rehberi', ['ücretsiz', 'kriptografi', 'steganografi'],
        'İnternetin en bilinen bulmacasının adım adım çözümü; steganografi, kitap şifresi ve '
        'Tor gizli servisleri bir arada kullanılıyor. Tekniklerin nasıl zincirlendiğine iyi bir örnek.',
        'A step-by-step solution of the internet’s best-known puzzle, chaining steganography, book ciphers and '
        'Tor hidden services — a good example of how techniques link together.', G)

    # ============================================================ KUANTUM BİLİŞİM
    K = 'kuantum'
    add('https://quantum.cloud.ibm.com/docs/en/guides', 'IBM Quantum', ['ücretsiz', 'dokümantasyon', 'donanım'],
        'Gerçek kuantum işlemcilerine kuyrukla erişim veriyor; Qiskit ile devre yazıp gönderiyorsun. '
        'Simülatörde görünmeyen gürültü ve hata oranlarını ancak burada karşılaşıyorsun.',
        'Queued access to real quantum processors, with circuits written and submitted through Qiskit. '
        'The noise and error rates a simulator hides only show up here.', K)
    add('https://quantum.microsoft.com/en-us/vision/quantum-roadmap', 'Microsoft Kuantum Yol Haritası', ['ücretsiz', 'referans'],
        'Gürültülü ara ölçek (NISQ) aşamasından hata düzeltmeli mantıksal kübitlere uzanan aşamalar. '
        'Alanın hangi vaatlerinin bugün, hangilerinin on yıl sonrası olduğunu tartmak için.',
        'The stages from noisy intermediate-scale (NISQ) to error-corrected logical qubits — '
        'useful for weighing which of the field’s promises are now and which are a decade out.', K)
    add('https://quantum.microsoft.com/en-us/insights/blogs/qsharp/why-do-we-need-q', 'Neden Q#?', ['ücretsiz', 'makale'],
        'Kuantum için neden ayrı bir dile ihtiyaç duyulduğunu anlatıyor: klonlanamama, ölçümün '
        'durumu bozması gibi kısıtlar klasik dil kalıplarına oturmuyor.',
        'Explains why quantum needs its own language — no-cloning and measurement collapsing state do not fit '
        'classical language idioms.', K)
    add('https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk', 'Q# Geliştirme Kiti Kurulumu', ['dokümantasyon', 'kurulum'],
        'Q# ve QDK kurulumu; VS Code uzantısıyla yerel simülatörde devre çalıştırmanın en kısa yolu. '
        'Donanıma erişim gerekmeden başlanabiliyor.',
        'Installing Q# and the QDK, with the VS Code extension as the shortest path to running circuits on a local '
        'simulator — no hardware access needed to start.', K)
    add('https://github.com/microsoft/qdk', 'Microsoft QDK', ['açık-kaynak', 'github', 'derleyici'],
        'Q# derleyicisi ve simülatörünün kaynak kodu. Kuantum devresinin nasıl derlenip '
        'simüle edildiğini görmek isteyenler için.',
        'Source for the Q# compiler and simulator — for anyone who wants to see how a quantum circuit is compiled '
        'and simulated.', K)
    add('https://azure.microsoft.com/tr-tr/resources/training-and-certifications/quantum-computing', 'Kuantum Öğrenme Kaynakları', ['ücretsiz', 'türkçe', 'kurs'],
        'Kuantum hesaplama eğitim kaynaklarının Türkçe derlemesi; alana sıralı bir giriş noktası.',
        'A Turkish compilation of quantum computing learning resources — an ordered way into the field.', K)
    add('https://stationq.github.io/Liquid/getting-started/', 'LIQUi|>', ['araştırma', 'arşiv'],
        'Microsoft’un erken dönem kuantum simülasyon platformu. Bugün yerini Q# aldı; '
        'alanın araç zincirinin nasıl geliştiğini görmek dışında pratik değeri kalmadı.',
        'Microsoft’s early quantum simulation platform, since superseded by Q#. Little practical value now beyond '
        'seeing how the field’s toolchain evolved.', K)
    add('https://www.tensorflow.org/quantum', 'TensorFlow Quantum', ['açık-kaynak', 'python', 'ml'],
        'Parametreli kuantum devrelerini Keras katmanı gibi kullanıp klasik ağlarla birleştiriyor. '
        'Hibrit klasik-kuantum modellerin deneysel olarak araştırıldığı yer.',
        'Wraps parameterised quantum circuits as Keras-style layers to combine with classical networks — '
        'where hybrid classical-quantum models get explored experimentally.', K)

    # ============================================================ REFERANS & KOLEKSİYONLAR
    R = 'referans'
    add('https://devdocs.io/', 'DevDocs', ['açık-kaynak', 'dokümantasyon', 'çevrimdışı'],
        'Yüzlerce teknolojinin resmî dokümanını tek arayüzde topluyor; çevrimdışı indirilebiliyor ve '
        'anlık arama sunuyor. Sekme sekme doküman sitesi gezmenin sonu.',
        'Gathers official documentation for hundreds of technologies in one interface, downloadable for offline use '
        'with instant search. The end of tab-hopping between doc sites.', R)
    add('https://quickref.me/index.html', 'QuickRef', ['ücretsiz', 'kopya-kâğıdı'],
        'Dil ve araçlar için tek sayfalık başvuru kâğıtları; sık kullanılanı öne alıyor. '
        'Tam dokümantasyon aramanın hantal kaldığı durumlar için.',
        'One-page cheat sheets for languages and tools, surfacing the common cases — '
        'for when reaching into full documentation is too slow.', R)
    add('https://learnxinyminutes.com/', 'Learn X in Y Minutes', ['ücretsiz', 'kopya-kâğıdı'],
        'Bir dili tek yorumlu kod dosyasıyla tanıtıyor. Başka dil bilenler için en hızlı geçiş yolu: '
        'kavramları değil yalnızca sözdizimi farklarını okuyorsun.',
        'Introduces a language through a single annotated file. The fastest crossover if you already know another '
        'language — you read only the syntax differences, not the concepts.', R)
    add('https://www.w3schools.com/', 'W3Schools', ['ücretsiz', 'referans', 'başlangıç'],
        'Denenebilir örnekli web referansı. MDN kadar kesin değil ve zaman zaman güncelliğini yitiriyor, '
        'ama “Try it” düzenleyicisi başlangıçta gerçek bir avantaj.',
        'A web reference with runnable examples. Less rigorous than MDN and occasionally out of date, '
        'though the “Try it” editor is a genuine advantage early on.', R)
    add('https://www.w3schools.com/c/ref_math_sqrt.php', 'W3Schools C Referansı', ['ücretsiz', 'c', 'referans'],
        'C standart kütüphane fonksiyonlarının kısa ve örnekli referansı; '
        'hızlı kullanım örneği aradığında man sayfasından pratik.',
        'A short, example-driven reference for C standard library functions — handier than a man page '
        'when you just want a usage example.', R)
    add('https://natureofcode.com/', 'The Nature of Code', ['ücretsiz', 'kitap', 'simülasyon'],
        'Doğal sistemleri (kuvvet, parçacık, sürü davranışı, hücresel otomat) kodla simüle etmeyi anlatan '
        'ücretsiz kitap. Matematiği etkileşimli örneklerle veriyor, formül yığını değil.',
        'A free book on simulating natural systems in code — forces, particles, flocking, cellular automata — '
        'delivering the maths through interactive examples rather than a pile of formulas.', R)
    add('https://free-for.dev/#/', 'Free for Developers', ['ücretsiz', 'awesome-liste'],
        'Ücretsiz katmanı olan geliştirici servislerinin listesi: barındırma, CI, izleme, e-posta. '
        'Yan projenin maliyetini sıfıra yakın tutmanın haritası.',
        'A list of developer services with free tiers — hosting, CI, monitoring, email. '
        'A map for keeping a side project near zero cost.', R)
    add('https://github.com/ripienaar/free-for-dev', 'free-for-dev (kaynak)', ['github', 'awesome-liste'],
        'Free for Developers listesinin kaynak deposu; katkı göndermek ya da bir servisin '
        'ne zaman eklendiğine bakmak için.',
        'The source repository behind the Free for Developers list — for contributing or checking when a service '
        'was added.', R)
    add('https://github.com/sdmg15/Best-websites-a-programmer-should-visit', 'Programcının Ziyaret Etmesi Gereken Siteler', ['github', 'awesome-liste'],
        'Kullanım amacına göre gruplanmış geliştirici bağlantı derlemesi: alıştırma, haber, '
        'araç, kitap. Konu bazlı listelerden farklı bir kesit veriyor.',
        'A developer link collection grouped by purpose — practice, news, tools, books — '
        'which cuts the space differently from topic-based lists.', R)
    add('https://github.com/exercism/problem-specifications', 'Exercism Problem Şartnameleri', ['açık-kaynak', 'github', 'alıştırma'],
        'Exercism alıştırmalarının dilden bağımsız tanımları ve test verileri. '
        'Kendi dilinde alıştırma seti kurmak isteyenler için hazır malzeme.',
        'Language-independent definitions and test data for Exercism’s exercises — ready material if you want to '
        'build a practice set in your own language.', R)
    add('https://github.com/abhigyanpatwari/GitNexus', 'GitNexus', ['açık-kaynak', 'github', 'araç'],
        'Depo içeriğini gezilebilir hâle getiriyor; büyük bir kod tabanına ilk kez bakarken '
        'nereden başlanacağını göstermesi işe yarıyor.',
        'Makes repository content navigable, which helps when you face a large codebase for the first time '
        'and need somewhere to start.', R)
    add('https://education.github.com/pack', 'GitHub Student Pack', ['ücretsiz', 'öğrenci'],
        'Öğrencilere ücretsiz araç ve bulut kredisi veren paket: alan adı, JetBrains lisansı, '
        'DigitalOcean kredisi ve fazlası. Doğrulama okul e-postasıyla yapılıyor.',
        'A bundle of free tools and cloud credit for students — a domain, JetBrains licences, DigitalOcean credit '
        'and more, verified with a school email.', R)
    add('https://en.wikipedia.org/wiki/Portal:Computer_programming', 'Programlama Portalı', ['ücretsiz', 'referans'],
        'Programlama konularının Vikipedi giriş kapısı; kavram haritası çıkarmak için '
        'satıcı etkisinden uzak bir başlangıç.',
        'Wikipedia’s entry point for programming topics — a vendor-neutral start for mapping the concept space.', R)
    add('https://tr.wikipedia.org/wiki/DjVu', 'DjVu', ['ücretsiz', 'türkçe', 'format'],
        'Taranmış belgeler için PDF’e alternatif biçim; aynı kalitede çok daha küçük dosya üretiyor. '
        'Eski arşivlerde sık karşına çıkar, ne olduğunu bilmek gerekir.',
        'A PDF alternative for scanned documents producing much smaller files at the same quality. '
        'You meet it often in older archives, so it is worth knowing what it is.', R)
    add('https://shipx.substack.com/', 'ShipX', ['ücretsiz', 'bülten'],
        'Teknoloji ve ürün üzerine bülten; günlük haber akışına karşı seçilmiş ve yorumlanmış içerik.',
        'A newsletter on technology and product — curated, interpreted content against the daily feed.', R)
    add('https://engineering.teknasyon.com/androidler-neden-elektrikli-koyun-d%C3%BC%C5%9Fleyemez-dab0ee1e85be', 'Androidler Neden Elektrikli Koyun Düşleyemez', ['ücretsiz', 'türkçe', 'makale'],
        'Türkçe mühendislik blogundan teknik bir yazı. Yerel dilde derinlikli teknik içerik '
        'az bulunduğu için örnek olarak değerli.',
        'A technical piece from a Turkish engineering blog — valuable as an example, since in-depth technical '
        'writing in the language is scarce.', R)
    add('https://www.btkakademi.gov.tr/portal/public/terimlersozlugu', 'BTK Terimler Sözlüğü', ['ücretsiz', 'türkçe', 'sözlük'],
        'Bilişim terimlerinin resmî Türkçe karşılıkları. Belge, sunum ya da çeviri yaparken '
        'terim tutarlılığı için başvurulacak yer.',
        'Official Turkish equivalents for computing terms — the reference for keeping terminology consistent '
        'in documents, talks and translation.', R)
    add('https://github.com/LuNiZz?tab=repositories', 'LuNiZz Depoları', ['github', 'türkçe', 'güvenlik'],
        'Türkçe güvenlik ve bilişim içerikleri üreten bir geliştiricinin depoları; '
        'yerel kaynak arayanlar için toplu bir giriş noktası.',
        'The repositories of a developer producing Turkish security and IT material — '
        'a single entry point for local resources.', R)
