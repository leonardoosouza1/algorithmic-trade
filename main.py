# main.py

import json
from datetime import datetime, timedelta
from analysis import data_fetch, trend_analysis
from strategies import entry_exit_strategies, risk_management
from utils import logger
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf


def main():
    # Define configuration
    ticker = 'USDJPY=X'  # Replace with your desired currency pair
    start_date = (datetime.now() - timedelta(days=365)
                  ).strftime('%Y-%m-%d')  # One year ago
    end_date = datetime.now().strftime('%Y-%m-%d')

    try:
        # Fetch historical data
        historical_data = data_fetch.fetch_historical_data(
            ticker, start_date, end_date)

        # Analyze trends
        trend_data = trend_analysis.analyze_trend(historical_data)

        # Implement entry and exit strategies for simulated trading
        entry_signals, exit_signals = entry_exit_strategies.determine_entry_exit(
            trend_data)

        # Implement risk management
        position_size = risk_management.calculate_position_size()

        # Log results to the terminal
        logger.log_entry_exit_signals(
            entry_signals, exit_signals, position_size)

        # Plotting the historical data with indicators, entry, and exit signals
        plot_data(trend_data, entry_signals, exit_signals)

        # Save aggregated signals to a JSON file (optional)
        signals_data = {
            "entry_signals": entry_signals.to_dict(orient='records'),
            "exit_signals": exit_signals.to_dict(orient='records'),
            "position_size": position_size,
        }

        with open("signals.json", "w") as json_file:
            # Use default=str for Timestamp objects
            json.dump(signals_data, json_file, indent=4, default=str)

    except Exception as e:
        logger.error(f"Error processing {ticker}: {str(e)}")


def plot_data(data, entry_signals, exit_signals):
    # Convert 'Date' to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)  # Set 'Date' column as the index

    # Create addplot objects
    ma_short_addplot = mpf.make_addplot(
        data['MA_Short'], color='blue', linestyle='--')
    ma_long_addplot = mpf.make_addplot(
        data['MA_Long'], color='orange', linestyle='--')

    # Entry and exit signals
    entry_addplot = mpf.make_addplot(
        entry_signals['Close'],
        scatter=True,
        color='g',
        marker='^',
        markersize=100,
        secondary_y=True,
    )

    exit_addplot = mpf.make_addplot(
        exit_signals['Close'],
        scatter=True,
        color='r',
        marker='v',
        markersize=100,
        secondary_y=True,
    )

    # Candlestick chart
    mpf.plot(
        data,
        type='candle',
        addplot=[ma_short_addplot, ma_long_addplot],
        show_nontrading=True,
        style='yahoo',
        title='Candlestick Chart with Entry and Exit Signals',
        ylabel='Price',
    )

    # Entry and exit signals on a separate axis
    mpf.plot(
        data,
        type='line',
        addplot=[entry_addplot, exit_addplot],
        show_nontrading=True,
        style='yahoo',
        ylabel='Signal',
    )

    plt.show()


if __name__ == "__main__":
    main()
