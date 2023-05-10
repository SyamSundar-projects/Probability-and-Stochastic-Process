
"""
Questioin:
A game consists of tossing a one rupee coin 3 times and noting its outcome each time.
Hanif wins if all the tosses give the same result i.e., three heads or three tails, 
and loses otherwise. Calculate the probability that Hanif win the game"""

#Intialization of variables
N=0 #Total possible cases counter
F=0 #Favourable cases counter
P=0 #The probability of Hanif winning(when all the threee tosses are same)

#code to compute the probability
for FirstToss in range(0,2,1):
  for SecondToss in range(0,2,1):
    for ThirdToss in range(0,2,1):
      N=N+1 #possible cases counting
      if(FirstToss==SecondToss and SecondToss==ThirdToss):
        F=F+1
P = F/N #The probability of Hanif winning

print("Total possible chances:",N)
print("Favourable cases:",F)
print("Probability of Hanif winning:",P)
