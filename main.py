import requests
import tkinter as tk
from tkinter import messagebox, Text
from PIL import Image, ImageTk

def get_employees_information():
    response = requests.get(url="https://jsonplaceholder.typicode.com/users")
    return response.json()

def showing_employees_information():
    employees_response = get_employees_information()
    user_input = employee_name_var.get()
    found_employee = False

    for employee in employees_response:
        if employee["name"] == user_input:
            found_employee = True
            employee_info = ""
            for key, value in employee.items():
                employee_info += f"{key}: {value}\n"
            input_text.delete(1.0, tk.END)
            input_text.insert(tk.END, employee_info)
            break

    if not found_employee:
        messagebox.showinfo("Employee Not Found", f"No employee with the name '{user_input}' found. Please enter a valid name.")

def update_button_text(*args):
    employee_name = employee_name_var.get()
    if not employee_name:
        save_button.config(text="Show Employee's Info")
    else:
        save_button.config(text=f"Show {employee_name}'s Info")

def main():
    global employee_name_var
    window = tk.Tk()
    window.title("Employee Information")
    window.config(padx=30, pady=30)

    image = Image.open("employee.png")
    image.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(image)

    canvas = tk.Canvas(window, height=200, width=200)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo
    canvas.pack()

    title_info_label = tk.Label(window, text="Enter an employee name to explore:", font=("Verdana", 20, "normal"))
    title_info_label.pack()

    employee_name_var = tk.StringVar()
    employee_name_entry = tk.Entry(window, width=30, textvariable=employee_name_var)
    employee_name_entry.pack()
    employee_name_var.trace_add("write", update_button_text)

    employee_information_label = tk.Label(window, text="Employee's information", font=("Verdana", 20, "normal"))
    employee_information_label.pack()

    global input_text
    input_text = Text(window, width=55, height=20)
    input_text.pack()

    global save_button
    save_button = tk.Button(window, text="Show Employee's Info", command=showing_employees_information)
    save_button.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
