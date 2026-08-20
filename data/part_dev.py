# -*- coding: utf-8 -*-
"""Öğrenme, Pratik, Diller, Web, Backend, Mobil"""


def load(add):
    # ============================================================ ÖĞRENME & YOL HARİTALARI
    O = 'ogrenme'
    add('https://roadmap.sh/linux', 'roadmap.sh · Linux', ['ücretsiz', 'yol haritası'],
        'Linux öğrenme yolunu adım adım şemalaştıran interaktif harita; kurs listesinden farkı, neyi hangi sırayla öğreneceğini göstermesi.',
        'An interactive map laying out the Linux learning path step by step; unlike a course list it shows what to learn in which order.', O)
    add('https://roadmap.sh/blockchain', 'roadmap.sh · Blockchain', ['ücretsiz', 'yol haritası'],
        'Blockchain geliştiriciliği için sıralı öğrenme haritası; her düğümde önerilen kaynaklar bağlantılı.',
        'An ordered learning map for blockchain development, with suggested resources linked at each node.', O)
    add('https://github.com/ossu/computer-science', 'OSSU Computer Science', ['ücretsiz', 'github', 'müfredat'],
        'Ücretsiz kaynaklardan derlenmiş eksiksiz bilgisayar bilimi lisans müfredatı; rastgele kurs listesi değil, üniversite programı sırasını izler.',
        'A complete CS degree curriculum assembled from free resources — it follows a university programme’s ordering, not a random course list.', O)
    add('https://github.com/jwasham/coding-interview-university', 'Coding Interview University', ['ücretsiz', 'github', 'mülakat'],
        'Yazılım mühendisliği mülakatına hazırlık için çalışma planı; konu listesinden farkı, işaretlenebilir bir ilerleme sistemi sunması.',
        'A study plan for software engineering interviews; unlike a topic list it gives you a checkable progress system.', O)
    add('https://github.com/mtdvio/every-programmer-should-know', 'Every Programmer Should Know', ['ücretsiz', 'github', 'koleksiyon'],
        'Her geliştiricinin bilmesi beklenen teknik konuların derlemesi; öğretmez, bilgi boşluklarını fark ettirir.',
        'A collection of technical topics every developer is expected to know — it does not teach, it reveals your gaps.', O)
    add('https://github.com/codecrafters-io/build-your-own-x', 'Build Your Own X', ['ücretsiz', 'github', 'proje'],
        'Veritabanı, işletim sistemi, Git gibi araçları sıfırdan yazma rehberleri; öğretici izlemek yerine yeniden inşa ederek öğrenme yaklaşımı.',
        'Guides to writing databases, operating systems and Git from scratch — learning by rebuilding rather than following tutorials.', O)
    add('https://github.com/CarterPerez-dev/Cybersecurity-Projects', 'Cybersecurity Projects', ['ücretsiz', 'github', 'proje', 'güvenlik'],
        'Başlangıçtan ileri seviyeye 70 güvenlik projesi; teoriden çok yapılacak iş listesi sunması ayırt edici yanı.',
        '70 security projects from beginner to advanced — offering a to-build list rather than theory is what sets it apart.', O)
    add('https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/?ref=lbp', 'Python Proje Fikirleri', ['ücretsiz', 'proje'],
        'Seviyeye göre sıralanmış Python proje listesi; her biri kısa açıklama ve kaynak kodla birlikte.',
        'A level-ordered list of Python projects, each with a short description and source code.', O)
    add('https://learn-anything.xyz/c-libraries', 'Learn Anything', ['ücretsiz', 'harita'],
        'Konular arası bağlantıyı graf olarak gösteren öğrenme haritası; doğrusal müfredatlardan farkı komşu konuları görünür kılması.',
        'A learning map showing topics as a connected graph; unlike linear curricula it makes neighbouring subjects visible.', O)
    add('https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md#c', 'Free Programming Books', ['ücretsiz', 'github', 'kitap'],
        'Dile göre ayrılmış ücretsiz programlama kitapları listesi; alanın en büyük ve en aktif güncellenen derlemesi.',
        'Free programming books organised by language — the largest and most actively maintained collection of its kind.', O)
    add('https://neetcode.io/roadmap', 'NeetCode Roadmap', ['freemium', 'mülakat', 'yol haritası'],
        'Algoritma sorularını bağımlılık sırasına dizen harita; rastgele soru çözmeye karşı yapılandırılmış alternatif.',
        'A map ordering algorithm problems by dependency — the structured alternative to grinding random questions.', O)
    add('https://www.youtube.com/@abdul_bari/videos', 'Abdul Bari', ['ücretsiz', 'video', 'algoritma'],
        'Algoritma ve veri yapılarını tahtada adım adım anlatan kanal; görsel anlatımıyla ders kitabına iyi bir tamamlayıcı.',
        'Channel explaining algorithms and data structures step by step on a board — a good visual complement to textbooks.', O)
    add('https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo', 'Computer Science (CrashCourse)', ['ücretsiz', 'video'],
        'Bilgisayar biliminin temel kavramlarını kısa bölümlerle anlatan seri; derinlik değil bütünü görme amaçlı.',
        'A series covering CS fundamentals in short episodes — aimed at seeing the whole picture rather than depth.', O)
    add('https://www.youtube.com/watch?v=jTJvyKZDFsY&ab_channel=TheCodingSloth', '20 Programlama Projesi', ['ücretsiz', 'video', 'proje'],
        'Beceri geliştiren proje önerilerini gerekçesiyle anlatan video; liste okumaktan farkı, neden o projenin işe yaradığını açıklaması.',
        'A video walking through skill-building project ideas with reasoning — unlike a list, it explains why each project helps.', O)
    add('https://www.youtube.com/watch?v=FCNg8KyMmGI&ab_channel=CodingwithLewis', '21 Proje Fikri', ['ücretsiz', 'video', 'proje'],
        'Başlangıçtan ileri seviyeye proje fikirleri; zorluk sırasına göre ilerlemesiyle yol haritası gibi kullanılabiliyor.',
        'Project ideas from beginner to advanced, progressing by difficulty so it doubles as a roadmap.', O)
    # eğitim platformları
    add('https://ocw.mit.edu/', 'MIT OpenCourseWare', ['ücretsiz', 'üniversite'],
        'MIT derslerinin ders notu, ödev ve sınavlarıyla birlikte açık arşivi; video kurslardan farkı, gerçek ders materyalinin tamamını vermesi.',
        'MIT’s open archive of course notes, assignments and exams — unlike video courses it gives the full real course material.', O)
    add('https://pll.harvard.edu/course/cs50-introduction-computer-science', 'CS50 (Harvard)', ['ücretsiz', 'üniversite'],
        'Bilgisayar bilimine giriş dersinin altın standardı; anlatım kalitesi ve ödev tasarımıyla çoğu ücretli kursun önünde.',
        'The gold standard intro to computer science; its lecture quality and problem-set design outclass most paid courses.', O)
    add('https://see.stanford.edu/', 'Stanford Engineering Everywhere', ['ücretsiz', 'üniversite'],
        'Stanford mühendislik derslerinin ücretsiz arşivi; klasik yapay zeka ve sistem derslerinin kaynağı olarak değerli.',
        'Free archive of Stanford engineering courses, valuable as the source of the classic AI and systems lectures.', O)
    add('https://pll.harvard.edu/', 'Harvard Online Learning', ['freemium', 'üniversite'],
        'Harvard’ın çevrimiçi ders kataloğu; ücretsiz derslerle sertifikalı programların bir arada listelendiği giriş noktası.',
        'Harvard’s online course catalogue — the entry point where free courses and certificate programmes are listed together.', O)
    add('https://lifelong-learning.ox.ac.uk/', 'Oxford Lifelong Learning', ['ücretli', 'üniversite'],
        'Oxford’un yarı zamanlı ve çevrimiçi sürekli eğitim programları; çoğu ücretli, akademik yönü ağır basıyor.',
        'Oxford’s part-time and online continuing education; mostly paid, with a strongly academic bent.', O)
    add('https://www.edx.org/', 'edX', ['freemium', 'kurs'],
        'Üniversite kaynaklı çevrimiçi kurs platformu; içeriği izlemek genelde ücretsiz, sertifika ücretli.',
        'University-sourced online course platform — auditing is usually free, certificates are paid.', O)
    add('https://www.theodinproject.com/', 'The Odin Project', ['ücretsiz', 'web', 'müfredat'],
        'Tam kapsamlı ücretsiz web geliştirme müfredatı; video ağırlıklı kurslardan farkı, projeyi kendin kurup dokümantasyon okumaya zorlaması.',
        'A complete free web development curriculum; unlike video-heavy courses it forces you to build and read documentation yourself.', O)
    add('https://learn.microsoft.com/en-us/training/', 'Microsoft Learn', ['ücretsiz', 'dokümantasyon'],
        'Microsoft teknolojileri için ücretsiz modüler eğitim; sertifika sınavlarına doğrudan eşlenmesi ayırt edici yanı.',
        'Free modular training for Microsoft technologies, distinguished by mapping directly onto certification exams.', O)
    add('https://skillbuilder.aws/', 'AWS Skill Builder', ['freemium', 'bulut'],
        'AWS’in resmî eğitim merkezi; 600+ ücretsiz kurs ve sınav hazırlığı bir arada.',
        'AWS’s official learning centre, combining 600+ free courses with exam preparation.', O)
    add('https://skillsbuild.org/', 'IBM SkillsBuild', ['ücretsiz', 'kurs'],
        'IBM’in ücretsiz beceri eğitimi programı; yapay zeka ve güvenlik tarafında rozet veren yolları var.',
        'IBM’s free skills programme, with badge-awarding paths in AI and security.', O)
    add('https://www.skills.google/', 'Google Skills', ['freemium', 'kurs'],
        'Google’ın eğitim ve sertifika platformu; bulut ve yapay zeka yollarını tek yerde toplar.',
        'Google’s training and certification platform, consolidating cloud and AI paths in one place.', O)
    add('https://www.skills.google/paths/2336?locale=tr', 'Google AI Essentials', ['ücretsiz', 'yapay zeka', 'türkçe'],
        'Yapay zekayı iş akışında kullanmaya odaklı giriş programı; teknik değil, uygulamaya dönük.',
        'An introductory programme on using AI in daily work — applied rather than technical.', O)
    add('https://skillshop.exceedlms.com/student/catalog/list?category_ids=7899&locale=tr', 'Google Dijital Atölye', ['ücretsiz', 'türkçe', 'sertifika'],
        'Google’ın Türkçe dijital beceri kursları; pazarlama ve temel kodlama tarafında ücretsiz sertifika veriyor.',
        'Google’s Turkish-language digital skills courses, giving free certificates in marketing and basic coding.', O)
    add('https://www.elementsofai.com/', 'Elements of AI', ['ücretsiz', 'yapay zeka'],
        'Programlama ve ileri matematik gerektirmeyen yapay zeka giriş kursu; teknik olmayanlar için tasarlanmış nadir kaynaklardan.',
        'An AI introduction requiring no programming or advanced maths — one of the rare courses genuinely designed for non-technical readers.', O)
    add('https://www.datacamp.com/', 'DataCamp', ['ücretli', 'veri'],
        'Tarayıcı içinde alıştırmalı veri bilimi kursları; video izlemek yerine her adımda kod yazdırması ayırt edici.',
        'Data science courses with in-browser exercises — it makes you write code at each step rather than watch video.', O)
    add('https://learn.unity.com/', 'Unity Learn', ['ücretsiz', 'oyun'],
        'Unity’nin resmî oyun geliştirme eğitimleri; motorun kendi sürümüyle güncel kalması üçüncü taraf kurslara üstünlüğü.',
        'Unity’s official game development training; staying current with the engine’s own releases is its edge over third-party courses.', O)
    add('https://www.oreilly.com/', "O'Reilly", ['ücretli', 'kitap'],
        'Teknik kitap ve video aboneliği; tek tek satın almaya karşı geniş kütüphaneye erişim modeli sunar.',
        'Subscription to technical books and video — access to a broad library instead of buying titles one by one.', O)
    add('https://www.thatquiz.org/tr/', 'ThatQuiz', ['ücretsiz', 'türkçe', 'matematik'],
        'Matematik ve temel konularda hızlı test üretme aracı; öğretmenler için hazırlık yükünü azaltıyor.',
        'Quick quiz generator for maths and basic subjects, cutting preparation time for teachers.', O)
    add('https://42turkiye.com.tr/', '42 Türkiye', ['ücretsiz', 'türkçe', 'okul'],
        'Öğretmensiz ve akran değerlendirmeli yazılım okulu; ücretsiz olması ve diploma şartı aramaması ayırt edici yanı.',
        'A tuition-free software school with no teachers and peer evaluation; requiring no prior diploma is what sets it apart.', O)
    add('https://www.kodluyoruz.org/', 'Kodluyoruz', ['ücretsiz', 'türkçe', 'topluluk'],
        'Türkiye’de ücretsiz yazılım eğitimi veren sosyal girişim; bootcamp’lere erişim engelini kaldırmayı hedefliyor.',
        'A Turkish social enterprise offering free software training, aimed at removing the access barrier to bootcamps.', O)
    # sertifika
    add('https://aws.amazon.com/certification/', 'AWS Sertifikasyon', ['ücretli', 'sertifika', 'bulut'],
        'AWS’in rol bazlı sertifika programı; bulut tarafında işverence en çok tanınan belgelerden.',
        'AWS’s role-based certification programme — among the most recognised credentials on the cloud side.', O)
    add('https://education.github.com/experiences/foundations_certificate', 'GitHub Foundations', ['ücretli', 'sertifika'],
        'GitHub’ın giriş seviyesi sertifikası; sürüm kontrolü ve iş akışı temellerini belgelemek için.',
        'GitHub’s entry-level certification, for evidencing version control and workflow fundamentals.', O)
    add('https://learning.lpi.org/en/', 'Linux Professional Institute', ['freemium', 'sertifika', 'linux'],
        'Dağıtımdan bağımsız Linux sertifikasyonu; Red Hat gibi satıcıya bağlı belgelerden farkı bu tarafsızlığı.',
        'Distribution-neutral Linux certification — that neutrality is what separates it from vendor-tied credentials.', O)
    add('https://www.broadcom.com/support/education/software/certification', 'Broadcom / Symantec Sertifikasyon', ['ücretli', 'sertifika', 'güvenlik'],
        'Symantec güvenlik ürünleri üzerine uzmanlık sertifikaları; belirli bir ürün ailesine bağlı, genel güvenlik belgesi değil.',
        'Specialist certifications on Symantec security products — tied to a product family rather than general security knowledge.', O)
    add('https://claudecertificationguide.com/mock-exam', 'Claude Sertifika Deneme Sınavı', ['ücretsiz', 'sertifika', 'yapay zeka'],
        'Claude Certified Architect sınavı için ücretsiz deneme; gerçek sınavın soru sayısı ve süresini taklit ediyor.',
        'A free mock for the Claude Certified Architect exam, mirroring the real question count and timing.', O)

    # ============================================================ PRATİK & ALIŞTIRMA
    P = 'pratik'
    add('https://exercism.org/', 'Exercism', ['ücretsiz', 'açık kaynak', 'alıştırma'],
        '70+ dilde alıştırma ve gönüllü mentor geri bildirimi; diğer platformlardan farkı, çözümüne insan yorumu alabilmen.',
        'Exercises in 70+ languages with volunteer mentor feedback — getting a human review of your solution is what sets it apart.', P)
    add('https://leetcode.com/', 'LeetCode', ['freemium', 'mülakat', 'algoritma'],
        'Teknik mülakat sorularının fiilî standardı; şirket etiketli soru havuzu başlıca avantajı.',
        'The de facto standard for technical interview questions; its company-tagged problem pool is the main draw.', P)
    add('https://www.codewars.com/', 'Codewars', ['ücretsiz', 'alıştırma'],
        'Dövüş sanatı derecelendirmesiyle oyunlaştırılmış kod alıştırmaları; çözüm sonrası başkalarının kodunu görmek öğreticiliğini artırıyor.',
        'Gamified coding practice with martial-arts ranks; seeing other people’s solutions after solving is where most of the learning happens.', P)
    add('https://edabit.com/challenges', 'Edabit', ['freemium', 'alıştırma'],
        'Küçük ve hızlı kod bulmacaları; LeetCode’un aksine algoritma teorisi değil, dil pratiği hedefliyor.',
        'Small, fast coding puzzles; unlike LeetCode it targets language fluency rather than algorithm theory.', P)
    add('https://projecteuler.net/', 'Project Euler', ['ücretsiz', 'matematik', 'algoritma'],
        'Matematik ağırlıklı programlama problemleri; mülakat sorularından farkı, çözümün algoritmadan çok sayı teorisine dayanması.',
        'Mathematics-heavy programming problems; unlike interview questions the solution rests on number theory more than algorithms.', P)
    add('https://adventofcode.com/', 'Advent of Code', ['ücretsiz', 'alıştırma', 'etkinlik'],
        'Her aralık ayında yayımlanan günlük bulmaca takvimi; topluluk aynı anda çözdüğü için tartışma ve çözüm karşılaştırması zengin.',
        'A daily puzzle calendar published each December; because the community solves in sync, discussion and solution comparison are rich.', P)
    add('https://www.codedex.io/', 'Codédex', ['freemium', 'oyunlaştırılmış', 'başlangıç'],
        'Rol yapma oyunu temalı kodlama öğrenme platformu; motivasyonu deneyim puanı ve harita ilerlemesiyle kurması ayırt edici.',
        'An RPG-themed learn-to-code platform, distinguished by driving motivation through XP and map progression.', P)
    add('https://coddy.tech/', 'Coddy', ['ücretsiz', 'interaktif'],
        '15+ dilde tarayıcı içi etkileşimli dersler; kurulum gerektirmemesi başlangıç engelini düşürüyor.',
        'In-browser interactive lessons in 15+ languages; needing no setup lowers the barrier to starting.', P)
    add('https://www.hackerrank.com/', 'HackerRank', ['freemium', 'mülakat'],
        'Alıştırma ve işe alım testlerini birleştiren platform; LeetCode’dan farkı, şirketlerin sınavı burada uygulaması.',
        'Combines practice with hiring assessments; unlike LeetCode, companies actually run their tests here.', P)
    add('https://www.interviewcake.com/', 'Interview Cake', ['freemium', 'mülakat'],
        'Mülakat sorularını çözümün düşünce adımlarıyla anlatan kaynak; cevabı vermek yerine nasıl vardığını göstermesi ayırt edici.',
        'Explains interview questions through the reasoning steps; showing how you get there rather than handing you the answer is its distinction.', P)
    add('https://www.algoexpert.io/product', 'AlgoExpert', ['ücretli', 'mülakat'],
        'Video çözümlü mülakat hazırlık platformu; ücretli olması karşılığında düzenli ve elenmiş bir soru seti sunar.',
        'Interview prep with video walkthroughs; in exchange for the price you get a curated, non-sprawling problem set.', P)
    add('https://datalemur.com/', 'DataLemur', ['freemium', 'sql', 'mülakat'],
        'SQL ve veri bilimi mülakat soruları; genel algoritma platformlarının kapsamadığı bir boşluğu dolduruyor.',
        'SQL and data science interview questions, filling a gap the general algorithm platforms do not cover.', P)
    add('https://visualgo.net/en', 'VisuAlgo', ['ücretsiz', 'görselleştirme', 'algoritma'],
        'Veri yapısı ve algoritmaları adım adım canlandıran görselleştirme; kodu okumadan mekanizmayı anlamak için.',
        'Step-by-step animation of data structures and algorithms — for understanding the mechanism without reading code.', P)
    add('https://csvistool.com/', 'CS 1332 Görselleştirmeleri', ['ücretsiz', 'görselleştirme', 'algoritma'],
        'Georgia Tech’in veri yapıları dersi için hazırlanmış görselleştirme aracı; VisuAlgo’ya göre daha dar ama ders akışına uyumlu.',
        'Visualisation tool built for Georgia Tech’s data structures course — narrower than VisuAlgo but aligned to a syllabus.', P)
    add('https://pythontutor.com/', 'Python Tutor', ['ücretsiz', 'görselleştirme', 'hata ayıklama'],
        'Kodun bellekteki durumunu satır satır gösteren görselleştirici; referans ve kapsam hatalarını anlatmakta eşsiz.',
        'Visualises memory state line by line — unmatched for explaining reference and scope bugs.', P)
    add('https://learngitbranching.js.org/', 'Learn Git Branching', ['ücretsiz', 'git', 'interaktif'],
        'Git dallanmasını görsel ve etkileşimli öğreten alıştırma; komut ezberlemek yerine grafiği anlamayı sağlıyor.',
        'Teaches Git branching visually and interactively — you learn the graph instead of memorising commands.', P)
    add('https://gitmastery.me/', 'GitMastery', ['ücretsiz', 'git', 'interaktif'],
        'Git komutlarını güvenli bir ortamda denetip geri bildirim veren alıştırma platformu.',
        'Practice platform for running Git commands in a safe environment with feedback.', P)
    add('https://killercoda.com/', 'Killercoda', ['ücretsiz', 'devops', 'interaktif'],
        'Tarayıcıda gerçek Linux ve Kubernetes ortamı veren senaryolar; simülasyon değil gerçek makine sunması ayırt edici.',
        'Scenarios giving you a real Linux and Kubernetes environment in the browser — real machines, not a simulation.', P)
    add('https://10fastfingers.com/typing-test/turkish', '10FastFingers (Türkçe)', ['ücretsiz', 'türkçe', 'klavye'],
        'Türkçe klavye hız testi; günlük pratikle yazma hızını ölçmek için basit ve reklamsız denecek kadar sade.',
        'Turkish typing speed test — simple enough to use for daily practice measurement.', P)
    add('https://www.m5bilisim.com/tr/on-parmak/', 'On Parmak Eğitimi', ['ücretsiz', 'türkçe', 'klavye'],
        'Türkçe on parmak klavye eğitimi; F ve Q düzenlerini ayrı ayrı desteklemesi yerel bir avantaj.',
        'Turkish touch-typing course; supporting both F and Q layouts separately is a locally useful advantage.', P)

    # ============================================================ PROGRAMLAMA DİLLERİ
    L = 'diller'
    add('https://python.yazbel.com/', 'Yazbel Python Belgeleri', ['ücretsiz', 'türkçe', 'python'],
        'Python’un en kapsamlı Türkçe kaynağı; çeviri değil, sıfırdan Türkçe yazılmış olması ayırt edici yanı.',
        'The most comprehensive Turkish Python resource — written natively in Turkish rather than translated.', L)
    add('https://www.freecodecamp.org/learn/python-v9/#lecture-introduction-to-python', 'freeCodeCamp Python', ['ücretsiz', 'python', 'sertifika'],
        'Ücretsiz Python müfredatı ve sertifikası; alıştırmaların tarayıcıda çalışması kurulum engelini kaldırıyor.',
        'Free Python curriculum and certificate; running exercises in the browser removes the setup barrier.', L)
    add('https://docs.astral.sh/uv/', 'uv', ['açık kaynak', 'python', 'araç'],
        'Rust ile yazılmış çok hızlı Python paket ve proje yöneticisi; pip, venv ve pip-tools’un yerini tek araçta topluyor.',
        'An extremely fast Python package and project manager written in Rust, replacing pip, venv and pip-tools with one tool.', L)
    add('https://omerfi.medium.com/python-virtual-environment-venv-nedir-981788752e5a', 'Sanal Ortam (venv) Nedir?', ['ücretsiz', 'türkçe', 'python'],
        'Python sanal ortamlarını Türkçe anlatan giriş yazısı; kavramı ilk kez duyanlar için kısa ve yeterli.',
        'A Turkish introduction to Python virtual environments — short and sufficient for a first encounter.', L)
    add('https://www.youtube.com/indently', 'Indently', ['ücretsiz', 'video', 'python'],
        'Kısa Python ipuçları yayımlayan kanal; uzun kurs yerine tek kavramı derinleştiren bölümler.',
        'A channel publishing short Python tips — single-concept episodes rather than long courses.', L)
    add('https://cppreference.com/', 'cppreference', ['ücretsiz', 'c++', 'referans'],
        'C ve C++ standart kütüphanesinin fiilî referansı; öğreticilerden farkı, standardın kendisine sadık ve sürüm farklarını göstermesi.',
        'The de facto reference for the C and C++ standard library; unlike tutorials it tracks the standard itself and marks version differences.', L)
    add('https://www.learn-c.org/', 'Learn C', ['ücretsiz', 'c', 'interaktif'],
        'Tarayıcıda çalıştırılabilir C öğreticisi; kurulum yapmadan dili denemek için en kısa yol.',
        'A C tutorial you can run in the browser — the shortest path to trying the language without installing anything.', L)
    add('https://www.tutorialspoint.com/cprogramming/index.htm', 'C Programming Tutorial', ['ücretsiz', 'c'],
        'C dilinin klasik baştan sona öğreticisi; kapsamlı ama üslubu eski, referans olarak daha kullanışlı.',
        'A classic end-to-end C tutorial — comprehensive but dated in style, more useful as a reference.', L)
    add('https://www.geeksforgeeks.org/c/c-programming-language/', 'GeeksforGeeks C', ['ücretsiz', 'c'],
        'Konu başlıklarına bölünmüş C kaynağı; sırayla okumaktan çok tek bir konuyu aramak için elverişli.',
        'C material split by topic — better for looking one thing up than reading front to back.', L)
    add('https://www.includehelp.com/c-programs/c-programs-basic-input-output-operations.aspx', 'IncludeHelp C Programları', ['ücretsiz', 'c', 'örnek'],
        'Çözülmüş C programları koleksiyonu; anlatım değil, örnek üzerinden öğrenmek isteyenler için.',
        'A collection of solved C programs — for learning from examples rather than exposition.', L)
    add('https://kodisyum.com/c-ornekler/', 'Kodisyum C Örnekleri', ['ücretsiz', 'türkçe', 'c'],
        'Türkçe C örnek programları; yerel kaynak kıtlığı olan bir alanda pratik derleme.',
        'Turkish C example programs — a practical collection in an area with few local resources.', L)
    add('https://github.com/oz123/awesome-c', 'Awesome C', ['ücretsiz', 'github', 'koleksiyon', 'c'],
        'C kütüphane ve araçlarının derlenmiş listesi; dilin standart kütüphanesi dar olduğu için özellikle değerli.',
        'A curated list of C libraries and tools — especially valuable because the language’s standard library is thin.', L)
    add('https://github.com/Koubae/Programming-CookBook/blob/master/Programming%20Languages/C/roadmap.md', 'C Yol Haritası', ['ücretsiz', 'github', 'c'],
        'C öğrenimini sıraya koyan kısa yol haritası; kapsamlı müfredat değil, konu sırası rehberi.',
        'A short roadmap ordering C topics — a sequence guide rather than a full curriculum.', L)
    add('https://llvm.org/docs/GettingStartedTutorials.html', 'LLVM Başlangıç', ['ücretsiz', 'dokümantasyon', 'derleyici'],
        'LLVM derleyici altyapısına giriş; kendi dilini yazmak isteyenlerin başlangıç noktası.',
        'Introduction to the LLVM compiler infrastructure — the starting point for writing your own language.', L)
    add('https://holyc-lang.com/', 'HolyC', ['açık kaynak', 'dil'],
        'TempleOS’un HolyC dilinin bağımsız derleyici ve dokümantasyonu; pratik değil, dil tasarımı meraklıları için.',
        'An independent compiler and docs for TempleOS’s HolyC — not practical, but of interest for language design.', L)
    add('https://www.youtube.com/watch?v=yuVatFCOISc', 'Sıfırdan C Programlama (Türkçe)', ['ücretsiz', 'türkçe', 'video', 'c'],
        'C dilini tek oturumda anlatan Türkçe video; hızlı giriş veya tekrar için.',
        'A Turkish video covering C in one sitting — for a fast introduction or a refresher.', L)
    add('https://www.youtube.com/watch?v=uhAnt4Iw1VQ&t=802s', 'Canlı C++ Kodlama', ['ücretsiz', 'video', 'c++'],
        'C++ öğrenme sürecini canlı kodlayarak gösteren video; cilalı ders yerine gerçek hata ayıklama süreci içeriyor.',
        'A live-coding video of learning C++ — real debugging rather than a polished lecture.', L)
    add('https://go.dev/tour/welcome/1', 'A Tour of Go', ['ücretsiz', 'go', 'interaktif'],
        'Go’nun resmî etkileşimli turu; her örneğin tarayıcıda çalıştırılabilmesiyle dilin standart giriş kapısı.',
        'Go’s official interactive tour — the standard entry point, with every example runnable in the browser.', L)
    add('https://gobyexample.com/', 'Go by Example', ['ücretsiz', 'go', 'örnek'],
        'Go kavramlarını yorumlu örneklerle anlatan referans; tur bittikten sonra bakılacak ikinci kaynak.',
        'Go concepts explained through annotated examples — the second stop after finishing the tour.', L)
    add('https://eloquentjavascript.net/', 'Eloquent JavaScript', ['ücretsiz', 'kitap', 'javascript'],
        'JavaScript’in ücretsiz klasik kitabı; söz dizimi öğretmekten çok programlama düşüncesi kurmasıyla ayrışıyor.',
        'The free classic JavaScript book, distinguished by teaching programming thinking rather than just syntax.', L)
    add('https://jsexercises.com/', 'JS Exercises', ['ücretsiz', 'javascript', 'alıştırma'],
        'Tarayıcıda çalıştırılabilir JavaScript alıştırmaları; okuma sonrası pratik için.',
        'Runnable JavaScript exercises in the browser, for practice after reading.', L)
    add('https://rust-lang.org/tr/learn/', 'Rust Öğrenin (Türkçe)', ['ücretsiz', 'türkçe', 'rust'],
        'Rust’ın resmî öğrenme sayfasının Türkçe hâli; dilin kendi kaynaklarına Türkçe giriş noktası.',
        'The Turkish version of Rust’s official learning page — a native-language entry into the official material.', L)
    add('https://fortran-lang.org/', 'Fortran', ['ücretsiz', 'fortran', 'bilimsel'],
        'Fortran’ın modern topluluk sitesi; dilin hâlâ sayısal hesaplamada canlı olduğunu gösteren güncel araç ve kütüphaneler.',
        'Fortran’s modern community site, showing the current tooling that keeps the language alive in numerical computing.', L)
