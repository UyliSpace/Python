def censor(text, word):
  words = text.split()
  stars = '*' * len(word)
  result = ''
  count = 0
  for i in words:
    if i == word:
      words[count] = stars
    count += 1
  result = ' '.join(words)
  print result
  return result
