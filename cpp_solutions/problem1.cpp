#include <iostream>

int main(int argc, char** argv){
    int sum = 0;
    for(int i = 1; i < 1000; i++){
        if(i % 3 == 0 or i % 5 == 0){
            sum += i;
        }
    }
    std::cout << "sum: " << sum << std::endl;
}    
    
