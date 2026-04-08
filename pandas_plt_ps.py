import pandas as pd
import kagglehub
import matplotlib.pyplot as plt

# python.exe -m pip install --upgrade pip

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# df["millions*rate"] = df["suicide_rate_per100k"] * df["population_millions"]*10
# print(df[["country", "millions*rate"]])

# df["gdp_geq_40k_low_help"] = df["population_millions"] * (df["treatment_gap_pct"]/100)
# print(df["lack_of_care_mln"])

# gdp_geq_40k = df[df["gdp_per_capita_usd"] >= 40000]
# gdp_geq_40k_low_help = gdp_geq_40k[gdp_geq_40k["mh_system_score"] <5]
# gdp_geq_40k_low_help["lack_of_care_mln"] = (gdp_geq_40k_low_help["population_millions"] *
#                                             (gdp_geq_40k["treatment_gap_pct"]/100))
#
# print(gdp_geq_40k_low_help[["country","mh_system_score","gdp_per_capita_usd","lack_of_care_mln"]])

top_5 = df.nlargest(5, "depression_pct")
print(top_5)

plt.figure(figsize = (8,4))
plt.plot(top_5["country"],top_5["depression_pct"],
         marker='o',label="anxiety" )
plt.plot(top_5["country"],top_5["anxiety_pct"],
         marker='o', label="depression")
plt.title("Anxiety vs Depression (%)")
plt.xlabel("Country")
plt.ylabel("Percents")
plt.legend()
plt.show()