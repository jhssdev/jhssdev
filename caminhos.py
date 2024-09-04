import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk  

def criar_conexao(nome_banco):
    conn = sqlite3.connect(nome_banco)
    return conn

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arquivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caminho TEXT NOT NULL,
            palavras_chave TEXT
        )
    ''')
    conn.commit()

def inserir_caminho(conn, caminho, palavras_chave):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO arquivos (caminho, palavras_chave) VALUES (?, ?)
    ''', (caminho, palavras_chave))
    conn.commit()

def buscar_por_palavra_chave(conn, palavra_chave):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT caminho FROM arquivos WHERE palavras_chave LIKE ?
    ''', ('%' + palavra_chave + '%',))
    resultados = cursor.fetchall()
    return [resultado[0] for resultado in resultados]

def selecionar_arquivo():
    caminho = filedialog.askopenfilename()
    entrada_caminho.delete(0, tk.END)
    entrada_caminho.insert(0, caminho)

def adicionar_arquivo():
    caminho = entrada_caminho.get()
    palavras_chave = entrada_palavras.get()
    if caminho and palavras_chave:
        inserir_caminho(conn, caminho, palavras_chave)
        messagebox.showinfo("Sucesso", "Arquivo e palavras-chave adicionados com sucesso!")
        entrada_caminho.delete(0, tk.END)
        entrada_palavras.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, insira o caminho e as palavras-chave.")

def buscar_arquivos():
    palavra_chave = entrada_busca.get()
    if palavra_chave:
        resultados = buscar_por_palavra_chave(conn, palavra_chave)
        if resultados:
            resultado_texto = "\n".join(resultados)
        else:
            resultado_texto = "Nenhum arquivo encontrado."
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado_texto)
        text_resultado.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Erro", "Por favor, insira uma palavra-chave para busca.")

app = tk.Tk()
app.title("NG-Naviguide")
app.geometry("600x500")
app.configure(bg='#2E4053')

titulo_font = ('Arial', 14, 'bold')
label_font = ('Arial', 12)
entry_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')
result_font = ('Arial', 10)
cor_texto = '#F7F9F9'
cor_botao = '#1ABC9C'
cor_botao_hover = '#16A085'
cor_entry_bg = '#34495E'
cor_entry_fg = '#F7F9F9'

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

frame_buscar = tk.Frame(notebook, bg='#2E4053')
notebook.add(frame_buscar, text='Buscar Arquivos')

frame_adicionar = tk.Frame(notebook, bg='#2E4053')
notebook.add(frame_adicionar, text='Adicionar Arquivos')

frame_ajuda = tk.Frame(notebook, bg='#2E4053')
notebook.add(frame_ajuda, text='Ajuda')

tk.Label(frame_adicionar, text="Selecionar Arquivo:", font=label_font, bg='#2E4053', fg=cor_texto).pack(pady=5)
entrada_caminho = tk.Entry(frame_adicionar, width=50, font=entry_font, bg=cor_entry_bg, fg=cor_entry_fg, insertbackground=cor_entry_fg)
entrada_caminho.pack(pady=5, padx=10)
tk.Button(frame_adicionar, text="Procurar", font=button_font, bg=cor_botao, fg=cor_texto, activebackground=cor_botao_hover, command=selecionar_arquivo).pack(pady=5)

tk.Label(frame_adicionar, text="Palavras-chave:", font=label_font, bg='#2E4053', fg=cor_texto).pack(pady=5)
entrada_palavras = tk.Entry(frame_adicionar, width=50, font=entry_font, bg=cor_entry_bg, fg=cor_entry_fg, insertbackground=cor_entry_fg)
entrada_palavras.pack(pady=5, padx=10)

tk.Button(frame_adicionar, text="Adicionar Arquivo", font=button_font, bg=cor_botao, fg=cor_texto, activebackground=cor_botao_hover, command=adicionar_arquivo).pack(pady=10)

tk.Label(frame_buscar, text="Buscar por Palavra-chave:", font=label_font, bg='#2E4053', fg=cor_texto).pack(pady=5)
entrada_busca = tk.Entry(frame_buscar, width=50, font=entry_font, bg=cor_entry_bg, fg=cor_entry_fg, insertbackground=cor_entry_fg)
entrada_busca.pack(pady=5, padx=10)
tk.Button(frame_buscar, text="Buscar", font=button_font, bg=cor_botao, fg=cor_texto, activebackground=cor_botao_hover, command=buscar_arquivos).pack(pady=10)

text_resultado = tk.Text(frame_buscar, height=10, width=60, font=result_font, bg=cor_entry_bg, fg=cor_entry_fg, state=tk.DISABLED)
text_resultado.pack(pady=5, padx=10)

ajuda_mensagem = "Este é um software para facilitar as nossas vidas                                                                                                                                                                                                                                                                                                                                                                                            "
tk.Label(frame_ajuda, text=ajuda_mensagem, font=result_font, bg='#2E4053', fg=cor_texto, wraplength=500).pack(pady=20, padx=10)

conn = criar_conexao('Banco_dados_1')
criar_tabela(conn)

app.mainloop()

conn.close()
