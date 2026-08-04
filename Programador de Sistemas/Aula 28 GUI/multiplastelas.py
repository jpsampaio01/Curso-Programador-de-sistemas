import tkinter as tk


def mudar():
    if tela1.winfo_viewable():
        tela1.pack_forget()
        tela2.pack(fill="both", expand=True)
    else:
        tela2.pack_forget()
        tela1.pack(fill="both", expand=True)


janela = tk.Tk()
janela.geometry("800x700")
janela.resizable(False, False)

tela1 = tk.Frame(janela,  bg="lightgreen")
label1 = tk.Label(tela1, text="Tela 1")
label1.pack(pady=10)
botao1 = tk.Button(tela1, text="Mudar", command=mudar)
botao1.pack(pady=10)

tela2 = tk.Frame(janela, bg="pink")
label2 = tk.Label(tela2, text="Tela 2")
label2.pack(pady=10)
botao2 = tk.Button(tela2, text="Mudar", command=mudar)
botao2.pack(pady=10)

tela1.pack(fill="both", expand=True)
janela.mainloop()
