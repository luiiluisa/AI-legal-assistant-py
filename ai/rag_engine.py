import chromadb


class RAGEngine:
    def __init__(self):
        self.__client = chromadb.Client()
        self.__collection = self.__client.get_or_create_collection(name="laws_collection")

    def load_articles(self, articles):
        existing = self.__collection.get()

        if existing["ids"]:
            return

        for i, article in enumerate(articles):
            document = f"{article.number} | {article.article_type} | {article.content}"

            self.__collection.add(
                documents=[document],
                ids=[str(i)]
            )

    def search_relevant_articles(self, case_text, n_results=6):
        results = self.__collection.query(
            query_texts=[case_text],
            n_results=n_results
        )

        return results["documents"][0]