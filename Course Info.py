#Create main function
def main():

    #Display available courses
    print('Your courses are: CS101, CS102, CS103, NT110, and CM241.')
    
    #Get course number from user
    course_num = input('Which course would you like the information for? ')

    #Display info
    print(course_num, ' meets in Room', course_room[course_num], \
          'with Professor', course_instructor[course_num], \
          'at', course_time[course_num])



#Dictionaries with course information
course_room = {'CS101':'3004', 'CS102':'4501',\
               'CS103':'6755','NT110':'1244','CM241':'1411'}

course_instructor = {'CS101':'Haynes', 'CS102':'Alvarado',\
               'CS103':'Rich','NT110':'Burke','CM241':'Lee'}

course_time = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.',\
               'CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

#Call main function
main()
