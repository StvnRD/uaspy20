from core.baseapp import *
from data_model.book import *
from data_model.author import *
from core.search_helper import *

class MainApp(BaseApp):
    def __init__(self):
        self.books = []

    def run(self):
        while True:
            key = super().menu()
            if key == "4":
                break
            elif key == "3":
                self.search_book()
            elif key == "2":
                self.add_book()
            elif key == "1":
                self.list_book()
            else:
                print("Pilihan tidak ada.")

    def list_book(self):
        print("Daftar Buku: ")
        for i in self.books:
            print(i.toString())

    def search_book(self):
        searchclass = SearchHelper(self.books)
        tanya = input("Search berdasarkan title/author (jawab title/author):")
        if tanya == "title":
            judul = input("Input judul:")
            hasil = searchclass.search_title(judul)
            print("Hasil pencarian:",hasil)
        else:
            author = input("Input author:")
            hasil = searchclass.search_author(author)
            print("Hasil pencarian:",hasil)
            
    def add_book(self):
        judul = input("Judul: ")
        pencipta = input("Pencipta: ")
        harga = input("Harga: ")
        kopi = input("Berapa kopi: ")
        author = Author(pencipta)
        book = Book(judul, author, harga, kopi)
        self.books.append(book)
        print("Sukses menambah buku!")
if __name__ == "__main__":
    app = MainApp()
    app.run()
