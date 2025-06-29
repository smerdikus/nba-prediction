import pandas as pd
from .elo import apply_elo
def engineer(df:pd.DataFrame)->pd.DataFrame:
    df=df.copy()
    df['TEAM']=df['homeTeam.shortName']
    df['OPP']=df['awayTeam.shortName']
    df['label']=(df['score.fullTime.home']>df['score.fullTime.away']).astype(int)
    df['HOME']=1
    df=apply_elo(df,'TEAM','OPP','label',k=20)
    df['rest_days']=7
    return df[['elo_diff','HOME','rest_days','label']]
