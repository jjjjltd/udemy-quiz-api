from tkinter import *
from os.path import dirname, join
from quiz_brain import QuizBrain

current_dir = dirname(__file__)
print(current_dir)
image_dir = current_dir + "\images"
wimage_file_loc = join(image_dir, "false.png")
rimage_file_loc = join(image_dir, "true.png")


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score:  0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white" )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="This is where question should go.", font=("Ariel", 15, "italic"))

        wrong_img = PhotoImage(file=wimage_file_loc)
        self.wbutton = Button(image=wrong_img, width=70, height=75, command=self.false_pressed)
        self.wbutton.grid(column=0, row=2)


        right_img = PhotoImage(file=rimage_file_loc)
        self.rbutton = Button(image=right_img, width=70, height=75, command=self.true_pressed)
        self.rbutton.grid(column=1, row=2)

    

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"  Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions.  Thanks for playing.")
            self.rbutton.config(state="disabled")
            self.wbutton.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
