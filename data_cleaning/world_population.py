import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


df = pd.read_csv("data_cleaning/world_population_data.csv")

df = df.drop_duplicates()

print(df)