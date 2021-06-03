import tkinter as tk
from hashlib import sha256

def show_fields():
    print("Source: %s\nCible: %s \nClé : %s" % (e1.get(), e2.get(), e3.get()))
    keys=sha256(e3.get().encode('utf-8')).digest()

    with open(e1.get(),'rb') as f_entree : 
	    with open(e2.get(), 'wb') as f_sortie:
		    i=0
		    while f_entree.peek():
			    c = ord(f_entree.read(1))
			    j = i % len(e3.get())

			    b = bytes([c^keys[j]])
			    f_sortie.write(b)
			    i = i+1







master = tk.Tk()
master.title('Turing by Dr Snake')



master.iconphoto(False, tk.PhotoImage(file='2.png'))

tk.Label(master, text="entrez le nom du fichier à chiffrer : ").grid(row=0)
tk.Label(master, text="entrez le nom du fichier final : ").grid(row=1)
tk.Label(master, text="entrez la clé : ").grid(row=2)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Show', command=show_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

master.mainloop()