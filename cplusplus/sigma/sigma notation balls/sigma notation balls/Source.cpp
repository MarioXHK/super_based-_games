#include<iostream>
using namespace std;

int main() {
	cout << "Rembering... ah! Hello, World, is it?\n";
	for (int i = 0; i < 10; i++)
		cout << i << " ";
	cout << "Ye... it's coming back to me.....\nWhat's the alpha frequency of Pi?\n";
	string amog;
	cin >> amog;
	cout << amog << "? " << amog << "?! W- Oh it works! Ye! YodfisrtghiugfiuIUFAOIUSERGGRODS!\n";
	float n = 0;
	for (int i = 1; i <= 3; i++)
		n += (2 * i) - 1;
	cout << n << endl;
	cout << "I got it!\n";
	n = 0;
	for (int i = 1; i <= 5; i++)
		n += 3+2*(i-1);
	cout << n << endl;
	n = 0;
	for (int i = 1; i <= 5; i++)
		n += -5 + 9 * (i - 1);
	cout << n << endl;
	n = 0;
	for (int i = 1; i <= 5; i++)
		n += 20 - 17 * (i - 1);
	cout << n << endl;
	n = 0;
	for (int i = 1; i <= 5; i++)
		n += 2 + 0.4 * (i - 1);
	cout << n << "\nGod, I love and hate math...\n";
}