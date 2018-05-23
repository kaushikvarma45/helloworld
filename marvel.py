import random

while True:
 index1 = random.randint(0,12)
 index2 = random.randint(0,12)
 if index1 != index2 :#
     break
     #generates two indices for the 13 avengers

#print index1,index2
marvelchar = ['Captain America','Doctor strange','Thor','Hulk','Loki','Gamora','Nebula','Drax','ironman','spiderman','black widow','scarlet witch','black panther']
score = [7,9,14,8,6,5,4,6,10,7,5,12,7] #each avenger has a score based on their strength out of 15 and together it sums up to 100

sum = score[index1]+score[index2]
print 'initial sum is :', sum
print 'your default marvel characters are '+marvelchar[index1]+' and '+ marvelchar[index2]
print
if index1<index2 :
    del marvelchar[index1]
    del marvelchar[index2-1]
    del score[index1]            #delete the 2 characters which are already chosen by computer depending on index1 and index2
    del score[index2-1]
else :
    del marvelchar[index2]
    del marvelchar[index1-1]
    del score[index2]
    del score[index1-1]

i = 0
while i<11 :
    print (i+1),marvelchar[i]
    i=i+1

while True :
    input1 = int(raw_input('enter the index of your first character : '))
    input2 = int(raw_input('enter the index of your second character : '))
    if (input1<12 and input2<12 and input1!=input2) : # checks the input of user whether its valid or not
        break
    else :
        print 'your input is invalid please type again'


print "\n you have chosen "+marvelchar[input1-1]+' and '+marvelchar[input2-1]
sum = sum + score[input2-1]+score[input1-1]
print 'your total score out of 100(which is all characters together) is :',sum
