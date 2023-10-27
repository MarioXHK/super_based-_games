#include <allegro5/allegro.h>
#include <allegro5/allegro_primitives.h>
#include <iostream>
#include <complex>
#include <windows.h>
using namespace std;

int mandelbrot(complex<double> c);

const int WIDTH = 1200;
const int HEIGHT = 900;

int main() {
    al_init();
    al_init_primitives_addon();
    auto display = al_create_display(WIDTH, HEIGHT);

    complex<double> c;
    int num;

    
    for (int h = 1; h < 11; h++){
        al_lock_bitmap(al_get_target_bitmap(), al_get_display_format(display), al_get_display_flags(display));
        cout << "hi\n";
        for (double i = -2; i < 2; i += 0.01/h) {
            for (double j = -2; j < 2; j += 0.01/h) {
                c = complex<double>(i, j);
                num = mandelbrot(c);
                al_put_pixel(i * (100*h) + (400 + 100*h), j * (100*h) + (400 + 30*h), al_map_rgb(num*5, pow(num, num), (num*num)));
            }
        }

        al_unlock_bitmap(al_get_target_bitmap());
        al_flip_display();
    }
    system("pause");
    al_destroy_display(display);
}

int mandelbrot(complex<double> c) {
    complex<double> z = 0;
    int counter = 0;
    while (abs(z) < 2 && counter < 90) {
        z = (z * z) + c;
        counter++;
    }
    return counter;
}