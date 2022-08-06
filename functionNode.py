class functionNode:
    codref = 0
    filepath = ''
    name = ''
    args = []
    body = ''
    calls = set()
    calledby = set()
    
    def __init__(self, cod, filepath, name, args, text):
        self.codref = cod
        self.filepath = self.trata_texto(filepath)
        self.name = self.trata_texto(name)
        self.args = self.trata_listaTexto(args)
        self.body = text
        
    def addCall(self, text):
        if text not in self.calls: self.calls.add(text)

    def addCalled(self, text):
        if text not in self.calledby: self.calledby.add(text)
        
    def trata_texto(self, item):
        return item.strip()
        
    def trata_listaTexto(self, lista):
        lista = lista.split(",")
        for i in range(len(lista)):
            lista[i] = self.trata_texto(lista[i])
        return lista
        
        
        
                
            
        