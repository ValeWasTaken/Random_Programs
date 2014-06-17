#include <iostream>
using namespace std;

int main()
{
    double cost = 0;
    cout << "Enter cost of item: ";
    cin >> cost;
    double total = (cost * 1.06); // The current tax rate here is 6%.
    cout << "The total price with tax is: $" << total << "\n\n";
    return 0;
}
