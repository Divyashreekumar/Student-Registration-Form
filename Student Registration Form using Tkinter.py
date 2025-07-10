import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
root.title("Student Registration Form")

student_data = [[1, 'John', 'john@gmail.com', 'Python'],
                [2, 'Smith', 'smith@gmail.com', 'C'],
                [3, 'Lucy', 'lucy@gmail.com', 'Python,C'],
                [4, 'Jack', 'jeffry@gmail.com', 'Python,C,C++'],
                [5, 'Jeffry', 'jeffry@gmail.com', 'Python'],
                [6, 'May', 'mary@gmail.com', 'C']]

def load_student_data():
    for item in record_table.get_children():
        record_table.delete(item)

    for r in range(len(student_data)):
        record_table.insert(parent='', index='end', text='',
                            iid=r, values=student_data[r])

def put_student_in_entry(index):
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_courses.delete(0, tk.END)

    stud_id = student_data[index][0]
    stud_name = student_data[index][1]
    stud_email = student_data[index][2]
    stud_courses = student_data[index][3]

    student_id.insert(0, stud_id)
    student_name.insert(0, stud_name)
    student_email.insert(0, stud_email)
    student_courses.insert(0, stud_courses)

def clear_student_data():
    student_id.delete(0, tk.END)
    student_name.delete(0, tk.END)
    student_email.delete(0, tk.END)
    student_courses.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    load_student_data()

def add_student_data(stud_id, stud_name, stud_email, stud_courses):
    student_data.append([stud_id, stud_name, stud_email, stud_courses])
    load_student_data()
    clear_student_data()

def update_student_data(stud_id, stud_name, stud_email, stud_courses, index):
    student_data[index] = [stud_id, stud_name, stud_email, stud_courses]
    load_student_data()
    clear_student_data()

def delete_student_data(index):
    del student_data[index]
    load_student_data()
    clear_student_data()

def find_student_by_id(stud_id):
    if stud_id != '':
        student_data_index = []

        for data in student_data:
            if str(stud_id) in str(data[0]):
                student_data_index.append(student_data.index(data))

        for item in record_table.get_children():
            record_table.delete(item)

        for r in student_data_index:
            record_table.insert(parent='', index='end', text='',
                                iid=r, values=student_data[r])
    else:
        load_student_data()

def on_update():
    selected_item = record_table.selection()
    if selected_item:
        index = int(selected_item[0])  
        update_student_data(student_id.get(), student_name.get(),
                            student_email.get(), student_courses.get(), index)
    else:
        messagebox.showwarning("No Selection", "Please select a record to update.")

def on_delete():
    selected_item = record_table.selection()
    if selected_item:
        index = int(selected_item[0]) 
        delete_student_data(index)
    else:
        messagebox.showwarning("No Selection", "Please select a record to delete.")

head_frame = tk.Frame(root)

heading_lb = tk.Label(head_frame, text="Student Registration form", font=('Bold', 13), bg='blue')
heading_lb.pack(fill=tk.X, pady=5)

student_id_lb = tk.Label(head_frame, text="Student Id :", font=('Bold', 10))
student_id_lb.place(x=0, y=50)

student_id = tk.Entry(head_frame, font=('Bold', 10))
student_id.place(x=110, y=50, width=180)

student_name_lb = tk.Label(head_frame, text="Student Name :", font=('Bold', 10))
student_name_lb.place(x=0, y=100)

student_name = tk.Entry(head_frame, font=('Bold', 10))
student_name.place(x=110, y=100, width=180)

student_email_lb = tk.Label(head_frame, text="Student Email :", font=('Bold', 10))
student_email_lb.place(x=0, y=150)

student_email = tk.Entry(head_frame, font=('Bold', 10))
student_email.place(x=110, y=150, width=180)

student_courses_lb = tk.Label(head_frame, text="Student Courses :", font=('Bold', 10))
student_courses_lb.place(x=0, y=200)

student_courses = tk.Entry(head_frame, font=('Bold', 10))
student_courses.place(x=110, y=200, width=180)

register_btn = tk.Button(head_frame, text="Register", font=('Bold', 12),
                         command=lambda: add_student_data(student_id.get(),
                                                          student_name.get(),
                                                          student_email.get(),
                                                          student_courses.get()))
register_btn.place(x=0, y=250)

update_btn = tk.Button(head_frame, text="Update", font=('Bold', 12), command=on_update)
update_btn.place(x=85, y=250)

delete_btn = tk.Button(head_frame, text="Delete", font=('Bold', 12), command=on_delete)
delete_btn.place(x=163, y=250)

clear_btn = tk.Button(head_frame, text="Clear", font=('Bold', 12), command=clear_student_data)
clear_btn.place(x=235, y=250)

head_frame.pack(pady=10)
head_frame.pack_propagate(False)
head_frame.configure(width=400, height=300)

search_bar_frame = tk.Frame(root)

search_lb = tk.Label(search_bar_frame, text="Search Student By Id:", font=('Bold', 10))
search_lb.pack(anchor=tk.W)

search_entry = tk.Entry(search_bar_frame, font=('Bold', 10))
search_entry.pack(anchor=tk.W)
search_entry.bind('<KeyRelease>', lambda e: find_student_by_id(search_entry.get()))

search_bar_frame.pack(pady=0)
search_bar_frame.pack_propagate(False)
search_bar_frame.configure(width=400, height=50)

record_frame = tk.Frame(root)

record_lb = tk.Label(record_frame, text="Select record for delete or update", bg="blue", font=('Bold', 13))
record_lb.pack(fill=tk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=tk.X, pady=5)

record_table['columns'] = ['Id', 'Name', 'Email', 'Courses']
record_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
record_table.column('Id', anchor=tk.W, width=50)
record_table.column('Name', anchor=tk.W, width=100)
record_table.column('Email', anchor=tk.W, width=120)
record_table.column('Courses', anchor=tk.W, width=160)

record_table.heading('Id', text='Id', anchor=tk.W)
record_table.heading('Name', text='Name', anchor=tk.W)
record_table.heading('Email', text='Email', anchor=tk.W)
record_table.heading('Courses', text='Courses', anchor=tk.W)

record_table.bind('<<TreeviewSelect>>', lambda e: put_student_in_entry(int(record_table.selection()[0])))

record_frame.pack(pady=10)
record_frame.pack_propagate(False)
record_frame.configure(width=400, height=200)

load_student_data()

root.mainloop()
