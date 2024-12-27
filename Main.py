import tkinter as tk
from tkinter import messagebox

# Dictionaries
dictionaries = {
    "French": {
        "bonjour": "Hello",
        "merci": "Thank you",
        "au revoir": "Goodbye",
        "viens": "Come",
        "maison": "House",
    },

    "Lang2": {
        #Add words from another language
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

# Create the main application window
root = tk.Tk()
root.title("Multi-Language Dictionary")

# Title
title_label = tk.Label(root, text="Multi-Language Dictionary")
title_label.pack(pady=10)

# Dropdown for Dictionary selection
dictionary_var = tk.StringVar(value="French")
dictionary_menu = tk.OptionMenu(root, dictionary_var, *dictionaries.keys())
dictionary_menu.pack()

# Word Entry
word_label = tk.Label(root, text="Enter a word:")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

# Search Button
search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Meaning will appear here.")
result_label.pack(pady=20)

# Run the application
root.mainloop()
