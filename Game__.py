import random
n = random.randint(1,100)
a = -1
gusses = 0

while(a != n):

   gusses  +=1

   a  = int(input("Guess the number"))

   if(a >n):

      print("Lower number please")

      gusses +=1
   elif(a<n):
      print("Higher number please")
      gusses +=1
print(f"You have gussed the numbwr {n} correctly in {gusses} attemps")




