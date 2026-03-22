import customtkinter as ctk


# Configurações de aparência
ctk.set_appearance_mode("dark")

# Função para validar o login
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "adyel" and senha == "123456":
        resultado_login.configure(text="Login bem-sucedido!", text_color="green")
    else:
        resultado_login.configure(text="Login falhou. Tente novamente.", text_color="red")

# Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

# Label para usuario
label_usuario = ctk.CTkLabel(app, text="Usuario:")
label_usuario.pack(pady=10)

# Campo de entrada para usuario
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuario")
campo_usuario.pack(pady=10)

# Campo de entrada para senha
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)

# Campo de entrada para senha
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)

# Botão de login
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=20)

# Label para exibir o resultado do login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)


# Inicia a aplicação
app.mainloop()