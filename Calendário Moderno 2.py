import tkinter as tk
from tkinter import messagebox
import calendar

# Função para gerar o calendário
def gerar_calendario():
    try:
        # Obter o mês e o ano digitados
        mes = mes_var.get()
        ano = int(ano_entry.get())
        
        # Obter o índice do mês baseado na seleção
        meses = {
            'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
            'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
        }
        
        mes_num = meses[mes.lower()]
        
        # Gerar o calendário do mês e ano selecionados
        cal = calendar.month(ano, mes_num)
        
        # Exibir o calendário na caixa de texto
        calendario_text.delete(1.0, tk.END)  # Limpar o conteúdo anterior
        calendario_text.insert(tk.END, cal)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um ano válido!")

# Criar a janela principal
root = tk.Tk()
root.title("Gerador de Calendário")

# Configurar a interface
root.geometry("400x400")
root.config(bg="#e0f7fa")

# Criar o título
titulo = tk.Label(root, text="Gerador de Calendário", font=("Helvetica", 16, "bold"), bg="#e0f7fa")
titulo.pack(pady=10)

# Caixa de seleção de mês
mes_var = tk.StringVar()
mes_var.set("janeiro")  # Definir valor padrão
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes_menu = tk.OptionMenu(root, mes_var, *meses)
mes_menu.config(width=15, font=("Helvetica", 12))
mes_menu.pack(pady=5)

# Caixa de entrada para o ano
ano_label = tk.Label(root, text="Digite o ano:", font=("Helvetica", 12), bg="#e0f7fa")
ano_label.pack(pady=5)

ano_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
ano_entry.pack(pady=5)

# Botão para gerar o calendário
botao_gerar = tk.Button(root, text="Gerar Calendário", font=("Helvetica", 12), bg="#4caf50", fg="white", command=gerar_calendario)
botao_gerar.pack(pady=10)

# Caixa de texto para exibir o calendário
calendario_text = tk.Text(root, height=10, width=35, font=("Courier", 12), bg="#f1f8e9", wrap=tk.WORD)
calendario_text.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
