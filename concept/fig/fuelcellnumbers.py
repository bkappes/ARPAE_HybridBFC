import numpy as np
from matplotlib import pyplot as plt


# year, "hydrogen fuel cell", "direct methanol alcohol fuel cell"
number_publications = np.array((
            (2005, 22400, 4610),
            (2006, 26200, 5640),
            (2007, 28300, 6110),
            (2008, 31400, 7110),
            (2009, 34100, 7620),
            (2010, 39000, 8250),
            (2011, 41600, 11200),
            (2012, 43700, 10300),
            (2013, 43500, 11500),
            (2014, 36900, 11600),
            (2015, 8150, 1550)
        ))

x = number_publications[:,0]
w0 = number_publications[:,1]
w1 = number_publications[:,2]

plt.rc('font', family='serif')
plt.rc('text', usetex=True)
fig,ax = plt.subplots()
width = 0.35

rects0 = ax.bar(x-width, w0, width, color='b', label='hydrogen')
rects1 = ax.bar(x, w1, width, color='r', label='alcohol')

ax.set_xlabel('Year')
ax.set_ylabel('No. publications')

ax.legend(loc='upper left', frameon=False)

plt.savefig('publication_count.pdf')
plt.show()

