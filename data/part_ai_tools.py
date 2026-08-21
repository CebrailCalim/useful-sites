# -*- coding: utf-8 -*-
"""AI - Applied Tools"""

C = 'yz_arac'


def load(add):
    # ---------------------------------------------------------- coding assistants
    add('https://github.com/features/copilot', 'GitHub Copilot', ['saas', 'freemium', 'kod', 'eklenti'],
        'Editör içi tamamlama ve sohbet; kurumsal planda kodun modele gönderilip gönderilmeyeceği '
        'politika olarak yönetilebiliyor. Bu yönetişim tarafı rakiplerinde zayıf.',
        'In-editor completion and chat, with enterprise policy control over whether code is sent to the model at all. '
        'That governance side is where rivals are thin.', C)
    add('https://cursor.com/', 'Cursor', ['masaüstü', 'freemium', 'kod', 'editör'],
        'VS Code çatalı; kod tabanını indeksleyip çok dosyalı düzenlemeyi ana akış hâline getiriyor. '
        'Eklentiden farkı, değişikliği diff olarak önerip onayını beklemesi.',
        'A VS Code fork that indexes your codebase and makes multi-file editing the primary flow. '
        'Unlike a plugin it proposes changes as diffs and waits for approval.', C)
    add('https://windsurf.com/', 'Windsurf', ['masaüstü', 'freemium', 'kod', 'agent'],
        'Cursor’ın en yakın rakibi; Cascade kipi uzun görevleri kendi başına yürütüp gerektiğinde '
        'terminal komutu çalıştırıyor. Otonomi daha yüksek, denetim daha az.',
        'Cursor’s closest rival; its Cascade mode carries long tasks alone and runs terminal commands when needed. '
        'More autonomy, less oversight.', C)
    add('https://www.continue.dev/', 'Continue', ['açık-kaynak', 'eklenti', 'kod', 'apache-2'],
        'VS Code ve JetBrains eklentisi; hangi modelin tamamlama, hangisinin sohbet yapacağını '
        'ayrı ayrı seçiyorsun. Yerel model bağlayıp kodu dışarı hiç göndermemek mümkün.',
        'A VS Code and JetBrains plugin where you pick which model does completion and which does chat, separately. '
        'You can point it at a local model and never send code out.', C)
    add('https://aider.chat/', 'Aider', ['açık-kaynak', 'cli', 'kod', 'git'],
        'Terminalde çalışıyor ve her değişikliği ayrı bir git commit’i olarak yazıyor. '
        'Beğenmediğin adımı `git revert` ile geri almak, editör tabanlı asistanlarda olmayan bir güvenlik ağı.',
        'Runs in the terminal and writes each change as its own git commit. Reverting a step you dislike with '
        '`git revert` is a safety net editor-based assistants do not offer.', C)
    add('https://cline.bot/', 'Cline', ['açık-kaynak', 'eklenti', 'kod', 'agent'],
        'VS Code içinde dosya oluşturup komut çalıştırabiliyor ama her eylem için ayrı onay istiyor. '
        'Yavaşlatan bu adım, aynı zamanda otonom agent’larda kaybettiğin denetimi geri veriyor.',
        'Creates files and runs commands inside VS Code, asking approval for each action. '
        'That slowing step is also what returns the oversight autonomous agents take away.', C)
    add('https://roocode.com/', 'Roo Code', ['açık-kaynak', 'eklenti', 'kod', 'agent'],
        'Cline’dan çatallanmış; mimar, kodcu ve hata ayıklayıcı kipleri ayrı sistem istemi ve '
        'ayrı model kullanabiliyor. Planlamaya güçlü, kodlamaya ucuz model koymak mümkün.',
        'Forked from Cline, with architect, coder and debugger modes carrying separate system prompts and models. '
        'You can put a strong model on planning and a cheap one on coding.', C)
    add('https://www.tabbyml.com/', 'Tabby', ['açık-kaynak', 'self-hosted', 'kod', 'rust'],
        'Kendi sunucunda çalışan tamamlama motoru; Rust ile yazılmış, tek GPU’da barınıyor. '
        'Kodun kurum dışına çıkmaması gereken durumlarda Copilot’un yerine geçen seçenek.',
        'A self-hosted completion engine written in Rust that fits on one GPU. '
        'The Copilot substitute when code must not leave the building.', C)
    add('https://www.all-hands.dev/', 'OpenHands', ['açık-kaynak', 'agent', 'kod', 'docker'],
        'Tarayıcı ve terminal kullanabilen otonom geliştirme agent’ı; izole bir Docker kapsayıcısında çalışıyor. '
        'Satır tamamlamak değil, bir konuyu (issue) baştan sona kapatmak için tasarlanmış.',
        'An autonomous development agent with browser and terminal access, running in an isolated Docker container. '
        'Built to close an issue end to end, not to complete a line.', C)
    add('https://www.blackbox.ai/', 'Blackbox AI', ['saas', 'freemium', 'kod', 'arama'],
        'Kod parçası aramayı sohbetle birleştiriyor; depo ve dokümanlarda arayıp bulduğunu bağlam olarak kullanıyor.',
        'Merges snippet search with chat, searching repositories and docs and using the hits as context.', C)
    add('https://codegeex.cn/', 'CodeGeeX', ['ücretsiz', 'kod', 'eklenti', 'çok-dilli'],
        'Açık kod modeli ve eklentisi; Çince arayüz ve bölgesel altyapı sunuyor. '
        'Batı servislerine erişimin sınırlı olduğu yerlerde çalışan bir alternatif.',
        'An open code model and plugin with a Chinese interface and regional infrastructure — '
        'a working alternative where access to Western services is limited.', C)
    add('https://replit.com/', 'Replit', ['saas', 'freemium', 'tarayıcı-içi', 'ide'],
        'Tarayıcıda tam bir geliştirme ortamı: düzenleme, çalıştırma ve yayına alma aynı sekmede. '
        'Kurulum yükü sıfır olduğu için öğretim ortamlarında yaygın.',
        'A complete development environment in the browser — edit, run and deploy in one tab. '
        'Zero setup is why it is common in teaching.', C)
    add('https://pieces.app/', 'Pieces for Developers', ['masaüstü', 'freemium', 'not', 'bellek'],
        'Kod parçalarını kaynağı ve o an ne yaptığınla birlikte saklıyor; sonra “geçen hafta şu hatayı '
        'çözerken kullandığım şey” diye arayabiliyorsun. Yerelde çalışan bir model kullanma seçeneği var.',
        'Stores snippets with their source and what you were doing at the time, so you can later search for '
        '“the thing I used while fixing that bug last week”. It can run on a local model.', C)
    add('https://v0.app/', 'v0', ['saas', 'freemium', 'ui', 'react'],
        'Metinden React bileşeni üretiyor; çıktı shadcn/ui ve Tailwind kullanıyor, yani '
        'mevcut bir projeye kopyalanabilir kod çıkıyor. Tam uygulama değil, parça üretiyor.',
        'Generates React components from text, using shadcn/ui and Tailwind so the output is copy-ready into '
        'an existing project. It produces pieces, not whole applications.', C)
    add('https://bolt.new/', 'Bolt.new', ['saas', 'freemium', 'ui', 'webcontainer'],
        'Node.js’i WebContainer ile tarayıcıda çalıştırıyor; üretilen tam yığın uygulama sunucuya '
        'gitmeden anında önizleniyor. Hata çıkarsa aynı yerde düzeltiliyor.',
        'Runs Node.js in the browser via WebContainers, so the generated full-stack app previews instantly '
        'without a server round trip, and errors are fixed in place.', C)
    add('https://lovable.dev/', 'Lovable', ['saas', 'freemium', 'ui', 'tam-yığın'],
        'Sohbetle uygulama kurup Supabase bağlantısı ve dağıtımı da üstleniyor. '
        'v0 bileşen verirken bu çalışan ve veritabanı bağlı bir ürün hedefliyor.',
        'Builds an app from chat and takes on the Supabase wiring and deployment too. '
        'Where v0 hands you a component, this aims at a running, database-backed product.', C)
    add('https://stitch.withgoogle.com/', 'Stitch', ['saas', 'ücretsiz', 'ui', 'tasarım'],
        'Metin ya da kaba çizimden arayüz tasarımı üretip düzenlenebilir tasarım dosyası veriyor. '
        'Kod üreten araçların aksine çıktısı tasarımcının devralabileceği biçimde.',
        'Turns text or a rough sketch into UI and hands back an editable design file — unlike the code generators, '
        'output a designer can take over.', C)
    add('https://github.com/resumax', 'ResuMax', ['açık-kaynak', 'github', 'kariyer'],
        'Özgeçmişi hedef ilana göre uyarlayan araç; ATS taramasından geçecek biçimlendirmeye dikkat ediyor. '
        'Genel yazım asistanlarının atladığı nokta bu eşleştirme.',
        'Tailors a résumé to a specific posting and watches the formatting that ATS parsers need. '
        'That matching step is what general writing assistants miss.', C)

    # ---------------------------------------------------------- image generation
    add('https://firefly.adobe.com/', 'Adobe Firefly', ['saas', 'freemium', 'difüzyon', 'ticari'],
        'Adobe Stock ve süresi dolmuş telifli eserlerle eğitildiği için ticari kullanımda hukuki risk düşük. '
        'Müşteri işinde tercih edilmesinin sebebi görsel kalitesi değil, bu lisans netliği.',
        'Trained on Adobe Stock and public-domain work, so commercial legal risk is low. '
        'It gets picked for client work because of that licence clarity, not image quality.', C)
    add('https://leonardo.ai/', 'Leonardo AI', ['saas', 'freemium', 'difüzyon', 'oyun'],
        'Kendi görsellerinle stil modeli eğitip tekrar kullanabiliyorsun; oyun varlığı üretiminde '
        'tutarlı görünüm gerektiğinde bu belirleyici oluyor.',
        'You can train a style model on your own images and reuse it, which becomes decisive when game assets '
        'need a consistent look.', C)
    add('https://ideogram.ai/', 'Ideogram', ['saas', 'freemium', 'difüzyon', 'tipografi'],
        'Görsel içinde okunaklı metin üretebilen ender modellerden. Afiş, logo ve ambalaj denemelerinde '
        'diğer difüzyon modellerinin bozduğu harfleri düzgün çıkarıyor.',
        'One of the few models that renders legible text inside an image, getting letters right on posters, '
        'logos and packaging where other diffusion models mangle them.', C)
    add('https://designer.microsoft.com/', 'Microsoft Designer', ['saas', 'ücretsiz', 'tasarım', 'şablon'],
        'Üretilen görseli katmanlı ve düzenlenebilir bir tasarım olarak veriyor; '
        'saf üreticilerde elde ettiğin düz raster dosyanın aksine üzerinde çalışmaya devam edebiliyorsun.',
        'Returns the generated image as a layered, editable layout, so unlike the flat raster you get from pure '
        'generators you can keep working on it.', C)
    add('https://www.bing.com/images/create', 'Bing Image Creator', ['ücretsiz', 'difüzyon'],
        'DALL·E tabanlı, Microsoft hesabı dışında engel yok. '
        'Kalite üst sınıf değil ama sürtünmesi en düşük seçeneklerden.',
        'DALL·E-based with no barrier beyond a Microsoft account. Not top-tier quality, but among the lowest-friction options.', C)
    add('https://www.craiyon.com/', 'Craiyon', ['ücretsiz', 'difüzyon'],
        'Kayıt istemeden çalışıyor. Çıktı kalitesi güncel modellerin belirgin gerisinde; '
        'hızlı ve engelsiz denemeden başka bir iddiası yok.',
        'Works without signup. Output quality sits well behind current models; it claims nothing beyond '
        'fast, frictionless experimentation.', C)
    add('https://playground.com/', 'Playground AI', ['saas', 'freemium', 'difüzyon', 'düzenleme'],
        'Üretim ve düzenlemeyi aynı tuvalde birleştiriyor; bölge seçip yalnızca orayı yeniden üretmek '
        '(inpainting) akışın parçası. Parça parça düzeltmeye elverişli.',
        'Combines generation and editing on one canvas, with region-selective regeneration (inpainting) built into '
        'the flow — which suits piecemeal correction.', C)
    add('https://piclumen.com/', 'PicLumen', ['ücretsiz', 'difüzyon', 'karakter'],
        'Karakter ve ürün görsellerine yoğunlaşmış; ücretsiz katmanı günlük kullanıma yetecek kadar cömert.',
        'Focused on character and product imagery, with a free tier generous enough for daily use.', C)
    add('https://github.com/AUTOMATIC1111/stable-diffusion-webui', 'Stable Diffusion WebUI', ['açık-kaynak', 'github', 'yerel-model', 'difüzyon'],
        'Yerel görsel üretimin en yaygın arayüzü; eklenti ekosistemi (ControlNet, LoRA yükleyiciler) '
        'çok geniş. Depo artık aktif geliştirilmiyor ama kurulu tabanı hâlâ en büyüğü.',
        'The most widespread interface for local generation, with a huge extension ecosystem (ControlNet, LoRA loaders). '
        'The repo is no longer actively developed, but the installed base is still the largest.', C)
    add('https://www.comfy.org/', 'ComfyUI', ['açık-kaynak', 'yerel-model', 'difüzyon', 'düğüm'],
        'Üretim hattını düğüm grafiği olarak kuruyorsun: model yükleme, örnekleme, VAE çözme ayrı düğümler. '
        'Kurulumu zahmetli ama akış JSON olarak paylaşılıp birebir tekrar edilebiliyor.',
        'You build the pipeline as a node graph — model loading, sampling, VAE decode as separate nodes. '
        'Harder to set up, but a workflow exports as JSON and reproduces exactly.', C)
    add('https://github.com/lllyasviel/Fooocus', 'Fooocus', ['açık-kaynak', 'github', 'yerel-model', 'difüzyon'],
        'ComfyUI’nin karşı kutbu: örnekleyici, adım sayısı, CFG gibi ayarları gizleyip iyi varsayılanlarla '
        'çalışıyor. Midjourney benzeri bir deneyimi yerelde vermeyi hedefliyor.',
        'The opposite pole from ComfyUI — it hides sampler, steps and CFG behind good defaults, '
        'aiming to deliver a Midjourney-like experience locally.', C)
    # invoke.com satisa cikarildi (Ag 2026); projenin gercek adresi depo.
    add('https://github.com/invoke-ai/InvokeAI', 'InvokeAI', ['açık-kaynak', 'yerel-model', 'difüzyon', 'tuval'],
        'Sonsuz tuval üzerinde bölgesel üretim ve düzenleme; profesyonel iş akışı ve ekip kullanımı '
        'düşünülerek yapılmış. Ticari bir sürümü de var.',
        'Regional generation and editing on an infinite canvas, built with professional workflows and team use '
        'in mind. A commercial edition exists alongside.', C)
    add('https://github.com/Acly/krita-ai-diffusion', 'Krita AI Diffusion', ['açık-kaynak', 'github', 'eklenti', 'difüzyon'],
        'Krita’nın katman ve maske sistemini doğrudan difüzyona bağlıyor; seçim yapıp o bölgeyi üretiyorsun. '
        'Ayrı bir araca geçmeden mevcut çizim akışının içinde kalıyorsun.',
        'Wires Krita’s layers and masks straight into diffusion — select a region and generate into it. '
        'You stay inside your existing painting flow instead of switching tools.', C)
    add('https://www.recraft.ai/projects', 'Recraft', ['saas', 'freemium', 'vektör', 'tasarım'],
        'SVG çıktı üretebiliyor. Logo, ikon ve illüstrasyon işlerinde raster üreticilerden temel farkı bu: '
        'sonucu ölçekleyip düzenleyebiliyorsun.',
        'Can output SVG. For logos, icons and illustration that is the fundamental split from raster generators — '
        'the result scales and stays editable.', C)
    add('https://www.remove.bg/', 'remove.bg', ['saas', 'freemium', 'görsel', 'api'],
        'Tek işe odaklı arka plan silme; API ve toplu işlem sunduğu için hattın içine gömülebiliyor. '
        'Saç ve şeffaf yüzey kenarlarında genel araçlardan iyi.',
        'Single-purpose background removal with an API and batch mode, so it drops into a pipeline. '
        'Better than general tools on hair and transparent edges.', C)
    add('https://clipdrop.co/', 'Clipdrop', ['saas', 'freemium', 'görsel', 'araç-seti'],
        'Nesne silme, yeniden ışıklandırma, büyütme ve arka plan değiştirmeyi tek yerde topluyor. '
        'Her biri için ayrı servis aramak yerine bir hesapla dolaşabiliyorsun.',
        'Bundles object removal, relighting, upscaling and background replacement in one place, '
        'so one account covers what would otherwise be several services.', C)
    add('https://app.gptzero.me/home', 'GPTZero', ['saas', 'freemium', 'tespit'],
        'Metnin yapay zeka üretimi olma olasılığını tahmin ediyor. Sonuç olasılıksal — '
        'kendi belgeleri de yanlış pozitif oranını kabul ediyor, delil olarak kullanılmamalı.',
        'Estimates the probability that a text was AI-generated. The result is probabilistic and its own docs '
        'acknowledge false positives — it should not be treated as proof.', C)

    # ---------------------------------------------------------- 3D & space
    add('https://www.meshy.ai/tr/?noRedirect=true', 'Meshy', ['saas', 'freemium', 'text-to-3d'],
        'Metin ya da görselden 3B model üretip PBR dokusunu da kendisi giydiriyor. '
        'Oyun varlığı hattında en çok vakit yiyen adımın doku olması bunu değerli kılıyor.',
        'Generates a 3D model from text or an image and applies PBR textures itself. '
        'Texturing being the slowest step in an asset pipeline is what makes that matter.', C)
    add('https://www.tripo3d.ai/', 'Tripo AI', ['saas', 'freemium', 'text-to-3d'],
        'Meshy’nin doğrudan rakibi; üretim süresi daha kısa ve çıkan topoloji genelde daha temiz, '
        'yani sonradan elle düzeltme yükü az.',
        'A direct rival to Meshy with shorter generation times and generally cleaner topology, '
        'which means less manual cleanup afterwards.', C)
    add('https://spline.design/', 'Spline', ['saas', 'freemium', '3b', 'web'],
        'Tarayıcıda 3B sahne tasarlayıp doğrudan web sayfasına gömüyorsun. '
        'Blender gibi genel amaçlı değil; çıktısı baştan web için optimize edilmiş.',
        'Design a 3D scene in the browser and embed it straight into a page. Not general-purpose like Blender — '
        'the output is optimised for the web from the start.', C)
    add('https://github.com/gd3kr/BlenderGPT', 'BlenderGPT', ['açık-kaynak', 'github', 'blender', 'eklenti'],
        'Doğal dil komutunu Blender Python API çağrısına çeviriyor. Model üretmiyor; '
        'Blender’ın kendi araçlarını senin yerine kullanıyor, yani sonuç tekrar edilebilir kalıyor.',
        'Translates a natural-language instruction into Blender Python API calls. It does not generate models — '
        'it operates Blender’s own tools for you, so the result stays reproducible.', C)
    add('https://github.com/carson-katri/dream-textures', 'Dream Textures', ['açık-kaynak', 'github', 'blender', 'doku'],
        'Blender içinde doku ve HDRI üretiyor; kesintisiz (seamless) döşeme ve projeksiyonla '
        'doğrudan mesh üzerine boyama yapabiliyor. Dışarıda üretip içeri aktarma adımı kalkıyor.',
        'Generates textures and HDRIs inside Blender, with seamless tiling and projection painting straight onto '
        'a mesh — removing the generate-elsewhere-then-import step.', C)
    add('https://huggingface.co/stabilityai/stable-fast-3d', 'Stable Fast 3D', ['açık-ağırlık', 'text-to-3d', 'model'],
        'Tek görselden yarım saniyede UV açılmış ve dokulu mesh çıkarıyor. '
        'Kalite üst düzey değil ama toplu varlık üretiminde hız farkı belirleyici.',
        'Produces a UV-unwrapped, textured mesh from one image in about half a second. Quality is not top-tier, '
        'but at batch scale the speed difference decides.', C)
    add('https://github.com/openai/shap-e', 'Shap-E', ['açık-kaynak', 'github', 'text-to-3d', 'araştırma'],
        'Metinden doğrudan örtük 3B temsil üreten OpenAI modeli. Araştırma sürümü — '
        'çıktısı üretim kalitesinde değil, tarihsel ve akademik değeri var.',
        'An OpenAI model producing implicit 3D representations from text. A research release: the output is not '
        'production quality, and its value is historical and academic.', C)
    add('https://github.com/openai/point-e', 'Point-E', ['açık-kaynak', 'github', 'text-to-3d', 'araştırma'],
        'Shap-E’den önceki nesil; nokta bulutu üretiyor, mesh’e dönüştürmek ayrı bir adım. '
        'Hızlı ama sonuç kaba, bugün pratik bir kullanımı kalmadı.',
        'The generation before Shap-E, producing point clouds that need a separate meshing step. '
        'Fast but coarse, with little practical use left today.', C)
    add('https://github.com/TencentARC/InstantMesh', 'InstantMesh', ['açık-kaynak', 'github', 'text-to-3d'],
        'Tek görselden çok görünüşlü difüzyonla ara görüntüler üretip bunlardan mesh çıkarıyor. '
        'Nokta bulutu değil doğrudan kullanılabilir yüzey vermesi, hattın kalan adımlarını kısaltıyor.',
        'Generates intermediate views from one image via multi-view diffusion, then reconstructs a mesh. '
        'Returning usable surfaces rather than a point cloud shortens the rest of the pipeline.', C)
    add('https://planner5d.com/', 'Planner 5D', ['saas', 'freemium', 'mimari', 'iç-mekan'],
        'Kat planı çizip anında 3B görselleştirme alıyorsun. CAD hassasiyeti yok; '
        'ölçülü teknik çizim değil, hızlı sunum görseli için.',
        'Draw a floor plan and get an instant 3D render. No CAD precision — it is for a fast presentation image, '
        'not a dimensioned technical drawing.', C)
    add('https://www.homestyler.com/', 'Homestyler', ['saas', 'freemium', 'iç-mekan', 'katalog'],
        'Gerçek mobilya markalarının kataloğu üzerinden tasarım yapıyorsun, yani çıkan sahnedeki '
        'her parçanın satın alınabilir bir karşılığı var.',
        'You design from catalogues of real furniture brands, so every item in the scene has a purchasable counterpart.', C)
    add('https://www.blueprint.am/', 'Blueprint.am', ['saas', 'donanım', 'eda'],
        'Donanım ve devre tasarımına yapay zeka desteği getiriyor. '
        'Yazılım asistanlarının yoğunlaştığı alanın dışında kalan, seyrek işlenmiş bir konu.',
        'Brings AI assistance to hardware and circuit design — a thinly covered area outside where software '
        'assistants have crowded in.', C)

    # ---------------------------------------------------------- video & audio
    add('https://www.capcut.com/', 'CapCut', ['masaüstü', 'freemium', 'video', 'altyazı'],
        'Otomatik altyazı, konuşmacı takibi ve dikey format şablonları. '
        'Kısa video akışında Premiere gibi paketlerden kat kat hızlı; renk ve ses tarafında ise sığ.',
        'Auto-captioning, speaker tracking and vertical-format templates. Far faster than Premiere for short-form, '
        'and correspondingly shallow on colour and audio.', C)
    add('https://pika.art/', 'Pika', ['saas', 'freemium', 'video', 'difüzyon'],
        'Metin ve görselden kısa video üretiyor; kamera hareketi ve efektleri parametre olarak seçiliyor. '
        'İstemle rastgele sonuç beklemek yerine hareketi yönlendirebiliyorsun.',
        'Generates short video from text and images, with camera motion and effects exposed as parameters — '
        'you steer the motion instead of hoping the prompt lands.', C)
    add('https://lumalabs.ai/', 'Luma AI', ['saas', 'freemium', 'video', 'nerf'],
        'Video üretiminin yanında telefonla çektiğin nesneyi NeRF/Gaussian splatting ile 3B’ye çeviriyor. '
        'Bu ikinci ayak onu saf video modellerinden ayırıyor.',
        'Alongside video generation it turns an object you filmed on a phone into 3D via NeRF/Gaussian splatting. '
        'That second leg is what separates it from pure video models.', C)
    add('https://github.com/jamiepine/voicebox', 'Voicebox', ['açık-kaynak', 'github', 'ses', 'tts'],
        'Ses klonlama, dikte ve üretimi tek açık kaynak stüdyoda topluyor. '
        'Ses örneğinin bulut servisine yüklenmemesi, klonlamada gerçek bir gizlilik farkı.',
        'Bundles voice cloning, dictation and generation into one open-source studio. Keeping the voice sample '
        'off a cloud service is a real privacy difference for cloning.', C)
    add('https://github.com/openai/whisper', 'Whisper', ['açık-kaynak', 'github', 'stt', 'yerel-model'],
        'Konuşma tanımanın açık standardı; 90+ dili destekliyor, Türkçede de kullanılabilir doğrulukta. '
        'Yerelde çalıştığı için kayıt makineden hiç çıkmıyor.',
        'The open standard for speech recognition, covering 90+ languages at usable accuracy in Turkish too. '
        'It runs locally, so the recording never leaves the machine.', C)
    add('https://otter.ai/', 'Otter.ai', ['saas', 'freemium', 'stt', 'toplantı'],
        'Toplantıya katılıp canlı yazıya döküyor ve konuşmacıları ayırıyor. '
        'Kayıt sonrası yükleme yapan araçlardan farkı, toplantı sürerken not almanı bırakabilmen.',
        'Joins a meeting, transcribes live and separates speakers. Unlike upload-after-the-fact tools '
        'it lets you stop taking notes while the meeting is still running.', C)
    add('https://fireflies.ai/', 'Fireflies.ai', ['saas', 'freemium', 'toplantı', 'özet'],
        'Ham döküm yerine karar, aksiyon maddesi ve soru listesi çıkarıyor; CRM’e yazabiliyor. '
        'Otter dökümde, bu çıkarımda yoğunlaşmış.',
        'Extracts decisions, action items and questions rather than a raw transcript, and can write into a CRM. '
        'Otter concentrates on transcription; this on extraction.', C)
    add('https://krisp.ai/', 'Krisp', ['masaüstü', 'freemium', 'ses'],
        'Sanal mikrofon aygıtı olarak kurulup gürültüyü kaynakta kesiyor — Zoom, Teams, kayıt yazılımı '
        'fark etmeksizin hepsinde çalışıyor. Uygulama bazlı çözümlerin sınırı burada aşılıyor.',
        'Installs as a virtual microphone device and kills noise at the source, so it works across Zoom, Teams '
        'and any recorder alike — past the limit of per-app solutions.', C)
    add('https://auphonic.com/', 'Auphonic', ['saas', 'freemium', 'ses', 'podcast'],
        'Seviye eşitleme, gürültü azaltma ve yayın normlarına (LUFS) göre ses yüksekliği ayarı yapıyor. '
        'Canlı değil son işlem aracı; podcast yayımlamadan önceki son adım.',
        'Levels, denoises and normalises loudness to broadcast targets (LUFS). A post-production tool, not a live one — '
        'the last step before a podcast ships.', C)

    # ---------------------------------------------------------- research & documents
    add('https://elicit.com/', 'Elicit', ['saas', 'freemium', 'akademik', 'tarama'],
        'Yüzlerce makaleyi tarayıp örneklem büyüklüğü, yöntem ve bulgu gibi alanları tabloya çıkarıyor. '
        'Sistematik derleme yaparken en çok vakit yiyen adım tam olarak bu ayıklama.',
        'Screens hundreds of papers and extracts fields like sample size, method and finding into a table — '
        'precisely the screening step that eats the most time in a systematic review.', C)
    add('https://consensus.app/', 'Consensus', ['saas', 'freemium', 'akademik'],
        'Bir soruya literatürün ne yönde eğildiğini özetliyor ve destekleyen/çelişen çalışma oranını gösteriyor. '
        'Tek makale bulmakla alanın genel eğilimini görmek farklı işler.',
        'Summarises which way the literature leans on a question and shows the ratio of supporting to contradicting '
        'studies. Finding one paper and seeing the field’s tendency are different jobs.', C)
    add('https://www.researchrabbit.ai/', 'ResearchRabbit', ['ücretsiz', 'akademik', 'graf'],
        'Bir makaleden başlayıp atıf ve ortak yazar ağını görsel olarak genişletiyorsun. '
        'Anahtar kelimeyi bilmediğin için kaçırdığın komşu çalışmalar böyle çıkıyor.',
        'Start from one paper and expand the citation and co-author network visually. '
        'This is how you surface adjacent work you missed because you did not know its keyword.', C)
    add('https://scispace.com/', 'SciSpace', ['saas', 'freemium', 'akademik'],
        'Makaleyi paragraf paragraf açıklıyor, seçtiğin denklemi ya da terimi yerinde çözüyor. '
        'Alan dışından okuyan biri için kritik olan, özet değil bu satır içi açıklama.',
        'Explains a paper paragraph by paragraph, unpacking a chosen equation or term in place. '
        'For a reader from outside the field, that inline explanation matters more than a summary.', C)
    add('https://www.explainpaper.com/', 'Explainpaper', ['saas', 'freemium', 'akademik'],
        'PDF’te işaretlediğin pasajı sadeleştiriyor. Tüm belgeyi özetlemiyor — '
        'takıldığın tek yeri açması onu dar ama isabetli kılıyor.',
        'Simplifies whichever passage you highlight in a PDF. It does not summarise the document; '
        'opening up the one place you got stuck is what makes it narrow but accurate.', C)
    add('https://www.scholarcy.com/', 'Scholarcy', ['saas', 'freemium', 'akademik', 'özet'],
        'Makaleyi yapılandırılmış kartlara indiriyor: temel iddia, yöntem, kısıtlar, atıflar ayrı ayrı. '
        'Hangi çalışmayı tam okuyacağına karar verdiğin ayıklama aşaması için.',
        'Reduces a paper to structured cards — core claim, method, limitations, references, each separate. '
        'For the triage stage where you decide what to read in full.', C)
    add('https://askyourpdf.com/', 'AskYourPDF', ['saas', 'freemium', 'pdf', 'rag'],
        'Birden çok belgeyi tek kütüphanede toplayıp hepsine birden soru sorabiliyorsun; '
        'cevaplar sayfa numarasıyla geliyor. Tek dosyalık araçlardan ayrıldığı yer bu.',
        'Collects many documents into one library you can query together, with page-cited answers. '
        'That is where it parts from single-file tools.', C)
    add('https://www.chatpdf.com/', 'ChatPDF', ['saas', 'freemium', 'pdf'],
        'Kayıt olmadan dosya yükleyip soru sorabiliyorsun. Tek belgeye hızlı bakış için en düşük sürtünmeli yol; '
        'kütüphane yönetimi ya da çoklu belge desteği yok.',
        'Upload and ask without signing up — the lowest-friction path to interrogating a single document. '
        'No library management or multi-document support.', C)
    add('https://www.humata.ai/', 'Humata', ['saas', 'freemium', 'pdf', 'teknik'],
        'Uzun teknik belgeleri karşılaştırmalı okumaya yönelik; her cevabın altında kaynak sayfa bağlantısı var, '
        'yani iddiayı belgede doğrulayabiliyorsun.',
        'Aimed at comparative reading of long technical documents, with a source-page link under each answer '
        'so you can verify the claim in the document itself.', C)
    add('https://pdf.ai/', 'PDF.ai', ['saas', 'freemium', 'pdf', 'eklenti'],
        'Tarayıcı eklentisiyle web’de karşılaştığın PDF’lerde de çalışıyor — '
        'indirip yükleme adımını atlamış oluyorsun.',
        'A browser extension makes it work on PDFs you meet on the web, skipping the download-then-upload step.', C)
    add('https://lightpdf.com/', 'LightPDF', ['saas', 'freemium', 'pdf', 'araç-seti'],
        'Dönüştürme, sıkıştırma, imzalama ve OCR gibi klasik PDF işlerinin üzerine sohbet eklenmiş. '
        'Tek işlevli rakiplerine göre geniş, her bir işlevde ise ortalama.',
        'Classic PDF chores — convert, compress, sign, OCR — with chat layered on. Broader than the single-purpose '
        'rivals and average at each individual job.', C)

    # ---------------------------------------------------------- writing & presentation
    add('https://www.grammarly.com/', 'Grammarly', ['saas', 'freemium', 'yazım', 'ingilizce'],
        'Yazdığın her yere giren eklentisiyle İngilizce dil bilgisi ve üslup denetimi. '
        'Türkçe desteklemiyor; yalnızca İngilizce yazarken anlamlı.',
        'English grammar and style checking through an extension that follows you everywhere you type. '
        'No Turkish support — it only makes sense when you write in English.', C)
    add('https://languagetool.org/', 'LanguageTool', ['açık-kaynak', 'yazım', 'çok-dilli', 'self-hosted'],
        '30’dan fazla dili, Türkçe dahil, kural tabanlı olarak denetliyor ve kendi sunucunda çalıştırılabiliyor. '
        'Metnin bir şirkete gitmemesi gerektiği durumlarda tek gerçek seçenek.',
        'Rule-based checking for 30+ languages including Turkish, and it can be self-hosted — '
        'the only real option when the text must not go to a company.', C)
    add('https://www.deepl.com/write', 'DeepL Write', ['saas', 'freemium', 'yazım'],
        'Hatayı işaretlemek yerine cümleyi yeniden kuruyor ve ton seçenekleri sunuyor. '
        'Grammarly düzeltiyor, bu yeniden yazıyor — ikisi farklı iş.',
        'Rewrites the sentence and offers tone variants instead of flagging errors. '
        'Grammarly corrects, this rewrites — two different jobs.', C)
    add('https://quillbot.com/', 'QuillBot', ['saas', 'freemium', 'yazım'],
        'Aynı cümlenin farklı ifade edilişlerini üretiyor; uzunluk ve resmiyet ayarlanabiliyor. '
        'Akademik yazımda intihal riskini artırabileceği için dikkatli kullanılması gereken bir araç.',
        'Produces alternative phrasings of the same sentence with adjustable length and formality. '
        'In academic writing it can raise plagiarism risk, so it needs careful use.', C)
    add('https://gamma.app/', 'Gamma', ['saas', 'freemium', 'sunum'],
        'Slayt yerine kaydırılabilir sayfa üretiyor; içerik uzadıkça düzen kendini ayarlıyor, '
        'kutuya sığdırma derdi kalkıyor. Çıktı PowerPoint ve PDF olarak alınabiliyor.',
        'Produces scrollable pages rather than slides, with the layout adapting as content grows so you stop '
        'fighting to fit a box. Exports to PowerPoint and PDF.', C)
    add('https://www.napkin.ai/', 'Napkin AI', ['saas', 'freemium', 'diyagram'],
        'Düz metinden akış şeması, zaman çizelgesi ve karşılaştırma görseli üretiyor; '
        'çıktı düzenlenebilir vektör. Sunum üretmiyor, tek bir fikri görselleştiriyor.',
        'Turns plain prose into flow charts, timelines and comparison graphics as editable vectors. '
        'It does not build decks; it visualises one idea.', C)
    add('https://www.canva.com/', 'Canva', ['saas', 'freemium', 'tasarım', 'şablon'],
        'Şablon kütüphanesi ve marka kiti sayesinde tasarım bilgisi olmadan tutarlı çıktı alınıyor. '
        'Sınırı da bu: şablonların dışına çıkıldığında araç direniyor.',
        'A template library and brand kit produce consistent output without design skill. '
        'That is also the ceiling — the tool resists once you step outside the templates.', C)
    add('https://pitch.com/', 'Pitch', ['saas', 'freemium', 'sunum', 'ekip'],
        'Eşzamanlı düzenleme, yorum ve marka şablonları; sunum bir ekip belgesi gibi çalışıyor. '
        'Analitik özelliği, gönderdiğin sunumun hangi slaytta bırakıldığını gösteriyor.',
        'Live co-editing, comments and brand templates make a deck behave like a team document. '
        'Its analytics show which slide a recipient stopped on.', C)
    add('https://www.slidesai.io/', 'SlidesAI', ['eklenti', 'freemium', 'sunum'],
        'Google Slides eklentisi olarak çalışıyor; mevcut dosyandan çıkmadan metinden slayt üretiyor. '
        'Ayrı platforma taşınma ve sonra dışa aktarma adımı yok.',
        'Runs as a Google Slides add-on, generating slides from text without leaving your existing file — '
        'no migration to another platform and no export step back.', C)

    # ---------------------------------------------------------- data science & AutoML
    add('https://julius.ai/', 'Julius AI', ['saas', 'freemium', 'veri', 'analiz'],
        'CSV veya Excel yükleyip sohbetle analiz ediyorsun; arka planda Python çalıştırıp grafik üretiyor '
        've kullandığı kodu gösteriyor. Sonucu doğrulayabilmen bu şeffaflığa bağlı.',
        'Upload a CSV or Excel and analyse by chatting; it runs Python behind the scenes, produces charts and '
        'shows the code it used — which is what makes the result verifiable.', C)
    add('https://www.knime.com/', 'KNIME', ['ücretsiz', 'veri', 'düğüm', 'etl'],
        'Düğüm tabanlı görsel analiz; hattın tamamı kaydedilip tekrar çalıştırılabiliyor. '
        'Kod yazmadan tekrarlanabilirlik isteyen kurumsal veri ekiplerinde yaygın.',
        'Node-based visual analytics where the whole pipeline is saved and re-runnable. '
        'Common in enterprise data teams that need reproducibility without writing code.', C)
    add('https://orangedatamining.com/', 'Orange', ['açık-kaynak', 'python', 'veri', 'eğitim'],
        'Görsel programlamayla veri madenciliği; widget’lar scikit-learn’i sarmalıyor. '
        'KNIME’dan hafif ve görselleştirme tarafı güçlü, bu yüzden derslerde tercih ediliyor.',
        'Visual-programming data mining whose widgets wrap scikit-learn. Lighter than KNIME with stronger '
        'visualisation, which is why it shows up in teaching.', C)
    add('https://ml.cms.waikato.ac.nz/weka/', 'Weka', ['açık-kaynak', 'java', 'veri', 'akademik'],
        'Klasik makine öğrenmesi algoritmalarının Java araç kutusu; alanın en eski açık projelerinden. '
        'Modern kütüphanelerin gerisinde ama algoritmaları yan yana kıyaslamak için hâlâ düzenli.',
        'A Java toolbox of classical ML algorithms and one of the field’s oldest open projects. '
        'Behind modern libraries, yet still tidy for comparing algorithms side by side.', C)
    add('https://auto.gluon.ai/', 'AutoGluon', ['açık-kaynak', 'python', 'automl', 'apache-2'],
        'Üç satırla tablo verisinde güçlü bir taban çizgisi kuruyor; birden çok modeli eğitip '
        'yığınlayarak (stacking) birleştiriyor. Kaggle taban çizgisi olarak sık kullanılıyor.',
        'Three lines gives a strong baseline on tabular data, training several models and combining them by '
        'stacking. Frequently used as a Kaggle baseline.', C)
    add('https://h2o.ai/', 'H2O.ai', ['freemium', 'automl', 'java', 'kurumsal'],
        'Dağıtık AutoML platformu; model açıklanabilirliği ve üretime çıkarma araçları kütüphane '
        'çözümlerinden ileride. Büyük veri kümelerinde bellek dışına taşabiliyor.',
        'A distributed AutoML platform whose explainability and productionisation tooling is ahead of library-only '
        'solutions, and which can spill out of memory on large datasets.', C)
    add('https://pycaret.org/', 'PyCaret', ['açık-kaynak', 'python', 'automl', 'düşük-kod'],
        '`compare_models()` tek satırda onlarca algoritmayı çapraz doğrulamayla kıyaslayıp tabloya döküyor. '
        'Keşif aşamasında hangi model ailesinin işe yaradığını hızla eliyor.',
        '`compare_models()` cross-validates dozens of algorithms in one line and tabulates the result, '
        'quickly narrowing which model family is worth pursuing.', C)
    add('https://mljar.com/automl/', 'MLJAR AutoML', ['açık-kaynak', 'python', 'automl', 'rapor'],
        'Model seçiminin yanında Markdown rapor üretiyor: öğrenme eğrileri, önem grafikleri ve '
        'karar açıklamaları dahil. Sonucu birine sunman gerekiyorsa bu fark yaratıyor.',
        'Alongside model selection it emits a Markdown report with learning curves, importance plots and '
        'decision explanations — which matters when you have to present the result to someone.', C)
    add('https://colab.research.google.com/', 'Google Colab', ['ücretsiz', 'not-defteri', 'gpu', 'python'],
        'Tarayıcıda Jupyter; ücretsiz katmanda T4 GPU veriyor. Oturum süresi sınırlı ve makine '
        'kapanınca dosyalar gidiyor — uzun eğitimler için Drive’a bağlamak gerekiyor.',
        'Jupyter in the browser with a free T4 GPU. Sessions are time-limited and files vanish when the machine '
        'recycles, so long training runs need Drive mounted.', C)
    add('https://www.kaggle.com/code', 'Kaggle Notebooks', ['ücretsiz', 'not-defteri', 'gpu', 'veri'],
        'Veri kümeleriyle aynı platformda duran not defterleri; haftalık GPU kotası Colab’dan öngörülebilir. '
        'Asıl değeri, başkalarının çözümlerini okuyabilmen.',
        'Notebooks sitting on the same platform as the datasets, with a weekly GPU quota more predictable than Colab’s. '
        'The real value is being able to read other people’s solutions.', C)

    # ---------------------------------------------------------- health & life sciences
    add('https://www.openevidence.com/', 'OpenEvidence', ['ücretsiz', 'tıp', 'akademik'],
        'Klinik soruya yalnızca hakemli literatürden, atıf vererek cevap veriyor; '
        'kayıtlı sağlık profesyonellerine açık. Genel botların tıpta güvenilmez olmasının sebebi kaynak denetimi eksikliği — burada var.',
        'Answers clinical questions only from peer-reviewed literature, with citations, for verified health '
        'professionals. General chatbots are unreliable in medicine because they lack that source control; this has it.', C)
    add('https://deepmind.google/models/gemma/medgemma/', 'MedGemma', ['açık-ağırlık', 'tıp', 'model'],
        'Gemma’nın tıbbi metin ve görüntüye uyarlanmış açık sürümü. Araştırma amaçlı — '
        'klinik karar desteği olarak kullanılması için düzenleyici onayı yok.',
        'An open Gemma variant adapted to medical text and imaging. Research use only — '
        'it carries no regulatory clearance for clinical decision support.', C)
    add('https://github.com/microsoft/BioGPT', 'BioGPT', ['açık-kaynak', 'github', 'biyomedikal', 'model'],
        'PubMed özetleriyle eğitilmiş dil modeli; ilaç-hastalık ilişkisi çıkarımı gibi görevlerde '
        'genel modellerden isabetli. Metin üretmekten çok bilgi çıkarımı için.',
        'A language model trained on PubMed abstracts, more accurate than general models at tasks like '
        'drug–disease relation extraction. Built for information extraction rather than generation.', C)
    add('https://github.com/kbressem/medAlpaca', 'MedAlpaca', ['açık-kaynak', 'github', 'tıp', 'model'],
        'Tıbbi soru-cevap için ince ayarlanmış açık model; USMLE tarzı sınav sorularıyla '
        'değerlendirilmiş. Klinik kullanım için değil, araştırma ve sınav çalışması için.',
        'An open model fine-tuned for medical Q&A and evaluated on USMLE-style questions. '
        'For research and exam practice, not clinical use.', C)
    add('https://ada.com/', 'Ada Health', ['saas', 'ücretsiz', 'sağlık'],
        'Belirtileri yapılandırılmış soru akışıyla daraltıp olası nedenleri sıralıyor; '
        'tıbbi cihaz olarak CE işaretli. Web’de belirti aramanın disiplinli hâli.',
        'Narrows symptoms through a structured question flow and ranks possible causes; CE-marked as a medical device. '
        'The disciplined form of searching symptoms online.', C)
    add('https://deepchem.io/', 'DeepChem', ['açık-kaynak', 'python', 'kemoinformatik', 'mit'],
        'İlaç keşfi için makine öğrenmesi; moleküler özellik hesaplama ve veri kümesi yükleyicileri dahil. '
        'Kimyasal veriyi modele hazır hâle getiren sıkıcı kısmı da üstleniyor.',
        'Machine learning for drug discovery, including molecular featurisation and dataset loaders — '
        'it takes on the tedious part of getting chemical data model-ready.', C)
    add('https://www.rdkit.org/', 'RDKit', ['açık-kaynak', 'python', 'c++', 'kemoinformatik'],
        'Kemoinformatiğin temel açık kütüphanesi: SMILES ayrıştırma, alt yapı arama, parmak izi üretimi. '
        'Alandaki araçların çoğu doğrudan bunun üzerine kurulu.',
        'The foundational open cheminformatics library — SMILES parsing, substructure search, fingerprints. '
        'Most tooling in the field is built directly on it.', C)
    add('https://github.com/ur-whitelab/chemcrow-public', 'ChemCrow', ['açık-kaynak', 'github', 'agent', 'kimya'],
        'Kimya araçlarını (RDKit, reaksiyon veritabanları, sentez planlayıcıları) kullanabilen LLM agent’ı. '
        'Modelin kendi belleğine değil gerçek hesaplamalara başvurması, kimyada hata payını ciddi düşürüyor.',
        'An LLM agent that operates chemistry tools — RDKit, reaction databases, synthesis planners. '
        'Consulting real computation instead of the model’s recall sharply lowers error in chemistry.', C)
    add('https://alphafoldserver.com/', 'AlphaFold Server', ['ücretsiz', 'biyoinformatik'],
        'AlphaFold 3 ile protein, DNA ve ligand komplekslerinin yapısını tahmin ediyor; '
        'kurulum ve GPU gerekmiyor. Günlük iş sayısı sınırlı ve ticari kullanım kısıtlı.',
        'Predicts structures of protein, DNA and ligand complexes with AlphaFold 3, needing no install or GPU. '
        'Daily job counts are capped and commercial use is restricted.', C)
    add('https://github.com/sokrypton/ColabFold', 'ColabFold', ['açık-kaynak', 'github', 'biyoinformatik', 'colab'],
        'MMseqs2 ile dizi hizalamayı hızlandırıp AlphaFold’u Colab’da çalıştırılabilir hâle getiriyor. '
        'Sunucunun kotasına takılmadan kendi dizilerini toplu işlemek isteyenler için.',
        'Speeds up sequence alignment with MMseqs2 to make AlphaFold runnable in Colab — '
        'for batch-processing your own sequences without hitting the server’s quota.', C)

    # ---------------------------------------------------------- law, business & finance
    add('https://legalesedecoder.com/', 'Legalese Decoder', ['saas', 'freemium', 'hukuk'],
        'Sözleşme dilini sade Türkçeye/İngilizceye çevirirken madde yapısını koruyor, '
        'yani hangi cümlenin hangi maddeden geldiği kayboluyor değil.',
        'Translates contract language into plain prose while preserving clause structure, so you do not lose '
        'which sentence came from which clause.', C)
    add('https://www.hubspot.com/campaign-assistant', 'HubSpot Campaign Assistant', ['ücretsiz', 'pazarlama'],
        'E-posta, açılış sayfası ve reklam metnini kampanya hedefine göre üretiyor; '
        'ücretsiz ve HubSpot hesabı şart değil.',
        'Generates email, landing page and ad copy against a campaign goal, free and without requiring a HubSpot account.', C)
    add('https://buffer.com/ai-assistant', 'Buffer AI Assistant', ['saas', 'freemium', 'sosyal-medya'],
        'Zamanlama aracının içinde çalışıyor; bir gönderiyi farklı platformların ton ve uzunluğuna '
        'göre yeniden paketliyor. Ayrı bir metin aracıyla gidip gelme adımı kalkıyor.',
        'Lives inside the scheduling tool, repackaging one post for each platform’s tone and length — '
        'removing the round trip to a separate copy tool.', C)
    add('https://predis.ai/', 'Predis.ai', ['saas', 'freemium', 'sosyal-medya', 'video'],
        'Metinle birlikte görsel ve kısa video da üretiyor; rakip için düşünülmüş şablonları var. '
        'Yalnızca metin üreten araçlardan ayrıldığı yer bu.',
        'Generates visuals and short video alongside copy, with competitor-oriented templates. '
        'That is where it separates from text-only tools.', C)
    add('https://simplified.com/', 'Simplified', ['saas', 'freemium', 'pazarlama', 'araç-seti'],
        'Tasarım, metin, video düzenleme ve zamanlamayı tek uygulamada topluyor. '
        'Her alanda uzman araçların gerisinde, ama araç sayısını azaltmak istiyorsan mantıklı bir denge.',
        'Bundles design, copy, video editing and scheduling in one app. Behind the specialists at each task, '
        'but a sensible trade if reducing tool count is the goal.', C)
    add('https://facebook.github.io/prophet/', 'Prophet', ['açık-kaynak', 'python', 'r', 'zaman-serisi'],
        'Zaman serisini eğilim, mevsimsellik ve tatil etkilerine ayırıyor; parametre ayarı yapmadan '
        'makul sonuç veriyor. İstatistik bilgisi olmayan analistler için tasarlanmış.',
        'Decomposes a time series into trend, seasonality and holiday effects and gives reasonable results without '
        'tuning. Designed for analysts who are not statisticians.', C)
    add('https://github.com/AI4Finance-Foundation/FinGPT', 'FinGPT', ['açık-kaynak', 'github', 'finans', 'llm'],
        'Finansal metin için açık modeller ve veri hattı; duygu analizi ve haber sınıflandırma üzerine '
        'ince ayarlı sürümler içeriyor. Bloomberg terminaline araştırma amaçlı açık alternatif.',
        'Open models and data pipelines for financial text, including fine-tunes for sentiment and news classification. '
        'An open research alternative to a Bloomberg terminal.', C)
    add('https://www.quantconnect.com/', 'QuantConnect', ['saas', 'freemium', 'finans', 'backtest'],
        'Strateji yazıp geçmiş veriyle test ediyorsun; hisse, opsiyon, futures ve kripto verisi hazır geliyor. '
        'Kendi kurulumunda en pahalı kısım olan temiz veriyi platform sağlıyor.',
        'Write a strategy and backtest it, with equity, options, futures and crypto data supplied. '
        'The platform provides the clean data that is the costliest part of a home setup.', C)
