# STUDENT A -- "x" and "w"

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
    f.write("Book No. 001 | Title: Learn Computer Programing\n")
    f.write("Book No. 002 | Title: Behind the Blue Sky\n")
    f.write("Book No. 003 | Title: Data Structure and Algorithms\n")
    f.write("Book No. 004 | Title: The Art of Computer Programming\n")

    f.close()

    print("Initial data written successfully!\n")

initialize_library()
write_initial_data()

#STUDENT B -- "a" append mode
def append_data():
    try:
        f = open("MLS.txt", "a")
        print("\n===== Add New Book Entries =====")
        
        while True:
            book_no = input("Enter Book No.: ")
            title = input("Enter Book Title: ")

            f.write(f"Book No. {book_no} | Title: {title}")
            
            another = input("Do you want to add another book? (y/n): \n")
            if another.lower() != 'y':
                break
        f.close()
        print("New book entries added successfully!")
        
    except FileNotFoundError:
        print("\nLibrary file not found! Please initialize the library first.")
        
append_data()

#STUDENT C -- "r" and print a count of lines
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

read_library()

#STUDENT D -- update the file
