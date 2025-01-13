from annual_analysis import Annual_df
from tqdm.notebook import tqdm
import pymannkendall as mk
import pandas as pd
import numpy as np

def row_Mann_Kendall(row : object):
    sub_group, data = row[:-5], row[-5:] # 마지막 5개 칼럼이 5개년 데이터이므로 마지막만 선택

    # perform Mann_Kendall Test
    trend, trend_exists, p_value, z_value, tau, s, var, slope, intercept= tuple(mk.original_test(data))
     
    return pd.Series([trend, trend_exists, p_value, z_value])

def Mann_Kendall(df : object):
    df_MK = df.iloc[:, :-5] # 마지막 5개 칼럼이 5개년 데이터이므로 마지막만 선택

    tqdm.pandas()
    df_MK[["trend", "trend_exists","p_value", "z_value"]] = df.progress_apply(lambda row : row_Mann_Kendall(row), axis=1)

    return df_MK