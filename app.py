import streamlit as st

# Set page configuration
st.set_page_config(page_title="Mad Libs Game", page_icon="🌸")

# User Input
st.title("🎉🌟  Mad Libs Game! 🕹️🎮✨")
st.header("🌟 Create Your Own Story Masterpiece! 🖋️")

name = st.text_input("Enter Your name: ")
city = st.selectbox("Choose a City:", ["Karachi", "Lahore", "Islamabad", "Peshawar"])
programming_language = st.selectbox("Choose a programming language:", ["Python", "JavaScript", "C++", "TypeScript"])
mentor = st.text_input("Enter the mentor's name:")
location = st.selectbox("Choose a location:", ["GIAIC", "PIAIC"])

# Display the story when all inputs are filled
if name and mentor:
    st.header("🌟✨ Here’s Your Magical Story! ✨🌟 \n")
    st.write(f"""
    \n🌆 Once upon a time, in {city}, there lived **{name}** 🧚.\n
    \n✨ {name} was very curious and always wanted to learn new things 📚.\n
    \n💻 One day, {name} decided to learn **{programming_language}** language at **{location}** 🎓!\n
    \n🎓 Luckily, {name} met **{mentor}**, who was an expert in **{programming_language}** 🌟.\n
    \n🚀 With hard work and dedication, One day {name} became a professional {programming_language} developer InshaAllah 🌸.\n
    """)

# Add some fun effects
st.balloons()
