import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("crop_production_eda_clean.csv")
print(df.shape); print(df.info()); print(df.describe())
df.yield_t_ha.hist(bins=18); plt.title("Yield Distribution"); plt.show()
annual=df.groupby(["year","crop"])["production_tonnes"].sum().reset_index()
for crop,g in annual.groupby("crop"): plt.plot(g.year,g.production_tonnes,marker="o",label=crop)
plt.legend(); plt.show()
for crop,g in df.groupby("crop"): plt.scatter(g.area_ha,g.production_tonnes,label=crop)
plt.xlabel("Area (ha)"); plt.ylabel("Production (tonnes)"); plt.legend(); plt.show()
print(df[["area_ha","production_tonnes","yield_t_ha"]].corr())
