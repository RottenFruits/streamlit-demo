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

def add_widget():
    add_filter_data_row_number = st.sidebar.number_input(
        'Select a max number of show data num',
        0, 10000, 10000,
        key = "1"
    )
    return add_filter_data_row_number


def add_bar_histogram(df, columns, bin):
    num_columns = len(columns)
    plot_cols = math.ceil(num_columns / 10)
    base = alt.Chart().mark_bar().encode().properties(
        width = 300 / plot_cols,
        height = 300 / plot_cols
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
    scatter_columns = st.multiselect(
    "Choose columns", list(columns), [columns[0], columns[1]]
    )
    if len(scatter_columns) != 2:
        st.error("Please select two columns.")
        return
    plot = alt.Chart(df).mark_circle().encode(
        x = scatter_columns[0], y = scatter_columns[1]
        ).interactive()
    return(plot)

def main():
    path = sys.argv[1]
    df = read_data(path)
    filter_data_row_number = add_widget()

    """
    # Sample 1: Check data app
    
    ## Summary
    """

    '### Data shape:'
    df_shape = df.shape
    'row:', df_shape[0]
    'col:', df_shape[1]

    '### Data table:'
    df_filtered = df.head(filter_data_row_number)
    df_filtered

    '### Data type:'
    df_types = df.dtypes
    df_types

    '### Statistics:'
    print_data_describe  = df.describe()
    print_data_describe

    '### Nan count:'
    df_nan_count = df.isnull().sum()
    df_nan_count

    """
    ## Plot

    Plot uses only filtered data. 
    """
    columns = df.columns
    int_float_columns = columns[(df_types == "int64") | (df_types == "float64")]
    category_columns = columns[~((df_types == "int64") | (df_types == "float64"))]

    # histogram
    if len(int_float_columns) > 0:
        '### Histogram:'
        h = add_bar_histogram(df_filtered, int_float_columns, bin = True)
        h

    # bar
    if len(category_columns) > 0:
        '### Bar plot:'
        b = add_bar_histogram(df_filtered, category_columns, bin = False)
        b

    # scatter plot
    if len(int_float_columns) > 2:
        '### Scatter plot:'
        p = add_scatter_plot(df_filtered, int_float_columns)
        p

main()