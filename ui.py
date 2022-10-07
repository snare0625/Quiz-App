from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #score label
        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(row=0, column=1)
        #quiz_canvas_message
        self.canvas = Canvas(width=300, height=250, bg="snow")
        self.question_text = self.canvas.create_text(150, 125, text="Text goes here", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #correct_button
        self.true_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0,)
        self.true_button.config(padx=20, pady=20, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        #wrong_button
        self.false_image = PhotoImage(file="images/true.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.config(padx=20, pady=20, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")

    def false_pressed(self):
        is_wrong = self.quiz.check_answer("False")

    def give_feedback(self, is_right):
        






