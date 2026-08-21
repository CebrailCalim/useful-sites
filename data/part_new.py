# -*- coding: utf-8 -*-
"""Yeni yer imi disa aktarimindan gelen kayitlar (eklenti.html, 20.08.2026).

Onceki dosyada olmayan 16 baglantidan 14'u alindi. Cikarilan ikisi:
Power BI oturum acma URL'si (ana kaydin tekrari) ve bir yetiskin site
uyelik profili — herkese acik bir dizine girmez.

Hepsi kullanicinin kendi arsivinden geldigi icin src varsayilan: kedi.
"""


def load(add):
    V = 'veri'
    add('https://scikit-learn.org/stable/', 'scikit-learn', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Klasik makine öğrenmesinin standart Python kütüphanesi: sınıflandırma, regresyon, kümeleme ve '
        'ön işleme aynı `fit`/`predict` arayüzü altında. Derin öğrenmeden önce gelen her şeyin ortak zemini.',
        'The standard Python library for classical machine learning — classification, regression, clustering '
        'and preprocessing behind one `fit`/`predict` interface. The common ground for everything before '
        'deep learning.', V)
    add('https://www.tensorflow.org/', 'TensorFlow', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Google’ın derin öğrenme çatısı. Araştırmada PyTorch’a yenildi ama mobil ve gömülü dağıtımda '
        '(TF Lite) ve üretim sunumunda (TF Serving) hâlâ güçlü.',
        'Google’s deep learning framework. It lost research ground to PyTorch, yet remains strong for '
        'mobile and embedded deployment (TF Lite) and production serving (TF Serving).', V)
    add('https://keras.io/', 'Keras', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Sinir ağını katman katman istiflemeyi birkaç satıra indiren yüksek seviye API. '
        'Artık TensorFlow, PyTorch ve JAX’in üçünde birden çalışıyor, yani çatı seçimini ertelemene izin veriyor.',
        'A high-level API reducing network construction to stacking layers in a few lines. It now runs on '
        'TensorFlow, PyTorch and JAX alike, which lets you defer the framework choice.', V)
    add('https://pandas.pydata.org/', 'pandas', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Tablo verisiyle çalışmanın standart kütüphanesi. Excel’den farkı, her dönüşümün '
        'tekrarlanabilir kod olması; bellek içi çalıştığı için veri RAM’e sığmak zorunda.',
        'The standard library for tabular data. Unlike Excel every transformation is reproducible code; '
        'it works in memory, so the data has to fit in RAM.', V)
    add('https://pola.rs/', 'Polars', ['açık-kaynak', 'rust', 'python', 'veri-bilimi'],
        'Rust ile yazılmış DataFrame kütüphanesi. pandas’tan farkı çok çekirdeği kullanması ve '
        'tembel değerlendirmeyle sorguyu çalıştırmadan önce optimize etmesi — büyük dosyalarda kat kat hızlı.',
        'A DataFrame library written in Rust. Unlike pandas it uses every core and optimises the query '
        'before running it through lazy evaluation, which makes it multiples faster on large files.', V)
    add('https://spark.apache.org/docs/latest/api/python/index.html', 'PySpark', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Apache Spark’ın Python arayüzü; veri tek makineye sığmadığında devreye giriyor. '
        'pandas benzeri API sunar ama işi kümedeki onlarca düğüme dağıtır.',
        'Apache Spark’s Python interface, for when the data no longer fits on one machine. '
        'It offers a pandas-like API while distributing the work across a cluster.', V)
    add('https://matplotlib.org/', 'Matplotlib', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Python görselleştirmenin temeli; seaborn ve pandas’ın çizim işlevleri bunun üstüne kurulu. '
        'Ayrıntılı denetim verir, karşılığında basit bir grafik için bile epey kod ister.',
        'The foundation of Python plotting — seaborn and pandas’ plotting are built on it. It gives fine '
        'control at the cost of considerable code even for a simple chart.', V)
    add('https://seaborn.pydata.org/', 'seaborn', ['açık-kaynak', 'python', 'veri-bilimi'],
        'Matplotlib üstüne kurulu istatistiksel grafik kütüphanesi. Dağılım, ilişki ve kategori '
        'grafiklerini tek satıra indiriyor; varsayılan estetiği de düzgün.',
        'A statistical plotting library on top of Matplotlib, reducing distribution, relationship and '
        'category plots to one line — with sane defaults out of the box.', V)
    add('https://plotly.com/', 'Plotly', ['freemium', 'python', 'veri-bilimi'],
        'Etkileşimli grafik kütüphanesi; yakınlaştırma, ipucu ve seçim kutudan çıkıyor. '
        'Matplotlib statik görsel üretir, bu tarayıcıda gezilebilir grafik verir.',
        'An interactive charting library with zoom, tooltips and selection built in. Matplotlib produces '
        'a static image; this produces a chart you can explore in the browser.', V)
    add('https://streamlit.io/', 'Streamlit', ['açık-kaynak', 'python', 'veri-bilimi', 'tarayıcı-içi'],
        'Python betiğini birkaç satırla web uygulamasına çeviriyor; HTML, CSS ya da JavaScript yok. '
        'Veri bilimcinin modelini paydaşa göstermesinin en kısa yolu.',
        'Turns a Python script into a web app in a few lines with no HTML, CSS or JavaScript — the '
        'shortest path for a data scientist to show a model to a stakeholder.', V)
    add('https://www.tableau.com/', 'Tableau', ['ücretli', 'veri-bilimi'],
        'Sürükle-bırak iş zekâsı platformu; kod yazmadan pano kuruluyor. '
        'Kurumsal raporlamada yaygın, tekrarlanabilirlik ve sürüm kontrolü tarafında zayıf.',
        'A drag-and-drop business intelligence platform for building dashboards without code. '
        'Common in enterprise reporting and weak on reproducibility and version control.', V)
    add('https://app.powerbi.com/', 'Power BI', ['ücretli', 'veri-bilimi'],
        'Microsoft’un iş zekâsı aracı; Excel ve Azure veri kaynaklarına yerleşik bağlanıyor. '
        'Kurum zaten Microsoft 365’teyse Tableau’ya karşı asıl avantajı lisansın ödenmiş olması.',
        'Microsoft’s business intelligence tool with native connections to Excel and Azure sources. '
        'If the organisation is already on Microsoft 365, its real edge over Tableau is a licence '
        'that is already paid for.', V)

    D = 'veritabani'
    add('https://sqlite.org/', 'SQLite', ['açık-kaynak', 'sql', 'veritabanı'],
        'Sunucusu olmayan, tek dosyada duran gömülü veritabanı. Dünyada en çok dağıtılmış veritabanı '
        'motoru; telefonundaki her uygulamanın içinde bir kopyası var. Test kapsamı efsanevi.',
        'A serverless embedded database living in a single file — the most widely deployed database engine '
        'in the world, with a copy inside nearly every app on your phone. Its test coverage is legendary.', D)
    add('https://www.oracle.com/database/sqldeveloper/', 'Oracle SQL Developer', ['ücretsiz', 'sql', 'veritabanı'],
        'Oracle veritabanları için ücretsiz masaüstü istemci; sorgu, şema gezme ve '
        'PL/SQL hata ayıklama bir arada. Oracle ile çalışıyorsan fiilî standart araç.',
        'A free desktop client for Oracle databases combining querying, schema browsing and PL/SQL '
        'debugging — the de facto tool if you work with Oracle.', D)
