# %% [markdown]
# ## Data science tools and ecosystem

# %% [markdown]
# In this notebook, Data Science Tools and Ecosystem are summarized.

# %% [markdown]
# Some of the popular languages that Data Scientists use are:
# 1. sql
# 2. python
# 3. R
# 4. Matlab

# %% [markdown]
# Some of the commonly used libraries used by Data Scientists include:

# %%
program = ['python','sql','java','c','c++','javascript']
program

# %% [markdown]
# **Objectives:**
#   
# - Identify commonly used tools in Data Science workflows  
# - Create and edit cells in a Jupyter Notebook  
# - Understand the role of GitHub for sharing and collaborating on code  
# - Demonstrate basic Python code and markdown formatting

# %% [markdown]
# Some of the commonly used libraries used by Data Scientists include:

# %%
library = ['numpy','pandas','matplotlib','scikit-learn','tensorflow']
library

# %%
import pandas as pd

table = pd.DataFrame(program, columns=['Data Science Tools'])
table

# %% [markdown]
# ### Below are a few examples of evaluating arithmetic expressions in Python.

# %% [markdown]
# 1. $+$
# 2. $-$ 
# 3. $*$
# 4. $/$
# 5. $//$
# 6. %
# 7. $**$

# %%
(3*4)+5
# This a simple arithmetic expression to multiply then add integers

# %%
def min_to_hour(minutes):
    return minutes / 60
# This will convert 200 minutes to hours by diving by 60.

round(min_to_hour(200),2)

# %% [markdown]
# ## Author
# Pongthanat Buranachon


