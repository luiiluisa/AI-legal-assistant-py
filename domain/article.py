class Article:
    def __init__(self, number, article_type, content):
        self.number = number
        self.article_type = article_type
        self.content = content

    def __str__(self):
        return f"{self.number} | {self.article_type} | {self.content}"