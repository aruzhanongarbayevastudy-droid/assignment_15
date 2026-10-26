"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError("Ingredient already exists")
        self.ingredients.append(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def get_current_floor(self):
        return self.current_floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def check_balance(self):
        return self.balance


"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y


"""
Exercise 8:
Create a class Car with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError("Speed and mileage cannot be negative")
        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student:
    def __init__(self, name, age=0):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age


class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        for student in self.students:
            print(student.name)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        hours, minutes = map(int, self.departure.split(":"))
        total_minutes = hours * 60 + minutes + delay_time * 60
        total_minutes %= 24 * 60
        hours = total_minutes // 60
        minutes = total_minutes % 60
        self.departure = f"{hours:02d}:{minutes:02d}"


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed.
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Matrices must have the same dimensions")
        if any(len(a) != len(b) for a, b in zip(self.matrix, other.matrix)):
            raise ValueError("Matrices must have the same dimensions")

        result = [
            [a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(self.matrix, other.matrix)
        ]
        return Matrix(result)

    def subtract(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Matrices must have the same dimensions")
        if any(len(a) != len(b) for a, b in zip(self.matrix, other.matrix)):
            raise ValueError("Matrices must have the same dimensions")

        result = [
            [a - b for a, b in zip(row1, row2)]
            for row1, row2 in zip(self.matrix, other.matrix)
        ]
        return Matrix(result)

    def multiply(self, other):
        if not self.matrix or not other.matrix:
            raise ValueError("Matrices cannot be empty")

        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Invalid dimensions for multiplication")

        if any(len(row) != len(self.matrix[0]) for row in self.matrix):
            raise ValueError("Invalid matrix dimensions")

        if any(len(row) != len(other.matrix[0]) for row in other.matrix):
            raise ValueError("Invalid matrix dimensions")

        result = [
            [
                sum(
                    self.matrix[i][k] * other.matrix[k][j]
                    for k in range(len(other.matrix))
                )
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and circumference of the circle. Handle exceptions for negative radius values.
"""
import math


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if (
            side_a <= 0
            or side_b <= 0
            or side_c <= 0
            or side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("Invalid triangle sides")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        return (
            s
            * (s - self.side_a)
            * (s - self.side_b)
            * (s - self.side_c)
        ) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


"""
Exercise 16:
Design shape classes with methods to calculate area and perimeter.
"""
class AbstractShape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Circle(AbstractShape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def perimeter(self):
        return self.circumference()


class Rectangle(AbstractShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        if (
            side_a <= 0
            or side_b <= 0
            or side_c <= 0
            or side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("Invalid triangle sides")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = self.perimeter() / 2
        return (
            s
            * (s - self.side_a)
            * (s - self.side_b)
            * (s - self.side_c)
        ) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, skip to the next song, and shuffle the playlist.
"""
import random


class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.current_index = 0

    def add_song(self, song):
        self.playlist.append(song)

    def play_song(self):
        if self.playlist:
            self.current_index = 0
            self.current_song = self.playlist[self.current_index]

    def next_song(self):
        if self.playlist:
            self.current_index = (
                self.current_index + 1
            ) % len(self.playlist)
            self.current_song = self.playlist[self.current_index]

    def shuffle(self):
        if self.playlist:
            random.shuffle(self.playlist)
            if self.current_song in self.playlist:
                self.current_index = self.playlist.index(self.current_song)
            else:
                self.current_index = 0
            self.current_song = self.playlist[self.current_index]


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels.
"""
class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity += quantity

    def sell(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if quantity > self.quantity:
            raise ValueError("Not enough stock")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        return (
            f"Title: {self.title}, "
            f"Genre: {self.genre}, "
            f"Rating: {self.rating}"
        )


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age.
"""
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


class Teacher(Person):
    pass


class Student(Person):
    def __init__(self, name, age=0):
        super().__init__(name, age)


class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
        return self.teachers + self.students

    def print_all(self):
        for person in self.get_all():
            print(f"{person.name}, {person.age}")


"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class.
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        ]
        self.cards = [
            Card(suit, rank)
            for suit in suits
            for rank in ranks
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise IndexError("No cards left in the deck")
        return self.cards.pop()

    def count(self):
        return len(self.cards)