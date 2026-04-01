from domain.article import Article


def parse_article(line):
    parts = line.strip().split("|")

    if len(parts) != 3:
        raise ValueError(f"Linie invalidă: {line}")

    number = parts[0].strip()
    article_type = parts[1].strip()
    content = parts[2].strip()

    return Article(number, article_type, content)