# entry_exit_strategies.py

def determine_entry_exit(data):
    entry_signals = data[data['Signal'] == 1].copy()
    exit_signals = data[data['Signal'] == -1].copy()
    return entry_signals, exit_signals
