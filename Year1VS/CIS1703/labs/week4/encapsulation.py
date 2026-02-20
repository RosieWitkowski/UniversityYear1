class Book():
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.__price = None

    def set_price(self, price: float):
        if price < 0:
            print("Error: price cannot be negative.")
            self.__price = "Price not found"
            return
        self.__price = price

    def get_price(self) -> float:
        return self.__price

    def display_info(self):
        print(f"{self.title} | {self.author} | £{self.get_price()}")

Gatsby = Book('The Great Gatsby', 'F.Scott Fitzgerald')
Gatsby.set_price(-10.99)
NinetyEightyFour = Book('1984', 'George Orwell')
NinetyEightyFour.set_price(8.99)

Gatsby.display_info()
NinetyEightyFour.display_info()

print(Gatsby.price)