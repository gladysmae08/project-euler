#include <iostream>

int main(int argc, char** argv){
    int sum = 0;
    int last = 1;
    int current = 2;
    int next;
    while (current < 4000000) {
        if (current%2 == 0){
            sum += current;
        }
        next = current + last;
        last = current;
        current = next;
    }
    std::cout << sum << std::endl;
}
        
