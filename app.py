import streamlit as st
import matplotlib.pyplot as plt

st.title("🗳️ Election Dashboard - Day 1")

parties = ['Party A', 'Party B', 'Party C', 'Party D']
votes = [120, 90, 60, 40]

fig, ax = plt.subplots()
ax.bar(parties, votes)

st.pyplot(fig)                                     