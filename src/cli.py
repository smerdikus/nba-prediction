import argparse, json
from src.pipeline import run
from src.data.loader import load_live
from src.features import nba, soccer, tennis
from src.models.predict import load as load_model, predict

LIVE_FE={'nba':nba.engineer,'soccer':soccer.engineer,'tennis':tennis.engineer}

def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='cmd',required=True)

    t=sub.add_parser('train')
    t.add_argument('--sport',choices=['nba','soccer','tennis'],required=True)
    t.add_argument('--seasons',nargs='+',required=True)

    q=sub.add_parser('predict')
    q.add_argument('--sport',choices=['nba','soccer','tennis'],required=True)
    q.add_argument('--home'); q.add_argument('--away')

    args=p.parse_args()

    if args.cmd=='train':
        kw={}
        if args.sport=='nba': kw={'seasons':args.seasons}
        elif args.sport=='soccer': kw={'league_code':'PL','seasons':[int(s) for s in args.seasons]}
        else: kw={'years':[int(y) for y in args.seasons]}
        run(args.sport, kw)

    else:
        live=load_live(args.sport)
        if args.home and args.away:
            if args.sport=='nba':
                mask=(live['HOME_TEAM_ABBREVIATION']==args.home)&(live['VISITOR_TEAM_ABBREVIATION']==args.away)
            elif args.sport=='soccer':
                mask=(live['homeTeam.shortName']==args.home)&(live['awayTeam.shortName']==args.away)
            else: raise ValueError("For tennis provide player names differently.")
            match=live[mask].head(1)
        else:
            match=live.head(1)
        fe=LIVE_FE[args.sport](match).iloc[0].to_dict()
        model=load_model(args.sport)
        prob=predict(model,fe)
        print(json.dumps({'home_win_probability':prob},indent=2))

if __name__=='__main__':
    main()
