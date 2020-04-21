import tkinter as tk


class sudoku:
    def __init__(self, parent):
        self.parent = parent

        logo_image = tk.PhotoImage(file="../logo/logo.png")
        self.image_logo = logo_image

        self.frame_logo = tk.Frame(
            self.parent, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.frame_logo.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=250)

        self.frame_text = tk.Frame(self.parent)
        self.frame_text.grid(row=2, column=2, sticky="", pady=5, padx=5)
        self.text = tk.Label(self.frame_text, text="press spacebar to start", font=(
            "Helvetica", 16), fg="gray")
        self.text.grid(row=2, column=2, sticky="")

        self.logo = tk.Canvas(self.frame_logo, width=350, height=350)
        self.logo.create_image((0, 10), image=self.image_logo, anchor="nw")
        self.logo.grid()
        self.parent.bind("<space>", self.difficultyScreen)

    def homeScreen(self, event):
        # self.logo.delete(tk.ALL)
        self.frame_logo.destroy()
        # self.label_difficulty_options.destroy()
        self.frame_difficulty_options.destroy()
        self.frame_image_rules.destroy()
        # self.button_very_easy.destroy()
        # self.button_easy.destroy()
        # self.button_medium.destroy()
        # self.button_difficult.destroy()
        # self.button_very_difficult.destroy()

        self.frame_logo = tk.Frame(
            self.parent, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.frame_logo.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=250)

        self.frame_text = tk.Frame(self.parent)
        self.frame_text.grid(row=2, column=2, sticky="", pady=5, padx=5)
        self.text = tk.Label(self.frame_text, text="press spacebar to start", font=(
            "Helvetica", 16), fg="gray")
        self.text.grid(row=2, column=2, sticky="")

        self.logo = tk.Canvas(self.frame_logo, width=350, height=350)
        self.logo.create_image((0, 10), image=self.image_logo, anchor="nw")
        self.logo.grid()
        self.parent.bind("<space>", self.difficultyScreen)

    def difficultyScreen(self, event):
        # still have to add the links to the buttons
        # add the link to the rule page in the hamburger_menu_icon
        # maybe a different logo

        self.text.destroy()
        self.logo.delete(tk.ALL)

        small_logo_header = tk.PhotoImage(file="../logo/logo_small.png")
        self.logo_header = small_logo_header

        self.frame_logo = tk.Frame(self.parent)
        self.frame_logo.grid(row=0, column=0, sticky="nw")
        self.logo = tk.Canvas(self.frame_logo, width=125, height=100)
        self.logo.create_image((0, 0), image=self.logo_header, anchor="nw")
        self.logo.grid(row=0, column=0, sticky="n")
        self.logo.bind("<Button-1>", self.homeScreen)

        hamburgermenu_icon = tk.PhotoImage(
            file="../images/hamburger_menu_gray.png")
        self.hamburgermenu_icon = hamburgermenu_icon

        self.frame_image_rules = tk.Frame(self.parent)
        self.frame_image_rules.grid(row=0, padx=130, sticky="nw")
        self.image_rules = tk.Canvas(
            self.frame_image_rules, width=60, height=100)
        self.image_rules.create_image(
            (0, 0), image=self.hamburgermenu_icon, anchor="nw")
        self.image_rules.grid(row=0, pady=25)

        self.frame_difficulty_options = tk.Frame(self.parent)
        self.frame_difficulty_options.grid(row=0, pady=150, padx=400)

        self.label_difficulty_options = tk.Label(
            self.frame_difficulty_options, text="Pick your difficulty", font=("Helvetica", 26), fg="black")
        self.label_difficulty_options.grid(
            row=0, pady=20, sticky="n")

        self.button_very_easy = tk.Button(self.frame_difficulty_options, text="very easy", font=(
            "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
        self.button_very_easy.grid(row=2, pady=10)

        self.button_easy = tk.Button(self.frame_difficulty_options, text="easy", font=(
            "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
        self.button_easy.grid(row=3, pady=10)

        self.button_medium = tk.Button(self.frame_difficulty_options, text="medium", font=(
            "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
        self.button_medium.grid(row=4, pady=10)

        self.button_difficult = tk.Button(self.frame_difficulty_options, text="difficult", font=(
            "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
        self.button_difficult.grid(row=5, pady=10)

        self.button_very_difficult = tk.Button(self.frame_difficulty_options, text="very difficult", font=(
            "Helvetica", 16), fg="black", highlightcolor="gray", highlightbackground="gray", highlightthickness=1, height=2, width=20)
        self.button_very_difficult.grid(
            row=6, pady=10)


first = tk.Tk()
game = sudoku(first)
first.mainloop()
