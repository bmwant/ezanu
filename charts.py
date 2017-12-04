import pandas as pd
import plotly

from plotly.graph_objs import Scatter, Layout

import config


DATASET_FILENAME = 'message_history.csv'


def messages_count_per_day(df):
    df.date = pd.DatetimeIndex(df.date).normalize()

    # Remove rows without message
    df = df[pd.notnull(df.message)]

    # Filter by user
    in_messages = df[df.to_id == config.CURRENT_USER_ID]
    out_messages = df[df.from_id == config.CURRENT_USER_ID]

    # Group by day
    in_messages = in_messages.groupby(in_messages.date).count()
    out_messages = out_messages.groupby(out_messages.date).count()

    # Reset datetime index to column
    in_messages.reset_index(inplace=True)
    out_messages.reset_index(inplace=True)

    data = [
        Scatter(x=in_messages.date, y=in_messages.message, mode='lines', name='in'),
        Scatter(x=out_messages.date, y=out_messages.message, mode='lines', name='out')
    ]

    plotly.offline.plot(data, show_link=False, auto_open=False,
                        filename='plots/messages_per_day.html')


def build_chart():
    df = pd.read_csv(DATASET_FILENAME)

    data = [Scatter(
              x=df.date,
              y=df.id)]

    plotly.offline.plot(data)


def main():
    """
        * Messages per day ✔
        * Characters per day
        * Messages per month
        * Characters per month
        * Edits per month
        * Media per month
    """
    df = pd.read_csv(DATASET_FILENAME)
    messages_count_per_day(df)


if __name__ == '__main__':
    main()

