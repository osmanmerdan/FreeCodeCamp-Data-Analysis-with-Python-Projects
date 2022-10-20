import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
               index_col='date',
               parse_dates=True)

# Clean data
df =df.loc[
    (df['value'] >= df['value'].quantile(0.025))
    &
    (df['value'] <= df['value'].quantile(0.975))
    ]


def draw_line_plot():
    fig=plt.figure(figsize=(16,5))
    plt.plot(df)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot.
    # First reset the index of df.
    # Resetting index wont change date data type. 
    # Then group it by year and month.
    # Finally do the necessary math and save it as temp_series. 
    
    temp_df= df.reset_index()
    temp_series= temp_df.groupby(
        by=[
        temp_df['date'].dt.year,
        temp_df['date'].dt.month
        ]
    )['value'].mean().round().astype('int32')
    # Change the index names-labels in temp_series.
    # In the next step we will convert theese names to col names. 
    temp_series.index.names=['Years','Month']
    # Resetting indexes will turn the series to data-frame.
    # The values in the series will be --> 
    # represented under column name 'Average Page Views'
    df_bar = temp_series.reset_index(name='Average Page Views')
    # To create bar chart our x axis value must be categories. 
    df_bar['Years']=df_bar['Years'].astype('category')
    df_bar['Month']=df_bar['Month'].astype('category')
    # Draw bar plot
    fig, axis = plt.subplots(figsize=(8,8))
    bar=sns.barplot(
        data=df_bar, 
        x='Years', 
        y='Average Page Views',
        hue='Month',
        ax=axis,
        palette='tab10')
    
    handles, labels = bar.get_legend_handles_labels()
    labeles_list= ["January", "February", "March", 
                   "April", "May", "June", "July", 
                   "August", "September", "October",
                   "November", "December"]
    bar.legend(handles=handles,
               labels=labeles_list,
               loc='upper left', 
               title= 'Months')
    



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    
    
    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(24,8))
    sns.boxplot(data=df_box,
                   x='year',
                   y='value',
                   ax=ax1).set(
    title='Year-wise Box Plot (Trend)',
    ylabel='Page Views',
    xlabel='Year')

    
    sns.boxplot(data=df_box,
                   x='month',
                   y='value',
                   ax=ax2,
                   order=["Jan", "Feb", "Mar",
                          "Apr", "May", "Jun", "Jul", 
                          "Aug", "Sep", "Oct",
                          "Nov", "Dec"]).set(
    title='Month-wise Box Plot (Seasonality)',
    ylabel='Page Views',
    xlabel='Month')
    
  





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
