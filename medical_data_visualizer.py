import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# First calculate the BMI using the formula given. 
# Height is converted to meters. 
# Use boolean operations to find who is overweight.
# Finally with .astype() method change boolean type data to int.  
BMI=(
    (df['weight']/((df['height']/100)**2))>25
).astype('int32')

df['overweight'] = BMI

# ===Normalization===
# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
df[['cholesterol','gluc']]=df[ ['cholesterol','gluc']].replace({1:0})

df['cholesterol'].values[df['cholesterol']>1]=1
df['gluc'].values[df['gluc']>1]=1


# ===Draw Categorical Plot===
def draw_cat_plot():
# Create DataFrame for cat plot using `pd.melt`.
# Using just the values from:
# 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(
        df,
        id_vars='cardio',
        value_vars=[
            'cholesterol',
            'gluc',
            'smoke',
            'alco',
            'active',
            'overweight'
        ]
    )


# === Group and reformat === 
# Split it by 'cardio'.
# Show the counts of each feature. 
# You will have to rename one of the columns for the catplot to work correctly.

# Instead of using pandas.DataFrame.groupby,
# Utilize value_counts which outputs series with multi-level-index.
# Then using series.reset_index(name='columnnname')--> 
# Flatten the multi index series to dataframe. 
# And indexes in the series become-->Individual columns.
# Then order data frame by column variable ---> because;
# Assignment requires the x axis ordered like : active,alco..
# Finally reset index of the data frame, dropping the previous index col. 
    
    df_cat = df_cat.value_counts().reset_index(name='total')
    df_cat = df_cat.sort_values(by='variable').reset_index(drop=True)
    

    # ===Draw the catplot with 'sns.catplot()'===
    plot1=sns.catplot(
        data=df_cat, 
        x="variable", 
        y="total", 
        col="cardio",
        kind="bar", 
        height=6, aspect=1,
        hue='value'
        )



    # Get the figure for the output
    fig = plot1.figure.get_figure()
    #plt.close(fig)


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


#===Draw Heat Map===
def draw_heat_map():
# Clean the data
# Filter out the following patient segments that represent incorrect data:
# diastolic pressure is higher than systolic 
# (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
# height is less than the 2.5th percentile 
# (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
# height is more than the 97.5th percentile
# weight is less than the 2.5th percentile
# weight is more than the 97.5th percentile

    df_heat = df.loc[
    (df['ap_lo'] <= df['ap_hi'])
    &
    (df['height'] >= df['height'].quantile(0.025))
    &
    (df['height'] <= df['height'].quantile(0.975))
    &
    (df['weight'] >= df['weight'].quantile(0.025))
    &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]


# Calculate the correlation matrix
    corr = df_heat.corr()

# Generate a mask for the upper triangle
# To achieve this look up for Seaborn user manual:
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
# 1. Create a zeros array at the same size to corr. 
    mask = np.zeros_like(corr)
# 2. Select the indeces of the upper triangle in the array.
# 3. And fill them with 1(will masked). 
    mask[np.triu_indices_from(mask)] = 1

# Set up the matplotlib figure
    fig,ax = plt.subplots(figsize=(10, 10))

# Draw the heatmap with 'sns.heatmap()'
    plot2=sns.heatmap(data=corr,
            vmin=-0.08,
            center=0,
            vmax=0.24,
            ax=ax,
            annot=True,
            fmt='.1f',
            mask=mask,
            square=True)
    #plt.close()

# Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig