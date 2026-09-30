import tkinter as tk
from tkinter import messagebox


# ---------------- Calculate Function ----------------
def calculate():
    try:
        rent = float(rent_entry.get())
        food = float(food_entry.get())
        electricity_units = float(electricity_entry.get())
        charge_per_unit = float(charge_entry.get())
        persons = int(persons_entry.get())

        if persons <= 0:
            messagebox.showerror(
                "Error",
                "Number of persons must be greater than 0"
            )
            return

        total_electricity_bill = electricity_units * charge_per_unit
        total_expenses = food + rent + total_electricity_bill
        amount_per_person = total_expenses / persons

        # Display result
        result_label.config(
            text=f"₹ {amount_per_person:.2f}",
            fg="#00ff99"
        )

        details_label.config(
            text=f"Electricity Bill: ₹{total_electricity_bill:.2f}\n"
                 f"Total Expenses: ₹{total_expenses:.2f}"
        )

        animate_result()

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in all fields."
        )


# ---------------- Animation ----------------
def animate_result():
    result_label.place(x=150, y=420)

    def move():
        x = result_label.winfo_x()

        if x < 250:
            result_label.place(x=x + 5, y=420)
            root.after(10, move)

    move()


# ---------------- Clear Function ----------------
def clear():
    rent_entry.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    electricity_entry.delete(0, tk.END)
    charge_entry.delete(0, tk.END)
    persons_entry.delete(0, tk.END)

    result_label.config(text="")
    details_label.config(text="")


# ---------------- Main Window ----------------
root = tk.Tk()

# Calculator Name
root.title("Bhura Singh Meena - Hostel Expense Calculator")

root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#101820")


# ---------------- Title ----------------
title = tk.Label(
    root,
    text="🏠 Bhura Singh Meena",
    font=("Arial", 24, "bold"),
    bg="#101820",
    fg="#00ff99"
)
title.pack(pady=25)


subtitle = tk.Label(
    root,
    text="Hostel Expense Calculator",
    font=("Arial", 14, "bold"),
    bg="#101820",
    fg="white"
)
subtitle.pack(pady=5)


description = tk.Label(
    root,
    text="Calculate the amount each person needs to pay",
    font=("Arial", 11),
    bg="#101820",
    fg="#cccccc"
)
description.pack(pady=5)


# ---------------- Input Frame ----------------
frame = tk.Frame(
    root,
    bg="#1c2733",
    padx=25,
    pady=20
)
frame.pack(pady=20)


def create_input(label_text, row):
    label = tk.Label(
        frame,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="#1c2733",
        fg="white"
    )
    label.grid(
        row=row,
        column=0,
        sticky="w",
        pady=8
    )

    entry = tk.Entry(
        frame,
        font=("Arial", 11),
        width=25,
        bg="#273746",
        fg="white",
        insertbackground="white"
    )
    entry.grid(
        row=row,
        column=1,
        padx=15,
        pady=8
    )

    return entry


rent_entry = create_input("🏠 Rent:", 0)
food_entry = create_input("🍔 Food:", 1)
electricity_entry = create_input("⚡ Electricity Units:", 2)
charge_entry = create_input("💰 Charge Per Unit:", 3)
persons_entry = create_input("👥 Number of Persons:", 4)


# ---------------- Buttons ----------------
button_frame = tk.Frame(
    root,
    bg="#101820"
)
button_frame.pack(pady=10)


calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    command=calculate,
    font=("Arial", 12, "bold"),
    bg="#00aa66",
    fg="white",
    width=12,
    cursor="hand2"
)
calculate_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    font=("Arial", 12, "bold"),
    bg="#d9534f",
    fg="white",
    width=12,
    cursor="hand2"
)
clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# ---------------- Result ----------------
result_title = tk.Label(
    root,
    text="Amount Per Person",
    font=("Arial", 15, "bold"),
    bg="#101820",
    fg="white"
)
result_title.place(
    x=210,
    y=390
)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 25, "bold"),
    bg="#101820"
)
result_label.place(
    x=150,
    y=420
)


details_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#101820",
    fg="#dddddd"
)
details_label.pack(
    pady=(100, 10)
)


# ---------------- Footer ----------------
footer = tk.Label(
    root,
    text="© Bhura Singh Meena | Python GUI Project",
    font=("Arial", 9),
    bg="#101820",
    fg="#888888"
)
footer.pack(
    side="bottom",
    pady=10
)


# ---------------- Run Application ----------------
root.mainloop()