import copy
import random
from main import *
import json

def leastBusyTeacher(teacher_List):
    val = teacher_List[0]
    for i in teacher_List:
        if teachers_Busy[val] + random.uniform(0,10)>teachers_Busy[i]+random.uniform(0,10):#random.uniform(0,10) this decides the randomness of the algorithm
            val = i
    
    return val
 

week_Map = {
    0:"Mon",
    1:"Tue",
    2:"Wed",
    3:"Thu",
    4:"Fri",
    5:"Sat"
}

time_Tables = []

teachers_Busy = {}
for i in teachers:
    teachers_Busy[i] = 0

sample_TimeTable = {
    0:["18CS71","18CS72"],
    1:["18CS734","18CS744","18CS71"],
    2:["18CS72","18CS71","18CS734"],
    3:["18CS71","18CS72","18CS71"],
    4:["18CS72","18CS71","18CS734"],
    5:["18CS71","18CS72"]
}


#Start of making a chromosome

asigned_Hours = {}
temp_No_Hours = list(no_Of_Hours_Subject.items())
for i in range(len(temp_No_Hours)):
    temp_No_Hours[i] = list(temp_No_Hours[i])
temp_No_Hours = sorted(temp_No_Hours, key=lambda x: (x[1] + int(random.uniform(0, 30))), reverse=True)
#print(temp_No_Hours)
temp_No_Days = no_Of_Days

#Assigning teachers to each subject to each section
assigned_Teachers = {}
for sec in range(1,no_Of_Sec+1):
    for subject in subjects:
        temp = sub_Teachers[subject]
        val = leastBusyTeacher(temp)
        assigned_Teachers[(sec,subject)] = val
        teachers_Busy[val] += int(str(no_Of_Hours_Subject[subject])[0])

#print(assigned_Teachers)
#Assigning teachers to each subject to each section done

cur_TimeTable = {week_Map[0]:[],
    week_Map[1]:[],
    week_Map[2]:[],
    week_Map[3]:[],
    week_Map[4]:[],
    week_Map[5]:[]}

for i in range(6):
    for j in range(max_No_Hours):
        cur_TimeTable[week_Map[i]].append("")

sem7 = [cur_TimeTable]
for sec in range(1,no_Of_Sec+1):
    cur_TimeTable1 = copy.deepcopy(cur_TimeTable)
    sem7.append(cur_TimeTable1)

print(sem7)

for sec in range(1,no_Of_Sec+1):
    temp_No_Hours = list(no_Of_Hours_Subject.items())
    for i in range(len(temp_No_Hours)):
        temp_No_Hours[i] = list(temp_No_Hours[i])

    #sem7[sec] = copy.deepcopy(cur_TimeTable)
    period = 1
    while temp_No_Hours:
        #print(temp_No_Hours)
        #print(sem7[sec])
        for day in range(6):
            temp_No_Hours = sorted(temp_No_Hours, key=lambda x: (x[1] + int(random.uniform(0, 10))), reverse=True)
            hTemp = []
            while temp_No_Hours and (week_Map[day],assigned_Teachers[(sec,temp_No_Hours[0][0])]) in asigned_Hours.keys():
                hTemp.append(temp_No_Hours.pop(0))
                temp_No_Hours = sorted(temp_No_Hours, key=lambda x: (x[1] + int(random.uniform(0, 30))), reverse=True)
            
            if temp_No_Hours:
                asigned_Hours[(week_Map[day],assigned_Teachers[(sec,temp_No_Hours[0][0])],period)] = True    
                temp_No_Hours[0][1] -= no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100)
                #print(no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100))
                sem7[sec][week_Map[day]][period-1] = ((temp_No_Hours[0][0],assigned_Teachers[(sec,temp_No_Hours[0][0])]))
                if temp_No_Hours[0][1] <=0:
                    temp_No_Hours.pop(0)
            if hTemp:
                temp_No_Hours = hTemp + temp_No_Hours
        #print(temp_No_Hours)
        period+=1
    #sem7.append(copy.deepcopy(sem7[sec]))
    #print("yooooooooooooooooooo")
    #print(sem7)

file = open('output.txt', 'w')           
print(sem7)
file.write(str(sem7))

#print(asigned_Hours)
#file.write(json.dumps(sem7, indent=2))

