class Book:
    def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def set_title(self, v):
        self.__title = v

    def set_year(self, v):
        self.__year = v

    def set_publisher(self, v):
        self.__publisher = v

    def set_genre(self, v):
        self.__genre = v

    def set_author(self, v):
        self.__author = v

    def set_price(self, v):
        self.__price = v

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_publisher(self):
        return self.__publisher

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


