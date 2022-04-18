# Blockchain with TypeScript

> nomadcoder 강의 참고

2022.04.18

---

[TOC]

---



## 코드

```ts
// js hash function library
import * as CryptoJS from "crypto-js";

class Block {
    // Use method before creating thb object
    static calculateBlockHash = (
        index:number,
        previousHash: string,
        timestamp: number,
        data: string
    ): string => CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
    
    static validateStructure = (aBlock: Block): boolean =>
        typeof aBlock.index === "number" &&
        typeof aBlock.hash === "string" &&
        typeof aBlock.previousHash === "string" &&
        typeof aBlock.timestamp === "number" &&
        typeof aBlock.data === "string";
    
    public index: number;
    public hash: string;
    public previousHash: string;
    public data: string;
    public timestamp: number;

    // constructor
    constructor(
        index: number,
        hash: string,
        previousHash: string,
        data: string,
        timestamp: number
    ) {
        this.index = index;
        this.hash = hash;
        this.previousHash = previousHash;
        this. data = data;
        this.timestamp = timestamp;
    }
}

const createGenesisBlock = (data: string): Block => {
    const initialTimestamp: number = Math.round(new Date().getTime() / 1000);
    const initialHash: string = Block.calculateBlockHash(
        0,
        "",
        initialTimestamp,
        data
    );
    const newBlock: Block = new Block(
        0,
        initialHash,
        "",
        data,
        initialTimestamp
      );
      return newBlock;
}

const genesisBlock: Block = createGenesisBlock("first block")

// push only Block object to the blockchain
let blockchain: Block[] = [genesisBlock];

const getBlockchain = (): Block[] => blockchain;

const getLatestBlock = (): Block => blockchain[blockchain.length - 1];

const getNewTimeStamp = (): number => Math.round(new Date().getTime() / 1000);

const createNewBlock = (data: string): Block => {
    const previousBlock: Block = getLatestBlock();
    const newIndex: number = previousBlock.index + 1;
    const newTimestamp: number = getNewTimeStamp();
    const newHash: string = Block.calculateBlockHash(
      newIndex,
      previousBlock.hash,
      newTimestamp,
      data
    );
    const newBlock: Block = new Block(
      newIndex,
      newHash,
      previousBlock.hash,
      data,
      newTimestamp
    );
    addBlock(newBlock);
    return newBlock;
  };

  const getHashforBlock = (aBlock: Block): string =>
  Block.calculateBlockHash(
    aBlock.index,
    aBlock.previousHash,
    aBlock.timestamp,
    aBlock.data
  );

const isBlockValid = (
    candidateBlock: Block,
    previousBlock: Block
): boolean => {
    if(!Block.validateStructure(candidateBlock)) {
        console.log(`this block(index ${candidateBlock.index}) has no valid structure.`)
        return false;
    } else if(previousBlock.index + 1 !== candidateBlock.index) {
        console.log(`this block(index ${candidateBlock.index}) has no valid index.`)
        return false;
    } else if (previousBlock.hash !== candidateBlock.previousHash) {
        console.log(`this block(index ${candidateBlock.index}) has no valid previous hash.`)
        return false;
    } else if (getHashforBlock(candidateBlock) !== candidateBlock.hash) {
        console.log(`this block(index ${candidateBlock.index}) has no valid structure.`)
        return false;
    } else {
        return true;
    }
};

const addBlock = (candidateBlock: Block): void => {
    if (isBlockValid(candidateBlock, getLatestBlock())) {
        blockchain.push(candidateBlock);
    }
}

//
createNewBlock("second block");
createNewBlock("third block");
createNewBlock("fourth block");
createNewBlock("fifth block");

console.log(getBlockchain())

export {};
```



***Copyright* © 2022 Song_Artish**