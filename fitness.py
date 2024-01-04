import ast
from main import *

#timetable = [{'Mon': ['', '', '', '', '', '', ''], 'Tue': ['', '', '', '', '', '', ''], 'Wed': ['', '', '', '', '', '', ''], 'Thu': ['', '', '', '', '', '', ''], 'Fri': ['', '', '', '', '', '', ''], 'Sat': ['', '', '', '', '', '', '']}, {'Mon': [('18CS71', 'Suhas'), ('18CS734', 'Shreenath'), ('18CS72', 'Shreenath2'), '', '', '', ''], 'Tue': [('18CS72', 'Shreenath2'), ('18CS71', 'Suhas'), ('18CS744', 'Harisha'), '', '', '', ''], 'Wed': [('18CS744', 'Harisha'), ('18CS744', 'Harisha'), ('18CS734', 'Shreenath'), '', '', '', ''], 'Thu': [('18CS734', 'Shreenath'), ('18CS72', 'Shreenath2'), '', '', '', '', ''], 'Fri': [('18CS72', 'Shreenath2'), ('18CS71', 'Suhas'), '', '', '', '', ''], 'Sat': [('18CS71', 'Suhas'), ('18CS734', 'Shreenath'), '', '', '', '', '']}, {'Mon': [('18CS72', 'Ashwini'), ('18CS744', 'Adarsh'), ('18CS734', 'Janardan'), '', '', '', ''], 'Tue': [('18CS71', 'Shiji'), ('18CS734', 'Janardan'), ('18CS744', 'Adarsh'), '', '', '', ''], 'Wed': [('18CS744', 'Adarsh'), ('18CS72', 'Ashwini'), ('18CS71', 'Shiji'), '', '', '', ''], 'Thu': [('18CS71', 'Shiji'), ('18CS71', 'Shiji'), '', '', '', '', ''], 'Fri': [('18CS734', 'Janardan'), ('18CS72', 'Ashwini'), '', '', '', '', ''], 'Sat': [('18CS72', 'Ashwini'), ('18CS71', 'Shiji'), '', '', '', '', '']}, {'Mon': [('18CS72', 'Shreenath2'), ('18CS744', 'Joylene'), ('18CS71', 'Reshma'), '', '', '', ''], 'Tue': [('18CS71', 'Reshma'), ('18CS734', 'Anand Prabhu'), ('18CS734', 'Anand Prabhu'), '', '', '', ''], 'Wed': [('18CS744', 'Joylene'), ('18CS72', 'Shreenath2'), ('18CS72', 'Shreenath2'), '', '', '', ''], 'Thu': [('18CS734', 'Anand Prabhu'), ('18CS71', 'Reshma'), '', '', '', '', ''], 'Fri': [('18CS71', 'Reshma'), ('18CS744', 'Joylene'), '', '', '', '', ''], 'Sat': [('18CS72', 'Shreenath2'), ('18CS72', 'Shreenath2'), '', '', '', '', '']}]

timetable = ast.literal_eval(open('output.txt', 'r').read()) 

def fitnessCalculation(timetable):
    fitness = checkHours(timetable)
    return fitness

def checkHours(timetables):
    sum_Of_Required_Hours = 0

    for i in no_Of_Hours_Subject.values():
        if isinstance(i,list):
            sum_Of_Required_Hours += i[0]
        else:
            sum_Of_Required_Hours += i

    firstDone = False
    each_Sec_Perc = []
    for sec_timetable in timetables:
        temp_No_Hours_count = no_Of_Hours_Subject.copy()

        #keeping only the required number of hours and not how long a class should be
        for tmpKey in temp_No_Hours_count.keys():
            if isinstance(temp_No_Hours_count[tmpKey],list):
                temp_No_Hours_count[tmpKey] = temp_No_Hours_count[tmpKey][0]   
        #keeping only the required number of hours and not how long a class should be done
        #print(temp_No_Hours_count)
        if not firstDone:
            firstDone=True
            continue
        for day in range(days_In_Week):
            for period in sec_timetable[week_Map[day]]:
                if period != '':
                    #print(period[0])
                    if temp_No_Hours_count[period[0]] > 0:
                        temp_No_Hours_count[period[0]] -= int(no_of_weeks * (week_Day_Probabilty[week_Map[day]])/100)
                        if temp_No_Hours_count[period[0]] <= 0:
                            temp_No_Hours_count[period[0]] = 0 
        sum_Of_Remaining_Hours = 0
        for hours in temp_No_Hours_count.values():
            sum_Of_Remaining_Hours += hours
        
        sum_Of_Assigned_hours = sum_Of_Required_Hours - sum_Of_Remaining_Hours

        sec_Perc = (sum_Of_Assigned_hours * 100)//sum_Of_Required_Hours
        each_Sec_Perc.append(sec_Perc)

    avg_Perc = 0
    for val in each_Sec_Perc:
        avg_Perc += val
    
    avg_Perc = avg_Perc//len(each_Sec_Perc)

    return avg_Perc

def checkTeacherAvailability(timetables):
    pass



print(fitnessCalculation(timetable))