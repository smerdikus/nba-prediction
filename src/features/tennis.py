import pandas as pd
from .elo import apply_elo
def engineer(df:pd.DataFrame)->pd.DataFrame:
    df1=df[['Winner','Loser']].copy(); df1.columns=['TEAM','OPP']; df1['label']=1
    df2=df[['Loser','Winner']].copy(); df2.columns=['TEAM','OPP']; df2['label']=0
    all_df=pd.concat([df1,df2],ignore_index=True)
    all_df['HOME']=0
    all_df=apply_elo(all_df,'TEAM','OPP','label',k=32)
    all_df['rest_days']=7
    return all_df[['elo_diff','HOME','rest_days','label']]
