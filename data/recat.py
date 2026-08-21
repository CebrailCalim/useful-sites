# -*- coding: utf-8 -*-
"""Category refinements applied on top of what each note declares.

After the directory passed 900 records three categories had become dumping
grounds -- Tools 116, AI Applied Tools 108, AI Agents/RAG 100, together more
than a third of everything. A category that large stops being navigation and
starts being a second search box.

Rather than edit the `cat` argument in a dozen part files, the moves live here
where they can be read as one list and argued with. New entries should declare
the right category directly; this table is for the reclassification, not for
routine use.

Four categories were added:
  medya       media, design and file tools split out of Tools
  barindirma  self-hosted and personal-cloud software, previously scattered
  yz_uretim   generative media, split out of AI Applied Tools
  yz_rag      retrieval, embeddings and vector stores, split out of AI Infra

Ten workflow-automation tools (Airflow, n8n, Zapier and the rest) moved from
AI Infra to DevOps, where they belonged before LLM orchestration borrowed the
vocabulary.
"""

MOVES = {
    # ---------------------------------------------------- media, design, files
    'medya': [
        '3Dassets.one', 'ambientCG', 'Aseprite', 'AudioNotes', 'Blender',
        'Carbon', 'CodingFont', 'Coolors', 'Devicons', 'diagrams.net',
        'draw.io', 'Excalidraw', 'Figma', 'FontForge', 'iLovePDF', 'Inkscape',
        'Krita', 'LosslessCut', 'LottieFiles', 'MediaInfo',
        'Mermaid Live Editor', 'Moqups', 'OpenReel Video', 'Photopea',
        'Piskel', 'Programming Fonts', 'ray.so', 'Same Energy',
        'SankeyDiagram.net', 'ShareX', 'Shutter Encoder', 'Squoosh',
        'Subtitle Edit', 'Subtitle Editor Online', 'The Noun Project',
        'TinyPNG', 'UI Design Daily', 'Vector Magic', 'VS Code Themes',
        'XnConvert', 'YouTube Video Kesici',
    ],

    # ------------------------------------------- self-hosting, personal cloud
    'barindirma': [
        'Audiobookshelf', 'Dawarich', 'Element', 'Immich', 'Nextcloud',
        'Organic Maps', 'Rocket.Chat', 'Syncthing', 'Thunderbird', 'Logseq',
        'KeepNote', 'LibreOffice', 'Feedly',
        'Pi-hole', 'AdGuard Home',        # came from Networking
    ],

    # ------------------------------------------------------- generative media
    'yz_uretim': [
        'Adobe Firefly', 'Auphonic', 'Bing Image Creator', 'BlenderGPT',
        'Canva', 'CapCut', 'Clipdrop', 'ComfyUI', 'Craiyon', 'Dream Textures',
        'Fooocus', 'Gamma', 'Homestyler', 'Ideogram', 'InstantMesh',
        'InvokeAI', 'Krisp', 'Krita AI Diffusion', 'Leonardo AI', 'Luma AI',
        'Meshy', 'Microsoft Designer', 'Napkin AI', 'Otter.ai', 'PicLumen',
        'Pika', 'Pitch', 'Planner 5D', 'Playground AI', 'Point-E',
        'Predis.ai', 'Recraft', 'remove.bg', 'Shap-E', 'Simplified',
        'SlidesAI', 'Spline', 'Stable Diffusion WebUI', 'Stable Fast 3D',
        'Stitch', 'Tripo AI', 'Video2X', 'Voicebox', 'Whisper',
    ],

    # ------------------------------------------ retrieval, embeddings, vectors
    'yz_rag': [
        'Atlas Vector Search', 'BGE Modelleri', 'Chroma', 'Cohere Embed',
        'Elasticsearch', 'Graphify', 'GraphRAG', 'Haystack', 'LangGraph Memory',
        'Letta', 'LlamaIndex', 'Mem0', 'Mem0 (kaynak)', 'Milvus', 'Neo4j',
        'OpenAI Embeddings', 'pgvector', 'Pinecone', 'PostgreSQL', 'Qdrant',
        'Ragas', 'RAGFlow', 'Raven', 'Redis', 'Sentence Transformers',
        'TruLens', 'Unstructured', 'Vertex AI Embeddings', 'Voyage AI',
        'Weaviate', 'Zep',
    ],

    # ------------------- workflow automation: infrastructure, not AI-specific
    'devops': [
        'Apache Airflow', 'Kestra', 'Make', 'n8n', 'n8n Dokümantasyonu',
        'Pipedream', 'Power Automate', 'Prefect', 'Temporal', 'Zapier',
    ],
}

BY_NAME = {}
for _cat, _names in MOVES.items():
    for _n in _names:
        BY_NAME[_n] = _cat
