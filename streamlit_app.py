import pandas as pd
import streamlit as st


df = pd.read_csv('QueryResults.csv', names=['Date', 'Tag', 'Posts'], header = 0)

st.title("Stackoverflow Posts by Tag")

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

# tag_slider returns an int value equal to whatever the user sets it to.
# this can be used to filter the dataframe.
tag_slider = st.slider(
    "Filter post counts less than: ",
    min_value = 0,
    max_value = 5000,
    step = 100
    )
language_choices = df['Tag'].unique().tolist()

languages = st.multiselect(
    'Select one or more languages:',
    language_choices,
    key= "Tag"
    )

# create a filtered dataframe using the filters defined above.
filt = (df['Posts'] > tag_slider) & (df['Tag'].isin(languages))

select_col = ['Date','Tag', 'Posts']

filtered_df = df.loc[filt, select_col]


st.dataframe(filtered_df, use_container_width=st.session_state.use_container_width)