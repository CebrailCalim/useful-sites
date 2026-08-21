# -*- coding: utf-8 -*-
"""Records surfaced by Invesp's "109 useful websites" post.

This source contributed almost nothing, and the reason is worth recording.
The post is largely a Web 2.0 graveyard: of its 96 links, 27 fail outright and
most of the survivors are dead services on resold domains. Odeo now serves an
Indonesian gambling site, imeem redirects to Myspace, Revver sells marine
industry marketing, ma.gnolia.com answers "THIS DOMAIN HAS BEEN SEIZED", and
gOffice and TekTag are parking pages. All of them return HTTP 200.

That is the case for checking content and not just status codes, and it is the
same failure mode as an archived GitHub repository: alive by every automated
measure, dead in every way that matters.

What is left below is the handful that both survived and belongs here.

These carry src='invesp'.
"""

S = 'invesp'


def load(add):
    def a(url, name, tags, tr, en, cat):
        add(url, name, tags, tr, en, cat, S)

    a('https://extendsclass.com/', 'ExtendsClass', ['tarayıcı-içi', 'ücretsiz', 'api'],
      'Geliştirici araçları koleksiyonu: REST istemcisi, SQLite tarayıcı, XML/JSON doğrulayıcı, '
      'normal ifade testi. IT Tools gibi derlemelerden farkı veritabanı ve API istemcisi gibi '
      '"ağır" araçları da tarayıcıda çalıştırması.',
      'A collection of developer tools: a REST client, a SQLite browser, XML and JSON validators, '
      'regex testing. Against collections like IT Tools it runs the heavier things — a database '
      'browser and an API client — in the browser too.',
      'araclar')
    a('https://promptlayer.com/', 'PromptLayer', ['llm', 'gözlemlenebilirlik', 'freemium'],
      'LLM istemlerini sürümleyen, kaydeden ve değerlendiren platform; hangi istemin hangi çıktıyı '
      'ürettiği izlenebiliyor. Genel APM araçlarından farkı istemi birinci sınıf nesne sayması — '
      'istem değişikliğini kod dağıtımından ayırıp ürün ekibine açıyor.',
      'A platform for versioning, logging and evaluating LLM prompts, so you can trace which prompt '
      'produced which output. Unlike general APM tooling it treats the prompt as a first-class '
      'object, separating prompt changes from code deploys.',
      'yz_altyapi')
    a('https://browse.ai/', 'Browse AI', ['otomasyon', 'freemium', 'agent'],
      'Web sitelerinden veri çıkarmayı ve değişiklikleri izlemeyi kod yazmadan kuran araç; '
      'tarayıcıda tıklayarak eğitiyorsun. Scrapy gibi çerçevelerden farkı seçici yazmaya gerek '
      'kalmaması ve sayfa düzeni değişince kendini onarmaya çalışması.',
      'Extracts data from websites and monitors them for changes without code — you train it by '
      'clicking in the browser. Against frameworks like Scrapy there are no selectors to write, and '
      'it attempts to self-heal when a page layout shifts.',
      'yz_arac')
    a('https://axiom.ai/', 'Axiom.ai', ['otomasyon', 'freemium', 'eklenti'],
      'Tarayıcı otomasyonunu tarayıcı eklentisi olarak kuran araç; form doldurma, tıklama ve veri '
      'çekme adımlarını sürükle bırak ile diziyorsun. Puppeteer ya da Playwright’tan farkı kendi '
      'oturumunda çalışması — giriş yapılmış sayfalarda ek kimlik doğrulama gerekmiyor.',
      'Browser automation as a browser extension, with form filling, clicking and scraping steps '
      'assembled by drag and drop. Against Puppeteer or Playwright it runs inside your own session, '
      'so pages you are already logged into need no separate authentication.',
      'yz_arac')
    a('https://teleporthq.io/', 'TeleportHQ', ['frontend', 'freemium', 'otomasyon'],
      'Görsel arayüz tasarımından temiz React, Vue ya da HTML kodu üreten düşük kodlu platform. '
      'Webflow’dan farkı çıktının dışa aktarılabilir ve okunabilir bileşen kodu olması — tasarımı '
      'devralıp elle geliştirmeye devam edebiliyorsun.',
      'A low-code platform that turns a visual interface design into clean React, Vue or HTML. '
      'Against Webflow the output is exportable, readable component code — you can take the design '
      'over and keep building by hand.',
      'web')
