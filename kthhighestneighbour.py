# 177. Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    try:
        x = employee['salary'].drop_duplicates().nlargest(N).iloc[N-1]
    except IndexError:
        x = None

    column_name = f'getNthHighestSalary({N})'
    df = pd.DataFrame({column_name: [x]})
    return df
