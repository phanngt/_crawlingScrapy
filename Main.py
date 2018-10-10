import os


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir('/Users/phannguyen/PycharmProjects/CrawlingInfo/' + directory)


create_directory('spotify')
create_directory('zingMp3')
