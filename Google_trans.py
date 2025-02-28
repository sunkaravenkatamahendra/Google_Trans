from tkinter import *
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

# Initialize the main window
root = Tk()
root.title('Translator')
root.geometry("800x400")
root.configure(bg="#f0f0f0")  # Set background color

# Function to translate text
def translate_it():
    translated_text.delete(1.0, END)
    try:
        from_language = original_combo.get()
        to_language = translated_combo.get()
        
        # Get language codes
        from_lang_key = [key for key, value in languages.items() if value == from_language][0]
        to_lang_key = [key for key, value in languages.items() if value == to_language][0]
        
        # Translate using googletrans
        translator = Translator()
        translation = translator.translate(original_text.get(1.0, END).strip(), src=from_lang_key, dest=to_lang_key)
        
        translated_text.insert(1.0, translation.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to clear text fields
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Load language list
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Labels
Label(root, text="Enter Text:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
Label(root, text="Translated Text:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)

# Text Boxes
original_text = Text(root, height=10, width=40, font=("Arial", 12))
original_text.grid(row=1, column=0, padx=10, pady=10)

translated_text = Text(root, height=10, width=40, font=("Arial", 12))
translated_text.grid(row=1, column=2, padx=10, pady=10)

# Language Selection Combo Boxes
original_combo = ttk.Combobox(root, width=40, value=language_list)
original_combo.current(21)  # Default: English
original_combo.grid(row=2, column=0, pady=10)

translated_combo = ttk.Combobox(root, width=40, value=language_list)
translated_combo.current(38)  # Default: Hindi
translated_combo.grid(row=2, column=2, pady=10)

# Buttons
translate_button = Button(root, text="Translate", font=("Arial", 14, "bold"), bg="blue", fg="white", command=translate_it)
translate_button.grid(row=1, column=1, padx=10, pady=5)

clear_button = Button(root, text="Clear", font=("Arial", 12), bg="red", fg="white", command=clear)
clear_button.grid(row=2, column=1, pady=10)

root.mainloop()
