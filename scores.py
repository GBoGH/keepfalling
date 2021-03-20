import pandas as pd

def dictionary():
    df = pd.read_csv("highscores.csv")
    df = df.sort_values("SCORE", ascending=False)
    scores = df.to_dict(orient="records")
    return scores

def bestx(arr, n):
    output = ["HIGHSCORES:"]

    if len(arr) < n:
        x = len(arr)
    else:
        x = n
    for i in range(x):
        name = arr[i].get("NAME")
        score = arr[i].get("SCORE")
        output.append(f"{name}  {score}")

    return output
