from shape_manager import *
from handlers import *

def main():
    shapes = ShapeManager()
    while True:
        print("Welcome to CRUD")
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_handle(shapes)

        elif choice == '2':
            show_shapes_handler(shapes)

        elif choice == '3':
            update_shape_handler(shapes)

        elif choice == '4':
            delete_shape_handler(shapes)

        elif choice == '5':
            print("Goodbye:)")
            break

        else:
            print("!!Not a valid option!!")
            continue

main()


