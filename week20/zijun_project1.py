import tkinter as tk
import tkinter.messagebox as tk_message_box

try:
    with open('library.txt', 'r') as file:
        file.read()
except FileNotFoundError:
    with open('library.txt', 'r') as file:
        file.read()

LIBRARY_FILE = 'library.txt'
window = tk.Tk()
libraries = []


def main():
    window.title('Library Graduation Project')
    window.geometry('1300x800')

    create_menu()

    # load_file()

    show_frame(create_add_ui(libraries))

    window.mainloop()


def show_frame(the_frame):
    for child in window.winfo_children():
        if isinstance(child, tk.Frame) and child is not the_frame:
            child.destroy()

    the_frame.pack(expand=True, fill=tk.BOTH)
    the_frame.pack_slaves()


def create_menu():
    menu_bar = tk.Menu(window)

    file_menu_bar = tk.Menu(menu_bar)
    file_menu_bar.add_command(label='Load', command=load_file)
    file_menu_bar.add_command(label='Save', command=save_file)

    library_menu_bar = tk.Menu(menu_bar)
    library_menu_bar.add_command(label='Add', command=show_add_ui)
    library_menu_bar.add_command(label='View', command=show_list_ui)
    library_menu_bar.add_command(label='Search', command=show_search_ui)

    menu_bar.add_cascade(label='File', menu=file_menu_bar)
    menu_bar.add_cascade(label='Library', menu=library_menu_bar)
    window.config(menu=menu_bar)


def load_file():
    with open(LIBRARY_FILE, 'r') as file0:
        for line in file0.read().splitlines():
            values = line.split(',')
            library = create_library(values[0], values[1], values[2], values[3])
            add_books(library)


def save_file():
    with open(LIBRARY_FILE, 'a') as file1:
        for library in libraries:
            file1.write(','.join(library) + '\n')
        tk_message_box.showinfo('File Saved!', 'File Saved!')


def show_add_ui():
    add_frame = create_add_ui(libraries)
    show_frame(add_frame)


def show_list_ui():
    list_frame = create_list_ui(libraries)
    show_frame(list_frame)


def show_search_ui():
    search_frame = create_search_ui(libraries)
    show_frame(search_frame)


def add_books(library):
    libraries.insert(0, library)


def library_to_str(library):
    return f"{library[0]:<10} Thickness:{library[1]}mm      Suitable_age:{library[2]:<10} "\
           f"Author:{library[3]:<10}"


def create_library(name, thickness, suitable_age, author):
    return name, thickness, suitable_age, author


def create_add_ui(books):

    def on_button_add_click():
        label_error_info['text'] = ''

        name = entry_name.get()
        try:
            thickness = entry_thickness.get()
            suitable_age = entry_suitable_age.get()
            author = entry_author.get()

            book = create_library(name, thickness, suitable_age, author)
            add_books(book)
            listbox.insert(0, library_to_str(book))

            entry_name.delete(0, tk.END)
            entry_thickness.delete(0, tk.END)
            entry_suitable_age.delete(0, tk.END)
            entry_author.delete(0, tk.END)
        except ValueError:
            label_error_info.config(foreground='red')
            label_error_info['text'] = 'Wrong number!'

    def on_button_add_delete():
        cur = listbox.curselection()
        if cur:
            del books[cur[0]]
            listbox.delete(cur)

    def on_button_save_click():
        save_file()

    frame = tk.Frame(window)

    frame_input = tk.Frame(frame, highlightbackground='red')
    frame_input.pack(fill=tk.X, pady=10)

    label_name = tk.Label(frame_input, text='Name:')
    entry_name = tk.Entry(frame_input)
    label_thickness = tk.Label(frame_input, text="Thickness(mm):")
    entry_thickness = tk.Entry(frame_input, width=5)
    label_suitable_age = tk.Label(frame_input, text='Suitable_age:')
    entry_suitable_age = tk.Entry(frame_input, width=5)
    label_author = tk.Label(frame_input, text='Author:')
    entry_author = tk.Entry(frame_input, width=5)
    button_add = tk.Button(frame_input, text='Add', width=15)
    button_add['command'] = on_button_add_click
    button_delete = tk.Button(frame_input, text='Delete', width=15)
    button_delete['command'] = on_button_add_delete
    button_save = tk.Button(frame_input, text='Save', width=15)
    button_save['command'] = on_button_save_click
    label_error_info = tk.Label(frame_input)
    label_error_info = tk.Label(frame_input)

    label_name.pack(side='left', padx=5)
    entry_name.pack(side='left', padx=5)
    label_thickness.pack(side='left', padx=5)
    entry_thickness.pack(side='left', padx=5)
    label_suitable_age.pack(side='left', padx=5)
    entry_suitable_age.pack(side='left', padx=5)
    label_author.pack(side='left', padx=5)
    entry_author.pack(side='left', padx=5)
    button_add.pack(side='left', padx=5)
    button_delete.pack(side='left', padx=5)
    button_save.pack(side='left', padx=5)
    label_error_info.pack(side='left', padx=10)

    listbox = tk.Listbox(frame, font=('Courier New', 12, 'normal'))
    listbox.pack(expand=True, fill=tk.BOTH)

    for library in books:
        listbox.insert(tk.END, library_to_str(library))

    return frame


def create_list_ui(books):

    def get_name(library_tuple):
        return library_tuple[0]

    def get_thickness(library_tuple):
        return int(library_tuple[1])

    def get_suitable_age(library_tuple):
        return int(library_tuple[2])

    def get_author(library_tuple):
        return library_tuple[3]

    def on_sort_by_thickness():
        sorted_libraries = sorted(books, key=get_thickness, reverse=True)
        list_sort_by_thickness.delete(0, 'end')
        for book in sorted_libraries:
            list_sort_by_thickness.insert(tk.END, f'Thickness: {get_thickness(book)} mm')

    def on_sort_by_suitable_age():
        sorted_libraries = sorted(books, key=get_suitable_age, reverse=True)
        list_sort_by_suitable_age.delete(0, 'end')
        for book in sorted_libraries:
            list_sort_by_suitable_age.insert(tk.END, f'Suitable_age: {get_suitable_age(book)}')

    def on_sort_by_author():
        sorted_libraries = sorted(books, key=get_author)
        list_sort_by_author.delete(0, 'end')
        for book in sorted_libraries:
            list_sort_by_author.insert(tk.END, f'Author: {get_author(book)}')

    def on_sort_by_name():
        sorted_libraries = sorted(books, key=get_name)
        list_sort_by_name.delete(0, 'end')
        for book in sorted_libraries:
            list_sort_by_name.insert(tk.END, get_name(book))

    frame = tk.Frame(window)

    button_section = tk.Frame(frame, height=100)
    button_section.pack(side='top', pady=10)

    button_sort_by_name = tk.Button(button_section, text='Sort by Name', height=2)
    button_sort_by_name.pack(side='left', padx=10)
    button_sort_by_name['command'] = on_sort_by_name

    button_sort_by_thickness = tk.Button(button_section, text='Sort by Thickness', height=2)
    button_sort_by_thickness.pack(side='left', padx=10)
    button_sort_by_thickness['command'] = on_sort_by_thickness

    button_sort_by_suitable_age = tk.Button(button_section, text='Sort by Suitable_age', height=2)
    button_sort_by_suitable_age.pack(side='left', padx=10)
    button_sort_by_suitable_age['command'] = on_sort_by_suitable_age

    button_sort_by_author = tk.Button(button_section, text='Sort by Author', height=2)
    button_sort_by_author.pack(side='left', padx=10)
    button_sort_by_author['command'] = on_sort_by_author

    sort_section = tk.Frame(frame)
    sort_section.pack(side='bottom', fill='both', expand=True, padx=10, pady=5)

    list_origin = tk.Listbox(sort_section)
    list_origin.pack(side='left', fill='both', expand=True, padx=5)

    list_sort_by_name = tk.Listbox(sort_section, width=20)
    list_sort_by_name.pack(side='left', fill='y', padx=20)

    list_sort_by_thickness = tk.Listbox(sort_section, width=20)
    list_sort_by_thickness.pack(side='left', fill='y', padx=20)

    list_sort_by_suitable_age = tk.Listbox(sort_section, width=20)
    list_sort_by_suitable_age.pack(side='left', fill='y', padx=20)

    list_sort_by_author = tk.Listbox(sort_section, width=20)
    list_sort_by_author.pack(side='left', fill='y', padx=20)

    for library in books:
        list_origin.insert(tk.END, library)

    return frame


def create_search_ui(libraries):

    def get_name(library_tuple):
        return library_tuple[0]

    def get_thickness(library_tuple):
        return int(library_tuple[1])

    def get_suitable(library_tuple):
        return int(library_tuple[2])

    def get_author(library_tuple):
        return library_tuple[3]

    # convert libraries list to library dict
    the_books = {}
    for book in libraries:
        the_book_dict = {'name': get_name(book),
                    'thickness': get_thickness(book),
                    'suitable': get_suitable(book),
                    'author': get_author(book)
                    }
        the_books[get_name(book)] = the_book_dict

    # the_books = {f'{get_name}': {f'thickness:': f'{get_thickness}',
    #                              f'suitable:': f'{get_suitable}',
    #                              f'author:': f'{get_author}'}}

    def on_search():
        # get book name from entry widget
        book_name = entry_pokemon_name.get()

        text_found_book.delete('1.0', tk.END)
        if book_name in the_books:
            # get book details from the_books dict, and show in the text widget
            text_found_book.insert('1.0', the_books.get(book_name))
        else:
            text_found_book.insert('1.0', 'This book is not here!')

    frame = tk.Frame(window)

    top_section = tk.Frame(frame, height=30, pady=10, background='SlateGray2')
    top_section.pack(side='top', pady=10)

    entry_pokemon_name = tk.Entry(top_section)
    entry_pokemon_name.pack(side='left', padx=10)

    button_search = tk.Button(top_section, text='Search')
    button_search.pack(side='left', padx=10)
    button_search['command'] = on_search

    list_all_books = tk.Listbox(frame)
    list_all_books.pack(side='bottom', expand=True, fill='both', padx=20, pady=5)

    label_all_book = tk.Label(frame, text="Here are all book's documents", background='SlateGray2')
    label_all_book.pack(side='bottom', pady=5)

    text_found_book = tk.Text(frame, height=5)
    text_found_book.pack(side='bottom', fill='x', padx=20, pady=5)

    # read the_books dict and insert into list widget
    for book_name, book in the_books.items():
        list_all_books.insert(tk.END, f'{book_name}   -  '
                                      f'Thickness: {book["thickness"]} '
                                      f'Suitable: {book["suitable"]} '
                                      f'Author: {book["author"]}')

    return frame


if __name__ == '__main__':
    main()