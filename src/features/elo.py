from collections import defaultdict
import pandas as pd
def update(r1,r2,score,k=20):
    exp=1/(1+10**((r2-r1)/400))
    return r1+k*(score-exp), r2+k*((1-score)-(1-exp))
def apply_elo(df, team_col, opp_col, res_col, k=20, init=1500):
    ratings=defaultdict(lambda:init)
    pre,opp=[],[]
    for _,row in df.iterrows():
        t,o=row[team_col],row[opp_col]
        r_t,r_o=ratings[t],ratings[o]
        pre.append(r_t); opp.append(r_o)
        ratings[t],ratings[o]=update(r_t,r_o,row[res_col],k)
    df=df.copy(); df['elo_pre']=pre; df['elo_opp']=opp; df['elo_diff']=df['elo_pre']-df['elo_opp']
    return df
