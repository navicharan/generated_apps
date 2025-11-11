import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=20)
        
        self.task_listbox = tk.Listbox(self.root, width=40)
        self.task_listbox.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)
        
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.load_tasks()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
    
    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()
        except IndexError:
            pass
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [task.strip() for task in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()