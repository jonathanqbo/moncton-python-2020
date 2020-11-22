import tkinter as tk
import tkinter.messagebox as tkmsgbox

POKEMON_FILE = 'pokemons.txt'
window = tk.Tk()
pokemons = []


def main():
    window.title('Pokemon Management System')
    window.geometry('1200x1000')

    load_pokemons()

    frame = create_add_ui()
    frame.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

    window.mainloop()


def load_pokemons():
    with open(POKEMON_FILE, 'r') as file:
        for line in file.read().splitlines():
            values = line.split(',')
            pokemon = create_pokemon(values[0], values[1], values[2], values[3])
            add_pokemon(pokemon)


def save_pokemons():
    with open(POKEMON_FILE, 'w') as file:
        for pokemon in pokemons:
            file.write(','.join(pokemon) + '\n')
        tkmsgbox.showinfo('File Saved!', 'File Saved!')


def create_pokemon(name, attack, defense, health):
    return name, attack, defense, health


def add_pokemon(pokemon):
    pokemons.append(pokemon)


def pokemon_to_str(pokemon):
    return f'{pokemon[0]:<30} Attack: {pokemon[1]:<30}  Defense: {pokemon[2]:<30}  HP: {pokemon[3]:<30}'


def create_add_ui():

    def on_button_add_click():
        label_error_info['text'] = ''

        name = entry_name.get()
        try:
            attack = entry_attack.get()
            defense = entry_defend.get()
            health = entry_health.get()

            pokemon = create_pokemon(name, attack, defense, health)
            add_pokemon(pokemon)
            listbox.insert(0, pokemon_to_str(pokemon))

            entry_name.delete(0, tk.END)
            entry_attack.delete(0, tk.END)
            entry_defend.delete(0, tk.END)
            entry_health.delete(0, tk.END)
        except ValueError:
            label_error_info.config(foreground='red')
            label_error_info['text'] = 'Wrong number!'


    def on_button_save_click():
        save_pokemons()

    frame = tk.Frame(window)

    frame_input = tk.Frame(frame, highlightbackground='red')
    frame_input.pack(fill=tk.X, pady=10)

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
    button_save = tk.Button(frame_input, text='Save', width=15)
    button_save['command'] = on_button_save_click
    label_error_info = tk.Label(frame_input)

    label_name.pack(side='left', padx=5)
    entry_name.pack(side='left', padx=5)
    label_attack.pack(side='left', padx=5)
    entry_attack.pack(side='left', padx=5)
    label_defend.pack(side='left', padx=5)
    entry_defend.pack(side='left', padx=5)
    label_health.pack(side='left', padx=5)
    entry_health.pack(side='left', padx=5)
    button_add.pack(side='left', padx=5)
    button_save.pack(side='left', padx=5)
    label_error_info.pack(side='left', padx=10)

    listbox = tk.Listbox(frame, font=('Courier New', 12, 'normal'))
    listbox.pack(expand=True, fill=tk.BOTH)

    for pokemon in pokemons:
        listbox.insert(tk.END, pokemon_to_str(pokemon))

    return frame


if __name__ == '__main__':
    main()