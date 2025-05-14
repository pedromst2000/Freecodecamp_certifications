import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("../sea-level-predictor/data/epa-sea-level.csv")
    print(df.head())

    # Create scatter plot
    plt.scatter(
        x=df["Year"],
        y=df["CSIRO Adjusted Sea Level"],
        color="blue",
        label="Data Points",
        s=5,
    )

    # Create first line of best fit
    slope, intercept = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])[
        :2
    ]  # slice to get slope and intercept because linregress returns a tuple
    years_extended = pd.Series(
        range(1880, 2051)
    )  # create a series of years from 1880 to 2050
    plt.plot(
        years_extended,
        slope * years_extended + intercept,
        color="red",
        label="Best Fit Line 1",
    )  # plot the line of best fit
    print(
        f"slope: {slope}, intercept: {intercept}"
    )  # print slope and intercept for debugging

    # Create second line of best fit
    df_recent = df[
        df["Year"] >= 2000
    ]  # filter the dataframe to only include years from 2000 onwards
    slope_recent, intercept_recent = linregress(
        x=df_recent["Year"], y=df_recent["CSIRO Adjusted Sea Level"]
    )[
        :2
    ]  # get slope and intercept for the recent yearss
    print(
        f"slope: {slope_recent}, intercept: {intercept_recent}"
    )  # print slope and intercept for debugging

    years_recent = pd.Series(range(2000, 2051))
    plt.plot(
        years_recent,
        slope_recent * years_recent + intercept_recent,
        color="green",
        label="Best Fit Line 2",
    )  # plot the line of best fit for recent years
    print(
        f"slope: {slope_recent}, intercept: {intercept_recent}"
    )  # print slope and intercept for debugging

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()


draw_plot()
