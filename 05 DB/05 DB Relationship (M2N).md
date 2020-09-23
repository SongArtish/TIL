# DB Relationship (M : N)

2020.09.23



---

[TOC]

---



## 1. 중개모델

> 각각의 모델과 1:N관계를 맺어 서로 다른 모델을 중개해주는 역할을 한다.



### 1.1 중개모델 만들기

**1.1.1 중개모델 작성**

- 먼저 `models.py`에 중개모델을 다음과 같이 작성한다.

```python
# hospitals/models.py

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

- 이후 DB 초기화를 해준다. DB를 초기화 할 때는 `migrations/000X`번 파일과 `db.sqlite3`를 삭제한다.
- migrate을 다시 진행한다.

**1.1.2 객체 만들기**

- 이후 shell_plus에서 객체를 생성한 후, reservation을 만든다.

```shell
In [4]: reservation1 = Reservation.objects.create(doctor=doctor1, patient=patient1)      

In [6]: reservation2 = Reservation.objects.create(doctor=doctor2, patient=patient1)      
```

**1.1.3 역참조**

- **`<모델>.<중개모델>_set.all()`**
- 서로 다른 의사와 예약이 2번 잡힌 patient1의 reservation을 조회해보면 다음과 같다.

```shell
In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 2번 의사의 1번 환자>]>
```

**1.1.4 `ManyToManyField` 활용**

- `ManyToManyField`는 2개의 모델 중 어느 쪽에 있어도 상관 없다.

```python
# hospitals/models.py

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    ...
```

- shell에서 다음과 같이 출력할 수 있다.

```shell
In [9]: patient1.doctors.all()
Out[9]: <QuerySet [<Doctor: 1번 의사 john>, <Doctor: 2번 의사 eric>]>
```

**1.1.5 `related_name`를 활용한 양쪽 역참조**

- `related_name`을 이용하면 Doctor에서도 역참조를 할 수 있다.

```python
# hospitals/models.py

    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

```

```shell
In [3]: doctor1 = Doctor.objects.get(pk=1)

In [4]: doctor1.patients.all()
Out[4]: <QuerySet [<Patient: 1번 환자 Song>]>
```



### 1.2 중개모델 없이 : `ManyToManyField`

> `M : N 관계`를 간단하게 사용할 경우, Django에서는 `ManyToManyField`와 `related_name`을 사용해서 중개모델이 없는 것처럼 사용할 수도 있다.

```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()
	# ...

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
	# ...
```





*Copyright* © Song_Artish