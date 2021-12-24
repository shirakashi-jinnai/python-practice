from importlib.resources import is_resource
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import tkinter

df = datasets.load_iris(as_frame=True).frame
# print(df)

# トイボックスデータ
# iris = datasets.load_iris()

# iris_df = pd.DataFrame(iris.data,columns=iris.feature_names)
# iris_df['MEDV']=iris.target


wine = datasets.load_wine()
wine_df = pd.DataFrame(wine.data,columns=wine.feature_names)
arg = np.arange(len(wine_df))

wine_plt_Y= wine_df.loc[:,'alcohol']
wine_plt_Y2= wine_df.loc[:,'malic_acid']



plt.plot(arg,wine_plt_Y)
plt.plot(arg,wine_plt_Y2)
plt.show()