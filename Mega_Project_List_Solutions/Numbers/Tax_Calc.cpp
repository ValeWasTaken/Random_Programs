#include <iostream>

int main()
{
    double cost = 0;
    std::cout << "Enter cost of item: ";
    std::cin >> cost;
    double total = (cost * 1.06); // The current tax rate here is 6%.
    std::cout << "The total price with tax is: $" << total << "\n\n";
    return 0;
}
