import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme("blue")
        self.title('Shopping Cart')
        self.minsize(400, 300)
        self.geometry('700x650')
        self.window1 = customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15)
        self.window1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.text1 = customtkinter.CTkLabel(
            master=self.window1,
            text="Shopping Cart.",
            font=('Arial', 60),
            width=90,
            height=35,
           
        )
        self.text1.place(x=115, y=90)

        self.text2 = customtkinter.CTkLabel(
            master=self.window1,
            text='Log in',
            font=('Arial',  30),
        )
        self.text2.place(x=267, y=250)

        self.entry1 = customtkinter.CTkEntry(
            placeholder_text='email',
            placeholder_text_color='#616178',
            master=self.window1,
            corner_radius=10,
            text_color='white',
            width=200,
            height=35
        )
        self.entry1.place(x=210, y=300)

        self.entry2 = customtkinter.CTkEntry(
            placeholder_text='senha',
            placeholder_text_color='#616178',
            master=self.window1,
            corner_radius=10,
            text_color='white',
            width=200,
            height=35
        )
        self.entry2.place(x=210, y=340 )

        self.buttom1 = customtkinter.CTkButton(
            master=self.window1,
            width=150,
            border_spacing=8,
            corner_radius=10,
            text='entrar',
            text_color='black',
            command=self.buttom_click
        )
        self.buttom1.place(x=235, y=390)



    def buttom_click(self):
        self.get_entry1()
        self.get_entry2()
        print('buttom click')

    def get_entry1(self):
        print(self.entry1.get())

    def get_entry2(self):
        print(self.entry2.get())