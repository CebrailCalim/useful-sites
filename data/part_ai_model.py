# -*- coding: utf-8 -*-
"""YZ · Modeller & Asistanlar"""

C = 'yz_model'


def load(add):
    # --- sohbet asistanları
    add('https://chatgpt.com/', 'ChatGPT', ['freemium', 'asistan'],
        'OpenAI’ın sohbet arayüzü. Görsel üretim, kod çalıştırma ve özel GPT’lerin aynı pencerede toplanması onu en geniş “her işi tek yerde” seçeneği yapıyor.',
        'OpenAI’s chat front-end. Image generation, code execution and custom GPTs in one window make it the broadest do-everything-in-one-place option.', C)
    add('https://claude.ai/new', 'Claude', ['freemium', 'asistan'],
        'Anthropic’in asistanı. Uzun belge okuma ve kod düzenlemede güçlü; Projects ile bağlam dosyaları sohbetler arasında kalıcı kalır.',
        'Anthropic’s assistant. Strong at long-document reading and code editing; Projects keeps context files persistent across chats.', C)
    add('https://gemini.google.com/', 'Google Gemini', ['freemium', 'asistan'],
        'Google’ın asistanı. Arama, Drive ve YouTube bağlantısı sayesinde zaten Google hesabındaki içerikle çalışırken avantajlı.',
        'Google’s assistant. Its hooks into Search, Drive and YouTube give it the edge when working with content already in your Google account.', C)
    add('https://www.perplexity.ai/', 'Perplexity', ['freemium', 'arama'],
        'Kaynak gösteren yapay zeka arama motoru. Sohbet botlarından farkı, her iddianın altına atıf koyup doğrulamayı mümkün kılması.',
        'An AI answer engine that cites. Unlike chatbots it puts a source under each claim, so the answer is actually checkable.', C)
    add('https://www.deepseek.com/', 'DeepSeek', ['ücretsiz', 'açık ağırlık', 'model'],
        'Çin merkezli açık ağırlıklı model ailesi. Akıl yürütme başarımını çok daha düşük eğitim ve kullanım maliyetiyle sunmasıyla dikkat çekti.',
        'Chinese open-weight model family that drew attention by matching reasoning performance at a fraction of the training and inference cost.', C)
    add('https://notebooklm.google.com/', 'NotebookLM', ['ücretsiz', 'araştırma'],
        'Yalnızca senin yüklediğin belgelerden cevap veren not defteri. Kaynak dışına çıkmadığı için genel botlara göre uydurma riski belirgin şekilde düşük.',
        'A notebook that answers only from the documents you upload. Because it will not step outside your sources, hallucination risk drops sharply.', C)
    add('https://www.phind.com/', 'Phind', ['freemium', 'geliştirici', 'arama'],
        'Geliştiriciye göre ayarlanmış arama asistanı. Genel arama motorlarından farkı, cevabı doğrudan kod parçası ve kaynak bağlantısıyla vermesi.',
        'A search assistant tuned for developers, answering with code snippets and source links rather than a page of results.', C)
    add('https://openclaw.ai/', 'OpenClaw', ['açık kaynak', 'asistan', 'kendi sunucunda'],
        'Kendi makinende çalışan açık kaynak kişisel asistan; bulut asistanlarından farkı, hâlihazırda kullandığın sohbet uygulamaları üzerinden çalışması.',
        'Open-source personal assistant that runs on your own machine and works through the chat apps you already use, unlike cloud assistants.', C)
    add('https://kimi-claw.com/', 'Kimi Claw', ['freemium', 'asistan', 'bellek'],
        'OpenClaw üzerine kurulu, uzun vadeli belleği ve zamanlanmış görevleri olan sürekli çalışan asistan.',
        'An always-on assistant built on OpenClaw, with long-term memory and scheduled, proactive tasks.', C)

    # --- sağlayıcı / API
    add('https://platform.openai.com/', 'OpenAI Platform', ['ücretli', 'api'],
        'GPT modellerinin API konsolu; anahtar, kota ve fiyat yönetimi burada yapılır.',
        'API console for GPT models — keys, quota and billing live here.', C)
    add('https://developers.openai.com/api/docs', 'OpenAI API Dokümantasyonu', ['dokümantasyon', 'api'],
        'OpenAI API’sinin resmî referansı ve rehberleri; uç noktalar ve parametreler için birincil kaynak.',
        'Official OpenAI API reference and guides — the primary source for endpoints and parameters.', C)
    add('https://www.anthropic.com/claude', 'Anthropic Claude', ['ücretli', 'api'],
        'Claude model ailesinin giriş sayfası; sürümler, bağlam limitleri ve fiyatlandırma buradan takip edilir.',
        'Entry point for the Claude model family — versions, context limits and pricing.', C)
    add('https://ai.google.dev/', 'Google AI for Developers', ['dokümantasyon', 'api', 'google'],
        'Gemini API ve açık Gemma modellerinin geliştirici kapısı; ücretsiz kotayla başlamak için en kısa yol.',
        'Developer gateway for the Gemini API and open Gemma models, with a free tier to start on.', C)
    add('https://aistudio.google.com/', 'Google AI Studio', ['ücretsiz', 'api', 'oyun alanı'],
        'Gemini modellerini tarayıcıda deneyip API anahtarı almak için oyun alanı. Cömert ücretsiz kotası prototip için elverişli kılıyor.',
        'Browser playground for trying Gemini models and getting API keys; its generous free tier suits prototyping.', C)
    add('https://www.llama.com/', 'Meta Llama', ['açık ağırlık', 'model'],
        'Meta’nın açık ağırlıklı model ailesi. Kapalı API’lerden farkı, ağırlıkları indirip kendi donanımında çalıştırabilmen.',
        'Meta’s open-weight model family. Unlike closed APIs you can download the weights and run them yourself.', C)
    add('https://mistral.ai/', 'Mistral AI', ['freemium', 'model'],
        'Avrupa merkezli model sağlayıcı. Küçük ve hızlı açık modelleriyle sınırlı donanımda çalıştırma senaryolarında öne çıkıyor.',
        'European model provider whose small, fast open models stand out when hardware is limited.', C)
    add('https://cohere.com/', 'Cohere', ['ücretli', 'api'],
        'Kurumsal odaklı sağlayıcı; RAG hatlarında özellikle arama ve yeniden sıralama (rerank) modelleriyle tercih ediliyor.',
        'Enterprise-oriented provider; its retrieval and rerank models are why it shows up in RAG pipelines.', C)

    # --- yerel çalıştırma
    add('https://ollama.com/', 'Ollama', ['ücretsiz', 'açık kaynak', 'yerel', 'cli'],
        'Yerel model çalıştırıcı. Tek komutla model indirip çalıştırır; LM Studio’dan farkı arayüz yerine terminal ve API odaklı olması.',
        'Local model runner — one command pulls and runs a model. Unlike LM Studio it is terminal- and API-first.', C)
    add('https://lmstudio.ai/', 'LM Studio', ['ücretsiz', 'yerel', 'masaüstü'],
        'Yerel model çalıştırmak için masaüstü uygulaması. Ollama’dan farkı, model arama ve sohbetin hazır grafik arayüzle gelmesi.',
        'Desktop app for running models locally; unlike Ollama, model discovery and chat ship as a ready-made GUI.', C)
    add('https://openwebui.com/', 'Open WebUI', ['açık kaynak', 'kendi sunucunda'],
        'Yerel modellere ChatGPT benzeri web arayüzü. Genelde Ollama üstüne kurulur; çok kullanıcı ve sohbet geçmişi ekler.',
        'A ChatGPT-like web UI for local models, usually layered on Ollama, adding multi-user support and chat history.', C)
    add('https://docs.vllm.ai/', 'vLLM', ['açık kaynak', 'sunum'],
        'Yüksek verimli LLM sunum motoru. Kişisel kullanım için değil; çok isteği paralel karşılayan üretim servisleri için.',
        'High-throughput LLM serving engine — not for personal use, but for production endpoints handling many concurrent requests.', C)

    # --- model arşivi
    add('https://huggingface.co/', 'Hugging Face', ['ücretsiz', 'model', 'topluluk'],
        'Açık model, veri kümesi ve demo deposu. Tek sağlayıcıya bağlı olmayan, alan bağımsız en büyük model arşivi.',
        'Repository of open models, datasets and demos — the largest vendor-neutral model archive there is.', C)
    add('https://huggingbay.xyz/', 'Hugging Bay', ['ücretsiz', 'model', 'dizin'],
        'Açık modelleri lisans ve kaynak kaydıyla birlikte karşılaştırmak için alternatif arayüz; indirilen dosyaların SHA-256 özetini yayımlaması ayırt edici yanı.',
        'Alternative browser for open models with licence and provenance side by side; publishing SHA-256 hashes for downloads is what sets it apart.', C)
    add('https://huggingface.co/baidu/Unlimited-OCR', 'Unlimited-OCR (Baidu)', ['açık ağırlık', 'model', 'ocr'],
        'Baidu’nun açık OCR modeli; uzun ve karmaşık düzenli belgelerde sayfa sınırı olmadan metin çıkarmaya odaklı.',
        'Baidu’s open OCR model, aimed at extracting text from long, complex-layout documents without page limits.', C)
    add('https://huggingface.co/moonshotai/Kimi-K2.7-Code', 'Kimi K2.7 Code', ['açık ağırlık', 'model', 'kod'],
        'Moonshot AI’ın kod odaklı açık ağırlıklı modeli; yerel kod asistanı kurmak isteyenler için kapalı API’lere alternatif.',
        'Moonshot AI’s code-focused open-weight model — an alternative to closed APIs if you want a local coding assistant.', C)
    add('https://huggingface.co/nvidia/LocateAnything-3B', 'LocateAnything-3B', ['açık ağırlık', 'model', 'görü'],
        'NVIDIA’nın görsel konumlandırma modeli; metinle tarif edilen nesneyi görüntüde işaretlemeye odaklı.',
        'NVIDIA’s visual grounding model, focused on locating an object in an image from a text description.', C)
    add('https://canivibecodeit.com/', 'Can I Vibecode It?', ['ücretsiz', 'referans'],
        'Yapay zekanın hangi uygulamaları yeniden üretebildiğini test edip puanlayan liste. Pazarlama vaadi yerine denenmiş sonuç sunması ayırt edici yanı.',
        'A scoreboard testing which apps AI can actually rebuild. Publishing tested verdicts rather than marketing claims is what distinguishes it.', C)
