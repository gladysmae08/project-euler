#include <iostream>
#include <vector>

int main(int argc, char** argv){
    long int sum_of_squares = 0;
    int sum = 0;
    for(int i = 1; i<=100; i++){    
        sum_of_squares += i*i;
        sum += i;
    }
    long int square_of_sum = sum * sum;
    std::cout << square_of_sum -sum_of_squares << std::endl;
    return 0;
}
    
