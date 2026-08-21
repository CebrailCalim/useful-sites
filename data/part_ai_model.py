# -*- coding: utf-8 -*-
"""AI - Models & Assistants"""

C = 'yz_model'


def load(add):
    # --- chat assistants
    add('https://chatgpt.com/', 'ChatGPT', ['saas', 'freemium', 'llm', 'asistan'],
        'Kod çalıştırma (sandbox Python), görsel üretim, dosya yükleme ve özel GPT’ler tek pencerede. '
        'Geniş olması pahasına her bir yeteneği kendi alanının en iyisi değil.',
        'Sandboxed Python execution, image generation, file upload and custom GPTs in one window. '
        'The breadth costs it depth — no single capability is best-in-class.', C)
    add('https://claude.ai/new', 'Claude', ['saas', 'freemium', 'llm', 'asistan'],
        '200K jetonluk bağlam penceresi uzun belge ve kod tabanı okumayı taşıyor. '
        'Projects, dosyaları sohbetler arası kalıcı bağlam olarak tutuyor; Artifacts çıktıyı ayrı bir panelde çalıştırıyor.',
        'A 200K-token context window carries long documents and whole codebases. '
        'Projects keeps files as persistent context across chats; Artifacts runs output in a side panel.', C)
    add('https://gemini.google.com/', 'Google Gemini', ['saas', 'freemium', 'llm', 'asistan'],
        'Gmail, Drive ve YouTube’a doğrudan bağlanıp hesabındaki içeriği kaynak alabiliyor. '
        'Bu entegrasyon onu Google ekosisteminde tutuyorsan avantajlı, tutmuyorsan sıradan kılıyor.',
        'Connects straight into Gmail, Drive and YouTube to use your own content as source. '
        'That integration is decisive if you live in Google’s ecosystem and irrelevant if you do not.', C)
    add('https://copilot.microsoft.com/', 'Microsoft Copilot', ['saas', 'ücretsiz', 'llm', 'asistan'],
        'Word, Excel ve Windows kabuğuna gömülü çalışıyor — belgeyi bir siteye kopyalamadan üzerinde işlem yapıyor. '
        'Model erişimi OpenAI’ınkiyle aynı, fark dağıtım noktasında.',
        'Runs embedded in Word, Excel and the Windows shell, so you operate on a document without copying it to a website. '
        'The underlying models are OpenAI’s; the difference is the delivery point.', C)
    add('https://www.perplexity.ai/', 'Perplexity', ['saas', 'freemium', 'arama', 'rag'],
        'Sorguyu web aramasına çevirip dönen sayfaları modele okutuyor, sonra her cümleye kaynak numarası iliştiriyor. '
        'Yani bir RAG hattı; modelin belleğine değil o anki arama sonuçlarına dayanıyor.',
        'Turns your query into a web search, feeds the retrieved pages to a model, then footnotes each sentence. '
        'It is a RAG pipeline: answers rest on live search results, not the model’s memory.', C)
    add('https://notebooklm.google.com/', 'NotebookLM', ['saas', 'ücretsiz', 'rag', 'araştırma'],
        'Yüklediğin PDF, doküman ve bağlantılarla sınırlı bir bağlam kuruyor; kaynak dışına çıkmayı reddediyor. '
        'Bu kısıt uydurma oranını düşürüyor, karşılığında genel bilgi soramıyorsun.',
        'Builds a context limited to the PDFs, docs and links you upload, and refuses to answer outside them. '
        'The constraint cuts hallucination; the price is that you cannot ask it general questions.', C)
    add('https://www.deepseek.com/', 'DeepSeek', ['açık-ağırlık', 'llm', 'akıl-yürütme'],
        'V3 ve R1 ağırlıkları indirilebilir durumda. Karışım-uzman (MoE) mimarisi sayesinde toplam parametre büyük ama '
        'her jetonda yalnızca bir kısmı etkin — akıl yürütme başarımını çok daha düşük çıkarım maliyetiyle veriyor.',
        'V3 and R1 weights are downloadable. A mixture-of-experts architecture keeps total parameters high while '
        'activating only a slice per token, which is how it delivers reasoning performance at far lower inference cost.', C)
    add('https://www.phind.com/', 'Phind', ['saas', 'freemium', 'arama', 'kod'],
        'Geliştirici sorularına doğrudan kod bloğu ve kaynak bağlantısıyla cevap veriyor. '
        'Stack Overflow gezmeye alternatif; alan dışı sorularda genel asistanların gerisinde kalıyor.',
        'Answers developer questions with a code block and source links rather than a page of results. '
        'A substitute for trawling Stack Overflow; it falls behind general assistants outside that domain.', C)
    add('https://openclaw.ai/', 'OpenClaw', ['açık-kaynak', 'self-hosted', 'asistan', 'agent'],
        'Kendi makinende çalışan kişisel asistan. Arayüzü yok — WhatsApp, Telegram gibi zaten kullandığın '
        'sohbet uygulamalarına bağlanıyor, veriler cihazından çıkmıyor.',
        'A personal assistant that runs on your own machine. It has no UI of its own; it hooks into chat apps '
        'you already use, and data never leaves the device.', C)
    add('https://kimi-claw.com/', 'Kimi Claw', ['saas', 'freemium', 'agent', 'bellek'],
        'OpenClaw üzerine kurulu barındırılmış sürüm: kalıcı bellek, zamanlanmış görevler ve sen istemeden '
        'tetiklenen işler ekliyor. Kendi sunucunu işletmek istemeyenler için.',
        'A hosted layer on OpenClaw adding persistent memory, scheduled tasks and jobs that fire without being asked. '
        'For people who do not want to operate their own server.', C)

    # --- API / platform
    add('https://platform.openai.com/', 'OpenAI Platform', ['api', 'ücretli', 'llm'],
        'API anahtarı, kullanım limitleri ve fatura yönetimi. Kuruluş bazlı kota ayarları ve '
        'model kullanım grafikleri de burada.',
        'API keys, rate limits and billing. Organisation-level quota settings and usage graphs live here too.', C)
    add('https://developers.openai.com/api/docs', 'OpenAI API Dokümantasyonu', ['dokümantasyon', 'api'],
        'Chat Completions, Responses ve Realtime uç noktalarının parametre referansı. '
        'Fonksiyon çağırma şeması ve akış (streaming) davranışı için birincil kaynak.',
        'Parameter reference for the Chat Completions, Responses and Realtime endpoints. '
        'The primary source for function-calling schemas and streaming behaviour.', C)
    add('https://www.anthropic.com/claude', 'Anthropic Claude', ['api', 'ücretli', 'llm'],
        'Model sürümleri, bağlam limitleri ve jeton fiyatları. Prompt caching ve batch API gibi '
        'maliyet düşüren özelliklerin karşılaştırması burada duruyor.',
        'Model versions, context limits and token pricing, with the cost-reducing features — prompt caching, '
        'the batch API — laid out side by side.', C)
    add('https://ai.google.dev/', 'Google AI for Developers', ['api', 'dokümantasyon', 'llm'],
        'Gemini API ve açık ağırlıklı Gemma ailesinin geliştirici kapısı. Ücretsiz kotası gerçek bir '
        'prototip taşıyacak kadar geniş, kredi kartı istemiyor.',
        'Developer gateway for the Gemini API and the open-weight Gemma family. The free tier is wide enough '
        'to carry a real prototype and asks for no card.', C)
    add('https://aistudio.google.com/', 'Google AI Studio', ['tarayıcı-içi', 'ücretsiz', 'api', 'test'],
        'İstem denemek, sistem talimatı ayarlamak ve sıcaklık gibi parametreleri kurcalamak için tarayıcı arayüzü. '
        'Denediğin çağrıyı doğrudan kod olarak dışa aktarıyor.',
        'A browser surface for testing prompts, setting system instructions and fiddling with temperature. '
        'It exports whatever call you just tried as ready code.', C)
    add('https://www.llama.com/', 'Meta Llama', ['açık-ağırlık', 'llm', 'yerel-model'],
        'Ağırlıklar indirilebilir ve kendi donanımında çalışır. Lisans tam OSI uyumlu değil — '
        'büyük ölçekli ticari kullanımda aylık aktif kullanıcı eşiği var, okumadan geçme.',
        'Weights are downloadable and run on your own hardware. The licence is not fully OSI-compliant: '
        'there is a monthly-active-user threshold for large commercial use — read it before shipping.', C)
    add('https://mistral.ai/', 'Mistral AI', ['açık-ağırlık', 'llm', 'freemium'],
        'Avrupa merkezli sağlayıcı. Küçük modelleri (7B ve altı) Apache-2.0 ile yayımlıyor; '
        'tek tüketici GPU’suna sığmaları sınırlı donanımda ayrı bir avantaj.',
        'Europe-based provider that ships its small models (7B and below) under Apache-2.0. '
        'They fit on a single consumer GPU, which matters when hardware is the constraint.', C)
    add('https://cohere.com/', 'Cohere', ['api', 'ücretli', 'rerank', 'embedding'],
        'Sohbet yarışına girmek yerine arama tarafına yerleşmiş: Rerank modeli, vektör aramanın döndürdüğü '
        'adayları yeniden sıralayarak RAG isabetini gözle görülür artırıyor.',
        'Rather than compete on chat, it sits on the retrieval side: its Rerank model reorders candidates '
        'returned by vector search and visibly lifts RAG precision.', C)

    # --- running locally
    add('https://ollama.com/', 'Ollama', ['açık-kaynak', 'cli', 'yerel-model', 'llama.cpp'],
        'llama.cpp üzerine kurulu, tek komutla model indirip çalıştıran araç. '
        'OpenAI uyumlu bir yerel API açıyor, yani mevcut istemci kodun değişmeden çalışıyor.',
        'Built on llama.cpp; one command pulls and runs a model. '
        'It exposes an OpenAI-compatible local endpoint, so existing client code runs unchanged.', C)
    add('https://lmstudio.ai/', 'LM Studio', ['masaüstü', 'ücretsiz', 'yerel-model', 'gguf'],
        'GGUF modelleri aramak, indirmek ve nicemleme seviyesi seçmek için masaüstü arayüz. '
        'Hangi nicemlemenin RAM’ine sığacağını önden gösteriyor — Ollama’da bunu kendin hesaplarsın.',
        'A desktop app for finding GGUF models, downloading them and picking a quantisation level. '
        'It tells you upfront which quant fits your RAM; with Ollama you work that out yourself.', C)
    add('https://openwebui.com/', 'Open WebUI', ['açık-kaynak', 'self-hosted', 'docker', 'web-ui'],
        'Ollama veya herhangi bir OpenAI uyumlu uç noktanın önüne geçen web arayüzü. '
        'Çok kullanıcı, rol yönetimi ve RAG için belge yükleme getiriyor; genelde Docker ile kuruluyor.',
        'A web front-end for Ollama or any OpenAI-compatible endpoint, adding multi-user accounts, '
        'role management and document upload for RAG. Usually deployed with Docker.', C)
    add('https://docs.vllm.ai/', 'vLLM', ['açık-kaynak', 'python', 'sunum', 'gpu'],
        'PagedAttention ile KV önbelleğini sayfalayarak GPU belleğini verimli kullanıyor; '
        'sürekli yığınlama (continuous batching) sayesinde eşzamanlı istek verimi Ollama’nın kat kat üstünde.',
        'PagedAttention pages the KV cache to use GPU memory efficiently, and continuous batching pushes '
        'concurrent-request throughput far past what Ollama manages.', C)

    # --- model archives
    add('https://huggingface.co/', 'Hugging Face', ['ücretsiz', 'model-arşivi', 'veri-kümesi', 'topluluk'],
        'Model, veri kümesi ve Spaces demolarının merkezî deposu. Her model kartında lisans, eğitim verisi '
        've değerlendirme sonuçları duruyor — indirmeden önce bakılacak yer orası.',
        'The central repository for models, datasets and Spaces demos. Each model card carries licence, '
        'training data and eval results — read that before you download.', C)
    add('https://huggingbay.xyz/', 'Hugging Bay', ['ücretsiz', 'model-arşivi', 'lisans'],
        'Açık modelleri lisans ve kaynak kaydıyla yan yana koyan alternatif tarayıcı. '
        'İndirilen dosyalar için SHA-256 özeti yayımlıyor, yani bütünlüğü doğrulayabiliyorsun.',
        'An alternative browser placing open models side by side with licence and provenance. '
        'It publishes SHA-256 hashes for downloads, so integrity is verifiable.', C)
    add('https://huggingface.co/baidu/Unlimited-OCR', 'Unlimited-OCR', ['açık-ağırlık', 'ocr', 'model'],
        'Baidu’nun OCR modeli; sayfa sınırı olmadan uzun ve çok sütunlu belgelerden metin çıkarıyor. '
        'Tablo ve düzen korumada klasik Tesseract hattından belirgin şekilde iyi.',
        'Baidu’s OCR model, extracting text from long multi-column documents with no page ceiling. '
        'Markedly better than a classic Tesseract pipeline at preserving tables and layout.', C)
    add('https://huggingface.co/moonshotai/Kimi-K2.7-Code', 'Kimi K2.7 Code', ['açık-ağırlık', 'kod', 'model'],
        'Moonshot AI’ın kod odaklı açık ağırlıklı modeli. Yerel kod asistanı kurmak isteyip '
        'kapalı API’ye bağlanmak istemeyenler için gerçek bir seçenek.',
        'Moonshot AI’s code-focused open-weight model — a genuine option if you want a local coding assistant '
        'without wiring yourself to a closed API.', C)
    add('https://huggingface.co/nvidia/LocateAnything-3B', 'LocateAnything-3B', ['açık-ağırlık', 'görü', 'model'],
        'Metinle tarif edilen nesneyi görüntüde sınırlayıcı kutuyla işaretleyen görsel konumlandırma modeli. '
        'Sınıflandırmadan farkı, önceden tanımlı etiket listesine bağlı olmaması.',
        'A visual grounding model that boxes an object in an image from a text description. '
        'Unlike classification it is not tied to a predefined label set.', C)
    add('https://canivibecodeit.com/', 'Can I Vibecode It?', ['ücretsiz', 'referans', 'değerlendirme'],
        'Bin küsur uygulamayı “yapay zeka bunu yeniden üretebilir mi” diye test edip sonucu yayımlayan tablo. '
        'Kullanılan istemi de veriyor, yani sonucu kendin doğrulayabiliyorsun.',
        'A table testing whether AI can rebuild a thousand-odd apps, with the verdict published. '
        'It hands you the exact prompt used, so the result is reproducible.', C)
