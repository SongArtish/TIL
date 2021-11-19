# RFID

> Near Field Communication

---

[TOC]

---



## General

---

- NFC targets are often programmable devices.



## Modes

---

### Communication Modes

1. Passive communication mode
   - the initiator always supplies the RF energy and the target gets powered by the initiator's field
2. Active communication mode
   - both target and initiator have their own energy sources

### Operating Modes

1. reader/writers
   - read data from a target and write to it
2. card emulators
   - acting like RFID tags when they're in the field of another NFC or RFID device
3. peer-to-peer mode
   - they can exchange data in both directions



## Formats

---

> **NDEF**(NFC Data Exchange Format) is a data format that NFC devices use between when exchanging data

### 1) Simple Text Records

- contain text string
- generally don't contain instructions for the target device
- also include metadata indicating the language and encoding scheme (e.g., UTF-8)

### 2) URIs

- contains network addresses
- expected to pass the record to an application of an target device that can display it, such as web browser

### 3) Smart Posters

- contains data you might attach to a poster to give it more information
- target device that receives a Smart Poster record might open a browser, SMS, or email application

### 4) Signatures

- a way to give trustworthy information about the origins of data contained in an NDEF record



***Copyright* © 2021 Song_Artish**