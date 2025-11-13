import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_task = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task)
            del self.tasks[selected_task]
        except IndexError:
            pass

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = []

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()