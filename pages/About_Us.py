import streamlit as st

st.title("About Us")

st.write("""
## Inspiration
In the whirlwind of college life and the societal pressures from platforms like social media, there's an underlying dream for 
         many to understand and master the stock market. However, tales of fortunes lost serve as cautionary tales. Inspired by 
         our university's motto of Ut Prosim, we decided to serve our community by taking on this challenge. Understanding the 
         need and thirst for financial literacy among students like us, coupled with the awareness of the intimidating nature of 
         the stock world, we envisioned and brought to life **"Stonks"** - a comprehensive and user-friendly Stock Market Simulator 
         designed to bridge knowledge gaps without the real-world financial risks. What makes us unique is our ease of use and 
         that we provide all features needed to trade stocks in a single platform.
""")

#st.image("https://path_to_your_image.com/our_team_image.jpg", caption="Our Awesome Team")

st.write("""
    ## How we built it
    The foundation of Stonks lies in **Python**. The interactive frontend is crafted with **Streamlit**, seamlessly presenting 
         data to users. A standout feature, the ability to search for stocks and retrieve their real-time values, is powered by 
         **Beautiful Soup** which scrapes data directly from **Google Finance**. **Auth0** underpins our login system, ensuring 
         personalized experiences by guarding individual portfolios. Our backend server, built on **MongoDB**, powers data storage 
         and processing, tying the different elements together into a cohesive application.
    """)

#st.image("https://path_to_your_image.com/our_journey_image.jpg", caption="The Journey So Far")

st.write("""
    ## An accomplishment we're proud of
    Our journey from concept to a functioning prototype, filled with countless hurdles, is our collective achievement. Grasping new 
         tech stacks, resolving unexpected bugs, and ultimately creating a platform that resonates with our vision are feats we hold 
         close.
         """)

#st.image("https://path_to_your_image.com/our_vision_image.jpg", caption="Our Vision for the Future")

st.write("""
    Thank you for visiting our About Us page. For more information or to get in touch, please visit our Contact page.
    """)