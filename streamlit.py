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

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

tbx = st.sidebar.text_input(
    'あなたの趣味を教えてください。')
'あなたの趣味：',tbx

cbx = st.sidebar.slider(
    '今日の体調を教えてください。',0,100,50)
'今日の体調：',cbx

left_c,right_c = st.columns(2)
push = left_c.button('右カラムに文字を表示')
if push:
    right_c.write('右カラムです。')

ex1 = st.expander('問い合わせ1')
ex1.write('問い合わせ1の回答')
ex2 = st.expander('問い合わせ2')
ex2.write('問い合わせ2の回答')
ex3 = st.expander('問い合わせ3')
ex3.write('問い合わせ3')

import time

saveunit = st.empty()
bar = st.progress(0)

for i in range(100):
    saveunit.text(f'accesing to memory card...{i+1}%')
    bar.progress(i+1)
    time.sleep(0.02)
'Succsess!!'

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
