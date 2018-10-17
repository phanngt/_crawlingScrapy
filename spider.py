from link_finder import  LinkFinder
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
        Spider.boot()

    @staticmethod
    def boot():
        create_data_file(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queued_file)
        Spider.crawled = file_to_set(Spider.crawled_file)