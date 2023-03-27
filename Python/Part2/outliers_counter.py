import pandas as pd
import numpy as np


train=pd.read_csv('train.csv')

t_d=train.describe()

q_ls=list(train.dtypes.loc[train.dtypes!='O'].index)

p_25=t_d.loc['25%',q_ls]
p_75=t_d.loc['75%',q_ls]
r_intq=p_75-p_25

low_bound=p_25-1.5*r_intq
upp_bound=p_75+1.5*r_intq


def outliers_finder(x,low_bound,upp_bound,column):
    
    
    
    if x <low_bound[column]:
        return ('low')
    
    if x >upp_bound[column]:
        return ('high')
    
    else:
        return ('middle')
                
        
        
def outliers_detector(q_ls,low_bound,upp_bound):
    
    outliers={}

    for i in q_ls:
        #print(i)



        s=train[i].apply(outliers_finder,args=(low_bound,upp_bound,i))

        a=s.value_counts()
        #print(a)
        val=list(a.values)
        indx=list(a.index)
        score={}



        k_n=0

        tl={}
        for k in indx:
            #print('k', k)

            score={}
            score[k]={val[k_n]}
            #print('score',score)

            k_n+=1

            tl.update(score)
            #print('tl:',tl)


        outliers[i]=tl
        
    return outliers