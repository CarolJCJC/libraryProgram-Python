import datetime

#####################################
#	Library Program             #
#	Name:Huang Jiachen          #
#####################################

# This function displays the introduction part of the main menu.
def display_main_intro():
	message = "-"*16 + " A Simple Library Program " + "-"*16
	print(message)

# This function displays the introduction part of the submenu.
def display_sub_intro():
	message = "-"*20 + " Lending Services " + "-"*20
	print(message)

# This function displays the separator between the menus.
def display_separator():
	lines = "-" * 58
	print(lines)

# This function displays the top level menu.
def display_main_menu():
	display_separator()
	print("1. Lending Services")
	print("2. Display All Books")
	print("3. Show Borrowing Records")
	print("4. Exit System")
	display_separator()

# This function displays the second level menu of lending.
def display_sub_menu():
	display_separator()
	print("1. Search a Book")
	print("2. Borrow a Book")
	print("3. Return a Book")
	print("4. Back to Main")
	display_separator()

# This function loads the book information from a file into a list.
# @param filename - the name of the input file
# @return - the list of books
def load_books(filename):
	infile = open(filename, "r")
	books_str = infile.read()
	infile.close() # Close the input file    
	books_list = books_str.split("\n")
	return books_list

# This function obtains the required attribute value of a book.
# @param item_list - the list contians the information of one book record. 
#		 option - 0 refers to the book code, 1 refers to the book title, 
#				  2 refers the upi status, and 3 refers to the due date.
# @return - the specific attribute value.
def get_attribute(item_list, option):
	if option == 0:
		attribute = item_list[0]
	elif option == 1:
		attribute = item_list[1]
	elif len(item_list) > 2 and option == 2:
		attribute = item_list[2]
	elif len(item_list) > 2 and option == 3:
		attribute = item_list[3]
	else:
		attribute = ""
	return attribute

# This function finds a book record from the list of books based on a given attribute value.
# @param books_list - the list of books. 
#		 option - 0 refers to the book code, 1 refers to the book title, 
#				  2 refers the upi status, and 3 refers to the due date.
#		 value - the value of the attribute to be found.
# @return - the index of the matching book record inside the list of books; 
#			it returns -1, if not found.
def find_book(books_list, option, value):
	index = 0
	found = False
	while not found and index < len(books_list):
		item = books_list[index]
		item_list = item.split(",")
		attribute = get_attribute(item_list, option)
		if attribute == value:
			found = True
		index = index +1
	if found:
		return index-1
	else:
		return -1

# This function obtains a valid book code from the user input. If an invalid code was
# provided, the function will continue asking for a valid book code until it gets one.
# @param books_list - the list of books.
# @return - the index of the matching book item inside the list of books.
def input_code(books_list):
	code = input("Enter book code: ")
	index = find_book(books_list, 0, code)
	while index == -1:
		print("Invalid book code.")
		code = input("Please try again: ")
		index = find_book(books_list, 0, code)
	return index

# This function calculates the due date of a borrowing, based on today's date plus 4 weeks (28 days).
# @return - the due date in a string of the format dd/mm/yyyy.
def get_due_date():
	duedate = datetime.date.today()+datetime.timedelta(days=28)
	date = duedate.strftime("%d/%m/%Y")
	return date

# This function changes upi status and date fields of a book record.
# @param books_list - the list of books.
#		 index - the index of the book record.
#		 upi - UPI of the borrower; if not borrowed, it stores "".
#		 date - return date of the borrowing; if not borrowed, it stores "".
def update_status(books_list, index, upi, date):
	item = books_list[index]
	item_list = item.split(",")
	new_item = item_list[0]+","+item_list[1]
	if (len(item_list) <= 2 and upi!=""):
		new_item =  new_item + "," + upi + ","+date
	books_list[index] = new_item

# This function obtains a valid menu option from the user input. If an invalid option was
# provided, the function will continue asking for a valid menu index until it gets one.
# @param start - the start value of the menu index.
#		 end - the end value of the menu index.
# @return - the menu index value.
def get_user_input(start,end):
	choice = int(input("Enter your choice: "))
	while (choice >end or choice < start):
		print("Invalid menu option.")
		choice = int(input("Please try again: "))
	return choice

# This function manages the top level menu.
def main_menu(books_list):
	display_main_menu()
	option = get_user_input(1,4)
	while option != 4:
		if option == 1:
			sub_menu(books_list)
			display_main_menu()
		elif option == 2:
			display_books(books_list)
		else:
			display_borrowing(books_list)
		option = get_user_input(1,4)
	print("Thank you for reading with us.")

# This function manages the second level menu on lending.
def sub_menu(books_list):
	display_sub_menu()
	option = get_user_input(1,4)
	while option != 4:
		if option == 1:
			search_book(books_list)
		elif option == 2:
			borrow_book(books_list)
		else:
			return_book(books_list)
		option = get_user_input(1,4)
	print("Back to main menu.")

# This function displays one book record in the required format.
def display_a_book(book):
	item_list = book.split(",")
	print("Code: " + item_list[0])
	print("Title: " + item_list[1])
	if len(item_list) > 2:
		print("Status: On Loan")
		print("Return Date: "+item_list[3])
	else:
		print("Status: Available")

# This is the main function of the libray system.
def main():
	books_list = load_books("books.txt")
	display_separator()
	display_main_intro()
	main_menu(books_list)
	display_separator()
	save_books(books_list, "books2.txt")

#################################################################################################
# The implementation of the above functions have already been given.                            #
# Please DO NOT MODIFY the content of the ABOVE functions, as they are used by other functions. #
# Please given the implementation of the following six functions to complete the program.       #
#################################################################################################

# This function displays all the books in the collection.
def display_books(books_list):
	display_separator()
	print("List of books in collection")
	display_separator()
	for i in range(0,len(books_list)):
		display_a_book(books_list[i])
		print("*" * 24)
	display_separator()


# This function processes the searching of a book based on an input book title.	
def search_book(books_list):
	title = input("Enter the book title to search: ")
	index = find_book(books_list,1,title)
	if index != -1:
		print("Record found in the collection: ")
		display_a_book(books_list[index])
	else:
		print("Sorry, this book is not in the collection.")
	display_separator()

# This function processes the borrowing of a book based on the input book code.
def borrow_book(books_list):
	index = input_code(books_list)
	item_list = books_list[index]
	item = item_list.split(",")
	if len(item) > 2:
		print("Sorry, the book " + "'" + str(item[1]) + "'" + " is on loan.")
		print("It will be returned by " + str(item[3]) + ".")
	else:
		print("The book - " + "'" + str(item[1]) + "'" + " is available.")
		upi = input("Enter the UPI to borrow: ")
		date = get_due_date()
		update_status(books_list, index, upi, date)
		print("The book - " + "'" + str(item[0]) + "'" + " is borrowed by " + str(upi) + ".")
		print("Due date for returning the book is : " + str(date))
	display_separator()
	
	
# This function processes the returning of a book based on the input book code.
def return_book(books_list):
	index = input_code(books_list)
	item_list = books_list[index]
	item = item_list.split(",")
	if len(item) > 2:
		print("Thank you for returning the book - " + "'" + str(item[1]) + "'" + ".")
	else:
		print("The book - " + "'" + str(item[1]) + "'" + " has not been  borrowed.")
	date = get_due_date()
	display_separator()
	
	
# This function displays the borrowing records based on an input UPI.
def display_borrowing(books_list):
	upi = input("Enter the UPI to retrieve: ")
	numbers_of_borrows = 0
	for i in range(0,len(books_list)):
		item_list = books_list[i]
		item_list = item_list.split(",")
		if len(item_list) > 2:
			if upi == item_list[2]:
				display_a_book(books_list[i])
				print("*" * 24)
				numbers_of_borrows = numbers_of_borrows + 1
	if numbers_of_borrows < 1:
		print("There is no record of books borrowed by " + str(upi) + ".")
	else:
		print("There are " + str(numbers_of_borrows) + " books borrowed by " + str(upi) + ".")
	display_separator()

# This function saves all the book records into a file.
# @param books_list - the list of books.
# 		 filename - the name of the file to be saved into.
def save_books(books_list, filename):
	outfile = open(filename,"w")
	content = books_list[0]
	for item in range(1,len(books_list)):
		content = content + "\n" + books_list[item]
	outfile.write(content)
	outfile.close()
	
	


main()
