import tkinter as tk


class sudoku:
    def __init__(self, parent):
        self.parent = parent

        logo_image = tk.PhotoImage(file="logo.png")
        self.image = logo_image

        self.logo_frame = tk.Frame(
            self.parent, width=700, height=700, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.logo_frame.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=350)

        self.canvas = tk.Canvas(self.logo_frame, width=350, height=350)
        self.canvas.create_image((0, 10), image=self.image, anchor="nw")
        self.canvas.grid()
        self.parent.bind("<space>", self.key)

        # self.logo_button = tk.Button(
        #     self.logo_frame, image=self.image, width=350, height=100)
        # self.logo_button.grid(row=0, column=0, sticky="")
        # self.logo_button.bind("<Button-1>", self.optionsDifficulty)

        # print("you pressed" repr(event.char)
        # logo_image = tk.PhotoImage(file="logo.png")
        # self.image = logo_image

        # self.logo_frame = tk.Frame(
        #     self.parent, width=700, height=700, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        # self.logo_frame.grid(row=0, column=0, sticky="",
        #                      columnspan=5, rowspan=5, padx=350, pady=350)
        # self.logo_button = tk.Button(
        #     self.logo_frame, image=self.image, width=350, height=100)
        # self.logo_button.grid(row=0, column=0, sticky="")
        # self.logo_button.bind("<Button-1>", self.optionsDifficulty)

    def key(self, event):
        if event.char == ' ':
            self.canvas.delete(tk.ALL)

        # return repr(event.char)
        # # print("pressed" + repr(event.char))

    def startScreen(self, event):
        logo_image = tk.PhotoImage(file="logo.png")
        self.image = logo_image

        self.logo_frame = tk.Frame(
            self.parent, width=700, height=700, highlightcolor="white", highlightbackground="white", highlightthickness=3)
        self.logo_frame.grid(row=0, column=0, sticky="",
                             columnspan=5, rowspan=5, padx=350, pady=350)
        self.logo_button = tk.Button(
            self.logo_frame, image=self.image, width=350, height=100)
        self.logo_button.grid(row=0, column=0, sticky="")
        self.logo_button.bind("<Button-1>", self.optionsDifficulty)

    def optionsDifficulty(self, event):

        self.logo_frame_small = tk.Canvas(self.parent, width=350, height=100)
        self.logo_frame_small.create_image(
            (0, 0), image=self.image, anchor="nw")
        self.logo_frame_small.grid(row=0, column=0, sticky="nw")


first = tk.Tk()
game = sudoku(first)
first.mainloop()

#         self.welcome = tk.Frame(self.parent, bg="white")
#         self.welcome.grid(row=0, column=3, columnspan=5, padx=50)
#         self.welcometext = tk.Label(
#             self.welcome, text="", fg="gray", font=("Helvetica", 26))
#         self.welcometext.grid(row=0, column=3, columnspan=2, padx=200, pady=20)

#         self.buttons = tk.Frame(
#             self.parent, bg="white")
#         self.buttons.grid(row=1, column=0, padx=50, sticky="w")

#         self.white_space = tk.Frame(self.buttons, bg="white")
#         self.white_space.grid(row=1, column=0, pady=30)

#         # all the buttons of the different difficulties in levels
#         self.bvery_easy = tk.Button(
#             self.buttons, text="very easy", highlightcolor="black", highlightbackground="black", highlightthickness=1, width=15, height=2, font=("Helvetica", 14))
#         self.bvery_easy.grid(row=2, column=0, pady=20)

#         self.beasy = tk.Button(self.buttons, text="easy",
#                                highlightcolor="black", highlightbackground="black", highlightthickness=1, width=15, height=2, font=("Helvetica", 14))
#         self.beasy.grid(row=3, column=0, pady=20)

#         self.bmedium = tk.Button(
#             self.buttons, text="medium", highlightcolor="black", highlightbackground="black", highlightthickness=1, width=15, height=2, font=("Helvetica", 14))
#         self.bmedium.grid(row=4, column=0, pady=20)

#         self.bdifficult = tk.Button(
#             self.buttons, text="difficult", highlightcolor="black", highlightbackground="black", highlightthickness=1, width=15, height=2, font=("Helvetica", 14))
#         self.bdifficult.grid(row=5, column=0, pady=20)

#         self.bvery_difficult = tk.Button(
#             self.buttons, text="very difficult", highlightcolor="black", highlightbackground="black", highlightthickness=1, width=15, height=2, font=("Helvetica", 14))
#         self.bvery_difficult.grid(row=6, column=0, pady=20)

#         # quit button
#         self.quit_frame = tk.Frame(
#             self.parent, bg="white")
#         self.quit_frame.grid(row=10, column=10, padx=5, pady=5)

#         self.bquit = tk.Button(self.quit_frame, text="quit", highlightcolor="red",
#                                highlightbackground="red", highlightthickness=1, height=1, font=("Helvetica", 16))
#         self.bquit.grid(row=10, column=10, padx=5, pady=5, sticky="e")

#         # grid for the sudoku field
#         self.entire_field = tk.Frame(
#             self.parent, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2, width=550, height=550)
#         self.entire_field.grid(row=1, column=1, padx=5,
#                                pady=3, columnspan=9, rowspan=9)

#         # cell number one with cells 1 to 9 in this cell
#         ########################################################################################################################################
#         self.cell_one = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                  highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_one.grid(row=1, column=1, columnspan=3, rowspan=3)

#         self.cell_one_one = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_one.grid(row=1, column=1)

#         self.cell_one_two = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_two.grid(row=1, column=2)

#         self.cell_one_three = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_three.grid(row=1, column=3)

#         self.cell_one_four = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_four.grid(row=2, column=1)

#         self.cell_one_five = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_five.grid(row=2, column=2)

#         self.cell_one_six = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_six.grid(row=2, column=3)

#         self.cell_one_seven = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_seven.grid(row=3, column=1)

#         self.cell_one_eight = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_eight.grid(row=3, column=2)

#         self.cell_one_nine = tk.Frame(self.cell_one, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_one_nine.grid(row=3, column=3)

#         # cell number two with cells 10 to 18 in this cell
#         ########################################################################################################################################
#         self.cell_two = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                  highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_two.grid(row=1, column=4, columnspan=3, rowspan=3)

#         self.cell_two_one = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_one.grid(row=1, column=1)

#         self.cell_two_two = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_two.grid(row=1, column=2)

#         self.cell_two_three = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_three.grid(row=1, column=3)

#         self.cell_two_four = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_four.grid(row=2, column=1)

#         self.cell_two_five = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_five.grid(row=2, column=2)

#         self.cell_two_six = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_six.grid(row=2, column=3)

#         self.cell_two_seven = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_seven.grid(row=3, column=1)

#         self.cell_two_eight = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_eight.grid(row=3, column=2)

#         self.cell_two_nine = tk.Frame(self.cell_two, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_two_nine.grid(row=3, column=3)

#         # cell number three with cells 19 to 27 in this cell
#         ########################################################################################################################################
#         self.cell_three = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                    highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_three.grid(row=1, column=7, columnspan=3, rowspan=3)

#         self.cell_three_one = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_one.grid(row=1, column=1)

#         self.cell_three_two = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_two.grid(row=1, column=2)

#         self.cell_three_three = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_three.grid(row=1, column=3)

#         self.cell_three_four = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_four.grid(row=2, column=1)

#         self.cell_three_five = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_five.grid(row=2, column=2)

#         self.cell_three_six = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_six.grid(row=2, column=3)

#         self.cell_three_seven = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_seven.grid(row=3, column=1)

#         self.cell_three_eight = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_eight.grid(row=3, column=2)

#         self.cell_three_nine = tk.Frame(self.cell_three, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_three_nine.grid(row=3, column=3)

#         # cell number four with cells 28 to 36 in this cell
#         ########################################################################################################################################
#         self.cell_four = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                   highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_four.grid(row=4, column=1, columnspan=3, rowspan=3)

#         self.cell_four_one = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_one.grid(row=1, column=1)

#         self.cell_four_two = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_two.grid(row=1, column=2)

#         self.cell_four_three = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_three.grid(row=1, column=3)

#         self.cell_four_four = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_four.grid(row=2, column=1)

#         self.cell_four_five = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_five.grid(row=2, column=2)

#         self.cell_four_six = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_six.grid(row=2, column=3)

#         self.cell_four_seven = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_seven.grid(row=3, column=1)

#         self.cell_four_eight = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_eight.grid(row=3, column=2)

#         self.cell_four_nine = tk.Frame(self.cell_four, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_four_nine.grid(row=3, column=3)

#         # cell number five with cells 37 to 45 in this cell
#         ########################################################################################################################################
#         self.cell_five = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                   highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_five.grid(row=4, column=4, columnspan=3, rowspan=3)

#         self.cell_five_one = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_one.grid(row=1, column=1)

#         self.cell_five_two = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_two.grid(row=1, column=2)

#         self.cell_five_three = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_three.grid(row=1, column=3)

#         self.cell_five_four = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_four.grid(row=2, column=1)

#         self.cell_five_five = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_five.grid(row=2, column=2)

#         self.cell_five_six = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_six.grid(row=2, column=3)

#         self.cell_five_seven = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_seven.grid(row=3, column=1)

#         self.cell_five_eight = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_eight.grid(row=3, column=2)

#         self.cell_five_nine = tk.Frame(self.cell_five, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_five_nine.grid(row=3, column=3)

#         # cell number six with cells 46 to 54 in this cell
#         ########################################################################################################################################
#         self.cell_six = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                  highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_six.grid(row=4, column=7, columnspan=3, rowspan=3)

#         self.cell_six_one = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_one.grid(row=1, column=1)

#         self.cell_six_two = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_two.grid(row=1, column=2)

#         self.cell_six_three = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_three.grid(row=1, column=3)

#         self.cell_six_four = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_four.grid(row=2, column=1)

#         self.cell_six_five = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_five.grid(row=2, column=2)

#         self.cell_six_six = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                      highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_six.grid(row=2, column=3)

#         self.cell_six_seven = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_seven.grid(row=3, column=1)

#         self.cell_six_eight = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_eight.grid(row=3, column=2)

#         self.cell_six_nine = tk.Frame(self.cell_six, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_six_nine.grid(row=3, column=3)

#         # cell number seven with cells 55 to 63 in this cell
#         ########################################################################################################################################
#         self.cell_seven = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                    highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_seven.grid(row=7, column=1, columnspan=3, rowspan=3)

#         self.cell_seven_one = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_one.grid(row=1, column=1)

#         self.cell_seven_two = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_two.grid(row=1, column=2)

#         self.cell_seven_three = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_three.grid(row=1, column=3)

#         self.cell_seven_four = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_four.grid(row=2, column=1)

#         self.cell_seven_five = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_five.grid(row=2, column=2)

#         self.cell_seven_six = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_six.grid(row=2, column=3)

#         self.cell_seven_seven = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_seven.grid(row=3, column=1)

#         self.cell_seven_eight = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_eight.grid(row=3, column=2)

#         self.cell_seven_nine = tk.Frame(self.cell_seven, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_seven_nine.grid(row=3, column=3)

#         # cell number eight with cells 64 to 72 in this cell
#         ########################################################################################################################################
#         self.cell_eight = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                    highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_eight.grid(row=7, column=4, columnspan=3, rowspan=3)

#         self.cell_eight_one = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_one.grid(row=1, column=1)

#         self.cell_eight_two = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_two.grid(row=1, column=2)

#         self.cell_eight_three = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_three.grid(row=1, column=3)

#         self.cell_eight_four = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_four.grid(row=2, column=1)

#         self.cell_eight_five = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_five.grid(row=2, column=2)

#         self.cell_eight_six = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_six.grid(row=2, column=3)

#         self.cell_eight_seven = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_seven.grid(row=3, column=1)

#         self.cell_eight_eight = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_eight.grid(row=3, column=2)

#         self.cell_eight_nine = tk.Frame(self.cell_eight, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_eight_nine.grid(row=3, column=3)

#         # cell number nine with cells 73 to 81 in this cell
#         ########################################################################################################################################
#         self.cell_nine = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#                                   highlightbackground="black", highlightthickness=2, width=183, height=183)
#         self.cell_nine.grid(row=7, column=7, columnspan=3, rowspan=3)

#         self.cell_nine_one = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_one.grid(row=1, column=1)

#         self.cell_nine_two = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_two.grid(row=1, column=2)

#         self.cell_nine_three = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_three.grid(row=1, column=3)

#         self.cell_nine_four = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_four.grid(row=2, column=1)

#         self.cell_nine_five = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_five.grid(row=2, column=2)

#         self.cell_nine_six = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                       highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_six.grid(row=2, column=3)

#         self.cell_nine_seven = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_seven.grid(row=3, column=1)

#         self.cell_nine_eight = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                         highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_eight.grid(row=3, column=2)

#         self.cell_nine_nine = tk.Frame(self.cell_nine, bg="white", highlightcolor="black",
#                                        highlightbackground="black", highlightthickness=1, width=61, height=61)
#         self.cell_nine_nine.grid(row=3, column=3)

#         # self.cell_two = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_two.grid(row=1, column=2)

#         # self.cell_three = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                            highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_three.grid(row=1, column=3)

#         # self.cell_four = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                           highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_four.grid(row=1, column=4)

#         # self.cell_five = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                           highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_five.grid(row=1, column=5)

#         # self.cell_six = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                          highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_six.grid(row=1, column=6)

#         # self.cell_seven = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                            highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_seven.grid(row=1, column=7)

#         # self.cell_eight = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                            highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_eight.grid(row=1, column=8)

#         # self.cell_nine = tk.Frame(self.entire_field, bg="white", highlightcolor="black",
#         #                           highlightbackground="black", highlightthickness=1, width=61, height=61)
#         # self.cell_nine.grid(row=1, column=9)

#         # self.cells = {}
#         # for self.row in range(3):
#         #     for self.column in range(3):
#         #         self.cell = tk.Frame(self.entire_field, bg='white', highlightbackground="black",
#         #                              highlightcolor="black", highlightthickness=2,
#         #                              width=183, height=183,  padx=3,  pady=3)
#         #         self.cell.grid(row=self.row, column=self.column)
#         #         self.cells[(self.row, self.column)] = self.cell

#         # self.cell_one = tk.Frame(self.cells[(0, 0)], bg='white', highlightbackground="black",
#         #                          highlightcolor="black", highlightthickness=1, width=61, height=61)
#         # self.cell_one.grid(row=0, column=0)

#         # self.cells_in_cell = {}
#         # for self.row in range(9):
#         #     for self.column in range(9):
#         #         self.cells = tk.Frame(self.entire_field, bg='white', highlightbackground="black",
#         #                               highlightcolor="black", highlightthickness=1,
#         #                               width=61, height=61,  padx=3,  pady=3)
#         #         self.cells.grid(row=self.row, column=self.column)
#         #         self.cells_in_cell[(self.row, self.column)] = self.cells

#         # self.cells_in_cell = {}
#         # for self.row in range(3):
#         #     for self.column in range(3):
#         #         self.cell_in_cell = tk.Frame(self.entire_field, bg='white', highlightbackground="black",
#         #                                      highlightcolor="black", highlightthickness=1,
#         #                                      width=90, height=90,  padx=3,  pady=3)
#         #         self.cell_in_cell.grid(row=self.row, column=self.column)
#         #         self.cells_in_cell[(self.row, self.column)] = self.cell_in_cell

#         # for self.cell in self.cells:
#         #     for self.row in range(3):
#         #         for self.column in range(3):
#         #             self.cell_in_cell = tk.Frame(self.cell, bg='white', highlightbackground="black",
#         #                                          highlightcolor="black", highlightthickness=1, width=90, height=90, padx=3, pady=3)
#         #             self.cell_in_cell.grid(row=self.row, column=self.column)

#         # self.cells_in_cell = {}
#         # for self.row in range(3):
#         #     for self.column in range(3):
#         #         self.cell_in_cell = tk.Frame(self.cell, bg='white', highlightbackground="black",
#         #                              highlightcolor="black", highlightthickness=2,
#         #                              width=90, height=90,  padx=3,  pady=3)
#         #         self.cell.grid(row=self.row, column=self.column)
#         #         self.cells[(self.row, self.column)] = self.cell

#         # self.cell_one = tk.Frame(
#         #     self.entire_field, bg="gray", width=90, height=90)
#         # self.cell_one.grid(row=1, column=0, padx=3, pady=3)

#         # self.cell_two = tk.Frame(
#         #     self.entire_field, bg="white", width=90, height=90)
#         # self.cell_two.grid(row=1, column=1, padx=3, pady=3)

#         # self.cell_three = tk.Frame(
#         #     self.entire_field, bg="gray", width=90, height=90)
#         # self.cell_three.grid(row=1, column=2, padx=3, pady=3)

#         # self.cell_four = tk.Frame(
#         #     self.entire_field, bg="white", width=90, height=90)
#         # self.cell_four.grid(row=2, column=0, padx=3, pady=3)

#         # self.cell_five = tk.Frame(
#         #     self.entire_field, bg="gray", width=90, height=90)
#         # self.cell_five.grid(row=2, column=1, padx=3, pady=3)

#         # self.cell_six = tk.Frame(
#         #     self.entire_field, bg="white", width=90, height=90)
#         # self.cell_six.grid(row=2, column=2, padx=3, pady=3)

#         # self.cell_seven = tk.Frame(
#         #     self.entire_field, bg="gray", width=90, height=90)
#         # self.cell_seven.grid(row=3, column=0, padx=3, pady=3)

#         # self.cell_eight = tk.Frame(
#         #     self.entire_field, bg="white", width=90, height=90)
#         # self.cell_eight.grid(row=3, column=1, padx=3, pady=3)
#         # self.cell_nine = tk.Frame(
#         #     self.entire_field, bg="gray", width=90, height=90)
#         # self.cell_nine.grid(row=3, column=2, padx=3, pady=3)
#         # self.cell_one_one = tk.Frame(
#         #     self.cell_one, bg="white", width=10, height=10)
#         # self.cell_one.grid(row=1, column=0, padx=3, pady=3)


# first = tk.Tk()
# game = sudoku(first)
# first.mainloop()

# # cells = {}
# # for row in range(9):
# #     for column in range(9):
# #         cell = tk.Frame(center, bg='white', highlightbackground="black",
# #                      highlightcolor="black", highlightthickness=1,
# #                      width=100, height=100,  padx=3,  pady=3)
# #         cell.grid(row=row, column=column)
# #         cells[(row, column)] = cell

# # self.cells = {}
# # for self.row in range(9):
# #     for self.column in range(9):
# #         self.cell = tk.Frame(self.parent, bg='white', highlightbackground="black",
# #                              highlightcolor="black", highlightthickness=1,
# #                              width=50, height=50,  padx=3,  pady=3)
# #         self.cell.grid(row=self.row, column=self.column)
# #         self.cells[(self.row, self.column)] = self.cell

# # self.parent = parent
