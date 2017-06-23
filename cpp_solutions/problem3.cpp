#include <stdio.h>
#include <math.h>
#include <vector>

int main(int argc, char** argv){
    int limit = sqrt(600851475143);
    std::vector<bool> primes(limit, true);
    
    printf("limit = %d\n", limit); 
}
