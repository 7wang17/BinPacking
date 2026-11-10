import pandas as pd
from utils.common import BEST_TIME_COLS

df = pd.read_csv('../experiment_results.csv')

def avg_time_for_best(df, prefix, best_cols):
    subset = df[df['instance'].str.startswith(prefix)]
    all_times = []
    for col in best_cols:
        all_times.extend(subset[col].dropna().tolist())
    return sum(all_times) / len(all_times) if all_times else 0

print(f"Triplet classic best time: {avg_time_for_best(df, 'Falkenauer_t', BEST_TIME_COLS):.3f} ms")
print(f"Triplet WFD(m) time: {df[df['instance'].str.startswith('Falkenauer_t')]['wfd_m_time_ms'].mean():.3f} ms")

# Hard28
print(f"Hard28 classic best time: {avg_time_for_best(df, 'Hard28', BEST_TIME_COLS):.3f} ms")
print(f"Hard28 WFD(m) time: {df[df['instance'].str.startswith('Hard28')]['wfd_m_time_ms'].mean():.3f} ms")

# Falkenauer_U
print(f"Falkenauer_U classic best time: {avg_time_for_best(df, 'FU_', BEST_TIME_COLS):.3f} ms")
print(f"Falkenauer_U WFD(m) time: {df[df['instance'].str.startswith('FU_')]['wfd_m_time_ms'].mean():.3f} ms")

# Scholl_1
print(f"Scholl_1 classic best time: {avg_time_for_best(df, 'Scholl1_', BEST_TIME_COLS):.3f} ms")
print(f"Scholl_1 WFD(m) time: {df[df['instance'].str.startswith('Scholl1_')]['wfd_m_time_ms'].mean():.3f} ms")

# Scholl_2
print(f"Scholl_2 classic best time: {avg_time_for_best(df, 'Scholl2_', BEST_TIME_COLS):.3f} ms")
print(f"Scholl_2 WFD(m) time: {df[df['instance'].str.startswith('Scholl2_')]['wfd_m_time_ms'].mean():.3f} ms")

# Wäscher
print(f"Wäscher classic best time: {avg_time_for_best(df, 'Wascher_', BEST_TIME_COLS):.3f} ms")
print(f"Wäscher WFD(m) time: {df[df['instance'].str.startswith('Wascher_')]['wfd_m_time_ms'].mean():.3f} ms")