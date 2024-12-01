list1=[]
list2=[]
with open("input.txt", "r") as file:
    for line in file:
        first, second = map(int, line.split())
        list1.append(first)
        list2.append(second)
list1.sort()
list2.sort()
sum=0;

for x in range((min(len(list1),len(list2)))):
    if len(list1)<x: sum+=list2[x]
    else:
        if len(list2)<x:
            sum+=list1[x]
    sum+=abs(list1[x]-list2[x])

#prvi
prev=-1; scoreprev=0;
for x in range(0,len(list1)):
    if len[x]==prev: sum+=scoreprev
    else:
        scoreprev=0
        for y in range(0,len(list2)):
            if list2[y]>list1[x]: scoreprev=scoreprev*list1[x]; break
            else:
                if list2[y]==list1[x]: scoreprev+=1


# drugi
tot_sum=0;
prev=-1; scoreprev=0;
for x in range(0,len(list1)):
    if list1[x]==prev: tot_sum+=scoreprev
    else:
        scoreprev=0
        for y in range(0,len(list2)):
            if list2[y]>list1[x]: scoreprev=scoreprev*list1[x]; prev=list1[x]; tot_sum+=scoreprev; break
            elif list2[y]==list1[x] : scoreprev+=1








