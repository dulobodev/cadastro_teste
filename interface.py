import customtkinter as ctk
from tkinter import ttk
from ctypes import windll
from PIL import Image
import sqlite3
import os



class SAP:

    def __init__(self):
        self.Config()
        self.campos_registro()
        self.botoes()
        self.tabela()
        ctk.set_appearance_mode('light')



    def Config(self):
        self.Screen = ctk.CTk()
        self.Screen.geometry('1200x750')
        self.Screen.resizable(False,False)
        self.Screen.title('')


    def campos_registro(self):
        
        Frame = ctk.CTkFrame(master = self.Screen, bg_color='white', fg_color ='white', width = 1250, height = 750)
        Frame.place(x=0,y=0)
        
        
        entry_codigo = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 306,
        height = 35 
        )
        
        entry_codigo.place(x=150,y=200)
        
        entry_produto = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 306,
        height = 35
        )
        
        entry_produto.place(x=150,y=260)
        
        entry_preco = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 306,
        height = 35
        )
        
        entry_preco.place(x=150,y=320)

        entry_descricao = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 306,
        height = 35
        )
        
        entry_descricao.place(x=150,y=380)

        entry_fabricante = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 306,
        height = 35
        )
        
        entry_fabricante.place(x=150,y=440)


        entry_buscar = ctk.CTkEntry(
        master = self.Screen,
        justify = 'left',
        border_color = 'grey',
        font=('Istok Web', 14),
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 400,
        height = 35
        )
        
        entry_buscar.place(x=170,y=50)


        text_buscar = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Buscar Produto:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_buscar.place(x=40, y=48)


        text_codigo = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Código:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_codigo.place(x=40, y=198)


        text_produto = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Produto:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_produto.place(x=40, y=258)
        

        text_preco = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Preço:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_preco.place(x=40, y=318)


        text_descricao = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Descrição:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_descricao.place(x=40, y=378)


        text_fabricante = ctk.CTkLabel(
        master = self.Screen,
        font=('Istok Web', 16),
        text = 'Fabricante:',
        bg_color = '#FFFFFF',
        fg_color = '#FFFFFF',
        corner_radius = 5,
        width = 50,
        height = 35   
        )

        text_fabricante.place(x=40, y=438)





    def botoes(self):
        button_adicionar = ctk.CTkButton(
        master = self.Screen,
        font=('Istok Web', 14, 'bold'),
        text = 'Adicionar',
        text_color= '#FFFFFF',
        bg_color = '#FFFFFF',
        fg_color = '#4F78F2',
        corner_radius = 5,
        width = 125,
        height = 35       
        )
        button_adicionar.place(x=42,y=488)


        button_editar = ctk.CTkButton(
        master = self.Screen,
        font=('Istok Web', 14, 'bold'),
        text = 'Editar',
        text_color= '#FFFFFF',
        bg_color = '#FFFFFF',
        fg_color = '#4F78F2',
        corner_radius = 5,
        width = 125,
        height = 35       
        )
        button_editar.place(x=187,y=488)

        button_editar = ctk.CTkButton(
        master = self.Screen,
        font=('Istok Web', 14, 'bold'),
        text = 'Excluir',
        text_color= '#FFFFFF',
        bg_color = '#FFFFFF',
        fg_color = '#4F78F2',
        corner_radius = 5,
        width = 125,
        height = 35       
        )
        button_editar.place(x=332,y=488)

        button_editar = ctk.CTkButton(
        master = self.Screen,
        font=('Istok Web', 14, 'bold'),
        text = 'Editar',
        text_color= '#FFFFFF',
        bg_color = '#FFFFFF',
        fg_color = '#4F78F2',
        corner_radius = 5,
        width = 150,
        height = 35       
        )
        button_editar.place(x=580,y=50)

        button_editar = ctk.CTkButton(
        master = self.Screen,
        font=('Istok Web', 14, 'bold'),
        text = 'Atualizar',
        text_color= '#FFFFFF',
        bg_color = '#FFFFFF',
        fg_color = '#4F78F2',
        corner_radius = 5,
        width = 150,
        height = 35       
        )
        button_editar.place(x=740,y=50)



    def tabela(self):

        self.style = ttk.Style()
        self.style.theme_use('clam')  
        self.style.configure("Custom.Treeview",
        bordercolor="grey",
        borderwidth=0,
        height=10,
                )         
        self.style.configure(
                        "Custom.Treeview", 
                        font=('Istok Web', 10),
                        rowheight=28
                                ) 
        self.style.configure("Custom.Treeview.Heading",
                background="#9FA3AD",  
                foreground="#000000",
                bordercolor = 'white',
                borderwidth=0.5,
                font=('Istok Web', 11, 'bold')) 
        
        self.style.map("Custom.Treeview.Heading",
          background=[('active', '#9FA3AD'), ('pressed', '#9FA3AD'), ('!active', '#9FA3AD')],
          foreground=[('active', '#000000'), ('pressed', '#000000'), ('!active', '#000000')]),
        
        table = ttk.Treeview(self.Screen, columns = ('Id', 'Código', 'Produto', 'Preço', 'Descrição', 'Fabricante'), show='headings', style="Custom.Treeview")


        table.heading('Id', text='Id',anchor='center')
        table.heading('Código', text='Código',anchor='center')
        table.heading('Produto', text='Produto',anchor='center')
        table.heading('Preço', text='Preço',anchor='center')
        table.heading('Descrição', text='Descrição',anchor='center')
        table.heading('Fabricante', text='Fabricante',anchor='center')

        table.column('Id', width=50)
        table.column('Código', width=50)
        table.column('Produto', width=50)
        table.column('Preço', width=50)
        table.column('Descrição', width=50)
        table.column('Fabricante', width=50)

        table.place(x=480, y=125, width=700, height=600)

    def start(self):
        self.Screen.mainloop()



    
loading = SAP()

loading.start()
