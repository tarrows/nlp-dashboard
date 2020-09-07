from lib import OpenGraph


def ogp():
    og = OpenGraph(url='http://www.imdb.com/title/tt0117500/')
    for p in ['title', 'type', 'image', 'url', 'description']:
        if p in og:
            print(p, og[p])
        else:
            print('no attr:', p)


if __name__ == '__main__':
    ogp()
