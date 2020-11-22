import tkinter as tk
import tkinter.messagebox as tkmsgbox

POKEMON_FILE = 'pokemons.txt'
window = tk.Tk()
pokemons = []

def main():
    window.title('Pokemon Management System')
    window.geometry('1200x1000')

    # menu
    create_menu()

    # load data
    load_file()

    # default UI
    show_frame(create_add_ui(pokemons))

    window.mainloop()


def show_frame(the_frame):
    for child in window.winfo_children():
        if isinstance(child, tk.Frame) and child is not the_frame:
            child.destroy()

    the_frame.pack(expand=True, fill=tk.BOTH)
    the_frame.pack_slaves()


def create_menu():
    menubar = tk.Menu(window)

    file_menubar = tk.Menu(menubar)
    file_menubar.add_command(label='Load', command=load_file)
    file_menubar.add_command(label='Save', command=save_file)

    pokemon_menubar = tk.Menu(menubar)
    pokemon_menubar.add_command(label='Add', command=show_add_ui)
    pokemon_menubar.add_command(label='View', command=show_list_ui)
    pokemon_menubar.add_command(label='Search', command=show_search_ui)

    menubar.add_cascade(label='File', menu=file_menubar)
    menubar.add_cascade(label='Pokemon', menu=pokemon_menubar)
    window.config(menu=menubar)


def load_file():
    with open(POKEMON_FILE, 'r') as file:
        for line in file.read().splitlines():
            values = line.split(',')
            pokemon = create_pokemon(values[0], values[1], values[2], values[3])
            add_pokemon(pokemon)


def save_file():
    with open(POKEMON_FILE, 'w') as file:
        for pokemon in pokemons:
            file.write(','.join(pokemon) + '\n')
        tkmsgbox.showinfo('File Saved!', 'File Saved!')


def show_add_ui():
    add_frame = create_add_ui(pokemons)
    show_frame(add_frame)


def show_list_ui():
    list_frame = create_list_ui(pokemons)
    show_frame(list_frame)


def show_search_ui():
    pass


def add_pokemon(pokemon):
    pokemons.insert(0, pokemon)


def pokemon_to_str(pokemon):
    return f'{pokemon[0]:<30} Attack: {pokemon[1]:<30}  Defense: {pokemon[2]:<30}  HP: {pokemon[3]:<30}'


def create_pokemon(name, attack, defense, health):
    return name, attack, defense, health


def create_add_ui(pokemons):

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

    # def on_button_save_click():
    #     save_pokemons()

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
    # button_save = tk.Button(frame_input, text='Save', width=15)
    # button_save['command'] = on_button_save_click
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
    # button_save.pack(side='left', padx=5)
    label_error_info.pack(side='left', padx=10)

    listbox = tk.Listbox(frame, font=('Courier New', 12, 'normal'))
    listbox.pack(expand=True, fill=tk.BOTH)

    for pokemon in pokemons:
        listbox.insert(tk.END, pokemon_to_str(pokemon))

    return frame


def create_list_ui(pokemons):

    def get_name(pokemon_tuple):
        return pokemon_tuple[0]

    def get_attack(pokemon_tuple):
        return int(pokemon_tuple[1])

    def get_defend(pokemon_tuple):
        return int(pokemon_tuple[2])

    def get_health(pokemon_tuple):
        return int(pokemon_tuple[3])

    def on_sort_by_attack():
        sorted_pokemons = sorted(pokemons, key=get_attack, reverse=True)
        list_sort_by_attack.delete(0, 'end')
        for pokemon in sorted_pokemons:
            list_sort_by_attack.insert(tk.END, f'{get_name(pokemon)} Attack: {get_attack(pokemon)}')

    def on_sort_by_defense():
        sorted_pokemons = sorted(pokemons, key=get_defend, reverse=True)
        list_sort_by_defend.delete(0, 'end')
        for pokemon in sorted_pokemons:
            list_sort_by_defend.insert(tk.END, f'{get_name(pokemon)} Defend: {get_defend(pokemon)}')

    def on_sort_by_health():
        sorted_pokemons = sorted(pokemons, key=get_health, reverse=True)
        list_sort_by_health.delete(0, 'end')
        for pokemon in sorted_pokemons:
            list_sort_by_health.insert(tk.END, f'{get_name(pokemon)} Health: {get_health(pokemon)}')

    def on_sort_by_name():
        sorted_pokemons = sorted(pokemons, key=get_name)
        list_sort_by_name.delete(0, 'end')
        for pokemon in sorted_pokemons:
            list_sort_by_name.insert(tk.END, get_name(pokemon))

    frame = tk.Frame(window)

    button_section = tk.Frame(frame, height=100)
    button_section.pack(side='top', pady=10)

    button_sort_by_name = tk.Button(button_section, text='Sort by Name', height=2)
    button_sort_by_name.pack(side='left', padx=10)
    button_sort_by_name['command'] = on_sort_by_name

    button_sort_by_attack = tk.Button(button_section, text='Sort by Attack', height=2)
    button_sort_by_attack.pack(side='left', padx=10)
    button_sort_by_attack['command'] = on_sort_by_attack

    button_sort_by_defend = tk.Button(button_section, text='Sort by Defend', height=2)
    button_sort_by_defend.pack(side='left', padx=10)
    button_sort_by_defend['command'] = on_sort_by_defense

    button_sort_by_health = tk.Button(button_section, text='Sort by Health', height=2)
    button_sort_by_health.pack(side='left', padx=10)
    button_sort_by_health['command'] = on_sort_by_health

    sort_section = tk.Frame(frame)
    sort_section.pack(side='bottom', fill='both', expand=True, padx=10, pady=5)

    list_origin = tk.Listbox(sort_section)
    list_origin.pack(side='left', fill='both', expand=True, padx=5)

    list_sort_by_name = tk.Listbox(sort_section, width=20)
    list_sort_by_name.pack(side='left', fill='y', padx=5)

    list_sort_by_attack = tk.Listbox(sort_section, width=20)
    list_sort_by_attack.pack(side='left', fill='y', padx=5)

    list_sort_by_defend = tk.Listbox(sort_section, width=20)
    list_sort_by_defend.pack(side='left', fill='y', padx=5)

    list_sort_by_health = tk.Listbox(sort_section, width=20)
    list_sort_by_health.pack(side='left', fill='y', padx=5)

    for pokemon in pokemons:
        list_origin.insert(tk.END,pokemon)

    return frame


def create_search_ui():
    pass


if __name__ == '__main__':
    main()