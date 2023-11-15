#include <iostream>
using namespace std;

string nyantaco[20];
int maxred = 9;
int curred = 0;
int maxblue = 19;
int curblue = 10;
void pop(char color);
void append(char color, string thing);
string give(char color);


int main()
{
    cout << "You are finally here, let's play with some stacks.\n";
    char colorchoice = '3';
    char youknow;
    string appending;
    while (colorchoice != 'q') {
        cout << "Pick of the 2 color stacks, r for red, or b for blue. (Or you can quit with q)\n";
        cin >> colorchoice;
        if (colorchoice != 'q') {
            cout << "What do you wanna do with your color?\na: show what's on top, b: append something to the top, c: pop the top one.\n";
            cin >> youknow;
            if (youknow == 'a')
                cout << give(colorchoice) << endl;
            else if (youknow == 'b') {
                cout << "What do you want to append?\n";
                cin >> appending;
                append(colorchoice, appending);
            }
            else if (youknow == 'c')
                pop(colorchoice);
        }
    }
}

void pop(char color) {
    if (color == 'r') {
        if (curred == -1)
            cout << "There's no more reds.\n";
        else {
            nyantaco[curred] = "";
            curred--;
        }
    }
    else {
        if (curblue == 9)
            cout << "There's no more blues.\n";
        else {
            nyantaco[curblue] = "";
            curblue--;
        }
    }
}
void append(char color, string thing) {
    if (color == 'r') {
        if (curred == 9)
            cout << "The red stack is full.\n";
        else {
            curred++; 
            nyantaco[curred] = thing;
        }
    }
    else {
        if (curblue == 19)
            cout << "The blue stack is full.\n";
        else {
            curblue++; 
            nyantaco[curblue] = thing;
        }
    }
}
string give(char color) {
    if (color == 'r') {
        if (curred == -1) {
            cout << "There's no more reds.\n";
            return "";
        }
        else
            return nyantaco[curred];
    }
    else {
        if (curblue == 9) {
            cout << "There's no more blues.\n";
            return "";
        }
        else 
            return nyantaco[curblue];
    }
}