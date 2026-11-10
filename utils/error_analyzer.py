import pandas as pd
import os
from typing import Dict, List
from utils.instance_reader import load_optimal_solutions_from_excel
from utils.common import classify_instance_type, INSTANCE_TYPES, ALGO_COLS


def add_error_columns(df, algo_cols, optimal_dict: Dict[str, int]):
    for col in algo_cols:
        errors = []
        for _, row in df.iterrows():
            best = optimal_dict[row['instance']]
            error = (row[col] - best) / best * 100
            errors.append(round(error, 2))
        df[f'{col}_error'] = errors
    return df


def compute_summary_statistics(df, algo_cols):
    df['instance_type'] = df['instance'].apply(classify_instance_type)

    summary = []
    for typ in INSTANCE_TYPES:
        subset = df[df['instance_type'] == typ]
        if len(subset) == 0:
            continue
        row = {'instance_type': typ, 'count': len(subset)}
        for col in algo_cols:
            row[f'{col}_error_mean'] = subset[f'{col}_error'].mean()
        summary.append(row)

    return pd.DataFrame(summary)


def generate_paper_table(summary_df, algo_cols):
    lines = [
        "| Instance Type | Count | FF | BF | WF | FFD | BFD | WFD | WFD(m) |"
    ]
    for _, row in summary_df.iterrows():
        values = [f"{row[f'{col}_error_mean']:.1f}%" for col in algo_cols]
        lines.append(f"| {row['instance_type']} | {int(row['count'])} | " + " | ".join(values) + " |")
    return "\n".join(lines)


def run_error_analysis(input_csv, solutions_excel_path, output_csv=None):
    df = pd.read_csv(input_csv)
    algo_cols = ALGO_COLS

    optimal_dict = load_optimal_solutions_from_excel(solutions_excel_path)
    print(f"Loaded {len(optimal_dict)} optimal solutions from BPPLIB")

    df = add_error_columns(df, algo_cols, optimal_dict)

    if output_csv is None:
        output_csv = input_csv.replace('.csv', '_with_error.csv')
    df.to_csv(output_csv, index=False)
    print(f"Saved: {output_csv}")

    summary_df = compute_summary_statistics(df, algo_cols)

    print("Average Relative Error by Instance Type (%)")
    for _, row in summary_df.iterrows():
        print(f"\n【{row['instance_type']}】 ({int(row['count'])} instances)")
        for col in algo_cols:
            print(f"  {col}: {row[f'{col}_error_mean']:.2f}%")

    print("Paper Table")
    print(generate_paper_table(summary_df, algo_cols))

    return df, summary_df

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "experiment_results.csv")
    excel_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(csv_path))),
                              "BPPLIB-main", "Instances", "Solutions", "Solutions.xlsx")

    run_error_analysis(input_csv=csv_path, solutions_excel_path=excel_path)