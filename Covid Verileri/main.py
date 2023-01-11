import matplotlib.pyplot as plt
import seaborn as sns
from covid import Covid
import pandas as pd

cvd = Covid()
df = pd.DataFrame(cvd.get_data())
top10 = df.head(10)
print(top10, sep=None)
ulke_ad = top10.country
vaka_sa = top10.confirmed
vefat_sa = top10.deaths
s_plot = sns.barplot(x=ulke_ad, y=vefat_sa, data=top10)
plt.bar_label(s_plot.containers[0])

plt.title("En fazla Covid vakası görülen ülkelerdeki vefat sayıları")
plt.show()