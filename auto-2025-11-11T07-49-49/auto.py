import tkinter as tk

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.master, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(self.master, width=50)
        self.task_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
        else:
            tk.messagebox.showerror("Error", "Task cannot be empty")
    
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            tk.messagebox.showerror("Error", "No task selected")
    
def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()