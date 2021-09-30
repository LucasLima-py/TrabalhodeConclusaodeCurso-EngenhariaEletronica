import tkinter as ttk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from tkinter import filedialog as fd
import webbrowser
import time

#INICIALIZAÇÃO DA JANELA DE RECEPÇÃO
root = Tk()
#root.deiconify()
root.iconbitmap('icon.ico')
root.geometry("300x330+750+300")
root.resizable(False, False)

root.title("Classificador de biscoitos - forno linha 6 - CILASI Alimentos S.A")
img = PhotoImage(file = "logo teste.png")
Foto = Label(root, image=img)
Foto.grid(column=0,row=0, sticky="NESW", pady=(15))

lbltitulo1_nome = StringVar()
lbltitulo1_nome.set("Selecione abaixo")
lbltitulo1 = Label(root, textvariable = lbltitulo1_nome, font = ("Calibri", 14), bg = '#FF0000', fg = 'white')
lbltitulo1.grid(column=0,row=1,padx=(5),pady=(10,10))

lbltitulo2_nome = StringVar()
lbltitulo2_nome.set("Aguarde, treinando modelo")
lbltitulo2 = Label(root, textvariable = lbltitulo2_nome, font = ("Calibri", 14), bg = '#FF0000', fg = 'white')
lbltitulo2.grid(column=0,row=5,padx=(5),pady=(10,10))
lbltitulo2.destroy()

varBarra = DoubleVar()
varBarra.set(50)
pb = ttk.Progressbar(root,variable=varBarra, maximum=100,length=200)
pb.grid(column=0,row=6)
pb.destroy()

#INICIALIZAÇÃO DA JANELA DE CLASSIFICAÇÃO
janela = Toplevel()
janela.withdraw()
janela.iconbitmap('icon.ico')
w, h = janela.winfo_screenwidth(), janela.winfo_screenheight()
janela.geometry("880x850+500+100")
janela.resizable(False, False)

janela.title("Classificador de biscoitos - forno linha 6 - CILASI Alimentos S.A.")
img1 = PhotoImage(file = "logo.png")
Foto1 = Label(janela, image=img1)
Foto1.grid(column=0,row=0)

img_if = PhotoImage(file = "logo if.png")
Foto_if = Label(janela, image=img_if)
Foto_if.grid(column=1,row=0,sticky=W)
lbltitulo_nome = StringVar()
lbltitulo_nome.set("ESTIMADOR - BISCOITOS BELA VISTA")
lbltitulo = Label(janela, textvariable = lbltitulo_nome, font = ("Calibri", 20), bg = '#FF0000', fg = 'white')
lbltitulo.grid(column=2,row=0,padx=(100,50))

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

#LABEL TEMPERATURA TETO Z1
lbltetoz1_nome = StringVar()
lbltetoz1_nome.set("Temperatura Z1 - Teto")
lbltetoz1 = Label(janela, textvariable = lbltetoz1_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz1.grid(column=0,row=1,padx=(20),pady=(20,10), columnspan='2')

lbltetoz1_entry = Entry(janela,bd = '4',justify=CENTER,width='25')
lbltetoz1_entry.grid(column=2, row=1)

#LABEL TEMPERATURA LASTRO Z1
lbllastroz1_nome = StringVar()
lbllastroz1_nome.set("Temperatura Z1 - Lastro")
lbllastroz1 = Label(janela, textvariable = lbllastroz1_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white',width='20')
lbllastroz1.grid(column=0,row=2,padx=(20),pady=(10,10), columnspan='2')

lbllastroz1_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz1_entry.grid(column=2, row=2)

#LABEL TEMPERATURA TETO z2
lbltetoz2_nome = StringVar()
lbltetoz2_nome.set("Temperatura Z2 - Teto")
lbltetoz2 = Label(janela, textvariable = lbltetoz2_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz2.grid(column=0,row=3,padx=(20),pady=(10,10), columnspan='2')

lbltetoz2_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbltetoz2_entry.grid(column=2, row=3)

#LABEL TEMPERATURA LASTRO z2
lbllastroz2_nome = StringVar()
lbllastroz2_nome.set("Temperatura Z2 - Lastro")
lbllastroz2 = Label(janela, textvariable = lbllastroz2_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbllastroz2.grid(column=0,row=4,padx=(20),pady=(10,10), columnspan='2')

lbllastroz2_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz2_entry.grid(column=2, row=4)

#LABEL TEMPERATURA TETO Z3
lbltetoz3_nome = StringVar()
lbltetoz3_nome.set("Temperatura Z3 - Teto")
lbltetoz3 = Label(janela, textvariable = lbltetoz3_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz3.grid(column=0,row=5,padx=(20),pady=(10,10), columnspan='2')

lbltetoz3_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbltetoz3_entry.grid(column=2, row=5)

#LABEL TEMPERATURA LASTRO Z3
lbllastroz3_nome = StringVar()
lbllastroz3_nome.set("Temperatura Z3 - Lastro")
lbllastroz3 = Label(janela, textvariable = lbllastroz3_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbllastroz3.grid(column=0,row=6,padx=(20),pady=(10,10), columnspan='2')

lbllastroz3_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz3_entry.grid(column=2, row=6)

#LABEL TEMPERATURA TETO z4
lbltetoz4_nome = StringVar()
lbltetoz4_nome.set("Temperatura Z4 - Teto")
lbltetoz4 = Label(janela, textvariable = lbltetoz4_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz4.grid(column=0,row=7,padx=(20),pady=(10,10), columnspan='2')

lbltetoz4_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbltetoz4_entry.grid(column=2, row=7)

#LABEL TEMPERATURA LASTRO z4
lbllastroz4_nome = StringVar()
lbllastroz4_nome.set("Temperatura Z4 - Lastro")
lbllastroz4 = Label(janela, textvariable = lbllastroz4_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbllastroz4.grid(column=0,row=8,padx=(20),pady=(10,10), columnspan='2')

lbllastroz4_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz4_entry.grid(column=2, row=8)

#LABEL TEMPERATURA TETO z5
lbltetoz5_nome = StringVar()
lbltetoz5_nome.set("Temperatura Z5 - Teto")
lbltetoz5 = Label(janela, textvariable = lbltetoz5_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz5.grid(column=0,row=9,padx=(20),pady=(10,10), columnspan='2')

lbltetoz5_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbltetoz5_entry.grid(column=2, row=9)

#LABEL TEMPERATURA LASTRO z5
lbllastroz5_nome = StringVar()
lbllastroz5_nome.set("Temperatura Z5 - Lastro")
lbllastroz5 = Label(janela, textvariable = lbllastroz5_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbllastroz5.grid(column=0,row=10,padx=(20),pady=(10,10), columnspan='2')

lbllastroz5_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz5_entry.grid(column=2, row=10)

#LABEL TEMPERATURA TETO z6
lbltetoz6_nome = StringVar()
lbltetoz6_nome.set("Temperatura Z6 - Teto")
lbltetoz6 = Label(janela, textvariable = lbltetoz6_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbltetoz6.grid(column=0,row=11,padx=(20),pady=(10,10), columnspan='2')

lbltetoz6_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbltetoz6_entry.grid(column=2, row=11)

#LABEL TEMPERATURA LASTRO z6
lbllastroz6_nome = StringVar()
lbllastroz6_nome.set("Temperatura Z6 - Lastro")
lbllastroz6 = Label(janela, textvariable = lbllastroz6_nome, font = ("Calibri", 18), bg = '#FF0000', fg = 'white', width='20')
lbllastroz6.grid(column=0,row=12,padx=(20),pady=(10,10), columnspan='2')

lbllastroz6_entry = Entry(janela, bd = '4',justify=CENTER,width='25')
lbllastroz6_entry.grid(column=2, row=12)


def estimar():
    print("estimar")
    global modelo, X_train,X_test,Y_train,Y_test, misterioso2

    misterioso = []
    try:
        #METODO GET NAS ENTRY:
        Temp_SUP_Z1 = float(lbltetoz1_entry.get())
        Temp_INF_Z1 = float(lbllastroz1_entry.get())
        Temp_SUP_Z2 = float(lbltetoz2_entry.get())
        Temp_INF_Z2 = float(lbllastroz2_entry.get())
        Temp_SUP_Z3 = float(lbltetoz3_entry.get())
        Temp_INF_Z3 = float(lbllastroz3_entry.get())
        Temp_SUP_Z4	= float(lbltetoz4_entry.get())
        Temp_INF_Z4 = float(lbllastroz4_entry.get())
        Temp_SUP_Z5	= float(lbltetoz5_entry.get())
        Temp_INF_Z5	= float(lbllastroz5_entry.get())
        Temp_SUP_Z6	= float(lbltetoz6_entry.get())
        Temp_INF_Z6 = float(lbllastroz6_entry.get())

        misterioso.append(Temp_SUP_Z1)
        misterioso.append(Temp_INF_Z1)
        misterioso.append(Temp_SUP_Z2)
        misterioso.append(Temp_INF_Z2)
        misterioso.append(Temp_SUP_Z3)
        misterioso.append(Temp_INF_Z3)
        misterioso.append(Temp_SUP_Z4)
        misterioso.append(Temp_INF_Z4)
        misterioso.append(Temp_SUP_Z5)
        misterioso.append(Temp_INF_Z5)
        misterioso.append(Temp_SUP_Z6)
        misterioso.append(Temp_INF_Z6)

    except:
        msg = 'Por favor, preencha todos os campos antes de prosseguir'
        messagebox.showerror("Classificador de biscoitos - Bela vista v1.0", msg)

    print("misterioso: ",misterioso)
    print("quantidade de valores de temperatura coletados: ",len(misterioso))


    teste = [misterioso,misterioso2]
    resultado = modelo.predict(teste)
    resultado_teste = resultado[0]
    print("o resultado foi: ", resultado_teste)

    if resultado[0] == 0:
        biscoito = 'BISCOITO BOM'
        print(biscoito)
        msg1 = 'O Biscoito gerado para esses valores de temperatura, é um biscoito dentro dos padrões ideais de qualidade.'
        messagebox.showinfo("Classificador de biscoitos - Bela vista v1.0", msg1)
    
    else:
        biscoito = 'BISCOITO RUIM'
        print(biscoito)
        msg1 = 'O biscoito gerado para esses valores de temperatura, está fora dos padrões ideais de qualidade.'
        messagebox.showinfo("Classificador de biscoitos - Bela vista v1.0", msg1)
    #janela.withdraw()
    #root.deiconify()
    janela.deiconify()

        
def treinarIA():
    print("treinar IA")
    global misterioso2, modelo, X_train,X_test,Y_train,Y_test, lbltitulo2, pb
    msg = "Selecione o dataset com valores de temperatura e saídas rotuladas."
    messagebox.showinfo("Classificador de biscoitos - Bela vista v1.0", msg)

    arquivo = fd.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

    root.geometry("300x400+750+300")
    root.resizable(False, False)
    
    lbltitulo2_nome = StringVar()
    lbltitulo2_nome.set("Aguarde, treinando modelo")
    lbltitulo2 = Label(root, textvariable = lbltitulo2_nome, font = ("Calibri", 14), bg = '#FF0000', fg = 'white')
    lbltitulo2.grid(column=0,row=5,padx=(5),pady=(10,10))

    varBarra = DoubleVar()
    pb = ttk.Progressbar(root,variable=varBarra, maximum=100,length=200)
    pb.grid(column=0,row=6)
    varBarra.set(0)
    root.update()
    time.sleep(1)
    varBarra.set(20)
    root.update()
    time.sleep(1)
    base = pd.read_excel(arquivo, engine='openpyxl')
    varBarra.set(30)
    root.update()
    time.sleep(1)
    previsores = base.iloc[:,:12].values #ESCOLHER QUAL COLUNA QUER AGRUPAR
    varBarra.set(40)
    root.update()
    time.sleep(1)
    classe = base['Classe'].values
    varBarra.set(50)
    root.update()
    time.sleep(1)

    X,Y = previsores,classe
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 10)
    varBarra.set(60)
    root.update()

    modelo = LinearSVC()
    varBarra.set(70)
    root.update()
    time.sleep(1)
    modelo.fit(X_train,Y_train)
    varBarra.set(80)
    root.update()
    time.sleep(1)
    misterioso2 = [1,1,1,1,1,1,1,1,1,1,1,1]
    varBarra.set(100)
    root.update()
    msg = 'Modelo treinado com sucesso!'
    messagebox.showinfo("Classificador de biscoitos - Bela vista v1.0", msg)
    root.withdraw()
    janela.deiconify()

def dashboard():
    print("abrindo dashboard no power BI")
    webbrowser.open('https://app.powerbi.com/view?r=eyJrIjoiZDI2ZGRhZjItZDAwMy00NDZmLTk1NTMtNmIzODk1YzA2MWM2IiwidCI6IjJiZmNjODY0LTc5MjktNGVlYi05ZGQ1LWJjYmEwMmNlZDlkYyJ9&pageName=ReportSection')

def voltar():
    global lbltitulo2, pb
    print("voltou")

    root.geometry("300x330+750+300")
    root.resizable(False, False)

    lbltitulo2.destroy()
    pb.destroy()
    janela.withdraw()
    root.deiconify()


#LAYOUT BOTÃO CLASSIFICAR
lblclassificar = ttk.Button(janela, text = "Estimar", command=estimar)
lblclassificar.grid(column=2,row=14)

#LAYOUT BOTÃO DASHBOARD
lbldash = ttk.Button(root, text = "Dashboard", width = '15', command=dashboard)
lbldash.grid(column=0,row=3, pady=(10,10))

#LAYOUT BOTÃO TREINAR IA
lblclassificador = ttk.Button(root, text = "Treinar IA", width = '15', command=treinarIA)
lblclassificador.grid(column=0,row=4, pady=(10,10))

#LAYOUT BOTÃO VOLTAR
lblvoltar = ttk.Button(janela, text = "Voltar", command=voltar)
lblvoltar.place(x = 700,y=804)

root.mainloop()
janela.mainloop()
