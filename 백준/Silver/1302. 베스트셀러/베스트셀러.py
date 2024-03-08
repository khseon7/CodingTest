import sys
n=int(input())
book_sell_dict=dict()
for _ in range(n):
  book_name=sys.stdin.readline().rstrip()
  if book_name in book_sell_dict.keys():
    book_sell_dict[book_name]+=1
  else:
    book_sell_dict[book_name]=1
max_value=max(book_sell_dict.values())
max_list=sorted([i for i,j in book_sell_dict.items() if j==max_value])
print(max_list[0])