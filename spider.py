from link_finder import  LinkFinder
from urllib.request import urlopen
from general import *


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queued_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queued_file = Spider.project_name + '/queue_file.txt'
        Spider.crawled_file = Spider.project_name + '/crawled_file.txt'
        Spider.boot()
        Spider.crawled_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_directory(Spider.project_name)
        create_data_file(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queued_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawled_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue' + str(len(Spider.queue)) + ' | Crawled' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
            return finder.page_links()
        except:
            print('Error: can not crawled page')
            return set()

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queued_file)
        set_to_file(Spider.crawled, Spider.crawled_file)