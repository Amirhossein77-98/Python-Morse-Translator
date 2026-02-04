import customtkinter as ctk
from views.messages import AppName
from core.converters import Converters
from utilities.utils import HelperFunctions
from views.messages import ErrorMessages, APIMessages
from dataclasses import dataclass

@dataclass
class GUIConstants:
    app_font_family: str = "Arial"
    title_font: tuple = (app_font_family, 60, "bold")
    switch_font: tuple = (app_font_family, 35)
    io_font: tuple = (app_font_family, 30)
    other_font: tuple = (app_font_family, 25)
    theme_values = ["System", "Dark", "Light"]
    translation_mode_values = ["Direct", "API"]
    api_states = ["on", "off"]
    current_translation_mode: str = translation_mode_values[0]
    window_default_size: str = "900x1000"
    default_color_theme: str = "blue"
    app_title: str = "Morse ⇄ Text Translator"
    switch_keys = {"ttm": "text-to-morse", "mtt": "morse-to-text"}
    io_border_color: str = "#313131"
    translation_direction_switch_theme_color = {
        "on": "darkturquoise", 
        "off": "darkturquoise", 
        "btn": "#004F98", 
        "btnh": "#015EB4"
    }
    api_state_switch_theme_color = {
        "on": "green", 
        "off": "red", 
        "btn": "#707070", 
        "btnh": "#666666"
    }
    option_menu_theme_colors = {
        "dark": {"fg": "#333333", "btn": "#2C2C2C"},
        "light": {"fg": "#DEDEDE", "btn": "#DCDCDC"}
    }


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.converter = Converters()
        
        ctk.set_appearance_mode(GUIConstants.theme_values[0])
        ctk.set_default_color_theme(GUIConstants.default_color_theme)
        
        self.geometry(GUIConstants.window_default_size)
        self.minsize(900, 1000)
        
        self.title(GUIConstants.app_title)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.title_label = ctk.CTkLabel(self, text=AppName.app_name, font=GUIConstants.title_font)
        self.title_label.grid(row=0, column=1, pady=20, sticky="nsew")

        self.center_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.center_frame.grid(row=1, column=1, pady=20)
        self.center_frame.grid_columnconfigure(0, weight=0)
        self.center_frame.grid_columnconfigure(1, weight=0)
        self.center_frame.grid_columnconfigure(2, weight=0)

        self.left_label = ctk.CTkLabel(self.center_frame, text="Text to Morse", font=GUIConstants.switch_font)
        self.left_label.grid(row=0, column=0, padx=(0, 8), sticky="e")

        self.operation_type_switch_var = ctk.StringVar(value="text-to-morse")
        self.operation_type_switch = ctk.CTkSwitch(self.center_frame,
                                              offvalue=GUIConstants.switch_keys["ttm"],
                                              onvalue=GUIConstants.switch_keys["mtt"],
                                              variable=self.operation_type_switch_var,
                                              switch_width=100,
                                              switch_height=50,
                                              text="",
                                              fg_color=GUIConstants.translation_direction_switch_theme_color["off"],
                                              progress_color=GUIConstants.translation_direction_switch_theme_color["on"],
                                              button_color=GUIConstants.translation_direction_switch_theme_color["btn"],
                                              button_hover_color=GUIConstants.translation_direction_switch_theme_color["btnh"])
        self.operation_type_switch.grid(row=0, column=1, padx=8)

        self.right_label = ctk.CTkLabel(self.center_frame, text="Morse to Text", font=GUIConstants.switch_font)
        self.right_label.grid(row=0, column=2, padx=(8, 0), sticky="w")

        self.input_field = ctk.CTkTextbox(self,
        width=800,
        height=200,
        font=GUIConstants.io_font,
        corner_radius=30,
        border_color=GUIConstants.io_border_color,
        border_width=1)
        self.input_field.insert("1.0", f"Enter your text here...{chr(0x200B)}")
        self.input_field.configure(text_color=("gray", "gray"))
        self.input_field.bind("<FocusIn>", self.on_textbox_entry)
        self.input_field.bind("<FocusOut>", self.on_textbox_exit)
        self.input_field.grid(row=2, column=0, columnspan=3, pady=(20, 0), padx=20, sticky="s")

        self.output_field = ctk.CTkTextbox(self,
        width=800,
        height=200,
        font=GUIConstants.io_font,
        corner_radius=30,
        border_color=GUIConstants.io_border_color,
        border_width=1)
        self.output_field.grid(row=3, column=0, columnspan=3, pady=(0, 20), padx=20, sticky="n")
        self.output_field.insert("1.0", "Translation")
        self.output_field.configure(text_color=("gray", "gray"))
        self.output_field.configure(state="disabled")

        self.translate_button = ctk.CTkButton(self,
        text="Translate",
        width=200,
        height=90,
        font=GUIConstants.other_font,
        corner_radius=50,
        command=self.transate_button)
        self.translate_button.grid(row=4, column=1, sticky="n")

        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=5, column=0, columnspan=3, sticky="ew")
        self.bottom_frame.grid_rowconfigure(0, weight=0)
        self.bottom_frame.grid_rowconfigure(1, weight=0)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_columnconfigure(2, weight=1)
        
        self.mode_selector_label = ctk.CTkLabel(self.bottom_frame, text="Mode:", font=GUIConstants.other_font)
        self.mode_selector_label.grid(row=0, column=0, padx=(20, 0), sticky="sw")

        self.translation_mode_var = ctk.StringVar(value=GUIConstants.translation_mode_values[0])
        self.mode_selection_menu = ctk.CTkOptionMenu(self.bottom_frame,
                                                      values=GUIConstants.translation_mode_values,
                                                      variable=self.translation_mode_var,
                                                      width=200,
                                                      height=50,
                                                      font=GUIConstants.other_font,
                                                      dropdown_font=GUIConstants.other_font,
                                                      fg_color=GUIConstants.option_menu_theme_colors["dark"]["fg"],
                                                      button_color=GUIConstants.option_menu_theme_colors["dark"]["btn"],
                                                      dynamic_resizing=False,
                                                      command=self.change_translation_mode)
        self.mode_selection_menu.grid(row=1, column=0, padx=(20, 0), sticky="sw")

        self.api_switcher_var = ctk.StringVar(value="off")
        self.api_switch_label = ctk.CTkLabel(self.bottom_frame,
                                             text=f"API State: {self.api_switcher_var.get().title()}",
                                             font=GUIConstants.other_font)
        self.api_switch_label.grid(row=0, column=1)

        self.api_switch = ctk.CTkSwitch(self.bottom_frame,
                                              offvalue=GUIConstants.api_states[1],
                                              onvalue=GUIConstants.api_states[0],
                                              variable=self.api_switcher_var,
                                              switch_width=70,
                                              switch_height=40,
                                              text="",
                                              command=self.change_api_state,
                                              fg_color=GUIConstants.api_state_switch_theme_color["off"],
                                              progress_color=GUIConstants.api_state_switch_theme_color["on"],
                                              button_color=GUIConstants.api_state_switch_theme_color["btn"],
                                              button_hover_color=GUIConstants.api_state_switch_theme_color["btnh"])
        self.api_switch.grid(row=1, column=1)

        self.theme_selector_label = ctk.CTkLabel(self.bottom_frame, text=":Theme", font=GUIConstants.other_font)
        self.theme_selector_label.grid(row=0, column=2, padx=(0, 20), sticky="se")

        self.theme_var = ctk.StringVar(value="System")
        self.theme_selection_menu = ctk.CTkOptionMenu(self.bottom_frame,
                                                      values=GUIConstants.theme_values,
                                                      variable=self.theme_var,
                                                      width=200,
                                                      height=50,
                                                      font=GUIConstants.other_font,
                                                      dropdown_font=GUIConstants.other_font,
                                                      fg_color=GUIConstants.option_menu_theme_colors["dark"]["fg"],
                                                      button_color=GUIConstants.option_menu_theme_colors["dark"]["btn"],
                                                      dynamic_resizing=False,
                                                      command=self.change_theme)
        self.theme_selection_menu.grid(row=1,column=2, padx=(0, 20), sticky="se")


    def transate_button(self):
        input_text = self.input_field.get("1.0", "end").strip()
        if not input_text or input_text == f"Enter your text here...{chr(0x200B)}":
            result = ""
        elif self.translation_mode_var.get() == GUIConstants.translation_mode_values[0]:
            result = self.offline_translator(input_text)
        else:
            result = self.online_translator(input_text)
            

        self.output_field.configure(state="normal")
        self.output_field.delete("1.0", "end")
        self.output_field.insert("1.0", result if result != "" else "Translation")
        self.output_field.configure(text_color=("black", "white") if result != "" else ("gray", "gray"))
        self.output_field.configure(state="disabled")

    def offline_translator(self, input_text: str) -> str:
        if self.operation_type_switch_var.get() == GUIConstants.switch_keys["ttm"]:
            return self.converter.text_to_morse(input_text)
        else:
            if HelperFunctions.is_morse_valid(input_text):
                return self.converter.morse_to_text(input_text)
            else:
                return ErrorMessages.invalid_morse_input

    def online_translator(self, input_text: str) -> str:
        try:
            import requests
            base_url: str = "http://127.0.0.1:8000/v1/"
            if self.operation_type_switch_var.get() == GUIConstants.switch_keys["ttm"]:
                url_param: str = GUIConstants.switch_keys["ttm"]
                result = requests.post(
                    url=base_url+url_param,
                    json={"text": input_text}
                )
                result_json = result.json()
                if result.status_code == 200:
                    return result_json[APIMessages.api_translated_text_key]
                else:
                    return result_json["detail"]
            else:
                if HelperFunctions.is_morse_valid(input_text):
                    url_param: str = GUIConstants.switch_keys["mtt"]
                    result = requests.post(
                        url=base_url+url_param,
                        json={"morse": input_text}
                    )
                    result_json = result.json()
                    if result.status_code == 200:
                        return result_json[APIMessages.api_translated_morse_key]
                    else:
                        return result_json["detail"]
                else:
                    return ErrorMessages.invalid_morse_input
        except requests.exceptions.ConnectionError:
            return "Connection Refused. Make sure API in On."

    def change_theme(self, choice):
        ctk.set_appearance_mode(choice)
        if str(ctk.get_appearance_mode()).lower() == GUIConstants.theme_values[2].lower():
            self.theme_selection_menu.configure(
                                                fg_color=GUIConstants.option_menu_theme_colors["light"]["fg"],
                                                button_color=GUIConstants.option_menu_theme_colors["light"]["btn"],
                                                text_color="black",
                                                )
            self.mode_selection_menu.configure(
                                                fg_color=GUIConstants.option_menu_theme_colors["light"]["fg"],
                                                button_color=GUIConstants.option_menu_theme_colors["light"]["btn"],
                                                text_color="black",
                                                )
        else:
            self.theme_selection_menu.configure(
                                                fg_color=GUIConstants.option_menu_theme_colors["dark"]["fg"],
                                                button_color=GUIConstants.option_menu_theme_colors["dark"]["btn"],
                                                text_color="white",
                                                )
            self.mode_selection_menu.configure(
                                                fg_color=GUIConstants.option_menu_theme_colors["dark"]["fg"],
                                                button_color=GUIConstants.option_menu_theme_colors["dark"]["btn"],
                                                text_color="white",
                                                )
    def on_textbox_entry(self, event):
        if self.input_field.get("1.0", "end-1c") == f"Enter your text here...{chr(0x200B)}":
            self.input_field.delete("1.0", "end")
            self.input_field.configure(text_color=("black", "white"))

    def on_textbox_exit(self, event):
        if self.input_field.get("1.0", "end-1c") == "":
            self.input_field.insert("1.0", f"Enter your text here...{chr(0x200B)}")
            self.input_field.configure(text_color=("gray", "gray"))
        
    def change_translation_mode(self, mode):
        self.translation_mode_var = ctk.StringVar(value=mode)


    def change_api_state(self):
        import threading
        if self.api_switcher_var.get() == GUIConstants.api_states[0]:
            threading.Thread(target=self.start_api, daemon=True).start()
        else:
            self.stop_api()


    def start_api(self):
        import subprocess
        
        try:
            self.api_process = subprocess.Popen(
                ["uvicorn", "api.app:app", "--reload"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("API started")
            self.api_switch_label.configure(text=f"API State: {self.api_switcher_var.get().title()}")
        except Exception as e:
            print("Failed to start API:", e)
            self.api_switcher_var = GUIConstants.api_states[1]
            self.api_switch.deselect()

    def api_stopper(self):
        if hasattr(self, "api_process") and self.api_process:
            self.api_process.terminate()
            self.api_process = None
            print("API stopped")
            self.api_switch_label.configure(text=f"API State: {self.api_switcher_var.get().title()}")

    def stop_api(self):
        self.api_stopper()

    def on_closing(self):
        self.api_stopper()
        self.destroy()



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()