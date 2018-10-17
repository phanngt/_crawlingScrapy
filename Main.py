import os
from pathlib import Path


def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(str(Path(os.path.dirname(__file__)).parent) + '/' + directory)


create_directory('spotify')
create_directory('zingMp3')
create_directory('for fun')

