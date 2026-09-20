# Quần thể, quần xã và hành vi — Population, Community and Behavior (개체군·군집·행동)

Sinh thái học (Ecology / 생태학) bắt đầu khi câu hỏi không còn chỉ là “một organism hoạt động thế nào?” mà trở thành “nhiều organism tương tác với nhau và với môi trường ra sao?”. Ở cấp quần thể, ta quan tâm số lượng, mật độ, growth và gene flow. Ở cấp quần xã, ta quan tâm competition, predation, mutualism và food-web structure. Hành vi lại là cầu nối giữa physiology của cá thể và ecology của population.

## Population và growth

Quần thể (Population / 개체군) là nhóm cá thể cùng species sống trong một khu vực và có khả năng tương tác sinh sản. Population size thay đổi bởi birth, death, immigration và emigration.

Nếu resource không giới hạn và per-capita growth rate gần như hằng, population có thể được mô hình hóa bằng exponential growth:

```math
\frac{dN}{dt}=rN
```

Nghiệm có dạng:

```math
N(t)=N_0e^{rt}
```

Điểm quan trọng là tốc độ tăng tuyệt đối lớn dần khi population lớn, vì mỗi cá thể có thể tạo thêm offspring.

## Logistic growth và carrying capacity

Trong thực tế, resource thường hữu hạn. Logistic model thêm carrying capacity `K`:

```math
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
```

Khi `N` nhỏ so với `K`, growth gần exponential. Khi `N` tiến gần `K`, competition tăng và growth chậm lại.

`K` không phải một con số cố định bất biến; nó phụ thuộc season, habitat quality, predator, disease và resource availability.

> Mental model: exponential growth hỏi “nếu constraint chưa xuất hiện thì hệ tăng nhanh đến đâu?”, còn logistic growth thêm feedback của resource limitation.

## Density-dependent và density-independent factor

Disease transmission, competition và một số predator effect thường mạnh hơn khi density cao. Đây là density-dependent regulation. Storm, fire hoặc extreme weather có thể tác động ít phụ thuộc density hơn.

Phân biệt này giúp hiểu vì sao population không luôn quay về một equilibrium đơn giản.

## Species interaction

Competition xảy ra khi organism cùng dùng resource giới hạn. Predation là một organism ăn organism khác. Herbivory là animal ăn plant. Parasitism có lợi cho parasite và gây cost cho host. Mutualism tạo lợi ích cho cả hai phía trong context nhất định.

Những label này không phải lúc nào tuyệt đối. Một interaction có thể đổi sign khi environment thay đổi.

## Niche

Ổ sinh thái (Ecological Niche / 생태적 지위) không chỉ là “nơi sống”. Nó mô tả tập condition, resource và interaction cho phép species tồn tại và sinh sản.

Fundamental niche là range lý thuyết nếu không bị một số biotic constraint; realized niche là phần thực tế sau competition và interaction.

## Competition và coexistence

Nếu hai species dùng resource giống hệt nhau trong environment ổn định, competitive exclusion có thể khiến một species thắng. Coexistence có thể xảy ra khi niche differentiation, temporal variation, spatial heterogeneity hoặc trade-off giảm direct overlap.

Điều này giải thích tại sao biodiversity không chỉ phụ thuộc “ai mạnh hơn”, mà phụ thuộc cách resource và interaction được chia trong không gian–thời gian.

## Predator–prey dynamics

Predator và prey có thể tạo oscillation. Lotka–Volterra model đơn giản hóa dynamics thành hệ differential equation, nhưng real ecosystem còn có carrying capacity, alternative prey, refuge, time delay và behavior.

Model đơn giản vẫn hữu ích vì cho thấy feedback: nhiều prey làm predator tăng; nhiều predator làm prey giảm; prey giảm lại làm predator giảm.

## Food web và trophic level

Food chain là simplification tuyến tính; food web thực tế có nhiều pathway. Producer cố định energy; consumer lấy energy từ organism khác; decomposer phân giải organic matter.

Energy transfer giữa trophic level không đạt 100% vì respiration, heat loss và material không được tiêu hóa. Vì vậy biomass và available energy thường giảm dần lên trophic level cao hơn.

## Hành vi như phenotype

Hành vi (Behavior / 행동) chịu ảnh hưởng cả gene, development, learning và environment. Natural selection có thể tác động lên behavior nếu variation có heritable component và ảnh hưởng fitness.

Foraging behavior thường phản ánh trade-off giữa energy gain, time và predation risk. Mating behavior phản ánh sexual selection và parental investment.

## Cooperation và kin selection

Một behavior có cost cho actor nhưng benefit cho relative vẫn có thể được selection hỗ trợ nếu shared genes đủ lớn. Hamilton's rule thường được viết:

```math
rB>C
```

Trong đó `r` là relatedness, `B` benefit cho recipient và `C` cost cho actor. Công thức là model cho inclusive fitness reasoning, không phải phép đo đơn giản cho mọi social behavior.

## Common misconceptions

“Population luôn tăng tới carrying capacity rồi đứng yên” là sai; real population fluctuation, delay và disturbance có thể tạo overshoot hoặc crash.

“Species sống cùng nhau vì ecosystem cần cân bằng” là cách nói teleological. Community structure phát sinh từ interaction, history, dispersal và evolution, không phải vì ecosystem có mục tiêu giữ harmony.

## Kết nối

Population genetics nằm trong [[../03_evolution_and_diversity/00_evolution_and_population_genetics]]. Physiology ảnh hưởng behavior qua [[../04_organismal_biology/02_nervous_endocrine_and_immune_systems]]. Dòng energy và nutrient ở cấp ecosystem được phát triển trong [[01_ecosystems_biogeochemical_cycles_and_conservation]].
