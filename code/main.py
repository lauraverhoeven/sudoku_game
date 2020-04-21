import tkinter as tk


class sudoku:
    def __init__(self, parent):
        self.parent = parent

        logo_image = tk.PhotoImage(file="../logo/logo.png")
        self.image = logo_image

        self.logo_frame = tk.Frame(
            self.parent, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.logo_frame.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=250)

        self.text_frame = tk.Frame(self.parent)
        self.text_frame.grid(row=2, column=2, sticky="", pady=5, padx=5)
        self.text = tk.Label(self.text_frame, text="press spacebar to start", font=(
            "Helvetica", 16), fg="gray")
        self.text.grid(row=2, column=2, sticky="")

        self.canvas = tk.Canvas(self.logo_frame, width=350, height=350)
        self.canvas.create_image((0, 10), image=self.image, anchor="nw")
        self.canvas.grid()
        self.parent.bind("<space>", self.difficultyScreen)

    def homeScreen(self, event):
        self.canvas.delete(tk.ALL)
        self.difficulty_text.destroy()
        self.difficulty_options.destroy()

        self.logo_frame = tk.Frame(
            self.parent, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.logo_frame.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=250)

        self.text_frame = tk.Frame(self.parent)
        self.text_frame.grid(row=2, column=2, sticky="", pady=5, padx=5)
        self.text = tk.Label(self.text_frame, text="press spacebar to start", font=(
            "Helvetica", 16), fg="gray")
        self.text.grid(row=2, column=1, sticky="")

        self.canvas = tk.Canvas(self.logo_frame, width=350, height=350)
        self.canvas.create_image((0, 10), image=self.image, anchor="nw")
        self.canvas.grid()
        self.parent.bind("<space>", self.difficultyScreen)

    def difficultyScreen(self, event):
        if event.char == ' ':
            self.text.destroy()
            self.canvas.delete(tk.ALL)
            self.logo_frame = tk.Frame(
                self.parent, width=350, height=125)
            self.logo_frame.grid(row=0, column=0, sticky="nw")
            self.canvas = tk.Canvas(self.logo_frame, width=350, height=125)
            self.canvas.create_image((0, 0), image=self.image, anchor="nw")
            self.canvas.grid(row=0, column=0, sticky="n")
            self.canvas.bind("<Button-1>", self.homeScreen)

            self.difficulty_options = tk.Frame(self.parent)
            self.difficulty_options.grid(row=1, column=1)

            self.difficulty_text = tk.Label(
                self.difficulty_options, text="Pick your difficulty", font=("Helvetica", 26), fg="black")
            self.difficulty_text.grid(row=1, column=1, pady=20)

            self.option_very_easy = tk.Button(self.difficulty_options, text="very easy", font=(
                "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
            self.option_very_easy.grid(row=2, column=1, pady=10)

            self.option_easy = tk.Button(self.difficulty_options, text="easy", font=(
                "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
            self.option_easy.grid(row=3, column=1, pady=10)

            self.option_medium = tk.Button(self.difficulty_options, text="medium", font=(
                "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
            self.option_medium.grid(row=4, column=1, pady=10)

            self.options_difficult = tk.Button(self.difficulty_options, text="difficult", font=(
                "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
            self.options_difficult.grid(row=5, column=1, pady=10)

            self.options_very_difficult = tk.Button(self.difficulty_options, text="very difficult", font=(
                "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
            self.options_very_difficult.grid(
                row=6, column=1, pady=10)


first = tk.Tk()
game = sudoku(first)
first.mainloop()
