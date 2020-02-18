class SearchHelper():
    def __init__(self, books = []):
        self.books = books

    def search_title(self, title):
        result = []
        for book in self.books:
            print(title.lower())
            if title.lower() in book.getTitle:
                result.append(book)

        return result

    def search_author(self, author):
        result = []
        for book in self.books:
            if author.lower() in book.getAuthor:
                result.append(book)

        return result
