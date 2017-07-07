#include <stdio.h>
#include <math.h>
#include <time.h>
#include <vector>

int main(int argc, char** argv){
    clock_t t1,t2;
    t1 = clock();
    long int big_num = 600851475143;
    int limit = sqrt(big_num);
    std::vector<bool> primes(limit, true);
    // set 0 and 1 to false
    primes[0] = false;
    primes[1] = false;
    // siv through primes
    for(int i = 2; i < ceil(sqrt(primes.size())); i++){
        if (!primes[i]) continue;
        for(int j=2*i; j<primes.size(); j+=i){
            primes[j] = false;
        }
    }
    // iterate backwards till first prime factor is found
    for(unsigned i = primes.size()-1; i-- > 0;){
        if (primes[i] && big_num % i == 0){
            printf("%d\n", i);
            break;
        }
    }   
    t2 = clock();
    float seconds = ((float)t2 - (float)t1) / CLOCKS_PER_SEC;
    printf("time: %f\n", seconds);
    return 0;        
}
