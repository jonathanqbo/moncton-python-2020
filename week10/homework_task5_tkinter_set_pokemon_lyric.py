import tkinter as tk


def on_btn_click():
    lyrics = text_lyrics.get('1.0', tk.END)
    words = lyrics.split()  # words is a list
    diff_words = set(words)  # create set from list

    text_words.delete('1.0', tk.END)
    # Task 5: show total amount of words, and total amount of unique words
    text_words.insert(tk.END, f'Total words [{len(words)}] ')
    text_words.insert(tk.END, f'Distinct words [{len(diff_words)}] \n\n')
    for word in diff_words:
        text_words.insert(tk.END, ' ' + word)


window = tk.Tk()
window.title('Pokemon Words')
window.geometry('800x800')
window.config(background='SlateGray2')

text_lyrics = tk.Text(window)
text_lyrics.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

button_all_words = tk.Button(window, text='See all different words', font=('Arial', 24, 'normal'))
button_all_words['command'] = on_btn_click
button_all_words.pack(pady=20, ipadx=5, ipady=5)

text_words = tk.Text(window)
text_words.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)


window.mainloop()

