import tkinter
import customtkinter




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.set_appearance_mode("dark")
        self.set_default_color_theme("green")
        self.title('Shopping Cart')
        self.geometry('800x650')

        self.frame = self.customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)





if __name__ == "main":
    app = App()
    app.mainloop()

