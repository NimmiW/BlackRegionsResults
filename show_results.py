import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy


def plot_results(year, from_month, to_month, currency):

    start_date = str(year) + "-" + str(from_month) + "-01"
    #end_date = request.form["year"] + "-" + str(int(request.form["to_month"]) + 1) + "-01"
    if (to_month == 12):
        end_date = str(year + 1) + "-" + str(1) + "-01"
    else:
        end_date = str(year) + "-" + str(to_month + 1) + "-01"

    quotes = pd.read_csv("data/"+currency+"/DAT_MT_"+currency+"_M1_" + str(year) + ".csv")
    print(quotes)
    # select desired range of dates
    quotes['Date_x'] = quotes['Date'].apply(lambda x: pd.to_datetime(x) - datetime.timedelta(hours=2))
    quotes.index = quotes.Date_x

    mask_1 = (quotes.index >= start_date) & (quotes.index <= end_date)
    quotes = quotes.loc[mask_1]

    print(quotes)

    quotes['Time'] = quotes[['Date', 'Time']].apply(lambda x: ' '.join(x), axis=1)
    quotes['Time'] = quotes['Time'].apply(lambda x: pd.to_datetime(x) - datetime.timedelta(hours=2))
    quotes.index = quotes.Time

    print(quotes)



    fig, ax = plt.subplots()
    ax.plot(quotes['Close'])
    ax.set_title('Black Regions')
    anormalies = pd.read_csv("results/"+currency+"/all_anomalies.csv")

    anormalies['Time'] = anormalies['DateHour'].apply(lambda x: pd.to_datetime(x))
    anormalies.index = anormalies.Time
    mask_2 = (anormalies.index >= start_date) & (anormalies.index <= end_date)
    anormalies = anormalies.loc[mask_2]
    print("anormalies")
    print(anormalies)
    #xdate = [datetime.datetime.fromtimestamp(i) for i in quotes['Time']]

    for index, row in anormalies.iterrows():
        a_index = row["Time"]
        b_index = row["Time"]+datetime.timedelta(hours=1)
        ax.axvspan(a_index, b_index, color='red', alpha=0.5)

    plt.show()


#https://stackoverflow.com/questions/42373104/candlestick-ochl-graph