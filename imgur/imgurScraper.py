from urllib.parse import urlparse, urlunparse

import lxml as lxml
import requests


class ImgurScraper(object):
    def fetch(self, url, user_agent="Copypasta", headers=None):
        if not headers:
            headers = {"User-Agent": user_agent}
        req = requests.get(url, headers=headers)
        return req

    def lxmldom(self, url):
        req = self.fetch(url)
        parser = lxml.html.HTMLParser(encoding='utf-8',
                                      remove_pis=True,
                                      remove_comments=True,
                                      remove_blank_text=True)
        dom = lxml.html.fromstring(req.text, base_url=url, parser=parser)
        dom.make_links_absolute(url)
        return dom

    def imgur_urls(self, url):

        scheme, domain, path, param, query, fragment = urlparse(url)
        if domain == "i.imgur.com":
            # Looks like a direct image already.
            return [url]
        paths = path[1:].split("/")
        if len(paths) == 1:
            # No /a/, /gallery/ but could be imgur.com/qVhCPQB,5fLQ9KT
            ids = paths[0].split(",")
            img_urls = []
            for id_ in ids:
                # imgur doesn't care if your url file ext is accurate.
                path = id_ + ".jpg"
                domain = "i.imgur.com"
                img_urls.append(urlunparse((scheme, domain, path, None, None, None)))
        else:
            # Scrape album, gallery pages.
            dom = self.lxmldom(url)
            # Galleries don't always show an entire album, but surely you want the
            #  entire album...
            # full_album_url = dom.xpath(imgur_img_xpath)
            # if full_album_url:
            #     dom = url.lxmldom(full_album_url[0])
            img_urls = dom.xpath(imgur_img_xpath)
        return img_urls


imgur_img_xpath = "//a[@class='image-list-link']/@href"
