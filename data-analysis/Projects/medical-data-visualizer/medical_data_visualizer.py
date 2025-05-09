import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("../medical-data-visualizer/data/medical_examination.csv")
print(df.head())  # debugging line to check the data loaded

# 2
df["overweight"] = df["weight"] / ((df["height"] / 100) ** 2)  # calculating the BMI

print(df.head())  # debugging line to check the overweight column added

df["overweight"] = df["overweight"].apply(
    lambda x: 1 if x > 25 else 0
)  # creating the overweight column based on the BMI

print(df.head())  # debugging line to check the overweight column added

# 3
df["cholesterol"] = df["cholesterol"].apply(
    lambda x: 1 if x > 1 else 0
)  # creating the cholesterol column based on the cholesterol level

df["gluc"] = df["gluc"].apply(
    lambda x: 1 if x > 1 else 0
)  # creating the gluc column based on the glucose level


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )

    # 6
    df_cat["total"] = (
        1  # creating a new column to count the occurrences of each category
    )

    df_cat = df_cat.groupby(
        ["cardio", "variable", "value"], as_index=False # as_index=False is used to avoid setting the index to the groupby columns because we want to keep the original DataFrame structure
    ).count()  # grouping the data by cardio, variable, and value to count the occurrences

    # 7
    fig = sns.catplot(
        x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar"
    )  # creating the catplot with the grouped data in long format to show value counts of categorical features

    # 8
    fig = fig.figure

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (
            df["ap_lo"] <= df["ap_hi"]
        )  # Ensure diastolic pressure is not greater than systolic
        & (
            df["height"] >= df["height"].quantile(0.025)
        )  # Remove outliers below 2.5th height percentile
        & (
            df["height"] <= df["height"].quantile(0.975)
        )  # Remove outliers above 97.5th height percentile
        & (
            df["weight"] >= df["weight"].quantile(0.025)
        )  # Remove outliers below 2.5th weight percentile
        & (
            df["weight"] <= df["weight"].quantile(0.975)
        )  # Remove outliers above 97.5th weight percentile
    ]  # Filtering the data to clean incorrect or extreme values

    print(
        f"df_heat: {df_heat.head()}"
    )  # debugging line to check the data after filtering

    # 12
    corr = df_heat.corr()  # calculating the correlation matrix

    # 13
    mask = np.triu(
        np.ones_like(corr, dtype=bool)
    )  # creating a mask for the upper triangle of the correlation matrix
    # np.triu is used to create a triangular mask for the upper triangle of the correlation matrix
    # 14
    fig, ax = plt.subplots(
        figsize=(12, 12)
    )  # creating a figure and axis for the heatmap

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,  # adding annotations to the heatmap
        fmt=".1f",  # formatting the annotations to one decimal place
        cmap="coolwarm",
        cbar_kws={"shrink": 0.8},  # shrinking the color bar to fit the figure
        square=True,  # making the heatmap square
        linewidths=0.5,
        linecolor="black",
    )  # creating the heatmap with the correlation matrix and the mask

    # 16
    fig.savefig("heatmap.png")  # saving the heatmap figure
    return fig  # returning the figure


draw_cat_plot()  # calling the draw_cat_plot function to create the catplot
draw_heat_map()  # calling the draw_heat_map function to create the heatmap
