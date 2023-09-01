import tkinter as tk
from tkinter import ttk

class BasicGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Textbox Example")
        self.root.geometry("600x400")

        # Apply the custom dark theme
        self.custom_style = self.set_custom_style()

        self.create_widgets()

    def set_custom_style(self):
        custom_style = ttk.Style()
        custom_style.theme_use("clam")  # Use the 'clam' theme as a base
        custom_style.configure("TLabel", foreground="white", background="black", font=("Helvetica", 24))
        custom_style.configure("TButton", foreground="white", background="black", font=("Helvetica", 16))
        custom_style.configure("TFrame", background="black")
        custom_style.configure("TText", foreground="white", background="black", font=("Helvetica", 12))
        return custom_style

    def call_api(self):
        user_input = self.textbox.get("1.0", "end-1c")

        # Prepare the payload (instead of making an API call)
        payload = {"user_input": user_input}

        return payload
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style="TFrame")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = ttk.Label(main_frame, text="API Interface")
        title_label.grid(row=0, column=0, pady=10)

        self.display_label = ttk.Label(main_frame, text="", font=("Helvetica", 16))
        self.display_label.grid(row=1, column=0, pady=10)

        self.textbox = tk.Text(main_frame, height=8, font=("Helvetica", 12))
        self.textbox.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

        call_button = ttk.Button(main_frame, text="Send Payload", command=self.call_api)
        call_button.grid(row=3, column=0, pady=10)

        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = BasicGui()
    gui.run()
