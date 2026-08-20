# -*- coding: utf-8 -*-
"""Web, Backend, Mobil, Veritabanı, DevOps, Ağ, Güvenlik, Veri"""


def load(add):
    # ============================================================ WEB & FRONTEND
    W = 'web'
    add('https://developer.mozilla.org/en-US/', 'MDN Web Docs', ['ücretsiz', 'referans', 'dokümantasyon'],
        'Web platformunun fiilî referansı; blog yazılarından farkı, tarayıcı uyumluluk tablolarıyla birlikte gelmesi.',
        'The de facto reference for the web platform; unlike blog posts it ships with browser compatibility tables.', W)
    add('https://javascript.info/', 'The Modern JavaScript Tutorial', ['ücretsiz', 'javascript'],
        'JavaScript’i temelden ileri seviyeye sıralı anlatan kaynak; MDN referans, bu ise öğretici olduğu için birbirini tamamlar.',
        'A sequential JavaScript course from basics to advanced; MDN is a reference, this is a tutorial, so they complement each other.', W)
    add('https://react.dev/learn', 'React', ['ücretsiz', 'dokümantasyon', 'javascript'],
        'React’in yeniden yazılmış resmî öğreticisi; eski dokümandan farkı, kancaları (hooks) merkeze alması.',
        'React’s rewritten official tutorial; unlike the old docs it puts hooks at the centre.', W)
    add('https://angular.dev/', 'Angular', ['ücretsiz', 'dokümantasyon'],
        'Angular’ın resmî sitesi; React’in aksine yönlendirme, form ve HTTP’yi çatının içinde vermesi temel farkı.',
        'Angular’s official site; the core difference from React is that routing, forms and HTTP ship inside the framework.', W)
    add('https://tailwindcss.com/docs/installation/using-vite', 'Tailwind CSS', ['ücretsiz', 'css', 'dokümantasyon'],
        'Yardımcı sınıf temelli CSS çatısı; Bootstrap’tan farkı hazır bileşen değil, kendi bileşenini kurmak için yapı taşı vermesi.',
        'Utility-first CSS framework; unlike Bootstrap it gives you building blocks to compose components rather than ready-made ones.', W)
    add('https://getbootstrap.com/docs/5.3/getting-started/introduction/', 'Bootstrap', ['ücretsiz', 'css', 'dokümantasyon'],
        'Hazır bileşenli klasik CSS çatısı; tasarım kararı vermeden hızlı arayüz kurmak isteyenler için hâlâ en kısa yol.',
        'The classic component-based CSS framework — still the shortest path to a UI when you would rather not make design decisions.', W)
    add('https://htmx.org/docs/', 'htmx', ['açık kaynak', 'javascript', 'dokümantasyon'],
        'HTML özniteliğiyle sunucudan parça güncelleyen kütüphane; SPA çatılarına karşı, JavaScript yazmadan etkileşim kurma yaklaşımı.',
        'Library that swaps server-rendered fragments via HTML attributes — the anti-SPA approach to interactivity without writing JavaScript.', W)
    add('https://htmlreference.io/', 'HTML Reference', ['ücretsiz', 'referans'],
        'Tüm HTML etiket ve özniteliklerinin görsel örnekli referansı; MDN’den farkı, hızlı göz gezdirmeye göre tasarlanmış olması.',
        'A visual reference of every HTML element and attribute; unlike MDN it is designed for fast scanning.', W)
    add('https://css-tricks.com/', 'CSS-Tricks', ['ücretsiz', 'css'],
        'CSS teknikleri ve düzen çözümleri arşivi; belirli bir düzen problemini aradığında dokümandan daha hızlı sonuç verir.',
        'An archive of CSS techniques and layout solutions — faster than the spec when you are hunting a specific layout problem.', W)
    add('https://cssgridgarden.com/', 'Grid Garden', ['ücretsiz', 'oyun', 'css'],
        'CSS Grid’i oyunla öğreten alıştırma; doküman okumaya karşı, özelliği yazarak öğrenme yolu.',
        'A game that teaches CSS Grid — learning the property by typing it rather than reading the spec.', W)
    add('https://flexboxfroggy.com/', 'Flexbox Froggy', ['ücretsiz', 'oyun', 'css'],
        'Flexbox’ı oyunla öğreten alıştırma; Grid Garden’ın kardeşi, hizalama kavramlarını oturtmak için en hızlı yol.',
        'A game that teaches Flexbox — sibling to Grid Garden and the fastest way to internalise alignment concepts.', W)
    add('https://validator.w3.org/', 'W3C Markup Validation', ['ücretsiz', 'araç'],
        'HTML’i standarda göre denetleyen resmî doğrulayıcı; tarayıcının sessizce düzelttiği hataları görünür kılar.',
        'The official validator checking HTML against the standard, surfacing errors browsers silently correct.', W)
    add('https://fonts.google.com/?preview.script=Latn', 'Google Fonts', ['ücretsiz', 'tipografi'],
        'Ücretsiz ve açık lisanslı yazı tipi kataloğu; lisans derdi olmadan kullanılabilmesi başlıca sebebi.',
        'Catalogue of free, openly licensed typefaces — usable without licensing friction, which is the main reason to reach for it.', W)
    add('https://grapesjs.com/', 'GrapesJS', ['açık kaynak', 'editör'],
        'Kendi ürününe gömülebilen görsel sayfa düzenleyici; hazır site kurucularından farkı, sen kendi editörünü kurarsın.',
        'An embeddable visual page editor; unlike hosted site builders, you build your own editor with it.', W)
    add('https://github.com/microsoft/web-dev-for-beginners', 'Web Dev for Beginners', ['ücretsiz', 'github', 'müfredat'],
        'Microsoft’un 24 derslik web geliştirme müfredatı; her ders öncesi ve sonrası sınavla ilerlemeyi ölçmesi ayırt edici.',
        'Microsoft’s 24-lesson web development curriculum, distinguished by pre- and post-lesson quizzes that measure progress.', W)
    add('https://shopify.dev/docs/api/liquid', 'Shopify Liquid', ['dokümantasyon', 'e-ticaret'],
        'Shopify tema şablon dilinin referansı; mağaza teması geliştirenler için birincil kaynak.',
        'Reference for Shopify’s theme templating language — the primary source for store theme development.', W)
    add('https://www.unsection.com/', 'Unsection', ['ücretsiz', 'tasarım', 'ilham'],
        'Bölüm bazlı web tasarımı örnekleri (hero, fiyatlandırma, CTA); tüm siteyi değil tek bir bölümü çözmek için.',
        'Web design examples organised by section (hero, pricing, CTA) — for solving one section rather than a whole site.', W)
    add('https://www.siteofsites.co/', 'Site of Sites', ['ücretsiz', 'tasarım', 'ilham'],
        'Öne çıkan web tasarımlarının derlendiği galeri; bütünsel tasarım dili örnekleri için.',
        'A gallery of standout web designs, useful for whole-site design language examples.', W)
    add('https://before.click/', 'before.click', ['ücretsiz', 'tasarım', 'mobil'],
        'App Store ekran görüntüsü tasarımlarının arşivi; uygulama mağaza sayfası hazırlarken dar ama isabetli bir kaynak.',
        'An archive of App Store screenshot designs — narrow but precisely useful when preparing a store listing.', W)
    add('https://www.gameuidatabase.com/', 'Game UI Database', ['ücretsiz', 'tasarım', 'oyun'],
        'Oyun arayüzlerinin ekran bazında sınıflandırılmış arşivi; menü, envanter gibi ekran türüne göre aranabilmesi ayırt edici.',
        'A screen-by-screen archive of game interfaces, searchable by screen type such as menu or inventory.', W)
    add('https://www.cagrigungor.com/seo-kriterleri/', 'SEO Kriterleri', ['ücretsiz', 'türkçe', 'seo'],
        'Teknik SEO kontrol listesi; Türkçe kaynaklar arasında derli toplu ve uygulanabilir olanlardan.',
        'A technical SEO checklist — one of the tidier, more actionable Turkish-language resources.', W)
    add('https://mapstracker.com/', 'Maps Tracker', ['ücretli', 'seo', 'yerel'],
        'Google Haritalar’da yerel sıralama takibi; genel SEO araçlarının zayıf kaldığı çok konumlu işletmeler için.',
        'Local rank tracking on Google Maps — aimed at multi-location businesses where general SEO tools are weak.', W)

    # ============================================================ BACKEND & SİSTEM TASARIMI
    B = 'backend'
    add('https://fastapi.tiangolo.com/', 'FastAPI', ['açık kaynak', 'python', 'dokümantasyon'],
        'Tip ipuçlarından otomatik doğrulama ve API dokümanı üreten Python çatısı; Flask’tan temel farkı bu otomatizm.',
        'Python framework deriving validation and API docs from type hints — that automation is the core difference from Flask.', B)
    add('https://flask.palletsprojects.com/en/stable/', 'Flask', ['açık kaynak', 'python', 'dokümantasyon'],
        'Minimal Python web çatısı; Django’nun aksine ne kullanacağına sen karar verirsin, çekirdek kasten küçük tutulmuştur.',
        'Minimal Python web framework; unlike Django you choose the pieces, because the core is deliberately small.', B)
    add('https://docs.djangoproject.com/en/6.0/', 'Django', ['açık kaynak', 'python', 'dokümantasyon'],
        'Yönetim paneli, ORM ve kimlik doğrulamayı hazır getiren Python çatısı; hız kazandırır, esneklikten bir miktar götürür.',
        'Python framework shipping an admin panel, ORM and auth out of the box — it buys speed at some cost in flexibility.', B)
    add('https://expressjs.com/', 'Express', ['açık kaynak', 'javascript', 'dokümantasyon'],
        'Node.js’in en yaygın minimal web çatısı; ara katman (middleware) modelini standartlaştırdığı için ekosistemin ortak zemini.',
        'Node.js’s most widespread minimal web framework — its middleware model became the ecosystem’s common ground.', B)
    add('https://nodejs.org/learn', 'Node.js Learn', ['ücretsiz', 'dokümantasyon', 'javascript'],
        'Node.js’in resmî öğrenme bölümü; çatı öğretmeden önce çalışma zamanının kendisini anlatması değerli.',
        'Node.js’s official learning section — valuable because it explains the runtime itself before any framework.', B)
    add('https://laravel.com/docs/13.x', 'Laravel', ['açık kaynak', 'php', 'dokümantasyon'],
        'PHP’nin en yaygın modern çatısı; kuyruğa alma, zamanlama ve test araçlarını çekirdekte sunması ayırt edici yanı.',
        'PHP’s most widespread modern framework, distinguished by shipping queues, scheduling and testing in the core.', B)
    add('https://laracasts.com/', 'Laracasts', ['ücretli', 'php', 'video'],
        'Laravel ekosisteminin ana video eğitim kaynağı; resmî dokümanın anlatmadığı pratik desenler için.',
        'The main video training source for the Laravel ecosystem, covering practical patterns the docs leave out.', B)
    add('https://www.php.net/manual/tr/', 'PHP El Kitabı (Türkçe)', ['ücretsiz', 'türkçe', 'php'],
        'PHP’nin resmî Türkçe kılavuzu; fonksiyon referansı için birincil kaynak.',
        'PHP’s official Turkish manual — the primary source for function reference.', B)
    add('https://phptherightway.com/', 'PHP: The Right Way', ['ücretsiz', 'php', 'rehber'],
        'Güncel PHP pratiklerini derleyen rehber; internetteki eski ve güvensiz PHP örneklerine karşı düzeltici bir kaynak.',
        'A guide to current PHP practice — a corrective to the outdated, insecure PHP examples scattered across the web.', B)
    add('https://developer.wordpress.org/', 'WordPress Developer', ['ücretsiz', 'dokümantasyon'],
        'WordPress eklenti ve tema geliştirme referansı; kanca (hook) sistemini anlamak için birincil kaynak.',
        'Reference for WordPress plugin and theme development — the primary source for understanding the hook system.', B)
    add('https://graphql.org/', 'GraphQL', ['açık kaynak', 'api', 'dokümantasyon'],
        'İstemcinin istediği alanı seçtiği sorgu dili; REST’ten farkı, fazla veri çekme sorununu şema düzeyinde çözmesi.',
        'A query language where the client picks the fields; unlike REST it solves over-fetching at the schema level.', B)
    add('https://github.com/donnemartin/system-design-primer', 'System Design Primer', ['ücretsiz', 'github', 'sistem tasarımı'],
        'Sistem tasarımı mülakatlarının en yaygın çalışma kaynağı; kavramları örnek mimarilerle birlikte vermesi ayırt edici.',
        'The most common study resource for system design interviews, pairing concepts with worked example architectures.', B)
    add('https://systemdesign.one/', 'System Design One', ['ücretsiz', 'sistem tasarımı'],
        'Gerçek şirket mimarilerini vaka çalışması olarak inceleyen kaynak; teorik anlatımlara karşı somut örnek sunar.',
        'Case studies of real company architectures — concrete examples against the usual theoretical write-ups.', B)
    add('https://highscalability.com/', 'High Scalability', ['ücretsiz', 'sistem tasarımı', 'arşiv'],
        'Büyük ölçekli sistem mimarilerinin uzun süredir tutulan arşivi; sektörün ölçeklenme tarihini görmek için değerli.',
        'A long-running archive of large-scale system architectures — valuable for seeing how scaling practice evolved.', B)
    add('https://refactoring.guru/', 'Refactoring Guru', ['freemium', 'tasarım deseni'],
        'Tasarım desenleri ve yeniden düzenleme tekniklerini görselle anlatan kaynak; kitaplardan farkı, her deseni birden çok dilde kodla göstermesi.',
        'Design patterns and refactoring techniques explained visually; unlike the books it shows each pattern in several languages.', B)
    add('https://github.com/public-apis/public-apis', 'Public APIs', ['ücretsiz', 'github', 'koleksiyon', 'api'],
        'Herkese açık ücretsiz API’lerin kategorili listesi; proje fikri ararken veya prototipe veri lazım olduğunda ilk durak.',
        'A categorised list of free public APIs — the first stop when hunting a project idea or data for a prototype.', B)
    add('https://github.com/public-api-lists/public-api-lists', 'Public API Lists', ['ücretsiz', 'github', 'koleksiyon', 'api'],
        'Public APIs listesinin sürdürülen bir çatalı; kimlik doğrulama ve CORS bilgisini tabloda göstermesi pratik.',
        'A maintained fork of the Public APIs list, practical for showing auth and CORS support in the table.', B)
    add('https://stripe.com/en-nl?utm_campaign=EMEA_NL_en_Google_Search_Brand_Stripe_EXA-20981195258&utm_medium=cpc&utm_source=google&utm_content=689219303694&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c', 'Stripe', ['ücretli', 'ödeme', 'api'],
        'Ödeme altyapısı; geliştirici dokümantasyonunun kalitesi sektörde referans kabul edilir.',
        'Payment infrastructure whose developer documentation is treated as an industry reference point.', B)
    add('https://www.youtube.com/watch?v=XvFmUE-36Kc', 'API Tasarımı ve Mimarisi', ['ücretsiz', 'video', 'api'],
        'Backend mühendisliğine bir saatlik giriş; API tasarım kararlarını gerekçeleriyle anlatıyor.',
        'A one-hour introduction to backend engineering, covering API design decisions with their reasoning.', B)
    add('https://www.youtube.com/watch?v=7iHl71nt49o', 'Kıdemli Mühendis Gibi API Tasarımı', ['ücretsiz', 'video', 'api'],
        'REST, GraphQL, kimlik doğrulama ve güvenliği tek videoda karşılaştıran anlatım.',
        'A single video comparing REST, GraphQL, authentication and security.', B)
    add('https://www.youtube.com/watch?v=bA0r0CBuj2Y', 'Otel Rezervasyon Sistemi Tasarımı', ['ücretsiz', 'video', 'sistem tasarımı'],
        'Uçtan uca sistem tasarımı vaka çalışması; mülakat formatında düşünme sürecini gösteriyor.',
        'An end-to-end system design case study, showing the thinking process in interview format.', B)
    add('https://www.youtube.com/watch?v=adOkTjIIDnk', 'Sistem Tasarımı Anlatımı', ['ücretsiz', 'video', 'sistem tasarımı'],
        'API, veritabanı, önbellek, CDN ve yük dengeleme kavramlarını tek videoda toplayan giriş.',
        'An introduction gathering APIs, databases, caching, CDNs and load balancing into one video.', B)

    # ============================================================ MOBİL & MASAÜSTÜ
    M = 'mobil'
    add('https://docs.flutter.dev/learn', 'Flutter', ['açık kaynak', 'dokümantasyon', 'mobil'],
        'Tek kod tabanından mobil, web ve masaüstü üreten çatı; React Native’den farkı, platform bileşenlerini kullanmak yerine kendi çizim motorunu kullanması.',
        'Framework producing mobile, web and desktop from one codebase; unlike React Native it draws its own widgets instead of using platform components.', M)
    add('https://docs.expo.dev/', 'Expo', ['açık kaynak', 'dokümantasyon', 'mobil'],
        'React Native geliştirmeyi yerel derleme zincirinden kurtaran araç seti; kurulum yükünü kaldırması başlıca avantajı.',
        'Toolchain freeing React Native development from native build setup — removing that burden is its main advantage.', M)
    add('https://www.electronjs.org/', 'Electron', ['açık kaynak', 'masaüstü'],
        'Web teknolojileriyle masaüstü uygulaması üreten çatı; kolaylık karşılığında yüksek bellek kullanımıyla eleştiriliyor.',
        'Framework building desktop apps with web technology — criticised for high memory use in exchange for the convenience.', M)
    add('https://www.electronjs.org/docs/latest', 'Electron Dokümantasyonu', ['dokümantasyon', 'masaüstü'],
        'Electron’un ana süreç ve işleyici süreç ayrımını anlatan resmî referans; güvenlik ayarları için birincil kaynak.',
        'Official reference explaining Electron’s main and renderer process split — the primary source for its security settings.', M)
    add('https://rive.app/docs/runtimes/flutter/flutter', 'Rive (Flutter)', ['freemium', 'animasyon', 'mobil'],
        'Etkileşimli vektör animasyonlarını uygulamaya gömme aracı; Lottie’den farkı, animasyonun duruma göre tepki verebilmesi.',
        'Embeds interactive vector animation into apps; unlike Lottie the animation can react to state.', M)

