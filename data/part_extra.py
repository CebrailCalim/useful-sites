# -*- coding: utf-8 -*-
"""Ilk gecise girmeyen kalan kayitlar."""


def load(add):
    add('https://copilot.microsoft.com/', 'Microsoft Copilot', ['ücretsiz', 'asistan'],
        'Microsoft’un asistanı. Windows ve Office içine gömülü olduğu için belge veya tablo üzerinde ayrı siteye gitmeden çalışabiliyorsun.',
        'Microsoft’s assistant. Embedded in Windows and Office, so you can work on a document or sheet without leaving for another site.',
        'yz_model')
    add('https://www.youtube.com/watch?v=iWS9ogMPOI0', 'FastAPI ile 15 Dakikada REST API', ['ücretsiz', 'video', 'python'],
        'FastAPI ile sıfırdan REST API kuran kısa video; dokümana dalmadan önce bütünü görmek için.',
        'A short video building a REST API from scratch with FastAPI — for seeing the whole shape before diving into the docs.',
        'backend')
    add('http://literateprogramming.com/', 'Literate Programming', ['ücretsiz', 'referans'],
        'Knuth’un okunabilir programlama yaklaşımının arşivi; kodu belgeyle iç içe yazma fikrinin kaynağı.',
        'The archive of Knuth’s literate programming approach — the source of the idea of writing code interwoven with prose.',
        'referans')
    add('http://www.shedai.net/', 'Şadi Evren Şeker', ['ücretsiz', 'türkçe', 'akademik'],
        'Türkçe bilgisayar mühendisliği ders notları ve terim açıklamaları arşivi; yerel kaynak kıtlığı olan konularda başvuru noktası.',
        'An archive of Turkish computer engineering lecture notes and term explanations — a reference point for topics with few local sources.',
        'referans')
    add('https://www.language-archives.org/', 'Open Language Archives Community', ['ücretsiz', 'dilbilim', 'arşiv'],
        'Dil kaynağı arşivlerini ortak standartla birleştiren topluluk; dağınık üniversite arşivlerini tek katalogda toplar.',
        'A community uniting language resource archives under a shared standard, gathering scattered university archives into one catalogue.',
        'bilim')
