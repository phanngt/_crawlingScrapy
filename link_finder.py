from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links


finder = LinkFinder('https://mp3.zing.vn/', 'https://mp3.zing.vn/')
finder.feed('<li><a id="navbar-top100" title="Top 100" href="/top100/Nhac-Tre/IWZ9Z088.html">Top 100</a>'
                '<div class="megamenu submenu menu-col-1">'
                    '<div class="subcol menu-col-1-narrow">'
                        '<div class="subinner_item">'
                            '<ul>'
                                '<li><a title="Việt Nam" href="/top100/Nhac-Tre/IWZ9Z088.html">Việt Nam</a></li>'
                                '<li><a title="Âu Mỹ" href="/top100/Pop/IWZ9Z097.html">Âu Mỹ</a></li>'
                                '<li><a title="Châu Á" href="/top100/Kpop/IWZ9Z08W.html">Châu Á</a></li>'
                                '<li><a title="Hòa Tấu" href="/top100/Classical/IWZ9Z0BI.html">Hòa Tấu</a></li>'
                            '</ul>'
                        '</div>'
                    '</div><!--End .sub-col -->'
                '</div>'
            '</li>')

