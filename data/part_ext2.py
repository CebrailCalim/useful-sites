# -*- coding: utf-8 -*-
"""Records from the external list - tools, AI, systems, interviews.

Source: Best-websites-a-programmer-should-visit. See part_ext1.py.
"""

SRC = 'bwapsv'


def load(add):
    def a(url, name, tags, tr, en, cat):
        add(url, name, tags, tr, en, cat, SRC)

    # ============================================================ TOOLS
    T = 'araclar'
    a('https://codepen.io', 'CodePen', ['freemium', 'tarayıcı-içi', 'frontend'],
      'HTML, CSS ve JavaScript’i tarayıcıda deneyip paylaştığın oyun alanı. '
      'Asıl değeri keşif tarafı: başkalarının CSS numaralarını sökerek öğreniyorsun.',
      'A browser playground for HTML, CSS and JavaScript. The real value is discovery — you learn by '
      'taking apart other people’s CSS tricks.', T)
    a('https://codesandbox.io', 'CodeSandbox', ['freemium', 'tarayıcı-içi'],
      'Tarayıcıda tam npm bağımlılıklı proje çalıştırıyor; CodePen’den farkı, '
      'gerçek bir React ya da Node projesini olduğu gibi açabilmesi.',
      'Runs projects with full npm dependencies in the browser. Unlike CodePen it opens a real React or '
      'Node project as-is.', T)
    a('https://stackblitz.com/', 'StackBlitz', ['freemium', 'tarayıcı-içi'],
      'WebContainer ile Node.js’i doğrudan tarayıcıda çalıştırıyor; sunucuya gitmediği için '
      'kurulum ve yeniden başlatma anlık. Çevrimdışı bile çalışabiliyor.',
      'Runs Node.js in the browser through WebContainers, so install and restart are instant with no '
      'server round trip — it even works offline.', T)
    a('https://jsfiddle.net', 'JSFiddle', ['ücretsiz', 'tarayıcı-içi', 'javascript'],
      'Küçük JavaScript parçalarını denemenin en eski ve en hafif yolu; '
      'hata raporlarına tekrar üretilebilir örnek eklemek için standart araç.',
      'The oldest and lightest way to test a small JavaScript snippet — the standard tool for attaching '
      'a reproducible example to a bug report.', T)
    a('https://jsbin.com/', 'JS Bin', ['ücretsiz', 'tarayıcı-içi', 'javascript'],
      'JSFiddle’a benzer, canlı çıktı paneli olan kod alanı; '
      'konsol çıktısını aynı ekranda göstermesi hata ayıklamada pratik.',
      'A JSFiddle-like scratchpad with a live output panel; showing console output on the same screen '
      'is handy when debugging.', T)
    a('https://ideone.com', 'Ideone', ['ücretsiz', 'tarayıcı-içi'],
      '60’tan fazla dili tarayıcıda derleyip çalıştırıyor, girdi akışı verebiliyorsun. '
      'Kurulum yapmadan bir dilin sözdizimini denemek için.',
      'Compiles and runs 60+ languages in the browser and accepts an input stream — for trying a '
      'language’s syntax without installing anything.', T)
    a('https://ide.judge0.com', 'Judge0 IDE', ['açık-kaynak', 'tarayıcı-içi'],
      'Açık kaynak çevrimiçi derleyici; motoru kendi sunucunda çalıştırabiliyorsun. '
      'Kod değerlendirme sistemi kuranların altyapı olarak kullandığı proje.',
      'An open-source online compiler whose engine you can self-host — the project people building code '
      'assessment systems use as infrastructure.', T)
    a('https://wandbox.org/', 'Wandbox', ['ücretsiz', 'tarayıcı-içi', 'c-ailesi'],
      'C++ derleyicilerinin onlarca sürümünü yan yana çalıştırıyor; '
      'bir davranışın hangi standarttan ya da hangi derleyici sürümünden geldiğini test etmek için.',
      'Runs dozens of C++ compiler versions side by side — for testing which standard or compiler '
      'release a behaviour comes from.', T)
    a('https://runjs.app/play', 'RunJS', ['freemium', 'javascript'],
      'Yazdıkça sonucu gösteren JavaScript oyun alanı; '
      'konsola `console.log` yazmadan değişkenin değerini görebiliyorsun.',
      'A JavaScript playground that evaluates as you type, showing a variable’s value without a '
      '`console.log`.', T)
    a('https://gist.github.com', 'GitHub Gist', ['ücretsiz', 'github'],
      'Tek dosyalık kod parçalarını sürüm geçmişiyle paylaşma servisi; '
      'yorum ve çatallama desteği olduğu için pastebin’den kalıcı.',
      'Shares single-file snippets with version history; comments and forking make it more durable than '
      'a pastebin.', T)
    a('https://pastebin.com', 'Pastebin', ['ücretsiz'],
      'Metin ve günlük paylaşmanın en basit yolu; sözdizimi vurgulama ve süre sınırı var. '
      'Hassas veri yapıştırmamak gerektiğini akılda tutmalı.',
      'The simplest way to share text or a log, with syntax highlighting and expiry. '
      'Worth remembering not to paste anything sensitive.', T)
    a('https://codeshare.io', 'CodeShare', ['ücretsiz', 'tarayıcı-içi'],
      'Tarayıcıda gerçek zamanlı ortak kod düzenleme; kurulum ve hesap gerektirmiyor. '
      'Uzaktan eşli programlama ya da mülakat için hızlı çözüm.',
      'Real-time collaborative code editing in the browser with no install or account — a fast option '
      'for remote pairing or an interview.', T)
    a('https://crontab.guru/', 'Crontab Guru', ['ücretsiz'],
      'Cron ifadesini yazdıkça düz dille ne anlama geldiğini ve sonraki çalışma zamanlarını gösteriyor. '
      'Yıldız ve eğik çizgi kombinasyonlarını tahmin etmeye son veriyor.',
      'Translates a cron expression into plain language as you type and shows the next run times, '
      'ending the guesswork over asterisks and slashes.', T)
    a('https://regexr.com', 'RegExr', ['ücretsiz'],
      'Düzenli ifade test aracı; regex101’e alternatif, arayüzü daha sade ve '
      'topluluk örnekleri kütüphanesi var.',
      'A regex tester and an alternative to regex101, with a simpler interface and a community library '
      'of patterns.', T)
    a('https://www.gitignore.io/', 'gitignore.io', ['ücretsiz', 'git'],
      'İşletim sistemi, editör ve dil seçerek `.gitignore` dosyası üretiyor. '
      'Her projede aynı satırları elle yazmaya son veriyor.',
      'Generates a `.gitignore` from your operating system, editor and language choices — '
      'the end of retyping the same lines on every project.', T)
    a('https://app.diagrams.net/', 'diagrams.net', ['ücretsiz', 'görsel-üretim'],
      'draw.io’nun çevrimiçi sürümü; dosyayı Drive, OneDrive ya da yerel diske kaydediyor, '
      'kendi sunucusunda tutmuyor.',
      'The online edition of draw.io, saving to Drive, OneDrive or local disk rather than keeping your '
      'file on its own server.', T)
    a('https://www.ray.so/', 'ray.so', ['ücretsiz', 'görsel-üretim'],
      'Kod parçasından paylaşılabilir görsel üretiyor; Carbon’a alternatif, '
      'daha az ayar ve daha hızlı sonuç.',
      'Turns a snippet into a shareable image — a Carbon alternative with fewer knobs and a faster result.', T)
    a('https://coolors.co/', 'Coolors', ['freemium', 'görsel-üretim'],
      'Renk paleti üreteci; boşluk tuşuyla yeni kombinasyon deniyor, beğendiğini kilitleyip '
      'gerisini yeniliyorsun. Kontrast denetimi de var.',
      'A palette generator — hit space for a new combination, lock what you like and regenerate the rest. '
      'It checks contrast too.', T)
    a('https://cors-error.dev/cors-tester/', 'CORS Tester', ['ücretsiz', 'api'],
      'Bir API’nin CORS başlıklarını dışarıdan test ediyor; '
      'tarayıcı konsolundaki belirsiz CORS hatasının hangi başlıktan geldiğini söylüyor.',
      'Tests an API’s CORS headers from the outside, telling you which header causes the vague CORS '
      'error in the browser console.', T)
    a('https://graphonline.ru/en/', 'Graph Online', ['ücretsiz', 'algoritma'],
      'Tarayıcıda graf çizip üzerinde en kısa yol, bağlantılılık ve akış algoritmalarını çalıştırıyor. '
      'Graf algoritmalarını sınamak için kod yazmadan.',
      'Draw a graph in the browser and run shortest path, connectivity and flow algorithms on it — '
      'testing graph algorithms without writing code.', T)
    a('https://osquery.io', 'osquery', ['açık-kaynak', 'güvenlik', 'ağ'],
      'İşletim sistemini SQL ile sorgulanabilir hâle getiriyor: çalışan süreçler, açık portlar ve '
      'kurulu paketler birer tablo. Uç nokta izlemede yaygın.',
      'Turns the operating system into something you query with SQL — running processes, open ports and '
      'installed packages become tables. Common in endpoint monitoring.', T)
    a('http://vorillaz.github.io/devicons/#/main', 'Devicons', ['ücretsiz', 'görsel-üretim'],
      'Programlama dili ve araç logolarının ikon fontu; '
      'özgeçmiş, sunum ve README’lerde teknoloji rozeti olarak kullanılıyor.',
      'An icon font of programming language and tool logos, used as technology badges in CVs, slides '
      'and READMEs.', T)
    a('https://lottiefiles.com/', 'LottieFiles', ['freemium', 'görsel-üretim'],
      'Hafif JSON tabanlı vektör animasyonların arşivi ve düzenleyicisi; '
      'GIF’e göre çok küçük dosyayla ölçeklenebilir animasyon veriyor.',
      'An archive and editor of lightweight JSON-based vector animations, giving scalable motion at a '
      'fraction of a GIF’s file size.', T)
    a('https://www.uidesigndaily.com/', 'UI Design Daily', ['ücretsiz', 'görsel-üretim'],
      'Her gün yayımlanan ücretsiz arayüz bileşeni tasarımları; kaynak dosyaları da açık, '
      'Figma ve Sketch biçiminde indirilebiliyor.',
      'Free UI component designs published daily, with the source files open and downloadable in Figma '
      'and Sketch format.', T)
    a('https://devurls.com/', 'DevURLs', ['ücretsiz', 'referans'],
      'Hacker News, Reddit, Lobsters ve onlarca kaynağı tek sayfada toplayan haber panosu. '
      'Ayrı ayrı gezmek yerine tek bakışta tarama imkânı.',
      'A news board gathering Hacker News, Reddit, Lobsters and dozens more on one page — one glance '
      'instead of visiting each.', T)

    # ============================================================ SYSTEM & SHELL
    A = 'ag'
    a('http://tldp.org/LDP/abs/html/', 'Advanced Bash-Scripting Guide', ['ücretsiz', 'kitap'],
      'Bash betiklemenin en kapsamlı ücretsiz referansı; her konu çalıştırılabilir örnekle. '
      'Üslubu eski ama kapsamı hâlâ eşsiz.',
      'The most comprehensive free reference on Bash scripting, every topic with a runnable example. '
      'Dated in style, still unmatched in coverage.', A)
    a('http://www.tldp.org/LDP/Bash-Beginners-Guide/html/', 'Bash Guide for Beginners', ['ücretsiz', 'öğretici'],
      'Kabuk betiklerine giriş; Advanced rehberin ağırlığına girmeden temelleri kuruyor.',
      'An introduction to shell scripting that lays the groundwork without the weight of the advanced guide.', A)
    a('https://www.gnu.org/software/bash/manual/bashref.html', 'Bash Referans Kılavuzu', ['ücretsiz', 'dokümantasyon'],
      'Bash’in resmî kılavuzu; genişletme kuralları ve parametre değiştirme gibi '
      'tartışmalı konularda son söz burada.',
      'Bash’s official manual — the final word on contested topics like expansion rules and parameter '
      'substitution.', A)
    a('http://mywiki.wooledge.org/BashGuide', 'BashGuide (Wooledge)', ['ücretsiz', 'öğretici'],
      'İnternetteki kötü Bash örneklerine karşı düzeltici bir rehber; '
      'tırnaklama ve sözcük bölme gibi en sık yapılan hataları merkeze alıyor.',
      'A corrective to the bad Bash examples circulating online, centred on the most common mistakes '
      'like quoting and word splitting.', A)
    a('https://github.com/dylanaraps/pure-bash-bible', 'Pure Bash Bible', ['github', 'kopya-kâğıdı'],
      'Dış program çağırmadan Bash’in kendi araçlarıyla iş yapma koleksiyonu. '
      'sed ve awk çağrılarını kaldırdığı için betikleri belirgin hızlandırıyor.',
      'A collection of ways to do things with Bash’s own facilities instead of calling external programs, '
      'which speeds scripts up markedly by removing sed and awk calls.', A)
    a('https://www.commandlinefu.com/commands/browse', 'Command-line Fu', ['ücretsiz', 'cli'],
      'Kullanıcıların paylaştığı UNIX komut tek satırlıkları arşivi, oyla sıralı. '
      'Bir işin kısa yolu var mı diye bakmak için.',
      'An archive of user-submitted UNIX one-liners ranked by vote — where you check whether a shortcut '
      'exists for a task.', A)

    # ============================================================ AI & DATA
    V = 'veri'
    a('http://course.fast.ai', 'fast.ai', ['ücretsiz', 'müfredat', 'veri-bilimi'],
      'Derin öğrenmeyi tepeden aşağı öğreten kurs: önce çalışan model, sonra teori. '
      'Matematikle başlayan akademik derslerin tam tersi bir sıra izliyor.',
      'Teaches deep learning top-down — a working model first, theory after. The exact inverse of the '
      'academic courses that open with mathematics.', V)
    a('https://www.deeplearning.ai', 'DeepLearning.AI', ['freemium', 'müfredat', 'veri-bilimi'],
      'Andrew Ng’in kurduğu eğitim platformu; derin öğrenme ve üretken YZ üzerine '
      'yapılandırılmış uzmanlık programları.',
      'Andrew Ng’s education platform, offering structured specialisations in deep learning and '
      'generative AI.', V)
    a('https://developers.google.com/machine-learning/crash-course', 'ML Crash Course', ['ücretsiz', 'müfredat', 'veri-bilimi'],
      'Google’ın makine öğrenmesine hızlı girişi; kısa video, okuma ve çalıştırılabilir '
      'alıştırma üçlüsüyle ilerliyor.',
      'Google’s fast introduction to machine learning, moving through short video, reading and runnable '
      'exercises.', V)
    a('https://mlcourse.ai/', 'mlcourse.ai', ['ücretsiz', 'müfredat', 'veri-bilimi'],
      'Açık makine öğrenmesi kursu; teori ile Kaggle yarışması ödevlerini birleştirmesi '
      'onu salt anlatımdan ayırıyor.',
      'An open machine learning course whose pairing of theory with Kaggle competition assignments '
      'separates it from lecture-only material.', V)
    a('https://mlu-explain.github.io/', 'MLU-Explain', ['ücretsiz', 'interaktif', 'veri-bilimi'],
      'Amazon’un makine öğrenmesi kavramlarını etkileşimli görsellerle anlatan seti; '
      'parametreyi kaydırıp modelin nasıl değiştiğini görüyorsun.',
      'Amazon’s set explaining machine learning concepts through interactive visuals — you drag a '
      'parameter and watch the model change.', V)
    a('https://machinelearningmastery.com/', 'Machine Learning Mastery', ['ücretsiz', 'öğretici', 'veri-bilimi'],
      'Uygulama odaklı ML öğreticileri; her yazı çalışan bir kod örneğiyle bitiyor. '
      'Teoriden çok “bunu nasıl yaparım” sorusuna cevap veriyor.',
      'Application-focused ML tutorials, each ending in working code — answering “how do I do this” '
      'rather than the theory.', V)
    a('http://aima.cs.berkeley.edu', 'AIMA', ['ücretsiz', 'kitap', 'akademik'],
      'Yapay Zeka: Modern Yaklaşım kitabının kaynak sayfası; ders kodu ve '
      'algoritma uygulamaları birden çok dilde yayımlanmış.',
      'The companion site for Artificial Intelligence: A Modern Approach, publishing course code and '
      'algorithm implementations in several languages.', V)
    a('https://github.com/SerpentAI/SerpentAI', 'SerpentAI', ['github', 'veri-bilimi'],
      'Herhangi bir video oyununu pekiştirmeli öğrenme ortamına çeviren çatı. '
      'Simülasyon yerine gerçek oyunla çalışması ayrıksı.',
      'A framework turning any video game into a reinforcement learning environment — working against '
      'real games rather than simulations is what makes it unusual.', V)

    # ============================================================ INTERVIEWS
    P = 'pratik'
    a('http://bigocheatsheet.com/#', 'Big-O Cheat Sheet', ['ücretsiz', 'kopya-kâğıdı', 'algoritma', 'mülakat'],
      'Veri yapıları ve sıralama algoritmalarının zaman ve alan karmaşıklıklarını tek tabloda '
      'renk kodlu gösteriyor. Mülakat öncesi son bakış için.',
      'A single colour-coded table of time and space complexity for data structures and sorting '
      'algorithms — the last look before an interview.', P)
    a('http://ssp.impulsetrain.com/big-o.html', 'Big-O Yanılgıları', ['ücretsiz', 'algoritma'],
      'Büyük-O gösterimi üzerine yaygın yanlış anlamaları düzelten yazı; '
      'en kötü durum ile ortalama durumun karıştırılması gibi.',
      'A piece correcting common misunderstandings of big-O notation, such as conflating worst case '
      'with average case.', P)
    a('https://www.hiredintech.com/algorithm-design', 'Algorithm Design Canvas', ['ücretsiz', 'mülakat'],
      'Mülakatta algoritma problemine yaklaşmak için adımlı bir çerçeve: kısıtlar, örnekler, '
      'kaba kuvvet, iyileştirme, test. Panik yerine yöntem sunuyor.',
      'A stepwise framework for approaching an interview algorithm problem — constraints, examples, '
      'brute force, optimise, test. Method instead of panic.', P)
    a('http://web.stanford.edu/class/cs9/', 'Stanford CS9', ['ücretsiz', 'mülakat', 'algoritma'],
      'Teknik mülakat için problem çözme dersi; Stanford’un ders materyali açık. '
      'Soru bankası değil, düşünme biçimi öğretiyor.',
      'Stanford’s problem-solving course for technical interviews with open materials — it teaches a '
      'way of thinking rather than a question bank.', P)
    a('https://gist.github.com/dideler/2365607', 'Bit İşlemleri Numaraları', ['ücretsiz', 'algoritma'],
      'Bit düzeyinde sık kullanılan numaraların derlemesi; '
      'düşük seviye optimizasyon ve mülakat sorularında karşına çıkan kalıplar.',
      'A collection of common bit-level tricks — the patterns that turn up in low-level optimisation '
      'and interview questions.', P)
    a('https://github.com/Twipped/InterviewThis', 'InterviewThis', ['github', 'mülakat'],
      'Mülakatta şirkete sorulacak soruların listesi; yön değiştirip '
      'iş yerini değerlendirmene yarıyor.',
      'A list of questions to ask the company in an interview — it flips the direction so you can '
      'assess the workplace.', P)
    a('https://github.com/sherxon/AlgoDS', 'AlgoDS', ['github', 'algoritma'],
      'Algoritma ve veri yapılarının Java uygulamaları; '
      'her biri testleriyle birlikte, okunabilir biçimde yazılmış.',
      'Java implementations of algorithms and data structures, each written readably and with tests.', P)

    # ============================================================ OPEN SOURCE & OTHER
    R = 'referans'
    a('https://sourceforge.net', 'SourceForge', ['ücretsiz', 'referans'],
      'Açık kaynak projelerin eski dağıtım platformu; GitHub öncesinin arşivi. '
      'Hâlâ bakılıyor çünkü bazı eski projelerin tek kaynağı burası.',
      'The older distribution platform for open-source projects and an archive of the pre-GitHub era. '
      'Still consulted because some old projects exist nowhere else.', R)
    a('https://launchpad.net', 'Launchpad', ['ücretsiz', 'referans'],
      'Canonical’ın proje barındırma ve hata takip platformu; '
      'Ubuntu paketlerinin hata kayıtları burada tutuluyor.',
      'Canonical’s project hosting and bug tracker — where Ubuntu package bug reports live.', R)
    a('https://www.baeldung.com', 'Baeldung', ['freemium', 'öğretici', 'backend'],
      'Java, Spring ve REST üzerine kısa ve odaklı öğreticiler; '
      'her yazı tek bir soruyu çalışan kodla cevaplıyor.',
      'Short, focused tutorials on Java, Spring and REST, each answering a single question with '
      'working code.', R)
