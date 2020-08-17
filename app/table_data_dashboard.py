import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import math
import sys

@st.cache
def read_data(path):
    df = pd.read_csv(path)
    return df

def add_summary(df, filter_data_row_number):
    df_shape = df.shape
    '### Data shape:'
    'row:', df_shape[0], 'col:', df_shape[1]

    '### Data table:'
    df_filtered = df.head(filter_data_row_number)
    df_filtered

    '### Data type:'
    df_types = df.dtypes
    df_types

    '### Statistics:'
    df_describe  = df.describe()
    df_describe

    '### Nan count:'
    df_nan_count = df.isnull().sum()
    df_nan_count
    return(df_filtered)

def add_widget(df):
    numberof_using_data = st.sidebar.number_input(
        'Select number of using data.',
        0, 10000, 10000,
        key = "1"
    )
    selected_columns = st.sidebar.multiselect(
    "Choose columns.", list(df.columns), list(df.columns)
    )
    return numberof_using_data, selected_columns

def add_bar_histogram(df, columns, bin):
    num_columns = len(columns)
    plot_cols = math.ceil(num_columns / 4)
    base = alt.Chart().mark_bar().encode().properties(
        width = 450 / plot_cols,
        height = 450 / plot_cols
    ).interactive()
    plot = alt.vconcat(data = df)
    i = 0
    row = alt.hconcat()
    for x_encoding in columns:
        if i % plot_cols == 0 and i != 0:
            plot &= row
            row = alt.hconcat()
        if bin:
            row |= base.encode(x = alt.X(x_encoding, bin = True), y = alt.Y('count()'))
        else:
            row |= base.encode(x = x_encoding, y='count()')
        if plot_cols == 1:
            plot &= row
        i += 1
    return(plot)

def add_scatter_plot(df, columns):
    plot = alt.Chart(df).mark_circle().encode(
        alt.X(alt.repeat("column"), type = 'quantitative'),
        alt.Y(alt.repeat("row"), type = 'quantitative')
    ).properties(
        width = 600 / len(columns),
        height = 600 / len(columns)
    ).repeat(
        column = list(columns),
        row = list(columns)
    )
    return(plot)

def add_plot(df):
    df_types = df.dtypes
    columns = df.columns
    int_float_columns = columns[(df_types == "int64") | (df_types == "float64")]
    category_columns = columns[~((df_types == "int64") | (df_types == "float64"))]
    # histogram
    if len(int_float_columns) > 0:
        '### Histogram:'
        h = add_bar_histogram(df, int_float_columns, bin = True)
        h
    # bar
    if len(category_columns) > 0:
        '### Bar plot:'
        b = add_bar_histogram(df, category_columns, bin = False)
        b
    # scatter plot
    if len(int_float_columns) > 2:
        '### Scatter plot:'
        p = add_scatter_plot(df, int_float_columns)
        p

def create_dashboard():
    path = sys.argv[1]
    df = read_data(path)
    numberof_using_data, selected_columns = add_widget(df)
    df = df[selected_columns]

    """
    # Table Data Dashboard    
    """

    """
    ## Summary
    """
    df_filtered = add_summary(df, numberof_using_data)

    """
    ## Plot

    Plot uses only filtered data. 
    """
    add_plot(df_filtered)

if __name__ == "__main__":
    create_dashboard()