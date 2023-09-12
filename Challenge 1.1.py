# 1.1 lmplement a recursive function to calculate the factorial of a given number


def fact_name(n):
  If n==0 or n==1:
  return 1
else:
return n * fact_name(n-1) 


number=2
res=fact_name(number)

print("the factorial of {}is{}.".format(number,res))

  