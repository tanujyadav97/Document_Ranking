def normalize(smallisbetter,score):
    vsmall=0.00001
    if smallisbetter:
        minscore=max(vsmall,min(score.values()))
        return dict([(u,float(minscore)/max(vsmall,l)) for (u,l) in score.items()])
    else:
        maxscore=max(score.values())
        if maxscore==0:maxscore=vsmall
        return dict([(u,float(c)/maxscore) for (u,c) in score.items()])