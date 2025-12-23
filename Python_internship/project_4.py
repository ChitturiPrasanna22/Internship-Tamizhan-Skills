import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What is Python?",
        "options": ["Snake", "Programming Language", "Car", "Game"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["func", "define", "def", "function"],
        "answer": 2
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": 3
    }
]

current_q = 0
score = 0
answers = [-1] * len(questions)

# Window
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x350")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

# Selected option
selected_option = tk.IntVar()

# Radio buttons
options = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value=i)
    rb.pack(anchor="w")
    options.append(rb)

# Load Question
def load_question():
    question_label.config(text=questions[current_q]["question"])
    selected_option.set(answers[current_q])
    for i, opt in enumerate(questions[current_q]["options"]):
        options[i].config(text=opt)

# Next Question
def next_question():
    global current_q
    answers[current_q] = selected_option.get()
    if current_q < len(questions) - 1:
        current_q += 1
        load_question()
    else:
        show_result()

# Previous Question
def prev_question():
    global current_q
    answers[current_q] = selected_option.get()
    if current_q > 0:
        current_q -= 1
        load_question()

# Show Result
def show_result():
    score = 0
    for i in range(len(questions)):
        if answers[i] == questions[i]["answer"]:
            score += 1

    messagebox.showinfo("Result", f"Your Score: {score}/{len(questions)}")
    root.destroy()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Previous", command=prev_question).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Next", command=next_question).grid(row=0, column=1, padx=10)

# Load first question
load_question()

root.mainloop()
