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
    shape_list = sm.get_all_shapes().copy()
    while True:
        print("Welcome to CRUD")
        menu()
        choice = input("enter your choice: ")
        if choice == '1':
            type = input("enter shape type to add: ")
            if type == "circle":
                new_shape = Circle(int(input("enter radius: ")))
                sm.create_shape(new_shape)
            elif type == "square":
                new_shape = Square(int(input("enter side: ")))
                sm.create_shape(new_shape)
            elif type == "rectangle":
                new_shape = Rectangle(int(input("enter length: ")), int(input("enter height: ")))
                sm.create_shape(new_shape)
            else:
                print("not an option")
        elif choice == '2':
            for shape in shape_list:
                print(shape.to_dict())
        elif choice == '3':
            try:
                id = int(input("enter shape id: "))
                for shape in shape_list:
                    if shape.shape_id == id:
                        if shape.shape_type == "circle":
                            shape.radius = int(input("enter radius: "))
                        elif shape.shape_type == "square":
                            shape.side = int(input("enter side: "))
                        elif shape.shape_type == "rectangle":
                            shape.length, shape.height = int(input("enter length")), int(input("enter height"))
                        else:
                            print("shape not found")
            except TypeError:
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
