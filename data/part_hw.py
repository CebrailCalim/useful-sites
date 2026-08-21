# -*- coding: utf-8 -*-
"""Hardware, CAD & Embedded - Smart Glasses & Wearables"""


def load(add):
    # ============================================================ HARDWARE, CAD & EMBEDDED
    H = 'donanim'
    add('https://www.onshape.com/en/', 'Onshape', ['saas', 'freemium', 'cad', 'tarayıcı-içi'],
        'Parametrik CAD, tamamen tarayıcıda. Dosya değil veritabanı üzerinde çalışıyor, '
        'bu yüzden dallanma ve birleştirme Git gibi işliyor — SolidWorks’te olmayan bir şey.',
        'Parametric CAD entirely in the browser, working on a database rather than files, '
        'so branching and merging behave like Git — something SolidWorks does not offer.', H)
    add('https://cadxstudio.in/', 'CadXStudio', ['ücretsiz', 'cad', 'tarayıcı-içi'],
        'Metinden CAD modeli üreten tarayıcı aracı; CAM tarafını da kapsıyor. '
        'Çizim bilmeden basit parça çıkarmayı hedefliyor, hassas mühendislik için değil.',
        'A browser tool generating CAD models from text, reaching into CAM as well. '
        'Aimed at simple parts without drafting skill, not at precision engineering.', H)
    add('https://www.mcmaster.com/', 'McMaster-Carr', ['ücretli', 'parça', 'cad'],
        'Endüstriyel parça kataloğu; neredeyse her ürünün CAD modelini indirebiliyorsun. '
        'Tasarımda gerçek bir cıvatanın ölçüsü lazım olduğunda referans kaynağa dönüşüyor.',
        'An industrial parts catalogue where nearly every item has a downloadable CAD model, '
        'which turns it into a reference whenever a design needs a real bolt’s dimensions.', H)
    add('https://grabcad.com/library/robotic-mini-tank-1', 'GrabCAD · Mini Tank', ['ücretsiz', 'cad', 'model'],
        'Paylaşılmış paletli robot platformu modeli. Şasi geometrisini sıfırdan çizmek yerine '
        'çalışan bir tasarımdan başlamak için.',
        'A shared tracked robot platform model — a way to start from a working design instead of drawing '
        'chassis geometry from scratch.', H)
    add('https://www.youtube.com/playlist?list=PLUMWjy5jgHK3j74Z5Tq6Tso1fSfVWZC8L', 'Kontrol Sistemleri Dersleri', ['video', 'ücretsiz', 'kontrol'],
        'Kontrol teorisinin tam ders serisi: transfer fonksiyonları, kararlılık ölçütleri, '
        'durum uzayı. Matematiksel temeli akademik sırayla kuruyor.',
        'A full lecture series on control theory — transfer functions, stability criteria, state space — '
        'building the mathematics in academic order.', H)
    add('https://www.youtube.com/playlist?list=PLn8PRpmsu08pFBqgd_6Bi7msgkWFKL33b', 'Kontrol Sistemleri Uygulamada', ['video', 'ücretsiz', 'kontrol'],
        'Aynı teorinin mühendislik sezgisi tarafı: PID’i gerçekte nasıl ayarlarsın, '
        'gürültü ve doygunluk ne yapar. Ders serisiyle birlikte okunması gereken taraf.',
        'The engineering-intuition side of the same theory: how you actually tune a PID, what noise and saturation '
        'do to it. The half that belongs alongside the lecture course.', H)
    add('https://github.com/yuchung886886/ORCAS', 'ORCAS', ['açık-kaynak', 'github', 'robotik', 'gömülü'],
        'Uzaktan kumandalı airsoft taret sistemi; gömülü denetim, video akışı ve mekanik tasarım '
        'aynı projede birleşiyor. Bitmiş ürünlerin gizlediği entegrasyon sorunlarını görüyorsun.',
        'A remote-controlled airsoft turret where embedded control, video streaming and mechanical design meet in '
        'one project — showing the integration problems finished products hide.', H)
    add('https://www.youtube.com/watch?v=d6PXSTV486c', 'Taret Süspansiyon Günlüğü', ['video', 'robotik', 'diy'],
        'Ev yapımı taret projesinin geliştirme günlüğü; başarısız denemeler kesilmemiş. '
        'Cilalı öğreticilerin aksine gerçek tasarım süreci böyle görünüyor.',
        'A build diary for a homemade turret with the failed attempts left in — '
        'what a real design process looks like, unlike a polished tutorial.', H)
    # embedded & IoT
    add('https://openipc.org/', 'OpenIPC', ['açık-kaynak', 'firmware', 'kamera'],
        'IP kameralar için açık ürün yazılımı; üretici bulutunu devreden çıkarıp RTSP akışını '
        'doğrudan kendi ağına veriyor. Kamerayı internete açmadan kullanmanın yolu.',
        'Open firmware for IP cameras that removes the vendor cloud and exposes the RTSP stream directly on your '
        'own network — the way to run a camera without putting it on the internet.', H)
    add('https://github.com/OpenIPC/firmware', 'OpenIPC Firmware', ['açık-kaynak', 'github', 'firmware'],
        'Desteklenen yonga listesi ve derleme talimatları. Kameranı almadan önce '
        'yongasının listede olup olmadığına bakmak gerekiyor.',
        'The supported chipset list and build instructions — check whether your camera’s SoC is on it '
        'before you buy.', H)
    add('https://github.com/OpenIPC/wiki/blob/master/en/installation.md', 'OpenIPC Kurulum', ['github', 'rehber', 'firmware'],
        'Alternatif yazılım yükleme adımları ve — daha önemlisi — geri dönüş yolu. '
        'Seri konsol bağlantısı olmadan denemek cihazı tuğlalama riskini ciddi artırıyor.',
        'The flashing steps and, more importantly, the way back. Attempting this without a serial console '
        'raises the bricking risk considerably.', H)
    add('https://github.com/openipc/coupler/', 'OpenIPC Coupler', ['açık-kaynak', 'github', 'firmware'],
        'Kamera ürün yazılımları arasında geçiş yapmayı ve orijinaline dönmeyi sağlıyor. '
        'Deneme yaparken elindeki tek kurtarma aracı bu olabiliyor.',
        'Moves between camera firmwares and back to stock — often the only recovery tool you have while experimenting.', H)
    add('https://github.com/OpenIPC/firmware/issues/1970', 'AK3918 Kamera Notları', ['github', 'gömülü', 'donanım'],
        'Belirli bir kamera yongası için donanım bilgisi ve yazılım dökümlerinin biriktiği tartışma. '
        'Bu tür modeller için tek kaynak genelde böyle bir konu başlığı oluyor.',
        'A thread accumulating hardware notes and firmware dumps for one camera SoC. For models like this, '
        'a single issue thread is usually the only source there is.', H)
    add('https://github.com/MuhammedKalkan/Anyka-Camera-Firmware', 'Anyka Kamera Firmware', ['açık-kaynak', 'github', 'firmware'],
        'Anyka yongalı kameralar için özel ürün yazılımı; OpenIPC’nin kapsamadığı bir aileyi hedefliyor. '
        'Ucuz Çin kameralarının çoğu bu yonga ailesini kullanıyor.',
        'Custom firmware for Anyka-based cameras, covering a family OpenIPC does not. '
        'Most cheap Chinese cameras use this chipset.', H)
    add('https://github.com/AvaotaSBC/AvaotaF1', 'AvaotaF1', ['açık-kaynak', 'github', 'sbc', 'risc-v'],
        'Madeni para boyutunda RISC-V Linux kartı: 64 MB RAM, MIPI kamera, SPI ekran ve Wi-Fi. '
        'Bu ölçekte mikrodenetleyici değil tam Linux çalıştırabilmesi ayrıksı.',
        'A coin-sized RISC-V Linux board with 64 MB RAM, MIPI camera, SPI display and Wi-Fi. '
        'Running full Linux rather than a microcontroller at that scale is what makes it unusual.', H)
    add('https://www.electronics-lab.com/avaotaf1-development-board-offers-allwinner-v821-soc-64mb-ram-mipi-camera-spi-display-and-wi-fi-in-coin-size-form/', 'AvaotaF1 İncelemesi', ['ücretsiz', 'donanım', 'inceleme'],
        'Kartın teknik özelliklerini ve olası kullanım alanlarını derleyen yazı; '
        'resmî depoya dalmadan önce hızlı bir bakış.',
        'An article summarising the board’s specifications and likely uses — a quick look before diving into the repo.', H)
    add('https://kokomotech.com/allwinner-v821/', 'Allwinner V821', ['ücretsiz', 'donanım', 'soc'],
        'V821 yonga setinin teknik özeti; görüntü işleme hattı ve NPU yetenekleri dahil. '
        'Kamera veya uç yapay zeka projesinde yonga seçerken karşılaştırma noktası.',
        'A technical summary of the V821 SoC including its image pipeline and NPU capability — '
        'a comparison point when choosing silicon for a camera or edge AI project.', H)
    add('https://github.com/LiteEMF?tab=repositories', 'LiteEMF', ['açık-kaynak', 'github', 'gömülü', 'usb'],
        'Gömülü sistem kütüphaneleri ve ürün yazılımı depoları; USB HID ve kablosuz '
        'giriş cihazı projeleri ağırlıkta. Kumanda ve klavye protokolleri için referans.',
        'Embedded libraries and firmware repositories weighted towards USB HID and wireless input devices — '
        'a reference for controller and keyboard protocols.', H)
    add('https://campaign.advantech.online/en/edgeaisdk/index.html', 'Advantech Edge AI SDK', ['ücretsiz', 'gömülü', 'sdk'],
        'Endüstriyel uç donanımda model çalıştırmak için geliştirme kiti. '
        'Fabrika ortamı gibi sertifikalı donanım gerektiren yerlerde Raspberry Pi sınıfı kartlar yeterli olmuyor.',
        'A development kit for running models on industrial edge hardware — where certified equipment is required, '
        'a Raspberry Pi-class board does not qualify.', H)
    add('https://eclipse.dev/ditto/', 'Eclipse Ditto', ['açık-kaynak', 'iot', 'dijital-ikiz'],
        'Cihazın durumunu sunucuda bir “dijital ikiz” olarak tutuyor; cihaz uykudayken bile '
        'son bilinen durumu sorgulanabiliyor ve komut kuyruğa alınabiliyor.',
        'Keeps device state server-side as a digital twin, so the last known state stays queryable and commands '
        'queue up even while the device sleeps.', H)
    add('https://tr.smartvision.dev/', 'SmartVision', ['freemium', 'türkçe', 'kamera'],
        'Türkçe arayüzlü video gözetim yazılımı; kamera yönetimi ve kayıt tarafını kapsıyor. '
        'Yerel kurulumlarda dil ve destek açısından pratik bir seçenek.',
        'Video surveillance software with a Turkish interface covering camera management and recording — '
        'a practical option locally for language and support reasons.', H)

    # ============================================================ SMART GLASSES & WEARABLES
    S = 'gozluk'
    add('https://github.com/Mentra-Community/MentraOS', 'MentraOS', ['açık-kaynak', 'github', 'işletim-sistemi'],
        'Akıllı gözlükler için açık işletim sistemi; farklı üreticilerin donanımını tek uygulama '
        'katmanında topluyor. Her gözlük için ayrı uygulama yazma sorununu hedefliyor.',
        'An open operating system for smart glasses unifying different vendors’ hardware under one app layer — '
        'aimed at the problem of writing a separate app per device.', S)
    add('https://github.com/Mentra-Community/OpenSourceSmartGlasses', 'Open Source Smart Glasses', ['açık-kaynak', 'github', 'donanım', 'diy'],
        'Tüm gün takılabilir açık kaynak gözlük tasarımı; şema, PCB ve yazılım açık. '
        'Kapalı ürünlerin aksine ne topladığını ve nereye gönderdiğini görebiliyorsun.',
        'An all-day wearable open-source glasses design with schematics, PCB and software published — '
        'so unlike closed products you can see what it collects and where it sends it.', S)
    add('https://github.com/Mentra-Community/OpenSourceSmartGlasses/wiki/How-to-build-the-Open-Source-Smart-Glasses/4f426a4923cd6265b6179954e8abb2e6308b893a', 'Açık Kaynak Gözlük Yapımı', ['github', 'rehber', 'diy'],
        'Malzeme listesi ve montaj sırasıyla adım adım yapım rehberi. '
        'Projeyi tekrar edilebilir kılan şey tam olarak bu ayrıntı düzeyi.',
        'A step-by-step build guide with a bill of materials and assembly order — exactly the level of detail '
        'that makes a project reproducible.', S)
    add('https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit', 'Mentra Bluetooth SDK', ['açık-kaynak', 'github', 'ble', 'android'],
        'Android’den gözlüğe BLE ile bağlanmak için başlangıç kiti. '
        'GATT servisleri ve karakteristikleri tanımlı geldiği için protokolü kendin çözmüyorsun.',
        'A starter kit for connecting to glasses over BLE from Android. GATT services and characteristics arrive '
        'defined, so you do not reverse-engineer the protocol yourself.', S)
    add('https://github.com/BasedHardware/OpenGlass', 'OpenGlass', ['açık-kaynak', 'github', 'donanım', 'diy'],
        'Mevcut bir gözlüğe kamera ve kart takarak akıllı gözlüğe çeviriyor; '
        'yaklaşık 25 dolarlık parça listesi var. Sıfırdan üretim yerine dönüştürme yolu.',
        'Converts an existing pair of glasses by attaching a camera and board, on a parts list of roughly $25. '
        'Conversion rather than manufacture.', S)
    add('https://github.com/BasedHardware/omi', 'Omi', ['açık-kaynak', 'github', 'giyilebilir', 'ses'],
        'Konuşmaları dinleyip özetleyen giyilebilir cihaz; gözlükten farklı olarak görüntü değil '
        'bağlam yakalıyor. Sürekli dinleme fikrinin etik tarafı ayrı bir tartışma.',
        'A wearable that listens to conversations and summarises them, capturing context rather than vision. '
        'The ethics of always-on listening are a separate argument.', S)
    add('https://github.com/topics/smart-glasses', 'GitHub · smart-glasses', ['github', 'dizin'],
        'Etiketli açık kaynak projelerin canlı listesi; derlenmiş listelerin aksine '
        'kendiliğinden güncel kalıyor. Yeni çıkanları yakalamak için.',
        'A live list of tagged open-source projects that stays current by itself, unlike curated lists — '
        'the way to catch new arrivals.', S)
    add('https://github.com/topics/ray-ban-meta', 'GitHub · ray-ban-meta', ['github', 'dizin', 'tersine-mühendislik'],
        'Ray-Ban Meta gözlükleri üzerine topluluk projeleri. Resmî SDK olmadığı için '
        'buradaki çalışmalar ağırlıkla protokol çözümlemesi ve gayriresmî köprüler.',
        'Community projects around Ray-Ban Meta glasses. With no official SDK, the work here is mostly protocol '
        'analysis and unofficial bridges.', S)
    # Even Realities
    add('https://www.evenrealities.com/smart-glasses', 'Even Realities G2', ['ücretli', 'ürün', 'ekran'],
        'Kamera koymayıp yalnızca ekran sunan günlük kullanım gözlüğü. '
        'Kamerasızlık teknik bir eksik değil bilinçli bir karar — sosyal kabul sorununu doğrudan çözüyor.',
        'Everyday glasses with a display and deliberately no camera. The omission is a decision rather than a '
        'shortfall — it addresses the social acceptance problem head on.', S)
    add('https://www.evenrealities.com/smart-glasses/selection', 'Even Realities · Çerçeve Seçimi', ['ücretli', 'ürün'],
        'Çerçeve ve numaralı cam seçenekleri. Gözlük gerçekten günlük takılacaksa '
        'teknolojiden çok bu kısım belirleyici oluyor.',
        'Frame and prescription lens options — the part that decides whether the glasses actually get worn daily, '
        'more than the technology does.', S)
    add('https://hub.evenrealities.com/', 'Even Hub', ['ücretsiz', 'geliştirici', 'sdk'],
        'Üreticinin geliştirici merkezi; uygulama geliştirme kaynakları ve API belgeleri burada.',
        'The vendor’s developer hub, holding app development resources and API documentation.', S)
    add('https://github.com/even-realities', 'Even Realities (GitHub)', ['açık-kaynak', 'github', 'sdk'],
        'Üreticinin resmî depoları; SDK ve örnek uygulamalar için birincil kaynak. '
        'Donanım üreticisinin kod yayımlaması bu sektörde hâlâ istisna.',
        'The vendor’s official repositories and the primary source for the SDK and sample apps. '
        'A hardware maker publishing code is still the exception in this sector.', S)
    add('https://github.com/pangoleen/awesome-even-realities-g2', 'Awesome Even Realities G2', ['github', 'awesome-liste'],
        'G2 için topluluk kaynakları derlemesi; resmî dokümanın kapsamadığı araçlar ve '
        'çözülmüş sorunlar burada birikiyor.',
        'A community resource collection for the G2, accumulating the tools and solved problems the official '
        'documentation does not cover.', S)
    add('https://github.com/i-soxi/even-g2-protocol', 'Even G2 Protokolü', ['açık-kaynak', 'github', 'tersine-mühendislik', 'ble'],
        'Cihazın BLE protokolünü tersine mühendislikle çözen çalışma. '
        'Resmî SDK’nın izin vermediği kullanımlar ancak buradan mümkün oluyor.',
        'Reverse-engineering of the device’s BLE protocol — the only route to uses the official SDK does not permit.', S)
    # HeyCyan
    add('https://github.com/ebowwa/HeyCyanSmartGlassesSDK', 'HeyCyan SDK', ['açık-kaynak', 'github', 'sdk', 'ble'],
        'HeyCyan gözlükleri için platformlar arası SDK; fotoğraf, video ve ses kaydını '
        'uygulama tarafından denetlemeyi sağlıyor.',
        'A cross-platform SDK for HeyCyan glasses giving application-level control over photo, video and audio capture.', S)
    add('https://github.com/ebowwa/HeyCyanSmartGlassesSDK/blob/main/WIFI_TRANSFER_ARCHITECTURE.md', 'HeyCyan Wi-Fi Aktarım Mimarisi', ['github', 'teknik', 'mimari'],
        'Gözlükten telefona medya aktarımının nasıl kurgulandığını anlatan teknik not: '
        'BLE ile denetim, Wi-Fi ile veri. Benzer cihaz tasarlayanlar için doğrudan uygulanabilir bir desen.',
        'A technical note on how media transfer from glasses to phone is structured — control over BLE, bulk data '
        'over Wi-Fi. A pattern directly applicable to similar devices.', S)
    add('https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK', 'Alternatif HeyCyan Uygulaması', ['açık-kaynak', 'github'],
        'Üreticinin uygulamasına açık kaynak alternatif; kapalı uygulamanın kilitlediği '
        'özellikleri açmayı ve bulut bağımlılığını kaldırmayı hedefliyor.',
        'An open-source alternative to the vendor app, aimed at unlocking restricted features and removing '
        'the cloud dependency.', S)
    add('https://github.com/AdeelHamid/HeyCyan-Web-Bridge-App', 'HeyCyan Web Köprüsü', ['açık-kaynak', 'github', 'web-bluetooth'],
        'Gözlüğü Web Bluetooth üzerinden tarayıcıya bağlıyor; yerel uygulama yazmadan '
        'cihazla konuşabiliyorsun. Prototip için hızlı bir yol.',
        'Connects the glasses to a browser over Web Bluetooth, so you can talk to the device without writing '
        'a native app — a fast route for prototyping.', S)
    # other products
    add('https://brilliant.xyz/', 'Brilliant Labs', ['ücretli', 'açık-kaynak', 'ürün'],
        'Donanım şemasını ve yazılımını yayımlayan gözlük üreticisi. '
        'Bu sektörde hem ürün satıp hem tasarımı açan neredeyse tek şirket.',
        'A glasses maker that publishes both hardware schematics and software — close to the only company in the '
        'sector selling a product while opening the design.', S)
    add('https://brilliant.xyz/products/halo', 'Brilliant Labs Halo', ['ücretli', 'ürün', 'geliştirici'],
        'Geliştiricinin kendi uygulamasını yükleyebildiği yapay zeka gözlüğü; '
        'kapalı ekosistemlerin aksine cihaz üzerinde çalıştırma yetkisi sende.',
        'AI glasses where a developer can load their own applications — unlike closed ecosystems, '
        'the right to run code on the device is yours.', S)
    add('https://www.meta.com/tr/ai-glasses/meta-ray-ban-display-shiny-sand-transitions-and-neural-band-sand/', 'Meta Ray-Ban Display', ['ücretli', 'ürün', 'ekran'],
        'Ekranlı ve sinir bandıyla (EMG bileklik) kontrol edilen Meta gözlüğü. '
        'Kapalı bir ekosistem ama giriş yönteminin nereye evrildiğini göstermesi bakımından referans.',
        'Meta’s display glasses controlled by an EMG wristband. A closed ecosystem, but a reference point for '
        'where the input method is heading.', S)
    add('https://www.instructables.com/Smart-Glasses-V2/', 'Akıllı Gözlük Yapımı', ['ücretsiz', 'rehber', 'diy'],
        'Parçadan başlayan adım adım yapım rehberi; hazır kit kullanmıyor. '
        'Optik birleştirici ve güç yönetimi kısımları en zor bölümler.',
        'A step-by-step build starting from components rather than a kit. The optical combiner and power management '
        'sections are the hard parts.', S)
    add('https://www.youtube.com/watch?v=4ZY760EIUc4', 'Açık Kaynak Gözlük Yaptık', ['video', 'diy'],
        'Açık kaynak gözlük üretim sürecini anlatan video; nelerin gerçekten zor olduğunu '
        'süslemeden gösteriyor. Projeye girişmeden önce izlenmeli.',
        'A video on building open-source glasses that is honest about which parts are genuinely hard. '
        'Worth watching before committing to the project.', S)
    # chips & platforms
    add('https://dymesty.com/blogs/articles/smart-glasses-processor-chip-guide', 'Akıllı Gözlük Yonga Rehberi', ['ücretsiz', 'donanım', 'referans'],
        'Gözlüklerde kullanılan işlemci ve NPU seçeneklerinin karşılaştırması; '
        'güç bütçesi ve ısı kısıtlarını da tartışıyor. Gözlükte asıl sınır işlem gücü değil ısı.',
        'A comparison of processors and NPUs used in glasses, weighing power budget and thermal limits — '
        'in a frame the real constraint is heat, not compute.', S)
    add('https://dymesty.com/blogs/articles/smart-glasses-operating-system-guide', 'Akıllı Gözlük İşletim Sistemleri', ['ücretsiz', 'referans'],
        'Horizon OS, Android XR ve diğer platformların karşılaştırması. '
        'Hangi ekosisteme yatırım yapılacağı kararı donanım seçiminden önce geliyor.',
        'A comparison of Horizon OS, Android XR and the rest. Which ecosystem to invest in is a decision that '
        'precedes hardware selection.', S)
    add('https://www.qualcomm.com/xr-vr-ar/applications/ai-glasses', 'Qualcomm AI Glasses', ['ücretsiz', 'donanım', 'soc'],
        'Piyasadaki gözlüklerin çoğunda bulunan Snapdragon AR platformunun resmî sayfası; '
        'referans tasarımlar ve güç tüketimi verileri burada.',
        'The official page for the Snapdragon AR platform found in most shipping glasses, '
        'holding the reference designs and power figures.', S)
    add('https://www.realmcu.com/en/Applications/Smart-Glasses', 'RealMCU Akıllı Gözlük', ['ücretsiz', 'donanım', 'soc'],
        'Düşük güçlü gözlük çözümleri sunan yonga üreticisi; Qualcomm’a göre daha basit ve '
        'ucuz cihazları hedefliyor. Bildirim gösteren gözlük için Snapdragon fazla geliyor.',
        'A vendor offering low-power glasses silicon aimed at simpler, cheaper devices than Qualcomm. '
        'For glasses that only show notifications, a Snapdragon is overkill.', S)
    add('https://www.infineon.com/assets/row/public/documents/30/42/infineon-an242193-smart-glasses-hmi-with-psoc4-capsense-applicationnotes-en.pdf', 'PSOC4 CAPSENSE Uygulama Notu', ['ücretsiz', 'pdf', 'donanım'],
        'Gözlük sapına dokunmatik kontrol eklemenin uygulama notu; devre şeması ve '
        'kalibrasyon parametreleri dahil. Bu düzeyde somut belge nadiren açık oluyor.',
        'An application note on adding touch control to a glasses temple, with circuit diagram and calibration '
        'parameters. Documentation this concrete is rarely public.', S)
    add('https://blog.imaginationtech.com/chipsets-for-smart-glasses-and-other-high-end-wearables/', 'Giyilebilir Yonga Setleri', ['ücretsiz', 'makale', 'gpu'],
        'Üst seviye giyilebilirlerde grafik ve güç dengesini tartışan yazı. '
        'Ekranlı gözlükte GPU seçimi doğrudan pil ömrünü belirliyor.',
        'An article on the graphics-versus-power trade-off in high-end wearables. In display glasses, '
        'the GPU choice sets battery life directly.', S)
