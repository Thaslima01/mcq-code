
q1="""1.Python is _____ programming language
a:high-level
b:mid-level
c:low-level
d:none of the above"""

q2="""2.IBM stands for
a:Indian Business Machine
b:Internal Business Machine
c:International Business Machine
d:Integrated Business Machine"""

q3="""3.What is the name of the fastest super computer of the world?
a:Maya
b:IBM jaguar
c:Mira
d:Tianhe-2"""

q4="""4.The person contributing the idea of stored program was
a:Chards babbage
b:Dennis ritchie
c:Howard aiken
d:John neumann"""

q5="""5.A _______ is a software application for retrieving, presenting and traversing information
a:HTTP
b:E-mail
c:Web browser
d:Search engine"""


print("welcome to MCQ test")
name=input("your name: ")
options={q1:"a",q2:"b",q3:"d",q4:"d",q5:"c"}
score=0
questions=[q1,q2,q3,q4,q5]
import random
random.shuffle(questions)
for i in questions:
    print(i)
    answer=input("your answer (a/b/c/d) : ")
    if answer==options[i]:
        print("correct")
        score+=1
        print(score)
    else:
        print("incorrect")
        print(score)
print("final score is: ",score)


