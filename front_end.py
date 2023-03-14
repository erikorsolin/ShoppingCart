import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shopping Cart')
        self.minsize(400, 300)
        self.geometry('700x650')
        customtkinter.set_appearance_mode('dark')
        self.window1 = customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15,fg_color='#245943')
        self.window1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.text1 = customtkinter.CTkLabel(
            master=self.window1,
            text="Shopping Cart.",
            font=('Arial', 60),
            width=90,
            height=35,
            text_color='#9CDFC3',
        )
        self.text1.place(x=115, y=90)

        self.text2 = customtkinter.CTkLabel(
            master=self.window1,
            text='Login',
            font=('Arial', 30),
            text_color='#9CDFC3'
        )
        self.text2.place(x=267, y=250)

        self.entry1 = customtkinter.CTkEntry(
            master=self.window1,
            corner_radius=10,
            fg_color='#9CDFC3',
            text_color='black',
            width=130
        )
        self.entry1.place(x=240, y=300)

        self.entry2 = customtkinter.CTkEntry(
            master=self.window1,
            corner_radius=10,
            fg_color='#9CDFC3',
            text_color='black',
            width=130
        )
        self.entry2.place(x=240, y=330 )