import tkinter as tk
from tkinter import messagebox, font

class TodoListApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="lightblue")

        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, height=10, width=50, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="lightyellow")
        self.task_listbox.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview, bg="lightblue")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(self.root, bg="lightblue")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=40, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task, bg="green", fg="white", font=("Helvetica", 10))
        self.add_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="blue", fg="white", font=("Helvetica", 10))
        self.update_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_as_done, bg="orange", fg="white", font=("Helvetica", 10))
        self.mark_done_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="red", fg="white", font=("Helvetica", 10))
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]] + " (Done)"
            self.tasks[selected_task_index[0]] = task
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, task)
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
