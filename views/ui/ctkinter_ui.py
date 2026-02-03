import customtkinter as ctk
from views.messages import AppName
from core.converters import Converters
from utilities.utils import HelperFunctions
from views.messages import ErrorMessages

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
converter = Converters()
app_font_family = "Arial"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x1000")
        self.minsize(900, 1000)
        self.title("Morse ⇄ Text Translator")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.title_label = ctk.CTkLabel(self, text=AppName.app_name, font=(app_font_family, 60, "bold"))
        self.title_label.grid(row=0, column=1, pady=20, sticky="nsew")

        self.center_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.center_frame.grid(row=1, column=1, pady=20)
        self.center_frame.grid_columnconfigure(0, weight=0)
        self.center_frame.grid_columnconfigure(1, weight=0)
        self.center_frame.grid_columnconfigure(2, weight=0)

        self.left_label = ctk.CTkLabel(self.center_frame, text="Text to Morse", font=(app_font_family, 35))
        self.left_label.grid(row=0, column=0, padx=(0, 8), sticky="e")

        self.operation_type_switch_var = ctk.StringVar(value="text-to-morse")
        self.operation_type_switch = ctk.CTkSwitch(self.center_frame,
                                              offvalue="text-to-morse",
                                              onvalue="morse-to-text",
                                              variable=self.operation_type_switch_var,
                                              switch_width=100,
                                              switch_height=50,
                                              text="",
                                              fg_color="darkturquoise",
                                              progress_color="darkturquoise",
                                              button_color="#004F98",
                                              button_hover_color="#015EB4")
        self.operation_type_switch.grid(row=0, column=1, padx=8)

        self.right_label = ctk.CTkLabel(self.center_frame, text="Morse to Text", font=(app_font_family, 35))
        self.right_label.grid(row=0, column=2, padx=(8, 0), sticky="w")

        self.input_field = ctk.CTkTextbox(self,
        width=800,
        height=200,
        font=(app_font_family, 30),
        corner_radius=30,
        border_color="#313131",
        border_width=1)
        self.input_field.grid(row=2, column=0, columnspan=3, pady=(20, 0), padx=20, sticky="s")

        self.output_field = ctk.CTkTextbox(self,
        width=800,
        height=200,
        font=(app_font_family, 30),
        corner_radius=30,
        border_color="#313131",
        border_width=1)
        self.output_field.grid(row=3, column=0, columnspan=3, pady=(0, 20), padx=20, sticky="n")
        self.output_field.configure(state="disabled")

        self.translate_button = ctk.CTkButton(self,
        text="Translate",
        width=200,
        height=90,
        font=("Atial", 25),
        corner_radius=50,
        command=self.transate_button)
        self.translate_button.grid(row=4, column=1, sticky="n")


    def transate_button(self):
        input_text = self.input_field.get("1.0", "end").strip()
        if not input_text:
            result = ""
        elif self.operation_type_switch_var.get() == "text-to-morse":
            result = converter.text_to_morse(input_text)
        else:
            if HelperFunctions.is_morse_valid(input_text):
                result = converter.morse_to_text(input_text)
            else:
                result = ErrorMessages.invalid_morse_input

        self.output_field.configure(state="normal")
        self.output_field.delete("1.0", "end")
        self.output_field.insert("1.0", result)
        self.output_field.configure(state="disabled")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()