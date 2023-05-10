""""
Questioin:
A game consists of tossing a one rupee coin 3 times and noting its outcome each time.
Hanif wins if all the tosses give the same result i.e., three heads or three tails, 
and loses otherwise. Calculate the probability that Hanif wil"""

#Intialization of variables
N=0 #Total possible cases counter
F=0 #Favourable cases counter
P=0 #The probability of Hanif winning(when all the threee tosses are same)


A=0 # possible outcomes for getting same face on all the 

#code to compute the probability
toss1={}
toss1["Head"]=1;
toss1["Tail"]=1;

toss2={}
toss2["Head"]=1;
toss2["Tail"]=1;

toss3={}
toss3["Head"]=1;
toss3["Tail"]=1;

for key in toss1:
    if key in toss2 and key in toss3:
        A=A+1
F=len(toss1)*len(toss2)*len(toss3)-A
N=len(toss1)*len(toss2)*len(toss3)
        
P = F/N #The probability of Hanif winning

print("Total possible chances:",N)
print("Favourable cases:",F)
print("Probability of Hanif winning:",P)

