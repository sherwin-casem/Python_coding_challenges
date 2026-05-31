from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

# Read input
n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

parser = MyHTMLParser()
parser.feed(html)
