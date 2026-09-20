# Quần thể, quần xã và hành vi — Population, Community and Behavior (개체군, 군집과 행동)

Ở organismal biology, ta theo dõi một cơ thể giữ homeostasis, sinh sản và phát triển. Ecology thay đổi câu hỏi bằng cách lùi camera ra xa hơn: **điều gì xảy ra khi nhiều cá thể cùng loài chia sẻ resource, khi nhiều loài tương tác, và khi behavior của từng cá thể làm thay đổi population-level pattern?**

Ecology không tách khỏi evolution. Population growth tạo competition; competition tạo selection pressure; evolution lại thay trait và interaction. Vì vậy chapter này nối trực tiếp physiology, behavior và population genetics.

## 1. Từ individual sang population

Một **population (quần thể / 개체군)** gồm cá thể cùng species sống trong cùng vùng và có interaction/reproduction liên quan.

Ở individual scale ta hỏi body temperature hay reproductive output. Ở population scale ta hỏi:

\[
N(t)=\text{population size at time }t
\]

Population size đổi vì birth, death, immigration và emigration:

\[
\Delta N = B-D+I-E
\]

Đây là accounting identity đơn giản nhưng rất mạnh: muốn hiểu population tăng/giảm phải tìm cơ chế đi qua bốn dòng này.

## 2. Exponential growth: khi mỗi cá thể tạo contribution tương tự

Nếu resource gần như không giới hạn và per-capita growth rate \(r\) ổn định:

\[
\frac{dN}{dt}=rN
\]

Solution:

\[
N(t)=N_0e^{rt}
\]

Vì growth rate tỷ lệ với N hiện tại, population lớn tạo nhiều offspring tuyệt đối hơn, làm curve tăng nhanh.

Bacteria trong early culture và invasive population ở stage đầu có thể gần model này.

Nhưng exponential growth không thể kéo dài vô hạn trong finite environment.

## 3. Logistic growth: resource limitation đi vào model

Khi population density tăng, food, territory hoặc nesting site trở nên hạn chế.

Một model đơn giản thêm **carrying capacity** \(K\):

\[
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
\]

Khi \(N\ll K\), term gần 1 và growth gần exponential.

Khi \(N\to K\), growth chậm lại.

Nhưng K không phải “sức chứa cố định vĩnh viễn”. Climate, resource, habitat quality và technology của organism có thể làm K thay đổi.

Model giúp reasoning, không phải law tuyệt đối.

## 4. Density dependence và feedback

Nếu crowding làm disease spread tăng hoặc food per individual giảm, death rate có thể tăng và birth rate giảm.

Đây là negative feedback ở population scale.

Một concept từ physiology quay lại trong ecology:

```text
population density rises
    ↓
competition / disease increases
    ↓
per-capita growth falls
    ↓
population growth slows
```

Feedback là pattern xuyên scale.

## 5. Life history: organism phân bổ resource hữu hạn

Mỗi organism có finite energy/time. Resource dùng cho growth không đồng thời dùng cho reproduction; reproduction hiện tại có thể giảm survival tương lai.

**Life-history strategy** mô tả trade-off giữa age at reproduction, offspring number, parental investment và lifespan.

Không có strategy tốt nhất universal. Environment khác nhau ưu tiên trade-off khác nhau.

Đây là điểm physiology nối evolution: energy budget của organism trở thành fitness outcome.

## 6. Behavior là phenotype có ecological consequence

Behavior ảnh hưởng nơi organism ăn, mating, tránh predator và cooperate.

Một behavior có thể innate, learned hoặc kết hợp.

Natural selection có thể shape behavioral tendency nếu variation có heritable component.

Nhưng behavior cũng flexible: learning cho phép response nhanh hơn genetic evolution khi environment thay đổi trong lifetime.

## 7. Optimal foraging là model trade-off

Animal tìm food phải cân bằng energy gain, search time và predation risk.

Model optimal foraging không nói animal “giải equation” trong đầu. Nó hỏi strategy nào có thể được favored hoặc produce observed pattern dưới constraint.

Đây là ví dụ economics-like reasoning trong biology.

## 8. Cooperation và kin selection

Một behavior giảm direct reproduction của actor nhưng giúp relative có thể vẫn spread nếu relative share allele.

Hamilton's rule thường viết:

\[
rB>C
\]

Trong đó \(r\) là relatedness, \(B\) benefit cho recipient, \(C\) cost cho actor.

Equation không phải universal calculator cho mọi behavior; nó là framework để hiểu inclusive fitness.

## 9. Community: khi nhiều species cùng tồn tại

Một **community (quần xã / 군집)** gồm population của nhiều species tương tác trong cùng area.

Từ đây interaction có thể được nhìn qua effect lên fitness/growth của hai bên:

- competition: cả hai chịu cost;
- predation/herbivory: một bên benefit, một bên cost;
- mutualism: cả hai benefit;
- commensalism: một bên benefit, bên kia effect nhỏ.

Nhưng real interaction có thể đổi theo context. Một mutualism có thể yếu hoặc chuyển cost khi resource thay đổi.

## 10. Competition và niche

**Niche (ổ sinh thái / 생태적 지위)** không chỉ là nơi species sống. Nó gồm resource use, environmental condition và interaction role.

Hai species overlap niche mạnh có thể competition.

Competitive exclusion nói hai species không thể coexist ổn định vô hạn nếu dùng resource hoàn toàn giống nhau trong model đơn giản.

Coexistence có thể xuất hiện qua niche differentiation, temporal separation hoặc trade-off khác.

## 11. Predator–prey tạo dynamics chứ không chỉ “ai ăn ai”

Predator abundance phụ thuộc prey; prey mortality phụ thuộc predator.

Lotka–Volterra model đơn giản:

\[
\frac{dN}{dt}=rN-aNP
\]

\[
\frac{dP}{dt}=baNP-mP
\]

Model có thể tạo oscillation.

Thực tế phức tạp hơn vì refuge, alternative prey, seasonality và density dependence, nhưng equation cho mental model về coupled dynamics.

## 12. Food web: interaction tạo network

Ecosystem không phải chain đơn “grass → rabbit → fox”. Species thường có nhiều food source và predator.

Food web là graph với species/node và feeding relation/edge.

Network structure ảnh hưởng stability và pathway energy flow.

Graph theory từ CS vì thế có application tự nhiên trong ecology.

## 13. Keystone species và indirect effect

Một species có abundance không lớn vẫn có effect lớn nếu position trong network quan trọng.

Remove predator có thể tăng herbivore, làm plant biomass giảm — **trophic cascade**.

Điều này cho thấy effect ecological thường indirect. Muốn causal reasoning phải theo network nhiều step, giống signaling pathway trong cell.

## 14. Succession: community thay đổi theo thời gian

Sau disturbance, community composition có thể đổi có pattern.

Early colonizer thay environment, tạo condition cho species khác; competition và soil development tiếp tục đổi system.

Succession không phải một con đường bắt buộc tới một “climax hoàn hảo”. Disturbance regime và historical contingency ảnh hưởng trajectory.

## 15. Behavior, community và evolution feedback nhau

Predator pressure shape prey behavior; prey behavior đổi grazing pattern; grazing pattern đổi plant community; plant community đổi habitat cho species khác.

Ecological interaction tạo selection pressure, rồi evolved trait lại đổi ecology.

Đây là **eco-evolutionary feedback**.

## 16. Từ community sang ecosystem: còn thiếu vật chất và năng lượng

Community ecology tập trung organism interaction. Nhưng organism phải lấy energy và matter từ environment.

Nếu chỉ biết “ai ăn ai”, ta vẫn chưa biết carbon đi đâu, nitrogen quay vòng thế nào, hay bao nhiêu solar energy vào food web.

Vì vậy scale tiếp theo là **ecosystem**, nơi biotic community và abiotic environment được xem cùng nhau.

Tiếp tục với [[01_ecosystems_biogeochemical_cycles_and_conservation]].