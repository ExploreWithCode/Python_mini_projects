import matplotlib.pyplot as plt
height = [2543130380, 2590270899, 2640278797, 2691979339, 2746072141, 2801002631, 2857866857, 2916108097, 2970292188,
          3019233434, 3068370609, 3126686743, 3195779247, 3267212338, 3337111983, 3406417036, 3475448166, 3546810808,
          3620655275, 3695390336, 3770163092, 3844800885, 3920251504, 3995517077, 4069437231, 4142505882, 4215772490,
          4289657708, 4365582871, 4444007706, 4524627658, 4607984871, 4691884238, 4775836074, 4861730613, 4950063339,
          5040984495, 5132293974, 5223704308, 5316175862, 5406245867, 5492686093, 5577433523, 5660727993, 5743219454,
          5825145298, 5906481261, 5987312480, 6067758458, 6148898975, 6230746982, 6312407360, 6393898365, 6475751478,
          6558176119, 6641416218, 6725948544, 6811597272, 6898305908, 6985603105, 7073125425, 7161697921, 7250593370,
          7339013419, 7426597537, 7513474238, 7599822404, 7683789828, 7764951032, 7840952880, 7909295151, 7975105156,
          8045311447]
tick_label = [1951, '', '', '', 1955, '', '', '', '', 1960, '', '', '', '', 1965, '', '', '', '', 1970, '',
              '',  '', '', 1975, '', '', '', '', 1980, '', '', '', '', 1985, '', '', '', '', 1990, '', '',
              '', '', 1995, '', '', '', '', 2000, '', '', '', '', 2005, '', '', '', '', 2010, '', '', '',
              '', 2015, '', '', '', '', 2020, '', '', 2023]
left = []
num = 0
while num < len(tick_label):
    num += 1
    left.append(num)
# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkslateblue', 'size': 15}
# naming the x-axis
plt.xlabel('Years', fontdict=font2)
# naming the y-axis
plt.ylabel('Population in billions', fontdict=font2)
# plot title
plt.title('World Population', fontdict=font1)
# function to show the plot
plt.show()
'''
years = [1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,
              1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,
              1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,
              2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
'''
