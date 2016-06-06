from itertools import permutations


digits = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

class permutator():
    def __init__(self, digits):
        self.digits = digits

    def next_permutation(self):
        '''generate the next permutation of input items list'''
        index = -1
        # find swap index
        while(True):
            if self.digits[index - 1] < self.digits[index]:
                break
            index -= 1
            if(abs(index-1) > len(self.digits)):
                return False

        # find next biggest number
        temp = self.digits[index-1]
        for i in range(-1, index-1, -1):
            if self.digits[i] > temp:
                # swap digits
                self.digits[index-1] = self.digits[i]
                self.digits[i] = temp
                break

        # sort end of list
        self.partial_sort(index)
        return True


    def partial_sort(self, index):
         '''sort digits list from index to end'''
         temp_list = self.digits[index:]
         temp_list.sort()
         self.digits = self.digits[:index] + temp_list
         
#myPerm = permutator(digits)
#print(myPerm.digits)
#while myPerm.next_permutation(): print(myPerm.digits)
#count = 1
#for i in permutations(digits):
#    count += 1
#    if count == 999999:
#        print(i)
#        break




