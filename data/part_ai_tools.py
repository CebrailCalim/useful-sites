# -*- coding: utf-8 -*-
"""YZ · Uygulama Araçları"""

C = 'yz_arac'


def load(add):
    # ---------------------------------------------------------- kod asistanları
    add('https://github.com/features/copilot', 'GitHub Copilot', ['freemium', 'kod'],
        'Editör içi kod tamamlama ve sohbet. Rakiplerinden farkı GitHub ve kurumsal politika yönetimiyle iç içe olması.',
        'In-editor code completion and chat; its distinction is being wired into GitHub and enterprise policy management.', C)
    add('https://cursor.com/', 'Cursor', ['freemium', 'kod', 'editör'],
        'YZ etrafında yeniden kurulmuş VS Code çatalı. Eklentiden farkı, proje genelinde çok dosyalı düzenlemeyi ana akış hâline getirmesi.',
        'A VS Code fork rebuilt around AI. Unlike a plugin it makes multi-file, project-wide editing the main flow.', C)
    add('https://windsurf.com/', 'Windsurf', ['freemium', 'kod', 'editör'],
        'Agent öncelikli YZ editörü; Cursor’a en yakın alternatif, farkı uzun otonom görevleri kendi başına yürütmeye daha çok yaslanması.',
        'Agent-first AI editor and the closest alternative to Cursor, leaning harder on running long autonomous tasks by itself.', C)
    add('https://www.continue.dev/', 'Continue', ['açık kaynak', 'kod', 'eklenti'],
        'VS Code ve JetBrains için açık kaynak YZ eklentisi. Kapalı editörlerden farkı, hangi modeli kullanacağını tamamen senin seçmen.',
        'Open-source AI plugin for VS Code and JetBrains; unlike closed editors you choose exactly which model backs it.', C)
    add('https://aider.chat/', 'Aider', ['açık kaynak', 'kod', 'cli'],
        'Terminalde çalışan eşli programlama aracı; değişiklikleri doğrudan git commit’i olarak yazması onu editör eklentilerinden ayırır.',
        'Terminal pair-programmer whose distinguishing habit is writing changes straight into git commits.', C)
    add('https://cline.bot/', 'Cline', ['açık kaynak', 'kod', 'eklenti'],
        'VS Code içinde dosya oluşturup komut çalıştırabilen otonom kodlama agent’ı; her adım için onay istemesiyle kontrolü sende bırakır.',
        'Autonomous coding agent inside VS Code that creates files and runs commands, asking approval at each step to keep you in control.', C)
    add('https://roocode.com/', 'Roo Code', ['açık kaynak', 'kod', 'eklenti'],
        'Cline’dan türeyen kodlama agent’ı; mimar, kodcu, hata ayıklayıcı gibi kip ayrımı sunmasıyla ayrışıyor.',
        'A coding agent forked from Cline, distinguished by separate modes such as architect, coder and debugger.', C)
    add('https://www.tabbyml.com/', 'Tabby', ['açık kaynak', 'kod', 'kendi sunucunda'],
        'Kendi sunucunda çalışan kod tamamlama; Copilot’tan farkı kodun hiçbir zaman dışarı çıkmaması.',
        'Self-hosted code completion; unlike Copilot your code never leaves your infrastructure.', C)
    add('https://www.all-hands.dev/', 'OpenHands', ['açık kaynak', 'kod', 'agent'],
        'Tarayıcı ve terminal kullanabilen otonom yazılım geliştirme agent’ı; tamamlamadan çok uçtan uca görev bitirmeye odaklı.',
        'Autonomous software-development agent that can use a browser and terminal, aimed at finishing tasks end to end rather than completing lines.', C)
    add('https://www.blackbox.ai/', 'Blackbox AI', ['freemium', 'kod'],
        'Kod arama ve üretme asistanı; kod parçası aramayı sohbetle birleştirmesi başlıca özelliği.',
        'Code search and generation assistant whose main trait is merging snippet search with chat.', C)
    add('https://codegeex.cn/', 'CodeGeeX', ['ücretsiz', 'kod', 'çok dilli'],
        'Çok dilli açık kod modeli ve eklentisi; Çince arayüz ve yerel model desteğiyle bölgesel bir alternatif.',
        'Multilingual open code model and plugin — a regional alternative with Chinese-language UI and local model support.', C)
    add('https://replit.com/', 'Replit', ['freemium', 'kod', 'tarayıcıda'],
        'Tarayıcıda çalışan geliştirme ortamı; kurulum yapmadan kod yazıp yayına almayı tek yerde toplaması ayırt edici yanı.',
        'Browser-based development environment; writing and deploying code with zero local setup is what sets it apart.', C)
    add('https://pieces.app/', 'Pieces for Developers', ['freemium', 'kod', 'not'],
        'Kod parçalarını bağlamıyla saklayan geliştirici hafızası; not uygulamalarından farkı, ne yaptığın üzerinden geçmişi hatırlaması.',
        'A developer memory that stores snippets with their context; unlike note apps it recalls history based on what you were doing.', C)
    add('https://v0.app/', 'v0', ['freemium', 'ui', 'üretim'],
        'Metinden React arayüzü üreten Vercel aracı; tam uygulama yerine bileşen düzeyinde çıktı vermesiyle ayrışıyor.',
        'Vercel’s text-to-React UI generator, distinguished by producing component-level output rather than whole apps.', C)
    add('https://bolt.new/', 'Bolt.new', ['freemium', 'ui', 'üretim'],
        'Tarayıcıda çalışan tam yığın uygulama üreticisi; kodu tarayıcı içinde çalıştırıp anında önizlemesi ayırt edici yanı.',
        'Full-stack app generator in the browser; running the code inside the browser for instant preview is its distinguishing trait.', C)
    add('https://lovable.dev/', 'Lovable', ['freemium', 'ui', 'üretim'],
        'Sohbetle tam uygulama üreten araç; v0’dan farkı veritabanı ve yayına almayı da üstlenmesi.',
        'Chat-to-full-app builder; unlike v0 it also takes on the database and deployment.', C)
    add('https://stitch.withgoogle.com/', 'Stitch (Google)', ['ücretsiz', 'ui', 'tasarım'],
        'Metin veya çizimden arayüz tasarımı üreten Google aracı; çıktıyı doğrudan tasarım dosyası olarak vermesi ayırt edici.',
        'Google’s text- or sketch-to-UI design tool, distinguished by handing back editable design files.', C)
    add('https://github.com/resumax', 'ResuMax', ['açık kaynak', 'github', 'kariyer'],
        'Özgeçmiş hazırlama ve iyileştirme aracı; genel yazım asistanlarından farkı, ilana göre uyarlamaya odaklanması.',
        'A résumé builder and optimiser; unlike general writing assistants it focuses on tailoring to a specific posting.', C)

    # ---------------------------------------------------------- görsel üretim
    add('https://firefly.adobe.com/', 'Adobe Firefly', ['freemium', 'görsel'],
        'Adobe’un görsel üretim modeli; ticari kullanım için lisanslı veriyle eğitilmiş olması kurumsal işlerde başlıca tercih sebebi.',
        'Adobe’s image generator; being trained on licensed data for commercial use is the main reason it is picked for client work.', C)
    add('https://leonardo.ai/', 'Leonardo AI', ['freemium', 'görsel'],
        'Oyun ve konsept sanatına eğilimli görsel üretici; kendi stil modellerini eğitip tekrar kullanabilmesiyle ayrışıyor.',
        'Image generator leaning towards game and concept art, distinguished by training and reusing your own style models.', C)
    add('https://ideogram.ai/', 'Ideogram', ['freemium', 'görsel', 'tipografi'],
        'Görsel içinde okunaklı metin üretebilmesiyle öne çıkan model; afiş ve logo denemelerinde diğerlerinden belirgin şekilde iyi.',
        'Known for rendering legible text inside images — markedly better than rivals for posters and logo experiments.', C)
    add('https://designer.microsoft.com/', 'Microsoft Designer', ['ücretsiz', 'görsel', 'şablon'],
        'Şablon tabanlı hızlı grafik tasarım; saf üreticilerden farkı, çıktıyı düzenlenebilir bir tasarım olarak vermesi.',
        'Template-based quick graphic design; unlike pure generators it hands back an editable layout.', C)
    add('https://www.bing.com/images/create', 'Bing Image Creator', ['ücretsiz', 'görsel'],
        'Ücretsiz görsel üretim; hesap dışında bir engeli olmaması onu en düşük sürtünmeli seçeneklerden biri yapıyor.',
        'Free image generation with no barrier beyond an account, making it one of the lowest-friction options.', C)
    add('https://www.craiyon.com/', 'Craiyon', ['ücretsiz', 'görsel'],
        'Kayıt istemeden çalışan basit görsel üretici; kalite düşük ama hızlı deneme için engelsiz.',
        'A simple generator that works without signup — lower quality, but frictionless for quick tries.', C)
    add('https://playground.com/', 'Playground AI', ['freemium', 'görsel', 'düzenleme'],
        'Üretim ve düzenlemeyi tuval üzerinde birleştiren araç; parça parça düzeltmeye elverişli.',
        'Combines generation and editing on a canvas, which suits piecemeal correction.', C)
    add('https://piclumen.com/', 'PicLumen', ['ücretsiz', 'görsel', 'karakter'],
        'Karakter ve ürün görselleri üzerine yoğunlaşan üretici; ücretsiz katmanının cömertliğiyle biliniyor.',
        'Generator focused on character and product imagery, known for a generous free tier.', C)
    add('https://github.com/AUTOMATIC1111/stable-diffusion-webui', 'Stable Diffusion WebUI', ['açık kaynak', 'github', 'yerel', 'görsel'],
        'Yerel görsel üretimin en yaygın arayüzü; eklenti ekosisteminin genişliği başlıca avantajı.',
        'The most widely used interface for local image generation; the breadth of its extension ecosystem is the main draw.', C)
    add('https://www.comfy.org/', 'ComfyUI', ['açık kaynak', 'yerel', 'görsel'],
        'Düğüm tabanlı görsel üretim arayüzü; WebUI’nin form yaklaşımından farkı, akışın her adımını görünür ve tekrar edilebilir kılması.',
        'Node-based image generation UI; unlike WebUI’s form approach it makes every step of the pipeline visible and reproducible.', C)
    add('https://github.com/lllyasviel/Fooocus', 'Fooocus', ['açık kaynak', 'github', 'yerel', 'görsel'],
        'Ayar yükünü gizleyen basitleştirilmiş Stable Diffusion arayüzü; ComfyUI’nin karşı kutbu, hiçbir şey ayarlamadan iyi sonuç hedefler.',
        'A simplified Stable Diffusion UI that hides the knobs — the opposite pole from ComfyUI, aiming for good output with zero tuning.', C)
    add('https://www.invoke.com/', 'InvokeAI', ['açık kaynak', 'yerel', 'görsel'],
        'Profesyonel iş akışına yönelik yerel görsel üretim paketi; tuval üzerinde bölgesel düzenlemeye güçlü destek verir.',
        'Local generation suite aimed at professional workflows, with strong support for regional editing on a canvas.', C)
    add('https://github.com/Acly/krita-ai-diffusion', 'Krita AI Diffusion', ['açık kaynak', 'github', 'görsel'],
        'Krita çizim programına görsel üretimi gömen eklenti; ayrı araç yerine mevcut çizim akışının içinde çalışması ayırt edici.',
        'Plugin embedding generation into the Krita painting app — it works inside your existing drawing flow rather than as a separate tool.', C)
    add('https://www.recraft.ai/projects', 'Recraft', ['freemium', 'görsel', 'vektör'],
        'Vektör çıktı üretebilen tasarım odaklı model; logo ve ikon işlerinde raster üreticilerden belirgin şekilde kullanışlı.',
        'Design-focused model that can output vectors — markedly more useful than raster generators for logos and icons.', C)
    add('https://www.remove.bg/', 'remove.bg', ['freemium', 'görsel', 'araç'],
        'Tek işe odaklı arka plan silme servisi; genel düzenleyicilerden farkı, tek tıkla ve toplu çalışabilmesi.',
        'A single-purpose background remover; unlike general editors it works in one click and in batches.', C)
    add('https://clipdrop.co/', 'Clipdrop', ['freemium', 'görsel', 'araç'],
        'Nesne silme, ışık düzeltme, büyütme gibi küçük görsel araçların toplandığı set; her biri için ayrı uygulama aramaya alternatif.',
        'A bundle of small image utilities — object removal, relighting, upscaling — instead of hunting a separate app for each.', C)
    add('https://app.gptzero.me/home', 'GPTZero', ['freemium', 'tespit'],
        'Metnin yapay zeka tarafından yazılıp yazılmadığını tahmin eden araç; sonuçlarının kesin olmadığını kendisi de belirtiyor.',
        'Estimates whether text was AI-written; it states itself that the verdict is probabilistic, not proof.', C)

    # ---------------------------------------------------------- 3B & mekân
    add('https://www.meshy.ai/tr/?noRedirect=true', 'Meshy', ['freemium', '3b'],
        'Metin veya görselden 3B model üreten araç; çıktıya otomatik doku giydirmesi oyun varlıkları için zaman kazandırıyor.',
        'Text- or image-to-3D generator whose automatic texturing saves real time on game assets.', C)
    add('https://www.tripo3d.ai/', 'Tripo AI', ['freemium', '3b'],
        'Tek görselden 3B model üretimi; hız ve topoloji temizliği iddiasıyla Meshy’ye doğrudan rakip.',
        'Single-image to 3D generation, competing directly with Meshy on speed and cleaner topology.', C)
    add('https://spline.design/', 'Spline', ['freemium', '3b', 'web'],
        'Tarayıcıda 3B tasarım ve web’e gömme aracı; Blender gibi genel amaçlı değil, web sahnesi üretmeye odaklı.',
        'Browser-based 3D design that embeds into web pages — not general-purpose like Blender, but focused on web scenes.', C)
    add('https://github.com/gd3kr/BlenderGPT', 'BlenderGPT', ['açık kaynak', 'github', '3b'],
        'Blender işlemlerini doğal dille yaptıran eklenti; model üretmez, mevcut araçları senin yerine kullanır.',
        'Plugin driving Blender operations from natural language — it does not generate models, it operates the existing tools for you.', C)
    add('https://github.com/carson-katri/dream-textures', 'Dream Textures', ['açık kaynak', 'github', '3b', 'doku'],
        'Blender içinde doku ve yüzey üreten eklenti; dışarıda üretip içeri aktarma adımını ortadan kaldırır.',
        'Blender add-on generating textures in place, removing the generate-elsewhere-then-import step.', C)
    add('https://huggingface.co/stabilityai/stable-fast-3d', 'Stable Fast 3D', ['açık ağırlık', '3b', 'model'],
        'Tek görselden saniyeler içinde 3B varlık üreten açık model; hızı kaliteye tercih eden akışlar için.',
        'Open model producing a 3D asset from one image in seconds — for pipelines that trade quality for speed.', C)
    add('https://github.com/openai/shap-e', 'Shap-E', ['açık kaynak', 'github', '3b', 'araştırma'],
        'OpenAI’ın metinden 3B üretim modeli; ürün değil araştırma çıktısı, üretim kalitesi beklenmemeli.',
        'OpenAI’s text-to-3D model — a research release rather than a product, so do not expect production quality.', C)
    add('https://github.com/openai/point-e', 'Point-E', ['açık kaynak', 'github', '3b', 'araştırma'],
        'Nokta bulutu üreten daha eski OpenAI modeli; Shap-E’den hızlı ama çıktı çok daha kaba.',
        'An earlier OpenAI model producing point clouds — faster than Shap-E but far coarser output.', C)
    add('https://github.com/TencentARC/InstantMesh', 'InstantMesh', ['açık kaynak', 'github', '3b'],
        'Tek görselden kullanılabilir mesh üreten açık model; nokta bulutu değil doğrudan yüzey vermesiyle ayrışıyor.',
        'Open model turning one image into a usable mesh — it returns surfaces directly rather than a point cloud.', C)
    add('https://planner5d.com/', 'Planner 5D', ['freemium', 'mimari'],
        'Tarayıcıda iç mekân planlama; profesyonel CAD yerine hızlı kat planı ve görselleştirmeye odaklı.',
        'Browser interior planning focused on quick floor plans and renders rather than professional CAD.', C)
    add('https://www.homestyler.com/', 'Homestyler', ['freemium', 'mimari'],
        'Mobilya kataloğu üzerinden iç mekân tasarımı; gerçek ürünlerle çalışması Planner 5D’den ayıran yanı.',
        'Interior design driven by a furniture catalogue; working with real products is what separates it from Planner 5D.', C)
    add('https://www.blueprint.am/', 'Blueprint.am', ['donanım', 'tasarım'],
        'Donanım tasarımına yapay zeka desteği getiren araç; yazılım odaklı asistanların değmediği bir alanı hedefliyor.',
        'Brings AI assistance to hardware design — a niche the software-focused assistants do not touch.', C)

    # ---------------------------------------------------------- video & ses
    add('https://www.capcut.com/', 'CapCut', ['freemium', 'video'],
        'Otomatik altyazı ve şablon ağırlıklı video düzenleyici; kısa video akışında profesyonel paketlere göre çok daha hızlı.',
        'Video editor built on auto-captioning and templates — far faster than professional suites for short-form work.', C)
    add('https://pika.art/', 'Pika', ['freemium', 'video'],
        'Metin ve görselden kısa video üreten model; hareket efektlerini seçilebilir hâle getirmesiyle ayrışıyor.',
        'Text- and image-to-short-video model, distinguished by exposing motion effects as selectable options.', C)
    add('https://lumalabs.ai/', 'Luma AI', ['freemium', 'video', '3b'],
        'Video üretimi ve gerçek nesne taramasını (NeRF) birlikte sunuyor; saf video modellerinden farkı bu ikinci ayağı.',
        'Combines video generation with real-object capture (NeRF) — that second leg is what separates it from pure video models.', C)
    add('https://github.com/jamiepine/voicebox', 'Voicebox', ['açık kaynak', 'github', 'ses'],
        'Açık kaynak ses stüdyosu: klonlama, dikte ve üretim bir arada; bulut servislerine kendi makinende alternatif.',
        'Open-source voice studio combining cloning, dictation and generation — a local alternative to cloud services.', C)
    add('https://github.com/openai/whisper', 'Whisper', ['açık kaynak', 'github', 'ses', 'yerel'],
        'OpenAI’ın açık konuşma tanıma modeli; bulut servislerinden farkı, ses kaydının makineden hiç çıkmaması.',
        'OpenAI’s open speech-recognition model; unlike cloud services the recording never leaves your machine.', C)
    add('https://otter.ai/', 'Otter.ai', ['freemium', 'ses', 'toplantı'],
        'Toplantıyı canlı yazıya döken asistan; kayıt sonrası değil toplantı sırasında çalışması ayırt edici yanı.',
        'Meeting transcription assistant that works during the meeting rather than after the recording.', C)
    add('https://fireflies.ai/', 'Fireflies.ai', ['freemium', 'ses', 'toplantı'],
        'Toplantı özeti ve aksiyon maddesi çıkaran asistan; ham döküm yerine karar ve görev listesi üretmeye odaklı.',
        'Meeting assistant producing summaries and action items, focused on decisions and tasks rather than a raw transcript.', C)
    add('https://krisp.ai/', 'Krisp', ['freemium', 'ses'],
        'Gerçek zamanlı gürültü engelleme; uygulama bağımsız çalışıp mikrofon düzeyinde araya girmesi ayırt edici.',
        'Real-time noise cancellation that works app-independently by intercepting at the microphone level.', C)
    add('https://auphonic.com/', 'Auphonic', ['freemium', 'ses', 'podcast'],
        'Ses kaydını otomatik seviyeleyip temizleyen son işlem servisi; canlı değil, yayın öncesi kalite düzeltme için.',
        'Post-production service that levels and cleans recordings — not live, but for pre-publish quality correction.', C)

    # ---------------------------------------------------------- araştırma & doküman
    add('https://elicit.com/', 'Elicit', ['freemium', 'araştırma', 'akademik'],
        'Akademik makale tarayıp bulguları tabloya döken asistan; arama motorlarından farkı, çalışmaların sonuçlarını karşılaştırılabilir kılması.',
        'Screens academic papers and extracts findings into a table; unlike search engines it makes results comparable.', C)
    add('https://consensus.app/', 'Consensus', ['freemium', 'araştırma', 'akademik'],
        'Bilimsel soruya literatürdeki uzlaşıyı özetleyen arama; tek makale bulmaktan çok “alan ne diyor” sorusuna yanıt verir.',
        'Search that summarises scientific consensus on a question — it answers “what does the field say” rather than finding one paper.', C)
    add('https://www.researchrabbit.ai/', 'ResearchRabbit', ['ücretsiz', 'araştırma', 'akademik'],
        'Makaleler arası atıf ağını görselleştiren keşif aracı; anahtar kelime aramasının kaçırdığı komşu çalışmaları bulmak için.',
        'Visualises citation networks between papers, surfacing neighbouring work that keyword search misses.', C)
    add('https://scispace.com/', 'SciSpace', ['freemium', 'araştırma', 'akademik'],
        'Makaleyi paragraf paragraf açıklayan asistan; alan dışından okuyanlar için terimleri yerinde çözmesiyle ayrışıyor.',
        'Explains a paper paragraph by paragraph, resolving jargon in place for readers from outside the field.', C)
    add('https://www.explainpaper.com/', 'Explainpaper', ['freemium', 'araştırma'],
        'Makalede seçtiğin kısmı sadeleştiren araç; tüm belgeyi özetlemek yerine takıldığın yeri açması ayırt edici.',
        'Simplifies whichever passage you highlight — it opens up the part you got stuck on rather than summarising the whole document.', C)
    add('https://www.scholarcy.com/', 'Scholarcy', ['freemium', 'araştırma'],
        'Makaleyi yapılandırılmış özet kartlarına indirgeyen araç; tarama aşamasında hangi çalışmayı okuyacağına karar vermek için.',
        'Reduces a paper to structured summary cards — for deciding, during triage, which study is worth reading.', C)
    add('https://askyourpdf.com/', 'AskYourPDF', ['freemium', 'pdf'],
        'PDF ile sohbet; birden çok belgeyi tek kütüphanede toplayıp hepsine birden soru sorabilmesi ayırt edici.',
        'Chat with PDFs; collecting many documents into one library and querying them together is what sets it apart.', C)
    add('https://www.chatpdf.com/', 'ChatPDF', ['freemium', 'pdf'],
        'Tek PDF’e soru sormanın en hızlı yolu; kayıt gerektirmeden yükleyip sormaya izin vermesiyle sürtünmesi düşük.',
        'The fastest way to question a single PDF, with low friction because you can upload and ask without signing up.', C)
    add('https://www.humata.ai/', 'Humata', ['freemium', 'pdf'],
        'Uzun teknik belgeleri karşılaştırmalı okumaya odaklı asistan; cevaba kaynak sayfa bağlantısı vermesi güven veriyor.',
        'Assistant for comparative reading of long technical documents, citing the source page for each answer.', C)
    add('https://pdf.ai/', 'PDF.ai', ['freemium', 'pdf'],
        'PDF sohbeti; tarayıcı eklentisiyle web’deki PDF’lerde de çalışabilmesi ayırt edici yanı.',
        'PDF chat whose distinguishing feature is a browser extension that also works on PDFs found on the web.', C)
    add('https://lightpdf.com/', 'LightPDF', ['freemium', 'pdf', 'araç'],
        'Dönüştürme, sıkıştırma, düzenleme gibi klasik PDF araçlarına YZ sohbeti eklenmiş set; tek işlevli rakiplerinden daha geniş.',
        'Classic PDF utilities — convert, compress, edit — with AI chat added, broader than the single-purpose rivals.', C)

    # ---------------------------------------------------------- yazım & sunum
    add('https://www.grammarly.com/', 'Grammarly', ['freemium', 'yazım', 'ingilizce'],
        'İngilizce yazım ve üslup denetleyicisi; her uygulamada çalışan eklentisiyle en yaygın seçenek.',
        'English grammar and style checker; its everywhere-you-type extension makes it the most widespread option.', C)
    add('https://languagetool.org/', 'LanguageTool', ['açık kaynak', 'yazım', 'çok dilli'],
        'Açık kaynak dil bilgisi denetleyicisi; Grammarly’den farkı Türkçe dahil çok dili desteklemesi ve kendi sunucunda çalışabilmesi.',
        'Open-source grammar checker; unlike Grammarly it supports many languages including Turkish and can be self-hosted.', C)
    add('https://www.deepl.com/write', 'DeepL Write', ['freemium', 'yazım'],
        'Metni yeniden yazarak akıcılaştıran araç; hata düzeltmekten çok üslup iyileştirmeye odaklı olmasıyla Grammarly’den ayrılıyor.',
        'Rewrites text for fluency; it differs from Grammarly by targeting style improvement rather than error correction.', C)
    add('https://quillbot.com/', 'QuillBot', ['freemium', 'yazım'],
        'Başka sözcüklerle ifade etme (paraphrase) aracı; ton ve uzunluk seçenekleriyle aynı cümlenin farklı sürümlerini üretir.',
        'A paraphrasing tool producing alternative versions of the same sentence with tone and length controls.', C)
    add('https://gamma.app/', 'Gamma', ['freemium', 'sunum'],
        'Metinden sunum ve doküman üreten araç; slayt yerine kaydırılabilir sayfa modeli kullanması ayırt edici yanı.',
        'Generates presentations and documents from text; using a scrollable page model instead of slides is what sets it apart.', C)
    add('https://www.napkin.ai/', 'Napkin AI', ['freemium', 'görselleştirme'],
        'Düz metni diyagram ve şemaya çeviren araç; sunum üreticilerinden farkı, tek bir fikri görselleştirmeye odaklanması.',
        'Turns plain text into diagrams; unlike deck generators it focuses on visualising one idea at a time.', C)
    add('https://www.canva.com/', 'Canva', ['freemium', 'tasarım'],
        'Şablon tabanlı genel tasarım aracı; tasarım bilgisi olmadan kabul edilebilir çıktı almanın en yaygın yolu.',
        'Template-based general design tool — the most common way to get acceptable output without design skills.', C)
    add('https://pitch.com/', 'Pitch', ['freemium', 'sunum', 'ekip'],
        'Ekip odaklı sunum aracı; eşzamanlı düzenleme ve marka şablonlarıyla PowerPoint’e web tabanlı alternatif.',
        'Team-oriented presentation tool — a web alternative to PowerPoint with live co-editing and brand templates.', C)
    add('https://www.slidesai.io/', 'SlidesAI', ['freemium', 'sunum'],
        'Google Slides içine gömülen sunum üreticisi; ayrı platforma geçmeden mevcut dosyanda çalışması ayırt edici.',
        'Deck generator embedded in Google Slides, working inside your existing file rather than a separate platform.', C)

    # ---------------------------------------------------------- veri bilimi & AutoML
    add('https://julius.ai/', 'Julius AI', ['freemium', 'veri', 'analiz'],
        'Veri dosyasını yükleyip sohbetle analiz eden araç; kod yazmadan grafik ve istatistik üretmeye odaklı.',
        'Upload a data file and analyse it by chatting — aimed at charts and statistics without writing code.', C)
    add('https://www.knime.com/', 'KNIME', ['ücretsiz', 'veri', 'görsel'],
        'Düğüm tabanlı görsel veri analizi platformu; kod yazmadan tekrarlanabilir hat kurmak isteyenler için.',
        'Node-based visual analytics platform for building reproducible pipelines without writing code.', C)
    add('https://orangedatamining.com/', 'Orange', ['açık kaynak', 'veri', 'eğitim'],
        'Görsel programlamayla veri madenciliği; KNIME’a göre daha hafif ve öğretim amaçlı kullanıma daha uygun.',
        'Visual-programming data mining — lighter than KNIME and better suited to teaching.', C)
    add('https://ml.cms.waikato.ac.nz/weka/', 'Weka', ['açık kaynak', 'veri', 'akademik'],
        'Klasik makine öğrenmesi algoritmalarının akademik araç kutusu; modern kütüphanelerden eski ama algoritma karşılaştırmak için hâlâ düzenli.',
        'Academic toolbox of classical ML algorithms — dated next to modern libraries but still tidy for comparing algorithms.', C)
    add('https://auto.gluon.ai/', 'AutoGluon', ['açık kaynak', 'automl', 'python'],
        'Birkaç satırla güçlü model üreten AutoML kütüphanesi; topluluk (ensemble) kurmayı otomatikleştirmesiyle ayrışıyor.',
        'AutoML library producing strong models in a few lines, distinguished by automating ensemble construction.', C)
    add('https://h2o.ai/', 'H2O.ai', ['freemium', 'automl'],
        'Kurumsal AutoML platformu; ölçekli veri ve model açıklanabilirliği tarafında kütüphane çözümlerinden ileri.',
        'Enterprise AutoML platform, ahead of library-only solutions on large data and model explainability.', C)
    add('https://pycaret.org/', 'PyCaret', ['açık kaynak', 'automl', 'python'],
        'Düşük kodlu makine öğrenmesi kütüphanesi; deneme aşamasında onlarca modeli tek satırla karşılaştırmak için.',
        'Low-code ML library for comparing dozens of models in a single line during experimentation.', C)
    add('https://mljar.com/automl/', 'MLJAR AutoML', ['açık kaynak', 'automl'],
        'Otomatik model seçimi yapıp sonucu okunabilir rapor olarak sunan kütüphane; açıklama üretmesi ayırt edici yanı.',
        'AutoML that also produces a readable report — generating explanations is what distinguishes it.', C)
    add('https://colab.research.google.com/', 'Google Colab', ['ücretsiz', 'not defteri', 'gpu'],
        'Tarayıcıda çalışan Python not defteri; ücretsiz GPU erişimi onu deneme ve öğretim için standart hâline getirdi.',
        'Browser-based Python notebook whose free GPU access made it the standard for experiments and teaching.', C)
    add('https://www.kaggle.com/code', 'Kaggle Notebooks', ['ücretsiz', 'not defteri', 'veri'],
        'Veri kümeleriyle aynı yerde duran not defterleri; Colab’dan farkı, başkalarının çözümlerini okuyabilmen.',
        'Notebooks sitting next to the datasets; unlike Colab you can read other people’s solutions.', C)

    # ---------------------------------------------------------- sağlık & yaşam bilimleri
    add('https://www.openevidence.com/', 'OpenEvidence', ['ücretsiz', 'tıp', 'akademik'],
        'Klinik sorulara kaynak göstererek yanıt veren tıbbi arama; genel botlardan farkı, yalnızca hakemli literatüre dayanması.',
        'Medical search answering clinical questions with citations; unlike general chatbots it draws only on peer-reviewed literature.', C)
    add('https://deepmind.google/models/gemma/medgemma/', 'MedGemma', ['açık ağırlık', 'tıp', 'model'],
        'Google’ın tıp alanına uyarlanmış açık modeli; klinik metin ve görüntü üzerinde araştırma amaçlı kullanım için.',
        'Google’s medically adapted open model, intended for research use on clinical text and images.', C)
    add('https://github.com/microsoft/BioGPT', 'BioGPT', ['açık kaynak', 'github', 'biyomedikal'],
        'Biyomedikal literatürde eğitilmiş dil modeli; genel modellerin zorlandığı alan terminolojisinde daha isabetli.',
        'Language model trained on biomedical literature, more accurate on domain terminology than general models.', C)
    add('https://github.com/kbressem/medAlpaca', 'MedAlpaca', ['açık kaynak', 'github', 'tıp'],
        'Tıbbi soru-cevap için ince ayarlanmış açık model; klinik kullanım için değil, araştırma ve sınav çalışması için.',
        'Open model fine-tuned for medical Q&A — for research and exam practice, not clinical use.', C)
    add('https://ada.com/', 'Ada Health', ['ücretsiz', 'sağlık'],
        'Belirtilerden olası nedenleri daraltan değerlendirme uygulaması; arama motorunda semptom aramaya yapılandırılmış alternatif.',
        'Symptom assessment app narrowing possible causes — a structured alternative to searching symptoms on the web.', C)
    add('https://deepchem.io/', 'DeepChem', ['açık kaynak', 'kimya', 'python'],
        'Kimya ve ilaç keşfi için makine öğrenmesi kütüphanesi; moleküler verinin hazırlanmasını da üstlenmesi ayırt edici.',
        'ML library for chemistry and drug discovery, distinguished by also handling molecular data preparation.', C)
    add('https://www.rdkit.org/', 'RDKit', ['açık kaynak', 'kimya'],
        'Kemoinformatiğin standart açık kütüphanesi; moleküler işlemler için fiilî temel, üzerine kurulan araçların çoğu buna dayanır.',
        'The standard open cheminformatics library — the de facto base most molecular tooling is built on.', C)
    add('https://github.com/ur-whitelab/chemcrow-public', 'ChemCrow', ['açık kaynak', 'github', 'kimya', 'agent'],
        'Kimya araçlarını kullanabilen LLM agent’ı; modelin kendi bilgisine değil, gerçek kimya kütüphanelerine başvurması ayırt edici.',
        'An LLM agent that operates chemistry tools — it consults real chemistry libraries rather than the model’s own recall.', C)
    add('https://alphafoldserver.com/', 'AlphaFold Server', ['ücretsiz', 'biyoloji'],
        'Protein yapısı tahmini için DeepMind’ın web arayüzü; kurulum gerektirmemesi araştırmacılar için giriş engelini kaldırıyor.',
        'DeepMind’s web interface for protein structure prediction; requiring no installation removes the barrier for researchers.', C)
    add('https://github.com/sokrypton/ColabFold', 'ColabFold', ['açık kaynak', 'github', 'biyoloji'],
        'AlphaFold’u Colab üzerinde hızlı çalıştıran uyarlama; kendi dizilerini toplu işlemek isteyenler için sunucudan esnek.',
        'An adaptation running AlphaFold quickly on Colab — more flexible than the server for batch-processing your own sequences.', C)

    # ---------------------------------------------------------- hukuk, iş & finans
    add('https://legalesedecoder.com/', 'Legalese Decoder', ['freemium', 'hukuk'],
        'Hukuki metni sade dile çeviren araç; genel özetleyicilerden farkı, madde yapısını koruyarak çevirmesi.',
        'Translates legal text into plain language, preserving clause structure unlike general summarisers.', C)
    add('https://www.hubspot.com/campaign-assistant', 'HubSpot Campaign Assistant', ['ücretsiz', 'pazarlama'],
        'Pazarlama metni üreten ücretsiz araç; HubSpot ekosistemine bağlanabilmesi kampanyaya taşımayı kolaylaştırıyor.',
        'Free marketing-copy generator whose tie into HubSpot makes moving the output into a campaign easy.', C)
    add('https://buffer.com/ai-assistant', 'Buffer AI Assistant', ['freemium', 'sosyal medya'],
        'Sosyal medya gönderisi üretip yeniden paketleyen asistan; zamanlama aracının içinde olması ayrı araç ihtiyacını kaldırıyor.',
        'Generates and repurposes social posts inside a scheduling tool, removing the need for a separate app.', C)
    add('https://predis.ai/', 'Predis.ai', ['freemium', 'sosyal medya'],
        'Metinle birlikte görsel ve video da üreten sosyal medya aracı; yalnız metin üretenlerden farkı bu.',
        'Social media tool generating visuals and video alongside copy — the difference from text-only generators.', C)
    add('https://simplified.com/', 'Simplified', ['freemium', 'pazarlama'],
        'Tasarım, metin, video ve zamanlamayı tek uygulamada toplayan set; parça parça araç kullanmaya alternatif.',
        'Bundles design, copy, video and scheduling in one app — an alternative to stitching separate tools.', C)
    add('https://facebook.github.io/prophet/', 'Prophet', ['açık kaynak', 'finans', 'python'],
        'Zaman serisi tahmini için kütüphane; tatil ve mevsimsellik etkilerini varsayılan olarak modellemesi ayırt edici yanı.',
        'Time-series forecasting library whose distinguishing trait is modelling holidays and seasonality by default.', C)
    add('https://github.com/AI4Finance-Foundation/FinGPT', 'FinGPT', ['açık kaynak', 'github', 'finans'],
        'Finans alanına açık kaynak model ve veri hattı; kapalı finansal terminallere araştırma amaçlı alternatif.',
        'Open-source models and data pipelines for finance — a research alternative to closed financial terminals.', C)
    add('https://www.quantconnect.com/', 'QuantConnect', ['freemium', 'finans', 'algoritmik'],
        'Algoritmik strateji yazıp geçmiş veriyle test etme platformu; veri ve altyapıyı hazır vermesiyle kendi kurulumundan hızlı.',
        'Platform for writing and backtesting algorithmic strategies, faster than a home setup because data and infrastructure come ready.', C)
