class DegreeExam:
    def question_paper(self):
        print('question paper set-1')
   
def new_question_paper(self):
    print('surprise......!! New Question paper')

DegreeExam.question_paper = new_question_paper

degree = DegreeExam()
degree.question_paper()