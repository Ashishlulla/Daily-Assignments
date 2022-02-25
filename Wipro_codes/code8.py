
class MovingTotal:
    lst_num = []

    def append(self,numbers):
        MovingTotal.lst_num += numbers
    
    def contains(self, total):
        for i in range(len(MovingTotal.lst_num)):
            for j in range(i+1):
                for k in range(j+1):
                    if i+j+k == total:
                        return True
                    else:
                        pass
        return False


movingtotal = MovingTotal()

movingtotal.contains([1,2,3,4])
print(movingtotal.contains(6))
print(movingtotal.contains(9))
print(movingtotal.contains(12))
print(movingtotal.contains(7))
