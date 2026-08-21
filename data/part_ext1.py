# -*- coding: utf-8 -*-
"""Records from the external list - learning, practice, languages, reference.

Source: Best-websites-a-programmer-should-visit (an archived compilation).
Of its 702 links, roughly 140 were taken: the ones still alive, not already
here, and inside this directory's scope. Personal blogs, dead course pages
and domains that had been taken over were dropped.

These carry src='bwapsv' and show up in the interface as "External List".
"""

SRC = 'bwapsv'


def load(add):
    def a(url, name, tags, tr, en, cat):
        add(url, name, tags, tr, en, cat, SRC)

    # ============================================================ LEARNING
    O = 'ogrenme'
    a('https://roadmap.sh/', 'roadmap.sh', ['ücretsiz', 'müfredat'],
      'Bütün yol haritalarının kök sayfası; frontend’den DevOps’a, Python’dan siber güvenliğe '
      'onlarca alan için sıralı öğrenme haritası. Tek bir alanın haritasına değil, hangi alanların '
      'olduğuna bakmak için burası.',
      'The root page for every roadmap — frontend to DevOps, Python to security. Come here to see which '
      'tracks exist rather than to follow one.', O)
    a('https://www.class-central.com', 'Class Central', ['ücretsiz', 'müfredat'],
      'Coursera, edX ve onlarca platformdaki kursları tek yerde arayan dizin. '
      'Aynı konunun farklı üniversitelerdeki sürümlerini yan yana koyup karşılaştırıyorsun.',
      'A search index across Coursera, edX and dozens more, letting you line up different universities’ '
      'versions of the same subject side by side.', O)
    a('https://www.coursera.org', 'Coursera', ['freemium', 'müfredat'],
      'Üniversite ve şirket ortaklıklı kurs platformu. Çoğu ders ücretsiz izlenebiliyor; '
      'ödev değerlendirmesi ve sertifika ücretli katmanda.',
      'Course platform partnered with universities and companies. Most lectures are free to audit; '
      'graded work and certificates sit behind the paid tier.', O)
    a('https://www.pluralsight.com', 'Pluralsight', ['ücretli', 'müfredat'],
      'Kurumsal teknoloji eğitimi aboneliği; beceri ölçüm testleri ve öğrenme yolları var. '
      'Tek tek kurs almak yerine bir yığında derinleşmek için tasarlanmış.',
      'A subscription for enterprise technology training with skill assessments and paths, '
      'designed for going deep in one stack rather than buying courses one at a time.', O)
    a('https://www.boot.dev/', 'Boot.dev', ['freemium', 'müfredat', 'interaktif'],
      'Backend geliştiriciliğine odaklı, tarayıcıda alıştırma yaptıran müfredat. '
      'Genel bootcamp’lerin aksine yalnızca sunucu tarafına bakıyor.',
      'A backend-focused curriculum with in-browser exercises. Unlike general bootcamps '
      'it looks only at the server side.', O)
    a('http://mooc.fi/english.html', 'MOOC.fi', ['ücretsiz', 'müfredat'],
      'Helsinki Üniversitesi’nin açık kursları; Java ve Python programlama dersleri '
      'otomatik değerlendirmeli alıştırmalarla geliyor.',
      'The University of Helsinki’s open courses, with Java and Python programming taught through '
      'auto-graded exercises.', O)
    a('https://github.com/prakhar1989/awesome-courses', 'Awesome CS Courses', ['github', 'awesome-liste', 'müfredat'],
      'Üniversitelerin çevrimiçi yayımladığı bilgisayar bilimi derslerinin listesi; '
      'ders notu ve ödevleri açık olanlara odaklanıyor.',
      'A list of university computer science courses published online, focused on those whose lecture '
      'notes and assignments are open.', O)
    a('https://github.com/karan/Projects', 'Projects', ['github', 'müfredat'],
      'Herhangi bir dilde çözülebilecek pratik proje listesi; matematik, metin işleme, ağ gibi '
      'başlıklara ayrılmış. Dil öğrenirken ne yazacağını bilememe sorununa karşı.',
      'A list of practical projects solvable in any language, split into maths, text processing, '
      'networking and so on — an answer to not knowing what to build while learning a language.', O)
    a('https://github.com/florinpop17/app-ideas', 'App Ideas', ['github', 'müfredat'],
      'Zorluk seviyesine göre derecelendirilmiş uygulama fikirleri; her fikirde kullanıcı hikâyesi '
      've bonus özellikler yazılı. Proje listelerinden farkı bu şartname düzeyi.',
      'App ideas graded by difficulty, each with user stories and bonus features written out. '
      'That level of specification is what separates it from plain project lists.', O)
    a('https://github.com/vicky002/1000_Projects', '1000 Projects', ['github', 'müfredat'],
      'Çok geniş proje fikri derlemesi; niceliği yüksek, ayıklaması sana kalıyor.',
      'A very broad compilation of project ideas — high on quantity, with the filtering left to you.', O)
    a('https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/', 'MIT EECS Dersleri', ['ücretsiz', 'müfredat'],
      'MIT’nin elektrik mühendisliği ve bilgisayar bilimi bölümünün açık ders arşivi; '
      'algoritma, işletim sistemi ve derleyici derslerinin kaynağı.',
      'MIT’s open archive for electrical engineering and computer science — the source of its algorithms, '
      'operating systems and compilers courses.', O)
    a('https://www.kadenze.com/courses?subjects%5B%5D=7', 'Kadenze · Yaratıcı Programlama', ['freemium', 'müfredat'],
      'Sanat ve yaratıcı kodlama odaklı kurs platformu; ses sentezi, görsel programlama ve '
      'makine öğrenmesinin sanatta kullanımı gibi konular.',
      'A course platform for art and creative coding — sound synthesis, visual programming and machine '
      'learning applied to art.', O)

    # ============================================================ PRACTICE
    P = 'pratik'
    a('https://www.freecodecamp.com', 'freeCodeCamp', ['ücretsiz', 'interaktif', 'müfredat'],
      'Tarayıcı içinde alıştırmalı, uçtan uca ücretsiz müfredat; sertifikaları da ücretsiz. '
      'Bitirme projeleri gerçek uygulama yazdırdığı için sadece alıştırmada kalmıyor.',
      'A complete free curriculum with in-browser exercises and free certificates. Its capstone projects '
      'make you build real applications rather than stopping at drills.', P)
    a('https://www.codechef.com', 'CodeChef', ['freemium', 'algoritma'],
      'Aylık yarışmalı algoritma platformu; sorular zorluk seviyesine göre etiketli ve '
      'editöryal çözümleri yayımlanıyor.',
      'A competitive algorithm platform with monthly contests, difficulty-tagged problems and '
      'published editorial solutions.', P)
    a('http://codeforces.com', 'Codeforces', ['ücretsiz', 'algoritma'],
      'Yarışmacı programlamanın en yoğun platformu; düzenli turnuvalar ve derecelendirme sistemi. '
      'Sorular LeetCode’dan zor ve matematik ağırlığı yüksek.',
      'The busiest competitive programming platform, with regular rounds and a rating system. '
      'Problems run harder than LeetCode and lean heavily mathematical.', P)
    a('https://atcoder.jp/', 'AtCoder', ['ücretsiz', 'algoritma'],
      'Japonya merkezli yarışma platformu; başlangıç seviyesi turnuvaları (ABC) '
      'yeni başlayanlar için Codeforces’tan daha ulaşılabilir.',
      'A Japan-based contest platform whose beginner rounds (ABC) are more approachable for newcomers '
      'than Codeforces.', P)
    a('http://www.spoj.com', 'SPOJ', ['ücretsiz', 'algoritma'],
      'Uzun süredir çalışan çevrimiçi yargıç; klasik algoritma problemlerinin geniş arşivi. '
      'Arayüzü eski ama soru havuzu hâlâ referans kabul ediliyor.',
      'A long-running online judge with a large archive of classic algorithm problems. '
      'The interface is dated, but the problem set is still treated as a reference.', P)
    a('https://www.codingame.com/start', 'CodinGame', ['freemium', 'interaktif', 'algoritma'],
      'Algoritma problemlerini oyun olarak sunuyor; kodun bir karakteri yönettiği görsel geri bildirim '
      'motivasyonu ayakta tutuyor. Ciddi yarışma platformlarına yumuşak bir giriş.',
      'Presents algorithm problems as games, with visual feedback where your code drives a character. '
      'A soft entry into the serious contest platforms.', P)
    a('https://www.hackerearth.com', 'HackerEarth', ['freemium', 'algoritma', 'mülakat'],
      'Yarışma ve işe alım değerlendirmesini birleştiren platform; '
      'şirketler teknik ön elemeyi burada yapıyor.',
      'Combines contests with hiring assessments — companies run technical screening here.', P)
    a('https://www.topcoder.com', 'Topcoder', ['ücretsiz', 'algoritma'],
      'Yarışmacı programlamanın en eski platformlarından; problem arşivi ve '
      'editöryalleri algoritma tarihinin bir kesiti.',
      'One of the oldest competitive programming platforms; its problem archive and editorials form '
      'a slice of algorithm history.', P)
    a('https://coderbyte.com/', 'Coderbyte', ['freemium', 'mülakat'],
      'Mülakat sorusu havuzu ve değerlendirme aracı; çözümlerin video anlatımı var.',
      'An interview problem bank and assessment tool with video explanations of solutions.', P)
    a('https://www.interviewbit.com', 'InterviewBit', ['freemium', 'mülakat', 'algoritma'],
      'Mülakat hazırlığını konu bağımlılığına göre sıralayıp oyunlaştıran platform; '
      'her konu bir öncekinin üstüne bina ediliyor.',
      'Gamified interview preparation ordered by topic dependency, each subject building on the last.', P)
    a('http://www.codeabbey.com', 'CodeAbbey', ['ücretsiz', 'interaktif'],
      'En kolaydan başlayıp kademeli zorlaşan problem dizisi; mutlak sıfırdan başlayanlar için '
      'yarışma platformlarından çok daha nazik bir eğri.',
      'A problem sequence starting at the very easiest and climbing gradually — a far gentler curve than '
      'the contest platforms for absolute beginners.', P)
    a('http://programmingbydoing.com', 'Programming by Doing', ['ücretsiz', 'öğretici'],
      'Küçük ve çok sayıda alıştırmayla programlamayı öğreten site; her adım bir öncekinin '
      'üstüne minik bir ekleme yapıyor. Lise düzeyi giriş için tasarlanmış.',
      'Teaches programming through many small exercises, each adding a little to the last. '
      'Designed for a high-school-level start.', P)
    a('https://vim-adventures.com/', 'Vim Adventures', ['freemium', 'interaktif'],
      'Vim kısayollarını Zelda benzeri bir oyunla öğreten alıştırma. '
      'hjkl ve hareket komutlarını ezberlemek yerine oynayarak kazanıyorsun.',
      'Teaches Vim shortcuts through a Zelda-like game — you earn hjkl and motion commands by playing '
      'rather than memorising them.', P)
    a('https://glitch.com/', 'Glitch', ['ücretsiz', 'tarayıcı-içi'],
      'Tarayıcıda çalışan, anında yayına giren küçük uygulama ortamı. '
      'Kurulum ve dağıtım adımını tamamen atlayıp fikri denemek için.',
      'A browser environment for small apps that go live instantly — for testing an idea while skipping '
      'setup and deployment entirely.', P)
    a('https://cryptohack.org/', 'CryptoHack', ['ücretsiz', 'interaktif', 'güvenlik'],
      'Kriptografiyi kırarak öğreten platform; her seviye gerçek bir zafiyeti sömürdürüyor. '
      'Teorik kriptografi dersinin uygulamalı karşılığı.',
      'Teaches cryptography by breaking it, with each level exploiting a real weakness — '
      'the applied counterpart to a theory course.', P)

    # ============================================================ LANGUAGES & COMPILERS
    L = 'diller'
    a('http://craftinginterpreters.com/', 'Crafting Interpreters', ['ücretsiz', 'kitap', 'c-ailesi'],
      'Bir dili iki kez sıfırdan yazdıran ücretsiz kitap: önce Java ile ağaç yürüyen yorumlayıcı, '
      'sonra C ile bayt kodu sanal makinesi. Alanın en iyi anlatımlarından.',
      'A free book that has you write a language twice — a tree-walking interpreter in Java, then a '
      'bytecode VM in C. One of the clearest treatments in the field.', L)
    a('https://ruslanspivak.com/lsbasi-part1/', 'Let’s Build A Simple Interpreter', ['ücretsiz', 'öğretici', 'python'],
      'Python ile adım adım yorumlayıcı yazdıran uzun seri; sözcüksel çözümlemeden '
      'soyut sözdizimi ağacına kadar her parçayı elle kurduruyor.',
      'A long series building an interpreter step by step in Python, constructing every piece by hand '
      'from lexing to the abstract syntax tree.', L)
    a('https://norasandler.com/2017/11/29/Write-a-Compiler.html', 'Writing a C Compiler', ['ücretsiz', 'öğretici', 'c-ailesi'],
      'C derleyicisini parça parça yazdıran yazı dizisi; her bölüm dilin küçük bir alt kümesini '
      'derleyebilen çalışan bir program bırakıyor.',
      'A series writing a C compiler piece by piece, each part leaving you a working program that '
      'compiles a small subset of the language.', L)
    a('https://github.com/thejameskyle/the-super-tiny-compiler', 'The Super Tiny Compiler', ['github', 'öğretici'],
      'Yorum satırlarıyla açıklanmış, birkaç yüz satırlık minik bir derleyici. '
      'Derleyici aşamalarının tamamını tek oturumda okunabilir kılıyor.',
      'A tiny compiler of a few hundred heavily commented lines, making every compiler stage readable '
      'in a single sitting.', L)
    a('http://aalhour.com/awesome-compilers/', 'Awesome Compilers', ['awesome-liste', 'referans'],
      'Derleyici, yorumlayıcı ve çalışma zamanı kaynaklarının derlemesi; '
      'kitaplar, dersler ve açık kaynak derleyiciler ayrı ayrı listelenmiş.',
      'A collection of compiler, interpreter and runtime resources, with books, courses and open-source '
      'compilers listed separately.', L)
    a('https://sarabander.github.io/sicp/html/index.xhtml', 'SICP', ['ücretsiz', 'kitap'],
      'Bilgisayar Programlarının Yapısı ve Yorumlanması — MIT’nin klasik ders kitabının '
      'okunabilir HTML sürümü. Dil öğretmiyor, soyutlama kurmayı öğretiyor.',
      'Structure and Interpretation of Computer Programs, MIT’s classic text in a readable HTML edition. '
      'It does not teach a language; it teaches how to build abstractions.', L)
    a('https://python.swaroopch.com', 'A Byte of Python', ['ücretsiz', 'kitap', 'python'],
      'Python’a giriş kitabı; kısa, doğrudan ve onlarca dile çevrilmiş. '
      'Programlamaya tamamen yeni başlayanlar için yazılmış.',
      'An introductory Python book — short, direct and translated into dozens of languages, '
      'written for people entirely new to programming.', L)
    a('https://docs.python-guide.org/writing/style/', 'Hitchhiker’s Guide to Python', ['ücretsiz', 'python', 'referans'],
      'Python’da üslup, proje düzeni ve araç seçimi üzerine topluluk rehberi. '
      'Dil referansının anlatmadığı “nasıl yazılır” kısmı.',
      'A community guide to Python style, project layout and tooling — the “how it is written” part the '
      'language reference leaves out.', L)
    a('https://www.python.org/dev/peps/pep-0008/', 'PEP 8', ['ücretsiz', 'python', 'referans'],
      'Python’un resmî üslup kılavuzu; standart kütüphanenin yazımında kullanılan kurallar. '
      'black ve ruff gibi araçların dayandığı metin.',
      'Python’s official style guide, the rules used for the standard library itself — '
      'the text tools like black and ruff are built on.', L)
    a('http://www.stroustrup.com/C++11FAQ.html', 'C++11 SSS (Stroustrup)', ['ücretsiz', 'c-ailesi', 'referans'],
      'Dilin yaratıcısının C++11 ile gelen her özelliği neden eklediğini anlattığı SSS. '
      'Özellik listesinden farkı, tasarım gerekçesini vermesi.',
      'The language’s creator explaining why each C++11 feature was added. Unlike a feature list, '
      'it gives the design rationale.', L)
    a('http://www.stroustrup.com/bs_faq2.html', 'C++ Üslup ve Teknik SSS', ['ücretsiz', 'c-ailesi', 'referans'],
      'Stroustrup’un C++ üslubu ve sık yapılan hatalar üzerine SSS’i; '
      '“bunu neden böyle yapmalıyım” sorularının doğrudan cevabı.',
      'Stroustrup’s FAQ on C++ style and common mistakes — direct answers to “why should I do it this way”.', L)

    # ============================================================ REFERENCE & STYLE
    R = 'referans'
    a('https://google.github.io/styleguide/cppguide.html', 'Google C++ Üslup Kılavuzu', ['ücretsiz', 'c-ailesi', 'referans'],
      'Google’ın C++ kuralları; bazı maddeleri tartışmalı (istisna yasağı gibi) ama '
      'her kuralın gerekçesi yazılı olduğu için kendi kurallarını kurarken iyi bir başlangıç.',
      'Google’s C++ rules. Some are contested — the ban on exceptions, for one — but every rule carries '
      'its reasoning, which makes it a good base for writing your own.', R)
    a('https://google.github.io/styleguide/pyguide.html', 'Google Python Üslup Kılavuzu', ['ücretsiz', 'python', 'referans'],
      'PEP 8’in üstüne Google’ın kendi eklemeleri: docstring biçimi, içe aktarma düzeni, '
      'tip ipucu kullanımı. Büyük kod tabanlarında tutarlılık için.',
      'Google’s additions on top of PEP 8 — docstring format, import ordering, type-hint usage — '
      'aimed at consistency in large codebases.', R)
    a('https://google.github.io/styleguide/javaguide.html', 'Google Java Üslup Kılavuzu', ['ücretsiz', 'referans'],
      'Java için biçimlendirme ve adlandırma kuralları; google-java-format aracı '
      'doğrudan bu belgeyi uyguluyor.',
      'Formatting and naming rules for Java — the google-java-format tool implements this document directly.', R)
    a('https://google.github.io/styleguide/csharp-style.html', 'Google C# Üslup Kılavuzu', ['ücretsiz', 'referans'],
      'C# için adlandırma ve düzen kuralları; Microsoft’un kendi kılavuzuna göre daha kısa ve kesin.',
      'Naming and layout rules for C#, shorter and more prescriptive than Microsoft’s own guide.', R)
    a('https://github.com/airbnb/javascript', 'Airbnb JavaScript Üslup Kılavuzu', ['github', 'javascript', 'referans'],
      'JavaScript’in fiilî üslup standardı; ESLint yapılandırması olarak doğrudan kurulabiliyor. '
      'Her kural örnek doğru ve yanlış kodla gösterilmiş.',
      'The de facto JavaScript style standard, installable directly as an ESLint config, with every rule '
      'shown as good and bad example code.', R)
    a('https://standardjs.com', 'JavaScript Standard Style', ['ücretsiz', 'javascript', 'referans'],
      'Yapılandırma dosyası olmayan JavaScript biçimlendirici; tartışmayı bitirmek için '
      'tüm kararları kendisi veriyor. Airbnb’nin esnekliğinin karşı kutbu.',
      'A JavaScript formatter with no configuration file — it makes every decision for you to end the '
      'argument. The opposite pole from Airbnb’s flexibility.', R)
    a('https://github.com/uber-go/guide', 'Uber Go Üslup Kılavuzu', ['github', 'go', 'referans'],
      'Go’da üretim kodu yazarken karşılaşılan tuzakları ve tercih edilen kalıpları derliyor; '
      'resmî Effective Go’nun bıraktığı yerden devam ediyor.',
      'Collects the traps and preferred patterns of writing production Go, picking up where the official '
      'Effective Go leaves off.', R)
    a('https://github.com/bbatsov/ruby-style-guide', 'Ruby Üslup Kılavuzu', ['github', 'referans'],
      'Topluluk tarafından yazılmış Ruby üslup kılavuzu; RuboCop aracının '
      'varsayılan kural setinin temeli.',
      'A community-written Ruby style guide that forms the basis of RuboCop’s default rule set.', R)
    a('https://github.com/rust-dev-tools/fmt-rfcs', 'Rust Biçimlendirme Kuralları', ['github', 'rust', 'referans'],
      'rustfmt’in uyguladığı biçimlendirme kararlarının gerekçeleriyle tartışıldığı depo; '
      'aracın neden öyle davrandığını buradan öğreniyorsun.',
      'The repository where rustfmt’s formatting decisions are debated with their reasoning — '
      'where you learn why the tool behaves as it does.', R)
    a('https://www.chiark.greenend.org.uk/~sgtatham/bugs.html', 'Hata Nasıl Bildirilir', ['ücretsiz', 'referans'],
      'Etkili hata raporu yazmanın klasik metni; PuTTY’nin yazarından. '
      'Açık kaynak projelere katkı verecek herkesin bir kez okuması gereken kısa bir yazı.',
      'The classic text on writing an effective bug report, from PuTTY’s author — a short piece worth '
      'reading once by anyone contributing to open source.', R)
    a('https://sourcemaking.com/', 'SourceMaking', ['ücretsiz', 'sistem-tasarımı', 'referans'],
      'Tasarım desenleri, kod kokuları ve yeniden düzenleme tekniklerini örneklerle anlatan referans. '
      'Refactoring Guru’nun yanında ikinci bakış olarak işe yarıyor.',
      'A reference covering design patterns, code smells and refactoring techniques with examples — '
      'useful as a second opinion alongside Refactoring Guru.', R)
    a('https://devhints.io', 'Devhints', ['ücretsiz', 'kopya-kâğıdı'],
      'Yüzlerce araç ve dil için tek sayfalık kopya kâğıdı arşivi; '
      'her biri gerçekten bir ekrana sığacak şekilde budanmış.',
      'An archive of one-page cheat sheets for hundreds of tools and languages, each genuinely pruned '
      'to fit a single screen.', R)
    a('https://github.com/chubin/cheat.sh', 'cheat.sh', ['github', 'cli', 'kopya-kâğıdı'],
      'Terminalden `curl cheat.sh/komut` yazarak kopya kâğıdı çeken servis. '
      'Tarayıcı açmadan, editörden çıkmadan cevap veriyor.',
      'Pulls a cheat sheet from the terminal with `curl cheat.sh/command` — an answer without opening '
      'a browser or leaving your editor.', R)
    a('http://overapi.com', 'OverAPI', ['ücretsiz', 'kopya-kâğıdı'],
      'Dil ve çatı kopya kâğıtlarını tek sayfada toplayan dizin; '
      'görsel olarak yoğun ama aradığını hızlı buluyorsun.',
      'A directory gathering language and framework cheat sheets on one page — visually dense, '
      'but you find things fast.', R)
    a('https://goalkicker.com', 'GoalKicker', ['ücretsiz', 'kitap'],
      'Stack Overflow Documentation arşivinden derlenmiş ücretsiz programlama kitapları; '
      'her biri örnek ağırlıklı ve konu konu ayrılmış.',
      'Free programming books compiled from the Stack Overflow Documentation archive, each '
      'example-heavy and split topic by topic.', R)
    a('https://www.gitbook.com', 'GitBook', ['freemium', 'dokümantasyon'],
      'Dokümantasyon yazma ve yayımlama platformu; Git ile senkron çalışıp '
      'teknik kitapları web sitesine çeviriyor.',
      'A platform for writing and publishing documentation, syncing with Git to turn technical books '
      'into websites.', R)
    a('https://jakevdp.github.io/PythonDataScienceHandbook/', 'Python Data Science Handbook', ['ücretsiz', 'kitap', 'python', 'veri-bilimi'],
      'NumPy, pandas, Matplotlib ve scikit-learn’ü kapsayan ücretsiz kitap; '
      'tamamı çalıştırılabilir Jupyter defterleri olarak yayımlanmış.',
      'A free book covering NumPy, pandas, Matplotlib and scikit-learn, published entirely as runnable '
      'Jupyter notebooks.', R)
    a('https://graphql.guide', 'The GraphQL Guide', ['freemium', 'kitap', 'api'],
      'GraphQL’i istemci ve sunucu tarafıyla birlikte anlatan kitap; '
      'resmî spesifikasyonun atladığı üretim pratiklerine giriyor.',
      'A book covering GraphQL from both client and server side, reaching into the production practices '
      'the spec leaves out.', R)
