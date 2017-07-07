#include <iostream>
#include <functional>
#include <numeric>
#include <vector>

int main(int argc, char** argv){
    // greatest prime factors 1-20
    // 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
    std::vector<int> primes = { 2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19 };    
    int product = std::accumulate(std::begin(primes), std::end(primes), 1, std::multiplies<int>());
    std::cout << product << std::endl;
    return 0;
}
