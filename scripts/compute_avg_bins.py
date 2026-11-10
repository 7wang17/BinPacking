import pandas as pd
from utils.common import classify_instance_type, INSTANCE_TYPES, ALGO_COLS

df = pd.read_csv("../experiment_results.csv")

df['type'] = df['instance'].apply(classify_instance_type)


algo_cols = ALGO_COLS
opt_col = 'optimal'
lb_col = 'lower_bound'


for typ in INSTANCE_TYPES:
    subset = df[df['type'] == typ]
    if len(subset) == 0:
        continue

    if subset[opt_col].notna().any():
        avg_opt = subset[opt_col].mean()
        opt_source = 'optimal'
    else:
        avg_opt = subset[lb_col].mean()
        opt_source = 'lower_bound'

    print(f"\n【{typ}】 ({len(subset)} instances)")
    print(f"  Average optimal solution: {avg_opt:.1f}")
    for col in algo_cols:
        avg = subset[col].mean()
        print(f"  {col}: {avg:.1f}")