from utils.parser import parse_article


class LegalService:
    def __init__(self, repo, rag_engine):
        self.__repo = repo
        self.__rag_engine = rag_engine

    def initialize_data(self):
        articles = self.__repo.find_all()
        self.__rag_engine.load_articles(articles)

    def analyze_case(self, case_text):
        docs = self.__rag_engine.search_relevant_articles(case_text, 6)

        violated = []
        favorable = []

        for doc in docs:
            article = parse_article(doc)

            if article.article_type == "violation":
                violated.append(article)
            elif article.article_type == "defense":
                favorable.append(article)

        return violated, favorable