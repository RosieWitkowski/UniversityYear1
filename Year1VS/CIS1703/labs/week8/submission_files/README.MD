# Exercies that require submission on VLE

# Some personal notes for future reference:

## Basics 
> Import tkinter as tk (alias)
Note tkinter and Tkinter, depends on version of Python 
> Config() for pre-existing widgets properties (and .cget('property) for retrieving)
> No parenthesis in command= (sending a reference, us lambda: if need arguments)
> Root.mainloop() ensures window stays open
> Max 1 layout manager per container - make frames that are packed then grid within
> Use messsagebox.askyesno('title, 'content)
also showinfo, askyesnocancel, etc.
ensure import (from tkinter import messagebox)

## Nielsen's 10 heurestics
1. Visibility of system status
2. Match between system and real world (terminology)
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and effeciency of use 
8. Aesthetic and minimilisitic 
9. Help users recognise/diagnose/recover from errors
10. Help and documentation

## More specific notes based on exercise 1.4
> Use classes for readabilitiy
in __main__ use tk.Tk() to create root, then pass as argument to class, then place root.mainloop() within
> Specific design 
e.g.
.pack(fill = tk.X) fills horizontal 
.place(relx=.9, rely=0) top corner (rely=.9 for bottom, etc.)
> Bind widgets to actions
.bind('<FocusIn>', fn) <- Click into entry
.bind('<Return>', lambda x: name.config(...)) < - Press enter
if using lambda, pass placeholder argument x as automatically passed

### Listboxes
> Listbox setup
make a frame to contain, scrollbar creation first
scrollbar = tk.Scrollbar(frame)
then make listbox
tk.Listbox(frame, selectmode = tk.SINGLE, activestyle='none', yscrollcommand=scrollbar.set)
connec scrollbar
scrollbar.config(command=listbox.yview)
> Accessing start to end
(0, tk.END)
e.g. use in sorting listbox:
for index, item in reversed(list(enumerate(listbox.get(0, tk.END)))):
(reversed to avoid index shift)
> Use .startswith() to check string
> Find index of selected item using listbox.curseselection()
> Update
delete then insert
listbox.delete(index), listbox.insert(index, 'new')



