import pandas as pd

def dictionary():
    df = pd.read_csv("highscores.csv")
    df = df.sort_values("SCORE", ascending=False)
    scores = df.to_dict(orient="records")
    return scores

def bestx(dict, n):
    output = ["HIGHSCORES:"]
    for i in range(n):
        name = dict[i].get("NAME")
        score = dict[i].get("SCORE")
        output.append(f"{name}  {score}")

    return output
