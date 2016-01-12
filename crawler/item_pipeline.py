class ItemPipeline:
    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return "Name:" + self.name
