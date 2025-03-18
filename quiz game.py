#questions to be asked on quiz

questions = [
    {"prompt": "What is the output of 3 + 2 * 2?",
        "options": ["A) 10", "B) 7", "C) 8", "D) 9"],
        "answer": "B"
    },
    {"prompt": "Which data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) String", "D) Set"],
        "answer": "C"
    },
    
    {"prompt":"Which of the following is used to define a function in Python?",
        "options": ["A) define", "B) func", "C) def", "D) function"],
        "answer": "C"
    },
    {"prompt":"What will be the output of print(type([]))?",
        "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"],
        "answer": "A"
    },
    {"prompt":"Which keyword is used to handle exceptions in Python?",
        "options": ["A) try", "B) except", "C) finally", "D) catch"],
        "answer": "B"
    },
    {"prompt":"What is the correct file extension for Python files?",
        "options": ["A) .py", "B) .python", "C) .pyt", "D) .pt"],
        "answer": "A"
    },
    {"prompt":"How do you start a comment in Python?", 
        "options": ["A) //", "B) <!--", "C) #", "D) **"],
        "answer": "C"
    },
    {"prompt":"Which of the following is NOT a Python data type?", 
        "options": ["A) int", "B) float", "C) char", "D) bool"],
        "answer": "C"
    },
    {"prompt":"Which function is used to get user input in Python?",
        "options": ["A) input()", "B) scan()", "C) get()", "D) read()"],
        "answer": "A"
    },
    {"prompt":"Which of the following loops in Python executes at least once?",
        "options": ["A) for loop", "B) while loop", "C) do-while loop", "D) None"],
        "answer": "C"
    },
    {"prompt":"Which module in Python is used for working with regular expressions?",
        "options": ["A) regex", "B) re", "C) reg", "D) pyregex"],
        "answer": "B"
    },
    {"prompt":"How do you create a tuple in Python?",
        "options": ["A) []", "B) {}", "C) ()", "D) <>"],
        "answer": "C"
    },
    {"prompt":"Which of the following statements is used to exit a loop in Python?",
        "options": ["A) break", "B) continue", "C) exit", "D) return"],
        "answer": "A"
    },
    {"prompt":"Which function is used to find the length of a list in Python?",
        "options": ["A) count()", "B) size()", "C) len()", "D) length()"],
        "answer": "C"
    },
    {"prompt":"Which keyword is used to define a class in Python?",
        "options": ["A) class", "B) struct", "C) define", "D) object"],
        "answer": "A"
    }
]
#
# codes for quiz game 
def run_quiz(questions):
    score =0 
    for question in questions:
        print(question["prompt"])
        for option in question["options"] :
            print(option)
        answer = input("Enter Your Answer(A,B,C or D) :").upper()
        if answer == question["answer"]:
            print("correct \n")
            score +=1
        else:
            print("incorrect, The correct answer is" , question["answer"],"\n")
    print(f" You got {score}  Out of  {len(questions)}  questions correct.")

run_quiz(questions)