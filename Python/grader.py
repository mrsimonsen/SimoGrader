import os, shutil, importlib.util, csv, subprocess, datetime, shelve, sys
from data_maker import Assignment,Student
from data_maker import main as setup

PIPE = subprocess.PIPE

def intro():
    print("Python Grader")
    print("This program needs to be ran from the parent directory of the collection of student repos")
    print()
    setup()
    n = True
    while n:
        assign = input("What is the number of the assignment folder?\n")
        try:
            data = shelve.open('grading_data')
            assign_obj = data[assign]
            n = False
        except:
            print("That wasn't a valid assignment number!")
        data.close()
    return assign_obj

def gather(a):
    root = os.getcwd()
    try:
        shutil.rmtree('testing')
    except:
        pass#old testing folder already removed
    finally:
        os.mkdir("testing")
    data = shelve.open('grading_data')
    students = data['students']
    for s in students:
        os.mkdir("testing\\"+s.github)
        if a.folder == "15-trivia-challenge-2.0":
            shutil.copyfile(os.path.join(root,"hs_helper.py"), os.path.join(root,'testing',s.github,"hs_helper.py"))
            shutil.copyfile(os.path.join(root,"trivia.txt"),os.path.join(root,'testing',s.github,"trivia.txt"))
            shutil.copyfile(os.path.join(root,"highscores.dat"),os.path.join(root,'testing',s.github,"highscores.dat"))
        shutil.copyfile(os.path.join(root,s.github,a.folder,a.file), os.path.join(root,'testing',s.github,a.file))
        shutil.copyfile(os.path.join(root,"test_"+a.file), os.path.join(root,'testing',s.github,'Test.py'))
        os.chdir(s.github)
        p = subprocess.Popen(["git","log","-1","--format=%ci"],stdout=PIPE)
        out = p.communicate()[0].decode()
        os.chdir(root)
        s.submit = format_date(out)
    data['students']=students
    data.close()

def format_date(raw):
    #format '2019-08-28 14:46:11 -0600'
    #index:  0123456789012345678901234
    year = int(raw[:4])
    month = int(raw[5:7])
    day = int(raw[8:10])
    hour = int(raw[11:13])
    minute = int(raw[14:16])
    second = int(raw[17:19])
    date = datetime.datetime(year, month, day, hour, minute, second)
    return date

def grade(a):
    data = shelve.open('grading_data')
    s = data['students']
    root = os.getcwd()
    os.chdir('testing')
    with open('report.csv','w',newline='') as f:
        w = csv.writer(f,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['Period','Student Name','assignment name','points earned','is late?'])

    folders = [f.name for f in os.scandir() if f.is_dir()]
    for i in folders:
        print(f"Grading: {i}")
        os.chdir(i)
        proc = subprocess.Popen("py test.py", shell=True,stdout=PIPE, stderr=PIPE)
        out,err = proc.communicate()
        if err:
            print(err.decode())
            points = 0
        else:
            points = string_to_math(out.decode()[:-2])#remove /r/n
        #seperate github username from 'github_file.py'
        for student in s:
            if student.github == i:
                student.set_grade(a, points)
        os.chdir('..');#back to testing folder
    f = open('report.csv','a',newline='')
    w = csv.writer(f,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    s.sort(key=lambda x: x.name)
    for i in s:
        w.writerow([i.period,i.name,i.assignment.folder,i.score,i.late])
    f.close()
    os.chdir(root)
    data['students'] = s
    data.close()
    shutil.copyfile(os.path.join(root,'testing','report.csv'), os.path.join(root,'report.csv'))
    shutil.rmtree('testing')

def string_to_math(thing):
    if len(thing)%3==0:
        #single digit values
        total = int(thing[-1])
        score = int(thing[0])
    if len(thing)%5==0:
        #double digit values
        total = int(thing[-2:])
        score = int(thing[:2])
    if len(thing)%2==0:
        #single digit score with 2 digit total
        total = int(thing[-2:])
        score = int(thing[0])
    return round(score/total * 10,2)

def main():
    assign_obj = intro()
    print("gathering files, please wait")
    gather(assign_obj)
    print('files gatherd, moving to grading')
    grade(assign_obj)
    print("Testing complete")
    #input("Press enter to exit...")

if __name__ == '__main__':
    main()
