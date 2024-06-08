from tkinter import *
from chat import get_response, bot_name

BG_GRAY = "#C1C3C6"
BG_COLOR = "#ECEEF1"
TEXT_COLOR = "#000000"
USER_COLOR = "#0079FA"
BOT_COLOR = "#1CC800"

FONT = "Helvetica 13"
FONT_BOLD = "Helvetica 12 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.geometry("500x550")
        self.window.resizable(width=True, height=True)
        self.window.configure(bg=BG_COLOR)

        # Head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.grid(row=1, column=0, columnspan=3, sticky="ew")

        # Frame for messages
        self.message_frame = Frame(self.window, bg=BG_COLOR)
        self.message_frame.grid(row=2, column=0, columnspan=3, rowspan=1, sticky="nsew")

        # Scroll bar
        scrollbar = Scrollbar(self.message_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Text widget
        self.text_widget = Text(self.message_frame, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=15, pady=5, wrap=WORD, yscrollcommand=scrollbar.set)
        self.text_widget.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.config(command=self.text_widget.yview)

        # Message entry box
        self.msg_entry = Entry(self.window, bg="#BBD1FF", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5, padx=5)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(self.window, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.grid(row=3, column=2, sticky="ew", pady=5, padx=5)

        # Bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=1)
        bottom_label.grid(row=4, column=0, columnspan=3, sticky="ew")

        # Set row and column weights
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=0)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You", USER_COLOR)

    def _insert_message(self, msg, sender, color):
        if not msg:
            return

        self.msg_entry.delete(0, END)

        # Format the message
        message_text = f"{sender}: {msg}\n"
        self.text_widget.insert(END, message_text, f"{color}_text")
        self.text_widget.tag_configure(f"{color}_text", foreground=color)

        # Ensure a new line after each message
        self.text_widget.insert(END, '\n')

        # Scroll to the bottom
        self.text_widget.yview_moveto(1.0)

        response_msg = f"{bot_name}: {get_response(msg)}\n"

        # Format the bot's response
        self.text_widget.insert(END, response_msg, f"{BOT_COLOR}_text")
        self.text_widget.tag_configure(f"{BOT_COLOR}_text", foreground=BOT_COLOR)

        # Ensure a new line after each response
        self.text_widget.insert(END, '\n')

        # Update the scrollbar
        self.text_widget.yview_moveto(1.0)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
