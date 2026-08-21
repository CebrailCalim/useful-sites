# -*- coding: utf-8 -*-
"""Databases - DevOps & Infrastructure - Networking & Sysadmin - Data Science"""


def load(add):
    # ============================================================ DATABASES
    V = 'veritabani'
    add('https://www.mysqltutorial.org/', 'MySQL Tutorial', ['ücretsiz', 'sql', 'mysql'],
        'Örnek veritabanı üzerinden MySQL’i baştan sona işliyor; JOIN türleri, alt sorgular ve '
        'saklı yordamlar ayrı ayrı ele alınmış. Resmî kılavuzdan çok daha okunur bir giriş.',
        'Works MySQL end to end over a sample database, treating join types, subqueries and stored procedures '
        'separately. Far more readable as an introduction than the official manual.', V)
    add('https://neon.com/postgresql/tutorial', 'PostgreSQL Tutorial', ['ücretsiz', 'sql', 'postgres'],
        'Her konuyu çalıştırılabilir sorguyla gösteren PostgreSQL öğreticisi. '
        'Pencere fonksiyonları ve CTE bölümleri, çoğu SQL kursunun atladığı yerde derinleşiyor.',
        'A PostgreSQL tutorial showing each topic with a runnable query, going deep on window functions and CTEs '
        'where most SQL courses stop.', V)
    add('https://learn.mongodb.com/', 'MongoDB University', ['ücretsiz', 'nosql', 'kurs'],
        'MongoDB’nin resmî ücretsiz kursları. Veri modelleme dersi kritik: ilişkisel alışkanlıkla '
        'belge veritabanı tasarlamak, ortaya çıkan en yaygın performans sorunu.',
        'MongoDB’s official free courses. The data modelling unit is the important one — designing a document store '
        'with relational habits is the most common source of performance trouble.', V)
    add('https://firebase.google.com/docs', 'Firebase', ['saas', 'freemium', 'backend', 'realtime'],
        'Gerçek zamanlı veritabanı, kimlik doğrulama, depolama ve barındırma tek pakette. '
        'Prototipi çok hızlandırıyor; sorgu esnekliği ve satıcı bağımlılığı ise sonradan sorun oluyor.',
        'Realtime database, auth, storage and hosting in one package. It accelerates a prototype sharply, '
        'while query flexibility and vendor lock-in become the later problem.', V)
    add('https://learn.couchbase.com/learn', 'Couchbase Learn', ['ücretsiz', 'nosql', 'kurs'],
        'Belge veritabanını SQL benzeri bir sorgu diliyle (N1QL) kullanıyor. '
        'İlişkisel dünyadan gelen ekipler için MongoDB’nin sorgu sözdiziminden daha az kırılma noktası.',
        'Queries a document store with a SQL-like language (N1QL), which is a gentler break for teams arriving '
        'from the relational world than MongoDB’s query syntax.', V)
    add('https://www.reddit.com/r/SQL/comments/11qe99b/best_way_to_learn_sql/', 'SQL Nasıl Öğrenilir', ['ücretsiz', 'topluluk', 'sql'],
        'Deneyimli kullanıcıların SQL öğrenme yollarını tartıştığı başlık. '
        'Kurs satmayan insanların önerileri olduğu için ayıklama işini önden yapmış oluyor.',
        'A thread where experienced users argue over how to learn SQL. Because nobody there is selling a course, '
        'the filtering is already done.', V)
    add('https://www.youtube.com/watch?v=OT1RErkfLNQ', 'SQL Sıfırdan İleri Seviye', ['video', 'ücretsiz', 'sql'],
        'Dört saatte temelden ileri seviyeye SQL; tek oturumda bütünü görmek isteyenler için. '
        'Pencere fonksiyonlarına kadar gidiyor, temel SELECT’te kalmıyor.',
        'SQL from basics to advanced in four hours for anyone who wants the whole picture in one sitting. '
        'It reaches window functions rather than stopping at basic SELECT.', V)
    add('https://www.youtube.com/watch?v=26ls5lNiijk', 'İlişkisel Veritabanı Tasarımı', ['video', 'ücretsiz', 'modelleme'],
        'Normalizasyon formlarını ve şema tasarımını işleyen tam kurs. '
        'Sorgu yazmayı değil tabloyu doğru kurmayı öğretiyor — sonraki tüm sorunların kaynağı burası.',
        'A full course on normal forms and schema design. It teaches getting the tables right rather than writing '
        'queries — which is where every later problem originates.', V)
    add('https://www.youtube.com/watch?v=pPqazMTzNOM', 'Veritabanları Derinlemesine', ['video', 'ücretsiz', 'iç-mekanizma'],
        'İndeks yapıları, işlem yalıtım seviyeleri ve kilitlenme gibi iç mekanizmaları anlatan kurs. '
        'Ürün öğreticisi değil; hangi veritabanını kullanırsan kullan geçerli.',
        'A course on internals — index structures, transaction isolation levels, locking. Not a product tutorial; '
        'it holds regardless of which database you use.', V)

    # ============================================================ DEVOPS & INFRASTRUCTURE
    O = 'devops'
    add('https://git-scm.com/book/tr/v2', 'Pro Git (Türkçe)', ['ücretsiz', 'türkçe', 'kitap', 'git'],
        'Git’in resmî kitabının Türkçe çevirisi. İç mekanizma bölümü (nesne modeli, referanslar) '
        'komut ezberlemekten kurtarıyor — Git’i asıl anlaşılır kılan kısım orası.',
        'The Turkish translation of Git’s official book. The internals chapter — object model, refs — is what '
        'frees you from memorising commands and actually makes Git make sense.', O)
    add('https://gource.io/', 'Gource', ['açık-kaynak', 'git', 'görselleştirme'],
        'Depo geçmişini büyüyen bir ağaç animasyonu olarak çiziyor; kimin nereye dokunduğu görünür oluyor. '
        'Teknik analiz aracı değil, proje tarihini anlatmak için.',
        'Renders repository history as a growing animated tree where you see who touched what. '
        'Not an analysis tool — a way to narrate a project’s history.', O)
    add('https://nginx.org/en/docs/', 'nginx', ['açık-kaynak', 'sunucu', 'reverse-proxy'],
        'Olay güdümlü mimarisi sayesinde on binlerce eşzamanlı bağlantıyı düşük bellekle taşıyor. '
        'Ters vekil ve yük dengeleyici olarak kullanımı, web sunucusu olmasından daha yaygın.',
        'Its event-driven architecture carries tens of thousands of concurrent connections on little memory. '
        'It is used as a reverse proxy and load balancer more often than as a web server.', O)
    add('https://httpd.apache.org/docs/', 'Apache HTTP Server', ['açık-kaynak', 'sunucu', 'dokümantasyon'],
        'Modül mimarisi ve .htaccess ile dizin bazlı yapılandırma esnekliği. '
        'Paylaşımlı barındırmada hâlâ hâkim; nginx’e göre yüksek eşzamanlılıkta daha çok bellek yiyor.',
        'A module architecture plus per-directory configuration through .htaccess. Still dominant in shared hosting, '
        'and hungrier for memory than nginx under high concurrency.', O)
    add('https://www.litespeedtech.com/', 'LiteSpeed', ['ücretli', 'sunucu'],
        'Apache yapılandırmasını olduğu gibi okuyabilen ticari sunucu; olay güdümlü çekirdeği '
        'ile daha az kaynak tüketiyor. WordPress barındırmada önbellek eklentisiyle birlikte yaygın.',
        'A commercial server that reads Apache configuration as-is while using an event-driven core and fewer '
        'resources. Common in WordPress hosting alongside its cache plugin.', O)
    add('https://docs.litespeedtech.com/', 'LiteSpeed Dokümantasyonu', ['dokümantasyon', 'sunucu', 'önbellek'],
        'Yapılandırma referansı; LSCache kurallarının nasıl yazılacağı burada. '
        'Önbellekleme ayarları performansın büyük kısmını belirliyor.',
        'The configuration reference, including how LSCache rules are written — '
        'cache settings account for most of the performance you get.', O)
    add('https://kafka.apache.org/42/getting-started/introduction/', 'Apache Kafka', ['açık-kaynak', 'kuyruk', 'olay-akışı'],
        'Mesajları tüketildikten sonra da saklıyor; tüketiciler kendi konumlarını (offset) taşıyıp '
        'geçmişi yeniden okuyabiliyor. Klasik kuyruklardan asıl ayrımı bu kalıcılık.',
        'Retains messages after consumption, with consumers carrying their own offsets so they can replay history. '
        'That durability is the real split from classic queues.', O)
    add('https://www.rabbitmq.com/tutorials', 'RabbitMQ Öğreticileri', ['açık-kaynak', 'kuyruk', 'amqp'],
        'Altı adımda mesaj kuyruğu desenlerini öğreten resmî seri: iş kuyruğu, yayın-abone, '
        'yönlendirme, RPC. Kafka olay akışına, bu görev dağıtımına odaklı.',
        'The official six-step series on queue patterns — work queues, pub/sub, routing, RPC. '
        'Kafka is for event streaming; this is for task distribution.', O)
    add('https://docs.celeryq.dev/en/stable/', 'Celery', ['açık-kaynak', 'python', 'kuyruk'],
        'Python’da arka plan görevlerinin standardı; Redis ya da RabbitMQ’yu aracı olarak kullanıyor. '
        'Zamanlanmış görevler (beat) ve yeniden deneme mantığı da içinde.',
        'The standard for background tasks in Python, using Redis or RabbitMQ as a broker, '
        'with scheduled tasks (beat) and retry logic included.', O)
    add('https://redis.io/docs/latest/', 'Redis Dokümantasyonu', ['dokümantasyon', 'önbellek', 'veri-yapısı'],
        'Liste, küme, sıralı küme ve akış gibi veri yapılarının referansı. '
        'Redis’i basit bir anahtar-değer deposu sanmak, elindeki aracın çoğunu kullanmamak demek.',
        'The reference for its data structures — lists, sets, sorted sets, streams. Treating Redis as a plain '
        'key-value store means leaving most of the tool unused.', O)
    add('https://grafana.com/', 'Grafana', ['açık-kaynak', 'gözlemlenebilirlik', 'pano'],
        'Prometheus, Loki, PostgreSQL ve onlarca kaynağı aynı panoda birleştiriyor. '
        'Veri kaynağından bağımsız olması, izleme yığınının ortak yüzü hâline gelmesini sağladı.',
        'Unifies Prometheus, Loki, PostgreSQL and dozens of sources on one dashboard. Being data-source agnostic '
        'is how it became the shared face of monitoring stacks.', O)
    add('https://sentry.io/welcome/', 'Sentry', ['freemium', 'açık-kaynak', 'hata-izleme'],
        'Hataları yığın izi, kaynak haritası ve kullanıcı bağlamıyla topluyor ve benzerlerini grupluyor. '
        'Günlük dosyası okumaya karşı, aynı hatanın kaç kullanıcıyı etkilediğini gösteriyor.',
        'Collects errors with stack traces, source maps and user context, grouping duplicates. Against reading log '
        'files, it tells you how many users a given error actually hit.', O)
    add('https://github.com/dokploy/dokploy', 'Dokploy', ['açık-kaynak', 'github', 'self-hosted', 'docker'],
        'Kendi VPS’inde Vercel benzeri dağıtım deneyimi kuruyor: git iterek yayına alma, '
        'veritabanı sağlama ve otomatik TLS. Heroku’nun ücretsiz katmanı kapandıktan sonra doğan boşluğu dolduruyor.',
        'Brings a Vercel-like deploy experience to your own VPS — git-push deploys, database provisioning, automatic TLS. '
        'It fills the hole left when Heroku’s free tier closed.', O)
    add('https://vercel.com/', 'Vercel', ['saas', 'freemium', 'barındırma', 'edge'],
        'Ön yüz odaklı dağıtım; her PR için önizleme ortamı açması sektörde standart hâline geldi. '
        'Next.js’in arkasındaki şirket, dolayısıyla o çatıda en iyi entegrasyon burada.',
        'Frontend-focused deployment whose per-PR preview environments became an industry standard. '
        'It is the company behind Next.js, so integration with that framework is tightest here.', O)
    add('https://aws.amazon.com/', 'Amazon Web Services', ['ücretli', 'bulut'],
        'Servis yelpazesi en geniş bulut. Genişlik avantaj ama maliyet takibi ayrı bir uzmanlık alanı; '
        'veri çıkış (egress) ücretleri özellikle sürpriz yapıyor.',
        'The cloud with the widest service range. The breadth is an advantage, while cost tracking is its own '
        'discipline — egress charges in particular catch people out.', O)
    add('https://www.hetzner.com/', 'Hetzner', ['ücretli', 'sunucu', 'barındırma'],
        'Almanya ve Finlandiya’da fiziksel sunucu ve VPS; aynı çekirdek/RAM için büyük bulutların '
        'birkaç katı ucuz. Yönetilen servis yok, işletim tamamen sana kalıyor.',
        'Dedicated servers and VPS in Germany and Finland at a fraction of the big clouds’ price for the same '
        'cores and RAM. No managed services — operations are entirely yours.', O)
    add('https://avenacloud.com/', 'AvenaCloud', ['ücretli', 'sunucu', 'vps'],
        'VPS ve fiziksel sunucu sağlayıcı; küçük ölçekli projeler için bütçe odaklı bir seçenek.',
        'A VPS and dedicated server provider positioned on budget for small-scale projects.', O)
    add('https://alexhost.com/', 'AlexHost', ['ücretli', 'sunucu', 'yargı-bölgesi'],
        'Moldova merkezli barındırma. Farklı bir yargı bölgesi ve gevşek içerik politikası '
        'sunması sebebiyle tercih ediliyor; bu aynı zamanda komşuların kim olduğu sorusunu doğuruyor.',
        'Moldova-based hosting chosen for a different jurisdiction and looser content policy — '
        'which also raises the question of who your neighbours are.', O)
    add('https://njal.la/', 'Njalla', ['ücretli', 'gizlilik', 'alan-adı'],
        'Alan adını senin adına kendi üstüne kaydediyor, yani WHOIS kaydında sen görünmüyorsun. '
        'Vekil gizlilik hizmetinden farkı, mülkiyetin hukuken onlarda olması — bu bir güven meselesi.',
        'Registers the domain in its own name on your behalf, so you do not appear in WHOIS. Unlike a privacy proxy '
        'the legal ownership sits with them, which makes it a question of trust.', O)
    add('https://www.guzel.net.tr/', 'Güzel Hosting', ['ücretli', 'türkçe', 'barındırma'],
        'Türkiye merkezli barındırma ve alan adı; .tr uzantısı, yerel ödeme ve Türkçe destek sunuyor. '
        'Sunucunun Türkiye’de olması gereken projeler için pratik.',
        'Turkey-based hosting and domains with .tr registration, local payment and Turkish support — '
        'practical when the server has to sit in Turkey.', O)
    add('https://github.com/m1k1o/neko', 'Neko', ['açık-kaynak', 'github', 'docker', 'webrtc'],
        'Kapsayıcı içinde tarayıcı çalıştırıp WebRTC ile paylaşıyor; birden çok kişi aynı oturumu '
        'kontrol edebiliyor. Birlikte izleme ve izole gezinme için kullanılıyor.',
        'Runs a browser in a container and shares it over WebRTC, with several people able to control one session. '
        'Used for watch-together and for isolated browsing.', O)

    # ============================================================ NETWORKING & SYSADMIN
    A = 'ag'
    add('https://www.netacad.com/', 'Cisco Networking Academy', ['ücretsiz', 'ağ', 'kurs'],
        'Cisco’nun resmî ağ müfredatı; CCNA’ya hazırlayan derslerin bir kısmı ücretsiz. '
        'Packet Tracer laboratuvarlarıyla teoriyi topoloji kurarak sınıyorsun.',
        'Cisco’s official networking curriculum, with part of the CCNA track free. '
        'Packet Tracer labs let you test the theory by building topologies.', A)
    add('https://www.netacad.com/catalogs/learn/networking?language=tr-tr', 'NetAcad Ağ Kursları (Türkçe)', ['ücretsiz', 'türkçe', 'ağ'],
        'Cisco ağ kurslarının Türkçe kataloğu; giriş seviyesi dersler ücretsiz ve rozet veriyor. '
        'Türkçe teknik ağ eğitimi bulmak yerelde kolay değil.',
        'The Turkish catalogue of Cisco networking courses, with free entry-level classes that award badges. '
        'Turkish-language networking training is not easy to find locally.', A)
    add('https://www.netacad.com/resources/lab-downloads?courseLang=en-US', 'Packet Tracer & Laboratuvarlar', ['ücretsiz', 'ağ', 'simülatör'],
        'Cisco Packet Tracer indirmesi ve laboratuvar dosyaları. '
        'Anahtar ve yönlendirici almadan VLAN, OSPF ve ACL yapılandırması denenebiliyor.',
        'The Packet Tracer download plus lab files, letting you practise VLAN, OSPF and ACL configuration '
        'without buying switches and routers.', A)
    add('https://www.firewall.cx/cisco/cisco-switches/cisco-switches-sg500-52p.html', 'Cisco SG500-52P Kurulumu', ['ücretsiz', 'ağ', 'rehber'],
        'Belirli bir anahtar modelinin ilk kurulumu, ekran görüntüleriyle adım adım. '
        'Resmî kılavuzun atladığı pratik ayrıntılar burada.',
        'First-time setup of one specific switch model, screenshot by screenshot — '
        'with the practical details the official manual skips.', A)
    add('https://www.firewall.cx/downloads/cisco-product-datasheets-a-guides/cisco-sg500-series-switches.html', 'Cisco SG500 Serisi', ['ücretsiz', 'ağ', 'referans'],
        'SG500 serisinin teknik veri sayfaları; port sayısı, PoE bütçesi ve yığınlama desteği karşılaştırmalı. '
        'İkinci el alırken model farklarını bilmek gerekiyor.',
        'Datasheets for the SG500 series comparing port counts, PoE budgets and stacking support — '
        'the model differences you need when buying second-hand.', A)
    add('https://www.wireshark.org/#download', 'Wireshark', ['açık-kaynak', 'ağ', 'analiz'],
        'Paket yakalama ve protokol çözümlemenin standardı; TLS anahtarı verirsen şifreli trafiği de açıyor. '
        'Ağ sorunlarında “sanırım” yerine kanıt üretmenin tek yolu.',
        'The standard for packet capture and protocol dissection, and it will decrypt TLS if you hand it the keys. '
        'The only way to replace “I think” with evidence in a network problem.', A)
    add('https://labex.io/linuxjourney', 'Linux Journey', ['ücretsiz', 'linux', 'interaktif'],
        'Linux’u küçük modüllere bölerek öğretiyor: dosya sistemi, izinler, süreçler, paket yönetimi. '
        'Kapsamlı kitapların yıldırdığı yerde sindirilebilir parçalar sunuyor.',
        'Teaches Linux in small modules — filesystem, permissions, processes, package management — '
        'offering digestible pieces where comprehensive books overwhelm.', A)
    add('https://www.youtube.com/watch?v=zIdv2NDRExI', 'Linux Öğrenmenin En İyi Yolu', ['video', 'ücretsiz', 'linux'],
        'Komut öğretmiyor, nasıl çalışılacağını tarif ediyor: hangi dağıtım, hangi sırayla, '
        'hangi projelerle. Yön bulmak için başlangıçta işe yarıyor.',
        'Does not teach commands but describes how to study — which distribution, in what order, through which '
        'projects. Useful for orientation at the start.', A)
    add('https://www.youtube.com/watch?v=fQbBPa0ADvs', 'Bilgisayar Ağları Temelleri', ['video', 'ücretsiz', 'ağ'],
        'OSI katmanlarından yönlendirmeye kadar ağ kavramlarını tam kurs formatında işliyor. '
        'Sertifika çalışmasına başlamadan önce zemin kurmak için.',
        'Works networking concepts from the OSI layers through routing in full-course format — '
        'for laying the ground before certification study.', A)
    add('https://www.youtube.com/watch?v=xj_GjnD4uyI', '20 Dakikada Tüm Ağ Kavramları', ['video', 'ücretsiz', 'ağ'],
        'Ağ terimlerini hızla tarayan özet. Öğrenmek için değil; bildiğini sandığın yerlerdeki '
        'boşlukları yirmi dakikada bulmak için.',
        'A rapid sweep of networking terminology. Not for learning, but for finding in twenty minutes the gaps '
        'in what you assumed you knew.', A)
    add('https://www.youtube.com/watch?v=HwUqCZFx6wk', 'DHCP (CompTIA A+)', ['video', 'sertifika', 'ağ'],
        'A+ müfredatındaki DHCP konusunun kısa anlatımı; kapsam sınav hedefine birebir oturuyor. '
        'Fazlasını anlatmaması sınav çalışmasında avantaj.',
        'A short treatment of DHCP as the A+ syllabus defines it, mapped exactly to the exam objective. '
        'Not covering more is an advantage when revising.', A)
    add('https://www.youtube.com/watch?v=lAHqO9sDVy4', 'DNS Yapılandırma (CompTIA A+)', ['video', 'sertifika', 'ağ'],
        'A+ kapsamındaki DNS kayıt türleri ve yapılandırması. Kısa ve sınav odaklı.',
        'DNS record types and configuration within the A+ scope — short and exam-focused.', A)
    add('https://www.youtube.com/watch?v=5kt4t2gzt9g', 'Windows 11 Tam Rehber', ['video', 'ücretsiz', 'windows'],
        'Windows 11 ayarlarını baştan sona gezen rehber; grup ilkesi ve kayıt defteri ayarlarına da giriyor. '
        'Kullanıcı desteği tarafında hızlı başvuru.',
        'A guide walking the whole of Windows 11’s settings, reaching into group policy and registry tweaks. '
        'A quick reference on the user-support side.', A)
    add('https://servicedesk-simulator.com/', 'ServiceDesk Simulator', ['saas', 'freemium', 'it-destek', 'simülasyon'],
        'Gerçek yardım masası biletleriyle çalışmayı simüle ediyor: önceliklendirme, tırmandırma, '
        'SLA takibi. IT destek eğitimlerinin teorik kaldığı yeri dolduruyor.',
        'Simulates working a real helpdesk queue — prioritisation, escalation, SLA tracking. '
        'It fills the practical gap that IT support courses leave theoretical.', A)
    add('https://www.hirensbootcd.org/', "Hiren's BootCD PE", ['ücretsiz', 'kurtarma', 'windows'],
        'Açılmayan sistemler için önyüklenebilir Windows PE ortamı; disk klonlama, parola sıfırlama '
        've veri kurtarma araçları tek imajda. Sistem yöneticisinin cebinde taşıdığı USB.',
        'A bootable Windows PE environment for systems that will not start, bundling disk cloning, password reset '
        'and data recovery in one image. The USB stick a sysadmin carries.', A)
    add('https://www.disk-image.com/index.html', 'Active@ Disk Image', ['ücretli', 'yedekleme', 'windows'],
        'Sektör bazında disk imajı alıp geri yüklüyor; dosya yedeklemesinden farkı, işletim sistemi '
        've önyükleme kaydı dahil her şeyi bire bir kopyalaması.',
        'Takes and restores sector-level disk images. Unlike file backup it copies everything bit for bit, '
        'operating system and boot record included.', A)
    add('https://www.cozumpark.com/', 'ÇözümPark', ['ücretsiz', 'türkçe', 'topluluk', 'sysadmin'],
        'Türkçe sistem yöneticiliği topluluğu ve makale arşivi; Active Directory, Exchange ve '
        'sanallaştırma tarafında derinlik var. Yerel senaryolar için nadir bir kaynak.',
        'A Turkish sysadmin community and article archive with real depth on Active Directory, Exchange and '
        'virtualisation — a rare resource for locally specific scenarios.', A)
    add('https://www.nist.gov/cryptography', 'NIST Kriptografi', ['ücretsiz', 'standart', 'kriptografi'],
        'Kriptografi standartlarının kaynağı; hangi algoritmanın hâlâ onaylı olduğunu buradan öğrenirsin. '
        'Kuantum sonrası algoritma seçimleri de burada yayımlandı.',
        'The source of cryptographic standards, where you check which algorithms remain approved. '
        'The post-quantum algorithm selections were published here too.', A)
    add('https://www.youtube.com/watch?v=0pXicD2hqFU', 'LFSR ve Rastgele Sayı Üreteçleri', ['video', 'kriptografi', 'donanım'],
        'Doğrusal geri beslemeli kaydırma yazmaçlarının nasıl çalıştığını devre düzeyinde anlatıyor. '
        'Sözde rastgeleliğin donanımda nasıl üretildiğine iyi bir giriş.',
        'Explains linear feedback shift registers at circuit level — a good introduction to how pseudo-randomness '
        'is actually produced in hardware.', A)

    # ============================================================ DATA SCIENCE & ML
    D = 'veri'
    add('https://www.kaggle.com/', 'Kaggle', ['ücretsiz', 'veri', 'yarışma', 'topluluk'],
        'Yarışma, veri kümesi ve not defteri aynı platformda. Asıl değeri, kazanan çözümlerin '
        'yarışma bitince açıkça paylaşılması — uygulamalı ML’in en iyi açık arşivi.',
        'Competitions, datasets and notebooks on one platform. The real value is that winning solutions are '
        'published once a contest closes, making it the best open archive of applied ML.', D)
    add('https://www.kaggle.com/competitions', 'Kaggle Yarışmaları', ['ücretsiz', 'veri', 'yarışma'],
        'Aktif ve geçmiş yarışmalar. Gerçek ölçütle değerlendirilmek, kendi projendeki '
        '“iyi görünüyor” yanılsamasını kırıyor.',
        'Active and past competitions. Being scored against a real metric breaks the “looks fine to me” illusion '
        'of working on your own project.', D)
    add('https://www.kaggle.com/competitions/arc-prize-2026-paper-track', 'ARC Prize 2026', ['ücretsiz', 'araştırma', 'yarışma'],
        'Soyut akıl yürütme üzerine yarışma; görevleri insanın kolay, modellerin zor bulduğu '
        'biçimde tasarlanmış. Ölçekleme yerine yeni yaklaşım gerektiriyor.',
        'A competition on abstract reasoning whose tasks are designed to be easy for humans and hard for models. '
        'It rewards a new approach rather than more scale.', D)
    add('https://datasetsearch.research.google.com/', 'Google Dataset Search', ['ücretsiz', 'veri', 'arama'],
        'Web’e dağılmış açık veri kümelerini schema.org işaretlemesi üzerinden arıyor. '
        'Tek bir depoya bağlı olmadığı için kurum arşivlerini de kapsıyor.',
        'Searches open datasets scattered across the web via schema.org markup. Being tied to no single repository, '
        'it reaches institutional archives too.', D)
    add('https://www.databricks.com/', 'Databricks', ['saas', 'ücretli', 'veri', 'spark'],
        'Spark üzerine kurulu veri ve ML platformu; Delta Lake ile veri gölüne işlem (ACID) garantisi getiriyor. '
        '“Lakehouse” iddiasının teknik karşılığı bu.',
        'A data and ML platform built on Spark, bringing ACID guarantees to the data lake through Delta Lake — '
        'which is the technical substance behind the “lakehouse” claim.', D)
    add('https://github.com/microsoft/Data-Science-For-Beginners/tree/main', 'Data Science for Beginners', ['github', 'müfredat', 'ücretsiz'],
        '20 derslik müfredat; her ders ders öncesi/sonrası sınav ve bir projeyle geliyor. '
        'Veri etiği ve görselleştirme bölümleri çoğu teknik kursta atlanan konular.',
        'A 20-lesson curriculum where each unit ships with pre/post quizzes and a project. '
        'Its data ethics and visualisation sections cover ground most technical courses skip.', D)
    add('https://github.com/mrdbourke/zero-to-mastery-ml', 'Zero to Mastery ML', ['github', 'not-defteri', 'python'],
        'Uçtan uca ML not defterleri; veri temizlemeden model değerlendirmeye kadar çalışan bir hat okutuyor. '
        'Kavram anlatımı yerine gerçek kod üzerinden ilerliyor.',
        'End-to-end ML notebooks walking a working pipeline from data cleaning to model evaluation, '
        'progressing through real code rather than concept prose.', D)
    add('https://github.com/rasbt/LLMs-from-scratch', 'LLMs from Scratch', ['github', 'kitap', 'pytorch'],
        'Bir GPT’yi PyTorch ile sıfırdan yazdıran kitap deposu: tokenizer, dikkat mekanizması, '
        'eğitim döngüsü ve ince ayar. Kütüphane çağırmak yerine mekanizmayı kurduruyor.',
        'A book repo that has you write a GPT from scratch in PyTorch — tokeniser, attention, training loop, '
        'fine-tuning. You build the mechanism instead of calling a library.', D)
    add('https://github.com/FareedKhan-dev/train-llm-from-scratch', 'Train LLM from Scratch', ['github', 'pytorch', 'eğitim'],
        'Veri indirmeden dağıtık eğitime kadar tüm hattı çalışan kodla gösteriyor. '
        'Teorik anlatımların atladığı kısım genelde bu altyapı tarafı.',
        'Shows the whole pipeline in working code, from data download to distributed training — '
        'the infrastructure side theoretical write-ups usually skip.', D)
    add('https://www.reddit.com/r/MachineLearningJobs/comments/1r5upkb/how_i_land_15_machine_learning_engineer_offers/', 'ML Mühendisliğinde İş Arama', ['ücretsiz', 'kariyer', 'topluluk'],
        'Bir ML mühendisinin iş arama sürecini sayılarla anlattığı başlık: kaç başvuru, hangi aşamalar, '
        'ne işe yaradı. Genel kariyer tavsiyelerine karşı birinci elden veri.',
        'An ML engineer’s account of a job hunt with the numbers — applications sent, stages reached, what worked. '
        'First-hand data against generic career advice.', D)
