class ItemPipeline:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name:" + self.name.encode('UTF-8')
