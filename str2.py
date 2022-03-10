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
