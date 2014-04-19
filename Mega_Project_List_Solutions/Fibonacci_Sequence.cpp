#include "stdafx.h" // For Visual Studio
#include <iostream>
using namespace std;

int main()
{
	int a = 0, b = 1, c = 0;
	int fib_num = 0, count = 0;
	cout << "Enter the place of the fibonacci number you want to find: ";
	cin >> fib_num;

	while (count < fib_num)
	{
		count++;
		c = a + b;
		cout << c << endl; // Remove this line to only see final number.
		a = b;
		b = c;
	}
	cout << "The value of the " << fib_num << " place in the Fibonacci Sequence is: " << c << "\n\n";

	system("pause");
	return 0;
}
