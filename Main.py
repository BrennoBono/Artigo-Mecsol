import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Função para calcular a deflexão de engastes
def calcular_deflexao(material, area, comprimento, forma):
    # Aqui você pode definir as constantes para cada material e forma geométrica
    materiais = {
        "Ferro": 1.5,
        "Alumínio": 2.0,
        "Concreto": 1.0
    }

    formas_geometricas = {
        "Retângulo": 1.5,
        "Círculo": 2.0,
        "Triângulo": 1.0
    }

    constante_material = materiais.get(material, 0.0)
    constante_forma = formas_geometricas.get(forma, 0.0)

    if constante_material == 0.0 or constante_forma == 0.0:
        messagebox.showerror("Erro", "Material ou forma geométrica inválidos.")
        return

    # Aqui você pode fazer o cálculo da deflexão com as constantes e valores informados
    deflexao = constante_material * constante_forma * (area * comprimento)

    # Exemplo de exibição do resultado
    resultado = f"A deflexão no material {material} com a forma {forma} é de {deflexao:.2f} unidades."
    messagebox.showinfo("Resultado", resultado)

# Função para abrir o menu
def abrir_menu():
    opcoes_materiais = ["Ferro", "Alumínio", "Concreto"]
    opcoes_formas = ["Retângulo", "Círculo", "Triângulo"]

    # Cria uma nova janela para exibir as opções do menu
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    menu_window.geometry("250x250")

    # Variáveis para armazenar os valores inseridos pelo usuário
    area_var = tk.DoubleVar()
    comprimento_var = tk.DoubleVar()

    # Função para lidar com o botão de confirmação
    def confirmar():
        material_selecionado = menu_material_var.get()
        forma_selecionada = menu_forma_var.get()
        area = area_var.get()
        comprimento = comprimento_var.get()

        calcular_deflexao(material_selecionado, area, comprimento, forma_selecionada)
        menu_window.destroy()

    # Cria o menu de opções para materiais
    lbl_material = tk.Label(menu_window, text="Material:")
    lbl_material.pack()
    menu_material_var = tk.StringVar(menu_window)
    menu_material_var.set(opcoes_materiais[0])  # Define o valor inicial
    menu_material = tk.OptionMenu(menu_window, menu_material_var, *opcoes_materiais)
    menu_material.pack(pady=10)

    # Cria o menu de opções para formas geométricas
    lbl_forma = tk.Label(menu_window, text="Forma:")
    lbl_forma.pack()
    menu_forma_var = tk.StringVar(menu_window)
    menu_forma_var.set(opcoes_formas[0])  # Define o valor inicial
    menu_forma = tk.OptionMenu(menu_window, menu_forma_var, *opcoes_formas)
    menu_forma.pack(pady=10)

    # Campo de entrada para a área
    lbl_area = tk.Label(menu_window, text="Área:")
    lbl_area.pack()
    entry_area = tk.Entry(menu_window, textvariable=area_var)
    entry_area.pack()

    # Campo de entrada para o comprimento
    lbl_comprimento = tk.Label(menu_window, text="Comprimento:")
    lbl_comprimento.pack()
    entry_comprimento = tk.Entry(menu_window, textvariable=comprimento_var)
    entry_comprimento.pack()

    # Cria um botão para confirmar a seleção
    confirmar_btn = tk.Button(menu_window, text="Confirmar", command=confirmar)
    confirmar_btn.pack(pady=20)

# Cria a janela principal
root = tk.Tk()
root.title("Calculo de flexao em vigas duplamente apoiadas")
root.geometry("400x300")

# Cria um botão para abrir o menu de opções
menu_btn = tk.Button(root, text="Iniciar", command=abrir_menu)
menu_btn.pack(pady=20)

# Inicia a interface gráfica
root.mainloop()
