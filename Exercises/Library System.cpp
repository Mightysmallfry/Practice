






#include <iostream>
#include <string>
#include <vector>
using namespace std;


//Highlights
//- An admin server for the librarians to add or handle library members and their records.
//- The booklist function displays the available books in the library.
//- A member server that shows a menu to which can request the admin server to rent books and also showcases the booklist and updates it.
//- A list of books that are already rented with their due dates, which only admins can edit.


//- get admin info or continue as guest



//- List available books, read always as guest


//- Sign in screen



string Name = b;
string Password = b;
bool isAdmin;

void main()
{
	userAccount User;

	User = login(User);


	while (true)
	{
		//- Menu
		cout << "===MENU===" << endl;
		cout << "<1> - Hug " << endl;
		cout << "<2> - Sit " << endl;
		cout << "ENTER NUM " << endl;
		int choice;
		cin >> choice;

		switch (choice)
		{
			case (choice == 1):
			//- List rented books, pass in admin value


				break;
			
			case (choice == 2):
			//- If admin show already rented booklist 


				break;
		}
	}

}





