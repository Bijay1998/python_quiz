from Questions import Question

question_prompts = [
    "Calculate the value of 2*2.\n(a) 4\n(b) 5\n(c) 23\n\n ",
    "Calculate the value of 5-2.\n(a) 1\n(b) 4\n(c) 3\n\n",
    "What is the value of 2 to the power 2?\n(a) 4\n(b) 5\n(c) 23\n\n "
]

questions =[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"a")
]

def run_test(questions):
    score =0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You have got"+ str(score)+"/"+str(len(questions))+" correct")


run_test(questions)
