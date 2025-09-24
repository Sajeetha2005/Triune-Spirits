i = None
w = None
def differ_by_one(w1,w2):
  if len(w1)!=len(w2):
      return False
  count = 0
  for i in  range (len(w1)):
    if w1[i] != w2[i] :
        count += 1
        if count>1:
            return False
  return count==1
def word_ladder(path,start,end):
  with open(path,"r") as f:
    words = [line.strip() for line in f.readlines()]
  queue = [[start]]
  visited = [start]
  while queue:
    ladder = queue.pop(0)
    word = ladder[-1]
    if word==end:
        return ladder
    for w in words:
      if w not in visited and differ_by_one(word, w):
          queue.append(ladder + [w])
          visited.append(w)
  return None
ladder = word_ladder("words.txt","hit","cog")
if ladder:
    print("->".join(ladder))
else:
  print("No ladder found")

