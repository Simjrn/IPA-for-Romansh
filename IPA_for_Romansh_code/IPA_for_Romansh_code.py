import streamlit as st

word = st.text_input("Write your word here")
finished = []
while True:
  letter = word[0]
for index in range(len(word)):
  if letter == "c":
    if word[1] == "e" or "i":
      finished.append('ts')
      word = word[1:]
    else:
      finish.append('k')
      word = word[1:]
  elif letter == "j":
    finished.append('y')
    word = word[j:]
  elif letter == "a":
    if word[1] == "u":
      finished.append('a')
      finished.append('o')
      word = word[1:]
      word = word[1:]
  elif letter == "t":
    if word[1] == "g":
      finished.append('c')
      finished.append('i')
      word = word[1:]
      word = word[1:]
    else:
      finished.append('t')
      word = word[1:]
  else:
    finished.append(letter)
    word = word[1:]
result = "".join(finished)
st.subheader(result)
