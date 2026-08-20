# -*- coding: utf-8 -*-
"""Web & Frontend · Backend, API & Sistem Tasarımı · Mobil & Masaüstü"""


def load(add):
    # ============================================================ WEB & FRONTEND
    W = 'web'
    add('https://developer.mozilla.org/en-US/', 'MDN Web Docs', ['ücretsiz', 'referans', 'dokümantasyon'],
        'Web platformunun fiilî referansı. Her sayfada tarayıcı uyumluluk tablosu var — '
        'bir özelliği kullanmadan önce Safari’de çalışıp çalışmadığını burada görürsün.',
        'The de facto reference for the web platform. Every page carries a browser compatibility table, '
        'which is where you check whether a feature works in Safari before shipping it.', W)
    add('https://javascript.info/', 'The Modern JavaScript Tutorial', ['ücretsiz', 'javascript', 'öğretici'],
        'Dili temelden ileriye sıralı işliyor; prototip zinciri, olay döngüsü ve Promise gibi '
        'zor konuları atlamıyor. MDN referanstır, bu öğreticidir — ikisi birbirini tamamlar.',
        'Works the language front to back without skipping the hard parts: prototype chain, event loop, promises. '
        'MDN is the reference and this is the tutorial; they complement each other.', W)
    add('https://react.dev/learn', 'React', ['ücretsiz', 'dokümantasyon', 'javascript'],
        'Yeniden yazılmış resmî doküman; kancalar (hooks) merkezde, sınıf bileşenleri artık yok. '
        '“You Might Not Need an Effect” bölümü en sık yapılan hatayı doğrudan hedefliyor.',
        'The rewritten official docs, centred on hooks with class components gone. '
        'The “You Might Not Need an Effect” page targets the single most common mistake head on.', W)
    add('https://angular.dev/', 'Angular', ['ücretsiz', 'dokümantasyon', 'typescript'],
        'Yönlendirme, form, HTTP ve bağımlılık enjeksiyonu çatının içinde geliyor. '
        'React’te bunları tek tek seçersin; burada karar verilmiş, karşılığında esneklik dar.',
        'Routing, forms, HTTP and dependency injection ship inside the framework. In React you pick each one; '
        'here the decisions are made for you, and flexibility narrows accordingly.', W)
    add('https://tailwindcss.com/docs/installation/using-vite', 'Tailwind CSS', ['ücretsiz', 'css', 'dokümantasyon'],
        'Yardımcı sınıflarla stil yazıyorsun; derleme adımı kullanılmayan sınıfları atıyor, '
        'CSS dosyası büyümüyor. Bootstrap hazır bileşen verir, bu yapı taşı verir.',
        'You style with utility classes and the build step drops unused ones, so the CSS file stops growing. '
        'Bootstrap hands you components; this hands you building blocks.', W)
    add('https://getbootstrap.com/docs/5.3/getting-started/introduction/', 'Bootstrap', ['ücretsiz', 'css', 'bileşen'],
        'Hazır bileşenler ve ızgara sistemi; tasarım kararı vermeden çalışan bir arayüz çıkarıyorsun. '
        'Bedeli, Bootstrap kullandığının uzaktan belli olması.',
        'Ready components and a grid system that get you a working interface without design decisions. '
        'The cost is that a Bootstrap site is recognisable from a distance.', W)
    add('https://htmx.org/docs/', 'htmx', ['açık-kaynak', 'javascript', 'hypermedia'],
        'HTML özniteliğiyle istek atıp dönen HTML parçasını sayfaya yerleştiriyorsun; JSON ve istemci '
        'durumu yok. 14 kB, bağımlılığı yok — SPA karmaşıklığına gerek olmayan yerde makul bir çıkış.',
        'Attributes fire requests and swap the returned HTML fragment into the page — no JSON, no client state. '
        '14 kB with no dependencies, and a sane exit where SPA complexity is not warranted.', W)
    add('https://htmlreference.io/', 'HTML Reference', ['ücretsiz', 'referans'],
        'Her HTML etiketi ve özniteliği görsel örnekle listelenmiş, tek sayfada göz gezdirilebiliyor. '
        'MDN’in derinliği yok ama “bu etiket ne yapıyordu” sorusuna daha hızlı cevap veriyor.',
        'Every HTML element and attribute with a visual example, scannable on one page. '
        'It lacks MDN’s depth but answers “what did this tag do again” faster.', W)
    add('https://css-tricks.com/', 'CSS-Tricks', ['ücretsiz', 'css', 'arşiv'],
        'Yirmi yıllık CSS tekniği arşivi; Flexbox ve Grid rehberleri fiilî başvuru kaynağı hâline geldi. '
        'Belirli bir düzen problemi ararken spesifikasyondan hızlı sonuç veriyor.',
        'Two decades of CSS technique, whose Flexbox and Grid guides became the de facto references. '
        'Faster than the spec when you are hunting a specific layout problem.', W)
    add('https://cssgridgarden.com/', 'Grid Garden', ['ücretsiz', 'oyun', 'css'],
        'Havuç sulayarak CSS Grid öğreten 28 bölümlük oyun. '
        'grid-column ve grid-area gibi özellikler yazarak öğrenildiğinde akılda kalıyor.',
        'A 28-level game teaching CSS Grid by watering carrots. Properties like grid-column and grid-area stick '
        'when you type them rather than read them.', W)
    add('https://flexboxfroggy.com/', 'Flexbox Froggy', ['ücretsiz', 'oyun', 'css'],
        'Kurbağaları hizalayarak Flexbox öğreten oyun; Grid Garden’ın kardeşi. '
        'justify-content ile align-items karışıklığını yirmi dakikada bitiriyor.',
        'The Flexbox sibling of Grid Garden, teaching alignment by positioning frogs. '
        'It settles the justify-content versus align-items confusion in twenty minutes.', W)
    add('https://validator.w3.org/', 'W3C Markup Validation', ['ücretsiz', 'araç', 'standart'],
        'HTML’i spesifikasyona göre denetliyor; tarayıcının sessizce toparladığı kapatılmamış etiket ve '
        'geçersiz iç içe geçmeleri ortaya çıkarıyor. Erişilebilirlik sorunlarının bir kısmı buradan çıkar.',
        'Checks HTML against the spec, surfacing unclosed tags and invalid nesting that browsers quietly repair. '
        'A share of accessibility problems begins right there.', W)
    add('https://fonts.google.com/?preview.script=Latn', 'Google Fonts', ['ücretsiz', 'tipografi'],
        'Açık lisanslı yazı tipi kataloğu; dosyaları indirip kendi sunucundan servis edebiliyorsun. '
        'GDPR gerekçesiyle CDN’den çekmek Almanya’da dava konusu oldu, indirmek daha güvenli.',
        'A catalogue of openly licensed typefaces you can download and self-host. Loading them from the CDN has been '
        'litigated in Germany on GDPR grounds, so self-hosting is the safer route.', W)
    add('https://grapesjs.com/', 'GrapesJS', ['açık-kaynak', 'editör', 'javascript'],
        'Kendi ürününe gömdüğün görsel sayfa düzenleyici; bileşen ve stil yöneticisini sen tanımlıyorsun. '
        'Barındırılan site kurucularının aksine editörün sahibi sensin.',
        'A visual page editor you embed in your own product, defining the component and style managers yourself. '
        'Unlike hosted site builders, you own the editor.', W)
    add('https://github.com/microsoft/web-dev-for-beginners', 'Web Dev for Beginners', ['github', 'müfredat', 'ücretsiz'],
        '24 derslik müfredat; her ders öncesi ve sonrası sınav, sonunda proje var. '
        'Kendi kendine çalışırken ilerlemeyi ölçebilmek için bu yapı işe yarıyor.',
        'A 24-lesson curriculum with a quiz before and after each lesson and a project at the end. '
        'That structure is what lets you measure progress when studying alone.', W)
    add('https://shopify.dev/docs/api/liquid', 'Shopify Liquid', ['dokümantasyon', 'e-ticaret', 'şablon'],
        'Shopify tema şablon dilinin nesne, filtre ve etiket referansı. '
        'Mağaza teması geliştiriyorsan hangi verinin hangi şablonda erişilebilir olduğu buradan görülüyor.',
        'The object, filter and tag reference for Shopify’s theme language — where you find which data is '
        'reachable from which template when building a store theme.', W)
    add('https://www.unsection.com/', 'Unsection', ['ücretsiz', 'tasarım', 'ilham'],
        'Bölüm bazlı tasarım örnekleri: hero, fiyatlandırma, SSS, footer ayrı ayrı. '
        'Tüm siteyi taramak yerine tek bir bölümü çözmek için filtreleyebiliyorsun.',
        'Design examples organised by section — hero, pricing, FAQ, footer — filterable so you solve one section '
        'instead of scanning whole sites.', W)
    add('https://www.siteofsites.co/', 'Site of Sites', ['ücretsiz', 'tasarım', 'ilham'],
        'Bütünsel tasarım dili örnekleri için galeri; tipografi ve hareket kullanımı güçlü siteler derleniyor.',
        'A gallery for whole-site design language, collecting sites with strong typography and motion.', W)
    add('https://before.click/', 'before.click', ['ücretsiz', 'tasarım', 'mobil'],
        'App Store ekran görüntüsü tasarımları arşivi. Uygulama mağaza sayfası dönüşümü doğrudan '
        'bu görsellere bağlı olduğu için dar ama isabetli bir kaynak.',
        'An archive of App Store screenshot designs. Store-page conversion hangs directly on these images, '
        'which makes it a narrow but well-aimed resource.', W)
    add('https://www.gameuidatabase.com/', 'Game UI Database', ['ücretsiz', 'tasarım', 'oyun'],
        'Oyun arayüzlerini ekran türüne göre sınıflandırıyor: envanter, harita, ayarlar, yükleme ekranı. '
        'Bu kadar sistematik bir arayüz arşivi başka alanlarda yok.',
        'Classifies game interfaces by screen type — inventory, map, settings, loading. '
        'No other field has an interface archive this systematic.', W)
    add('https://www.cagrigungor.com/seo-kriterleri/', 'SEO Kriterleri', ['ücretsiz', 'türkçe', 'seo'],
        'Teknik SEO kontrol listesi; başlık yapısı, şema işaretlemesi ve sayfa hızı maddeleri uygulanabilir. '
        'Türkçe kaynaklar arasında pazarlama söyleminden en uzak duranlardan.',
        'A technical SEO checklist covering heading structure, schema markup and page speed in actionable terms — '
        'one of the Turkish resources furthest from marketing talk.', W)
    add('https://mapstracker.com/', 'Maps Tracker', ['saas', 'ücretli', 'seo', 'yerel'],
        'Google Haritalar sıralamasını konum ızgarası üzerinde ölçüyor; aynı sorgunun mahalleden mahalleye '
        'nasıl değiştiğini gösteriyor. Genel SEO araçlarının kör noktası tam olarak burası.',
        'Measures Google Maps ranking across a grid of locations, showing how the same query shifts block by block — '
        'precisely the blind spot of general SEO tools.', W)

    # ============================================================ BACKEND & SİSTEM TASARIMI
    B = 'backend'
    add('https://fastapi.tiangolo.com/', 'FastAPI', ['açık-kaynak', 'python', 'async', 'openapi'],
        'Tip ipuçlarından hem doğrulama hem OpenAPI şeması üretiyor; `/docs` adresinde çalışan bir '
        'test arayüzü kendiliğinden geliyor. Asenkron desteği ASGI üzerinden yerleşik.',
        'Derives both validation and an OpenAPI schema from type hints, and a working test UI appears at `/docs` '
        'by itself. Async support is native through ASGI.', B)
    add('https://flask.palletsprojects.com/en/stable/', 'Flask', ['açık-kaynak', 'python', 'mikro-çatı'],
        'Çekirdek kasten küçük: yönlendirme ve şablon var, ORM ve kimlik doğrulama yok. '
        'Ne kullanacağına sen karar veriyorsun, bu da her projede yeniden karar vermek anlamına geliyor.',
        'A deliberately small core — routing and templating, no ORM or auth. You choose the pieces, '
        'which also means choosing them again on every project.', B)
    add('https://docs.djangoproject.com/en/6.0/', 'Django', ['açık-kaynak', 'python', 'orm', 'batteries-included'],
        'ORM, göç sistemi, yönetim paneli ve kimlik doğrulama kutudan çıkıyor. '
        'İlk haftayı kazandırıyor; Django’nun kalıbı dışına çıkmak istediğinde direnç gösteriyor.',
        'ORM, migrations, admin panel and authentication out of the box. It buys you the first week, '
        'and pushes back when you want to step outside its shape.', B)
    add('https://expressjs.com/', 'Express', ['açık-kaynak', 'javascript', 'node'],
        'Node.js’in minimal çatısı; ara katman (middleware) modelini standartlaştırdığı için '
        'ekosistemin ortak dili hâline geldi. Yıllardır neredeyse hiç değişmemesi hem güç hem zayıflık.',
        'Node’s minimal framework, whose middleware model became the ecosystem’s shared vocabulary. '
        'That it has barely changed in years is both its strength and its weakness.', B)
    add('https://nodejs.org/learn', 'Node.js Learn', ['ücretsiz', 'dokümantasyon', 'javascript'],
        'Çatı öğretmeden önce çalışma zamanının kendisini anlatıyor: olay döngüsü, akışlar, '
        'işçi iş parçacıkları. Express öğrenip Node bilmemek yaygın bir boşluk.',
        'Explains the runtime itself before any framework — event loop, streams, worker threads. '
        'Learning Express without knowing Node is a common gap.', B)
    add('https://laravel.com/docs/13.x', 'Laravel', ['açık-kaynak', 'php', 'orm'],
        'Kuyruk, zamanlayıcı, olay yayını ve test araçları çekirdekte. '
        'PHP’nin “eski dil” imajının aksine burada kurulan geliştirici deneyimi çoğu modern çatının üstünde.',
        'Queues, scheduler, broadcasting and testing tools live in the core. Against PHP’s dated reputation, '
        'the developer experience here is ahead of most modern frameworks.', B)
    add('https://laracasts.com/', 'Laracasts', ['ücretli', 'php', 'video'],
        'Laravel ekosisteminin ana video kaynağı; resmî dokümanın anlatmadığı mimari kararları işliyor. '
        'Ekosistem eğitimini tek bir sitenin taşıması alışılmadık bir durum.',
        'The main video resource for the Laravel ecosystem, covering the architectural decisions the docs leave out. '
        'One site carrying an ecosystem’s training is unusual.', B)
    add('https://www.php.net/manual/tr/', 'PHP El Kitabı (Türkçe)', ['ücretsiz', 'türkçe', 'php', 'referans'],
        'Fonksiyon referansı için birincil kaynak. Sayfa altındaki kullanıcı yorumları bazen '
        'dokümanın kendisinden faydalı, bazen on yıllık kötü tavsiye — tarihe bakmak gerekiyor.',
        'The primary function reference. The user notes below each page are sometimes more useful than the doc '
        'and sometimes decade-old bad advice — check the dates.', B)
    add('https://phptherightway.com/', 'PHP: The Right Way', ['ücretsiz', 'php', 'rehber'],
        'Güncel PHP pratiklerini derliyor: Composer, PSR standartları, hazırlanmış sorgular. '
        'İnternette dolaşan `mysql_*` fonksiyonlu eski örneklere karşı düzeltici bir metin.',
        'Collects current PHP practice — Composer, PSR standards, prepared statements. '
        'A corrective to the old `mysql_*` examples still circulating online.', B)
    add('https://developer.wordpress.org/', 'WordPress Developer', ['ücretsiz', 'php', 'dokümantasyon'],
        'Eklenti ve tema geliştirme referansı. Kanca (hook) sistemi WordPress’in tamamını açıklayan '
        'tek kavram; onu anlamadan hiçbir şey yerine oturmuyor.',
        'The plugin and theme development reference. The hook system is the one concept that explains all of '
        'WordPress, and nothing falls into place until you have it.', B)
    add('https://graphql.org/', 'GraphQL', ['açık-kaynak', 'api', 'şema'],
        'İstemci hangi alanları istediğini kendi belirtiyor; fazla veri çekme ve az veri çekme sorunu '
        'şema düzeyinde çözülüyor. Bedeli önbellekleme ve hız sınırlamanın REST’ten zor olması.',
        'The client declares which fields it wants, so over- and under-fetching are solved at the schema level. '
        'The cost is that caching and rate limiting get harder than in REST.', B)
    add('https://github.com/donnemartin/system-design-primer', 'System Design Primer', ['github', 'sistem-tasarımı', 'mülakat'],
        'Ölçekleme kavramlarını (önbellek, parçalama, kuyruk, CAP) örnek mimarilerle birlikte veriyor. '
        'Alanın en çok yıldızlanan kaynağı; mülakat dışında da mimari sözlüğü olarak işe yarıyor.',
        'Pairs scaling concepts — caching, sharding, queues, CAP — with worked architectures. '
        'The field’s most-starred resource, and useful as an architecture vocabulary beyond interviews.', B)
    add('https://systemdesign.one/', 'System Design One', ['ücretsiz', 'sistem-tasarımı', 'vaka'],
        'Gerçek şirketlerin mimarisini vaka çalışması olarak çözümlüyor; sayısal büyüklükler ve '
        'yapılan takasları veriyor. Soyut anlatımlardan bu somutluk ayırıyor.',
        'Breaks down real company architectures as case studies with actual numbers and the trade-offs taken. '
        'That concreteness is what separates it from abstract write-ups.', B)
    add('https://highscalability.com/', 'High Scalability', ['ücretsiz', 'sistem-tasarımı', 'arşiv'],
        'On beş yılı aşkın mimari yazısı arşivi. Eski yazılar teknoloji olarak eskimiş olsa da '
        'ölçekleme baskısının nasıl karşılandığını görmek için hâlâ okunuyor.',
        'An archive of architecture write-ups spanning fifteen-plus years. The old posts are dated in technology '
        'but still read for how scaling pressure was actually met.', B)
    add('https://refactoring.guru/', 'Refactoring Guru', ['freemium', 'tasarım-deseni', 'refactoring'],
        'Her tasarım desenini şema, gerçekçi örnek ve kod olarak veriyor — üstelik altı ayrı dilde. '
        'Gang of Four kitabının okunması güç metnine karşı erişilebilir bir karşılık.',
        'Presents each design pattern as a diagram, a realistic scenario and code — in six languages. '
        'An accessible counterpart to the Gang of Four book’s difficult prose.', B)
    add('https://github.com/public-apis/public-apis', 'Public APIs', ['github', 'awesome-liste', 'api'],
        'Kategorili ücretsiz API listesi; kimlik doğrulama türü, HTTPS ve CORS desteği tabloda işaretli. '
        'Prototipe veri lazım olduğunda ilk durak.',
        'A categorised list of free APIs with auth type, HTTPS and CORS support marked in the table. '
        'First stop when a prototype needs data.', B)
    add('https://github.com/public-api-lists/public-api-lists', 'Public API Lists', ['github', 'awesome-liste', 'api'],
        'Public APIs’in sürdürülen çatalı. Asıl depo bir dönem bakımsız kaldığında ortaya çıktı; '
        'bazı girdileri daha güncel.',
        'A maintained fork of Public APIs, born while the original went untended. Some of its entries are fresher.', B)
    add('https://stripe.com/en-nl?utm_campaign=EMEA_NL_en_Google_Search_Brand_Stripe_EXA-20981195258&utm_medium=cpc&utm_source=google&utm_content=689219303694&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c', 'Stripe', ['saas', 'ücretli', 'ödeme', 'api'],
        'Ödeme altyapısı. Dokümantasyonu sektörde ölçüt kabul ediliyor — test kartları, webhook '
        'yeniden deneme mantığı ve idempotency anahtarları örneklerle anlatılmış.',
        'Payment infrastructure whose documentation is treated as an industry benchmark — test cards, '
        'webhook retry logic and idempotency keys all worked through with examples.', B)
    add('https://www.youtube.com/watch?v=XvFmUE-36Kc', 'API Tasarımı ve Mimarisi', ['video', 'ücretsiz', 'api'],
        'Bir saatlik backend giriş anlatımı; kaynak adlandırma, sürümleme ve hata biçimi '
        'kararlarını gerekçeleriyle işliyor.',
        'An hour-long backend introduction working through resource naming, versioning and error-format decisions '
        'with their reasoning.', B)
    add('https://www.youtube.com/watch?v=7iHl71nt49o', 'Kıdemli Mühendis Gibi API Tasarımı', ['video', 'ücretsiz', 'api'],
        'REST ile GraphQL’i, kimlik doğrulama ve güvenlik kararlarını tek videoda karşılaştırıyor. '
        'Hangisinin ne zaman doğru olduğu sorusuna cevap veriyor.',
        'Compares REST against GraphQL alongside authentication and security decisions in one video, '
        'answering when each is the right call.', B)
    add('https://www.youtube.com/watch?v=bA0r0CBuj2Y', 'Otel Rezervasyon Sistemi Tasarımı', ['video', 'sistem-tasarımı'],
        'Uçtan uca vaka çalışması; eşzamanlı rezervasyon çakışması ve envanter kilitleme gibi '
        'gerçek problemleri mülakat formatında çözüyor.',
        'An end-to-end case study solving real problems — concurrent booking conflicts, inventory locking — '
        'in interview format.', B)
    add('https://www.youtube.com/watch?v=adOkTjIIDnk', 'Sistem Tasarımı Anlatımı', ['video', 'sistem-tasarımı'],
        'API, veritabanı, önbellek, CDN ve yük dengeleyiciyi tek anlatımda birleştiren giriş. '
        'Parçaların birbirine nasıl bağlandığını görmek için.',
        'An introduction gathering APIs, databases, caching, CDNs and load balancers into one narrative — '
        'for seeing how the pieces connect.', B)

    # ============================================================ MOBİL & MASAÜSTÜ
    M = 'mobil'
    add('https://docs.flutter.dev/learn', 'Flutter', ['açık-kaynak', 'dart', 'mobil', 'masaüstü'],
        'Skia/Impeller ile her pikseli kendisi çiziyor; platform bileşeni kullanmıyor. '
        'Bu yüzden iOS ve Android’de birebir aynı görünüyor — istediğin buysa güç, değilse sorun.',
        'Draws every pixel itself through Skia/Impeller rather than using platform widgets, so iOS and Android look '
        'identical. A strength if that is what you want, a problem if it is not.', M)
    add('https://docs.expo.dev/', 'Expo', ['açık-kaynak', 'react-native', 'mobil'],
        'React Native’i Xcode ve Android Studio kurmadan geliştirilebilir kılıyor; '
        'EAS ile derleme bulutta yapılıyor. Yerel modül eklemek eskisi kadar sorun değil artık.',
        'Makes React Native developable without installing Xcode or Android Studio, with EAS building in the cloud. '
        'Adding native modules is no longer the obstacle it once was.', M)
    add('https://www.electronjs.org/', 'Electron', ['açık-kaynak', 'javascript', 'masaüstü'],
        'Chromium ve Node.js’i paketleyip web teknolojisiyle masaüstü uygulaması çıkarıyor. '
        'VS Code ve Slack bununla yazıldı; bellek tüketimi de bu yüzden sürekli eleştiriliyor.',
        'Bundles Chromium and Node.js to ship desktop apps built with web technology. VS Code and Slack were built '
        'this way — and its memory footprint is criticised for the same reason.', M)
    add('https://www.electronjs.org/docs/latest', 'Electron Dokümantasyonu', ['dokümantasyon', 'masaüstü', 'güvenlik'],
        'Ana süreç ile işleyici süreç ayrımı ve bunlar arası iletişim (IPC) referansı. '
        'contextIsolation ve nodeIntegration ayarları güvenlik açısından kritik; varsayılanları değiştirme.',
        'Reference for the main/renderer process split and the IPC between them. The contextIsolation and '
        'nodeIntegration settings are security-critical — leave the defaults alone.', M)
    add('https://rive.app/docs/runtimes/flutter/flutter', 'Rive (Flutter)', ['saas', 'freemium', 'animasyon', 'mobil'],
        'Vektör animasyonu uygulamaya gömüyor; Lottie’den farkı, animasyonun durum makinesi taşıyıp '
        'kullanıcı etkileşimine tepki verebilmesi. Dosya boyutu da belirgin küçük.',
        'Embeds vector animation into an app. Unlike Lottie the animation carries a state machine and reacts to '
        'user interaction, and the file size is markedly smaller.', M)
