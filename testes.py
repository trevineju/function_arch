




#        
#
#def testa_graph(aux):
#    filepathList = []
#    nameList = [] 
#    argsList = [] 
#    bodyList = [] 
#    callsList = [] 
#    calledbyList = []
#    
#    for node in aux.function_Node_List:
#        imprime_no(node)
#        filepathList = filepathList.append(node.filepath)
#        nameList = nameList.append(node.name)
#        argsList = argsList.append(node.args)
#        bodyList = bodyList.append(node.body) 
#        callsList = callsList.append(node.calls) 
#        calledbyList = calledbyList.append(node.calledby)
#        
#    return [filepathList, nameList, argsList, bodyList, callsList, calledbyList]
#    
#
#def testa_dados(aux):
#    return (aux.data)    
#    
#def testa_listaNo(aux):
#    return (aux.function_Node_List)    
#    
#def testa_lib(aux):
##    for item in aux.libraries_List:
##        print(item)
#    return(aux.libraries_List)
#    
#    
#def testa_pack(aux):
##    for item in aux.packages_List:
##        print(item)
#    return(aux.packages_List)
#    
#
#def testa_url(aux):
##    for item in aux.url_List:
##        print(item)    
#    return(aux.url_List)
#    
#
#
#
#
#

#
#
#
## TESTA NODE
#testa_node(aux)
#
## TESTA GRAFO
#infos = testa_graph(aux)
#libs = testa_lib(aux)
#packs = testa_pack(aux)
#urls = testa_url(aux)
#
#
#
#        
###COLOCAR EM FILE NODE
##if str(node.filepath) in countAux.keys(): countAux[str(node.filepath)] += 1
##else: countAux[str(node.filepath)] = 0
#


#################################################

#           TESTA CONSTRUÇÃO DE NÓ              #

#################################################

from functionNode import functionNode

        
def testa_construcao_no(data=[]):    
    if data == []:
        f = 0
        aList, bList, cList, dList, eList, fList = [], [], [], [], [], []
        for a in gera_filepath():
            for b in gera_name():
                for c in gera_args():
                    for d in gera_body():
                        no = functionNode(f, a, b, c, d)
                        imprime_no(no)
                        
                        for e in gera_conjunto():
                            no.addCall(e)
                            no.addCalled(e)
                            
#                        imprime_no(no)
                        testa_coesao(no)
                                            
                        aList += [no.filepath]
                        bList += [no.name]
                        cList += [no.args]
                        dList += [no.body]
                        eList += [list(no.calls)]
                        fList += [no.codref]
                        
                        f+=1
                    
    else:
        no = functionNode(data[0], data[1], data[2], data[3], data[4])
        imprime_no(no)
        testa_coesao(no)
        
                    
    return aList, bList, cList, dList, eList, fList
                    
                    
def imprime_no(node):
    if node == None:
        print(">>>>>>>>>>>>>>>>>>> ERRO DE CONSTRUÇÃO DO NÓ")
    else:
        print("-"*30)
        print(f"COD:   {node.codref}")
        print(f"FILE:   {node.filepath}")
        print(f"NAME:   {node.name}")
        print(f"ARGS:   {node.args}")
        print(f"BODY:   {node.body}")
        print(f"CALLS:   {node.calls}")
        print(f"CALLED:   {node.calledby}")


def testa_coesao(node):
    if node.filepath == node.name: print("ERRO 0")
    if node.filepath == node.args: print("ERRO 1")
    if node.filepath == node.body: print("ERRO 2")
    if node.filepath == node.calls: print("ERRO 3")
    if node.filepath == node.calledby: print("ERRO 4")
    
    if node.name == node.args: print("ERRO 5")
    if node.name == node.body: print("ERRO 6")
    if node.name == node.calls: print("ERRO 7")
    if node.name == node.calledby: print("ERRO 8")
    
    if node.args == node.body: print("ERRO 9")
    if node.args == node.calls: print("ERRO 10")
    if node.args == node.calledby: print("ERRO 11")
    
    if node.body == node.calls: print("ERRO 12")
    if node.body == node.calledby: print("ERRO 13")
    
    #if node.calls == node.calledby: print("ERRO 14")

def gera_filepath():
    return ['','../../../arquivo']

def gera_name():
    return ['','funcao_ficticia', ' funcao_ficticia ']

def gera_args():
    return [[],['arg1', 'arg2'], [' arg1 ', ' arg2 ']]

def gera_body():
    return ['', 'blablabla']

def gera_conjunto():
    return ['', 'blablabla']   


#################################################

#          TESTA CONSTRUÇÃO DE GRAFO            #

#################################################

from r_graph import r_graph


def testa_construcao_grafo(data):
    aux = r_graph(data)
    
    tamanho = acessa_len(aux)
    nodeList = acessa_listaNos(aux)
    libList = list(acessa_listaBibliotecasgraph(aux))
    packList = list(acessa_listaPacotes(aux))
    urlList = list(acessa_listaUrls(aux))
    
    codList = []
    filepathList = []
    nameList = []
    argsList = []
    bodyList = []
    callsList= []
    calledList = []       
    
    for no in nodeList:
        codList += [no.codref]
        filepathList += [no.filepath]
        nameList += [no.name]
        argsList += [no.args]
        bodyList += [no.body]
        callsList += [list(no.calls)]
        calledList += [list(no.calledby)]  
        
        testa_coesao(no)
        imprime_no(no)
    
    return tamanho, nodeList, libList, packList, urlList, codList, filepathList, nameList, argsList, bodyList, callsList, calledList 

    

def acessa_len(graph):
    return graph.graph_len

def acessa_listaNos(graph):
    return graph.function_Node_List

def acessa_listaBibliotecasgraph(graph):
    return graph.libraries_List    

def acessa_listaPacotes(graph):
    return graph.packages_List
    
def acessa_listaUrls(graph):
    return graph.url_List


# CHAMADA DE TESTES
    
## TESTA CONSTRUÇÃO DE NÓ   
#a_pathList, b_nameList, c_argsList, d_bodyList, e_callsList, f_codsList = testa_construcao_no()

# TESTA CONSTRUÇÃO DE GRAFO

#cria df para teste
from main import filesData


directory = "/home/trevo/Desktop/Definitivo/GitHub/repos/-reforma-perfil-parlamentar-dados"
data = filesData(directory)
data = data[data['extension'] =='R']
data = data.iloc[0:1,]

a_tamanho, a_nodeList, a_libList, a_packList, a_urlList, a_codList, a_filepathList, a_nameList, a_argsList, a_bodyList, a_callsList, a_calledList = testa_construcao_grafo(data)




