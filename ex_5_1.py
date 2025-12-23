class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Title: {self.title}. Author: {self.author}.  Year: {self.year}"
book1 = Book('Трудно быть богом', 'Джейсон Стэтхом', 1909)
print(book1.get_info())