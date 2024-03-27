import matplotlib.pyplot as plt

print("We are assuming that lower priority number has a higher priority")
n=int(input("Enter the number of processes:"))
arr=[]
for i in range(n):
  name=input("Enter the name of the process:")
  at=int(input("Enter the arrival time of the process:"))
  bt=int(input("Enter the burst time of the process:"))
  pr=int(input("Enter the priority of the process:"))
  arr.append([name,at,bt,pr])

tq=int(input("Enter the time quant of the algorithm:"))


plt.figure(figsize=(12, 12))
###################################################  FCFS   ###############################################################
plt.subplot(3, 2, 1)
p1=[]
for i in range(n):
  p1.append([arr[i][0],arr[i][2],arr[i][1]])


for i in range(n-1,-1,-1):
  plt.barh(p1[i][0],0)

left=0
p=sorted(p1,key=lambda x:(x[2]))

for i in range(n):
  if (p[i][2]<=left):
    plt.barh(p[i][0],p[i][1],left=left,color='red',height=1)
    left+=p[i][1]
    p[i].append(left)
  else:
    plt.barh(p[i][0],p[i][1],left=p[i][2],color='red',height=1)
    left=p[i][2]+p[i][1]
    p[i].append(left)

#finaldisplay
print("TAT:Turn Around Time")
print("WT:Waiting Time")
print()
print("---------------    FCFS   ------------------")
print()
print("Name Arrival-time Burst-time Finish-time TAT WT")
sumtat=0
sumwt=0
p.sort(key=lambda x:x[0])
for i in range(n):
  tat=p[i][3]-p[i][2]
  wt=tat-p[i][1]
  print(p[i][0],"     ",p[i][2],"       ",p[i][1],"        ",p[i][3],"        ",tat,"  ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('FCFS')


###################################################  SJF   ###############################################################
plt.subplot(3, 2, 2)
p=[]
burst=[]
for i in range(n):
  burst.append(arr[i][2])
  p.append([arr[i][0],arr[i][2],arr[i][1]])

for i in range(n-1,-1,-1):
  plt.barh(p[i][0],0)

left=0
while[True]:
  index=0
  mini=100
  for i in range(n):
    if (p[i][1]!=0 and p[i][2]<=left and p[i][1]<mini):
      mini=p[i][1]
  minijobslist=[]
  for i in range(n):
    if (p[i][1]!=0 and p[i][2]<=left and p[i][1]==mini):
      minijobslist.append(i)
  if (len(minijobslist)==0):
    left+=1
    continue
  elif (len(minijobslist)==1):
    index=minijobslist[0]
  else:
    miniarrivaltime=p[minijobslist[0]][2] #arrival of the first mini job process
    for i in minijobslist:
      if (p[i][2]<miniarrivaltime):
        miniarrivaltime=p[i][2]
    for i in minijobslist:
      if (p[i][2]==miniarrivaltime):
        index=i
        break

  plt.barh(p[index][0],p[index][1],left=left,color='red',height=1)
  left+=p[index][1]
  p[index][1]=0
  p[index].append(left)

  countzeros=0
  for i in range(n):
    if (p[i][1]==0):
      countzeros+=1

  if (countzeros==n):
    break

print()
print("---------------    SJF   ------------------")
print()
print("Name Arrival-time Burst-time Finish-time TAT WT")
sumtat=0
sumwt=0

for i in range(n):
  tat=p[i][3]-p[i][2]
  wt=tat-burst[i]
  print(p[i][0],"     ",p[i][2],"       ",burst[i],"        ",p[i][3],"        ",tat,"  ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('SJF')



###################################################  Priority NON-Premptive  ###############################################################
plt.subplot(3, 2, 3)
p1=[]
for i in range(n):
  p1.append([arr[i][0],arr[i][2],arr[i][3]])

for i in range(n-1,-1,-1):
  plt.barh(p[i][0],0)

left=0
p=sorted(p1,key=lambda x:(x[2]))

for i in range(n):
  plt.barh(p[i][0],p[i][1],left=left,color='red',height=1)
  left+=p[i][1]
  p[i].append(left)

#finaldisplay

print()
print("---------------    Priority NON-Premptive   ------------------")
print()
print("Name Priority Burst-time Finish-time TAT WT")
sumtat=0
sumwt=0
p.sort(key=lambda x:x[0])
for i in range(n):
  tat=p[i][3]
  wt=p[i][3]-p[i][1]
  print(p[i][0],"     ",p[i][2],"       ",p[i][1],"        ",p[i][3],"        ",tat,"  ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('Priority Non-Premptive')


###################################################  Round Robin   ###############################################################
plt.subplot(3, 2, 4)

p=[]
burst=[]
for i in range(n):
  wt=0
  burst.append(arr[i][2])
  p.append([arr[i][0],arr[i][2],arr[i][1],wt])

for i in range(n-1,-1,-1):
  plt.barh(p[i][0],0)

visited=[False]*n
left=0

while(True):
  indexlist=[]
  maxwt=0
  for i in range(n):
    if (p[i][2]<=left and p[i][1]!=0 and p[i][3]>maxwt):
      maxwt=p[i][3]

  for i in range(n):
    if (p[i][2]<=left and p[i][1]!=0 and p[i][3]==maxwt):
      indexlist.append(i)
  if (len(indexlist)==0):
    left+=1
    continue
  elif (len(indexlist)>1):
    if (visited[indexlist[0]]==False):
      index=indexlist[0]
      visited[indexlist[0]]=True
    else:
      index=indexlist[1]
      visited[index]=True
  else:
    index=indexlist[0]
    visited[index]=True

  #found the index which has to be plotted
  if (p[index][1]<tq):
    plt.barh(p[index][0],p[index][1],left=left,color='r',height=1)
    newleft=left+p[index][1]
    p[index][3]=0
    p[index][1]=0
  else:
    plt.barh(p[index][0],tq,left=left,color='r',height=1)
    newleft=left+tq
    p[index][3]=0
    p[index][1]=p[index][1]-tq

  #plotted and that record updated
  for i in range(n):
    if (i!=index and p[i][1]!=0 and p[i][2]<newleft):
      if (p[i][2]<=left):
        p[i][3]=p[i][3]+(newleft-left)
      elif (p[i][2]>left and p[i][2]<newleft):
        p[i][3]=p[i][3]+(newleft-p[i][2])
      else:
        continue

  left=newleft
  if (p[index][1]==0):
    p[index].append(left)

  countzeros=0
  #updated the waiting times of all records except the one we are working on
  for i in range(n):
    if (p[i][1]==0):
      countzeros+=1

  if (countzeros==n):
    break

print()
print("---------------    Round Robin   ------------------")
print()
print("Name Arrival-time Burst-time Finish-time TAT WT")
sumtat=0
sumwt=0
for i in range(n):
  tat=p[i][4]-p[i][2]
  wt=tat-burst[i]
  print(p[i][0],"     ",p[i][2],"       ",burst[i],"        ",p[i][4],"        ",tat,"  ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('Round Robin')

###################################################  SRTN   ###############################################################
plt.subplot(3, 2, 5)

p=[]
burst=[]
for i in range(n):
  wt=0
  burst.append(arr[i][2])
  p.append([arr[i][0],arr[i][2],arr[i][1],wt])

visited=[False]*n
left=0
#for ordered display
for i in range(n-1,-1,-1):
  plt.barh(p[i][0],0)

while[True]:
  minbt=100
  for i in range(n):
    if (p[i][1]<minbt and p[i][2]<=left and p[i][1]!=0):
      minbt=p[i][1]

  indexlist=[]
  index=0
  for i in range(n):
    if (p[i][1]==minbt and p[i][2]<=left):
      indexlist.append(i)

  if (len(indexlist)==0):
    left+=1
    continue
  elif (len(indexlist)==1):
    index=indexlist[0]
  else:
    maxwt=0
    for i in indexlist:
      if (p[i][3]>maxwt):
        maxwt=p[i][3]
    maxwtlist=[]
    for i in indexlist:
      if (p[i][3]==maxwt):
        maxwtlist.append(i)
    if (len(maxwtlist)==1):
      index=maxwtlist[0]
    else:
      for i in maxwtlist:
        if (visited[i]==False):
          index=i
          break

  visited[index]=True
  plt.barh(p[index][0],1,left=left,color='red',height=1)
  p[index][1]=p[index][1]-1
  p[index][3]=0
  left+=1
  if (p[index][1]==0):
    p[index].append(left)

  for i in range(n):
    if (i!=index and p[i][2]<left):
      p[i][3]=p[i][3]+1


  countzeros=0
  for i in range(n):
    if (p[i][1]==0):
      countzeros+=1

  if (countzeros==n):
    break

print()
print("---------------    SRTN   ------------------")
print()
print("Name Arrival-time Burst-time Finish-time TAT WT")
sumtat=0
sumwt=0

for i in range(n):
  tat=p[i][4]-p[i][2]
  wt=tat-burst[i]
  print(p[i][0],"     ",p[i][2],"       ",burst[i],"        ",p[i][4],"        ",tat,"  ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('SRTN')


###################################################  Priority-Premptive   ###############################################################
plt.subplot(3, 2, 6)

p=[]
burst=[]
for i in range(n):
  burst.append(arr[i][2])
  p.append([arr[i][0],arr[i][2],arr[i][1],arr[i][3]])

for i in range(n-1,-1,-1):
  plt.barh(p[i][0],0)

left=0
while[True]:
  minpr=100
  count=0
  for i in range(n):
    if (p[i][1]!=0 and p[i][2]<=left and p[i][3]<minpr):
      count+=1
      minpr=p[i][3]
  index=0

  if (count==0):
    left+=1
    continue
  for i in range(n):
    if (p[i][1]!=0 and p[i][2]<=left and p[i][3]==minpr):
      index=i
  plt.barh(p[index][0],1,left=left,color='red',height=1)
  left+=1
  p[index][1]=p[index][1]-1
  if (p[index][1]==0):
    p[index].append(left)

  countzeros=0
  for i in range(n):
    if (p[i][1]==0):
      countzeros+=1

  if (countzeros==n):
    break

print()
print("---------------    Priority Premptive   ------------------")
print()
print("Name Arrival-time Burst-time Priority Finish-time TAT WT")
sumtat=0
sumwt=0


for i in range(n):
  tat=p[i][4]-p[i][2]
  wt=tat-burst[i]
  print(p[i][0],"     ",p[i][2],"       ",burst[i],"        ",p[i][3],"        ",p[i][4],"  ",tat," ",wt)
  sumtat+=tat
  sumwt+=wt

print("Average Turn-Around Time: ",sumtat/n)
print("Average Waiting Time: ",sumwt/n)

plt.xticks(range(left+1))
plt.grid(True)
plt.title('Priority-Premptive')


###########################################################   END   ####################################################
plt.show()
