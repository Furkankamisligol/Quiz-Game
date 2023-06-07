from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Quizz",
                                                font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        image_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=image_true, highlightthickness=0, command=self.clicked_true_button)
        self.true_button.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=image_false, highlightthickness=0, command=self.clicked_false_button)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.true_button.config(state="normal")
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz_brain.next_question())

        else:
            self.canvas.itemconfig(self.question,
                                   text=f"Quiz is over.\nYou score is {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_true_button(self):
        if self.quiz_brain.check_answer is True:
            self.quiz_brain.score += 1
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)

    def clicked_false_button(self):
        if not self.quiz_brain.check_answer is True:
            self.quiz_brain.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)






