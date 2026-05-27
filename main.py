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
        choice = input("enter your choice: ")
        if choice == '1':
            try:
                type = input("enter shape type to add: ")
                if type == "c":
                    new_shape = Circle(int(input("enter radius: ")))
                    Shape.count -= 1
                    sm.create_shape(new_shape)
                elif type == "s":
                    new_shape = Square(int(input("enter side: ")))
                    Shape.count -= 1
                    sm.create_shape(new_shape)
                elif type == "r":
                    new_shape = Rectangle(int(input("enter length: ")), int(input("enter height: ")))
                    Shape.count -= 1
                    sm.create_shape(new_shape)
                else:
                    print("not an option")
            except ValueError:
                print("must enter a number")
        elif choice == '2':
            for shape in sm.get_all_shapes():
                print(shape.to_dict())
        elif choice == '3':
            try:
                id = int(input("enter shape id: "))
                type = sm.find_type(id)
                if type is None :
                    print("shape not found")
                info = {"circle":"radius", "square":"side"}
                if type in info.keys():
                    sm.update_shape(id, {info[type]:int(input(f"enter new{info[type]}"))})
                elif type == "rectangle":
                    sm.update_shape(id, {"length":int(input("enter height")), "height":int(input("enter length")) })
            except ValueError:
                print("must be number")
        elif choice == '4':
            try:
                sm.delete_shape(int(input("enter id to delete")))
            except ValueError:
                print("not a number")
        elif choice == '5':
            print("Goodbye:)")
            break
        else:
            print("not a valid option")
            continue

main()



