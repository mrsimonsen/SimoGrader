#data maker for java
import csv, shelve, pickle
#support classes
class Assignment(object):
    '''an assignment with a file name'''

    def __init__(self,file,test):
        self.file = file
        self.test = test

    def __str__(self):
        rep = f"{self.file}\n{self.test}"
        return rep
class Student(object):
    '''a student with name, weber username, and github username'''

    def __init__(self, name, period, github):
        self.name = name
        self.github = github
        self.period = period
        self.assignment = Assignment('error','')
        self.score = 0

    def __str__(self):
        rep = f"{self.name}, Period {self.period}\n{self.github}\n--Current Assignment--\n{self.assignment.file}\n{self.score} points"
        return rep

    def set_grade(self, assign_obj, score):
        self.assignment = assign_obj
        self.score = score
        
def main():
    #create shelve file, overwrite old file if exists
    data = shelve.open('grading_data','n')

    #assignment details
    assignments = ('00j','01j','02j','03j','04j','05j','06j','07j','08j','09j','10j','11j','12j','13j','14j','15j','16j','17j','18j','19j','20j','21j')
    file_names = {
    "00j":("HelloWorld.java",),
    "01j":("BasicInput.java",),
    "02j":("PaintEstimator.java",),
    "03j":("TextMsgAbbreviation.java",),
    "04j":("TextMsgDecoder.java",),
    "05j":("TextMsgExpander.java",),
    "06j":("DrawRightTriangle.java",),
    "07j":("DrawHalfArrow.java",),
    "08j":("PeopleWeights.java",),
    "09j":("PlayerRoster.java",),
    "10j":("CoinFlipper.java",),
    "11j":("ReverseMessage.java",),
    "12j":("DiceStats.java",),
    "13j":("TextAnalyzer.java",),
    "14j":("AuthoringAssistant.java",),
    "15j":("ShoppingCartPrinter.java","ItemToPurchase.java"),
    "16j":("ShoppingCartManager.java","ItemToPurchase.java","ShoppingCart.java"),
    "17j":("BinConverter.java",),
    "18j":("ParseStrings.java",),
    "19j":("DataVisualizer.java",),
    "20j":("CaesarCipher.java","ReadWrite.java","Support.java"),
    "21j":("Yahtzee.java",)
	}
    tests = {
    '00j':'Test00.java',
    '01j':'Test01.java',
    '02j':'Test02.java',
    '03j':'Test03.java',
    '04j':'Test04.java',
    '05j':'Test05.java',
    '06j':'Test06.java',
    '07j':'Test07.java',
    '08j':'Test08.java',
    '09j':'Test09.java',
    '10j':'Test10.java',
    '11j':'Test11.java',
    '12j':'Test12.java',
    '13j':'Test13.java',
    '14j':'Test14.java',
    '15j':'Test15.java',
    '16j':'Test16.java',
    '17j':'Test17.java',
    '18j':'Test18.java',
    '19j':'Test19.java',
    '20j':'Test20.java',
    '21j':'Test21.java'
	}

    for i in assignments:
        data[i]=Assignment(file_names[i],tests[i])
	
	#load list of periods that are java
	f = open('classes.dat','rb')
	classes = pickle.load(f)
	f.close()
	periods = []
	for i in classes.keys():
		if classes[i] == 'j':
			periods.append(i)

    #student details
    students = []
    with open("What's in a Username_ (Responses) - Copy of Form Responses 1.csv",'r',newline='') as f:
        #format = time,first,last,period,git
        raw = csv.reader(f,delimiter=',',quotechar='"')
        for row in raw:
            if row[0] == "Timestamp":
                continue#skip the first row/header
			if row[3] not in periods:
				continue#skip non-java students
            students.append(Student(f"{row[2]}, {row[1]}",row[3],row[4]))
    data['students'] = students
    #save all the things
    data.close()

