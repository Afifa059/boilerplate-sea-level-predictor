import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)
   
    # Create first line of best fit
    res = linregress(x, y)
    years_extended=np.arange(1880,2050,1)
    line_1 = [res.slope*xi + res.intercept for xi in years_extended]
    plt.plot(years_extended, line_1, color = 'orange', label="Fitting Line", linewidth=1)
    

    # Create second line of best fit
    years_extended_2010=np.arange(2010,2050,1)
    res_2 = linregress(x.iloc[130:-1], y.iloc[130:-1])
    line_2 = [res_2.slope*xi + res_2.intercept for xi in years_extended_2010]
    plt.plot(years_extended_2010, line_2, color = 'red', label="Fitting Line", linewidth=1)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
