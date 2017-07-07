#include <string>
#include <iostream>
#include <chrono>

static bool isPalindrome(int const &num){
    std::string numstr = std::to_string(num);
    for(std::string::iterator i = numstr.begin(), j = numstr.end()-1; i <= j; i++,j--){
        if (*i != *j) return false;
    }
    return true;  
}

int main(int argc, char** argv){
    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();
    // loop through all 3 digit numbers
    int max_pal = 0;
    int product;
    for (int i=100; i<1000; i++){
        for (int j=i; j<1000; j++){
            product = i*j;
            if (product <= max_pal) continue;
            if (isPalindrome(product)){
                max_pal = product;
            }
        }
    }
    end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "max palindrome: " << max_pal << std::endl;
    std::cout << "elapsed time: " << elapsed_seconds.count() << std::endl; 
    return 0;
}
