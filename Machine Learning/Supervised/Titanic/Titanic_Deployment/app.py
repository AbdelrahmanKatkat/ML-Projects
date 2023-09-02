import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
from joblib import load
import sklearn

TITLE = "Streamlit demonstration"
st.title(TITLE)
DESCRIPTION = "Survivorship analysis from the Titanic Dataset"
st.markdown(DESCRIPTION)
