import tkinter as tk
import random

def play(user_input):
    com_choice = random.choice([-1, 0, 1])
    show_dict = {-1: "Rock", 0: "Paper", 1:"Scissor"}

    result_label.config(text=f"You chose {show_dict[user_input]} and the computer chose {show_dict[com_choice]}")

    if com_choice ==  user_input:
        outcome_label.config(text= "It is a draw")
    else:
        if (com_choice == -1 and user_input == 0) or (com_choice == 0 and user_input == 1) or (com_choice == 1 and user_input == -1):
            outcome_label.config(text= "You win")
        else:
            outcome_label.config(text= "You lose")


root = tk.Tk()
root.title("Rock, Paper and Scissor")

instruction_label = tk.Label(root,text = "Enter you choice of Rock, Paper or Scissor")
instruction_label.pack()

button_frame = tk.Frame()
button_frame.pack()

rock_button = tk.Button(button_frame, text= "Rock", command = lambda: play(-1) )
rock_button.pack(side = tk.LEFT, padx= 10)

paper_button = tk.Button(button_frame, text= "Paper", command = lambda: play(0))
paper_button.pack(side = tk.LEFT, padx= 10)

scissor_button = tk.Button(button_frame, text="Scissor", command = lambda: play(1))
scissor_button.pack(side = tk.LEFT, padx= 10)

result_label = tk.Label(root, text ="")
result_label.pack()

outcome_label = tk.Label(root, text ="")
outcome_label.pack()

root.mainloop()

