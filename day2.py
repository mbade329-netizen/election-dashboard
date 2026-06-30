import streamlit as st
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Election Dashboard",
    page_icon="🗳️",
    layout="wide"
)

# Header
st.title("🗳️ Election Result Dashboard")
st.markdown("### 📊 Real-Time Political Data Analytics")

# Data
parties = ["Party A", "Party B", "Party C", "Party D"]
votes = [120, 95, 75, 40]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("🏛 Total Parties", len(parties))
col2.metric("🗳 Total Votes", sum(votes))
col3.metric("🏆 Leading Party", parties[votes.index(max(votes))])

st.divider()

# Chart
fig, ax = plt.subplots(figsize=(9,5))

bars = ax.bar(
    parties,
    votes,
    color=["#1E88E5","#43A047","#FB8C00","#E53935"]
)

ax.set_title("Election Result Analysis", fontsize=16)
ax.set_xlabel("Political Parties")
ax.set_ylabel("Votes")

for bar in bars:
    y = bar.get_height()
    ax.text(
        bar.get_x()+bar.get_width()/2,
        y+2,
        int(y),
        ha="center"
    )

st.pyplot(fig) 