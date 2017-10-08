from urllib.parse import urlparse, urlunparse
import lxml as lxml
import requests
from lxml.html import parse, HTMLParser


class ImgurScraper(object):
    def fetch(self, url, user_agent="Copypasta", headers=None):
        if not headers:
            headers = {"User-Agent": user_agent}
        req = requests.get(url, headers=headers)
        return req

    def lxmldom(self, url):
        req = self.fetch(url)
        parser = HTMLParser(encoding='utf-8',
                                      remove_pis=True,
                                      remove_comments=True,
                                      remove_blank_text=True)
        dom = lxml.html.fromstring(req.text, base_url=url, parser=parser)
        dom.make_links_absolute(url)
        return dom

    def imgur_urls(self, url):
        scheme, domain, path, param, query, fragment = urlparse(url)
        if domain == "i.imgur.com":
            return [url]
        paths = path[1:].split("/")
        if len(paths) == 1:
            ids = paths[0].split(",")
            img_urls = []
            for id_ in ids:
                path = id_ + ".jpg"
                domain = "i.imgur.com"
                img_urls.append(urlunparse((scheme, domain, path, None, None, None)))
        else:
            dom = self.lxmldom(url)
            img_urls = dom.xpath(imgur_img_xpath)
        return img_urls


imgur_img_xpath = "//a[@class='image-list-link']/@href"
