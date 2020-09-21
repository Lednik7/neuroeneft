import matplotlib.pyplot as plt
import pandas as pd

def plot(df, fcst, n=7, xlabel='Дата', ylabel='Цена', figsize=(10, 6)):
    """
    df - датафрейм со всемии данными
    fcst(forecast) - предсказание модели
    P.S. Лучше не пытайся разбирать код, я сам хз))
    """
    
    df = df[-100:]
    fcst = fcst[-100:]

    df['ds'] = fcst["ds"].to_list()

    df = df[-(24+n):-n]
    fcst = fcst[-n:]
    temp = [df.iloc[-1], fcst.iloc[0]]
    temp2 = pd.DataFrame({"ds":[temp[0]["ds"], temp[1]["ds"]], "y":[temp[0]["y"], temp[1]["yhat"]]})
    
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    fig = ax.get_figure()
    

    ax.plot(df['ds'].dt.to_pydatetime(), df['y'], '-', c="#0072B2")

    ax.plot(temp[0]["ds"], temp[0]["y"], ".", c="red")

    ax.plot(temp2['ds'].dt.to_pydatetime(), temp2['y'], "-", c="green")

    fcst_t = fcst['ds'].dt.to_pydatetime()
    ax.plot(fcst_t, fcst['yhat'], '-', c='green')

    ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.6)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig
