# -*- coding: utf-8 -*-
"""Donanım, CAD & Gömülü · Akıllı Gözlük & Giyilebilir"""


def load(add):
    # ============================================================ DONANIM, CAD & GÖMÜLÜ
    H = 'donanim'
    add('https://www.onshape.com/en/', 'Onshape', ['freemium', 'cad', 'tarayıcıda'],
        'Tarayıcıda çalışan parametrik CAD; SolidWorks gibi masaüstü paketlerden farkı, sürüm geçmişini Git gibi tutması ve kurulum istememesi.',
        'Parametric CAD in the browser; unlike desktop suites it keeps version history like Git and needs no installation.', H)
    add('https://cadxstudio.in/', 'CadXStudio', ['ücretsiz', 'cad', 'yapay zeka'],
        'Metinden CAD modeli üreten tarayıcı tabanlı araç; çizim bilmeden parça oluşturmayı hedefliyor.',
        'Browser-based text-to-CAD tool aimed at producing parts without knowing how to draft.', H)
    add('https://www.mcmaster.com/', 'McMaster-Carr', ['ücretli', 'parça', 'referans'],
        'Endüstriyel parça kataloğu; her ürünün CAD modelini indirmeye izin vermesi onu tasarım aşamasında referans kaynağa çeviriyor.',
        'Industrial parts catalogue; letting you download a CAD model for nearly every item turns it into a design-time reference.', H)
    add('https://grabcad.com/library/robotic-mini-tank-1', 'GrabCAD · Mini Tank', ['ücretsiz', 'cad', 'model'],
        'Paylaşılan bir robotik platform CAD modeli; sıfırdan çizmek yerine mevcut tasarımdan yola çıkmak için.',
        'A shared robotic platform CAD model — a starting point instead of drawing from scratch.', H)
    add('https://www.youtube.com/playlist?list=PLUMWjy5jgHK3j74Z5Tq6Tso1fSfVWZC8L', 'Kontrol Sistemleri Dersleri', ['ücretsiz', 'video', 'kontrol'],
        'Kontrol teorisinin tam ders serisi; matematiksel temeli sıfırdan kuran akademik anlatım.',
        'A full lecture series on control theory, building the mathematical foundation from scratch.', H)
    add('https://www.youtube.com/playlist?list=PLn8PRpmsu08pFBqgd_6Bi7msgkWFKL33b', 'Kontrol Sistemleri Uygulamada', ['ücretsiz', 'video', 'kontrol'],
        'Kontrol teorisinin pratik karşılığını anlatan seri; ders serisinden farkı, denklemden çok mühendislik sezgisi vermesi.',
        'A series on what control theory looks like in practice; unlike the lecture course it builds intuition over equations.', H)
    add('https://github.com/yuchung886886/ORCAS', 'ORCAS', ['açık kaynak', 'github', 'robotik'],
        'Uzaktan kumandalı airsoft taret sistemi; gömülü kontrol ve mekanik tasarımın bir arada göründüğü çalışan bir proje.',
        'A remote-controlled airsoft turret system — a working project where embedded control and mechanical design meet.', H)
    add('https://www.youtube.com/watch?v=d6PXSTV486c', 'Taret Süspansiyon Günlüğü', ['ücretsiz', 'video', 'robotik'],
        'Ev yapımı taret projesinin geliştirme günlüğü; cilalı öğretici değil, deneme yanılma süreci.',
        'A build diary for a homemade turret project — trial and error rather than a polished tutorial.', H)
    # gömülü & IoT
    add('https://openipc.org/', 'OpenIPC', ['açık kaynak', 'gömülü', 'kamera'],
        'IP kameralar için açık kaynak alternatif ürün yazılımı; üretici yazılımının bulut bağımlılığını ortadan kaldırıyor.',
        'Open-source alternative firmware for IP cameras, removing the vendor firmware’s cloud dependency.', H)
    add('https://github.com/OpenIPC/firmware', 'OpenIPC Firmware', ['açık kaynak', 'github', 'gömülü'],
        'OpenIPC ürün yazılımının kaynak deposu; desteklenen yonga listesi ve derleme talimatları burada.',
        'The OpenIPC firmware source repository, holding the supported chip list and build instructions.', H)
    add('https://github.com/OpenIPC/wiki/blob/master/en/installation.md', 'OpenIPC Kurulum', ['ücretsiz', 'github', 'rehber'],
        'Kameraya alternatif yazılım yükleme adımları; geri dönüş yolunu da anlatması cihazı tuğlalamamak için önemli.',
        'Steps for flashing alternative firmware onto a camera; it also documents the way back, which matters for not bricking the device.', H)
    add('https://github.com/openipc/coupler/', 'OpenIPC Coupler', ['açık kaynak', 'github', 'gömülü'],
        'Kamera ürün yazılımları arasında sorunsuz geçiş sağlayan araç; deneme sırasında cihazı kurtarma imkânı verir.',
        'Tool for switching cleanly between camera firmwares, giving you a recovery path while experimenting.', H)
    add('https://github.com/OpenIPC/firmware/issues/1970', 'AK3918 Kamera Notları', ['ücretsiz', 'github', 'gömülü'],
        'Belirli bir kamera yongası için donanım bilgisi ve yazılım dökümlerinin toplandığı tartışma; bu modelle uğraşanlar için birincil kaynak.',
        'A thread collecting hardware notes and firmware dumps for one camera chipset — the primary source if you own that model.', H)
    add('https://github.com/MuhammedKalkan/Anyka-Camera-Firmware', 'Anyka Kamera Firmware', ['açık kaynak', 'github', 'gömülü'],
        'Anyka yongalı kameralar için özel ürün yazılımı ve uygulamalar; OpenIPC’nin kapsamadığı bir yonga ailesini hedefliyor.',
        'Custom firmware and apps for Anyka-based cameras, targeting a chipset family OpenIPC does not cover.', H)
    add('https://github.com/AvaotaSBC/AvaotaF1', 'AvaotaF1', ['açık kaynak', 'github', 'sbc'],
        'Madeni para boyutunda RISC-V Linux tek kart bilgisayar; bu ölçekte tam Linux çalıştırabilmesi ayırt edici yanı.',
        'A coin-sized RISC-V Linux single-board computer — running full Linux at that scale is what sets it apart.', H)
    add('https://www.electronics-lab.com/avaotaf1-development-board-offers-allwinner-v821-soc-64mb-ram-mipi-camera-spi-display-and-wi-fi-in-coin-size-form/', 'AvaotaF1 İncelemesi', ['ücretsiz', 'donanım', 'inceleme'],
        'AvaotaF1 kartının teknik özelliklerini derleyen yazı; resmî depodan önce hızlı bir genel bakış.',
        'An article summarising the AvaotaF1 board’s specifications — a quick overview before the official repo.', H)
    add('https://kokomotech.com/allwinner-v821/', 'Allwinner V821', ['ücretsiz', 'donanım', 'referans'],
        'V821 yongasının teknik özet sayfası; kamera ve yapay zeka uygulamaları için yonga seçerken karşılaştırma noktası.',
        'A technical summary of the V821 SoC — a comparison point when picking a chip for camera and AI applications.', H)
    add('https://github.com/LiteEMF?tab=repositories', 'LiteEMF', ['açık kaynak', 'github', 'gömülü'],
        'Gömülü sistemler için kütüphane ve ürün yazılımı depoları; USB ve kablosuz giriş cihazı projeleri ağırlıkta.',
        'Repositories of embedded libraries and firmware, weighted towards USB and wireless input device projects.', H)
    add('https://campaign.advantech.online/en/edgeaisdk/index.html', 'Advantech Edge AI SDK', ['ücretsiz', 'gömülü', 'sdk'],
        'Uç cihazlarda yapay zeka geliştirme kiti; endüstriyel donanım üzerinde model çalıştırmayı hedefliyor.',
        'An AI development kit for edge devices, aimed at running models on industrial hardware.', H)
    add('https://eclipse.dev/ditto/', 'Eclipse Ditto', ['açık kaynak', 'iot', 'çatı'],
        'Nesnelerin interneti için dijital ikiz çatısı; cihazın durumunu, cihaz çevrimdışıyken bile sorgulanabilir kılması ayırt edici.',
        'A digital twin framework for IoT; keeping device state queryable even while the device is offline is its distinction.', H)
    add('https://tr.smartvision.dev/', 'SmartVision', ['freemium', 'türkçe', 'kamera'],
        'Video gözetim yazılımı; Türkçe arayüzüyle yerel kurulumlarda tercih edilebilir bir seçenek.',
        'Video surveillance software with a Turkish interface, a viable option for local deployments.', H)

    # ============================================================ AKILLI GÖZLÜK & GİYİLEBİLİR
    S = 'gozluk'
    add('https://github.com/Mentra-Community/MentraOS', 'MentraOS', ['açık kaynak', 'github', 'işletim sistemi'],
        'Akıllı gözlükler için açık kaynak işletim sistemi; farklı üreticilerin donanımını tek uygulama katmanında toplaması ayırt edici yanı.',
        'Open-source operating system for smart glasses, distinguished by unifying different vendors’ hardware under one app layer.', S)
    add('https://github.com/Mentra-Community/OpenSourceSmartGlasses', 'Open Source Smart Glasses', ['açık kaynak', 'github', 'donanım'],
        'Tüm gün takılabilir açık kaynak akıllı gözlük tasarımı; kapalı ürünlere karşı şeması ve yazılımı açık bir alternatif.',
        'An all-day wearable open-source smart glasses design — an alternative with open schematics and software.', S)
    add('https://github.com/Mentra-Community/OpenSourceSmartGlasses/wiki/How-to-build-the-Open-Source-Smart-Glasses/4f426a4923cd6265b6179954e8abb2e6308b893a', 'Açık Kaynak Gözlük Yapımı', ['ücretsiz', 'github', 'rehber'],
        'Gözlüğü sıfırdan üretmenin adım adım rehberi; parça listesi ve montaj sırasını içermesiyle projeyi tekrarlanabilir kılıyor.',
        'A step-by-step build guide with bill of materials and assembly order, which makes the project reproducible.', S)
    add('https://github.com/Mentra-Community/Mentra-Bluetooth-SDK-Starter-Kit', 'Mentra Bluetooth SDK', ['açık kaynak', 'github', 'sdk'],
        'Android’den gözlüğe BLE ile bağlanmak için başlangıç kiti; protokolü sıfırdan çözmek yerine çalışan örnekle başlatıyor.',
        'A starter kit for connecting to glasses over BLE from Android, starting you from working code instead of reverse-engineering the protocol.', S)
    add('https://github.com/BasedHardware/OpenGlass', 'OpenGlass', ['açık kaynak', 'github', 'donanım'],
        'Herhangi bir gözlüğü yapay zeka destekli akıllı gözlüğe çeviren proje; sıfırdan üretim yerine mevcut çerçeveyi dönüştürmesi ayırt edici.',
        'Turns any pair of glasses into AI-powered smart glasses — converting an existing frame rather than manufacturing one.', S)
    add('https://github.com/BasedHardware/omi', 'Omi', ['açık kaynak', 'github', 'giyilebilir'],
        'Ekranı dinleyip konuşmaları takip eden giyilebilir yapay zeka cihazı; gözlükten farklı olarak görüntü değil bağlam yakalamaya odaklı.',
        'A wearable AI device that listens and tracks conversations — focused on capturing context rather than vision.', S)
    add('https://github.com/topics/smart-glasses', 'GitHub · smart-glasses', ['ücretsiz', 'github', 'dizin'],
        'Akıllı gözlük etiketli açık kaynak projelerin canlı listesi; derlenmiş listelerden farkı, kendiliğinden güncel kalması.',
        'A live list of open-source projects tagged smart-glasses; unlike curated lists it stays current by itself.', S)
    add('https://github.com/topics/ray-ban-meta', 'GitHub · ray-ban-meta', ['ücretsiz', 'github', 'dizin'],
        'Ray-Ban Meta gözlükleri üzerine topluluk projeleri; resmî SDK olmayan bir cihaz için gayriresmî çalışmaların toplandığı yer.',
        'Community projects around Ray-Ban Meta glasses — where unofficial work gathers for a device with no official SDK.', S)
    # Even Realities
    add('https://www.evenrealities.com/smart-glasses', 'Even Realities G2', ['ücretli', 'ürün'],
        'Ekranlı günlük kullanım akıllı gözlüğü; kamera koymayıp yalnızca bilgi göstermeye odaklanmasıyla rakiplerinden ayrılıyor.',
        'Everyday smart glasses with a display, differing from rivals by omitting a camera and focusing purely on showing information.', S)
    add('https://www.evenrealities.com/smart-glasses/selection', 'Even Realities · Çerçeve Seçimi', ['ücretli', 'ürün'],
        'G2 çerçeve ve numaralı cam seçenekleri; gözlük gerçekten günlük takılacaksa belirleyici olan kısım.',
        'G2 frame and prescription lens options — the part that decides whether the glasses are actually wearable daily.', S)
    add('https://hub.evenrealities.com/', 'Even Hub', ['ücretsiz', 'geliştirici'],
        'Even Realities cihazları için geliştirici merkezi; resmî uygulama geliştirme kaynaklarının giriş noktası.',
        'Developer hub for Even Realities devices — the entry point for official app development resources.', S)
    add('https://github.com/even-realities', 'Even Realities (GitHub)', ['açık kaynak', 'github'],
        'Üreticinin resmî açık kaynak depoları; SDK ve örnek uygulamalar için birincil kaynak.',
        'The manufacturer’s official open-source repositories — the primary source for the SDK and sample apps.', S)
    add('https://github.com/pangoleen/awesome-even-realities-g2', 'Awesome Even Realities G2', ['ücretsiz', 'github', 'koleksiyon'],
        'G2 için topluluk kaynaklarının derlemesi; resmî dokümanın kapsamadığı araç ve ipuçlarını toplar.',
        'A community resource collection for the G2, gathering tools and tips the official docs leave out.', S)
    add('https://github.com/i-soxi/even-g2-protocol', 'Even G2 Protokolü', ['açık kaynak', 'github', 'tersine mühendislik'],
        'G2’nin iletişim protokolünü tersine mühendislikle çözen çalışma; resmî SDK’nın izin vermediği kullanımlar için gerekli.',
        'Reverse-engineering of the G2’s communication protocol — needed for uses the official SDK does not permit.', S)
    # HeyCyan
    add('https://github.com/ebowwa/HeyCyanSmartGlassesSDK', 'HeyCyan SDK', ['açık kaynak', 'github', 'sdk'],
        'HeyCyan gözlükleri için platformlar arası SDK; fotoğraf, video ve ses kaydını uygulamadan denetlemeyi sağlıyor.',
        'Cross-platform SDK for HeyCyan glasses, giving app-level control over photo, video and audio capture.', S)
    add('https://github.com/ebowwa/HeyCyanSmartGlassesSDK/blob/main/WIFI_TRANSFER_ARCHITECTURE.md', 'HeyCyan Wi-Fi Aktarım Mimarisi', ['ücretsiz', 'github', 'teknik'],
        'Gözlükten telefona medya aktarımının nasıl çalıştığını anlatan teknik not; benzer cihaz geliştirenler için model.',
        'A technical note on how media transfer from glasses to phone works — a model for anyone building a similar device.', S)
    add('https://github.com/FerSaiyan/Alternative-HeyCyan-App-and-SDK', 'Alternatif HeyCyan Uygulaması', ['açık kaynak', 'github'],
        'Üreticinin uygulamasına açık kaynak alternatif; kapalı uygulamanın sınırladığı özellikleri açmayı hedefliyor.',
        'An open-source alternative to the vendor app, aimed at unlocking features the closed app restricts.', S)
    add('https://github.com/AdeelHamid/HeyCyan-Web-Bridge-App', 'HeyCyan Web Köprüsü', ['açık kaynak', 'github'],
        'Gözlüğü web uygulamasına bağlayan köprü; yerel uygulama yazmadan tarayıcıdan denetim sağlıyor.',
        'A bridge connecting the glasses to a web app, allowing browser control without writing a native app.', S)
    # diğer ürünler
    add('https://brilliant.xyz/', 'Brilliant Labs', ['ücretli', 'açık kaynak', 'ürün'],
        'Açık kaynak akıllı gözlük üreticisi; donanım şemalarını ve yazılımını yayımlaması sektörde ender.',
        'An open-source smart glasses maker — publishing both hardware schematics and software is rare in this sector.', S)
    add('https://brilliant.xyz/products/halo', 'Brilliant Labs Halo', ['ücretli', 'ürün'],
        'Brilliant Labs’ın yapay zeka gözlüğü; geliştiricinin kendi uygulamasını yükleyebilmesi üzerine kurulu.',
        'Brilliant Labs’ AI glasses, built around letting developers load their own applications.', S)
    add('https://www.meta.com/tr/ai-glasses/meta-ray-ban-display-shiny-sand-transitions-and-neural-band-sand/', 'Meta Ray-Ban Display', ['ücretli', 'ürün'],
        'Ekranlı ve sinir bandı kontrollü Meta gözlüğü; kapalı bir ekosistem ama pazarın yönünü göstermesi bakımından referans.',
        'Meta’s display-equipped glasses with a neural wristband — a closed ecosystem, but a reference point for where the market is heading.', S)
    add('https://www.instructables.com/Smart-Glasses-V2/', 'Akıllı Gözlük Yapımı', ['ücretsiz', 'rehber', 'diy'],
        'Adım adım akıllı gözlük yapım rehberi; hazır kit yerine parçadan başlayan bir hobi projesi.',
        'A step-by-step build guide — a hobby project starting from components rather than a kit.', S)
    add('https://www.youtube.com/watch?v=4ZY760EIUc4', 'Açık Kaynak Gözlük Yaptık', ['ücretsiz', 'video'],
        'Açık kaynak akıllı gözlük üretim sürecini anlatan video; nelerin zor olduğunu gerçekçi biçimde gösteriyor.',
        'A video on building open-source smart glasses, realistic about which parts are hard.', S)
    # yonga & platform araştırması
    add('https://dymesty.com/blogs/articles/smart-glasses-processor-chip-guide', 'Akıllı Gözlük Yonga Rehberi', ['ücretsiz', 'referans', 'donanım'],
        'Gözlüklerde kullanılan işlemci ve NPU seçeneklerinin karşılaştırması; donanım tasarımına başlarken yonga seçimi için.',
        'A comparison of processors and NPUs used in glasses — for the chip selection step of a hardware design.', S)
    add('https://dymesty.com/blogs/articles/smart-glasses-operating-system-guide', 'Akıllı Gözlük İşletim Sistemleri', ['ücretsiz', 'referans'],
        'Horizon OS, Android XR ve diğer platformların karşılaştırması; hangi ekosisteme yatırım yapılacağına karar vermek için.',
        'A comparison of Horizon OS, Android XR and other platforms — for deciding which ecosystem to invest in.', S)
    add('https://www.qualcomm.com/xr-vr-ar/applications/ai-glasses', 'Qualcomm AI Glasses', ['ücretsiz', 'donanım', 'referans'],
        'Piyasadaki gözlüklerin çoğunda bulunan Snapdragon platformunun resmî sayfası; referans tasarımlar için birincil kaynak.',
        'The official page for the Snapdragon platform found in most shipping glasses — the primary source for reference designs.', S)
    add('https://www.realmcu.com/en/Applications/Smart-Glasses', 'RealMCU Akıllı Gözlük', ['ücretsiz', 'donanım'],
        'Düşük güçlü gözlük çözümleri sunan yonga üreticisi; Qualcomm’a göre daha basit ve ucuz cihazları hedefliyor.',
        'A chip vendor offering low-power glasses solutions, targeting simpler and cheaper devices than Qualcomm.', S)
    add('https://www.infineon.com/assets/row/public/documents/30/42/infineon-an242193-smart-glasses-hmi-with-psoc4-capsense-applicationnotes-en.pdf', 'PSOC4 CAPSENSE Uygulama Notu', ['ücretsiz', 'pdf', 'donanım'],
        'Gözlük gövdesine dokunmatik kontrol eklemenin uygulama notu; devre şeması düzeyinde somut bir referans.',
        'An application note on adding touch control to a glasses frame — a concrete reference at circuit-diagram level.', S)
    add('https://blog.imaginationtech.com/chipsets-for-smart-glasses-and-other-high-end-wearables/', 'Giyilebilir Yonga Setleri', ['ücretsiz', 'makale'],
        'Üst seviye giyilebilirlerde yonga seçimini tartışan yazı; grafik ve güç dengesine odaklanması ayırt edici.',
        'An article on chipset selection for high-end wearables, distinguished by focusing on the graphics/power trade-off.', S)
