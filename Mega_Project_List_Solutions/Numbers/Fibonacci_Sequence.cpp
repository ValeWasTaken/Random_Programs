#include <iostream>
using namespace std;

int main()
{
	int a = 0, b = 1, c = 0;
	int fib_num = 0, count = 0;
	std::cout << "Enter the place of the fibonacci number you want to find: ";
	std::cin >> fib_num;

	while (count < fib_num)
	{
		count++;
		c = a + b;
		std::cout << c << std::endl; // Remove this line to only see final number.
		a = b;
		b = c;
	}
	std::cout << "The value of the " << fib_num << " place in the Fibonacci Sequence is: " << c << "\n\n";
	return 0;
}
