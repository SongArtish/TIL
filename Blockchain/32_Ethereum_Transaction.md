# Ethereum Transaction

---

[TOC]

---



## 수수료

> 수수료를 지불하는 이유?
>
> 이더리움은 튜링 완전 언어이기 때문에, 반복문을 지원하며 이는 무한 루프 문제를 일으킬 수 있다. 따라서, 수수료를 통해서 악의적인 사용자가 큰 자원을 소모하는 트랜잭션을 실행시켜 이더리움 네트워크에 영향을 주는 것을 방지한다. 또한, 의도치 않게 무한 루프를 만든 코드를 실행시키더라도 Gas Limit을 설정하여 가스를 다 소모하기 전에 실행을 멈출 수 있다.

### 거래 수수료

이더리움에서 거래 수수료는 **가스(Gas)**라고 하며, 이는 트랜잭션 코드에 있는 모든 Opcode를 실행하는데 필요한 수수료를 측정하는 단위이다. 트랜잭션 **송신자**는 Gas Limit과 Gas Price를 트랜잭션에 지정한다.

- Gas Price: 가스 당 지불하려고 하는 이더의 양 (단위: Gwei)
- Gas Limit: 송신자가 지불하고자 하는 가스의 최대값

> - 1 Ether = 10^18 Wei
> - 1 Gwei = 10^9 Wei

$$
Gas Limit * Gas Price = Max Transaction Fee
$$

만약 CA에 최대 수수료(Max Transaction Fee)보다 충분한 이더가 들어있다면 트랜잭션은 문제 없이 실행될 것이다. 송신자는 트랜잭션이 완료된 후, 사용되지 않은 가스를 기존 비율로 환불받는다.
$$
Gas Limit - Use Gas - Use Gas - ... = Remaining Gas
$$
반대로 송신자가 트랜잭션 실행에 충분한 가스를 제공하지 않으면, 트랜잭션은 OOG 상태가 되며 실행이 중지된다. 그러면 결국 상태는 트랜잭션 이전의 상태로 돌아가고, 실패한 트랜잭션에 대한 기록은 남으며, 연산에 사용된 가스는 환불되지 않는다.

### 스토리지 수수료

스토리지를 사용할 때도 수수료를 내야하며, 스토리지의 최종 수수료는 32byte 단위에 비례한다. 스토리지 수수료는 저장되는 데이터 양을 최대한 적게 유지할수록 인센티브를 부여하는데, 만약 트랜잭션이 스토리지에 있는 특정 요소를 지우는 연산을 수행하면, 해당 연산을 수행하는 데에 대한 수수료는 면제하고, 저장 공간을 확보했기 때문에 기존에 요소를 스토리지에 추가했을 때 지불했던 가스를 환불받을 수 있다.



***Copyright* © 2022 Song_Artish**