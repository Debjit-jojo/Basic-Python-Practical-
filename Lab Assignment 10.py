# Book Management System

books = [
    {"title": "Python Basics", "author": "Amit", "publisher": "TechPress", "price": 300, "year": 2020},
    {"title": "Data Science", "author": "Ravi", "publisher": "EduWorld", "price": 500, "year": 2022},
    {"title": "AI Guide", "author": "Amit", "publisher": "TechPress", "price": 800, "year": 2023},
    {"title": "C Programming", "author": "Suresh", "publisher": "CodeHouse", "price": 200, "year": 2018},
    {"title": "Web Dev", "author": "Ravi", "publisher": "EduWorld", "price": 450, "year": 2021}
]

# a) Print complete report in tabular form
print("\n--- Complete Book Report ---")
print("Title\t\tAuthor\tPublisher\tPrice\tYear")
for b in books:
    print(f"{b['title']}\t{b['author']}\t{b['publisher']}\t{b['price']}\t{b['year']}")

# b) Books by a given author
author_name = input("\nEnter author name: ")
print(f"\nBooks by {author_name}:")
for b in books:
    if b["author"].lower() == author_name.lower():
        print(b["title"])

# c) Books by a given publisher
publisher_name = input("\nEnter publisher name: ")
print(f"\nBooks by {publisher_name}:")
for b in books:
    if b["publisher"].lower() == publisher_name.lower():
        print(b["title"])

# d) Cheapest and costliest book
cheapest = min(books, key=lambda x: x["price"])
costliest = max(books, key=lambda x: x["price"])

print("\nCheapest Book:", cheapest["title"], "-", cheapest["price"])
print("Costliest Book:", costliest["title"], "-", costliest["price"])

# e) Sort by year of publication
sorted_books = sorted(books, key=lambda x: x["year"])

print("\nBooks sorted by year:")
for b in sorted_books:
    print(b["title"], "-", b["year"])


#2 

# Information about 5 states

states = [
    {"name": "Maharashtra", "area": 307713, "capital": "Mumbai"},
    {"name": "Gujarat", "area": 196024, "capital": "Gandhinagar"},
    {"name": "Rajasthan", "area": 342239, "capital": "Jaipur"},
    {"name": "Karnataka", "area": 191791, "capital": "Bengaluru"},
    {"name": "Tamil Nadu", "area": 130058, "capital": "Chennai"}
]

print("\n--- State Information Table ---")
print("Name\t\tArea (sq km)\tCapital")

for s in states:
    print(f"{s['name']}\t{s['area']}\t{s['capital']}")