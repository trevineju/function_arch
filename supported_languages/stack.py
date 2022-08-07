class Stack:
    data = []                       
    aux_text = ''
    
    assignments = []
    opening_brackets = []           
    closening_brackets = []              
    
    def __init__(self):
        '''(None) -> None
        '''
        
    def addData(self, line):
        ''' (string) -> None
        '''
        self.data.append(line)
        
    def addAssign(self):
        '''
        '''
        self.assignments.append(len(self.data)-1)    
    
    def addOB(self):
        '''
        '''
        self.opening_brackets.append(len(self.data)-1)

    def addCB(self):
        '''(None) -> string
        '''
        self.closening_brackets.append(len(self.data)-1)
        
        
        
    def bodyExtract(self):
        ''' (None) -> string
        '''
        if self.interation_needed("bodyExtract"):
            for i in range(self.opening_brackets[-1], self.closening_brackets[-1]+1):
                self.aux_text += self.data[i]
        else: 
            self.aux_text = self.data[-1]
        
        body = self.aux_text
        self.aux_text = ''  #clears aux text
        
        return body
    
    def returnsExtract(self):
        '''
        '''
        returns = self.aux_text[self.aux_text.find("return"):]
        returns = self.string_split(self.parenthesis_extract(returns))

        return returns
        
        
    
        
    def remove(self):
        '''
        '''
        pass
    
    def signatureExtract(self):
        '''(None) -> string, list
        '''
        if self.interation_needed("signatureExtract"):
            for i in range(self.assignments[-1], self.opening_brackets[-1]+1):
                self.aux_text += self.data[i]
        else: 
            self.aux_text = self.data[-1]
 
        name = self.name_extract(self.aux_text)
        args = self.string_split(self.parenthesis_extract(self.aux_text))
        
        self.aux_text = ''  #clears aux text
        
        return name, args            
            
            
    def name_extract(self, text):
        '''(string) -> string
        '''
        return text[: text.find("<-")].strip()


    def parenthesis_extract(self, text):
        '''(string) -> string
        '''
        return text[text.find("(")+1 : text.rfind(")")]
            
    
    def string_split(self, string):
        '''(string) -> list
        '''
        string = string.split(",")
        for i in range(len(string)):
            string[i] = string[i].strip()
        return string
        
    
        
    def interation_needed(self, operacao):        
        if operacao == "signatureExtract":
            if self.assignments[-1] != self.opening_brackets[-1]: return True  
            else: return False
        if operacao == "bodyExtract":
            if self.opening_brackets[-1] != self.closening_brackets[-1]: return True  
            else: return False
        
        
        

        