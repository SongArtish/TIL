# Blockchain with Python

2020.12.23

---

[TOC]

---



## 블록체인 생성1

### 블록 구조체 구현

- 하나의 정보단위인 block을 정의한다.

```python
import datetime as dt
import hashlib  ## hash function 이용

class Block(object):
    # index, 블록 생성 시간, 데이터, 이전 hash value 등을 이용해서 새로운 hash를 가지는 블록 생성
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data    # important
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        # 아래 hash 함수를 보면 이전 block의 hash를 가져와서 다시 hash함수를 만든다.
        # 즉, 새롭게 hash값을 만들 때 이전 블록의 hash 값을 참고해서 만들기 때문에 이를 활용해서 무결성이 확보될 수 있다.
        sha = hashlib.sha256()
        new_str_bin = str(self.index) +  str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(new_str_bin.encode())
        return sha.hexdigest()
```

- `hash_block()` 함수는 아래와 같이 정의할 수도 있다.

  ```python
  def hash_block(self):
      return hashlib.sha256(str(self.index).encode() + str(self.data).encode() + str(self.nonce).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()
  ```

### Block 인스턴스 생성 함수

- Genesis 블록을 생성하는 함수를 정의한다.
- 이전 블록과 연결되는 블록을 생성하는 함수를 정의한다.

```python
# Genesis 블록을 만드는 함수
def create_genesis_block():
    return Block(0, dt.datetime.now(), data='genesis block', previous_hash="0")

def create_next_block(last_block):
    return Block(
        index = last_block.index+1,
        timestamp = dt.datetime.now(),
        data = f"Hey, I am blcok {last_block.index+1}",
        previous_hash = last_block.hash
    )
```

### block 생성하기

```python
# 블록체인이기는 하지만, linear한 linked 구조라고 생각하면 된다.
# 따라서 각 주소값을 리스트에 넣어서 관리해도 편하다.

blockchain = [create_genesis_block()]
previous_block = blockchain[-1]

num_of_block_to_add = 5
for i in range(num_of_block_to_add):
    # 이전 블록에 이어서 새로운 블록 생성
    block_to_add = create_next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
    print(f"{block_to_add.data}")
    print(f"prevhash: {block_to_add.previous_hash}")
    print(f"hash: {block_to_add.hash}")
    print()
```



## 블록체인 생성2

```python
import hashlib, time

class Block():
    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = ''
        self.nonce = 0
        self.hash = self.getHash()

    def getHash(self):
        # 주석의 코드를 하면 속도가 느리다.
        # sha = hashlib.sha256()
        # new_str_bin = str(self.index) +  str(self.timestamp) + str(self.data) + str(self.prevhash)
        # sha.update(new_str_bin.encode())
        # return sha.hexdigest()
        return hashlib.sha256(
            str(self.index).encode() + str(self.data).encode() + 
            str(self.nonce).encode() + str(self.timestamp).encode() + 
            str(self.prevhash).encode()
        ).hexdigest()

    # 조건: 앞의 5자리까지가 0 (difficulty)
    # 위의 조건에 만족하는 hash값을 찾는 함수
    def mine(self, difficulty):
        ans = ["0"]*difficulty
        answer = "".join(ans)
        while str(self.hash)[:difficulty] != answer:
            self.nonce += 1
            self.hash = self.getHash()
        return self.hash


class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 5
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(), 'Genesis Block'))

    def addBlock(self, nBlock):
        nBlock.prevhash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.mine(self.difficulty)
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

blocks = BlockChain()
blocks.addBlock(Block(len(blocks.chain),time.time(), "2nd"))
blocks.addBlock(Block(len(blocks.chain),time.time(), "3rd"))
for block in blocks.chain:
    print(f'nonce: {block.nonce}')
    print(f'data: {block.data}')
    print(f'prevhash: {block.prevhash}')
    print(f'hash: {block.hash}')
    print()
```

- hash 값을 구하는 함수에서 아래의 코드로 작성하면 계산이 되지 않는다. (시간이 지체가 된다.)

  ```python
      def getHash(self):
          sha = hashlib.sha256()
          new_str_bin = str(self.index) +  str(self.timestamp) + str(self.data) + str(self.prevhash)
          sha.update(new_str_bin.encode())
          return sha.thexdigest()
  ```

  - 정상적으로 작동하는 코드

  ```python
  def getHash(self):
          return hashlib.sha256(
              str(self.index).encode() + str(self.data).encode() + 
              str(self.nonce).encode() + str(self.timestamp).encode() + 
              str(self.prevhash).encode()
          ).hexdigest()
  ```

  - `왜 그럴까?`

- 위의 코드를 실행하면 아래와 같은 결과값을 출력한다.

```console
$ python blockchain.py

nonce: 0
data: Genesis Block
prevhash:
hash: 81d46e8b146c73799c8317545b57a841dc8b73ae277ffd22810017ce31caefc6

nonce: 830748
data: 2nd
prevhash: 81d46e8b146c73799c8317545b57a841dc8b73ae277ffd22810017ce31caefc6
hash: 00000c04cb0ab258b1eab58da76e798ac497148b74db851a3a3fc44c3a01160d

nonce: 244822
data: 3rd
prevhash: 00000c04cb0ab258b1eab58da76e798ac497148b74db851a3a3fc44c3a01160d
hash: 00000249ef371ca574bbba7b02fccd726e8d16ffc80c2054ef32f69be9bea381
```



***Copyright* © 2020 Song_Artish**