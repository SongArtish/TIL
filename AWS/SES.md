# Simple Email Service

> Amazon SES

---

[TOC]

---



## 개념

> outbound만 가능한 이메일 전송 서비스

- 마케팅 혹은 webzine 메일 등의 **대량의 이메일 발송에 적합**
- 발송한 이메일 수와 데이터 전송에 대해 요금이 부과됨 (사전 확약금 X)
- 전송 작업의 상태를 쉽게 모니터링할 수 있어서 가용성이 높음
- 입증된 네트워크 인프라와 데이터 센터에서 운영되므로 안정성이 높음



## Email Sender Reputation

> a score that an Internet Service Provider (ISP) assigns to an organization that sends email
>
> - 참고 문서: [sparkpost](https://www.sparkpost.com/resources/email-explained/email-sender-reputation/)

- a crucial component of email deliverability
- determinant
  - the **amount** of email sent by the organization
  - **how many recipients mark the organization’s emails as spam** or otherwise complain to the ISP about the messages
  - how often the organization’s emails hit the ISP’s spam trap
  - the organization’s inclusion on different blacklists
  - how many of the organization’s emails bounce because they were sent to unknown users or for other reasons
  - how many recipients open, reply to, forward, and delete the organization’s messages, as well as click the links found in them
  - how many recipients unsubscribe from the organization’s email list



https://www.sparkpost.com/resources/email-explained/email-sender-reputation/



- 이메일의 도달 가능성을 높여줌: ISP(Internet Service Provider)는 SES 서비스를 거친 이메일을 신뢰하게 되기 때문에
  - 컨텐츠 필터링 기능을 사용하여 바이러스나 멀웨어를 포함한 메시지를 감지하여 발신전에 차단한다.
  - ISP와 함께 수신 거부 피드백 루프를 유지한다. 이는 전송 전략을 추진하는 데 도움을 준다.
  - SPF(Sender Policy Framework) 및 DKIM(DomainKeys Identified Mail)과 같은 인증 메커니즘을 지원한다.

http://wildpup.cafe24.com/archives/1003







***Copyright* © 2021 Song_Artish**