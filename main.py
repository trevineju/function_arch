
import os
import pandas as pd

# importing sys
import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/home/trevo/Desktop/Definitivo/GitHub/repos/arch_builder')

from supported_languages.r_graph import r_graph
        
def filesData(project_diretory):
    aux = [[],[],[]]
    for root, dirs, files in os.walk(project_diretory):
        aux[0] += [root + "/"]*len(files)
        aux[1] += files
        for file in files:
            aux[2].append(file[file.find(".")+1:])
    return pd.DataFrame(aux).transpose().rename(columns={0: "path", 1: "filename", 2: "extension"})

    
def main():
    directory = "/home/trevo/Desktop/Definitivo/GitHub/repos/-reforma-perfil-parlamentar-dados"
    
    # DATA
    data = filesData(directory)
    
    #PROCESSING
    #dbInfo = data[data['extension'].isin(["csv", "csv.zip"])]
    rInfo = r_graph(data[data['extension'] =='R'])
    
    
    return rInfo
    
    

    
   
    
    
    
#if __name__ == "__main__":
#    main()





