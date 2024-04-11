text = '''
apple and banana one apple one banana
a red apple and a green apple
'''

def make_index(words):
  words = text.split( )
  index = {}
  for w in words:
    if w in index:
      index[w] += 1
    else:
      index[w] = 1

  return index

# print the symbols in longest word in index:
def find_max_word_length(index):
  max_word_length = 0
  for key in index.keys():
    if max_word_length< len(key):
      max_word_length = len(key)

  return max_word_length

def display_index(index):
  for k,v in index.items():
    print("{} - {}".format(k,v))

# print sorted by values
def display_sorted_index(index, max_word_length):
  for item in sorted(index.items(), key=lambda t:t[1], reverse=True):
    print("|{word:<{word_width}}|{count:^{count_width}}|".format(
      word=item[0], word_width=max_word_length, count=item[1], count_width=5))

index = make_index(text)
max_word_length = find_max_word_length(index)
# print("max_word_length", max_word_length)
display_sorted_index(index, max_word_length)
# display_index(index)