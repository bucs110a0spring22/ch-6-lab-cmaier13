
def seq3np1(n):
    count = 0
    while(n != 1):
        count = count + 1
        if(n % 2) == 0:        
            n = n // 2
        else:               
            n = n * 3 + 1
    return count              

seq3np1(2)


def main():
  n = int(input("enter an upper bound: "))

  while n > 0:
    seq3np1(n)
    if n < 0:
      print("end program")
      break 

  for start in range(1, (n + 1)):
    print(start)
    currentstart = seq3np1(start)
    print(currentstart)
    
  

main()
