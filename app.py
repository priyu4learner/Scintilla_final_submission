from tkinter import *
from chatbot import get_response, bot_name, predict_class

BG_WHITE = "#abb2b9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#eaecee"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap(r"C:\Users\UMANG\Desktop\Chat_bot\bot.ico")
        self._setup_main_window()

    def _setup_main_window(self):
        self.window.title("Your travelling Agent")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_WHITE)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5,
                                cursor="arrow", state=DISABLED)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_WHITE, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, relx=0.008, rely=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.onclick)

        # send button
        send_btn = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_WHITE, command=lambda : self.onclick(None))
        send_btn.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def onclick(self, event):
        msg = self.msg_entry.get()
        self._insert_msg(msg, "You")

    def _insert_msg(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name} : {get_response(predict_class(msg))}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def run_app(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = ChatApplication()
    app.run_app()
