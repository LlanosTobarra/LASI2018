from random import randint
import datetime

courses = ['bio11111','chem1111','phys1111','socio1111','arts1111','hist1111','econ1111','mgmt1111','acct1111']

tutors = ['AAAA','BBBB','CCCC','DDDD','EEEE','FFFF','GGGGG','HHHHH','IIII']

tools = {'blog':10,'assessment':60,'wiki':40,'forum':20,'quiz':40,'LTI':10,'book':23,'link':56,'video':12,'scorm':4}

def createStruct():

        courseData=[]
        for week in range(1, 11):
            weekdata = []
            r = randint(0,100)
            done = False
            for key,value in tools.items():
                r = randint(0,100)
                if (r<value):
                    weekdata.append(key)
                    done=True
            if not done:
                    weekdata.append('link')
            struct={}
            struct[week]=weekdata
            courseData.append(struct)

        return courseData

def out(f2,timestamp, actor, role, Action,Object_Instance,Object_Type,Topic,Course_ID):

        h = str(randint(0,24))
        if len(h)==1:
            h='0'+h

        m =  str(randint(0,60))
        if len(m)==1:
            m='0'+m

        timestamp = timestamp+' ' + h + ":" + m

        if Object_Type == 'assessment':
            Action = 'submit'

        if Object_Type == 'forum' and randint(0,10)<4:
            Action = 'post'

        f2.write(timestamp)
        f2.write(',')
        f2.write(actor)
        f2.write(',')
        f2.write(role)
        f2.write(',')
        f2.write(Action)
        f2.write(',')
        f2.write(Object_Instance)
        f2.write(',')
        f2.write(Object_Type)
        f2.write(',')
        f2.write(Topic)
        f2.write(',')
        f2.write(Course_ID)
        f2.write ('\n')



start = datetime.datetime(2017, 9, 1)

f = open('out.csv','w')
f2 = open('out2.csv','w')

f2.write('Timestamp,Actor,Role,Action,Object_Instance,Object_Type,Topic,Course_ID\n')

all ={}
for course in courses:
    all[course]=createStruct()



for key,value in all.items():
    print(key)
    for items in value:
        for week in items:
            for i in items[week]:
                    f.write (key + ',' + str(week) + ',' + i + '\n')
                    createDate =  start +datetime.timedelta(days=randint(1,20))
                    if randint(0,10)>6:
                        createDate =  createDate +datetime.timedelta(days=randint(1,10))
                    #creator=tutors[randint(0,len(tutors)-1)]
                    creator = key.replace('1111','-TUTOR')
                    out(f2,createDate.strftime('%Y-%m-%d'),creator,'staff','create',str(week),i,'Topic ' + str(week),key)



for course in courses:
    for week in range(1,11):
        print('week ' + str(week))
        currentweek =  start +datetime.timedelta(days=7*week)
        acts= all[course][week-1][week]
        for student in range (100,200):
            for n in range(0, randint(0,10)):
                for tool in acts:
                    r = randint(0,100)
                    if r>20:
                        out(f2,currentweek.strftime('%Y-%m-%d'),str(student),'student','view',str(week),tool,'Topic ' + str(week),course)
                    if r<3:
                        r = randint(1,10)
                        randAct= all[course][r-1][r]
                        for tool in randAct:
                                r = randint(0,100)
                                if r>50:
                                        out(f2,currentweek.strftime('%Y-%m-%d'),str(student),'student','view',str(week),tool,'Topic ' + str(week),course)
                if r<5 and week>1:
                        r = randint(1,10)
                        randAct= all[course][week-2][week-1]
                        for tool in randAct:
                                r = randint(0,100)
                                if r>50:
                                        out(f2,currentweek.strftime('%Y-%m-%d'),str(student),'student','view',str(week),tool,'Topic ' + str(week),course)
                if r<3 and week<10:
                        r = randint(1,10)
                        randAct= all[course][week][week+1]
                        for tool in randAct:
                                r = randint(0,100)
                                if r>50:
                                    out(f2,currentweek.strftime('%Y-%m-%d'),str(student),'student','view',str(week),tool,'Topic ' + str(week),course)