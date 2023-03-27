import sys
from os import system, name
# UI code
uiBorder = '=' * 48

# Main code
print(uiBorder)
bookCase = {"ExampleBook":{"Author": "None", "Sheets": 0, "Genre": "None", "Cover": "None"}}
while True:
    print("Welcome to 'My Bookcase'!")
    print("""You have an opportunity: 
       1. Add book
       2. Delete book
       3. Edit book
       4. Search book
       0. Exit""")
    print(uiBorder)

    userAction = input("Your choice: _\b")



    match userAction:
        case "1":
            print(uiBorder)
            print("Book Add menu")
            print(uiBorder)
            bookName = input("Enter name of book: ")
            bookAuthor = input(f"Enter {bookName}'s Author: ")
            bookSheets = int(input(f"Enter {bookName} Sheets: "))
            bookGenre = input(f"Enter {bookName} Genre: ")
            bookCover = input(f"Enter {bookName} Cover(hard/soft): ")
            
            bookCase[bookName] = {"Author":bookAuthor, "Sheets":bookSheets, "Genre":bookGenre, "Cover":bookCover}
            print(bookCase)
            print("Book has been added!")
            print(uiBorder)
            # Clear screen
            userAction = input("Enter to continue...")
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            


        case "2":
            print(uiBorder)
            print("Book Delete menu")
            print(uiBorder)
            print("Your bookcase:\n", list(bookCase.keys()))
            bookName = input("Enter book that will deleted: ")
            if bookName in bookCase:
                bookCase.pop(bookName, "Book not exist!")
                print(f"{bookName} has been deleted!")
                 # Clear screen
                userAction = input("Enter to continue...")
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')
            else:
                print(f"{bookName} not in bookcase!")
                 # Clear screen
                userAction = input("Enter to continue...")
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')



        case "3":
            print(uiBorder)
            print("Book Editor menu")
            print(uiBorder)
            bookName = input("Enter name of book for edit: ")
            if bookName in bookCase:
                bookOptions = bookCase[bookName]
                bookOptions["Author"] = input(f"Enter {bookName}'s new Author: ")
                bookOptions["Sheets"] = input(f"Enter {bookName} edited Sheets: ")
                bookOptions["Genre"] = input(f"Enter {bookName} edited Genre: ")
                bookOptions["Cover"] = input(f"Enter {bookName} edited Cover: ")
                bookCase[bookName] = bookOptions
                print("Edit has been successful!")
                # Clear screen
                userAction = input("Enter to continue...")
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')
            else:
                print(f"{bookName} not in bookcase!")
                 # Clear screen
                userAction = input("Enter to continue...")
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')



        case "4":
            print(uiBorder)
            print("Book Search menu")
            print(uiBorder)
            bookName = input("Enter name of book for search: ")
            
            if bookName in bookCase:
                print(f"{bookName} found!")
                print(f"Out information about it book?")
                bookOptions = bookCase[bookName]
                userAction = input("Enter yes/no: ").lower()
                match userAction:
                    case "yes":
                        print(uiBorder)
                        print(f"""Info about '{bookName}'
    Author: {bookOptions["Author"]}
    Genre: {bookOptions["Genre"]}
    Cover: {bookOptions["Cover"]}
    Sheets: {bookOptions["Sheets"]}""")
                        # Clear screen
                        userAction = input("Enter to continue...")
                        if name == 'nt':
                            _ = system('cls')
                        else:
                            _ = system('clear')
                    case "no":
                        print("You choice no!")
                         # Clear screen
                        userAction = input("Enter to continue...")
                        if name == 'nt':
                            _ = system('cls')
                        else:
                            _ = system('clear')
                    case _:
                        print("Not correct choice!")
                     # Clear screen
                        userAction = input("Enter to continue...")
                        if name == 'nt':
                            _ = system('cls')
                        else:
                            _ = system('clear')
            else:
                print(f"{bookName} NOT found!")
                 # Clear screen
                userAction = input("Enter to continue...")
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')



        case "0":
            print("You are exiting...Bye!")
            sys.exit()
        case _:
            print("Not correct choice!")
             # Clear screen
            userAction = input("Enter to continue...")
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
