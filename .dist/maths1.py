#Write a program in Python to solve the homogenous system Ax=0 and write the general solution in parametric vector form.

#Your program should accept as input the size of the matrix, i.e. the number of rows and the number of columns of A, and also the entries of A.

#The input should ideally be read from a text file, but if you haven't learnt how to do this, you may hard-code your input, as long as you are able to explain to your TA how to change the input to your program.

#Your code should be based on algorithms learned in the course. No pre-existing routines from Python libraries should be used.

#Demos of your code will be conducted.
f1=open(r"C:\Users\adity\OneDrive\Documents\maths_file.txt","r")
g=f1.readlines()
i=0
list1=(g[0].replace("\n","")).split(" ")
r=int(list1[0])
c=int(list1[1])
#print(r,c)
list2=[]
i=1
while i<len(g):
    list3=g[i].replace("\n","").split(" ")
    list2.append(list3)
    i+=1
#print(list2)
def funswapROWS(n,i,list2):
    flag=True
    while flag:
        if float(list2[n][i])==0:
            f=n+1
            while f<r:
                count1=0
                if float(list2[f][i])!=0:
                    g=list2[n]
                    list2[n]=list2[f]
                    list2[f]=g
                    count1+=1
                    break
                f+=1
            if count1==0:
                flag=False
                i+=1
                try:
                    scaling_ROWS1(n,i,list2)
                except:
                    IndexError
        else:
            flag=False
def scaling_ROWS1(n,i,list2):
    if float(list2[n][i])!=0:
        j=n+1
        while j<r:
            s=float(list2[j][i])/float(list2[n][i])
            t=i
            while t<c:
                list2[j][t]=str(((float(list2[j][t])-s*float(list2[n][t]))))
                t+=1
            j+=1
def scaling_ROWS(n,i,list2):
    if float(list2[n][i])!=0:
        j=n+1
        while j<r:
            s=float(list2[j][i])/float(list2[n][i])
            t=i
            while t<c:
                list2[j][t]=str(((float(list2[j][t])-s*float(list2[n][t]))))
                t+=1
                #regeggegewge
                #wfeqfqeffeqfqf
            j+=1
    else:
        funswapROWS(n,i,list2)
        scaling_ROWS1(n,i,list2)
g=0
f=0
while g<r-1 and f<c:
    scaling_ROWS(g,f,list2)
    g+=1
    f+=1
#print(list2)
def funCHANGE_TO_RREF1(list2):
    l=0
    while l<r:
        k=0
        count1=0
        count2=0
        while k<c:
            if float(list2[l][k])!=0:
                count1+=1
            if count1>0:
                u=0
                while u<r:
                    if u!=l:    
                        s=float(list2[u][k])/float(list2[l][k])
                        i=0
                        while i<len(list2[u]):
                            list2[u][i]=str(round((float(list2[u][i])-(float(list2[l][i])*s)),2))
                            i+=1
                        
                            
                    u+=1
                l+=1
                break
            elif count2>=c-1:
                return(list2)
            else:
                count2+=1
                k+=1
    return(list2)
(funCHANGE_TO_RREF1(list2))

for i in list2:
    y=0
    count1=0
    while y<len(i):
        if float(i[y])!=0:
            count1+=1
        if count1>0:
            v=0
            g=float(i[y])
            while v<len(i):
                i[v]=str(round((float(i[v])/g),3))
                v+=1
            break
        else:
            y+=1

y=0
while y<len(list2):
    g=0
    while g<len((list2[y])):
        if list2[y][g]=="-0.0":
            list2[y][g]="0.0"
        g+=1
    y+=1
print("the rref of the matrix is:")
print(list2)
# as the matrix equation is form Ax=0 the equation will always equate to 0 for all the equations
list3=[]
i=0
while i<c:#
    u=0
    list4=[]
    while u<r:
        list4.append(list2[u][i])
        u+=1
    list3.append(list4)
    i+=1
#print(list3)
def parametric(list2):
    d={} # d containly gives me the pivot columns
    d_freevariable={} # containly gives me the free variable columns of the matrix
    for i in list2:
        k=0
        while k<len(i):
            if float(i[k])==1:
                d[k+1]=1
                break
            k+=1
    h=1
    while h<=len(list2[0]):
        if h not in d:
            d_freevariable[h]=1
        h+=1
    answer=""
    for y in d_freevariable:
        k=1
        while k<=len(list3):
            if k==y:
                a=0
                while a<len(list3[k-1]):
                    if float(list3[k-1][a])!=0:
                        list3[k-1][a]=str(-float(list3[k-1][a]))
                    
                    a+=1
                list_00=[]
                for g in d_freevariable:
                    if g!=y and (len(list3[k-1])<c):
                        list3[k-1].insert(g-1,"0.0")
                    list_00.append(g)
                list3[k-1].insert(k-1,"1.0")
                while len(list3[k-1])>c:
                    list3[k-1].pop()
                answer+=str(list3[k-1])+"*x"+str(k)+"+"

            k+=1    
    print("the parametric of the matrix is:")  
    print(answer[:len(answer)-1])
    print("the solution of the equation is:")
    if answer[:len(answer)-1]!="":
        print(str([0]*c)+"+"+answer[:len(answer)-1])
    else:
        print(str([0]*c))
    
    #print(d)
    #print(d_freevariable)    
parametric(list2)
 
#in the paramatric form the matrix ahead of the the free variable is the paramatric coefficient (the obvious solution x=0 is not included in the answer)

                
                
    
        
        
        
    
                
            

            
    
    
        

        
            
        
