import sys
sys.path.insert(0, '/home/trevo/Desktop/Definitivo/GitHub/repos/arch_builder')

from graph_nodes.functionNode import FunctionNode
from supported_languages.stack import Stack

class R_graph:
    graph_len = 0
    nodeList = []
    
    # file aux
    __stack = Stack()
    __file = ''
    
    # node aux
    __node = FunctionNode()  
    __hasBody = False
    __hasSignature = False



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
            self.reinitializeNode()
            self.reinitializeStack()
            
            self.__file = df.at[i,"path"] + df.at[i,"filename"]
            
            # iterates lines through file
            file = open(self.__file, 'r')
            lines = file.readlines()
            
            for line in lines:                
                self.line_consumer(line) # procedures for line content

            
    
    def line_consumer(self, line):
        self.__stack.addData(line)
        
        if "<-" in line: self.__stack.addAssign()
        if "function" in line: self. __hasSignature = True
        if "{" in line:
            self.__stack.addOB()
            if self.__hasSignature:
                self.__node.name, self.__node.args = self.__stack.signatureExtract()
                self. __hasSignature = False #finished collecting signature
            self.__hasBody = True      # block begins
        if "}" in line:
            self.__stack.addCB()
            if self.__hasBody: 
                self.__node.body, self.__node.returns = self.__stack.bodyExtract()
                self.addExtraInfo()
                self.addNode()
                
                
            
    def addNode(self):
        self.__node.filepath = self.__file
        self.nodeList.append(self.__node)
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
        self.__node.filepath = ''
        self.__node.name = ''
        self.__node.args = []
        self.__node.returns = []
        self.__node.body = ''
        self.__node.calls = set()
        self.__node.calledby = set()  
        self.__hasBody = False
        self.__hasSignature = False
        
    
    
    def reinitializeStack(self): 
        self.__stack = Stack()
        
