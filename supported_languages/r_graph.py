from functionNode import functionNode

class r_graph:
    graph_len = 0
    data = []
    function_Node_List = []
    libraries_List = set()
    packages_List = set()
    url_List = set()
    
    ###
    __name = ''
    __params = ''
    __body = ''
    __hasBody = False
    __oneMoreLine = False
    __findFunction = False


    def __init__(self, df):
        self.data = df
        self.files_walk(df)
        self.build_graph()


    def files_walk(self, df):
        for i in list(df.index):
            self.file_reader(df.at[i,"path"], df.at[i,"filename"])

            
    def file_reader(self, path, filename):
        filepath = path + filename
        file = open(filepath, 'r')
        lines = file.readlines()
        
        for line in lines:
            self.line_checker(line)
            if self.__hasBody:
                self.create_node(filepath)
                self.reinitialize()
                
                
    def line_checker(self, line):         
        if "http" in line or "www" in line: 
            self.url_extract(line)
        
        elif "library" in line: 
            self.library_extract(line)
        
        elif "package" in line: 
            self.package_extract(line)
        
        elif "<-" in line:
            self.__name = self.name_extract(line)            
            self.find_funcSignature(line)
        
        elif self.__oneMoreLine or self.__findFunction:
            self.find_funcSignature(line)            

        
    def find_funcSignature(self, line):
        if self.__findFunction:
            self.__body += line 
            if "{" in line:
                self.__params = self.parenthesis_extract(self.__body)
            elif "}" in line:
                self.__hasBody = True

        elif "function" in line:            
            self.__findFunction = True
            self.__body += line 
            if "{" in line: #if { in line, then ) is also
                self.__params = self.parenthesis_extract(line)
            
        else: # need one more line
            if self.__oneMoreLine: #but u already had one more line
                pass   # isnt a function       
            else:
                self.__oneMoreLine = True


    def create_node(self, filepath):
        self.graph_len += 1
        self.function_Node_List.append(functionNode(self.graph_len, filepath, self.__name, self.__params, self.__body))        
        
        
    def reinitialize(self):
            self.__name = ''
            self.__params = ''
            self.__body = ''
            self.__hasBody = False
            self.__oneMoreLine = False
            self.__findFunction = False
        
    
    def build_graph(self):
        for function in self.function_Node_List:
            for function_compared in self.function_Node_List:
                if function.name in function_compared.body:
                    function.addCall(function_compared.name)
                    function_compared.addCalled(function.name)  
                  

    def url_extract(self,text):
        # MELHORAR
        self.url_List.add(text)
        
        
    def library_extract(self, text):
        lib = self.parenthesis_extract(text)
        self.libraries_List.add(lib)


    def package_extract(self, text):
        pac = self.parenthesis_extract(text)
        self.packages_List.add(pac)

  
    def name_extract(self, text):
        return text[: text.find("<-")]


    def parenthesis_extract(self, text):
        return text[text.find("(")+1 : text.rfind(")")]
    
    
    def baned(self, text):
        ban = ["suppressMessages", "suppressWarnings", "error"]        
        i = 0
        while i < len(ban):
            if ban[i] in text: return True
            i+=1
        return False
    
    
 
    
