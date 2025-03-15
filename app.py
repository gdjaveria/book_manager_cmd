import json
import os

data_file = 'library.txt'


def load_library():
    if os.path.exists(data_file):
        with open(data_file,'r') as file:
            return json.load(file)
        return []
    
def save_library(library):
    with open (data_file , 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):

    title = input('enter the title of the book:')
    author = input ('enter the author of the book:')
    year = input ('enter the year of the book:')
    genre = input ('enter the genre of the book:')
    rating = input ('enter the rating of the book:')
    read = input ('Have you read the book? (yes/no):')

    new_book ={
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'rating': rating,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print('Book added successfully!')

def remove_book(library):
    title = input('enter the title of the book you want to remove:')
    intial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]

    if len(library) < intial_length:
        save_library(library)
        print(f'Book with title {title} removed successfully!')
    else:
        print(f'Book with title {title} not found!')

def search_book(library):
    search_by = input('Enter the search by title or author:').strip().lower()
    if search_by not in ['title', 'author']:
        print('Inavalid search option! please enter title or author')
        return
    search_term = input ('Enter the {search by}:').strip().lower()
    search_results = [book for book in library if search_term in book[search_by].lower()]

    if search_results:
        for book in search_results:
         print (f'title:{book ['title']}')
         print (f'author: {book["author"]}')
         print (f'year:{book ['year']}')
         print (f'genre:{book ['genre']}')
         print (f'read:{book ['read']}')
         print (f'status:{book ['status']}')
    else:
        print(f'No books found for the {search_term} in the {search_by} field')

def display_all_books(library):
    if library:
        for book in library:
            status = 'Read' if book['read'] == 'yes' else 'Not read'
            print(f'title: {book["title"]}') 
            print(f'author: {book["author"]}')
            print(f'year: {book["year"]}')
            print(f'genre: {book["genre"]}')
            print(f'read: {book["read"]}')
            print(f'status: {status}')
    else:
        print('library of books is empty!')

def display_statics(library):
    total_books = len (library)
    read_books =  sum(1 for book in library if book['read'] == 'yes')
    not_read_books = total_books - read_books
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'Read books: {read_books}')
    print(f'percentage read:{percentage_read:.2f}%')

def main():
    library = load_library()
    while True:
        print('Welcome to the library!📘📖')
        print('1. Add a book to the library')
        print('2. Remove a book from the library')
        print('3. Search for a book in the library')
        print('4. Display all books in the library')
        print('5. Display library statistics')
        print('6. Exit the library')
        choice = input('Enter your choice:').strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statics(library)
        elif choice == '6':
            print('Thank you for using the library Goodbye!')
            break
        else:
            print('Invalid chooice! please enter a right choice from the list')

if __name__ == '__main__':
    main()

   





         

    

    
    
   


    

