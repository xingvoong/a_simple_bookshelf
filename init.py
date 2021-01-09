'''
My bookshelf
'''
from __future__ import division
import sqlite3 as sql


def connect():
    global db, cursor
    db = sql.connect('bookshelf.db')
    cursor = db.cursor()


def close():
    try:
        cursor.close()
        db.commit()
        db.close()
    except:
        print('Can not close')
        raise


def create_tables():

    db.execute('''CREATE TABLE IF NOT EXISTS books
             ([Name] text PRIMARY KEY , [Author] text, [Finish] text,
             [Genre1] text, [Genre2] text, [Genre3] text,
             [End_Date] text, [Rating] int, [Comment] text)''')


def insert_book(Name, Author, Finish, Genre1, Genre2,
                Genre3, End_Date, Rating, Comment):
    query = '''
    insert into books
    (Name, Author, Finish, Genre1, Genre2, Genre3, End_Date, Rating, Comment)
    values (?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    cursor.execute(query, (Name, Author, Finish, Genre1, Genre2,
                           Genre3, End_Date, Rating, Comment))
    db.commit()
    return True


def list_books():
    all_books = cursor.execute('select Name from books')
    if all_books:
        for book in cursor.fetchall():
            print(book)
    else:
        print('you have no books on the shelf :(')


def list_authors():
    all_authors = cursor.execute('select Author from books')
    if all_authors:
        for a in cursor.fetchall():
            print(a)
    else:
        print('you have no books on the shelf :(')


def top_5_rating_books():
    cursor.execute('select * from books order by Rating DESC limit 5')
    count = 1
    for book in cursor:
        print(count)
        count += 1
        print(book)
        print()


def read_command():
    print('what would you like to do with your bookshelf?')
    print('type: insert a book, list all books, list all authors')
    print('or top 5 rating books, exit')
    command = input()
    if command == 'insert a book':
        name = input("book name: ")
        author = input("author: ")
        finish = input("finish: ")
        genre1 = input("genre1: ")
        genre2 = input("genre2: ")
        genre3 = input("genre3: ")
        end_date = input("end date: ")
        rating = int(input("rating: "))
        comment = input("comment: ")
        insert_success = insert_book(name, author, finish, genre1, genre2,
                                     genre3, end_date, rating, comment)
        if insert_success:
            print('you just put a read book in your bookshelf. Yay!')

    elif command == 'list all books':
        list_books()
    elif command == 'list all authors':
        list_authors()
    elif command == 'top 5 rating books':
        top_5_rating_books()
    elif command == 'exit':
        close()
        print("see you next time, go read more!")
        exit()
    else:
        print('Sorry, I do not support this command :( ')
    next_command = input("would you like to continue, yes, no? ")
    if next_command == 'yes':
        read_command()
    else:
        print('see you next time')
        exit()


if __name__ == "__main__":
    connect()
    create_tables()
    read_command()
