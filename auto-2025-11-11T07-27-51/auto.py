import tkinter as tk
from tkinter import scrolledtext

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def save_file(self):
        try:
            file_content = self.text_area.get("1.0", tk.END)
            with open("saved_file.txt", "w") as file:
                file.write(file_content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = TextEditorApp(root)

    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save", command=app.save_file)

    root.mainloop()

if __name__ == "__main__":
    main()