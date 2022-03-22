# AWS

2022.03.01

---

[TOC]

---



## Overview

- 네이티브 어플리케이션 설계 및 서버리스, 스토리지, 네트워크, 소프트웨어 인프라 서비스 등의 모든 범주에서 사용자가 요구하는 기능을 모두 제공



## 사용 사례

```markdown
1. 백업 및 저장
2. 빅데이터
3. 엔터프라이즈
4. 게임
5. Web, Mobile & Social Apps
6. Websites
```



## 대표 서비스 1: Compute

### EC2 (Elastic Compute Cloud)

- 클라우드 환경에서 서버를 할당 받아 사용할 수 있는 서비스
- 서버 호스팅과 비슷한 개념이지만 물리적인 서버가 아닌 AWS 클라우드에서 가상 환경을 할당받는다.

### Auto Scaling

- 수요에 따라 EC2의 규모를 자동으로 조절할 수 있다.

## 대표 서비스 2: Networking

### Direct Connect

- AWS와 사용자의 데이터 센터, 사무실, 코로케이션 환경 사이에서 private 연결을 설정할 수 있다.
- 802.1q VLAN을 사용하기 때문에 여러 가상 인터페이스를 나눌 수 있어, public 환경과 private 환경 간의 네트워크 분리를 유지하면서 동일한 연결을 사용한다.

### Route S3

- AWS에서 제공하는 DNS 서비스로 IPv6를 사용할 수 있고, Amazon EC2 인스턴스, Elastic Load Balancing 로드 밸런서, Amazon S3 버킷 등 AWS에서 실행되는 인프라에 효과적으로 연결할 수 있다.

### VPC (Virtual Private Cloud)

- 사설 네트워크 서비스로 IPv4와 IPv6를 모두 사용하여 리소스와 어플리케이션에 접근할 수 있다.

### Elastic Load Balancing

- AWS의 LB 서비스로 어플리케이션 트래픽을 Amazon EC2 인스턴스, 컨테이너, IP 주소, Lambda 함수, 가상 appliance와 같은 여러 대상에 자동으로 분산할 수 있다.

## 대표 서비스 3: Storage & Content Delivery

### Glacier

- 저비용 데이터 보관 및 백업 서비스
- 자주 사용하지 않는 데이터를 보관 및 백업하기 위해 사용하는 콘드 스토리지 서비스

### S3 (Simple Storage Service)

- 규모와 업종에 상관 없이 고객이 이 서비스를 이용하여 데이터 레이크, 웹사이트, 모바일 어플리케이션, 백업 및 복원, 아카이브, 엔터프라이즈 어플리케이션, IoT 디바이스, 빅데이터 분석과 같은 다양한 사용 사례에서 원하는 만큼의 데이터를 저장하고 보호할 수 있는 서비스

### EBS (Elasitc Block Storage)

- 대규모로 처리량과 transaction 집약적인 workload 모두를 지원하기 위해 Amazon Elastic Compute CLoud(EC2)에서 사용하도록 설계된 사용하기 쉬운 고성능 블록 스토리지 서비스

### Storage Gateway

- 클라우드 스토리지에 대한 on-promise 액세스 권한을 제공하는 하이브리드 클라우드 스토리지 서비스

## 대표 서비스 4: Database

> BigData

### RDS (Relational Database Service)

- Amazon Auroa, PostgreSQL, MySQL, MariaDB, ORACLE, Microsoft SQL Server 등 관계형 데이터베이스 서비스
- AWS에서 메모리, 선으 또는 I/O 최적화를 진행하며, 기존 데이터베이스를 Amazon RDS로 마이그레이션 또는 복제할 수 있다.

### DynamoDB

- 어떤 규모에서도 10밀리초 미만의 성능을 제공하는 키-값 및 문서 데이터베이스(NoSQL)

### SDB (Simple Database)

- 데이터베이스 관리 작업의 부담을 덜어주는 고가용성의 NoSQL 데이터 스토어
- 발자는 웹 서비스 요청을 통해 데이터 항목을 저장하고 쿼리하며 이후 나머지 부분은 Amazon SimpleDB가 처리한다.

### Elasticache

- 처리량이 많고 지연 시간이 짧은 인 메모리 데이터 스토어에서 데이터를 검색하여 데이터 집약적 앱을 구축하거나 기존 데이터베이스 성능을 올릴 수 있다.
- 캐싱, 세션 스토어, 게이밍, 지리 공간 서비스, 실시간 분석 및 대기열과 같은 실시간 사용 사례에 많이 사용된다.

### EMR (Elastic MapReduce)

- Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi 및 Presto와 같은 오픈 소스 도구를 사용하여 방대한 양의 데이터를 처리하기 위한 빅 데이터 플랫폼
- 프로비저닝 용량 및 클러스터 조정 등의 시간이 소요되는 작업을 자동화하여 빅데이터 환경을 쉽게 설치, 운영, 확장할 수 있다.

### Data Pipeline

- on-promise 데이터 소스뿐 아니라 여러 AWS 컴퓨팅 및 스토리지 서비스 간에 데이터를 안정적으로 처리하고 지정된 간격으로 이동할 수 있게 지원하는 웹 서비스

## 대표적 서비스 5: Deploy & Management

### CloudFormation

- Infrastructure as Code를 통해 손쉬운 방법으로 관련된 AWS 및 서드 파티 리소스 모음을 모델링하고, 일관된 방식으로 간단히 프로비저닝 하고, 수명 주기 전반에 걸쳐 관리할 수 있는 서비스

### CloudWatch

- Infrastructure as Code를 통해 손쉬운 방법으로 관련된 AWS 및 서드 파티 리소스 모음을 모델링하고, 일관된 방식으로 간단히 프로비저닝 하고, 수명 주기 전반에 걸쳐 관리할 수 있는 서비스

### Elastic Beanstalk

- Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker를 사용하여 Apache, Nginx, Passenger, IIS와 같은 친숙한 서버에서 개발된 웹 애플리케이션 및 서비스를 간편하게 배포하고 조정할 수 있는 서비스

### OpsWorks

- Chef 및 Puppet의 관리형 인스턴스를 제공하는 구성 관리 서비스
- Chef 및 Puppet은 코드를 사용해 서버 구성을 자동화할 수 있게 해주는 플랫폼



***Copyright* © 2022 Song_Artish**