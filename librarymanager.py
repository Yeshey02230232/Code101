books_list = []
authors_set= set()
books_dict={}
books_list.append("Python Programming")
authors_set.add ("John Smith")
books_dict["PythonProgrsmming"]="John Smith"

books_list.append("Data Structures and Algorithms")
authors_set.add ("Jane Doe")
books_dict["Data structures and algorithms"]="Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add ("Alice Johnson")
books_dict["Machine Learniing Basics"]="Alice Johnson"

search=input("Enter the Title of the books to search :")
if search in books_list:
    print(f"Book found!! Author:{books_dict[search]}")
else:
    print("The resource you have entered is not Found!!!")

print("list of books that we have in the Computer Resources:")
for books in books_list: 
    print(books)
remove_title=input("Enter the title of the book to remove or else enter to Skip!!!:")
if remove_title in books_list:
    remove_author= books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed Succesfully!!")
else:
    print("BOOK NOT FOUND!!")