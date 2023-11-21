# entry_exit_strategies.py

def determine_entry_exit(data, trend):
    # Assume trend is based on the last signal in the 'Signal' column
    entry_point = data['Signal'].iloc[-1] == 1
    exit_point = data['Signal'].iloc[-1] == -1

    return entry_point, exit_point
