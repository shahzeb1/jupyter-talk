
# coding: utf-8

# # Demo
#
# In this notebook we'll create a basic plot.

# In[13]:


# Preamble:
import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt


# ## Part 1. Defining the data.
#
# We'll first define the data we're working with.

# In[14]:


# Global Vars:
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]


# ## Part 2. Make the plot.
#
# Now that the data is defined, let's go ahead and create the plot.

# In[15]:


def make_plot():
    '''
    Make the plot of the programming languages
    '''
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.savefig('output/languages.png')


# In[16]:


make_plot()

