import streamlit as st
import numpy as np
import pandas as pd


st.title('はじめてのStreamlit')
st.write('本文を追加')

st.write('DataFrame')
df = pd.DataFrame({
    '1列目':[1,2,3,4,5,6,7],
    '2列目':[10,20,30,40,50,60,70]
}
)

st.write('表',df)
st.dataframe(df.style.highlight_max(axis=1),width=100,height=100)
st.table(df.style.highlight_max(axis=0))

"""

# h1
## h2
### h3

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston

dataset = load_boston()

x,t = dataset.data,dataset.target
colmuns = dataset.feature_names

type(x),x.shape
```

"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df3)

from PIL import Image

img = Image.open('だいち.png')
st.image(img,caption='ＮＴＴＤＡＴＡだいち',use_column_width=True)
if st.checkbox('表示'):
    img = Image.open('だいち.png')
    st.image(img,caption='ＮＴＴＤＡＴＡだいち',use_column_width=True)

sbx = st.selectbox(
    '好きな数字を選んでください',list(range(1,11))
)
'選んだ数字は',sbx,'です。'

tbx = st.text_input(
    'あなたの趣味を教えてください。')
'あなたの趣味：',tbx

cbx = st.slider(
    '今日の体調を教えてください。',0,100,50)
'今日の体調：',cbx
