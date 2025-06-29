from src.data.loader import load_historical
from src.features import nba, soccer, tennis
from src.models.train import train

FE={'nba':nba.engineer,'soccer':soccer.engineer,'tennis':tennis.engineer}

def run(sport:str, load_kwargs:dict):
    df=load_historical(sport, **load_kwargs)
    df=FE[sport](df)
    train(df,sport)
