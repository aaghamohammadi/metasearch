class ItemPipeline:
    def __init__(self, uid, title, abstract, authors):
        self.uid = str(uid)
        self.title = str(title)
        self.abstract = str(abstract)
        self.authors = []
        for author in authors:
            self.authors.append(str(author.text))

    def __str__(self):
        return ("uid:" + self.uid +
                "\r\n" + "title: " + self.title +
                "\r\n" + "abstract: " + self.abstract)
