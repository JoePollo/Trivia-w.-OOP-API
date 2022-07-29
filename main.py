from tkinter import Button, Label, Tk, Canvas, PhotoImage
from questions import Questions


THEME_COLORS = {
    "BACKGROUND": "#3e1585",
    "FOREGROUND": "#f0e731",
    "SCORE_COLOR": "#cf006b",
    "CORRECT": "#73bf86",
    "INCORRECT": "#e06f67",
    "GAME_OVER": "#6faf7c"
}
WIDTH = 300
HEIGHT = 250


class Interface:
        def __init__(self):
            self.window = Tk()
            self.window.title("Quizeroo")
            self.window.configure(padx = 20,
                                  pady = 20,
                                  background = THEME_COLORS["BACKGROUND"])
            
            
            self.questions = Questions()
            self.questionTuple = self.question_response()
            
            
            self.canvas = Canvas(width = WIDTH,
                                 height = HEIGHT,
                                 bg = THEME_COLORS["FOREGROUND"])
            self.question_text = self.canvas.create_text(
                WIDTH/2,
                HEIGHT/2,
                text = self.questionTuple[0],
                fill = THEME_COLORS["BACKGROUND"],
                font = ("Arial 15 italic"),
                width = WIDTH*.93)
            self.canvas.grid(row = 1,
                             column = 0,
                             columnspan = 2,
                             pady = 20)
            
            
            self.score = 0
            self.score_label = Label(self.window,
                                     font = ("Arial 10 bold"),
                                     fg = THEME_COLORS["FOREGROUND"],
                                     bg = THEME_COLORS["BACKGROUND"],
                                     text = "Score: 0")
            self.score_label.grid(row = 0, column = 1)
            
            
            trueImage = self.photoGenerator("./images/true.png")
            self.trueButton = Button(image = trueImage,
                                     command = lambda: self.userAnswer("True"))
            falseImage = self.photoGenerator("./images/false.png")
            self.falseButton = Button(image = falseImage,
                                      command = lambda: self.userAnswer("False"))
            self.trueButton.grid(row = 2,
                                 column = 1)
            self.falseButton.grid(row = 2,
                                  column = 0)
            
            
            self.window.mainloop()
        
        
        def question_response(self):
            questionTuple = self.questions.questionGenerator()
            return questionTuple


        def photoGenerator(self, path: str) -> PhotoImage: 
            return_image = PhotoImage(file = path)
            return return_image


        def userAnswer(self, buttonResponse: str):
            if self.questions.quizLength >= 0:
                if buttonResponse == self.questionTuple[1]:
                    self.score += 1
                    self.canvas.itemconfig(self.question_text,
                                        text = "Correct!")
                    self.canvas.config(bg = THEME_COLORS["CORRECT"])
                    self.score_label.config(text = f"Score: {self.score}")
                    self.window.after(1000,
                                    self.uiReset)
                else:
                    self.canvas.config(bg = THEME_COLORS["INCORRECT"])
                    self.canvas.itemconfig(self.question_text,
                                        text = "Incorrect!")
                    self.window.after(1000,
                                      self.uiReset)
            else:
                self.canvas.itemconfig(self.question_text,
                                       text = f"The quiz is over! You've scored {self.score} out of {self.questions.gameLength}.")
                self.score_label.configure(text = "")
                self.canvas.config(bg = THEME_COLORS["GAME_OVER"])
                self.trueButton.config(state = "disabled")
                self.falseButton.config(state = "disabled")
                
                
        def uiReset(self):
                self.canvas.config(bg = THEME_COLORS["FOREGROUND"])
                self.questionTuple = self.question_response()
                self.canvas.itemconfig(self.question_text,
                                    text = f"{self.questionTuple[0]}")



interface = Interface()