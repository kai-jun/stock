import pandas as pd
def streakIdentifier(data, SMA, period, period1):
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['_orig_order'] = range(len(data))
    data = data.sort_values(['Date'], ascending=True, kind='mergesort').reset_index(drop=True)
    data['SMA'] = SMA(data['Close/Last'], period)
    data['SMA1'] = SMA(data['Close/Last'], period1)
    data = data.dropna().reset_index(drop=True)
    data.loc[:, 'Streak'] = 0
    data.loc[:, 'StreakIdx'] = 0
    streak = 0
    streakIdx = 0
    UpToDown = False
    DownToUp = False
    for i in range(1, len(data)):
        if data.at[i, 'SMA'] > data.at[i-1, 'SMA'] or data.at[i, 'SMA1'] > data.at[i-1, 'SMA1']:
            if UpToDown:
                streakIdx = 0
                UpToDown = False
            DownToUp = True
            streak += 1
            streakIdx += 1
        elif data.at[i, 'SMA'] < data.at[i-1, 'SMA'] or data.at[i, 'SMA1'] < data.at[i-1, 'SMA1']:
            if DownToUp:
                streakIdx = 0
                DownToUp = False
            UpToDown = True
            streak -= 1
            streakIdx -= 1
        data.at[i, 'Streak'] = streak
        data.at[i, 'StreakIdx'] = streakIdx
    data = data.sort_values('_orig_order').drop(columns='_orig_order').reset_index(drop=True)   
    return data