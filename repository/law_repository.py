from utils.parser import parse_article


class LawRepository:
    def __init__(self, filename):
        self.__filename = filename

    def find_all(self):
        articles = []

        with open(self.__filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                article = parse_article(line)
                articles.append(article)

        return articles