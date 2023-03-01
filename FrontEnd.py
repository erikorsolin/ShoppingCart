import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shopping Cart')
        self.geometry('700x650')
        customtkinter.set_appearance_mode('light')
        self.frame = customtkinter.CTkFrame(master=self, width=650, height=600, corner_radius=15,fg_color='#0DD473')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.texto = customtkinter.CTkLabel(master=self.frame, fg_color='white')
        
        self.entrada = customtkinter.CTkEntry(master=self.frame, placeholder_text='Digite seu nome')
        self.entrada.pack(padx=650, pady=600)
