
from threading import Thread

import requests


class DownloadHeader(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('E:/code/picture/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get(
        "http://api.tianapi.com/meinv/?key=8440a83c08e31246c82659cc76507748&num=10")
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHeader(url).start()


if __name__ == '__main__':
    main()
