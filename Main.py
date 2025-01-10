import tkinter as tk
from tkinter import messagebox

# Dictionaries
dictionaries = {
    "French": {
        "bonjour": "Hello",
        "merci": "Thank you",
        "au revoir": "Goodbye",
        "viens": "Come",
        "maison": "House.",
    },

      "Igbo": {
        "thank you": "daalu",
        "please": "biko",
        "yes": "ee",
        "no": "mba",
        "water": "mmiri",
        "food": "nri",
        "house": "ụlọ",
        "book": "akwụkwọ",
        "man": "nwoke",
        "woman": "nwanyị"
    },
    

   "Yourba": {
         "thank you": "ẹ ṣeun",
         "please": "ẹ jọ̀ọ́",
         "yes": "béẹ́ni",
         "no": "ràrà",
         "water": "omi",
         "food": "ounjẹ",
         "house": "ilé",
         "book": "ìwé",
         "man": "ọkùnrin",
         "woman": "obìnrin"
    },
 
   "Hausa": {
         "thank you": "na gode",
         "please": "don Allah",
         "yes": "eh",
         "no": "a'a",
         "water": "ruwa",
         "food": "abinci",
         "house": "gida",
         "book": "littafi",
         "man": "namiji",
         "woman": "mace",
         "chair": "Kujera",
         "bag" : "Jaka",
         "walk" : "Tafiya",
         "sit": "Zauna",
         "leg" : "kafa",
         "shoe" : "takalmi",
         "talk" : 'magana',
         "sleep": "baci",
         "right": "dama",
         "left" : "hagu"

    },
    
   "Igala": {
         "thank you": "anẹ",
         "please": "ẹ biko",
         "yes": "ẹẹ",
         "no": "ọda",
         "water": "ama",
         "food": "nra",
         "house": "ụla",
         "book": "akwụkwọ",
         "man": "ọmẹ",
         "woman": "ọb’iyọ"
    }
    
}

# Function to search the selected dictionary
def search_word():
    selected_dictionary = dictionary_var.get()
    word = entry.get().strip().lower()  # Get user input, trim spaces, and convert to lowercase
    meaning = dictionaries.get(selected_dictionary, {}).get(word)

    if meaning:
        result_label.config(text=f"Meaning: {meaning}")
    else:
        result_label.config(text="")
        messagebox.showinfo(
            "Not Found",
            f"The word '{word}' is not in the {selected_dictionary} dictionary.",
        )

# Tkinter main Window
root = tk.Tk()
root.title("Multi-Language Dictionary")
welcome_label = tk.Label(root, text="Welcome to our Dictionary", padx=200, pady=100, bg='blue', fg="white", font='Arial 16')
welcome_label.pack()
root.geometry("600x600")

# Title
title_label = tk.Label(root, text="Please select a Language")
title_label.pack(pady=10)

#Sekection menu
dictionary_var = tk.StringVar(value="French")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()

# Word Entry
word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search_word, pady=10, padx=10)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)

# Run the application
root.mainloop()
