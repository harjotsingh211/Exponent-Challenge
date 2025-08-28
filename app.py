import tkinter as tk
import random

def new_question():
    global base, power, correct_answer
    base = random.randint(2, 9)      # base between 2–9
    power = random.randint(2, 5)     # exponent between 2–5
    correct_answer = base ** power
    question_label.config(text=f"What is {base}^{power}?")
    entry.delete(0, tk.END)
    result_label.config(text="")

def check_answer():
    user_input = entry.get()
    try:
        if int(user_input) == correct_answer:
            result_label.config(text=f"✅ Correct 🎉 ({base}^{power} = {correct_answer})", fg="lime")
        else:
            result_label.config(text="❌ Wrong", fg="red")
    except ValueError:
        result_label.config(text="Enter a valid number!", fg="yellow")

# Main window
root = tk.Tk()
root.title("⚡ Exponent Challenge")
root.configure(bg="black")

# Card frame
card = tk.Frame(root, bg="orange", bd=5, relief="ridge")
card.pack(padx=40, pady=40)

# Title
title = tk.Label(card, text="⚡ Exponent Challenge", font=("Arial", 20, "bold"), bg="orange", fg="white")
title.pack(pady=10)

# Question label
question_label = tk.Label(card, text="", font=("Arial", 16), bg="orange", fg="black")
question_label.pack(pady=5)

# Input box
entry = tk.Entry(card, font=("Arial", 14))
entry.pack(pady=5)

# Submit button
submit_btn = tk.Button(card, text="Submit", font=("Arial", 14, "bold"), bg="black", fg="orange",
                       activebackground="orange", activeforeground="black", command=check_answer)
submit_btn.pack(pady=10)

# Next question button
next_btn = tk.Button(card, text="Next Question", font=("Arial", 12, "bold"), bg="orange", fg="black",
                     command=new_question)
next_btn.pack(pady=5)

# Result label
result_label = tk.Label(card, text="", font=("Arial", 14, "bold"), bg="orange")
result_label.pack(pady=5)

# Start with a random question
new_question()

root.mainloop()
