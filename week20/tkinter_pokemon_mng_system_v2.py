import tkinter as tk
import os
import pickle

FONT_TITLE = ('Courier New', 36, 'bold')
FONT_CONTENT = ('Courier New', 12, 'normal')


class AddUIFrame(tk.Frame):

    def __init__(self, parent, pokemons_manager):
        super().__init__(parent)
        self.pokemons_manager = pokemons_manager

        label_title = tk.Label(self, text='Add Pokemon', font=FONT_TITLE)
        label_title.pack()

        frame_input = tk.Frame(self, highlightbackground='red')
        frame_input.pack(fill=tk.X, pady=10)

        label_name = tk.Label(frame_input, text='Name')
        self.entry_name = tk.Entry(frame_input)
        label_attack = tk.Label(frame_input, text='Attack:')
        self.entry_attack = tk.Entry(frame_input, width=5)
        label_defend = tk.Label(frame_input, text='Defend:')
        self.entry_defend = tk.Entry(frame_input, width=5)
        label_health = tk.Label(frame_input, text='Health:')
        self.entry_health = tk.Entry(frame_input, width=5)
        button_add = tk.Button(frame_input, text='Add', width=15)
        button_add['command'] = self.on_button_add_click
        # button_save = tk.Button(frame_input, text='Save', width=15)
        # button_save['command'] = on_button_save_click
        self.label_error_info = tk.Label(frame_input)

        label_name.pack(side='left', padx=5)
        self.entry_name.pack(side='left', padx=5)
        label_attack.pack(side='left', padx=5)
        self.entry_attack.pack(side='left', padx=5)
        label_defend.pack(side='left', padx=5)
        self.entry_defend.pack(side='left', padx=5)
        label_health.pack(side='left', padx=5)
        self.entry_health.pack(side='left', padx=5)
        button_add.pack(side='left', padx=5)
        # button_save.pack(side='left', padx=5)
        self.label_error_info.pack(side='left', padx=10)

        self.listbox = tk.Listbox(self, font=FONT_CONTENT)
        self.listbox.pack(expand=True, fill=tk.BOTH)

        for pokemon in self.pokemons_manager.pokemons:
            self.listbox.insert(tk.END, self.pokemons_manager.pokemon_to_str(pokemon))

    def on_button_add_click(self):
        self.label_error_info['text'] = ''

        name = self.entry_name.get()
        try:
            attack = int(self.entry_attack.get())
            defense = int(self.entry_defend.get())
            health = int(self.entry_health.get())
        except ValueError:
            self.label_error_info.config(foreground='red')
            self.label_error_info['text'] = 'Wrong number!'
        else:
            pokemon = self.pokemons_manager.create_pokemon(name, attack, defense, health)
            self.pokemons_manager.add_pokemon(pokemon)
            self.listbox.insert(0, self.pokemons_manager.pokemon_to_str(pokemon))

            self.entry_name.delete(0, tk.END)
            self.entry_attack.delete(0, tk.END)
            self.entry_defend.delete(0, tk.END)
            self.entry_health.delete(0, tk.END)


class ListUIFrame(tk.Frame):

    def __init__(self, parent, pokemons_manager):
        super().__init__(parent)
        self.pokemons_manager = pokemons_manager

        label_title = tk.Label(self, text='Sort Pokemon', font=FONT_TITLE)
        label_title.pack(side=tk.TOP)

        button_section = tk.Frame(self, height=100)
        button_section.pack(side='top', pady=10)

        button_sort_by_name = tk.Button(button_section, text='Sort by Name', height=2)
        button_sort_by_name.pack(side='left', padx=10)
        button_sort_by_name['command'] = self.on_sort_by_name

        button_sort_by_attack = tk.Button(button_section, text='Sort by Attack', height=2)
        button_sort_by_attack.pack(side='left', padx=10)
        button_sort_by_attack['command'] = self.on_sort_by_attack

        button_sort_by_defend = tk.Button(button_section, text='Sort by Defend', height=2)
        button_sort_by_defend.pack(side='left', padx=10)
        button_sort_by_defend['command'] = self.on_sort_by_defense

        button_sort_by_health = tk.Button(button_section, text='Sort by Health', height=2)
        button_sort_by_health.pack(side='left', padx=10)
        button_sort_by_health['command'] = self.on_sort_by_health

        sort_section = tk.Frame(self)
        sort_section.pack(side='bottom', fill='both', expand=True, padx=10, pady=5)

        self.list_origin = tk.Listbox(sort_section, font=FONT_CONTENT)
        self.list_origin.pack(side='left', fill='both', expand=True, padx=5)

        self.list_sort_by_name = tk.Listbox(sort_section, width=20, font=FONT_CONTENT)
        self.list_sort_by_name.pack(side='left', fill='y', padx=5)

        self.list_sort_by_attack = tk.Listbox(sort_section, width=20, font=FONT_CONTENT)
        self.list_sort_by_attack.pack(side='left', fill='y', padx=5)

        self.list_sort_by_defend = tk.Listbox(sort_section, width=20, font=FONT_CONTENT)
        self.list_sort_by_defend.pack(side='left', fill='y', padx=5)

        self.list_sort_by_health = tk.Listbox(sort_section, width=20, font=FONT_CONTENT)
        self.list_sort_by_health.pack(side='left', fill='y', padx=5)

        for pokemon in self.pokemons_manager.pokemons:
            self.list_origin.insert(tk.END, pokemon)

    def get_name(self, pokemon_tuple):
        return pokemon_tuple[0]

    def get_attack(self, pokemon_tuple):
        return pokemon_tuple[1]

    def get_defend(self, pokemon_tuple):
        return pokemon_tuple[2]

    def get_health(self, pokemon_tuple):
        return pokemon_tuple[3]

    def on_sort_by_attack(self):
        sorted_pokemons = sorted(self.pokemons_manager.pokemons, key=self.get_attack, reverse=True)
        self.list_sort_by_attack.delete(0, 'end')
        for pokemon in sorted_pokemons:
            self.list_sort_by_attack.insert(tk.END, f'{self.get_name(pokemon)} Attack: {self.get_attack(pokemon)}')

    def on_sort_by_defense(self):
        sorted_pokemons = sorted(self.pokemons_manager.pokemons, key=self.get_defend, reverse=True)
        self.list_sort_by_defend.delete(0, 'end')
        for pokemon in sorted_pokemons:
            self.list_sort_by_defend.insert(tk.END, f'{self.get_name(pokemon)} Defend: {self.get_defend(pokemon)}')

    def on_sort_by_health(self):
        sorted_pokemons = sorted(self.pokemons_manager.pokemons, key=self.get_health, reverse=True)
        self.list_sort_by_health.delete(0, 'end')
        for pokemon in sorted_pokemons:
            self.list_sort_by_health.insert(tk.END, f'{self.get_name(pokemon)} Health: {self.get_health(pokemon)}')

    def on_sort_by_name(self):
        sorted_pokemons = sorted(self.pokemons_manager.pokemons, key=self.get_name)
        self.list_sort_by_name.delete(0, 'end')
        for pokemon in sorted_pokemons:
            self.list_sort_by_name.insert(tk.END, self.get_name(pokemon))


class MenuBar(tk.Menu):

    def __init__(self, window, pokemons_manager, ui_switcher):
        super().__init__(window)
        self.pokemons_manager = pokemons_manager
        self.ui_switcher = ui_switcher

        file_menubar = tk.Menu(self)
        file_menubar.add_command(label='Load', command=self.pokemons_manager.load)
        file_menubar.add_command(label='Save', command=self.pokemons_manager.save)

        pokemon_menubar = tk.Menu(self)
        pokemon_menubar.add_command(label='Add', command=self.ui_switcher.show_add_ui)
        pokemon_menubar.add_command(label='View', command=self.ui_switcher.show_list_ui)
        pokemon_menubar.add_command(label='Search', command=self.ui_switcher.show_search_ui)

        self.add_cascade(label='File', menu=file_menubar)
        self.add_cascade(label='Pokemon', menu=pokemon_menubar)


class UIManager:

    def __init__(self, window, pokemons_manager):
        self.window = window
        self.pokemons_manager = pokemons_manager

    def show_add_ui(self):
        add_ui = AddUIFrame(self.window, self.pokemons_manager)
        self.show_frame(add_ui)

    def show_list_ui(self):
        list_ui = ListUIFrame(self.window, self.pokemons_manager)
        self.show_frame(list_ui)

    def show_search_ui(self):
        pass

    def show_frame(self, the_frame):
        for child in self.window.winfo_children():
            if isinstance(child, tk.Frame) and child is not the_frame:
                child.destroy()

        the_frame.pack(expand=True, fill=tk.BOTH)
        the_frame.pack_slaves()


class PokemonManager:

    DATA_FILE = '../week10/pokemons.pkl'

    def __init__(self):
        self.pokemons = self.load_pokemons_from_file()

    def load_pokemons_from_file(self):
        if not os.path.exists(PokemonManager.DATA_FILE):
            return []

        with open(PokemonManager.DATA_FILE, 'rb') as file:
            return pickle.load(file)

    def load(self):
        self.pokemons.clear()
        self.pokemons.extend(self.load_pokemons_from_file())

    def save(self):
        if os.path.exists(PokemonManager.DATA_FILE):
            os.remove(PokemonManager.DATA_FILE)

        with open(PokemonManager.DATA_FILE, 'wb') as file:
            pickle.dump(self.pokemons, file)

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def create_pokemon(self, name, attack, defense, health):
        return name, int(attack), int(defense), int(health)

    def pokemon_to_str(self, pokemon):
        return f'{pokemon[0]:<30} Attack: {pokemon[1]:<30}  Defense: {pokemon[2]:<30}  HP: {pokemon[3]:<30}'


def main():
    window = tk.Tk()
    window.title('Pokemon Management System')
    window.geometry('1200x1000')

    # pokrmon manager to manage pokemon data
    pokemons_manager = PokemonManager()

    # ui manager to manager UI: create and switch
    ui_manager = UIManager(window, pokemons_manager)

    # create menu
    menu_bar = MenuBar(window, pokemons_manager, ui_manager)
    window.config(menu=menu_bar)

    # show add_ui as first ui
    ui_manager.show_add_ui()

    window.mainloop()


if __name__ == '__main__':
    main()
