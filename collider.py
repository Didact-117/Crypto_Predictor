import pandas as pd
import numpy as np

def create_date(df):#creates a new column in the data frame for the date
    new_col = []
    for i in range(len(df)):
        new_col.append(df['time'][i][:df['time'][i].index("T")])
    df['Day'] = new_col
    return df
def split_news(df,coin_type):#this looks inside news data and only grab based on coin types and will look based on date published and polarity of description
    df_new = df[df['Type'] == coin_type][['DatePublished', 'Polarity_of_Desc']]
    return df_new
def merger(df_left,df_right):# merges bitcoin historical price data with news associated with bitcoin 
    df_merged = pd.merge(df_left, df_right, how = 'left', left_on='Day',right_on='DatePublished').drop(columns = 'DatePublished')
    df_merged.replace('', np.nan, inplace=True)
    df_merged['Polarity_of_Desc'].replace(np.nan,"0", inplace = True)
    return df_merged

def merge_news_with_df(csv_path='csv/processed/processed_cleaned_daily_BTC.csv'):# this saves it to a csv --> last 2 lines create df and dump in csv 
    df = pd.read_csv(csv_path)
    df_BTC = create_date(df)
    df_news = pd.read_csv('csv/news_gb_days.csv')
    df_news_BTC = split_news(df_news,'Bitcoin')
    news_and_BTC = merger(df_BTC,df_news_BTC)
    news_and_BTC.to_csv('csv/processed/BTC_with_news_daily.csv', index=False)

merge_news_with_df()