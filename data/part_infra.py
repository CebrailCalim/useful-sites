# -*- coding: utf-8 -*-
"""Veritabanı, DevOps & Altyapı, Ağ & Sistem, Veri Bilimi"""


def load(add):
    # ============================================================ VERİTABANI
    V = 'veritabani'
    add('https://www.mysqltutorial.org/', 'MySQL Tutorial', ['ücretsiz', 'sql'],
        'MySQL’i baştan sona örneklerle anlatan öğretici; resmî dokümana göre çok daha okunur bir giriş.',
        'A hands-on MySQL tutorial that is far more readable as an introduction than the official manual.', V)
    add('https://neon.com/postgresql/tutorial', 'PostgreSQL Tutorial', ['ücretsiz', 'sql', 'postgres'],
        'PostgreSQL’e örnek veri tabanı üzerinden giriş; her konuyu çalıştırılabilir sorguyla göstermesi ayırt edici.',
        'An introduction to PostgreSQL over a sample database, showing each topic with a runnable query.', V)
    add('https://learn.mongodb.com/', 'MongoDB University', ['ücretsiz', 'nosql', 'kurs'],
        'MongoDB’nin resmî ücretsiz kursları; ilişkisel modelden geçenler için veri modelleme dersi en kritik kısım.',
        'MongoDB’s official free courses; the data modelling unit is the critical part for anyone arriving from relational.', V)
    add('https://firebase.google.com/docs', 'Firebase', ['freemium', 'dokümantasyon', 'backend'],
        'Google’ın sunucusuz arka uç servisi; veritabanı, kimlik doğrulama ve barındırmayı tek pakette vermesi hız kazandırıyor.',
        'Google’s serverless backend bundling database, auth and hosting in one package, which buys development speed.', V)
    add('https://learn.couchbase.com/learn', 'Couchbase Learn', ['ücretsiz', 'nosql', 'kurs'],
        'Couchbase’in resmî eğitim portalı; belge veritabanını SQL benzeri sorgu diliyle kullanması diğer NoSQL seçeneklerinden ayırıyor.',
        'Couchbase’s official training; querying a document store with a SQL-like language is what separates it from other NoSQL options.', V)
    add('https://www.reddit.com/r/SQL/comments/11qe99b/best_way_to_learn_sql/', 'SQL Nasıl Öğrenilir (r/SQL)', ['ücretsiz', 'topluluk', 'sql'],
        'Deneyimli kullanıcıların SQL öğrenme yollarını tartıştığı başlık; pazarlama içermeyen kaynak önerileri için.',
        'A thread where experienced users debate how to learn SQL — resource suggestions without marketing.', V)
    add('https://www.youtube.com/watch?v=OT1RErkfLNQ', 'SQL Sıfırdan İleri Seviye', ['ücretsiz', 'video', 'sql'],
        'Dört saatte temelden ileri seviyeye SQL; tek oturumda bütünü görmek isteyenler için.',
        'SQL from basics to advanced in four hours — for seeing the whole picture in one sitting.', V)
    add('https://www.youtube.com/watch?v=26ls5lNiijk', 'İlişkisel Veritabanı Tasarımı', ['ücretsiz', 'video'],
        'Normalizasyon ve şema tasarımına odaklı tam kurs; sorgu yazmayı değil, tabloyu doğru kurmayı öğretir.',
        'A full course on normalisation and schema design — it teaches getting the tables right, not writing queries.', V)
    add('https://www.youtube.com/watch?v=pPqazMTzNOM', 'Veritabanları Derinlemesine', ['ücretsiz', 'video'],
        'Veritabanı iç mekanizmalarını (indeks, işlem, kilit) anlatan kapsamlı kurs; ürün öğretici değil kavram dersi.',
        'A comprehensive course on database internals — indexes, transactions, locks. Concepts rather than a product tutorial.', V)

    # ============================================================ DEVOPS & ALTYAPI
    O = 'devops'
    add('https://git-scm.com/book/tr/v2', 'Pro Git (Türkçe)', ['ücretsiz', 'türkçe', 'kitap', 'git'],
        'Git’in resmî kitabının Türkçe çevirisi; komut ezberi yerine Git’in veri modelini anlatması ayırt edici yanı.',
        'The Turkish translation of Git’s official book, distinguished by teaching Git’s data model rather than command recipes.', O)
    add('https://gource.io/', 'Gource', ['açık kaynak', 'git', 'görselleştirme'],
        'Depo geçmişini animasyonlu ağaç olarak gösteren araç; teknik analizden çok proje tarihini anlatmak için.',
        'Renders repository history as an animated tree — more for telling a project’s story than technical analysis.', O)
    add('https://nginx.org/en/docs/', 'nginx', ['açık kaynak', 'dokümantasyon', 'sunucu'],
        'Yaygın web sunucusu ve ters vekilin resmî dokümanı; Apache’den farkı, olay güdümlü mimarisiyle yüksek eşzamanlılıkta daha az bellek kullanması.',
        'Official docs for the widespread web server and reverse proxy; its event-driven architecture uses less memory than Apache under high concurrency.', O)
    add('https://httpd.apache.org/docs/', 'Apache HTTP Server', ['açık kaynak', 'dokümantasyon', 'sunucu'],
        'Klasik web sunucusunun resmî dokümanı; .htaccess ile dizin bazlı yapılandırma esnekliği hâlâ ayırt edici yanı.',
        'Official docs for the classic web server; per-directory configuration via .htaccess remains its distinguishing flexibility.', O)
    add('https://www.litespeedtech.com/', 'LiteSpeed', ['ücretli', 'sunucu'],
        'Apache uyumlu ama daha hızlı olduğu iddiasındaki ticari web sunucusu; paylaşımlı barındırmada yaygın.',
        'A commercial web server claiming Apache compatibility with better performance; common in shared hosting.', O)
    add('https://docs.litespeedtech.com/', 'LiteSpeed Dokümantasyonu', ['dokümantasyon', 'sunucu'],
        'LiteSpeed yapılandırma referansı; önbellek eklentisi ayarları için birincil kaynak.',
        'LiteSpeed configuration reference — the primary source for its cache plugin settings.', O)
    add('https://kafka.apache.org/42/getting-started/introduction/', 'Apache Kafka', ['açık kaynak', 'dokümantasyon', 'kuyruk'],
        'Yüksek hacimli olay akışı platformu; klasik mesaj kuyruklarından farkı, mesajları tüketildikten sonra da saklaması.',
        'High-volume event streaming platform; unlike classic message queues it retains messages after consumption.', O)
    add('https://www.rabbitmq.com/tutorials', 'RabbitMQ Öğreticileri', ['açık kaynak', 'dokümantasyon', 'kuyruk'],
        'Mesaj kuyruğu desenlerini altı adımda öğreten resmî seri; Kafka’dan farkı, klasik iş kuyruğu senaryolarına odaklanması.',
        'The official six-step series on message queue patterns; unlike Kafka it centres on classic task-queue scenarios.', O)
    add('https://docs.celeryq.dev/en/stable/', 'Celery', ['açık kaynak', 'python', 'kuyruk'],
        'Python’da arka plan görev kuyruğunun standardı; zamanlanmış ve gecikmeli işleri de üstlenmesi ayırt edici.',
        'The standard background task queue in Python, also handling scheduled and delayed jobs.', O)
    add('https://redis.io/docs/latest/', 'Redis Dokümantasyonu', ['dokümantasyon', 'önbellek'],
        'Redis veri yapıları ve kalıcılık seçeneklerinin resmî referansı; hangi yapının ne zaman kullanılacağı burada anlatılıyor.',
        'Official reference for Redis data structures and persistence — which structure to use when is documented here.', O)
    add('https://grafana.com/', 'Grafana', ['açık kaynak', 'gözlem', 'panel'],
        'Metrik ve günlük görselleştirme panosu; veri kaynağından bağımsız olması, izleme yığınında ortak arayüz olmasını sağlıyor.',
        'Dashboarding for metrics and logs; being data-source agnostic is why it became the common front-end of monitoring stacks.', O)
    add('https://sentry.io/welcome/', 'Sentry', ['freemium', 'gözlem', 'hata'],
        'Uygulama hatalarını yığın izi ve bağlamıyla toplayan servis; günlük dosyası okumaya karşı gruplandırılmış hata görünümü sunar.',
        'Collects application errors with stack traces and context, giving grouped error views instead of log-file reading.', O)
    add('https://github.com/dokploy/dokploy', 'Dokploy', ['açık kaynak', 'github', 'kendi sunucunda'],
        'Kendi sunucunda çalışan dağıtım platformu; Vercel/Heroku deneyimini kendi VPS’inde kurmayı hedefliyor.',
        'A self-hosted deployment platform aiming to bring the Vercel/Heroku experience to your own VPS.', O)
    add('https://vercel.com/', 'Vercel', ['freemium', 'barındırma'],
        'Ön yüz odaklı dağıtım platformu; git iterek yayına alma ve önizleme ortamlarını standartlaştırmasıyla biliniyor.',
        'Frontend-focused deployment platform, known for standardising git-push deploys and preview environments.', O)
    add('https://aws.amazon.com/', 'Amazon Web Services', ['ücretli', 'bulut'],
        'En geniş servis yelpazesine sahip bulut sağlayıcı; genişlik avantajı, karmaşıklık ve maliyet takibi ise dezavantajı.',
        'The cloud provider with the widest service range; breadth is the advantage, complexity and cost tracking the downside.', O)
    add('https://www.hetzner.com/', 'Hetzner', ['ücretli', 'sunucu', 'barındırma'],
        'Almanya merkezli sunucu sağlayıcı; büyük bulutlara göre belirgin şekilde ucuz olması başlıca tercih sebebi.',
        'German server provider whose markedly lower price than the big clouds is the main reason people choose it.', O)
    add('https://avenacloud.com/', 'AvenaCloud', ['ücretli', 'sunucu'],
        'VPS ve fiziksel sunucu sağlayıcı; küçük ölçekli projeler için bütçe odaklı bir seçenek.',
        'VPS and dedicated server provider — a budget-oriented option for small-scale projects.', O)
    add('https://alexhost.com/', 'AlexHost', ['ücretli', 'sunucu'],
        'Moldova merkezli barındırma sağlayıcı; içerik politikası esnekliği ve yargı bölgesi farkıyla tercih ediliyor.',
        'Moldova-based hosting provider, chosen for its content policy flexibility and different jurisdiction.', O)
    add('https://njal.la/', 'Njalla', ['ücretli', 'gizlilik', 'alan adı'],
        'Gizlilik odaklı alan adı ve sunucu sağlayıcı; alan adını senin adına kendi üstüne kaydetmesiyle ayrışıyor.',
        'Privacy-focused domain and server provider, distinguished by registering the domain in its own name on your behalf.', O)
    add('https://www.guzel.net.tr/', 'Güzel Hosting', ['ücretli', 'türkçe', 'barındırma'],
        'Türkiye merkezli barındırma ve alan adı sağlayıcı; yerel ödeme ve Türkçe destek isteyenler için.',
        'Turkey-based hosting and domain provider, for those wanting local payment and Turkish-language support.', O)
    add('https://github.com/m1k1o/neko', 'Neko', ['açık kaynak', 'github', 'kendi sunucunda'],
        'Tarayıcıda paylaşılabilir sanal tarayıcı çalıştıran sunucu; birlikte izleme ve izole gezinme için kullanılıyor.',
        'Runs a shareable virtual browser in a container, used for watch-together sessions and isolated browsing.', O)

    # ============================================================ AĞ & SİSTEM YÖNETİMİ
    A = 'ag'
    add('https://www.netacad.com/', 'Cisco Networking Academy', ['ücretsiz', 'ağ', 'kurs'],
        'Cisco’nun resmî ağ eğitimi programı; sanal laboratuvarlarla teoriyi uygulamaya bağlaması ayırt edici yanı.',
        'Cisco’s official networking curriculum, distinguished by tying theory to practice through virtual labs.', A)
    add('https://www.netacad.com/catalogs/learn/networking?language=tr-tr', 'NetAcad Ağ Kursları (Türkçe)', ['ücretsiz', 'türkçe', 'ağ'],
        'Cisco ağ kurslarının Türkçe kataloğu; ücretsiz giriş seviyesi dersleri buradan seçilebiliyor.',
        'The Turkish catalogue of Cisco networking courses, where the free entry-level classes can be picked.', A)
    add('https://www.netacad.com/resources/lab-downloads?courseLang=en-US', 'Packet Tracer & Laboratuvarlar', ['ücretsiz', 'ağ', 'araç'],
        'Cisco Packet Tracer ve laboratuvar dosyaları; donanım almadan ağ topolojisi kurup denemek için.',
        'Cisco Packet Tracer and lab files — for building and testing network topologies without buying hardware.', A)
    add('https://www.firewall.cx/cisco/cisco-switches/cisco-switches-sg500-52p.html', 'Cisco SG500-52P Kurulumu', ['ücretsiz', 'ağ', 'rehber'],
        'Belirli bir Cisco anahtar modelinin kurulum rehberi; resmî kılavuzdan farkı, adım adım ekran görüntüleriyle ilerlemesi.',
        'A setup guide for a specific Cisco switch; unlike the official manual it walks through with screenshots.', A)
    add('https://www.firewall.cx/downloads/cisco-product-datasheets-a-guides/cisco-sg500-series-switches.html', 'Cisco SG500 Serisi', ['ücretsiz', 'ağ', 'referans'],
        'SG500 anahtar serisinin teknik veri sayfaları; model seçimi ve özellik karşılaştırması için.',
        'Datasheets for the SG500 switch series, for model selection and feature comparison.', A)
    add('https://www.wireshark.org/#download', 'Wireshark', ['açık kaynak', 'ağ', 'araç'],
        'Ağ paketlerini yakalayıp çözümleyen standart araç; ağ sorunlarında tahmin yerine kanıt sağlar.',
        'The standard packet capture and analysis tool — it replaces guessing with evidence in network problems.', A)
    add('https://labex.io/linuxjourney', 'Linux Journey', ['ücretsiz', 'linux', 'interaktif'],
        'Linux’u küçük modüllerle öğreten ücretsiz kaynak; kapsamlı kitaplara karşı kısa ve sindirilebilir bölümler sunar.',
        'A free resource teaching Linux in small modules — short, digestible units against comprehensive books.', A)
    add('https://www.youtube.com/watch?v=zIdv2NDRExI', 'Linux Öğrenmenin En İyi Yolu', ['ücretsiz', 'video', 'linux'],
        'Linux öğrenme stratejisini anlatan video; komut öğretmekten çok nasıl çalışılacağını tarif ediyor.',
        'A video on strategy for learning Linux — it describes how to study rather than teaching commands.', A)
    add('https://www.youtube.com/watch?v=fQbBPa0ADvs', 'Bilgisayar Ağları Temelleri', ['ücretsiz', 'video', 'ağ'],
        'Ağ kavramlarının tam kurs formatında anlatımı; sertifika çalışmasından önce temel oturtmak için.',
        'A full-course walk through networking concepts, useful for grounding before certification study.', A)
    add('https://www.youtube.com/watch?v=xj_GjnD4uyI', '20 Dakikada Tüm Ağ Kavramları', ['ücretsiz', 'video', 'ağ'],
        'Ağ terimlerini hızlıca tarayan özet video; öğrenmek için değil, hatırlamak ve boşluk bulmak için.',
        'A rapid sweep of networking terms — not for learning, but for refreshing and spotting gaps.', A)
    add('https://www.youtube.com/watch?v=HwUqCZFx6wk', 'DHCP (CompTIA A+)', ['ücretsiz', 'video', 'sertifika'],
        'CompTIA A+ müfredatındaki DHCP konusunun kısa anlatımı; sınav kapsamına birebir eşlenmesi ayırt edici.',
        'A short explanation of DHCP from the CompTIA A+ syllabus, mapped exactly to exam scope.', A)
    add('https://www.youtube.com/watch?v=lAHqO9sDVy4', 'DNS Yapılandırma (CompTIA A+)', ['ücretsiz', 'video', 'sertifika'],
        'A+ sınavı kapsamındaki DNS yapılandırma konusu; kısa ve sınav odaklı.',
        'DNS configuration as covered by the A+ exam — short and exam-focused.', A)
    add('https://www.youtube.com/watch?v=5kt4t2gzt9g', 'Windows 11 Tam Rehber', ['ücretsiz', 'video', 'windows'],
        'Windows 11’in ayarlarını baştan sona gezen rehber; sistem yönetimi tarafında hızlı başvuru.',
        'A guide walking the whole of Windows 11’s settings — a quick reference on the sysadmin side.', A)
    add('https://servicedesk-simulator.com/', 'ServiceDesk Simulator', ['freemium', 'it destek', 'simülasyon'],
        'Yardım masası biletleriyle çalışmayı simüle eden ortam; teorik IT destek eğitimlerine karşı gerçek vaka pratiği sunar.',
        'Simulates working helpdesk tickets — real case practice against theoretical IT support courses.', A)
    add('https://www.hirensbootcd.org/', "Hiren's BootCD PE", ['ücretsiz', 'araç', 'kurtarma'],
        'Açılmayan sistemleri onarmak için kullanılan önyüklenebilir araç seti; disk, parola ve veri kurtarma araçlarını tek imajda toplar.',
        'A bootable toolkit for repairing systems that will not start, bundling disk, password and data recovery tools in one image.', A)
    add('https://www.disk-image.com/index.html', 'Active@ Disk Image', ['ücretli', 'araç', 'yedekleme'],
        'Disk imajı alma ve geri yükleme yazılımı; dosya yedeklemesinden farkı, sistemin tamamını bire bir kopyalaması.',
        'Disk imaging and restore software; unlike file backup it copies the entire system bit for bit.', A)
    add('https://www.cozumpark.com/', 'ÇözümPark', ['ücretsiz', 'türkçe', 'topluluk'],
        'Türkçe sistem yöneticiliği topluluğu ve makale arşivi; yerel senaryolar için nadir bulunan bir kaynak.',
        'A Turkish sysadmin community and article archive — a rare resource for locally specific scenarios.', A)
    add('https://www.nist.gov/cryptography', 'NIST Kriptografi', ['ücretsiz', 'standart', 'güvenlik'],
        'Kriptografi standartlarının kaynağı; hangi algoritmanın hâlâ güvenli sayıldığını blog yorumlarına değil buraya bakarak öğrenirsin.',
        'The source of cryptography standards — check here, not blog commentary, for which algorithms are still considered safe.', A)
    add('https://www.youtube.com/watch?v=0pXicD2hqFU', 'LFSR ve Rastgele Sayı Üreteçleri', ['ücretsiz', 'video', 'kriptografi'],
        'Doğrusal geri beslemeli kaydırma yazmaçlarının nasıl çalıştığını anlatan video; rastgelelik üretiminin donanım tarafına giriş.',
        'A video on how linear feedback shift registers work — an introduction to the hardware side of randomness generation.', A)

    # ============================================================ VERİ BİLİMİ & ML
    D = 'veri'
    add('https://www.kaggle.com/', 'Kaggle', ['ücretsiz', 'veri', 'yarışma'],
        'Veri bilimi yarışmaları, veri kümeleri ve not defterleri; çözümlerin açıkça paylaşılması onu en iyi öğrenme kaynaklarından biri yapıyor.',
        'Data science competitions, datasets and notebooks — open solution sharing makes it one of the best learning resources.', D)
    add('https://www.kaggle.com/competitions', 'Kaggle Yarışmaları', ['ücretsiz', 'veri', 'yarışma'],
        'Aktif ve geçmiş yarışmalar; gerçek problem ve gerçek değerlendirme ölçütüyle çalışma imkânı.',
        'Active and past competitions — a chance to work against real problems with real evaluation metrics.', D)
    add('https://www.kaggle.com/competitions/arc-prize-2026-paper-track', 'ARC Prize 2026', ['ücretsiz', 'araştırma', 'yarışma'],
        'Soyut akıl yürütme üzerine yarışma; mevcut modellerin en çok zorlandığı görev tipini hedeflemesiyle ayrışıyor.',
        'A competition on abstract reasoning, distinguished by targeting the task type current models struggle with most.', D)
    add('https://datasetsearch.research.google.com/', 'Google Dataset Search', ['ücretsiz', 'veri', 'arama'],
        'Web’deki açık veri kümelerini arayan motor; tek bir depoya bağlı olmayıp dağınık kaynakları tarıyor.',
        'A search engine for open datasets across the web, sweeping scattered sources rather than one repository.', D)
    add('https://www.databricks.com/', 'Databricks', ['ücretli', 'veri', 'platform'],
        'Büyük ölçekli veri ve ML platformu; veri gölü ile ambarı tek mimaride birleştirme iddiası temel ayrımı.',
        'Large-scale data and ML platform whose core claim is unifying data lake and warehouse in one architecture.', D)
    add('https://github.com/microsoft/Data-Science-For-Beginners/tree/main', 'Data Science for Beginners', ['ücretsiz', 'github', 'müfredat'],
        'Microsoft’un 20 derslik veri bilimi müfredatı; her ders proje ve sınavla geldiği için kendi kendine çalışmaya uygun.',
        'Microsoft’s 20-lesson data science curriculum; each lesson ships with a project and quiz, which suits self-study.', D)
    add('https://github.com/mrdbourke/zero-to-mastery-ml', 'Zero to Mastery ML', ['ücretsiz', 'github', 'not defteri'],
        'Uçtan uca makine öğrenmesi not defterleri; kavram anlatımı yerine çalışan hattı okutması ayırt edici.',
        'End-to-end machine learning notebooks — it has you read a working pipeline rather than concept prose.', D)
    add('https://github.com/rasbt/LLMs-from-scratch', 'LLMs from Scratch', ['ücretsiz', 'github', 'kitap'],
        'Dil modelini PyTorch ile adım adım sıfırdan yazan kitap deposu; kütüphane çağırmak yerine iç mekanizmayı kurdurması ayırt edici.',
        'Book repo building a language model from scratch in PyTorch — you construct the mechanism instead of calling a library.', D)
    add('https://github.com/FareedKhan-dev/train-llm-from-scratch', 'Train LLM from Scratch', ['ücretsiz', 'github'],
        'Veri indirmeden eğitime kadar LLM eğitim hattının tamamını gösteren depo; teorik anlatıma karşı çalışan kod.',
        'A repo showing the full LLM training pipeline from data download to training — working code against theory.', D)
    add('https://www.reddit.com/r/MachineLearningJobs/comments/1r5upkb/how_i_land_15_machine_learning_engineer_offers/', 'ML Mühendisi İş Bulma Deneyimi', ['ücretsiz', 'kariyer', 'topluluk'],
        'Makine öğrenmesi mühendisliği iş arama sürecini birinci elden anlatan başlık; genel kariyer tavsiyelerine karşı somut deneyim.',
        'A first-hand account of the ML engineering job hunt — concrete experience against generic career advice.', D)
