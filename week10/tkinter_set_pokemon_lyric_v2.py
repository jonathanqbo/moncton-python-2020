import tkinter as tk

"""
We're A Miracle

Here we are
Safe at last
We can breathe a sigh
It seems the storm has passed
Through it all
No one knew
That all the tears in heaven
Would bring me back to you
No one I know imagined we would make it
But it only matters that we both believe

(Chorus) You and me, we're a miracle
Meant to be and nothing can change it.
Mountains move and oceans part
When they are standing in our way
You and me, we're a miracle
Angels stand watching over us
And heaven shines upon us every day

Every time
I felt defeat
You were there for me
On my side completely
You give me strength
You set me free
Just as because of you I'm more then I can be
When I'm with you
The world is ours to reach for
Together, there is nothing we can do
(Chorus)

The chance was so unlikely
That we would ever be
Two stars among the heavens
Destiny brought you to me
(Chorus)

You and me, we're a miracle
You and me, we're a miracle
Miracle

---------
Together Forever

You've been such a good friend
I've known you since I don't know when
We've got a lot of friends,
But they come and go
Even though we've never said it,
There's something that the two of us both know

CHORUS
Together, forever no maater how long
From now, until the end of time
We'll be together and you can be sure
That forever and a day
That's how long we'll stay
Together and forever more

Always gone that extra mile
Depended on you all the while
Even in the good and bad times
You will see
From now until our journey's end
You know that you can always count on me

REPEAT CHORUS

No matter where our destiny leads
I'll be there for you, always come through
And that you can believe.

--------

CHORUS: Til' the end I will be with you,
We will go where our dreams come true,
All the times that we have been through,
You will always be my best friends...

Here we are-on a new adventure
Danger lurks-somewhere in the darkness
We are set-for surprises-even battle!
We're a team-no one better mess with us!

If we stand as one,
There's nothing to fear,
We'll beat the darkness,
And we'll stay right here!
Time after time,
That's how it will be,
Just you and me.

REPEAT CHORUS

Good friends-are those who stick together
When there's sun and in the heavy weather..

Smile after smile,
That's how it will be,
Just you and me...

REPEAT CHORUS

Remember when we first met?
We had such fun, oh I never will forget...
Since then, the times are so good-
We've always stuck together like best friends should.

"""
def on_btn_click():
    lyric1 = text_lyrics1.get('1.0', tk.END)
    lyric2 = text_lyrics2.get('1.0', tk.END)

    words1 = set(lyric1.split())
    words2 = set(lyric2.split())

    same_words = words1 & words2

    list_same_words.delete(0, tk.END)
    for word in same_words:
        list_same_words.insert(0, word)


window = tk.Tk()
window.title('Pokemon Words')
window.geometry('800x800')
window.config(background='SlateGray2')

frame = tk.Frame(window, background='SlateGray2')
frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

text_lyrics1 = tk.Text(frame, width=30, background='white', font=('Times', '18', 'italic'))
text_lyrics1.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=2)

text_lyrics2 = tk.Text(frame, width=30, background='white', font=('Times', '18', 'italic'))
text_lyrics2.pack(side=tk.LEFT, expand=True, fill=tk.Y, padx=2)

list_same_words = tk.Listbox(frame, background='SlateGray3', font=('Times', '18', 'italic'))
list_same_words.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10)

button_all_words = tk.Button(window, text='See all same words', width=50, height=2, background='SlateGray4')
button_all_words['command'] = on_btn_click
button_all_words.pack(side=tk.TOP, pady=20)

window.mainloop()
