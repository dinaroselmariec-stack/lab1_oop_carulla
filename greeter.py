class Car:
    wheels = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand}{self.model}{self.year} - wheels {self.wheels}"

car1= Car("Toyota", "Wigo", "2020")
car2= Car("Toyota", "Innova", "2021")
car3= Car("Toyota", "Fortuner", "2022")

print(car1)
print(car2)
print(car3)


class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, km):
      if km > 0:
          self.mileage += km
          print(f"Drove {km} km. Total: {self.mileage} km")
      else:
          print("Distance must be positive!")

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} - Wheels: {self.wheels}, Mileage: {self.mileage} km"

if __name__=="__main__":
        car1 = Car("Toyota", "Wigo", 2020)
        car2 = Car("Toyota", "Innova", 2021)
        car3 = Car("Toyota", "Fortuner", 2022)

        print(car1)
        car1.drive(50)
        car1.drive(-10)
        print(f"Age: {car1.age(2026)} years")

        print(car2)
        print(car3)


class LibraryBook:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        LibraryBook.counter += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}')"


# Creating book objects
book1 = LibraryBook("Noli Me Tangere", "Jose Rizal")
book2 = LibraryBook("El Filibusterismo", "Jose Rizal")
book3 = LibraryBook("Florante at Laura", "Francisco Balagtas")

# Testing the methods
print(book1)
book1.borrow()
book1.return_book()

print(book2)
book2.borrow()

print("Total books:", LibraryBook.counter)

print(repr(book3))
