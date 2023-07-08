# Issues

## 하나의 construct를 여러 item으로 측정한 경우

해당 item이 서로 일관성이 있는지 확인 후, item 간 평균을 구하여 하나의 데이터로 만든다.

```r
library(dplyr)
attitude <- data %>%
+ mutate(attitude = (attitude1+attitude2+attitude3)/3)
```