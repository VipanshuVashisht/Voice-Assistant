import tkinter as tk
import threading
import assistant

class PersonalAssistantGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Assistant")
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.window, text="Welcome to Personal Assistant!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.query_label = tk.Label(self.window, text="What can I help you with?", font=("Arial", 12))
        self.query_label.pack(pady=10)

        self.query_entry = tk.Entry(self.window, width=50, font=("Arial", 12))
        self.query_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Submit", font=("Arial", 12), command=self.submit_query)
        self.submit_button.pack(pady=10)

        self.response_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.response_label.pack(pady=10)

    def submit_query(self):
        query = self.query_entry.get()
        self.query_entry.delete(0, tk.END)
        self.response_label.configure(text="Processing...")

        response_thread = threading.Thread(target=self.process_query, args=(query,))
        response_thread.start()

    def process_query(self, query):
        response = assistant.respond(query)
        self.response_label.configure(text=response)

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = PersonalAssistantGUI()
    gui.start()
