import json


class ItemPipeline:
    def __init__(self, uid, title, abstract, authors, links):
        self.uid = str(uid)
        self.title = str(title)
        self.abstract = str(abstract)
        self.authors = []
        for author in authors:
            self.authors.append(str(author.text))
        self.links = links

    def __str__(self):
        return ("uid:" + self.uid +
                "\r\n" + "title: " + self.title )



