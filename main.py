#initialisations of values
'''
AIML: 18CS71
Big D: 18CS72
Crypto: 18CS744
UID: 18CS734
'''

techers_Subs = {
    "Suhas":["18CS71","18CSL76"],
    "Shiji":["18CS71","18CS72","18CSL76"],
    "Anand Prabhu":["18CS734"],
    "Shreenath":["18CS734"],
    "Adarsh":["18CS744"],
    "Harisha":["18CS744"],
    "Ashwini":["18CS72"],
    "Reshma" : ["18CS71"],
    "Shreenath2" : ["18CS72"],
    "Joylene" : ["18CS744"],
    "Janardan" : ["18CS734"],
    "Ragavendra Sooda" : ["18CSL77"],
    "Prasad Chandran N" : ["18CSOP1"],
    "Vishal" : ["18CSOP1"],
    "Smitha" : ["18CSOP2"],
    "Natural":["18CSOP3"]

}

max_No_Hours = 9
lab_Hours = 3
no_Of_Opt_Subs = 3
no_Of_Sec_In_Batch = 3
teachers = ["Suhas","Shiji","Ashwini","Shreenath","Anand Prabhu","Adarsh","Harisha","Reshma","Shreenath2","Joylene","Janardan","Prasad Chandran N","Smitha","Natural","Vishal","Ragavendra Sooda"]
subjects = ["18CS71","18CS72","18CS734","18CS744","18CSOP1","18CSOP2","18CSOP3","18CSL76","18CSL77"]
no_Of_Students_Per_Class = 60
no_Of_Batch_For_Div_Sub = 3
lunch_BreakAfter_Hour = 4
break_timings = [2,4]           

sub_Teachers = { 
    "18CS71" : ["Suhas","Shiji","Reshma"],
    "18CS72" : ["Shiji","Ashwini","Shreenath2"],
    "18CS734" : ["Shreenath","Anand Prabhu","Janardan"],
    "18CS744" : ["Adarsh","Harisha","Joylene"],
    "18CSOP1": ["Prasad Chandran N","Vishal"],
    "18CSOP2": ["Smitha"],
    "18CSOP3": ["Natural"],
    "18CSL76": ["Suhas","Shiji"],
    "18CSL77": ["Ragavendra Sooda"],
    "Opt" : ["18CSOP1","18CSOP2","18CSOP3"],
    "Lab":["18CSL76","18CSL77"]
}

no_Of_Hours_Subject = {
    "18CS71":50,
    "18CS72":50,
    "18CS734":40,
    "18CS744":40,
    "Opt": 40 #[18CSOP1,18CSOP2,18CSOP3]#[40,40,40] #as many as number of sections
    ,"Lab" : [36,3]
}

#Mapping lab and optional subjects to their parent names
multi_Sub_Parent = {
    "18CSOP1" : "Opt",
    "18CSOP2" : "Opt",
    "18CSOP3" : "Opt",
    "18CSL76" : "Lab",
    "18CSL77" : "Lab"
}

#class_Div_Subs = set(["Lab"])
class_Div_Subs ={
    "Lab" : ["18CSL76","18CSL77"]
}
class_Div_Subs_Check = {value for values_list in class_Div_Subs.values() for value in values_list}

class_Mix_Subs = {
    "Opt" : ["18CSOP1","18CSOP2","18CSOP3"]
}
class_Mix_Subs_Check = {value for values_list in class_Mix_Subs.values() for value in values_list}

extra_Hour_Subs = {
    "Lab" : 3
}

no_Of_Days = 102 
no_Of_Sec = 3
no_of_weeks = 17
no_Of_Days_In_Week = 6

week_Day_Probabilty = {
    "Mon" : 90,
    "Tue" : 80,
    "Wed" : 85,
    "Thu" : 80,
    "Fri" : 85,
    "Sat" : 50
}

teachers_Busy = {}
for i in teachers:
    teachers_Busy[i] = 0


week_Map = {
    0:"Mon",
    1:"Tue",
    2:"Wed",
    3:"Thu",
    4:"Fri",
    5:"Sat"
}

days_In_Week = 6
#initialisations of values done

# print("Calling function from file2.py")
# print_something()
