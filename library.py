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
