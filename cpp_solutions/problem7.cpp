#include<iostream>
#include<chrono>
#include<cmath>
#include<cstring>

int main(int argc, char** argv){
    // start timer
    std::chrono::time_point<std::chrono::system_clock> start, end; 
    start = std::chrono::system_clock::now();
    // compute upper bound for nth prime
    const int n = 10001;
    const int size = ceil(n*log(n) + n*log(log(n)));
    bool* primes = new bool[size];
    memset(primes, true, size*sizeof(bool));
    // set 0 and 1 to false
    primes[0] = false;
    primes[1] = false;
    // sieve primes
    for(int i = 2; i<=(int)sqrt(size); i++){
        if (!primes[i]) continue;
        for(int j=i+i; j<size; j+=i)
            primes[j] = false;
    }
    // count to nth prime
    int prime_count = 0;
    for(int i=0; i<size; i++){
        if (primes[i]) prime_count++;
        if (prime_count == n){
            std::cout << i << std::endl;
            break;
        }
    }
    // delete array
    delete[]  primes;
    // stop timer
    end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "time: " << elapsed_seconds.count() << std::endl;   
    return 0;
}
