# -*- coding: utf-8 -*-
"""YZ · Agent, RAG & Altyapı"""

C = 'yz_altyapi'


def load(add):
    # ---------------------------------------------------------- çatılar
    add('https://www.langchain.com/', 'LangChain', ['açık kaynak', 'çatı', 'python'],
        'LLM uygulamaları için en yaygın çatı. Geniş entegrasyon kütüphanesi başlıca avantajı; kalın soyutlama katmanı ise en sık eleştirilen yanı.',
        'The most widely used framework for LLM apps. Its huge integration library is the upside; its thick abstraction layer is the most common complaint.', C)
    add('https://docs.langchain.com/oss/python/langchain/overview', 'LangChain Dokümantasyonu', ['dokümantasyon', 'çatı'],
        'LangChain’in güncel resmî dokümanı; sadeleştirilmiş `create_agent` yaklaşımı burada anlatılıyor.',
        'LangChain’s current official docs, covering the simplified `create_agent` approach.', C)
    add('https://www.langchain.com/langgraph', 'LangGraph', ['açık kaynak', 'agent'],
        'Agent akışını durum grafiği olarak kuran LangChain katmanı. Düz zincirlerden farkı döngü, dallanma ve insan onayı adımlarını taşıyabilmesi.',
        'LangChain layer modelling agent flow as a state graph. Unlike plain chains it supports loops, branching and human-approval steps.', C)
    add('https://python.langchain.com/docs/tutorials/agents/', 'LangChain Agents (öğretici)', ['dokümantasyon', 'agent'],
        'İlk agent’ı kurmayı anlatan resmî öğretici; çatının araç çağırma modelini kavramak için en kısa yol.',
        'Official tutorial for building your first agent — the shortest path to understanding the tool-calling model.', C)
    add('https://www.llamaindex.ai/', 'LlamaIndex', ['açık kaynak', 'rag'],
        'Belge alma (retrieval) odaklı çatı. LangChain genel amaçlıyken bu, indeksleme ve sorgu hattını ince ayarlamak için tasarlanmış.',
        'Retrieval-first framework. Where LangChain is general-purpose, this is built for tuning the indexing and query pipeline.', C)
    add('https://docs.llamaindex.ai/en/stable/module_guides/workflow/', 'LlamaIndex Workflows', ['dokümantasyon', 'agent'],
        'LlamaIndex’in olay güdümlü agent akış motoru; graf yerine olay/adım modeli kullandığı için asenkron işlerde okuması kolay.',
        'LlamaIndex’s event-driven agent runtime; using events/steps instead of a graph reads more naturally for async work.', C)
    add('https://www.crewai.com/', 'CrewAI', ['açık kaynak', 'agent', 'python'],
        'Rol tabanlı çoklu agent çatısı. Çekirdek fikri, agent’lara “araştırmacı, yazar” gibi roller verip iş bölümü kurmak.',
        'Role-based multi-agent framework whose core idea is assigning roles like “researcher, writer” and letting them divide the work.', C)
    add('https://microsoft.github.io/autogen/', 'Microsoft AutoGen', ['açık kaynak', 'agent', 'araştırma'],
        'Agent’ların birbiriyle konuşarak iş çözdüğü Microsoft çatısı; araştırma kökenli olduğu için deneysel desenlere daha açık.',
        'Microsoft framework where agents solve tasks by conversing with each other; research-rooted, so more open to experimental patterns.', C)
    add('https://learn.microsoft.com/en-us/agent-framework/', 'Microsoft Agent Framework', ['dokümantasyon', 'agent'],
        'AutoGen ve Semantic Kernel’in birleştirildiği üretim odaklı Microsoft agent çatısı; Azure ile sıkı entegre.',
        'Microsoft’s production-oriented agent framework merging AutoGen and Semantic Kernel, tightly integrated with Azure.', C)
    add('https://strandsagents.com/', 'AWS Strands Agents', ['açık kaynak', 'agent', 'aws'],
        'AWS’in model güdümlü agent SDK’sı. Akışı elle kurmak yerine modele araç listesi verip planı ona bırakma yaklaşımını benimser.',
        'AWS’s model-driven agent SDK: instead of hand-wiring flow you hand the model a tool list and let it plan.', C)
    add('https://www.camel-ai.org/', 'CAMEL-AI', ['açık kaynak', 'agent', 'araştırma'],
        'Çok agent’lı toplum simülasyonuna odaklı araştırma çatısı; ürün geliştirmekten çok agent davranışı incelemek için elverişli.',
        'Research framework for multi-agent society simulation — better for studying agent behaviour than shipping products.', C)
    add('https://www.agno.com/', 'Agno', ['açık kaynak', 'agent', 'python'],
        'Hafif ve hızlı agent kütüphanesi. LangChain’e göre çok daha ince bir katman sunar; bellek ve araç desteği çekirdeğe gömülüdür.',
        'Lightweight, fast agent library — a far thinner layer than LangChain, with memory and tools built into the core.', C)
    add('https://openai.github.io/openai-agents-python/', 'OpenAI Agents SDK', ['açık kaynak', 'agent', 'python'],
        'OpenAI’ın resmî agent kütüphanesi. Kasten sade: agent, araç, devretme ve koruma bandı dışında kavram yok.',
        'OpenAI’s official agent library — deliberately minimal: agents, tools, handoffs and guardrails, and little else.', C)
    add('https://ai.pydantic.dev/', 'Pydantic AI', ['açık kaynak', 'agent', 'python'],
        'Tip güvenli agent çatısı. Farkı, model çıktısını Pydantic şemasıyla doğrulaması; serbest metin yerine yapısal veri garantisi verir.',
        'Type-safe agent framework whose distinction is validating model output against a Pydantic schema — structured data, not free text.', C)
    add('https://learn.microsoft.com/semantic-kernel/', 'Semantic Kernel', ['dokümantasyon', 'agent', 'dotnet'],
        'Microsoft’un .NET/Python agent SDK’sı; kurumsal .NET yığınında çalışanlar için Python ağırlıklı alternatiflerden daha uygun.',
        'Microsoft’s .NET/Python agent SDK — a better fit than Python-centric alternatives inside an enterprise .NET stack.', C)
    add('https://adk.dev/', 'Agent Development Kit (ADK)', ['açık kaynak', 'agent', 'google'],
        'Google’ın agent geliştirme kiti; değerlendirme ve dağıtım araçlarının kutudan çıkması onu ayırıyor.',
        'Google’s agent development kit; built-in evaluation and deployment tooling is what sets it apart.', C)
    add('https://aws.amazon.com/bedrock/agents/', 'AWS Bedrock Agents', ['ücretli', 'agent', 'aws'],
        'AWS’in yönetilen agent servisi; kendi çatını işletmek yerine altyapıyı AWS’e bırakmak isteyenler için.',
        'AWS’s managed agent service — for teams who would rather hand the infrastructure to AWS than run their own framework.', C)
    add('https://learn.microsoft.com/azure/ai-foundry/', 'Azure AI Foundry', ['ücretli', 'agent', 'azure'],
        'Azure’un uçtan uca YZ uygulama platformu: model kataloğu, agent servisi ve değerlendirme tek çatı altında.',
        'Azure’s end-to-end AI application platform: model catalogue, agent service and evaluation under one roof.', C)

    # ---------------------------------------------------------- RAG
    add('https://haystack.deepset.ai/', 'Haystack', ['açık kaynak', 'rag', 'python'],
        'Boru hattı merkezli RAG çatısı. Bileşenleri açıkça bağladığın için akışın nerede ne yaptığı LangChain’e göre daha görünür.',
        'Pipeline-centric RAG framework; because you wire components explicitly, the flow is more visible than in LangChain.', C)
    add('https://dspy.ai/', 'DSPy', ['açık kaynak', 'rag', 'araştırma'],
        'İstem yazmak yerine istemleri programlayıp optimize eden çatı; elle prompt ayarlamayı bir derleyiciye devretme fikri üzerine kurulu.',
        'Framework that programs and optimises prompts instead of writing them — built on handing prompt-tuning to a compiler.', C)
    add('https://ragflow.io/', 'RAGFlow', ['açık kaynak', 'rag', 'kendi sunucunda'],
        'Derin belge anlama odaklı, kendi sunucunda çalışan RAG motoru; karmaşık PDF ve tablo ayrıştırmada kütüphane çözümlerinden güçlü.',
        'Self-hosted RAG engine focused on deep document understanding — stronger than library-only solutions on messy PDFs and tables.', C)
    add('https://microsoft.github.io/graphrag/', 'GraphRAG', ['açık kaynak', 'rag', 'araştırma'],
        'Belgelerden bilgi grafiği çıkarıp öyle sorgulayan yaklaşım. Klasik parça-getir yönteminin cevaplayamadığı “bütüne dair” sorular için.',
        'Extracts a knowledge graph from documents and queries that — aimed at whole-corpus questions plain chunk retrieval cannot answer.', C)
    add('https://unstructured.io/', 'Unstructured', ['açık kaynak', 'rag', 'ayrıştırma'],
        'PDF, Word ve e-posta gibi düzensiz belgeleri LLM’e verilebilir parçalara çeviren kütüphane; RAG hattının en sık kırılan ilk adımını üstlenir.',
        'Library turning messy PDFs, Word files and email into LLM-ready chunks — it owns the first and most fragile step of a RAG pipeline.', C)
    add('https://github.com/Graphify-Labs/graphify', 'Graphify', ['açık kaynak', 'github', 'rag', 'kod'],
        'Kod tabanını dokümanları, şemaları ve PDF’leriyle birlikte sorgulanabilir bilgi grafiğine çeviren araç; kod asistanlarına bağlam vermek için.',
        'Turns a codebase — with its docs, schemas and PDFs — into a queryable knowledge graph to feed context to coding agents.', C)
    add('https://github.com/headroomlabs-ai/headroom', 'Headroom', ['açık kaynak', 'github', 'optimizasyon'],
        'Araç çıktısı ve RAG parçalarını modele ulaşmadan sıkıştıran katman; aynı cevabı belirgin şekilde daha az jetonla almayı hedefler.',
        'Layer that compresses tool output and RAG chunks before they reach the model, aiming for the same answers at markedly fewer tokens.', C)

    # ---------------------------------------------------------- embedding
    add('https://platform.openai.com/docs/guides/embeddings', 'OpenAI Embeddings', ['dokümantasyon', 'embedding'],
        'OpenAI gömme modellerinin resmî kılavuzu; boyut, fiyat ve kullanım örnekleri.',
        'Official guide to OpenAI embedding models — dimensions, pricing and usage examples.', C)
    add('https://cohere.com/embed', 'Cohere Embed', ['ücretli', 'embedding'],
        'Çok dilli gömme modeli; 100+ dili tek uzayda temsil etmesi Türkçe dahil diller arası aramada avantaj sağlıyor.',
        'Multilingual embedding model; representing 100+ languages in one space is its edge for cross-language search.', C)
    add('https://www.voyageai.com/', 'Voyage AI', ['ücretli', 'embedding'],
        'Alan odaklı gömme modelleri (hukuk, kod, finans); genel amaçlı modellere göre dar alanlarda daha isabetli sonuç hedefler.',
        'Domain-specific embedding models (legal, code, finance) aiming to beat general-purpose ones inside narrow domains.', C)
    add('https://sbert.net/', 'Sentence Transformers', ['açık kaynak', 'embedding', 'python'],
        'Yerel gömme üretmenin standart kütüphanesi; API’ye para vermeden ve veriyi dışarı çıkarmadan çalışır.',
        'The standard library for producing embeddings locally — no API bill and no data leaving your machine.', C)
    add('https://huggingface.co/BAAI', 'BGE Modelleri (BAAI)', ['açık kaynak', 'embedding', 'model'],
        'Açık gömme modellerinin en çok kullanılan ailesi; ücretli API’lere yakın başarımı ücretsiz sunduğu için yaygın.',
        'The most used family of open embedding models — close to paid-API quality at no cost.', C)
    add('https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings', 'Vertex AI Embeddings', ['dokümantasyon', 'embedding', 'google'],
        'Google Cloud tarafındaki gömme servisi; GCP içinde kalan veri hatları için doğal seçim.',
        'Google Cloud’s embedding service — the natural pick for pipelines that stay inside GCP.', C)
    add('https://learn.microsoft.com/azure/ai-services/openai/', 'Azure OpenAI Service', ['dokümantasyon', 'api', 'azure'],
        'OpenAI modellerinin Azure üzerinden, kurumsal uyumluluk ve bölge denetimiyle sunulan hâli.',
        'OpenAI models delivered through Azure with enterprise compliance and region control.', C)

    # ---------------------------------------------------------- MCP
    add('https://modelcontextprotocol.io/', 'Model Context Protocol', ['açık kaynak', 'mcp', 'standart'],
        'Modelleri dış araç ve veriye bağlamak için açık protokol; her uygulamaya ayrı eklenti yazma sorununu tek standartla çözmeyi hedefler.',
        'Open protocol connecting models to external tools and data, aiming to replace per-app plugin work with one standard.', C)
    add('https://gofastmcp.com/', 'FastMCP', ['açık kaynak', 'mcp', 'python'],
        'Python’da MCP sunucusu yazmanın kısa yolu; ham SDK’ya göre çok daha az kalıp kod ister.',
        'The quick way to write an MCP server in Python — far less boilerplate than the raw SDK.', C)
    add('https://registry.modelcontextprotocol.io/', 'MCP Registry', ['ücretsiz', 'mcp', 'dizin'],
        'Resmî MCP sunucu dizini; dağınık GitHub listelerinden farkı merkezî ve makine tarafından okunabilir olması.',
        'The official MCP server registry — central and machine-readable, unlike scattered GitHub lists.', C)
    add('https://github.com/github/github-mcp-server', 'GitHub MCP Server', ['açık kaynak', 'mcp', 'github'],
        'GitHub’ın resmî MCP sunucusu; depo, konu ve PR işlemlerini asistana araç olarak açar.',
        'GitHub’s official MCP server, exposing repo, issue and PR operations as assistant tools.', C)
    add('https://github.com/modelcontextprotocol/servers', 'MCP Sunucu Koleksiyonu', ['açık kaynak', 'mcp', 'github', 'koleksiyon'],
        'Referans MCP sunucuları (dosya sistemi, PostgreSQL, Slack, Drive); kendi sunucunu yazmadan önce bakılacak ilk yer.',
        'Reference MCP servers (filesystem, PostgreSQL, Slack, Drive) — the first place to look before writing your own.', C)
    add('https://mcpmarket.com/tools/skills', 'MCP Market · Agent Skills', ['ücretsiz', 'mcp', 'dizin'],
        'Topluluk agent yetenek ve MCP sunucu pazarı; resmî kayıt defterine göre daha geniş ama daha az denetimli.',
        'Community marketplace of agent skills and MCP servers — broader than the official registry but less vetted.', C)
    add('https://composio.dev/', 'Composio', ['freemium', 'agent', 'entegrasyon'],
        'Agent’lara hazır araç ve yetkilendirme sağlayan katman; her SaaS için ayrı OAuth akışı yazma yükünü ortadan kaldırır.',
        'Layer giving agents ready-made tools and delegated auth, removing the need to write an OAuth flow per SaaS.', C)

    # ---------------------------------------------------------- güvenlik
    add('https://github.com/NVIDIA/NeMo-Guardrails', 'NeMo Guardrails', ['açık kaynak', 'güvenlik', 'github'],
        'LLM konuşmasına kurallı korkuluk ekleyen NVIDIA araç seti; konu sapması ve yasak istekleri diyalog akışı düzeyinde engeller.',
        'NVIDIA toolkit adding rule-based rails to LLM conversations, blocking topic drift and disallowed requests at the dialogue level.', C)
    add('https://www.guardrailsai.com/', 'Guardrails AI', ['açık kaynak', 'güvenlik', 'python'],
        'Model çıktısını şema ve kurallara göre doğrulayan kütüphane. NeMo diyaloğu denetler, bu ise çıktının biçim ve içeriğini.',
        'Library validating model output against schemas and rules. NeMo guards the dialogue; this guards the output’s shape and content.', C)
    add('https://microsoft.github.io/presidio/', 'Microsoft Presidio', ['açık kaynak', 'gizlilik'],
        'Metin ve görselden kişisel veri tespit edip maskeleyen araç; modele veri göndermeden önceki anonimleştirme adımı için.',
        'Detects and redacts personal data in text and images — the anonymisation step before data reaches a model.', C)
    add('https://www.lakera.ai/', 'Lakera Guard', ['ücretli', 'güvenlik'],
        'İstem enjeksiyonu ve jailbreak tespitine odaklı ticari koruma katmanı; saldırı örüntülerini sürekli güncellenen veriyle yakalar.',
        'Commercial protection layer for prompt injection and jailbreak detection, backed by continuously updated attack data.', C)
    add('https://www.prompt.security/', 'Prompt Security', ['ücretli', 'güvenlik'],
        'Kurumda çalışanların YZ kullanımını denetleyen katman; sızan veriyi ve gölge YZ kullanımını görünür kılar.',
        'Layer governing employee AI use inside an organisation, surfacing data leakage and shadow AI.', C)
    add('https://protectai.com/', 'Protect AI', ['ücretli', 'güvenlik', 'mlops'],
        'Model tedarik zinciri güvenliği; model dosyalarını ve ML hattını zararlı yük için tarar.',
        'ML supply-chain security — scans model files and pipelines for malicious payloads.', C)
    add('https://azure.microsoft.com/products/ai-services/ai-content-safety', 'Azure AI Content Safety', ['ücretli', 'güvenlik', 'azure'],
        'Metin ve görselde zararlı içerik sınıflandıran Azure servisi; kendi sınıflandırıcını eğitmeye alternatif.',
        'Azure service classifying harmful content in text and images — an alternative to training your own classifier.', C)
    add('https://aws.amazon.com/bedrock/guardrails/', 'AWS Bedrock Guardrails', ['ücretli', 'güvenlik', 'aws'],
        'Bedrock üzerindeki modellere içerik ve konu filtresi ekleyen yönetilen katman.',
        'Managed content and topic filtering for models running on Bedrock.', C)

    # ---------------------------------------------------------- gözlemlenebilirlik
    add('https://smith.langchain.com/', 'LangSmith', ['freemium', 'gözlem'],
        'LangChain ekibinin izleme ve değerlendirme aracı; zincirin her adımını ayrı ayrı görmek için tasarlanmış.',
        'Tracing and evaluation from the LangChain team, designed to show each step of a chain separately.', C)
    add('https://langfuse.com/', 'Langfuse', ['açık kaynak', 'gözlem', 'kendi sunucunda'],
        'Açık kaynak LLM gözlemlenebilirliği; LangSmith’ten farkı kendi sunucunda çalıştırılabilmesi ve çatı bağımsız olması.',
        'Open-source LLM observability. Unlike LangSmith it can be self-hosted and is framework-agnostic.', C)
    add('https://phoenix.arize.com/', 'Arize Phoenix', ['açık kaynak', 'gözlem'],
        'Yerelde çalışan izleme ve değerlendirme aracı; not defteri içinde hızlı hata ayıklama için elverişli.',
        'Locally running tracing and evaluation tool, handy for quick debugging inside a notebook.', C)
    add('https://wandb.ai/site/weave/', 'W&B Weave', ['freemium', 'gözlem', 'mlops'],
        'Weights & Biases’ın LLM izleme ürünü; zaten W&B ile model eğitiyorsan izleri deney kayıtlarıyla aynı yerde tutar.',
        'Weights & Biases’ LLM tracing product, keeping traces alongside existing experiment tracking.', C)
    add('https://www.trulens.org/', 'TruLens', ['açık kaynak', 'değerlendirme'],
        'RAG çıktılarını sadakat ve alaka ölçütleriyle puanlayan kütüphane; “doğru mu” sorusunu ölçülebilir hâle getirir.',
        'Library scoring RAG output on groundedness and relevance, turning “is it right?” into a number.', C)
    add('https://docs.ragas.io/', 'Ragas', ['açık kaynak', 'değerlendirme', 'rag'],
        'RAG hattı için standart değerlendirme ölçütleri kütüphanesi; göz kararı test etmeye karşı sayısal alternatif.',
        'Standard evaluation metrics for RAG pipelines — the numeric alternative to eyeballing outputs.', C)
    add('https://www.promptfoo.dev/', 'Promptfoo', ['açık kaynak', 'değerlendirme', 'cli'],
        'İstemleri ve modelleri yan yana test eden CLI aracı; sürüm değişince çıktının bozulup bozulmadığını CI’da yakalar.',
        'CLI tool for side-by-side prompt and model testing; catches output regressions in CI when a version changes.', C)
    add('https://www.helicone.ai/', 'Helicone', ['açık kaynak', 'gözlem'],
        'Tek satır vekil değişikliğiyle LLM isteklerini kaydeden gözlem katmanı; kod değişikliği gerektirmemesi ayırt edici yanı.',
        'Observability via a one-line proxy change — requiring no code changes is what distinguishes it.', C)

    # ---------------------------------------------------------- bellek
    add('https://mem0.ai/', 'Mem0', ['freemium', 'bellek'],
        'Agent ve asistanlar için yönetilen kullanıcı belleği; kişiye özel bağlamı oturumlar arasında taşır.',
        'Managed user memory for agents and assistants, carrying personal context across sessions.', C)
    add('https://github.com/mem0ai/mem0', 'Mem0 (kaynak kod)', ['açık kaynak', 'bellek', 'github'],
        'Mem0’ın açık kaynak deposu; neyin hatırlanmaya değer olduğuna karar veren katmanı kendi altyapında çalıştırmak için.',
        'Mem0’s open-source repository — run the layer that decides what is worth remembering on your own infrastructure.', C)
    add('https://www.getzep.com/', 'Zep', ['açık kaynak', 'bellek'],
        'Zamana duyarlı bilgi grafiği tabanlı bellek; basit vektör belleğinden farkı, gerçeklerin ne zaman değiştiğini takip etmesi.',
        'Memory built on a temporal knowledge graph; unlike plain vector memory it tracks when facts changed.', C)
    add('https://www.letta.com/', 'Letta', ['açık kaynak', 'bellek', 'agent'],
        'MemGPT araştırmasından doğan, kendi belleğini yöneten agent altyapısı; bağlam penceresini işletim sistemi gibi sayfalar.',
        'Agent runtime born from the MemGPT research, paging its context window like an operating system.', C)
    add('https://langchain-ai.github.io/langgraph/concepts/memory/', 'LangGraph Memory', ['dokümantasyon', 'bellek'],
        'LangGraph’ta kısa ve uzun vadeli bellek desenlerini anlatan resmî kavram sayfası.',
        'Official concept page on short- and long-term memory patterns in LangGraph.', C)
    add('https://github.com/breferrari/obsidian-mind', 'Obsidian Mind', ['açık kaynak', 'github', 'bellek'],
        'Kod asistanlarına kalıcı bellek veren, kendini düzenleyen Obsidian kasası; bellek servisine bağlanmak yerine düz dosyalarda tutar.',
        'A self-organising Obsidian vault giving coding agents persistent memory — plain files instead of a memory service.', C)

    # ---------------------------------------------------------- vektör & veri deposu
    add('https://www.pinecone.io/', 'Pinecone', ['ücretli', 'vektör'],
        'Tam yönetilen vektör veritabanı; kendi kurulumunu yapmak istemeyenler için en az bakım gerektiren seçenek.',
        'Fully managed vector database — the lowest-maintenance option if you do not want to run your own.', C)
    add('https://weaviate.io/', 'Weaviate', ['açık kaynak', 'vektör'],
        'Açık kaynak vektör veritabanı; gömme üretimini kendi modülleriyle yapabilmesi hat kurulumundaki adımları azaltır.',
        'Open-source vector database that can generate embeddings itself via modules, cutting pipeline steps.', C)
    add('https://qdrant.tech/', 'Qdrant', ['açık kaynak', 'vektör', 'rust'],
        'Rust ile yazılmış vektör veritabanı; zengin filtreleme ve düşük kaynak tüketimiyle küçük sunucularda öne çıkar.',
        'Vector database written in Rust; rich filtering and low resource use make it strong on small servers.', C)
    add('https://milvus.io/', 'Milvus', ['açık kaynak', 'vektör', 'ölçek'],
        'Milyar ölçekli vektör aramaya odaklı dağıtık veritabanı; küçük projeler için fazla ağır kalır.',
        'Distributed database aimed at billion-scale vector search — overkill for small projects.', C)
    add('https://www.trychroma.com/', 'Chroma', ['açık kaynak', 'vektör', 'python'],
        'Gömülü çalışan, kurulumu neredeyse sıfır vektör veritabanı; prototip ve yerel geliştirmede en hızlı başlangıç.',
        'Embedded vector database with near-zero setup — the fastest start for prototypes and local development.', C)
    add('https://github.com/pgvector/pgvector', 'pgvector', ['açık kaynak', 'vektör', 'github'],
        'PostgreSQL’e vektör araması ekleyen eklenti; yeni bir sistem işletmek yerine mevcut veritabanında kalmak isteyenler için.',
        'Extension adding vector search to PostgreSQL — for teams who would rather stay in their existing database.', C)
    add('https://www.elastic.co/elasticsearch', 'Elasticsearch', ['freemium', 'arama'],
        'Metin arama motoru; artık vektör aramayı da destekliyor, anahtar kelime ve anlamsal aramayı birlikte isteyenler için uygun.',
        'Text search engine that now also does vector search — a fit when you want keyword and semantic retrieval together.', C)
    add('https://www.mongodb.com/products/platform/atlas-vector-search', 'Atlas Vector Search', ['ücretli', 'vektör'],
        'MongoDB belgelerinin yanında vektör araması; veri zaten Mongo’daysa ayrı senkronizasyon derdini ortadan kaldırır.',
        'Vector search next to your MongoDB documents, removing a sync step if the data already lives there.', C)
    add('https://redis.io/', 'Redis', ['açık kaynak', 'veritabanı', 'önbellek'],
        'Bellek içi veri deposu; YZ tarafında oturum durumu, önbellek ve hızlı vektör araması için kullanılıyor.',
        'In-memory data store used on the AI side for session state, caching and fast vector search.', C)
    add('https://www.postgresql.org/', 'PostgreSQL', ['açık kaynak', 'veritabanı'],
        'Kurumsal düzeyde açık kaynak ilişkisel veritabanı; pgvector eklentisiyle ayrı bir vektör veritabanına gerek bırakmayabilir.',
        'Enterprise-grade open-source relational database; with pgvector it can remove the need for a separate vector DB.', C)
    add('https://neo4j.com/', 'Neo4j', ['freemium', 'veritabanı', 'graf'],
        'Graf veritabanı; ilişkilerin kendisi veri olduğunda (bilgi grafiği, GraphRAG) tablodan çok daha doğal bir model sunar.',
        'Graph database — when relationships themselves are the data, it models the problem far more naturally than tables.', C)

    # ---------------------------------------------------------- otomasyon
    add('https://n8n.io/', 'n8n', ['açık kaynak', 'otomasyon', 'kendi sunucunda'],
        'Kendi sunucunda çalıştırılabilen görsel iş akışı otomasyonu; Zapier’den farkı kaynağının açık ve kendi kurulumunda sınırsız olması.',
        'Visual workflow automation you can self-host; unlike Zapier the source is open and self-hosted runs are unmetered.', C)
    add('https://docs.n8n.io/', 'n8n Dokümantasyonu', ['dokümantasyon', 'otomasyon'],
        'n8n’in resmî dokümanı; düğüm referansı ve kendi sunucuna kurulum rehberleri.',
        'n8n’s official documentation — node reference and self-hosting guides.', C)
    add('https://zapier.com/', 'Zapier', ['freemium', 'otomasyon'],
        'SaaS uygulamalarını birbirine bağlayan otomasyon servisi; en geniş entegrasyon kataloğuna sahip olması başlıca avantajı.',
        'Automation service wiring SaaS apps together; the widest integration catalogue is its main advantage.', C)
    add('https://www.make.com/', 'Make', ['freemium', 'otomasyon'],
        'Görsel senaryo tabanlı otomasyon; Zapier’in doğrusal adım modeline karşılık dallanma ve döngüyü daha rahat kurar.',
        'Visual scenario-based automation, handling branching and loops more comfortably than Zapier’s linear steps.', C)
    add('https://www.microsoft.com/power-platform/products/power-automate', 'Power Automate', ['ücretli', 'otomasyon'],
        'Microsoft 365 içindeki otomasyon aracı; kurumsal Office ve SharePoint akışlarında yerleşik olması sebebiyle tercih ediliyor.',
        'Automation inside Microsoft 365, chosen mainly because it is native to corporate Office and SharePoint flows.', C)
    add('https://temporal.io/', 'Temporal', ['açık kaynak', 'orkestrasyon'],
        'Uzun süreli ve hataya dayanıklı iş akışı motoru; basit otomasyon araçlarından farkı, günlerce süren işlemi çökse bile kaldığı yerden sürdürmesi.',
        'Durable workflow engine; unlike simple automation tools it resumes multi-day processes from where they crashed.', C)
    add('https://airflow.apache.org/', 'Apache Airflow', ['açık kaynak', 'orkestrasyon'],
        'Veri hattı zamanlayıcısının fiilî standardı; zamanlanmış toplu işlerde güçlü, olay güdümlü akışlarda hantal.',
        'The de facto standard scheduler for data pipelines — strong for scheduled batch work, clumsy for event-driven flows.', C)
    add('https://www.prefect.io/', 'Prefect', ['açık kaynak', 'orkestrasyon', 'python'],
        'Airflow’a Python öncelikli alternatif; akışı ayrı bir DSL yerine sıradan Python fonksiyonu olarak yazarsın.',
        'Python-first alternative to Airflow — you write flows as ordinary Python functions rather than a separate DSL.', C)
    add('https://kestra.io/', 'Kestra', ['açık kaynak', 'orkestrasyon'],
        'YAML ile tanımlanan orkestrasyon motoru; akışı kodlamak yerine bildirimsel yazmak isteyen ekipler için.',
        'Orchestration defined in YAML — for teams who prefer declaring flows over coding them.', C)
    add('https://pipedream.com/', 'Pipedream', ['freemium', 'otomasyon', 'geliştirici'],
        'Adımlarına doğrudan kod yazılabilen otomasyon platformu; no-code araçların duvara tosladığı yerde devam etmeni sağlar.',
        'Automation platform whose steps can contain real code — it keeps going where no-code tools hit a wall.', C)

    # ---------------------------------------------------------- agent araç & yetenek
    add('https://github.com/affaan-m/everything-claude-code', 'Everything Claude Code', ['açık kaynak', 'github', 'agent'],
        'Kod asistanları için yetenek, kural ve bellek düzeni sunan kapsamlı yapılandırma seti.',
        'A comprehensive configuration set of skills, rules and memory layout for coding agents.', C)
    add('https://github.com/ComposioHQ/awesome-claude-skills', 'Awesome Claude Skills', ['açık kaynak', 'github', 'koleksiyon'],
        'Claude yetenekleri için derlenmiş liste; tek tek arama yapmadan neyin mevcut olduğunu görmek için.',
        'A curated list of Claude skills — a way to see what exists without searching one by one.', C)
    add('https://github.com/obra/superpowers', 'Superpowers', ['açık kaynak', 'github', 'agent'],
        'Agent’lara metodoloji dayatan yetenek çatısı; serbest istem yerine adımlı bir geliştirme disiplini kurar.',
        'A skills framework that imposes a methodology on agents — a stepwise development discipline instead of free-form prompting.', C)
    add('https://github.com/gsd-build/get-shit-done', 'Get Shit Done', ['açık kaynak', 'github', 'agent'],
        'Meta-istem ve şartname güdümlü geliştirme sistemi; “vibe coding”den planlı üretime geçmeyi hedefler.',
        'A meta-prompting and spec-driven development system aimed at moving from vibe coding to planned delivery.', C)
    add('https://github.com/HKUDS/OpenSpace', 'OpenSpace', ['açık kaynak', 'github', 'agent'],
        'Agent’lar için yetenek yönetim katmanı; hangi yeteneğin ne zaman yükleneceğine karar vererek maliyeti düşürmeyi amaçlar.',
        'A skill-management layer for agents, deciding which skill loads when in order to cut cost.', C)
    add('https://github.com/blader/humanizer', 'Humanizer', ['açık kaynak', 'github', 'yazım'],
        'Metinden yapay zeka yazımına özgü kalıpları temizleyen yetenek; üslup düzeltmesine odaklı dar bir araç.',
        'A skill that strips tell-tale AI writing patterns from text — a narrow tool focused purely on style.', C)
    add('https://github.com/DietrichGebert/ponytail', 'Ponytail', ['açık kaynak', 'github', 'agent'],
        'Agent’ı gereksiz kod yazmaktan alıkoyan yetenek; “en iyi kod yazılmayan koddur” ilkesini davranışa çevirir.',
        'A skill that stops an agent writing unnecessary code, turning “the best code is the code you never wrote” into behaviour.', C)
    add('https://github.com/shanraisshan/claude-code-best-practice', 'Claude Code Best Practice', ['açık kaynak', 'github', 'rehber'],
        'Kod asistanıyla çalışma pratiklerini derleyen depo; tek bir aracın dokümanından çok saha notu niteliğinde.',
        'A repo collecting practices for working with a coding agent — field notes rather than official docs.', C)
    add('https://github.com/mvanhorn/last30days-skill', 'last30days', ['açık kaynak', 'github', 'araştırma'],
        'Bir konuda son 30 günün Reddit, X ve YouTube içeriğini tarayan agent yeteneği; eğitim verisi eskimesini kapatmaya yönelik.',
        'An agent skill sweeping the last 30 days of Reddit, X and YouTube on a topic — aimed at closing the training-cutoff gap.', C)
    add('https://github.com/evermind-ai/raven', 'Raven', ['açık kaynak', 'github', 'agent'],
        'Bellek öncelikli, kendini geliştiren agent koşum takımı; oturumlar arası öğrenmeyi merkeze alır.',
        'A memory-first, self-improving agent harness that puts cross-session learning at the centre.', C)
    add('https://github.com/diegosouzapw/OmniRoute', 'OmniRoute', ['açık kaynak', 'github', 'ağ geçidi'],
        'Tek uç noktadan yüzlerce sağlayıcıya yönlendiren MIT lisanslı YZ ağ geçidi; sağlayıcıya bağımlılığı azaltmak için.',
        'MIT-licensed AI gateway routing one endpoint to hundreds of providers — aimed at reducing vendor lock-in.', C)
    add('https://github.com/lyogavin/airllm', 'AirLLM', ['açık kaynak', 'github', 'yerel'],
        '70B modeli 4 GB GPU ile çalıştırmayı sağlayan katman katman çıkarım tekniği; nicemlemeden farklı bir bellek stratejisi.',
        'Layer-by-layer inference that runs a 70B model on a 4 GB GPU — a different memory strategy from quantisation.', C)
    add('https://github.com/microsoft/BitNet', 'BitNet', ['açık kaynak', 'github', 'araştırma'],
        'Microsoft’un 1-bit LLM çıkarım çatısı; ağırlıkları uç noktaya kadar sıkıştırarak CPU üzerinde çalıştırmayı hedefler.',
        'Microsoft’s 1-bit LLM inference framework, compressing weights to the extreme to run models on CPU.', C)
    add('https://github.com/microsoft/call-center-ai', 'Call Center AI', ['açık kaynak', 'github', 'örnek'],
        'API çağrısıyla telefon araması yapan agent örneği; sesli agent mimarisi için çalışan bir referans uygulama.',
        'An agent that places phone calls from an API call — a working reference implementation for voice-agent architecture.', C)
    add('https://amilabs.xyz/', 'AMI Labs', ['araştırma'],
        'Dünya modeli tabanlı yapay zeka geliştiren araştırma şirketi; dil modeli yerine fiziksel dünyayı modellemeye odaklı.',
        'Research company building world-model-based AI, focused on modelling the physical world rather than language.', C)
    add('https://www.youtube.com/playlist?list=PL4cUxeGkcC9g4YJeBqChhFJwKQ9TRiivY', 'Agent Geliştirme (oynatma listesi)', ['video', 'ücretsiz'],
        'Agent geliştirme üzerine video dersi dizisi; okumak yerine izleyerek başlamak isteyenler için.',
        'A video course series on agent development, for those who would rather watch than read.', C)
