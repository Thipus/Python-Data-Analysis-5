import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv',parse_dates=True)


    # Create scatter plot
    df_x=df['Year']
    #df_x=df_x.append(pd.Series([2050]),ignore_index=True)
    df_x=np.arange(1880,2051,1)
    plt.scatter(data=df,x='Year',y='CSIRO Adjusted Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    result=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    plt.plot(df_x,result.intercept+result.slope*df_x,'r')

    # Create second line of best fit
    df_2000=df[df['Year']>=2000]
    result2=linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])
    df_2000_x=df_2000['Year']
    #df_2000_x=df_2000_x.append(pd.Series([2050]),ignore_index=True)
    df_2000_x=np.arange(2000,2051,1)

    plt.plot(df_2000_x,result2.intercept+result2.slope*df_2000_x,'b')
    # Add labels and title
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()