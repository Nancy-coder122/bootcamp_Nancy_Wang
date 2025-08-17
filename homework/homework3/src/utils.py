def get_summary_stats(df):
    return df.groupby("category")["value"].mean().reset_index()