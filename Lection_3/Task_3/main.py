import os
# UI constants
solidBlock = "\u2501"

# UI functions
def border(block, size):
    print(block * size)
def clear_console():
  x = input("Enter to continue...")
  os.system('clear')

# Logs functions
def logInfo(*args):
    print("[Info] ", *args)
def logErro(text):
    print("[Erro] ", text)

# Input Info
def getInputStr(text):
    userInput = input(f"Enter {text}: ")
    return userInput
def getInputNum(text):
    userInput = int(input(f"Enter {text}: "))
    return userInput
def getInputArray(text):
    userInput = input(f"Enter {text}:")
    return userInput.split(",")
    
# BookCase functions
def genBookId(bookCase):
    bookId = 0
    while bookId in bookCase:
        bookId += 1
    return bookId

def bookInit(bookCase, bookName = "Example", bookAuthor = "Unknown", bookSheets = 0, bookGenres = [], bookCover = None):
    bookExample = {
                "bookName":bookName,
                "bookAuthor":bookAuthor,
                "bookSheets": bookSheets,
                "bookGenres": bookGenres,
                "bookCover": bookCover,
                }
    bookId = genBookId(bookCase)
    bookCase[bookId] = bookExample

def addBook(bookCase):
    logInfo("For to add book enter information about book: ")
    bookName = getInputStr("book name")
    bookAuthor = getInputStr("author name")
    bookSheets = getInputNum("sheets in book")
    bookGenres = getInputArray("genres of book by ','")
    bookCover = getInputStr("cover of book")
    newBook = bookInit(bookCase, bookName, bookAuthor, bookSheets, bookGenres, bookCover)

def delBook(bookCase, bookId = 0):
    bookCase.pop(bookId)
    logInfo("Book has been deleted!")

def editBook(bookCase, bookId):
    editing = 1
    while editing:
        if bookId in bookCase.keys():
            logInfo("""What's need edit?
        1. Name
        2. Author
        3. Sheets
        4. Genres
        5. Cover
        0. Nothing, I want leave!""")
            userAction = getInputNum("action")
            match userAction:
                case 1:
                    newName = getInputStr("new book name")
                    bookCase[bookId]["bookName"] = newName
                    clear_console()
                case 2:
                    newAuthor = getInputStr("new author")
                    bookCase[bookId]["bookAuthor"] = newAuthor
                    clear_console()
                case 3:
                    newSheets = getInputNum("new sheets")
                    bookCase[bookId]["bookSheets(number)"] = newSheets
                    clear_console()
                case 4:
                    newGenres = getInputArray("new genres(by ',')")
                    bookCase[bookId]["bookGenres"] = newGenres
                    clear_console()
                case 5:
                    newCover  = getInputStr("new cover")
                    bookCase[bookId]["bookCover"] = newCover
                    clear_console()
                case 0:
                    editing = 0
                case _:
                    logErro("I dont't know it command!")
        else:
            logErro("It's ID not in BookCase!")
            break

def showBookCase(bookCase):
    logInfo("All books in BookCase: ")
    for key in bookCase.keys():
        logInfo(f"""ID: {key}
Name:{bookCase[key]["bookName"]}
Author: {bookCase[key]["bookAuthor"]}
Sheets: {bookCase[key]["bookSheets"]}
Genres: {bookCase[key]["bookGenres"]}
Cover: {bookCase[key]["bookCover"]}""")
        border(solidBlock, 64)

def searchBook(bookCase, bookName):
    for key in bookCase.keys():
        if bookName in bookCase[key].values():
            logInfo(f"Book {bookName} is found!")
            logInfo(f"Book ID:{key}")
            logInfo(f"Book data:\n",bookCase[key])
        else:
            logErro(f"Book {bookName} not in BookCase!")

def choiceMenu(bookCase, userInput):
        match userInput:
            case 1:
                addBook(bookCase)
                clear_console()
            case 2:
                userBookId = getInputNum("book ID for delete")
                delBook(bookCase, userBookId)
                clear_console()
            case 3:
                userBookId = getInputNum("book ID for edit")
                editBook(bookCase, userBookId)
                clear_console()
            case 4:
                userBookName = getInputStr("book name for search")
                searchBook(bookCase, userBookName)
                clear_console()
            case 5:
                showBookCase(bookCase)
                clear_console()
            case 6:
                exit()
            case _:
                logErro("I dont't known this command!")
                clear_console()
# Main
myBooks = {}
bookInit(myBooks)
while True:

    border(solidBlock, 64)
    logInfo("Welcome to BookCase by DiachenkoRP!")
    border(solidBlock, 64)
    logInfo("""Action with BookCase:
    1. Add book
    2. Delete book
    3. Edit book
    4. Search book
    5. Show BookCase
    6. Exit""")
    border(solidBlock, 64)
    userInput = getInputNum("your choice")
    border(solidBlock, 64)
    
    choiceMenu(myBooks, userInput)


