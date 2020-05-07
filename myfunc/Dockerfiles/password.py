mport sys
password=sys.argv[1]
print ("password ="+password)
invpass=[]
import re
flag = 0
cnt=0
while (cnt<len(password)):
    if (len(password)<8):
        if 1 not in invpass:
            invpass.append(1)
        flag = -1

    if not re.search("[a-z]", password):
        if 2 not in invpass:
         invpass.append(2)
        flag = -1

    if not re.search("[A-Z]", password):
        if 3 not in invpass:
         invpass.append(3)
        flag = -1

    if not re.search("[0-9]", password):
        if 4 not in invpass:
         invpass.append(4)
        flag = -1
    if not re.search("[_@$]", password):
        if 5 not in invpass:
         invpass.append(5)
        flag = -1
    if re.search("\s", password):
        if 6 not in invpass:
         invpass.append(6)
        flag = -1
    cnt+=1
if flag==0:
    print ("Valid Password...")
else:
   print ("Not Valid Password - Below rules aren\'t met")
for j in invpass:
    if (j==1):
        print ("Not Enough Length")
    elif (j==2):
        print ("No Lower Case Characters")
    elif (j==3):
        print ("No Upper Case")
    elif (j==4):
        print ("No Digits Characters")
    elif (j==5):
        print("No special characters")
    else:
        print ("No Spaces Allowed")

