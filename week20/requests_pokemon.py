import tkinter
import requests


class Pokemons:

    def __init__(self):
        self.pokemons = []
        self.get_all_pokemons()

    def get_all_pokemons(self):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1200')
        json = response.json()
        self.pokemons = json['results']

    def get_pokemon_names(self):
        return [pokemon['name'] for pokemon in self.pokemons]

    def get_pokemon(self, name):
        for pokemon in self.pokemons:
            if pokemon['name'] != name:
                continue

            json = requests.get(pokemon['url']).json()
            return [{stat['stat']['name'], stat['base_stat']} for stat in json['stats']]

        return 'not found'


pokemons = Pokemons()


def on_search():
    pokemon_name = entry_pokemon_name.get()
    text_found_pokemon.delete('1.0', tkinter.END)
    text_found_pokemon.insert('1.0', pokemons.get_pokemon(pokemon_name))


window = tkinter.Tk()
window.title('Pokemon Dictionary')
window.geometry('800x800')
window.config(background='SlateGray2')

top_section = tkinter.Frame(window, height=30, pady=10, background='SlateGray2')
top_section.pack(side='top', pady=10)

entry_pokemon_name = tkinter.Entry(top_section)
entry_pokemon_name.pack(side='left', padx=10)

button_search = tkinter.Button(top_section, text='Search')
button_search.pack(side='left', padx=10)
button_search['command'] = on_search

list_all_pokemons = tkinter.Listbox(window)
list_all_pokemons.pack(side='bottom', expand=True, fill='both', padx=20, pady=5)

label_all_pokemon = tkinter.Label(window, text='Here is all Pokemon documents', background='SlateGray2')
label_all_pokemon.pack(side='bottom', pady=5)

text_found_pokemon = tkinter.Text(window, height=5)
text_found_pokemon.pack(side='bottom', fill='x', padx=20, pady=5)


for name in pokemons.get_pokemon_names():
    list_all_pokemons.insert(tkinter.END, f'{name}')


tkinter.mainloop()



