data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
#1
def quiz():
    wrongAnswer  =[]
    for item in data:
        print(item["question"])
        answer = input("Enter your answer: ")
        print("answer",answer)
        if answer == item["answer"]:
            print("Correct")
        else :
            wrongAnswer.append(item["answer"])


        print(wrongAnswer)
        """
        if answer == item["answer"]:
            wrongAnswer.append(answer)
            print(answer)
            
        wrongAnswer.sort()
        """
quiz()

