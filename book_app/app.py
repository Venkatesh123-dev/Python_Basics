

import csv


def list_books():
    #import pdb;pdb.set_trace()
    # Opens the file in reading and writing mode
    with open('books.csv', mode='r+') as f:
        rows = csv.DictReader(f)

        for row in rows:
            #import pdb;pdb.set_trace()
            print("\n")
            print("Book Name :: " + row["BookName"])
            print("Author :: " + row["Author"])
            print("Read :: " + row["Read"])
            print("SharedWith :: " + row["SharedWith"])


def update_book():
    # 5.1
    book_name = input("Enter book name ::")

    # 5.2
    is_book_read = input("Book Read (Y/N)?")

    if is_book_read == "Y":
        is_book_read = True

    elif is_book_read == "N":
        is_book_read = False

    # 5.3
    import csv
    rows = []

    # Opens the file in reading and writing mode
    with open('books.csv', mode='r') as f:
        rows = list(csv.DictReader(f))

        # 5.4
        for row in rows:
            if row["BookName"] == book_name:
                row["Read"] = is_book_read
                break

    with open('books.csv', mode='w') as f:
        csv_writer = csv.DictWriter(
            f, fieldnames=["BookName", "Author", "Read", "SharedWith"])
        csv_writer.writerows(rows)

    print("Book Successfully Updated")


def add_book():
    # 4.1
    book_name = input("Enter book name")
    author = input("Enter Author name")


    with open('books.csv', mode='a') as f:
        fieldnames = ['BookName', 'Author', 'Read','SharedWith']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'BookName': book_name, 'Author': author})
    print("YOU WANT ADD MORE BOOKs")
    print("YES" '\n' "NO")
    choice = input("Enter your option ::")
    if choice == "YES":
        add_book()

    print("Book Successfully Added")
  





def share_book():
    print("Please  select  where you want share the  book '\n' 1.Facebook '\n' 2. Twitter '\n' 3.Instagram .")
    choice = int(input("Enter a provide options:"))
    if choice == 1:
        Facebook()

    if choice == 2:
        Twitter()

    if choice == 3:
        Instagram()

        


def status():
    book_name = input("Enter book name ::")

    # 5.2
    is_book_read = input("Book Read (Y/N)?")

    if is_book_read == "Y":
        is_book_read = True
        print("Please enter your user_name:")
        print("Please enter your password:")
        print("Book Shared  Successfully")

    elif is_book_read == "N":
        is_book_read = False
        print("Try after some time")


def Facebook():
    status()

def Twitter():
    status()

def Instagram():
    status()






print("Menu ::")
print("1. Add Book")
print("2. Update Book")
print("3. Share Book")
print("4. List Book")


choice = int(input("Enter your option ::"))

if choice == 1:
    add_book()

elif choice == 2:
    update_book()

elif choice == 3:
    share_book()

elif choice == 4:
    list_books()
