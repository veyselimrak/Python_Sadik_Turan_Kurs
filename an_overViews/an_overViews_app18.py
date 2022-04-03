
class Questions():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer
         

class Quiz():
    
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0
    
    def getQuestions(self):
        return self.questions[self.questionsIndex]
    
    def displayQuestion(self):
        question = self.getQuestions()
        print(f"Soru {self.questionsIndex + 1} : {question.text} ")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevabınız nedir :")
        print(question.checkAnswer(answer))

        self.guess(answer)
        self.loadQuestion()
    
    def  guess(self, answer):
        question = self.getQuestions()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionsIndex += 1 

        

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayProgress(self):

        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100,"*"))





    def showScore(self):
        print("Score : " , self.score)


q1 = Questions("En iyi programlama dili hangisidir ?", ["Python" , "C#" , "Java" ,"C++"] , "Python")
q2 = Questions("En iyi bölüm hangisidir ?", ["PC Müh." , "İnş. Müh." , "Makine Müh." ,"Mekatronik Müh."] , "PC Müh.")
q3 = Questions("3 ün 2 katının 4 eksiği kaçtır  ?", ["3" , "2" , "5" ,"1"] , "2")
q4 = Questions("En çok kazandıran programlama dili  ?", ["Python" , "Java" , "C#" ,"C"] , "Java")
q5 = Questions("En çok sevilen programalama dili  ?", ["C#" , "Python" , "Java" ,"Javascript"] , "Javascript")

# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("Makine Müh."))

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()

# question = quiz.getQuestions()
# print(question.text)


# quiz.displayQuestion()
