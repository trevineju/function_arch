




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










import os
import pandas as pd

# importing sys
import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/home/trevo/Desktop/Definitivo/GitHub/repos/arch_builder')






def filesData(project_diretory):
    aux = [[],[],[]]
    for root, dirs, files in os.walk(project_diretory):
        aux[0] += [root + "/"]*len(files)
        aux[1] += files
        for file in files:
            aux[2].append(file[file.find(".")+1:])
    return pd.DataFrame(aux).transpose().rename(columns={0: "path", 1: "filename", 2: "extension"})


#################################################

#           TESTA CONSTRUÇÃO DE NÓ              #

#################################################

from graph_nodes.functionNode import FunctionNode

        
#def testa_construcao_no(data=[]):    
#    if data == []:
#        f = 0
#        aList, bList, cList, dList, eList, fList = [], [], [], [], [], []
#        for a in gera_filepath():
#            for b in gera_name():
#                for c in gera_args():
#                    for d in gera_body():
#                        no = FunctionNode(f, a, b, c, d)
#                        imprime_no(no)
#                        
#                        for e in gera_conjunto():
#                            no.addCall(e)
#                            no.addCalled(e)
#                            
##                        imprime_no(no)
#                        testa_coesao(no)
#                                            
#                        aList += [no.filepath]
#                        bList += [no.name]
#                        cList += [no.args]
#                        dList += [no.body]
#                        eList += [list(no.calls)]
#                        fList += [no.codref]
#                        
#                        f+=1
#                    
#    else:
#        no = FunctionNode(data[0], data[1], data[2], data[3], data[4])
#        imprime_no(no)
# 
#        
#                    
#    return aList, bList, cList, dList, eList, fList
                    
                    
def imprime_no(node):
    if node == None:
        print(">>>>>>>>>>>>>>>>>>> ERRO DE CONSTRUÇÃO DO NÓ")
    else:
        print("-"*30)
        print(f"FILE:   {node.filepath}")
        print(f"NAME:   {node.name}")
        print(f"ARGS:   {node.args}")
        print(f"RETURNS:   {node.returns}")
        print(f"BODY:   {node.body}")
        print(f"CALLS:   {node.calls}")
        print(f"CALLED:   {node.calledby}")




#################################################

#          TESTA CONSTRUÇÃO DE GRAFO            #

#################################################

from supported_languages.r_graph import R_graph
from supported_languages.stack import Stack


def testa_construcao_grafo(data):
    aux = R_graph(data)
    
    tamanho = acessa_len(aux)
    nodeList = acessa_listaNos(aux)
#    libList = list(acessa_listaBibliotecasgraph(aux))
#    packList = list(acessa_listaPacotes(aux))
#    urlList = list(acessa_listaUrls(aux))
    
    filepathList = []
    nameList = []
    argsList = []
    returnsList = []
    bodyList = []
    callsList= []
    calledList = []       
    
    for no in nodeList:
        filepathList += [no.filepath]
        nameList += [no.name]
        argsList += [no.args]
        returnsList += [no.returns]
        bodyList += [no.body]
        callsList += [list(no.calls)]
        calledList += [list(no.calledby)]  
        
        imprime_no(no)
    
    return tamanho, nodeList, filepathList, nameList, argsList, returnsList, bodyList, callsList, calledList 

    

def acessa_len(graph):
    return graph.graph_len

def acessa_listaNos(graph):
    return graph.nodeList

#def acessa_listaBibliotecasgraph(graph):
#    return graph.libraries_List    
#
#def acessa_listaPacotes(graph):
#    return graph.packages_List
#    
#def acessa_listaUrls(graph):
#    return graph.url_List


# CHAMADA DE TESTES
    
## TESTA CONSTRUÇÃO DE NÓ   
#a_pathList, b_nameList, c_argsList, d_bodyList, e_callsList, f_codsList = testa_construcao_no()

# TESTA CONSTRUÇÃO DE GRAFO

#cria df para teste
directory = "/home/trevo/Desktop/Definitivo/GitHub/repos/-reforma-perfil-parlamentar-dados"
data = filesData(directory)
data = data[data['extension'] =='R']
data = data.iloc[0:30,]

a_tamanho, a_nodeList, a_filepathList, a_nameList, a_argsList, a_returnsList, a_bodyList, a_callsList, a_calledList = testa_construcao_grafo(data)

print("fim!")



