// Thing program lets a user enter a number and then takes the user's number and
// checks for all prime numbers that are less than that number.

#include "stdafx.h"
#include <iostream>
		// Note: You could add "using namespace std;" here and delete all "std::"s from the program if desired.
int main() {
	int max_prime, x;
	std::cout << "Please enter the highest number you wish to find prime numbers under? ";
	std::cin >> max_prime;

	//This for loop goes through each number checking for prime numbers until it hits max_prime entered by the user.
	for (int a = 3; a < max_prime; a++) // a starts at 3 because the numbers 1 and 2 are by default prime numbers.
	{      
		x = 0;    //a variable to check if a number is prime. If it gets set to 1 the number is not prime.
		for (int b = 2; b < a; b++)
		{        
			if (a%b == 0) 
			{
				x = 1;
				break;
			}
		}
		if (x == 0)
		{        
			std::cout << a << " is a prime number.\n";
		}
	}
	char k;		// These two lines are in place so that when the program is finished
	std::cin >> k; // the user must press a key or close the console before the program finishes. (So that the user can read the output)
	return 0;
}
