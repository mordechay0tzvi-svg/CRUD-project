from shape_manager import *
def menu():
    print("================")
    print("Add shape .1")
    print("Show all shapes .2")
    print("Update shape .3")
    print("Delete shape .4")
    print("Exit .5")

def main():
    sm = ShapeManager()
    while True:
        print("Welcome to CRUD")
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                type = input("Enter shape type to add: ")
                if type == "c":
                    new_shape = Circle(int(input("Enter radius: ")),sm.get_id())
                    sm.create_shape(new_shape)
                elif type == "s":
                    new_shape = Square(int(input("Enter side: ")),sm.get_id())
                    sm.create_shape(new_shape)
                elif type == "r":
                    new_shape = Rectangle(int(input("Enter length: ")), int(input("enter height: ")),sm.get_id())
                    sm.create_shape(new_shape)
                else:
                    print("Not an option")
            except ValueError:
                print("Must enter a number")

        elif choice == '2':
            for shape in sm.get_all_shapes():
                print(shape)

        elif choice == '3':
            try:
                id = int(input("Enter shape id: "))
                type = sm.find_type(id)
                if type is None :
                    print("!!Shape not found!!")
                info = {"circle":"radius", "square":"side"}
                if type in info.keys():
                    sm.update_shape(id, {info[type]:int(input(f"enter new{info[type]}"))})
                elif type == "rectangle":
                    sm.update_shape(id, {"height":int(input("enter length")), "length":int(input("enter height"))})
            except ValueError:
                print("=======\n Must be number \n========")

        elif choice == '4':
            try:
                sm.delete_shape(int(input("Enter id to delete")))
            except ValueError:
                print("!!Not a number!!")

        elif choice == '5':
            print("Goodbye:)")
            break

        else:
            print("!!Not a valid option!!")
            continue

main()



