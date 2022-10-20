import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file 
    data=pd.read_csv('epa-sea-level.csv')
    data=data[['Year','CSIRO Adjusted Sea Level']]
    data.columns=['Year', 'Sea Level (inches)']
    # Create scatter plot
    plt.scatter(data['Year'],
            data['Sea Level (inches)'],
            c='skyblue',
            s=20,
            alpha=0.5,
            label='Original Data')
    #plt.xlim([data['Year'].min()-10,2070])

    # Create first line of best fit
    regression1=linregress(x=data['Year'],
                          y=data['Sea Level (inches)'])
    n=x=pd.Series(np.arange(1880,2051,1))
    plt.plot(n,
    (regression1.intercept+regression1.slope*n).round(7),
    c='steelblue',
    label='Fitted Line')

    # Create second line of best fit
    regression2=linregress(x=data[data['Year']>=2000]['Year'],
          y=data[data['Year']>=2000]['Sea Level (inches)'])
    x=pd.Series(np.arange(2000,2051,1))
    plt.plot(x,
         (regression2.intercept+regression2.slope*x).round(7),
         c='indianred',
         label='Fitted Line-2')
    #plt.ylim([-1,16])

    # Add labels and title
    plt.grid()
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()