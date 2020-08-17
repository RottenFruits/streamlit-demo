import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import sys

@st.cache
def read_data(path):
    df = pd.read_csv(path)
    #df = df[df["type"] == 1]
    return df

def add_widget():
    add_filter_data_row_number = st.sidebar.number_input(
        'Select a max number of show data num',
        0, 1000, 100,
        key = "1"
    )
    return add_filter_data_row_number

def main():
    path = sys.argv[1]
    df = read_data(path)
    filter_data_row_number = add_widget()

    """
    # Sample 1: Check data app
    
    ## Data summary
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

    '### Statistics summary:'
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

    '### Histogram:'
    base = alt.Chart().mark_bar().encode().properties(
        width = 150,
        height = 150
    ).interactive()
    h1 = alt.vconcat(data = df_filtered)
    i = 0
    row = alt.hconcat()
    for x_encoding in int_float_columns:
        if i % 4 == 0 and i != 0:
            h1 &= row
            row = alt.hconcat()
        row |= base.encode(x = alt.X(x_encoding, bin = True), y='count()')
        i += 1 
    h1

    '### Bar plot:'
    base2 = alt.Chart().mark_bar().encode().properties(
        width = 150,
        height = 150
    ).interactive()
    b = alt.vconcat(data = df_filtered)
    i = 0
    row = alt.hconcat()
    for x_encoding in category_columns:
        if i % 4 == 0 and i != 0:
            b &= row
            row = alt.hconcat()
        row |= base2.encode(x = x_encoding, y = 'count()')
        i += 1 
    b


    '### Scatter plot:'
    scatter_columns = st.multiselect(
    "Choose columns", list(int_float_columns), [int_float_columns[0], int_float_columns[1]]
    )
    if len(scatter_columns) != 2:
        st.error("Please select two columns.")
        return
    
    p1 = alt.Chart(df_filtered).mark_circle().encode(
        x = scatter_columns[0], y = scatter_columns[1]
    )
    p1

main()