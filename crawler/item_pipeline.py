import json


class ItemPipeline:
    def __init__(self, uid, title, abstract, authors, in_links, out_links):
        self.uid = str(uid)
        self.title = str(title.encode(encoding='utf-8', errors='ignore'))
        self.abstract = str(abstract.encode(encoding='utf-8', errors='ignore'))
        self.authors = []
        for author in authors:
            self.authors.append(str(author.text.encode(encoding='utf-8', errors='ignore')))
        self.in_links = in_links
        self.out_links = out_links

    def __str__(self):
        return ("uid:" + self.uid +
                "\r\n" + "title: " + self.title )



