import customtkinter as ctk
from tkinter import ttk
from ctypes import windll
from PIL import Image
import csv
import os
from data_base import Funcionario, engine
from sqlalchemy.orm import sessionmaker



windll.shcore.SetProcessDpiAwareness(2)

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

# criando sessao para conectar ao banco
try:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = SessionLocal()
        print("Sessão criada com sucesso!")
except Exception as e:
        print(f"Erro ao criar sessão: {e}")
        exit()


#------------------------------------------------------
#------------------- Login ---------------------------


#----------------------------------------------------
#---------------------------------------------------




home = ctk.CTk()
ctk.set_appearance_mode('light')


home_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/fundohome.png'), size=(1200, 750))
home_label = ctk.CTkLabel(master=home, image=home_image,text=None)
home_label.pack(anchor='center')


home.geometry('1200x750')
home.resizable(False,False)
home.title('')







#-------------------------------------------------------
#--------------------- Def Hover -----------------------

def fc_enter(event):
    funcionario_button.configure(image=funcionario_hover_image)
 
def fc_leave(event):
    funcionario_button.configure(image=funcionario_image)

def md_enter(event):
        meusdados_button.configure(image=md_hover)

def md_leave(event):
        meusdados_button.configure(image=meusdados_image)

def cd_enter(event):
        cadastro_button.configure(image=cadastro_hover)

def cd_leave(event):
        cadastro_button.configure(image=cadastro_image)
#-------------------------------------------------------
#--------------------- Funcionário ---------------------

def Abrir_tela_funcionario():

        global table

        def deletar_linha():
                #Deleta uma linha selecionada no Treeview e no banco SQLite
                selecionado = table.selection()

                if not selecionado:
                        print("Nenhuma linha selecionada!")
                        return

                for item in selecionado:
                        valores = table.item(item)['values']
                        id = valores[0]  

                        # busca cpf no banco
                        funcionario = session.query(Funcionario).filter_by(id=id).first()

                if funcionario:
                        session.delete(funcionario)
                        session.commit()  # Confirma a exclusão no banco
                        table.delete(item)  # Remove a linha do Treeview

                else:
                        print(f"Funcionário com ID {id} não encontrado no banco!")


        def carregar_dados():
                funcionarios = session.query(Funcionario).all()
                
                return [(f.id, f.nome, f.cargo, f.setor, f.salario, f.cpf, f.email) for f in funcionarios]


        def buscar_dados(event=None):
                search_query = barra_pesquisa.get().strip().lower()  # Obtém o texto da barra de pesquisa e normaliza

                # Limpa a tabela antes de adicionar os novos resultados
                for row in table.get_children():
                        table.delete(row)

                # Busca no banco de dados funcionários cujo nome contenha a string pesquisada
                funcionarios = session.query(Funcionario).filter(Funcionario.nome.ilike(f"%{search_query}%")).all()

                # Insere os dados filtrados na tabela
                for funcionario in funcionarios:
                        table.insert("", "end", values=(funcionario.id, funcionario.nome, funcionario.cargo, funcionario.setor, 
                                                        funcionario.salario, funcionario.cpf, funcionario.email))


        

        meusdados_button = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=meusdados_image,
                                 bg_color='#E9E5E5',
                                 fg_color='white',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                 command=Abrir_tela_md
                                                      )
        meusdados_button.place(x=-8,y=320)
        
        cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
        cadastro_button.place(x=-8,y=255)
        
        
        funcionario_button.place_forget()
        func_hover = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_hover_image,
                                   bg_color='#E9E5E5',
                                   fg_color='#E9E5E5',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                            )
        func_hover.place(x=-9,y=190)    

        interior_func = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='#DEDEDE',width=840,height=636)
        interior_func.place(x=298,y=62)


        


        barra_pesquisa = ctk.CTkEntry(
                                      master=interior_func,
                                      placeholder_text='Pesquisar',
                                      border_color='white',
                                      font=('Istok Web', 14),
                                      bg_color='#DEDEDE',
                                      fg_color='white',
                                      corner_radius=5,
                                      width=345,
                                      height=28
                                                           )
        barra_pesquisa.place(x=25,y=0)
        barra_pesquisa.bind("<KeyRelease>", buscar_dados)
        lupa_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/ttt.png'), size=(28,28))
        lupa_label = ctk.CTkLabel(master=interior_func,text=None,height=28,image=lupa_image)
        lupa_label.place(x=0,y=0)
        
        filtro = ctk.CTkEntry(
                              master=interior_func,
                              placeholder_text='Filtro',
                              justify='center',                              
                              border_color='white',
                              font=('Istok Web', 14),
                              bg_color='#DEDEDE',
                              fg_color='white',
                              corner_radius=5,
                              width=120,
                              height=28)
        filtro.place(x=420,y=0)
        filtro_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/Filter.png'), size=(20,20))
        filtro_label = ctk.CTkLabel(master=interior_func, 
                                    image=filtro_image,
                                    text=None,
                                    bg_color='white',
                                    fg_color='white',
                                    width=0,
                                    height=0)
        filtro_label.place(x=425,y=4)
        
        adicionar_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/adicionar.png'), size=(110,28))
        adicionar_button = ctk.CTkButton(master=interior_func, 
                                        image=adicionar_image,
                                        text=None,
                                        bg_color='#DEDEDE',
                                        fg_color='#DEDEDE',
                                        hover=None,
                                        width=0,
                                        height=0,
                                        border_spacing=0,
                                        command=Abrir_tela_cadastro
                                                                    )
        adicionar_button.place(x=580,y=-3.5)




        delete_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/delete.png'), size=(110,28))
        delete_label = ctk.CTkButton(master=interior_func, 
                                     image=delete_image,
                                     text=None,
                                     bg_color='#DEDEDE',
                                     fg_color='#DEDEDE',
                                     hover=None,
                                     width=0,
                                     height=0,
                                     border_spacing=0,
                                     command=deletar_linha
                                                           )
        delete_label.place(x=727,y=-3.5)

        style = ttk.Style()
        style.theme_use('clam')  # Use um tema que permita personalização
        style.configure("Custom.Treeview",
        bordercolor="white",
        borderwidth=0,
        height=10,
                )         
        style.configure(
                        "Custom.Treeview", 
                        font=('Istok Web', 10),
                        rowheight=28
                                ) 
        style.configure("Custom.Treeview.Heading",
                background="white",  # Cor de fundo dos cabeçalhos
                foreground="#000000", # Cor do texto dos cabeçalhos
                borderwidth=0,
                font=('Istok Web', 11, 'bold')) 

        style.map("Custom.Treeview.Heading",
          background=[('active', 'white'), ('pressed', 'white'), ('!active', 'white')],
          foreground=[('active', '#000000'), ('pressed', '#000000'), ('!active', '#000000')]) 
        
  
        
        table = ttk.Treeview(interior_func, columns = ('id','nome', 'cargo', 'setor','salario','cpf','email'), show='headings', style="Custom.Treeview")
        
        table.heading('id', text='ID',anchor='w')
        table.heading('nome', text='Nome',anchor='w')
        table.heading('cargo', text='Cargo',anchor='w')
        table.heading('setor', text='Setor',anchor='w')
        table.heading('salario', text='Salario',anchor='w')
        table.heading('cpf', text='Cpf',anchor='w')
        table.heading('email', text='Email',anchor='w')

        table.column('id', width=45)
        table.column('nome', width=110)
        table.column('cargo', width=110)
        table.column('setor', width=60)
        table.column('salario', width=40)
        table.column('cpf', width=60)
        table.column('email', width=160)
        

        dados = carregar_dados()
        
        for item in dados:
                table.insert("", "end", values=item)


  
        table.place(x=0, y=36, width=840, height=600)

        
        def md_enter(event):
                meusdados_button.configure(image=md_hover)

        def md_leave(event):
                meusdados_button.configure(image=meusdados_image)

        def cd_enter(event):
                cadastro_button.configure(image=cadastro_hover)

        def cd_leave(event):
                cadastro_button.configure(image=cadastro_image)


        cadastro_button.bind("<Enter>", cd_enter)
        cadastro_button.bind("<Leave>", cd_leave)

        meusdados_button.bind("<Enter>", md_enter)
        meusdados_button.bind("<Leave>", md_leave)

#-----------------------------------------
#------------ Cadastro ------------------

def Abrir_tela_cadastro():
    
        


        meusdados_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=meusdados_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_md
                                                )
        meusdados_button.place(x=-8,y=320)

        funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
        funcionario_button.place(x=-8,y=190)
        
        
        cadastro_button.place_forget()

        cd_hover = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_hover,
                                bg_color='#E9E5E5',
                                fg_color='#E9E5E5',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                         )
        cd_hover.place(x=-8,y=255)
        
        
        interior_cadastro = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='white',width=840,height=636)
        interior_cadastro.place(x=298,y=62)


        def reset():
                nome_entry.delete(0, ctk.END)
                email_entry.delete(0, ctk.END)
                cpf_entry.delete(0, ctk.END)
                salario_entry.delete(0, ctk.END)
                setor_entry.delete(0, ctk.END)
                senha_entry.delete(0, ctk.END)
                cargo_entry.delete(0, ctk.END)


        def salvar_dados():  
                nome = nome_entry.get()
                email = email_entry.get()
                cpf = cpf_entry.get()
                salario = salario_entry.get()
                setor = setor_entry.get()
                senha = senha_entry.get()
                cargo = cargo_entry.get()
        
        

                novo_funcionario = Funcionario(
                        nome=nome,
                        cargo=cargo,
                        setor=setor,
                        salario=float(salario),  # Converter para float se necessário
                        cpf=cpf,
                        email=email,
                        senha = senha
                        )


                session.add(novo_funcionario)  # Adiciona o novo funcionário
                session.commit()  # Salva as mudanças no banco


                
                nome_entry.delete(0, ctk.END)
                email_entry.delete(0, ctk.END)
                cpf_entry.delete(0, ctk.END)
                salario_entry.delete(0, ctk.END)
                setor_entry.delete(0, ctk.END)
                senha_entry.delete(0, ctk.END)
                cargo_entry.delete(0, ctk.END)

        text_preencher = ctk.CTkLabel( 
                                interior_cadastro,
                                text='Preencher',
                                text_color='#EF5151',
                                font=('Istok Web', 32, 'bold'),
                                fg_color='white',
                                bg_color='white',
                                width=155,
                                height=46
                                          )
        text_preencher.place(x=35,y=35)


        nome_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Nome',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=37,
                                height=20
                                          )
        nome_text.place(x=35,y=121)                               
        
        
        email_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Email',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        email_text.place(x=429,y=121)


        cpf_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Cpf',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=22,
                                height=20
                                          )
        cpf_text.place(x=35,y=219)


        salario_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Salario',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=43,
                                height=20
                                          )
        salario_text.place(x=429,y=219)


        setor_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Setor',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        setor_text.place(x=35,y=317)


        senha_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Senha',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=39,
                                height=20
                                          )
        senha_text.place(x=429,y=317)



        cargo_text = ctk.CTkLabel(
                                interior_cadastro,
                                text='Cargo',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=38,
                                height=20
                                          )
        cargo_text.place(x=35,y=415)


        resetar_text = ctk.CTkButton(
                                interior_cadastro,
                                text='Resetar',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                width=38,
                                height=20,
                                command=reset
                                          )
        resetar_text.place(x=35,y=545)


        cadastrar_button = ctk.CTkButton(
                                interior_cadastro,
                                text='Cadastrar',
                                text_color='white',
                                font=('Istok Web', 15, 'bold'),
                                fg_color='#EF5151',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                corner_radius=5,
                                width=100,
                                height=26,
                                command= salvar_dados
                                                     )
        cadastrar_button.place(x=705,y=545)
        

        
        
        nome_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        nome_entry.place(x=35,y=146)                               
        

        email_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        email_entry.place(x=429,y=146)


        cpf_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cpf_entry.place(x=35,y=244)


        salario_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        salario_entry.place(x=429,y=244)


        setor_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        setor_entry.place(x=35,y=342)


        senha_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        senha_entry.place(x=429,y=342)



        cargo_entry = ctk.CTkEntry(
                                interior_cadastro,
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                border_width=0,
                                width=376,
                                height=3
                                          )
        cargo_entry.place(x=35,y=440)

        linha_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/linha.png'), size=(376,3))
        
        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=166)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=166)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=264)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=264)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=362)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=362)

        linha = ctk.CTkLabel(
                             interior_cadastro,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=460)




        
        def md_enter(event):
                meusdados_button.configure(image=md_hover)

        def md_leave(event):
                meusdados_button.configure(image=meusdados_image)


        def fc_enter(event):
                funcionario_button.configure(image=funcionario_hover_image)
        
        def fc_leave(event):
                funcionario_button.configure(image=funcionario_image)
        
        funcionario_button.bind("<Enter>", fc_enter)
        funcionario_button.bind("<Leave>", fc_leave)

        meusdados_button.bind("<Enter>", md_enter)
        meusdados_button.bind("<Leave>", md_leave)

#----------------------------------------
#------------- Meus Dados ----------------

def Abrir_tela_md():
        


        def buscar_email(email_buscado):
                with open('C:/cadastro_teste/clientes.csv', 'r') as csvfile:
                        linhas_encontradas = []  # Lista para armazenar as linhas encontradas
                        reader = csv.reader(csvfile)
                        next(reader)  # Pular o cabeçalho
                        for linha in reader:
                                print(linha)  # Adiciona impressão para depuração
                                if linha[1].strip() == email_buscado:  # Remove espaços em branco
                                        linhas_encontradas.append(linha)  # Adiciona a linha à lista
                return linhas_encontradas  # Retorna a lista de linhas

        # Chamada da função e armazenamento da saída em uma lista
        resultado = buscar_email('ff')

        for linha in resultado:
                if linha:  # Verifica se a linha não está vazia
                        nome = linha[0]  
                        email = linha[1]  
                        cpf = linha[2]
                        salario = linha[3]
                        setor = linha[4]
                        senha = linha[5]
                        cargo = linha[6]


        funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
        funcionario_button.place(x=-8,y=190)
        
        
        cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
        cadastro_button.place(x=-8,y=255)
        
        

        meusdados_button.place_forget()

        md_hovb = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=md_hover,
                                 bg_color='#E9E5E5',
                                 fg_color='#E9E5E5',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                         )
        md_hovb.place(x=-8,y=320)
        
        
        interior_md = ctk.CTkFrame(master=home,bg_color='#DEDEDE',fg_color='white',width=840,height=636)
        interior_md.place(x=298,y=62)

        text_dados = ctk.CTkLabel( 
                                interior_md,
                                text='Seus Dados',
                                text_color='#EF5151',
                                font=('Istok Web', 32, 'bold'),
                                fg_color='white',
                                bg_color='white',
                                width=155,
                                height=46
                                          )
        text_dados.place(x=35,y=35)


        nome_text = ctk.CTkLabel(
                                interior_md,
                                text='Nome',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=37,
                                height=20
                                          )
        nome_text.place(x=35,y=121)                               
        

        email_text = ctk.CTkLabel(
                                interior_md,
                                text='Email',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        email_text.place(x=429,y=121)


        cpf_text = ctk.CTkLabel(
                                interior_md,
                                text='Cpf',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=22,
                                height=20
                                          )
        cpf_text.place(x=35,y=219)


        salario_text = ctk.CTkLabel(
                                interior_md,
                                text='Salario',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=43,
                                height=20
                                          )
        salario_text.place(x=429,y=219)


        setor_text = ctk.CTkLabel(
                                interior_md,
                                text='Setor',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=34,
                                height=20
                                          )
        setor_text.place(x=35,y=317)


        senha_text = ctk.CTkLabel(
                                interior_md,
                                text='Senha',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=39,
                                height=20
                                          )
        senha_text.place(x=429,y=317)



        cargo_text = ctk.CTkLabel(
                                interior_md,
                                text='Cargo',
                                text_color='#787878',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=38,
                                height=20
                                          )
        cargo_text.place(x=35,y=415)


        aumento_button = ctk.CTkButton(
                                interior_md,
                                text='Pedir Aumento',
                                text_color='white',
                                font=('Istok Web', 15, 'bold'),
                                fg_color='#EF5151',
                                bg_color='white',
                                border_width=None,
                                hover=None,
                                corner_radius=5,
                                width=376,
                                height=26,

                                                           )
        aumento_button.place(x=429,y=437)
        

        
        
        nome_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{nome}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        nome_entry.place(x=35,y=146)                               
        

        email_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{email}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        email_entry.place(x=429,y=146)


        cpf_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{cpf}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        cpf_entry.place(x=35,y=244)


        salario_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{salario}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        salario_entry.place(x=429,y=244)


        setor_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{setor}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        setor_entry.place(x=35,y=342)


        senha_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{senha}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        senha_entry.place(x=429,y=342)



        cargo_entry = ctk.CTkLabel(
                                interior_md,
                                text=f'{cargo}',
                                font=('Istok Web', 15),
                                fg_color='white',
                                bg_color='white',
                                width=376,
                                height=3,
                                anchor='w'
                                          )
        cargo_entry.place(x=35,y=440)

        linha_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/linha.png'), size=(376,3))
        
        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=166)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=166)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=264)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=264)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=362)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=429,y=362)

        linha = ctk.CTkLabel(
                             interior_md,
                             text=None,
                             fg_color='#D9D9D9',
                             bg_color='white',
                             width=0,
                             height=0,
                             image=linha_image
                                     )
        linha.place(x=35,y=460)

                 


        def fc_enter(event):
                funcionario_button.configure(image=funcionario_hover_image)
 
        def fc_leave(event):
                funcionario_button.configure(image=funcionario_image)

        def cd_enter(event):
                cadastro_button.configure(image=cadastro_hover)

        def cd_leave(event):
                cadastro_button.configure(image=cadastro_image)

        
        funcionario_button.bind("<Enter>", fc_enter)
        funcionario_button.bind("<Leave>", fc_leave)

        cadastro_button.bind("<Enter>", cd_enter)
        cadastro_button.bind("<Leave>", cd_leave)

#--------------------------------------
#------------  LATERAL -----------------



logo_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/vslogo.png'), size=(40,40))
logo_label = ctk.CTkLabel(
                          master=home, 
                          image=logo_image,
                          text=None,bg_color='white',
                          fg_color='white',
                          width=0,
                          height=0
                                  )
logo_label.place(x=27,y=20)


foto_user_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/foto.png'), size=(40,40))
logo_label = ctk.CTkLabel(
                          master=home, 
                          image=foto_user_image,
                          text=None,
                          bg_color='white',
                          fg_color='white',
                          width=0,
                          height=0
                                  )
logo_label.place(x=23,y=110)
logo_text_label = ctk.CTkLabel(
                               master=home,
                               text='Eduardo Costa Lobo',
                               text_color='#787878',
                               font=('Istok Web', 14),
                               bg_color='white',
                               width=0,
                               height=0)
logo_text_label.place(x=73,y=120)



funcionario_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/func.png'), size=(237,50))
funcionario_hover_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/func_hover.png'), size=(237,50))
funcionario_button = ctk.CTkButton(
                                   master=home,
                                   text=None,
                                   image=funcionario_image,
                                   bg_color='#E9E5E5',
                                   fg_color='white',
                                   hover_color='#E9E5E5',
                                   border_color='#E9E5E5',
                                   width=0,
                                   height=0,
                                   command=Abrir_tela_funcionario,
                                                                 )
funcionario_button.place(x=-8,y=190)


cadastro_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/cadastro.png'), size=(237,50))
cadastro_hover = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/cad_hover.png'), size=(237,50))
cadastro_button = ctk.CTkButton(
                                master=home,
                                text=None,
                                image=cadastro_image,
                                bg_color='#E9E5E5',
                                fg_color='white',
                                hover_color='#E9E5E5',
                                border_color='#E9E5E5',
                                width=0,
                                height=0,
                                command=Abrir_tela_cadastro
                                                           )
cadastro_button.place(x=-8,y=255)


meusdados_image = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/meusdados.png'), size=(237,50))
md_hover = ctk.CTkImage(light_image=Image.open('C:/cadastro_teste/images/md_hover.png'), size=(237,50))
meusdados_button = ctk.CTkButton(
                                 master=home,
                                 text=None,
                                 image=meusdados_image,
                                 bg_color='#E9E5E5',
                                 fg_color='white',
                                 hover_color='#E9E5E5',
                                 border_color='#E9E5E5',
                                 width=0,
                                 height=0,
                                 command=Abrir_tela_md
                                                      )
meusdados_button.place(x=-8,y=320)





funcionario_button.bind("<Enter>", fc_enter)
funcionario_button.bind("<Leave>", fc_leave)

cadastro_button.bind("<Enter>", cd_enter)
cadastro_button.bind("<Leave>", cd_leave)

meusdados_button.bind("<Enter>", md_enter)
meusdados_button.bind("<Leave>", md_leave)


centralizar_janela(home)

home.iconbitmap('C:/cadastro_teste/images/vslogo.png')

home.mainloop()

