import streamlit as st
st.title('This is a title')
# Header
st.header('This is a header')
#Subheader
st.subheader('This is a subheader')
#Text
st.text('This is a text')
# Latex widget example
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# to display pandas dataframe object
import pandas as pd
import numpy as np

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  
# Example of line chart
import pandas as pd
import numpy as np
import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

import numpy as np
import numpy as np
import plotly.figure_factory as ff
import streamlit as st

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

# radio widget to take inputs from mulitple options
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
# Usage of multiselect widget
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue','Pink','Purple','Grey','Navy Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)
from PIL import Image
image = Image.open('sunrisemountain.jpg')
st.image("sunrisemountain.jpg", caption="Sunrise and Mountain")
