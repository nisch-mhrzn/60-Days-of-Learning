import os
def create_file(filename):
    try:
        with open(filename,'x')as f:
            print("File created successfully")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("An error occured")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files in the directory")
    else:
        print('files in directory : \n')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File has been deleted")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

def read_file(filename):
    try:
        with open('sample.txt','r' ) as f:
            content = f.read() 
            print(f"content of {filename}:{content}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")
        
def edit_file(filename):
    try:
        with open('smaple.txt','a') as f:
            content = input("enter data to add = ")
            f.write(content + "\n")
            print(f"content added to {filename}")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")
        
def main():
    while True:
        print("\n File management file")
        print("1. Create a file")
        print('2.View all files')
        print('3.Delete a file')
        print('4.Read a file')
        print('5.Edit a file')
        print('6.Exit')
        
        choice = input("enter your choice (1-6) = ")
        if choice =='1':
            filename =input('enter the filename to create: ')
            create_file(filename)
        elif choice =='2':
            view_all_files()
        elif choice =='3':
            filename = input('enter the filename to delete: ')
            delete_file(filename)
        elif choice =='4':
            filename = input('enter the filename to read: ')
            read_file(filename)
        elif choice =='5':
            filename = input('enter the filename to edit: ')
            edit_file(filename)
        elif choice =='6':
            print("Thank you")
            break
        else:
            print('Invalid Syntax')

if __name__ == "__main__":
    main()