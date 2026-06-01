import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = range(df['Year'].min(), 2051)
    ax.plot(years_all,
            [res.slope * x + res.intercept for x in years_all],
            'r', label='Best fit: 1880-2050')
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    ax.plot(years_recent,
            [res_recent.slope * x + res_recent.intercept for x in years_recent],
            'green', label='Best fit: 2000-2050')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()