    
def get_summary_stats(dataframe):
    """
    Returns summary statistics for numeric columns
    and groupby aggregation if 'Category' exists.
    """
    stats = dataframe.describe()
    if "Category" in dataframe.columns:
        group_stats = dataframe.groupby("Category").mean(numeric_only=True)
    else:
        group_stats = None
    return stats, group_stats