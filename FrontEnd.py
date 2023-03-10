import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shopping Cart')
        self.minsize(400, 300)
        self.geometry('700x650')
        customtkinter.set_appearance_mode('dark')
        self.janela1 = customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15,fg_color='#245943')
        self.janela1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.texto1 = customtkinter.CTkLabel(
            master=self.janela1,
            text="Shopping Cart.",
            font=('Arial', 60),
            width=90,
            height=35,
            text_color='#9CDFC3',
        )
        self.texto1.place(x=115, y=90)
        self.entrada1 = customtkinter.CTkEntry(
            master=self.janela1,
            corner_radius=10,
            fg_color='#9CDFC3',
            text_color='black'
        )
        self.entrada1.place(x=240, y=300)
