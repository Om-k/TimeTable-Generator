import copy
import random
from main import *
import json

def process_decimal(value):
    return int(value)

def process_decimal2(value):
    if isinstance(value, (float, int)):
        if isinstance(value, float):
            # Check if the value is a decimal
            if value.is_integer():
                # If it's an integer, return the next integer value
                return int(value) + 1
            else:
                # If it's a decimal, return the next integer value
                return int(value) + 1
        else:
            # If the value is an integer, return the next integer value
            return value


opt_Sub_Batch = {}
opt_Sub_Batch_Oppsite = {}

if no_Of_Sec<=no_Of_Opt_Subs:
    for i in range(1,no_Of_Sec+1):
        if 1 in opt_Sub_Batch.keys():
            opt_Sub_Batch[1].append(i)
        else:
            opt_Sub_Batch[1] = [i]
        opt_Sub_Batch_Oppsite[i] = 1
else:
    sec=1
    while sec<=no_Of_Sec:
        for i in range(sec,sec+no_Of_Sec_In_Batch+1):
            if i in opt_Sub_Batch.keys():
                opt_Sub_Batch[i].append(sec)
            else:
                opt_Sub_Batch[i] = [i]
                opt_Sub_Batch_Oppsite[sec] = i
        sec+=no_Of_Sec_In_Batch

#print(opt_Sub_Batch,opt_Sub_Batch_Oppsite)

def leastBusyTeacher(teacher_List):
    val = teacher_List[0]
    for i in teacher_List:
        if teachers_Busy[val] + random.uniform(0,10)>teachers_Busy[i]+random.uniform(0,10):#random.uniform(0,10) this decides the randomness of the algorithm
            val = i
    
    return val

def avg_of_sublist(sublist):
    return sum(sublist) / len(sublist) if sublist else 0

def custom_sort_key(item):
    if isinstance(item[1], list):
        return avg_of_sublist(item[1]) + int(random.uniform(0, 30))
    else:
        return item[1] + int(random.uniform(0, 30))


#sorted_a = sorted(a, key=lambda x: avg_of_sublist(x) if isinstance(x, list) else x)

def checkIfCollisionAndOptSub(temp_No_Hours,day,period,sec):
    if isinstance(temp_No_Hours[0][1],list):
        for i in temp_No_Hours[0][0]:
            if (week_Map[day],assigned_Teachers[(sec,i)],period) in asigned_Hours.keys():
                return True
        return False
    elif temp_No_Hours[0][0] == "Opt":
        for subs in sub_Teachers["Opt"]:
            if (week_Map[day],assigned_Teachers[(sec,subs)],period) in asigned_Hours.keys():
                return True

            return False
        pass
    else:
        return (week_Map[day],assigned_Teachers[(sec,temp_No_Hours[0][0])],period) in asigned_Hours.keys()


time_Tables = []

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
temp_No_Hours = sorted(temp_No_Hours, key=custom_sort_key, reverse=True)
#print(temp_No_Hours)
temp_No_Days = no_Of_Days

#Assigning teachers to each subject to each section
assigned_Teachers = {}
for sec in range(1,no_Of_Sec+1):
    for subject in subjects:
        if subject != "Opt":
            teacher_List = sub_Teachers[subject]
            val = leastBusyTeacher(teacher_List)
            assigned_Teachers[(sec,subject)] = val
            if subject in sub_Teachers["Opt"]:
                teachers_Busy[val] += int(str(no_Of_Hours_Subject["Opt"])[0])
            else:
                teachers_Busy[val] += int(str(no_Of_Hours_Subject[subject])[0])

#print(assigned_Teachers)
#Assigning teachers to each subject to each section done

cur_TimeTable = {week_Map[0]:[],
    week_Map[1]:[],
    week_Map[2]:[],
    week_Map[3]:[],
    week_Map[4]:[],
    week_Map[5]:[]}

for i in range(days_In_Week):
    for j in range(max_No_Hours):
        cur_TimeTable[week_Map[i]].append("")

sem7 = [cur_TimeTable]
for sec in range(1,no_Of_Sec+1):
    cur_TimeTable1 = copy.deepcopy(cur_TimeTable)
    sem7.append(cur_TimeTable1)

#print(sem7)
temp_No_Hours_Lst = [copy.deepcopy(temp_No_Hours)]
for sec in range(1,no_Of_Sec+1):
    temp_No_Hours_Lst.append(copy.deepcopy(temp_No_Hours)) 
#print(temp_No_Hours_Lst)

for sec in range(1,no_Of_Sec+1):
    #print(sem7)
    #sem7[sec] = copy.deepcopy(cur_TimeTable)
    period = 1
    while temp_No_Hours_Lst[sec]:
        
        #print(temp_No_Hours_Lst[sec])
        #print(sem7[sec])
        for day in range(6):
            if sem7[sec][week_Map[day]][period-1] == ('Opt', ''):
                continue


            temp_No_Hours_Lst[sec] = sorted(temp_No_Hours_Lst[sec], key=custom_sort_key, reverse=True)
            hTemp = []
            while temp_No_Hours_Lst[sec] and (checkIfCollisionAndOptSub(temp_No_Hours_Lst[sec],day,period,sec)):
                hTemp.append(temp_No_Hours_Lst[sec].pop(0))
                temp_No_Hours_Lst[sec] = sorted(temp_No_Hours_Lst[sec], key=custom_sort_key, reverse=True)

            if temp_No_Hours_Lst[sec]:
                if temp_No_Hours_Lst[sec][0][0] == "Opt":
                    for subs in sub_Teachers["Opt"]:
                        asigned_Hours[(week_Map[day],assigned_Teachers[(sec,subs)],period)] = True    
                    
                    for section in opt_Sub_Batch[opt_Sub_Batch_Oppsite[sec]]:
                        for subs_H in temp_No_Hours_Lst[section]:
                            if subs_H[0]=="Opt":
                                    subs_H[1] -= process_decimal(no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100))
                    #print(no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100))
                    for section in opt_Sub_Batch[opt_Sub_Batch_Oppsite[sec]]:
                        sem7[section][week_Map[day]][period-1] = ((temp_No_Hours_Lst[sec][0][0],""))
                    #make batches and assign
                else:
                    asigned_Hours[(week_Map[day],assigned_Teachers[(sec,temp_No_Hours_Lst[sec][0][0])],period)] = True    
                    temp_No_Hours_Lst[sec][0][1] -= process_decimal(no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100))
                    #print(no_of_weeks*(week_Day_Probabilty[week_Map[day]]/100))
                    sem7[sec][week_Map[day]][period-1] = ((temp_No_Hours_Lst[sec][0][0],assigned_Teachers[(sec,temp_No_Hours_Lst[sec][0][0])]))
                if temp_No_Hours_Lst[sec][0][1] <=0:
                    temp_No_Hours_Lst[sec].pop(0)
            if hTemp:
                temp_No_Hours_Lst[sec] = hTemp + temp_No_Hours_Lst[sec]
        #print(temp_No_Hours)
        period+=1
        #print(hTemp)
        #print(temp_No_Hours_Lst[sec],sec)
    #sem7.append(copy.deepcopy(sem7[sec]))
    #print("yooooooooooooooooooo")
    #print(sem7)

file = open('output.txt', 'w')           
print(sem7)
file.write(str(sem7))

#print(asigned_Hours)
#file.write(json.dumps(sem7, indent=2))

