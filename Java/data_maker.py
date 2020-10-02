#data maker for java
import csv, shelve, datetime
#support classes
class Assignment(object):
    '''an assignment with a folder, file name'''

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
    "00":("HelloWorld.java",),
    "01":("BasicInput.java",),
    "02":("PaintEstimator.java",),
    "03":("TextMsgAbbreviation.java",),
    "04":("TextMsgDecoder.java",),
    "05":("TextMsgExpander.java",),
    "06":("DrawRightTriangle.java",),
    "07":("DrawHalfArrow.java",),
    "08":("PeopleWeights.java",),
    "09":("PlayerRoster.java",),
    "10":("CoinFlipper.java",),
    "11":("ReverseMessage.java",),
    "12":("DiceStats.java",),
    "13":("TextAnalyzer.java",),
    "14":("AuthoringAssistant.java",),
    "15":("ShoppingCartPrinter.java","ItemToPurchase.java"),
    "16":("ShoppingCartManager.java","ItemToPurchase.java","ShoppingCart.java"),
    "17":("BinConverter.java",),
    "18":("ParseStrings.java",),
    "19":("DataVisualizer.java",),
    "20":("CaesarCipher.java","ReadWrite.java","Support.java"),
    "21":("Yahtzee.java",)
	}
    tests = {
    '00':'Test00.java',
    '01':'Test01.java',
    '02':'Test02.java',
    '03':'Test03.java',
    '04':'Test04.java',
    '05':'Test05.java',
    '06':'Test06.java',
    '07':'Test07.java',
    '08':'Test08.java',
    '09':'Test09.java',
    '10':'Test10.java',
    '11':'Test11.java',
    '12':'Test12.java',
    '13':'Test13.java',
    '14':'Test14.java',
    '15':'Test15.java',
    '16':'Test16.java',
    '17':'Test17.java',
    '18':'Test18.java',
    '19':'Test19.java',
    '20':'Test20.java',
    '21':'Test21.java'
	}

    for i in assignments:
        data[i]=Assignment(folders[i],file_names[i],tests[i])

    #student details
    names = {}
    students = []
    with open('What's in a Username_ (Responses) - Copy of Form Responses 1.csv','r',newline='') as f:
        #format = time,first,last,period,git
        raw = csv.reader(f,delimiter=',',quotechar='"')
        for row in raw:
            if row[0] == "Timestamp":
                continue#skip the first row/header
            students.append(Student(f"{row[2]}, {row[1]}",row[3],row[4]))
    data['students'] = students
    #save all the things
    data.close()
