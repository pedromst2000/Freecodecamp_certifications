import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()  # This is used to register the converters for the date and time data types in pandas. It is not necessary in the latest versions of pandas, but it is a good practice to include it for compatibility with older versions.

df = pd.read_csv(
    "../page-view-time-series-visualizer/data/fcc-forum-pageviews.csv",
    parse_dates=["date"],  # This is used to parse the date column in the csv file
    index_col="date",
)
print(df.head())
print(df.dtypes)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]  # Remove the top and bottom 2.5% of the data


def draw_line_plot():

    # Draw line plot
    plt.figure(figsize=(12, 6))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")  # title
    plt.xlabel("Date")  # x-axis label
    plt.ylabel("Page Views")  # y-axis label

    plt.plot(df.index, df["value"], color="red", linewidth=1.5)  # plotting the data

    fig = plt.gcf()  # get current figure its used to save the figure
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_bar = df.copy()  # copy of the original dataframe
    df_bar.reset_index(
        inplace=True
    )  # reset the index of the dataframe and changes in the original dataframe

    # Extracting the year and month from the date column
    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.strftime(
        "%B"
    )  # to format the month as full name like January, February, etc.

    # Ordering the months correctly
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    df_bar["month"] = (
        pd.Categorical(  # the month can be a Categorical variable since it haves unique values
            df_bar["month"], categories=month_order, ordered=True
        )
    )

    # Grouping the data by year and month and calculating the mean / unstacking - this will create a pivot table
    df_grouped = (
        df_bar.groupby(["year", "month"], observed=False)["value"].mean().unstack()
    )  # obsrved=False is used to avoid the warning of the future deprecation of the unstack method

    # custom colors for the bars to represent each month
    custom_colors = [
        "#1F77B4",
        "#FF7F0E",
        "#2CA02C",
        "#D62728",
        "#9467BD",
        "#2A9D8F",
        "#8C564B",
        "#E377C2",
        "#7F7F7F",
        "#BCBD22",
        "#17BECF",
        "#FF8000",
    ]

    df_grouped.plot(
        kind="bar", figsize=(12, 8), color=custom_colors, width=0.7, legend=True
    )

    plt.title("Monthly Average Page Views")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.xticks(rotation=45)
    plt.legend(
        title="Months", bbox_to_anchor=(1.05, 1), loc="upper left"
    )  # legend outside the plot / bbox_to_anchor is used to place the legend outside the plot
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.gca().set_facecolor("#F0F0F0")

    fig = plt.gcf()
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    # Ensure correct month order
    month_order = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    df_box["month"] = pd.Categorical(
        df_box["month"], categories=month_order, ordered=True
    )

    # Define fixed y-axis ticks and labels
    yticks = list(range(0, 220000, 20000))  # 0 to 200000 step 20000
    ytick_labels = [str(y) for y in yticks]

    # Draw box plots
    fig, axes = plt.subplots(ncols=2, figsize=(12, 6))

    # Year-wise box plot
    sns.boxplot(
        ax=axes[0],
        x="year",
        y="value",
        data=df_box,
        hue="year",
        palette="Set2",
        dodge=False,
        legend=False,
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_yticks(yticks)
    axes[0].set_yticklabels(ytick_labels)
    axes[0].grid(axis="y", linestyle="--", alpha=0.7)
    axes[0].set_facecolor("#F0F0F0")
    axes[0].tick_params(axis="x", rotation=45)

    # Month-wise box plot
    sns.boxplot(
        ax=axes[1],
        x="month",
        y="value",
        data=df_box,
        hue="month",
        palette="Set2",
        dodge=False,
        legend=False,
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_yticks(yticks)
    axes[1].set_yticklabels(ytick_labels)
    axes[1].grid(axis="y", linestyle="--", alpha=0.7)
    axes[1].set_facecolor("#F0F0F0")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    fig.savefig("box_plot.png")
    return fig


draw_line_plot()
draw_bar_plot()
draw_box_plot()
