class TrieNode:
    def __init__(self):
        # Node의 children은 자료형이 딕셔너리
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        # 초기 루트 노드 생성
        self.root=TrieNode()
        
    def insert(self,word):
        # 루트 노드부터 시작
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            # 하위 노드로 이동
            node=node.children[char]
        # word에 대한 접근이 끝나면 마지막 노드에 "단어의 끝" 표시
        node.is_end_of_word=True

    # 사실상 search와 같은 방식
    def starts_with(self, prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
trie=Trie()
cnt=0
for _ in range(n):
    trie.insert(input().strip())
for _ in range(m):
    if trie.starts_with(input().strip()):
        cnt+=1
print(cnt)