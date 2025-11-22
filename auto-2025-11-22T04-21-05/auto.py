import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.task_list = []
        self.task_var = tk.StringVar()
        
        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, width=30)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_display = tk.Listbox(self.root, width=40)
        self.task_display.pack(pady=10)
        
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_list.append(task)
            self.task_display.insert(tk.END, task)
        else:
            tk.messagebox.showerror("Error", "Task cannot be empty")

    def remove_task(self):
        try:
            index = self.task_display.curselection()[0]
            self.task_display.delete(index)
            del self.task_list[index]
        except IndexError:
            tk.messagebox.showerror("Error", "Please select a task to remove")
        
def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()