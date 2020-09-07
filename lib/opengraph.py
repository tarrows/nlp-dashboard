import re
import requests
from bs4 import BeautifulSoup


class OpenGraph:
    data = {}

    def __init__(self, url: str):
        res = requests.get(url)
        self.data = OpenGraph.parse(res.text)

    def __contains__(self, item):
        return item in self.data

    def __getattr__(self, name):
        return self.data[name]

    def __getitem__(self, name):
        return self.data[name]

    @staticmethod
    def parse(html):
        doc = BeautifulSoup(html, features="html.parser")
        graphs = doc.html.findAll(property=re.compile(r'^og:'))

        data = {
            og['property'][3:]: og['content'] for og in graphs if og.has_attr('content')
        }

        return data
