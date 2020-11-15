import tkinter as tk

window = tk.Tk()


def main():
    window.title('Pokemon Management System')
    window.geometry('1200x1000')

    frame = create_add_ui()
    frame.pack(expand=True, fill=tk.BOTH, pady=10)

    window.mainloop()


def create_add_ui():

    def on_button_add_click():
        name = entry_name.get()
        attack = int(entry_attack.get())
        defense = int(entry_defend.get())
        health = int(entry_health.get())

        listbox.insert(0, (name, attack, defense, health))

        entry_name.delete(0, tk.END)
        entry_attack.delete(0, tk.END)
        entry_defend.delete(0, tk.END)
        entry_health.delete(0, tk.END)

    frame = tk.Frame(window)

    frame_input = tk.Frame(frame)
    frame_input.pack(pady=10)

    label_name = tk.Label(frame_input, text='Name')
    entry_name = tk.Entry(frame_input)
    label_attack = tk.Label(frame_input, text='Attack:')
    entry_attack = tk.Entry(frame_input, width=5)
    label_defend = tk.Label(frame_input, text='Defend:')
    entry_defend = tk.Entry(frame_input, width=5)
    label_health = tk.Label(frame_input, text='Health:')
    entry_health = tk.Entry(frame_input, width=5)
    button_add = tk.Button(frame_input, text='Add', width=15)
    button_add['command'] = on_button_add_click

    label_name.pack(side='left', padx=10)
    entry_name.pack(side='left', padx=10)
    label_attack.pack(side='left', padx=10)
    entry_attack.pack(side='left', padx=10)
    label_defend.pack(side='left', padx=10)
    entry_defend.pack(side='left', padx=10)
    label_health.pack(side='left', padx=10)
    entry_health.pack(side='left', padx=10)
    button_add.pack(side='left', padx=10)

    listbox = tk.Listbox(frame)
    listbox.pack(expand=True, fill=tk.BOTH)

    return frame


if __name__ == '__main__':
    main()
