def initialize_library():
    try:
        f = open("MLS.txt", "x")
        f.close()
        print("Library file created successfully!")

    except FileExistsError:
        print("Library file already exists!")

def write_initial_data():
    f = open("MLS.txt", "w")

    f.write("===== Welcome to the Mini Library System of Group 10 =====\n")
    f.write("Book No. 001 | Title: Clean Code | Author: Robert C. Martin\n")
    f.write("Book No. 002 | Title: Behind the Blue Sky | Author: Ineryss\n")
    f.write("Book No. 003 | Title: Don Quixote| Author: Miguel de Cervantes.\n")
    f.write("Book No. 004 | Title: Python Crash Course | Author: Eric Matthes \n")

    f.close()
    
    print("Initial data written successfully!\n")

initialize_library()
write_initial_data()

def append_data():
    try:
        f = open("MLS.txt", "a")
        print("\n===== Add New Book Entries =====\n")
        
        while True:
            book_no = input("Enter Book No.: ")
            title = input("Enter Book Title: ")
            author = input("Enter the Author: ")

            f.write(f"Book No. {book_no} | Title: {title} | Author: {author}\n")
            
            another = input("Do you want to add another book? (y/n): ")
            if another.lower() != 'y':
                break
        f.close()
        print("\nNew book entries added successfully!")
        
    except FileNotFoundError:
        print("\nLibrary file not found! Please initialize the library first.")

def read_library():
    try:
        f = open("MLS.txt", "r")
        lines = f.readlines()
        f.close()

        print("\n=== Library Contents ===\n")
        for line in lines:
            print(line.strip())
        
        print(f"\nTotal number of books: {len(lines) - 1}") 

    except FileNotFoundError:
        print("\nLibrary file not found! Please initialize the library first.")

def update_book():
    try:
        f = open("MLS.txt", "r")
        lines = f.readlines()
        f.close()

        print("\n===== CURRENT BOOK LIST =====\n")
        for line in lines:
            print(line.strip())

        book_no = input("\nEnter Book No. to update: ")

        found = False
        updated_lines = []

        for line in lines:
            if f"Book No. {book_no}" in line:
                new_title = input("Enter new book title: ")
                author = input("Enter the Author: ")
                updated_lines.append(f"Book No. {book_no} | Title: {new_title} | Author: {author}\n")
                found = True
            else:
                updated_lines.append(line)

        if found:
            f = open("MLS.txt", "w")
            f.writelines(updated_lines)
            f.close()
            print("\nBook updated successfully!")
        else:
            print("\nBook not found!")

    except FileNotFoundError:
        print("File not found.")

def search_book():
    try:
        f = open("MLS.txt", "r")
        keyword = input("\nEnter Book No. or Title to search: ")
        found = False

        print("\n===== SEARCH RESULT =====\n")

        for line in f:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
                print("Book not found! Search again. ")

        f.close()

    except FileNotFoundError:
        print("\nLibrary file not found! Please initialize the library first.")

def delete_book():
    try:
        f = open("MLS.txt", "r")
        lines = f.readlines()
        f.close()

        print("\n===== CURRENT BOOK LIST =====\n")

        for line in lines:
            print(line.strip())
            
        delete_book_no = input("\nEnter Book No. to delete: ")
        updated_lines = []
        found = False
        
        for line in lines:
            if f"Book No. {delete_book_no}" in line:
                updated_lines.append(line)
                
        else:
            found = True

        if found:
            f = open("MLS.txt", "w")
            f.writelines(updated_lines)
            f.close()
            print("\nBook deleted successfully!")

        else:
            print("\nBook not found!")
            
    except FileNotFoundError:
        print("\nLibrary file not found! Please initialize the library first.")

while True:

    print("\n===== MINI LIBRARY SYSTEM MENU =====\n")
    print("1. Add New Book")
    print("2. Read Library")
    print("3. Update Book")
    print("4. Search Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        append_data()
    
    elif choice == "2":
        read_library()

    elif choice == "3":
        update_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        delete_book()
    
    elif choice == "6":
        print("\nExiting Mini Library System...Bye.")
        break

    else:
        print("\nInvalid choice! Please try again.")