import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

##2
df=pd.read_csv('world_alcohol.csv')
out=df.loc[(df['WHO region']=='Africa') | (df['WHO region']=='Eastern Mediterranean') | (df['WHO region']=='Europe')]
print(out)

##3
out=df.loc[(df['WHO region']!='Africa') & (df['WHO region']!='Eastern Mediterranean') & (df['WHO region']!='Europe')]
print(out)

##4
out=df.loc[(df['Display Value']>0.5) & (df['Display Value']<2.5)]
print(out)

##5
out=df.loc[(df['Beverage Types']=='Wine') & (df['Display Value']>2)]
print(out)

##6
def last_0_bool(df):
    bool_ls=[]
    for i in df.index:
        i=str(i)
        bool_ls.append(i[-1]!='0')
    return bool_ls

out=df.loc[last_0_bool(df)]
print(out)    

##7
out=df.iloc[0:9,0:3]
print(out)

##8
index_ls=range(1,100,5)
out=df.iloc[list(range(1,100,5))]
print(out)

#9
student_data.groupby('school_code')
print(type(student_data.groupby('school_code')))

#10
out=student_data.groupby('school_code').agg({'age':['mean','min','max']})
print(out)

#11
student_data.groupby(['school_code','class'])

#12
my_df=pd.DataFrame({'a':np.random.randn(10),'b':np.random.randn(10),'c':np.random.randn(10),'d':np.random.randn(10)})
my_df= my_df.applymap(lambda x: x if x>0 else np.nan)

def highlighter(cell_value):
    if cell_value!=cell_value:
        return "background-color: yellow"

my_df.style.applymap(highlighter)

#13
column_color_dict={}

for i,j in zip(my_df.columns,['grey','yellow','blue','red']):
    column_color_dict[i]=j

   
def f(dat, c):
    return [f'background-color: {c}' for i in dat]

my_df_style=my_df.style
for column, color in column_color_dict.items():
    
    my_df_style=style.apply(f, axis=0,subset=column,c=color)
    
my_df_style

#14
my_df.style.background_gradient(cmap ='YlOrRd',axis=None)