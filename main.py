
def seq3np1(n):
    count = 0
    while(n != 1):
        count = count + 1
        if(n % 2) == 0:       
            n = n // 2
        else:                 
            n = n * 3 + 1
    print("Number of iterations: ", count)

def main():
  n = int(input("Enter upper bound: "))
  while n < 0:
    print("Please enter a positive number") 
    break

  for start in range(1, n+1):
    print("Current value: ", start)
    seq3np1(start)
    


  
main()
