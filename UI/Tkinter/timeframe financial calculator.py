import tkinter as tk


def calculate_desired():
    timeframe = float(timeframe_entry.get())
    goal = float(goal_entry.get())
    in_am = float(in_am_entry.get())
    val = goal-in_am

    if timeframe <= 0:
        result_label.config(text="Error: Timeframe should be greater than 0!")
    else:
        result = round((val / timeframe), 2)
        result_label.config(text=f"You must get {result} per year or {round(result / 12, 2)} per month.", relief=tk.GROOVE, bg="AliceBlue")


root = tk.Tk()
root.title('Target amount')
root.iconbitmap('C:/Users/Tsimos/Downloads/Icons/python_square_icon_icon_257067.ico')
root.config(bg="AliceBlue")

tk.Label(root, text="Target amount:", bg="AliceBlue").pack()
goal_entry = tk.Entry(root, bg="lightblue", borderwidth=5)
goal_entry.pack()

tk.Label(root, text="Initial amount:", bg="AliceBlue").pack()
in_am_entry = tk.Entry(root, bg="lightblue", borderwidth=5)
in_am_entry.pack()

tk.Label(root, text="In how many years do you want to hit the target?\n (Timeframe)", bg="AliceBlue").pack()
timeframe_entry = tk.Entry(root, bg="lightblue", borderwidth=5)
timeframe_entry.pack()

tk.Button(root, text="Calculate", command=calculate_desired).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
