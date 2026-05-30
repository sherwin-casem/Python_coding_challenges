from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
    
    def handle_data(self, data):
        if data.strip():   # ignore empty or '\n'
            print(">>> Data")
            print(data)

parser = MyHTMLParser()

n = int(input())
html = ""

for _ in range(n):
    html += input() + "\n"

parser.feed(html)
