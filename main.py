import turtle 

def seq3np1(n):
    count = 0
    while(n != 1):
        count = count + 1
        if(n % 2) == 0:       
            n = n // 2
        else:                 
            n = n * 3 + 1
    print("Number of iterations: ", count)

graphy = turtle.Turtle()
data = turtle.Turtle()

def lineGraph(myturtle=None, n=None):
  graphy = turtle.Turtle()
  data = turtle.Turtle()
  wn = turtle.Screen()
  turtle.setworldcoordinates(0,0,10,10)
  max_so_far = 0

  for i in range(1, n+1):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result
      set.worldcoordinates(0,0, i+10, max_so_far + 10)
      data.goto(0, max_so_far)
      data.write(str("Maximum so far: ", i, max_so_far), True, align="center")
    else: 
      max_so_far = max_so_far 
    return max_so_far



def main():
  n = int(input("Enter upper bound: "))
  while n < 0:
    print("Please enter a positive number") 
    break

  for start in range(1, n+1):
    print("Current value: ", start)
    seq3np1(start)

  lineGraph(graphy, n)
  

  
main()
