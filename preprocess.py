import pandas as pd



def preprocess(calories,exercise):
    df = pd.merge(calories,exercise,on='User_ID')
    df = df.replace({'Gender':{'male':0,'female':1}})
    df = df.drop('User_ID',axis=1)

    x = df.drop('Calories',axis=1)
    y = df['Calories']

    return x,y