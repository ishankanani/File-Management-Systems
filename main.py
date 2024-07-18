#File Management tool ~ ISHAN KANANI

import os 

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"FileName {filename}: Created Successfully !!")
    except FileExistsError:
        print(f"File name {filename} is already exists")

    except Exception as E:
        print("An error occurred !")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files in dictrory :")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print("File name does't exits")
    except Exception as e:
        print("An error eccurred!")

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input('Enter data to add :')
            f.write(content+"\n")
            print("Content added to {filename} successfully!")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occuured!")


def main():
    while True:
        print("FILE MANAGEMENT TOOL")
        print('1.Create File')
        print('2.View All Files')
        print('3.Delete file')
        print('4.Read Files')
        print('5.Edit Files')
        print('6.Exits')

        choice = input("Enter the choice [1-6] :-")

        if choice == '1':
            filename = input('Enter the fike-name to create =')
            create_file(filename)

        elif choice == '2':
            view_all_files()
        
        elif choice == '3':
            filename = input("Enter the name of fike you want to delete :-")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter file name to read :-")
            read_file(filename)
        
        elif choice == '5':
            filename = input("Enter the name of file :-")
            edit_file(filename)

        elif choice == '6':
            print("Closing the Tool........")
            break

        else:
            print("Invaild input")

if __name__ == "__main__":
    main()
