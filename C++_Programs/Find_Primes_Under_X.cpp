// Program that lets a user enter a number and then takes the user's number and
// prints all prime numbers that are less than that number.

#include <iostream>

int main() {
	int max_prime = 0;
	std::cout << "Enter an integer, all primes less than this number will be printed: ";
	std::cin >> max_prime;

	if (max_prime <= 1) { return 0; }
	if (max_prime >= 3) { std::cout << "2" << std::endl; }

	for (int a = 3; a < max_prime; a++) // a starts at 3 because the numbers 1 and 2 are by default prime numbers.
	{
		bool is_prime = true;
		for (int b = 2; b < a; b++)
		{
			if (a % b == 0)
			{
				is_prime = false;
				break;
			}
		}
		if (is_prime)
		{std::cout << a << std::endl;}
	} return 0;
}
