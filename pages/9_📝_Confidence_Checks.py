import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Pre and Post-Bootcamp Confidence Checks',
    page_icon="📚"
)

local_css("css/style.css")

st.markdown(
    """
## 📋 Confidence Checks

These surveys help us assess whether this bootcamp improves your Python skills. Please complete both surveys at the appropriate times.
"""
)

st.divider()

# Pre-bootcamp section
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### 📝")
with col2:
    st.markdown("### Pre-Bootcamp Survey")

st.info("⏰ **Complete this BEFORE the bootcamp starts**")

st.markdown(
    """
Record your current confidence level with the topics and techniques that will be covered in the bootcamp.

[📋 Open Pre-Bootcamp Survey](https://forms.office.com/Pages/DesignPageV2.aspx?subpage=design&FormId=_epnVXfnpUKRu5RA_UO4k3yz2YdvzEJIrB8SYoRSlYlUOEpLV1hPU0Q5WFJGS1Q2Wkg0TTFOMVgwNi4u&Token=2528cf8b897d4544957afbf175cb3020)
"""
)

st.divider()

# Post-bootcamp section
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### ✅")
with col2:
    st.markdown("### Post-Bootcamp Survey")

st.success("⏰ **Complete this AFTER the bootcamp ends**")

st.markdown(
    """
Record your confidence level with the topics and techniques after completing the bootcamp.

[📊 Open Post-Bootcamp Survey](https://forms.office.com/Pages/DesignPageV2.aspx?subpage=design&FormId=_epnVXfnpUKRu5RA_UO4k3yz2YdvzEJIrB8SYoRSlYlUQU9FTjUwMzNBS1hBOUJIWjRYUzM1MEE4WS4u&Token=2b7162eee37c499ea05de24ce5d31a05)
"""
)
st.divider()

# Celebration section
st.markdown("## 🎉 Congratulations!")

st.markdown(
    """
If you've completed the bootcamp and both surveys, you've accomplished something significant! 
You've developed new Python skills, tackled challenging problems, and expanded your data science toolkit.
"""
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎈 Celebrate Your Achievement! 🎈", use_container_width=True):
        st.balloons()
        st.success("🌟 **Well done!** Keep building on what you've learned. The Digital Skills Lab is here to support your continued learning journey.")

st.markdown(
    """
### What's Next?

- 💡 Apply your new skills to your coursework or research projects
- 🔍 Explore more advanced workshops available through the Digital Skills Lab
- 🤝 Connect with fellow bootcamp participants to continue learning together
"""
)