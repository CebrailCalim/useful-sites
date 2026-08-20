# -*- coding: utf-8 -*-
"""Öğrenme & Yol Haritaları · Pratik & Alıştırma · Programlama Dilleri"""


def load(add):
    # ============================================================ ÖĞRENME & YOL HARİTALARI
    O = 'ogrenme'
    add('https://roadmap.sh/linux', 'roadmap.sh · Linux', ['ücretsiz', 'yol-haritası', 'linux'],
        'Dosya sisteminden süreç yönetimine, kabuk betiğinden sistemd’ye kadar konuları bağımlılık '
        'sırasına dizen etkileşimli harita. Her düğümde ücretsiz kaynak bağlantısı var.',
        'An interactive map ordering topics by dependency — filesystem, process management, shell scripting, systemd — '
        'with free resources linked at each node.', O)
    add('https://roadmap.sh/blockchain', 'roadmap.sh · Blockchain', ['ücretsiz', 'yol-haritası', 'blockchain'],
        'Kriptografi temellerinden akıllı sözleşme ve Solidity’ye uzanan sıralı harita. '
        'Alanın gürültüsünde neyin gerçekten temel olduğunu ayırıyor.',
        'An ordered map running from cryptographic fundamentals to smart contracts and Solidity, '
        'separating what is actually foundational from the field’s noise.', O)
    add('https://github.com/ossu/computer-science', 'OSSU Computer Science', ['github', 'müfredat', 'ücretsiz'],
        'Ücretsiz kaynaklardan kurulmuş tam bir lisans müfredatı: ön koşullar, çekirdek dersler ve '
        'ileri seçmeliler ayrı ayrı sıralı. Kurs listesi değil, gerçekten bir program.',
        'A full undergraduate curriculum assembled from free material, with prerequisites, core courses and '
        'advanced electives each in order. Not a course list — an actual programme.', O)
    add('https://github.com/jwasham/coding-interview-university', 'Coding Interview University', ['github', 'mülakat', 'müfredat'],
        'Yazarın Amazon’a girerken tuttuğu çalışma planı; işaretlenebilir uzun bir kontrol listesi. '
        'Kapsamı geniş, o yüzden hepsini yapmak yerine eksiklerini bulmak için kullanılır.',
        'The study plan its author used to get into Amazon, as a long checkable list. The scope is wide, '
        'so it works better for finding your gaps than for completing end to end.', O)
    add('https://github.com/mtdvio/every-programmer-should-know', 'Every Programmer Should Know', ['github', 'awesome-liste'],
        'Dağıtık sistemlerden karakter kodlamasına, gecikme sayılarından güvenliğe uzanan konu derlemesi. '
        'Öğretmiyor; hangi konuyu hiç duymadığını fark ettiriyor.',
        'A compilation spanning distributed systems, character encoding, latency numbers and security. '
        'It does not teach — it shows you which topics you have never heard of.', O)
    add('https://github.com/codecrafters-io/build-your-own-x', 'Build Your Own X', ['github', 'proje', 'ücretsiz'],
        'Veritabanı, Git, Docker, işletim sistemi ve derleyiciyi sıfırdan yazma rehberleri. '
        'Öğretici izlemekle bir şeyi yeniden inşa etmek arasındaki anlama farkı ciddi.',
        'Guides to writing a database, Git, Docker, an operating system or a compiler from scratch. '
        'The gap in understanding between following a tutorial and rebuilding the thing is substantial.', O)
    add('https://github.com/CarterPerez-dev/Cybersecurity-Projects', 'Cybersecurity Projects', ['github', 'proje', 'güvenlik'],
        'Başlangıçtan ileriye 70 güvenlik projesi, her biri kaynak koduyla. '
        'Teori okumak yerine kendi araçlarını yazarak öğrenme yolu.',
        'Seventy security projects from beginner to advanced, each with source. '
        'Learning by writing your own tools rather than reading theory.', O)
    add('https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/?ref=lbp', 'Python Proje Fikirleri', ['ücretsiz', 'proje', 'python'],
        'Seviyeye göre gruplanmış Python proje listesi; her başlıkta kısa açıklama ve çalışan kod var. '
        'Ne yapacağını bilmediğin boş sayfa problemini çözüyor.',
        'A level-grouped list of Python projects, each with a short brief and working code — '
        'a fix for the blank-page problem of not knowing what to build.', O)
    add('https://learn-anything.xyz/c-libraries', 'Learn Anything', ['ücretsiz', 'graf', 'öğrenme'],
        'Konuları ve aralarındaki bağı graf olarak gösteriyor. Doğrusal müfredatın gizlediği '
        'komşu konular böyle görünür oluyor.',
        'Renders topics and their connections as a graph, which is how the adjacent subjects a linear curriculum '
        'hides become visible.', O)
    add('https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-langs.md#c', 'Free Programming Books', ['github', 'kitap', 'ücretsiz'],
        'Dile göre ayrılmış ücretsiz kitap listesi; alanın en büyük ve en aktif güncellenen derlemesi. '
        'Türkçe bölümü de var, çoğu benzer listede yok.',
        'A free-book list split by language and the largest actively maintained collection of its kind. '
        'It has a Turkish section, which most comparable lists lack.', O)
    add('https://neetcode.io/roadmap', 'NeetCode Roadmap', ['freemium', 'mülakat', 'algoritma'],
        'Algoritma sorularını konu bağımlılığına göre diziyor: iki işaretçiden kayan pencereye, '
        'oradan dinamik programlamaya. Rastgele soru çözmenin yapılandırılmış alternatifi.',
        'Orders algorithm problems by topic dependency — two pointers into sliding window into dynamic programming. '
        'The structured alternative to grinding random questions.', O)
    add('https://www.youtube.com/@abdul_bari/videos', 'Abdul Bari', ['video', 'ücretsiz', 'algoritma'],
        'Algoritmaları tahtada adım adım, karmaşıklık analiziyle birlikte işleyen kanal. '
        'Kod göstermek yerine mekanizmayı çizerek anlatması ders kitabına iyi bir eşlikçi.',
        'A channel working through algorithms on a board with complexity analysis. Drawing the mechanism rather '
        'than showing code makes it a good companion to a textbook.', O)
    add('https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo', 'Computer Science (Crash Course)', ['video', 'ücretsiz'],
        'Mantık kapılarından işletim sistemine, bilgisayar biliminin bütününü kısa bölümlerde tarayan seri. '
        'Derinlik değil, parçaların birbirine nasıl bağlandığını görmek için.',
        'A series sweeping the whole of computer science in short episodes, from logic gates to operating systems. '
        'Not for depth, but for seeing how the pieces connect.', O)
    add('https://www.youtube.com/watch?v=jTJvyKZDFsY&ab_channel=TheCodingSloth', '20 Programlama Projesi', ['video', 'ücretsiz', 'proje'],
        'Proje önerilerini hangi beceriyi geliştirdiği gerekçesiyle anlatan video. '
        'Liste okumaktan farkı, neden o projeyi yapman gerektiğini söylemesi.',
        'A video presenting project ideas with the reasoning for which skill each builds — '
        'unlike a list, it tells you why the project is worth doing.', O)
    add('https://www.youtube.com/watch?v=FCNg8KyMmGI&ab_channel=CodingwithLewis', '21 Proje Fikri', ['video', 'ücretsiz', 'proje'],
        'Zorluk sırasına dizilmiş proje fikirleri; baştan sona takip edilirse yol haritası gibi çalışıyor.',
        'Project ideas arranged by difficulty; followed end to end it works like a roadmap.', O)
    # eğitim platformları
    add('https://ocw.mit.edu/', 'MIT OpenCourseWare', ['ücretsiz', 'üniversite', 'ders-notu'],
        'MIT derslerinin ders notu, ödev, sınav ve çözümleriyle birlikte açık arşivi. '
        'Video kursların vermediği şey burada: gerçek problem setleri ve cevap anahtarları.',
        'MIT’s open archive of lecture notes, assignments, exams and solutions. What video courses do not give you '
        'is here: real problem sets with answer keys.', O)
    add('https://pll.harvard.edu/course/cs50-introduction-computer-science', 'CS50', ['ücretsiz', 'üniversite'],
        'Bilgisayar bilimine girişin ölçüt kabul edilen dersi; C ile başlayıp Python ve SQL’e geçiyor. '
        'Problem setleri otomatik değerlendiriliyor, yani geri bildirim gerçek.',
        'The benchmark introduction to computer science, starting in C and moving to Python and SQL. '
        'Problem sets are auto-graded, so the feedback is real.', O)
    add('https://see.stanford.edu/', 'Stanford Engineering Everywhere', ['ücretsiz', 'üniversite', 'arşiv'],
        'Stanford mühendislik derslerinin ücretsiz arşivi. Kayıtlar eski ama Andrew Ng’in '
        'makine öğrenmesi dersi gibi klasiklerin kaynağı burası.',
        'A free archive of Stanford engineering lectures. The recordings are dated, but this is the source of '
        'classics like Andrew Ng’s machine learning course.', O)
    add('https://pll.harvard.edu/', 'Harvard Online Learning', ['freemium', 'üniversite'],
        'Harvard’ın çevrimiçi ders kataloğu; ücretsiz izlenebilen derslerle ücretli sertifika '
        'programları aynı listede duruyor, hangisi olduğunu filtreden seçiyorsun.',
        'Harvard’s online catalogue, listing free-to-audit courses and paid certificate programmes together — '
        'you separate them with the filter.', O)
    add('https://lifelong-learning.ox.ac.uk/', 'Oxford Lifelong Learning', ['ücretli', 'üniversite'],
        'Oxford’un yarı zamanlı ve çevrimiçi sürekli eğitim programları. Ağırlıklı olarak ücretli '
        've akademik; teknik beceri kursundan çok üniversite dersi niteliğinde.',
        'Oxford’s part-time and online continuing education — mostly paid and academic, closer to university '
        'coursework than to skills training.', O)
    add('https://www.edx.org/', 'edX', ['freemium', 'kurs', 'üniversite'],
        'Üniversite kaynaklı kurs platformu. İçeriği izlemek çoğu derste ücretsiz; '
        'ödev değerlendirmesi ve sertifika ücretli katmanda kalıyor.',
        'A university-sourced course platform. Auditing is free for most courses; graded assignments and the '
        'certificate sit behind the paid tier.', O)
    add('https://www.theodinproject.com/', 'The Odin Project', ['ücretsiz', 'müfredat', 'frontend'],
        'Tam kapsamlı ücretsiz web geliştirme müfredatı. Video izletmiyor — resmî dokümanı okutup '
        'projeyi kendin kurdurtuyor, ki gerçek işe en yakın öğrenme biçimi bu.',
        'A complete free web development curriculum. It does not play you videos — it sends you to the official '
        'docs and makes you build, which is the closest thing to real work.', O)
    add('https://learn.microsoft.com/en-us/training/', 'Microsoft Learn', ['ücretsiz', 'dokümantasyon', 'azure'],
        'Modüler ücretsiz eğitim; sandbox’ta gerçek Azure kaynağı açtırıp uygulatıyor. '
        'Modüller sertifika sınavı hedeflerine birebir eşlenmiş durumda.',
        'Free modular training that spins up real Azure resources in a sandbox for you to work in. '
        'Modules map one to one onto certification exam objectives.', O)
    add('https://skillbuilder.aws/', 'AWS Skill Builder', ['freemium', 'bulut', 'aws'],
        'AWS’in resmî eğitim merkezi: 600+ ücretsiz kurs, sınav hazırlığı ve ücretli katmanda '
        'gerçek hesapta çalışan laboratuvarlar.',
        'AWS’s official learning centre — 600+ free courses, exam prep, and hands-on labs against real accounts '
        'in the paid tier.', O)
    add('https://skillsbuild.org/', 'IBM SkillsBuild', ['ücretsiz', 'kurs', 'sertifika'],
        'IBM’in ücretsiz beceri programı; yapay zeka, güvenlik ve veri yollarında dijital rozet veriyor. '
        'Öğrenci ve kariyer değiştirenlere yönelik kurgulanmış.',
        'IBM’s free skills programme awarding digital badges on AI, security and data tracks, '
        'shaped for students and career changers.', O)
    add('https://www.skills.google/', 'Google Skills', ['freemium', 'kurs', 'bulut'],
        'Google’ın eğitim ve sertifika platformu; Cloud Skills Boost laboratuvarlarını da içine almış durumda. '
        'Ücretsiz yolların yanında kredi gerektiren uygulamalı laboratuvarlar var.',
        'Google’s training and certification platform, now folding in the Cloud Skills Boost labs. '
        'Free tracks sit alongside hands-on labs that cost credits.', O)
    add('https://www.skills.google/paths/2336?locale=tr', 'Google AI Essentials', ['ücretsiz', 'türkçe', 'yapay-zeka'],
        'Yapay zekayı günlük işe katmayı anlatan giriş programı; kod yok, model matematiği yok. '
        'Teknik olmayan meslekler için tasarlanmış nadir kaynaklardan.',
        'An introduction to folding AI into everyday work — no code, no model mathematics. '
        'One of the rare resources actually designed for non-technical roles.', O)
    add('https://skillshop.exceedlms.com/student/catalog/list?category_ids=7899&locale=tr', 'Google Dijital Atölye', ['ücretsiz', 'türkçe', 'sertifika'],
        'Google’ın Türkçe dijital beceri kursları; dijital pazarlama sertifikası Avrupa’da tanınıyor. '
        'Türkçe içerik ve ücretsiz sertifika birleşimi yerelde ender.',
        'Google’s Turkish-language digital skills courses; the digital marketing certificate is recognised in Europe. '
        'Turkish content plus a free certificate is a rare pairing locally.', O)
    add('https://www.elementsofai.com/', 'Elements of AI', ['ücretsiz', 'yapay-zeka', 'giriş'],
        'Helsinki Üniversitesi’nin yapay zeka giriş dersi; programlama ve ileri matematik istemiyor. '
        'Kavramları felsefi ve toplumsal boyutuyla birlikte veriyor, salt teknik değil.',
        'The University of Helsinki’s AI introduction, requiring no programming or advanced maths and covering '
        'the philosophical and social dimensions alongside the technical.', O)
    add('https://www.datacamp.com/', 'DataCamp', ['ücretli', 'veri', 'interaktif'],
        'Kısa video sonrası tarayıcı içinde kod yazdırıp anında değerlendiriyor. '
        'Öğretme biçimi etkili ama alıştırmalar dar kalıplı; gerçek projeye geçişte boşluk bırakıyor.',
        'Short video then in-browser coding with instant grading. The format works, though the exercises are narrow '
        'and leave a gap when you move to a real project.', O)
    add('https://learn.unity.com/', 'Unity Learn', ['ücretsiz', 'oyun', '3b'],
        'Unity’nin resmî eğitimleri; motorun sürümüyle birlikte güncelleniyor. '
        'Üçüncü taraf kurslarda en sık karşılaşılan sorun olan sürüm uyumsuzluğu burada yok.',
        'Unity’s official training, updated in step with the engine. The version drift that plagues third-party '
        'courses does not occur here.', O)
    add('https://www.oreilly.com/', "O'Reilly", ['ücretli', 'kitap', 'video'],
        'Teknik kitap ve video aboneliği; erken erişim sürümleriyle henüz basılmamış kitapları okuyabiliyorsun. '
        'Tek tek satın almaya göre pahalı ama kapsam çok geniş.',
        'A subscription to technical books and video, including early-access editions of unpublished titles. '
        'Expensive against buying individually, but the catalogue is very wide.', O)
    add('https://www.thatquiz.org/tr/', 'ThatQuiz', ['ücretsiz', 'türkçe', 'matematik'],
        'Matematik ve temel konularda hızlı test üretip sonuçları toplayan araç; reklamsız ve hesapsız çalışıyor. '
        'Öğretmenler için hazırlık yükünü belirgin azaltıyor.',
        'Generates quick quizzes in maths and basic subjects and collects results, ad-free and account-free. '
        'It cuts teachers’ preparation load noticeably.', O)
    add('https://42turkiye.com.tr/', '42 Türkiye', ['ücretsiz', 'türkçe', 'okul'],
        'Öğretmensiz, akran değerlendirmeli ve ücretsiz yazılım okulu; diploma ya da ön bilgi şartı yok. '
        'Giriş, “piscine” denen dört haftalık yoğun eleme sürecinden geçiyor.',
        'A tuition-free software school with no teachers and peer evaluation, requiring no diploma or prior knowledge. '
        'Entry runs through a four-week intensive selection called the piscine.', O)
    add('https://www.kodluyoruz.org/', 'Kodluyoruz', ['ücretsiz', 'türkçe', 'topluluk'],
        'Türkiye’de ücretsiz yazılım eğitimi veren sosyal girişim; bootcamp’lerin ücret engelini '
        'kaldırmayı ve istihdama bağlamayı hedefliyor.',
        'A Turkish social enterprise offering free software training, aimed at removing the cost barrier of '
        'bootcamps and connecting graduates to jobs.', O)
    # sertifika
    add('https://aws.amazon.com/certification/', 'AWS Sertifikasyon', ['ücretli', 'sertifika', 'bulut'],
        'Rol bazlı sertifika programı (Solutions Architect, DevOps Engineer vb.). '
        'Bulut tarafında işveren tanınırlığı en yüksek belge ailesi; üç yılda bir yenileniyor.',
        'A role-based certification programme — Solutions Architect, DevOps Engineer and so on. '
        'The most employer-recognised credential family in cloud, renewable every three years.', O)
    add('https://education.github.com/experiences/foundations_certificate', 'GitHub Foundations', ['ücretli', 'sertifika', 'git'],
        'Sürüm kontrolü, işbirliği akışı ve GitHub yönetişimini kapsayan giriş seviyesi sınav. '
        'Kapsamı dar, o yüzden hazırlığı kısa.',
        'An entry-level exam covering version control, collaboration flow and GitHub governance. '
        'The scope is narrow, so preparation is short.', O)
    add('https://learning.lpi.org/en/', 'Linux Professional Institute', ['freemium', 'sertifika', 'linux'],
        'Dağıtımdan bağımsız Linux sertifikasyonu; Red Hat’in RHCSA’sı gibi tek satıcıya bağlı değil. '
        'Öğrenme materyalleri açık lisanslı ve ücretsiz indirilebiliyor.',
        'Distribution-neutral Linux certification, unlike vendor-bound credentials such as Red Hat’s RHCSA. '
        'Its learning material is openly licensed and downloadable.', O)
    add('https://www.broadcom.com/support/education/software/certification', 'Broadcom Sertifikasyon', ['ücretli', 'sertifika', 'kurumsal'],
        'Symantec ve VMware ürün ailelerine bağlı uzmanlık sınavları. '
        'Genel güvenlik ya da sanallaştırma bilgisi değil, belirli ürünün yapılandırılmasını ölçüyor.',
        'Product-bound specialist exams across the Symantec and VMware families — they measure configuration of a '
        'specific product, not general security or virtualisation knowledge.', O)
    add('https://claudecertificationguide.com/mock-exam', 'Claude Sertifika Denemesi', ['ücretsiz', 'sertifika', 'yapay-zeka'],
        'Claude Certified Architect sınavı için ücretsiz deneme; 28 soruluk kısa ve 60 soruluk '
        'tam uzunlukta iki kip, gerçek sınavın süre ve geçme eşiğiyle.',
        'A free mock for the Claude Certified Architect exam in two modes — a 28-question short form and a '
        'full 60-question run — matching the real timing and pass threshold.', O)

    # ============================================================ PRATİK & ALIŞTIRMA
    P = 'pratik'
    add('https://exercism.org/', 'Exercism', ['açık-kaynak', 'ücretsiz', 'alıştırma', 'mentor'],
        '70’ten fazla dilde alıştırma; çözdüğün soruya gönüllü bir mentorun yorum yazması '
        'onu diğerlerinden ayırıyor. Testler yerelde çalışıyor, kendi editörünü kullanabiliyorsun.',
        'Exercises in 70+ languages, distinguished by a volunteer mentor reviewing what you submitted. '
        'Tests run locally, so you stay in your own editor.', P)
    add('https://leetcode.com/', 'LeetCode', ['freemium', 'mülakat', 'algoritma'],
        'Teknik mülakat sorularının fiilî standardı; sorular şirket etiketiyle filtreleniyor. '
        'Tartışma bölümü çoğu zaman resmî çözümden öğreticidir.',
        'The de facto standard bank of interview questions, filterable by company tag. '
        'The discussion section is usually more instructive than the official solution.', P)
    add('https://www.codewars.com/', 'Codewars', ['ücretsiz', 'alıştırma', 'oyunlaştırılmış'],
        'Dövüş sanatı derecelendirmesiyle oyunlaştırılmış alıştırmalar. '
        'Asıl öğrenme çözümden sonra: aynı soruya başkalarının yazdığı çözümleri okuyorsun.',
        'Practice gamified with martial-arts ranks. The learning happens after you solve — '
        'you read what everyone else wrote for the same problem.', P)
    add('https://edabit.com/challenges', 'Edabit', ['freemium', 'alıştırma'],
        'Küçük ve hızlı bulmacalar; algoritma teorisi değil dil akıcılığı hedefliyor. '
        'Yeni bir dile geçerken sözdizimini oturtmak için LeetCode’dan uygun.',
        'Small, fast puzzles targeting language fluency rather than algorithm theory — '
        'better than LeetCode for settling syntax when you move to a new language.', P)
    add('https://projecteuler.net/', 'Project Euler', ['ücretsiz', 'matematik', 'algoritma'],
        'Kaba kuvvetin yetmediği matematik problemleri; çözüm sayı teorisi ya da kombinatorik içgörü gerektiriyor. '
        'Mülakat sorularıyla karıştırılmamalı, farklı bir kas çalıştırıyor.',
        'Mathematical problems where brute force does not finish; solutions need number theory or combinatorial insight. '
        'Not to be confused with interview questions — it trains a different muscle.', P)
    add('https://adventofcode.com/', 'Advent of Code', ['ücretsiz', 'alıştırma', 'etkinlik'],
        'Her aralık ayında günde bir bulmaca. Herkes aynı anda çözdüğü için tartışma ve '
        'çözüm karşılaştırması o hafta çok zengin oluyor; arşiv yıl boyu açık.',
        'One puzzle a day each December. Because everyone solves in sync the discussion that week is unusually rich; '
        'the archive stays open year round.', P)
    add('https://www.codedex.io/', 'Codédex', ['freemium', 'başlangıç', 'oyunlaştırılmış'],
        'Rol yapma oyunu temalı öğrenme; deneyim puanı ve harita ilerlemesiyle motivasyonu ayakta tutuyor. '
        'Tamamen yeni başlayanlar için tasarlanmış, ileri seviyeye çıkmıyor.',
        'RPG-themed learning that sustains motivation with XP and map progress. '
        'Built for complete beginners and it does not carry you to advanced.', P)
    add('https://coddy.tech/', 'Coddy', ['ücretsiz', 'interaktif', 'tarayıcı-içi'],
        '15+ dilde tarayıcı içi dersler; ortam kurulumu gerektirmiyor. '
        'Kurulum aşamasında pes eden yeni başlayanlar için gerçek bir engel kaldırıyor.',
        'In-browser lessons across 15+ languages with no environment setup — '
        'removing the barrier that stops beginners at installation.', P)
    add('https://www.hackerrank.com/', 'HackerRank', ['freemium', 'mülakat', 'sınav'],
        'Alıştırma ve işe alım sınavı aynı platformda; şirketler teknik testleri gerçekten burada uyguluyor. '
        'Yani sınav ortamını önceden tanımış oluyorsun.',
        'Practice and hiring assessments on one platform — companies genuinely run their technical tests here, '
        'so you get to know the exam environment in advance.', P)
    add('https://www.interviewcake.com/', 'Interview Cake', ['freemium', 'mülakat'],
        'Cevabı vermek yerine çözüme giden düşünce adımlarını açıyor; kaba kuvvetten optimale '
        'nasıl geçileceğini gösteriyor. Mülakatta beklenen tam olarak bu akıl yürütme.',
        'Opens up the reasoning steps rather than handing over the answer, showing how you move from brute force '
        'to optimal — which is exactly the reasoning an interview looks for.', P)
    add('https://www.algoexpert.io/product', 'AlgoExpert', ['ücretli', 'mülakat', 'video'],
        'Elenmiş bir soru seti ve her soru için video çözüm. Ücretli olmasının karşılığı, '
        'LeetCode’un binlerce sorusu içinde kaybolmadan sınırlı bir yolu bitirebilmen.',
        'A curated problem set with a video walkthrough for each. What the price buys is finishing a bounded path '
        'instead of getting lost among LeetCode’s thousands.', P)
    add('https://datalemur.com/', 'DataLemur', ['freemium', 'sql', 'mülakat'],
        'SQL ve veri bilimi mülakat soruları; tarayıcıda gerçek sorgu çalıştırıp doğruluyorsun. '
        'Genel algoritma platformlarının kapsamadığı bir boşluk.',
        'SQL and data science interview questions with real queries run and checked in the browser — '
        'a gap the general algorithm platforms leave open.', P)
    add('https://visualgo.net/en', 'VisuAlgo', ['ücretsiz', 'görselleştirme', 'algoritma'],
        'Veri yapısı ve algoritmaları adım adım canlandırıyor; kendi girdini verip izleyebiliyorsun. '
        'AVL ağacı dönmesi gibi konuları kod okuyarak anlamak çok daha zor.',
        'Animates data structures and algorithms step by step against input you supply. '
        'Something like an AVL rotation is far harder to grasp by reading code.', P)
    add('https://csvistool.com/', 'CS 1332 Görselleştirmeleri', ['ücretsiz', 'görselleştirme', 'algoritma'],
        'Georgia Tech’in veri yapıları dersi için hazırlanmış görselleştirme aracı. '
        'VisuAlgo’dan dar kapsamlı ama bir müfredata birebir oturuyor.',
        'A visualisation tool built for Georgia Tech’s data structures course — narrower than VisuAlgo '
        'but aligned exactly to a syllabus.', P)
    add('https://pythontutor.com/', 'Python Tutor', ['ücretsiz', 'görselleştirme', 'hata-ayıklama'],
        'Kodu satır satır çalıştırıp yığın çerçevelerini ve heap’teki nesneleri çiziyor. '
        'Referans, kapsam ve değişebilir varsayılan argüman hatalarını anlatmakta eşi yok.',
        'Steps through code drawing stack frames and heap objects. Nothing explains reference semantics, scope and '
        'mutable default arguments as clearly.', P)
    add('https://learngitbranching.js.org/', 'Learn Git Branching', ['ücretsiz', 'git', 'interaktif'],
        'Commit grafiğini canlı çizerek rebase, cherry-pick ve merge’ün ne yaptığını gösteriyor. '
        'Git’i komut ezberleyerek değil grafiği anlayarak öğrenmenin en kısa yolu.',
        'Draws the commit graph live to show what rebase, cherry-pick and merge actually do — '
        'the shortest path to learning Git by understanding the graph rather than memorising commands.', P)
    add('https://gitmastery.me/', 'GitMastery', ['ücretsiz', 'git', 'interaktif'],
        'Git komutlarını güvenli bir ortamda deneyip anında geri bildirim alıyorsun. '
        'Gerçek depoda hata yapma korkusu olmadan pratik.',
        'Run Git commands in a safe environment with immediate feedback — practice without the fear of breaking '
        'a real repository.', P)
    add('https://killercoda.com/', 'Killercoda', ['ücretsiz', 'devops', 'k8s', 'lab'],
        'Tarayıcıda gerçek Linux ve Kubernetes makinesi açıyor; simülasyon değil. '
        'CKA ve CKS sınavlarına hazırlık senaryoları resmî sınav ortamına çok yakın.',
        'Spins up a real Linux or Kubernetes machine in the browser — not a simulation. '
        'Its CKA and CKS scenarios sit very close to the actual exam environment.', P)
    add('https://10fastfingers.com/typing-test/turkish', '10FastFingers (Türkçe)', ['ücretsiz', 'türkçe', 'klavye'],
        'Türkçe kelime listesiyle yazma hızı testi; sonuçları kaydedip ilerlemeyi izleyebiliyorsun.',
        'A typing speed test on a Turkish word list, saving results so you can track progress.', P)
    add('https://www.m5bilisim.com/tr/on-parmak/', 'On Parmak Eğitimi', ['ücretsiz', 'türkçe', 'klavye'],
        'F ve Q düzenlerini ayrı ayrı destekleyen Türkçe on parmak eğitimi. '
        'F klavye materyalinin ücretsiz bulunması yerelde ender.',
        'Turkish touch-typing training supporting F and Q layouts separately. '
        'Free material for the F layout is rare locally.', P)

    # ============================================================ PROGRAMLAMA DİLLERİ
    L = 'diller'
    add('https://python.yazbel.com/', 'Yazbel Python Belgeleri', ['ücretsiz', 'türkçe', 'python'],
        'Python’un en kapsamlı Türkçe kaynağı ve çeviri değil; baştan Türkçe yazılmış olduğu için '
        'terimler zorlama durmuyor. Karakter kodlaması bölümü Türkçe metinle çalışanlar için özellikle değerli.',
        'The most comprehensive Turkish Python resource, written natively rather than translated, so the terminology '
        'does not feel forced. Its encoding chapter is especially valuable if you work with Turkish text.', L)
    add('https://www.freecodecamp.org/learn/python-v9/#lecture-introduction-to-python', 'freeCodeCamp Python', ['ücretsiz', 'python', 'sertifika'],
        'Ücretsiz müfredat ve sertifika; alıştırmalar tarayıcıda çalışıyor. '
        'Sertifika işveren nezdinde ağır basmıyor ama müfredat düzgün sıralanmış.',
        'A free curriculum and certificate with browser-based exercises. The certificate carries little weight with '
        'employers, but the curriculum is properly sequenced.', L)
    add('https://docs.astral.sh/uv/', 'uv', ['açık-kaynak', 'rust', 'python', 'araç'],
        'Rust ile yazılmış paket ve proje yöneticisi; pip’ten onlarca kat hızlı. '
        'venv, pip, pip-tools ve pyenv’in işini tek ikili dosyada topluyor.',
        'A package and project manager written in Rust, tens of times faster than pip. '
        'It collapses venv, pip, pip-tools and pyenv into a single binary.', L)
    add('https://omerfi.medium.com/python-virtual-environment-venv-nedir-981788752e5a', 'Sanal Ortam (venv) Nedir?', ['ücretsiz', 'türkçe', 'python'],
        'Python sanal ortamlarını Türkçe anlatan kısa giriş; kavramı ilk kez duyanlar için yeterli. '
        'Modern araç zinciri artık uv tarafına kayıyor, onu da bilmekte fayda var.',
        'A short Turkish introduction to Python virtual environments, sufficient on first contact. '
        'The modern toolchain is shifting toward uv, which is worth knowing alongside.', L)
    add('https://www.youtube.com/indently', 'Indently', ['video', 'ücretsiz', 'python'],
        'Tek bir Python kavramını derinleştiren kısa bölümler; uzun kurs formatına almayan konuları işliyor.',
        'Short episodes each deepening one Python concept, covering things a long-course format skips.', L)
    add('https://cppreference.com/', 'cppreference', ['ücretsiz', 'c++', 'c', 'referans'],
        'C ve C++ standart kütüphanesinin fiilî referansı; her özellikte hangi standartta (C++11/17/20/23) '
        'geldiği işaretli. Öğretici siteler bu sürüm ayrımını genelde atlıyor.',
        'The de facto reference for the C and C++ standard library, marking which standard (C++11/17/20/23) each '
        'feature landed in — a distinction tutorial sites usually skip.', L)
    add('https://www.learn-c.org/', 'Learn C', ['ücretsiz', 'c', 'interaktif'],
        'Tarayıcıda derleyip çalıştırabildiğin C öğreticisi. '
        'Derleyici kurmadan dile bakmak isteyenler için giriş engelini kaldırıyor.',
        'A C tutorial you compile and run in the browser, removing the entry barrier for anyone who wants a look '
        'at the language before installing a toolchain.', L)
    add('https://www.tutorialspoint.com/cprogramming/index.htm', 'C Programming Tutorial', ['ücretsiz', 'c'],
        'Baştan sona klasik C anlatımı. Kapsamlı ama üslubu ve örnekleri eski; '
        'sıralı okumaktan çok tek konu aramak için pratik.',
        'A classic front-to-back treatment of C. Comprehensive, but dated in style and examples — '
        'handier for looking one topic up than for reading through.', L)
    add('https://www.geeksforgeeks.org/c/c-programming-language/', 'GeeksforGeeks C', ['ücretsiz', 'c'],
        'Konu başlığına bölünmüş C kaynağı; arama sonucundan doğrudan ilgili sayfaya düşüyorsun. '
        'Örnek kodların bir kısmı eski derleyici davranışına dayanıyor, dikkatli okumak gerekiyor.',
        'C material split by topic so a search lands you straight on the relevant page. '
        'Some examples rely on old compiler behaviour, so read carefully.', L)
    add('https://www.includehelp.com/c-programs/c-programs-basic-input-output-operations.aspx', 'IncludeHelp C Programları', ['ücretsiz', 'c', 'örnek'],
        'Çözülmüş C programları koleksiyonu; anlatım yok, doğrudan çalışan örnek var. '
        'Bir kalıbı hızla hatırlamak için elverişli.',
        'A collection of solved C programs — no exposition, just working examples. Handy for recalling a pattern quickly.', L)
    add('https://kodisyum.com/c-ornekler/', 'Kodisyum C Örnekleri', ['ücretsiz', 'türkçe', 'c'],
        'Türkçe C örnek programları; ders ödevi düzeyindeki klasik alıştırmaları kapsıyor. '
        'Yerelde C kaynağı kıt olduğu için değerli.',
        'Turkish C example programs covering the classic coursework-level exercises — valuable because Turkish C '
        'material is thin on the ground.', L)
    add('https://github.com/oz123/awesome-c', 'Awesome C', ['github', 'awesome-liste', 'c'],
        'C kütüphane, çatı ve araç listesi. Dilin standart kütüphanesi kasten dar olduğu için '
        'C’de “hangi kütüphane” sorusu diğer dillerden çok daha sık sorulur.',
        'A list of C libraries, frameworks and tools. Because the standard library is deliberately thin, '
        '“which library” comes up far more often in C than elsewhere.', L)
    add('https://github.com/Koubae/Programming-CookBook/blob/master/Programming%20Languages/C/roadmap.md', 'C Yol Haritası', ['github', 'yol-haritası', 'c'],
        'C öğrenimini konu sırasına koyan kısa harita; işaretçi ve bellek yönetimini nereye '
        'yerleştireceğini gösteriyor.',
        'A short map ordering C topics, showing where pointers and memory management belong in the sequence.', L)
    add('https://llvm.org/docs/GettingStartedTutorials.html', 'LLVM Başlangıç', ['dokümantasyon', 'derleyici', 'c++'],
        'LLVM altyapısına giriş ve Kaleidoscope öğreticisi — kendi dilini yazmanın klasik başlangıcı. '
        'Ara temsil (IR) kavramını somutlaştıran en iyi kaynaklardan.',
        'An introduction to the LLVM infrastructure plus the Kaleidoscope tutorial, the classic starting point for '
        'writing your own language and one of the best ways to make the IR concept concrete.', L)
    add('https://holyc-lang.com/', 'HolyC', ['açık-kaynak', 'dil', 'derleyici'],
        'TempleOS’un HolyC dili için bağımsız derleyici ve dokümantasyon. '
        'Pratik bir kullanımı yok; dil tasarımı ve bilgisayar tarihi merakı için duruyor.',
        'An independent compiler and documentation for TempleOS’s HolyC. No practical use — '
        'it stands for the language design and computing history interest.', L)
    add('https://www.youtube.com/watch?v=yuVatFCOISc', 'Sıfırdan C Programlama', ['video', 'türkçe', 'c'],
        'C dilini tek oturumda anlatan Türkçe video; hızlı giriş ya da sınav öncesi tekrar için.',
        'A Turkish video covering C in a single sitting — for a fast introduction or pre-exam revision.', L)
    add('https://www.youtube.com/watch?v=uhAnt4Iw1VQ&t=802s', 'Canlı C++ Kodlama', ['video', 'c++'],
        'C++ öğrenme sürecinin canlı kaydı; derleyici hataları ve çıkmaz sokaklar kesilmemiş. '
        'Cilalı derslerin gizlediği gerçek süreci gösteriyor.',
        'An uncut recording of learning C++, compiler errors and dead ends included — '
        'the real process that polished lectures hide.', L)
    add('https://go.dev/tour/welcome/1', 'A Tour of Go', ['ücretsiz', 'go', 'interaktif'],
        'Go’nun resmî turu; her örnek tarayıcıda çalıştırılıp değiştirilebiliyor. '
        'Goroutine ve kanalları anlatan son bölüm dilin asıl ayırt edici kısmı.',
        'Go’s official tour, with every example runnable and editable in the browser. '
        'The closing section on goroutines and channels is the language’s real differentiator.', L)
    add('https://gobyexample.com/', 'Go by Example', ['ücretsiz', 'go', 'örnek'],
        'Her kavramı yorumlu tek bir programla anlatıyor. Turu bitirdikten sonra '
        '“bunu Go’da nasıl yapıyordum” sorusunun cevabı burada.',
        'Explains each concept through one annotated program. After the tour, this is where '
        '“how do I do that in Go again” gets answered.', L)
    add('https://eloquentjavascript.net/', 'Eloquent JavaScript', ['ücretsiz', 'kitap', 'javascript'],
        'Ücretsiz ve çevrimiçi klasik. Sözdizimi öğretmekten çok programlama düşüncesi kuruyor; '
        'alıştırmaları kitabın içinde çalıştırılabiliyor.',
        'A free online classic that builds programming thinking rather than teaching syntax, '
        'with exercises runnable inside the book itself.', L)
    add('https://jsexercises.com/', 'JS Exercises', ['ücretsiz', 'javascript', 'alıştırma'],
        'Tarayıcıda çalıştırılabilir JavaScript alıştırmaları; okuma sonrası pekiştirme için.',
        'Runnable JavaScript exercises in the browser, for consolidating after reading.', L)
    add('https://rust-lang.org/tr/learn/', 'Rust Öğrenin (Türkçe)', ['ücretsiz', 'türkçe', 'rust'],
        'Rust’ın resmî öğrenme sayfasının Türkçe hâli. Sahiplik (ownership) ve ödünç alma '
        'kavramlarına kendi dilinde girmek, dilin en dik yokuşunu biraz yumuşatıyor.',
        'The Turkish version of Rust’s official learning page. Meeting ownership and borrowing in your own language '
        'softens the language’s steepest climb a little.', L)
    add('https://fortran-lang.org/', 'Fortran', ['ücretsiz', 'fortran', 'bilimsel'],
        'Modern Fortran topluluğunun sitesi; fpm paket yöneticisi ve güncel derleyiciler burada. '
        'Dil sayısal hesaplama ve iklim modellemede hâlâ üretimde, tarihî merak değil.',
        'The modern Fortran community site, home to the fpm package manager and current compilers. '
        'The language is still in production in numerical computing and climate modelling — not a historical curiosity.', L)
