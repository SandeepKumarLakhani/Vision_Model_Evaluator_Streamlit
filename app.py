
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Vision Model Evaluator")

# Simulated data
epochs = list(range(1, 11))
accuracy = [0.6 + i*0.03 for i in range(10)]
loss = [1.0 - i*0.08 for i in range(10)]

df = pd.DataFrame({'Epoch': epochs, 'Accuracy': accuracy, 'Loss': loss})

st.line_chart(df.set_index('Epoch'))

fig = px.bar(df, x="Epoch", y="Accuracy", title="Accuracy per Epoch", color="Accuracy")
st.plotly_chart(fig)
