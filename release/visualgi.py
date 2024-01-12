import tkinter as tk
import os
import json

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interface")

        with open("list.txt", "r") as file:
            folder_names = file.read().splitlines()

        self.folder_var = tk.StringVar()
        self.folder_var.set("")
        self.folder_dropdown = tk.OptionMenu(self.root, self.folder_var, *folder_names)
        self.folder_dropdown.pack()

        self.button = tk.Button(self.root, text="OK !", command=self.display_json)
        self.button.pack()

        self.text_widget = tk.Text(self.root, wrap=tk.WORD)
        self.text_widget.pack()

        self.text_widget.tag_config("blue1", foreground="#6495ED")
        self.text_widget.tag_config("blue2", foreground="#4169E1")
        self.text_widget.tag_config("blue3", foreground="#0000FF")

    def display_json(self):
        restartbutton = tk.Button(self.root, text="Restart", command=self.restart)
        restartbutton.pack()
        selected_folder = self.folder_var.get()
        if selected_folder:
            modname = ""
            with open("name.txt", "r") as file:
                modname = file.read()
            folder_path = os.path.join("mod", "data", modname, "recipes", selected_folder)
            for root, dirs, files in os.walk(folder_path):
                json_files = [name for name in files if name.endswith(".json")]
                if json_files:
                    for i, json_file in enumerate(json_files[:3]):
                        json_path = os.path.join(root, json_file)
                        with open(json_path, "r") as file:
                            json_content = json.load(file)
                        formatted_json = json.dumps(json_content, indent=4)
                        if i == 0:
                            self.text_widget.insert(tk.END, formatted_json, "blue1")
                        elif i == 1:
                            self.text_widget.insert(tk.END, formatted_json, "blue2")
                        elif i == 2:
                            self.text_widget.insert(tk.END, formatted_json, "blue3")
                        self.text_widget.insert(tk.END, "\n\n")
                        copy_button = tk.Button(self.root, text="Copy Code", command=lambda content=formatted_json: self.copy_to_clipboard(content))
                        copy_button.pack()
                return
            json_files = [name for name in os.listdir(folder_path) if name.endswith(".json")]
            if json_files:
                for i, json_file in enumerate(json_files[:3]):
                    json_path = os.path.join(folder_path, json_file)
                    with open(json_path, "r") as file:
                        json_content = json.load(file)
                    formatted_json = json.dumps(json_content, indent=4)
                    if i == 0:
                        self.text_widget.insert(tk.END, formatted_json, "blue1")
                    elif i == 1:
                        self.text_widget.insert(tk.END, formatted_json, "blue2")
                    elif i == 2:
                        self.text_widget.insert(tk.END, formatted_json, "blue3")
                    self.text_widget.insert(tk.END, "\n\n")
                    copy_button = tk.Button(self.root, text="Copy Code",
                                            command=lambda content=formatted_json: self.copy_to_clipboard(content))
                    copy_button.pack()
                return
            self.text_widget.insert(tk.END, "Nothing has been find.....")


    def copy_to_clipboard(self, json_content):
        self.root.clipboard_clear()
        self.root.clipboard_append(json_content)

    def restart(self):
        self.root.destroy()
        os.startfile("visualgi.py")

app = MyApp()
app.root.mainloop()




