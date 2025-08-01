import streamlit as st

word = st.text_input("Write your word here")
finished = []
while True:
  letter = word[0]
for index in range(len(word)):
  if letter == "c":
    if word[1] == "e" or "i":
      finished.append('ts')
      word = word.lstrip("c")
    else:
      finish.append('k')
      word = word.lstrip("c")
  elif letter == "j":
    finished.append('y')
    word = word.lstrip("j")
  elif letter == "a":
    if word[1] == "u":
      finished.append('a')
      finished.append('o')
      word = word.lstrip("a")
      word = word.lstrip("u")
  elif letter == "t":
    if word[1] == "g":
      finished.append('c')
      finished.append('i')
      word = word.lstrip("t")
      word = word.lstrip("g")
    else:
      finished.append('t')
      word = word.lstrip("t")
  else:
    finished.append(letter)
    word = word.lstrip(letter)
result = "".join(finished)
st.subtittle(result)
