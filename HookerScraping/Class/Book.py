class Book():
    # CONSTRUCTOR
    def __init__(self, title, price, stock, category, cover, description):
        # VARIABLES
        self.__title = title
        self.__price = price
        self.__stock = stock
        self.__category = category
        self.__cover = cover
        self.__description = description
    # ACCESADORES Y MUTADORES

    # Title
    @property 
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title=title
    # Price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price=price
    # Stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        self.__stock=stock
    
    # Category
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category):
        self.__category=category

    # Cover
    @property
    def cover(self):
        return self.__cover
    @cover.setter
    def cover(self, cover):
        self.__cover=cover

    # Description
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description=description

    # FUNCIONES Y PROCEDIMIENTOS
    def to_string(self):
        return f"Title: {self.title}.\nPrice: {self.price}.\nStock: {self.stock}.\nCategory: {self.category}.\nCover: {self.cover}.\nDescription: {self.description}\n"