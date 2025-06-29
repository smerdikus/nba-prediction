import pandas as pd
from dateutil import parser
from .elo import apply_elo

def engineer(df:pd.DataFrame)->pd.DataFrame:
    df=df.copy()
    df['GAME_DATE']=pd.to_datetime(df['GAME_DATE'])
    df['HOME']=df['MATCHUP'].str.contains(' vs ')
    df['label']=(df['WL']=='W').astype(int)
    df['OPP']=df.apply(lambda r: r['MATCHUP'].split(' ')[-1] if r['HOME'] else r['MATCHUP'].split(' ')[0],axis=1)
    df=apply_elo(df,'TEAM_ABBREVIATION','OPP','label',k=20)
    df=df.sort_values(['TEAM_ABBREVIATION','GAME_DATE'])
    df['prev_date']=df.groupby('TEAM_ABBREVIATION')['GAME_DATE'].shift(1)
    df['rest_days']=(df['GAME_DATE']-df['prev_date']).dt.days.fillna(7)
    return df[['elo_diff','HOME','rest_days','label']]
