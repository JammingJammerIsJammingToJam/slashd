def parse(text, start, chars):
  i = start
  returnVal = ""
  while text[i] not in chars:
    returnVal += text[i]
    i += 1
  return returnVal