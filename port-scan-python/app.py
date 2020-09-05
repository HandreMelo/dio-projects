import tkinter as tk
import pscan_nmap_v2 as psnmap

fields = {
    'entryLabels': {
        'Portas',
        'Ip / Hostname'
    },
    'radios':{
        'Varredura do tipo SYN':'1',
        'Varredura do Tipo UDP':'2',
        'Varredura do Tipo Instensa':'3',
    },
    'resultLabels':{
        'Versão do Nmap :', 
        'Status do IP :',
        'Protocolos :',
        'Portas Abertas :',
        'Status da Solicitação :'
    }
}

def showResults(results,labelObj):

    labelObj['Versão do Nmap :']['text'] = 'Versão do Nmap :'+str(results['version'])
    labelObj['Status do IP :']['text'] = 'Status do IP :'+str(results['status'])
    labelObj['Protocolos :']['text'] = 'Protocolos :'+str(results['protocols'])
    labelObj['Portas Abertas :']['text'] = 'Portas Abertas :'+str(results['doors'])
    labelObj['Status da Solicitação :']['text'] = labelObj['Status da Solicitação :']['text']+' Sucesso'

def fetch(entradas,labelObj):
    opcao = option.get()
    ip = entradas['Ip / Hostname'].get()
    portas = entradas['Portas'].get()
        
    results = psnmap.startScan(ip, portas, opcao)
    if results:
        showResults(results,labelObj)
    else:
        labelObj['Status da Solicitação :']['text'] = labelObj['Status da Solicitação :']['text']+' Ocorreu um erro'

def makeform(root, fields):
    entradas = {}
    entryLabels = fields['entryLabels']
    radios = fields['radios']
    resultLabels = fields['resultLabels']
    res = {}
    
    for label in entryLabels:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=label, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entradas[label] = ent
    
    for radio in radios:
        r = tk.Radiobutton(root, text=radio, value=radios[radio], var=option)
        r.pack(side=tk.TOP, anchor='n')
    
    for label in resultLabels:
        row = tk.Frame(root)
        lab = tk.Label(row,  text=label, anchor='w')
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        res[label] = lab
        
    return res,entradas

if __name__ == '__main__':
    root = tk.Tk()
    option = tk.StringVar()
    res,ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e,res)))   
    b1 = tk.Button(root, text='Scan', command=(lambda e=ents: fetch(e,res)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
