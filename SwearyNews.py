# %%
import requests
from bs4 import BeautifulSoup
import re
import random
import streamlit as st

# %%
BASE_URL = "https://www.bbc.co.uk/news"
response = requests.get(BASE_URL, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
most_read_div = soup.find("div", {"data-component": "mostRead"})

# %%
# Dictionary: {link_text: full_url}
links = []
for a in most_read_div.find_all("a", href=True):
    text = a.get_text(strip=True)
    href = a["href"]
    full_url = "https://www.bbc.co.uk" + href if href.startswith("/") else href
    links.append({
        "url": full_url,
        "headline": text
    })

print(links)

# %%
swearyadditions = [
    "... what a fucking surprise",
    "... if you even give a shit",
    "... who even cares about this crap",
    "... oh, fucking brilliant",
    "... because the world clearly needed *that*",
    "... as if that’s the biggest fucking problem right now",
    "... cue the collective eye-roll",
    "... just what we fucking needed",
    "... hold the front page, you absolute legends",
    "... because everything’s totally fine otherwise, right?",
    "... cheers for the mental breakdown, BBC",
    "... another day, another steaming pile of news",
    "... thank fuck someone’s keeping score",
    "... as if we weren’t all already exhausted",
    "... a real feel-good headline, that one",
    "... guess we’re doing this bullshit again",
    "... is it too early to start drinking?",
    "... and people wonder why no one trusts the news",
    "... because misery loves a goddamn headline",
    "... add it to the growing list of disasters, why not?",
    "... fuck me, that’s depressing",
    "... is this the Onion or the actual news?",
    "... what a fucking surprise",
    "... if you even give a shit",
    "... who even cares about this crap",
    "... oh, fucking brilliant",
    "... because the world clearly needed *that*",
    "... as if that’s the biggest fucking problem right now",
    "... cue the collective eye-roll",
    "... just what we fucking needed",
    "... hold the front page, you absolute legends",
    "... because everything’s totally fine otherwise, right?",
    "... cheers for the mental breakdown, BBC",
    "... another day, another steaming pile of news",
    "... thank fuck someone’s keeping score",
    "... as if we weren’t all already exhausted",
    "... a real feel-good headline, that one",
    "... guess we’re doing this bullshit again",
    "... is it too early to start drinking?",
    "... and people wonder why no one trusts the news",
    "... because misery loves a goddamn headline",
    "... add it to the growing list of disasters, why not?",
    "... fuck me, that’s depressing",
    "... is this the Onion or the actual news?"
]


# %%
st.title("Sweary News:middle_finger:")

st.success(f"\"Oh look at me, i'm interested in current affairs!\"")

st.markdown("Here's the fucking news:")

st.markdown('''
<style>
a.bbc-link {
    color: #1a0dab;
    text-decoration: none;
    font-weight: 600;
    font-family: Arial, sans-serif;
    cursor: pointer;
    transition: color 0.2s ease-in-out;
}
a.bbc-link:hover, a.bbc-link:focus {
    color: #004080;
    text-decoration: underline;
    outline: none;
}
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 10px 0;
}
</style>
''', unsafe_allow_html=True)

# %%
for i, headline in enumerate(links, start=1):
    swearyheadline = headline["headline"] + random.choice(swearyadditions)
    swearyheadline = (f"{i}. {swearyheadline}")
    url= headline["url"]
    
    link_html = (f"<a href=\"{url}\" target=\"_blank\" class=\"bbc-link\">{swearyheadline}</a><hr>")

    st.markdown(link_html, unsafe_allow_html=True)



