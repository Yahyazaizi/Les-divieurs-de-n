N = int (input("Veuillez saisir la valeur de N : "))
while N <= 0:
     N = int(input("Veuillez saisir la valeur de N: "))
print("Les divieurs de ",N," sont")
for i in range(1, N+1):
   if (N % i == 0):
      print(i)