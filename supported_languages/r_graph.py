import sys
sys.path.insert(0, '/home/trevo/Desktop/Definitivo/GitHub/repos/arch_builder')

from graph_nodes.functionNode import FunctionNode
from supported_languages.stack import Stack

class R_graph:
    graph_len = 0
    nodeList = []
    
    # file aux
    stack = Stack()
    file = ''
    
    # node aux
    node = FunctionNode()  
    hasBody = False
    hasSignature = False



    def __init__(self, df):
        ''' (DataFrame) -> None
        df: tabela de arquivos 
        '''
        self.build_nodes(df)
        self.build_graph()



    def build_nodes(self, df):
        ''' (DataFrame) -> None
        Alimenta lista de nós ao percorrer arquivos do df para encontrar funções (nós)
        '''
        # iterates through dir files
        for i in list(df.index):            
            self.file = df.at[i,"path"] + df.at[i,"filename"]
            
            # iterates lines through file
            file = open(self.file, 'r')
            lines = file.readlines()
            
            for line in lines:                
                self.line_consumer(line) # procedures for line content
            
            self.reinitializeNode()
            self.reinitializeStack()

            
    
    def line_consumer(self, line):
        self.stack.addData(line)
        
        if "<-" in line: 
            self.stack.addAssign()
        if "function" in line: 
            functionPosition = len(self.stack.data)-1
            assignPosition = self.stack.assignments[-1]
            if functionPosition - assignPosition == 0 or functionPosition - assignPosition == 1:
                self.hasSignature = True
        if "{" in line:
            self.stack.addOB()
            if self.hasSignature:
                self.node.name, self.node.args = self.stack.signatureExtract()
            self.hasBody = True      # block begins
        if "}" in line:
            self.stack.addCB()
            if self.hasSignature and self.hasBody:
                self.node.body = self.stack.bodyExtract()
                self.addExtraInfo()
                self.addNode()

                
    def addNode(self):
        self.node.filepath = self.file
        self.nodeList.append(self.node)
        self.graph_len += 1
        self.reinitializeNode()
     



    def addExtraInfo(self): pass
#        
#
#         
#        if "http" in line or "www" in line: 
#            self.url_extract(line)
#        
#        elif "library" in line: 
#            self.library_extract(line)
#        
#        elif "package" in line: 
#            self.package_extract(line)
#        
#        elif "<-" in line:
#            self.__name = self.name_extract(line)            
#            self.find_funcSignature(line)
#        
#        elif self.__oneMoreLine or self.__findFunction:
#            self.find_funcSignature(line)            

    
    def build_graph(self):
        for i in range(self.graph_len):
            for j in range(self.graph_len):
                if i == j: pass
                else:
                    if self.nodeList[i].name in self.nodeList[j].body:
                        self.nodeList[j].addCall(self.nodeList[i].name)

                  

#    def url_extract(self,text):
#        # MELHORAR
#        self.url_List.add(text)
#        
#        
#    def library_extract(self, text):
#        lib = self.parenthesis_extract(text)
#        self.librariesList.add(lib)
#
#
#    def package_extract(self, text):
#        pac = self.parenthesis_extract(text)
#        self.packages_List.add(pac)
#
#  
#
#    
#    
#    def baned(self, text):
#        ban = ["suppressMessages", "suppressWarnings", "error"]        
#        i = 0
#        while i < len(ban):
#            if ban[i] in text: return True
#            i+=1
#        return False
    
    
 
    def reinitializeNode(self):
        self.node = FunctionNode()
        self.hasBody = False
        self.hasSignature = False       
    
    
    def reinitializeStack(self): 
        self.stack = Stack()
        self.file = ''

        
