# Hành vi, quần thể và quần xã — Behavior, Population and Community Ecology (행동, 개체군과 군집생태학)

Khi chuyển từ một organism sang nhiều organism, Sinh học gặp loại câu hỏi mới. Một individual có physiology; một population có growth rate và allele frequency; một community có food web và interaction network. Những property này chỉ xuất hiện khi nhiều individual tương tác.

Ecology (sinh thái học / 생태학) nghiên cứu relationship giữa organism với nhau và với environment. File này đi từ behavior của individual lên population rồi community.

## Behavior — phenotype diễn ra theo thời gian

**Behavior (hành vi / 행동)** là action hoặc response của organism trước internal/external stimulus.

Behavior có thể được giải thích ở nhiều level. Ví dụ bird song:

- mechanism: neuron, hormone và muscle tạo sound;
- development: song learned hoặc matured thế nào;
- function: song ảnh hưởng territory/mating ra sao;
- evolution: behavior này phát sinh và thay đổi qua lineage thế nào.

Tinbergen nổi tiếng với bốn loại câu hỏi tương tự. Điều quan trọng là không coi một level explanation thay thế level khác.

## Innate và learned không phải hai hộp tách tuyệt đối

Một behavior có genetic/developmental predisposition nhưng vẫn cần learning. Bird có neural bias để học species-specific song nhưng experience vẫn quan trọng.

**Learning (học tập / 학습)** làm behavior thay đổi dựa experience. Habituation, conditioning, spatial learning và social learning là một số pattern.

Nature vs nurture thường là false dichotomy; behavior emerge từ gene × development × environment.

## Optimal foraging — behavior như bài toán trade-off

Animal tìm food phải cân bằng energy gained, time, predation risk và competition.

Một simplified model có thể xem net payoff:

\[
Net\ gain = Energy\ gained - Cost\ of\ searching/handling/risk
\]

Natural selection có thể favor decision rule tăng expected fitness, nhưng organism không cần consciously tính equation.

“Optimal” trong ecology là model dưới constraint, không phải behavior hoàn hảo.

## Social behavior và kin selection

Behavior có thể làm individual chịu cost nhưng relative nhận benefit.

**Inclusive fitness** tính cả direct reproduction và effect lên relatives mang shared allele.

Hamilton's rule thường viết:

\[
rB > C
\]

Trong đó \(r\) là relatedness, \(B\) benefit cho recipient, \(C\) cost cho actor.

Equation là model để hiểu khi altruistic behavior có thể được selection favor, không phải organism tính toán consciously.

# Population ecology — number thay đổi theo time

**Population (quần thể / 개체군)** có size \(N\), density, age structure, birth/death rate và spatial distribution.

## Exponential growth

Nếu per-capita growth rate \(r\) gần constant và resource chưa limiting:

\[
\frac{dN}{dt}=rN
\]

Solution:

\[
N(t)=N_0e^{rt}
\]

Growth absolute tăng khi N tăng vì nhiều individual sinh sản hơn.

Exponential growth có thể mô tả early bacterial culture hoặc invasive population trong period ngắn. Nhưng không thể kéo dài vô hạn vì resource finite.

### Doubling time

Nếu r constant:

\[
t_d = \frac{\ln 2}{r}
\]

Logarithm xuất hiện vì ta giải exponential equation theo time.

## Logistic growth

Một model thêm resource limitation:

\[
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
\]

\(K\) là **carrying capacity (sức chứa môi trường / 환경수용력)** trong model.

K không phải một con số cố định vĩnh viễn. Nó thay đổi theo climate, resource, predator, disease và habitat.

Khi N nhỏ so với K, model gần exponential. Khi N tiến K, growth giảm.

Logistic curve hữu ích nhưng real population có time lag, seasonality, age structure và stochasticity.

## Density-dependent và density-independent factor

**Density-dependent factor** có effect thay đổi theo population density: competition, disease transmission hoặc resource depletion.

**Density-independent factor** theo classification cơ bản tác động không trực tiếp phụ thuộc density, như extreme weather event.

Trong reality boundary có thể mixed.

## Life history — organism phân bổ finite resource

Organism không thể tối đa đồng thời growth, maintenance và reproduction.

**Life-history theory (생활사 이론)** nghiên cứu trade-off giữa age at reproduction, offspring number, parental investment và lifespan.

Species tạo rất nhiều offspring với low investment và species tạo ít offspring high investment đại diện different strategy, nhưng old r/K selection labels chỉ là oversimplification nếu dùng quá cứng.

## Survivorship curve

Type I: mortality thấp ở young/midlife, tăng late; thường minh họa large mammal.

Type II: mortality rate tương đối constant.

Type III: mortality rất cao early, survivor sau đó sống lâu hơn; nhiều fish/invertebrate.

Curve là descriptive model; species thực có thể không fit hoàn hảo.

## Metapopulation — nhiều population patch nối bởi migration

Habitat thường fragmented thành patch. Local population có thể extinct rồi được recolonized.

**Metapopulation (메타개체군)** giúp hiểu conservation: không chỉ size mỗi patch mà connectivity giữa patch cũng quan trọng.

# Community ecology — interaction giữa species

**Community (quần xã / 군집)** gồm population của nhiều species cùng khu vực và interaction.

## Competition

Hai species dùng resource limited có thể giảm growth của nhau.

**Competitive exclusion principle** nói hai species dùng niche hoàn toàn giống nhau trong environment stable khó coexist indefinitely theo model đơn giản.

Coexistence có thể xảy ra nhờ niche differentiation, temporal variation hoặc trade-off.

## Ecological niche

**Niche (ổ sinh thái / 생태적 지위)** không chỉ là “nơi species sống”. Nó là tập resource, condition và interaction xác định cách species tồn tại/reproduce.

**Fundamental niche** là range có thể sống nếu bỏ bớt biotic constraint. **Realized niche** là phần thực tế sau competition/predation và interaction khác.

## Predation và herbivory

Predator làm prey mortality tăng; prey abundance lại ảnh hưởng food availability predator. Coupled interaction có thể tạo cycle.

Lotka–Volterra predator–prey model đơn giản:

\[
\frac{dN}{dt}=rN-aNP
\]

\[
\frac{dP}{dt}=baNP-mP
\]

N là prey, P predator. Model giúp thấy interaction term \(NP\) xuất hiện vì encounter phụ thuộc cả hai population.

Real ecosystem phức tạp hơn với alternative prey, refuge và functional response.

## Mutualism, commensalism và parasitism

Mutualism (+/+), competition (-/-), predation/parasitism (+/-), commensalism (+/0) là symbolic shorthand.

Nhưng interaction có thể đổi sign theo environment. Mycorrhiza beneficial khi phosphorus low có thể costlier khi nutrient abundant.

Vì vậy relationship là dynamic context-dependent.

## Keystone species

**Keystone species (핵심종)** có impact ecosystem lớn hơn expected từ abundance.

Classic predator removal experiment cho thấy mất một predator có thể làm competitor dominate và species diversity giảm.

Keystone không đồng nghĩa “loài phổ biến nhất”.

## Food chain và food web

Food chain linear là simplification. Real community tạo **food web (lưới thức ăn / 먹이그물)**.

Node = species/trophic group; edge = feeding interaction. Đây là graph theory ứng dụng trực tiếp.

Network topology ảnh hưởng pathway energy và response khi species mất.

## Trophic cascade

Thay predator abundance có thể lan xuống nhiều trophic level. Predator giảm herbivore; herbivore giảm làm vegetation tăng là một pattern cascade.

Nhưng cascade strength tùy ecosystem và interaction network, không phải rule universal.

## Succession

Sau disturbance, community composition thay đổi theo time gọi là **ecological succession (천이)**.

Primary succession bắt đầu nơi gần như không có soil/biological legacy; secondary succession diễn ra nơi disturbance nhưng soil/seed bank còn.

Succession không phải lúc nào cũng đi đến một climax cố định. Disturbance, climate và stochastic event làm community dynamic.

## Island biogeography

MacArthur–Wilson model xem island species richness như balance giữa immigration và extinction.

Island gần mainland có immigration cao hơn; island lớn thường extinction thấp hơn do population lớn/habitat diversity.

Model này ảnh hưởng conservation design vì habitat fragment có thể behave giống “island” trong landscape.

## Common misconceptions

### “Population sẽ tự dừng chính xác ở K”

K là model parameter dynamic. Population có thể overshoot, oscillate hoặc fluctuate random.

### “Predator xấu vì làm prey chết”

Predation là ecological interaction; removal predator có thể làm whole food web thay đổi bất ngờ.

### “Niche = habitat”

Habitat là nơi sống; niche rộng hơn, gồm resource, condition và ecological role.

### “Nature luôn ở trạng thái cân bằng”

Ecosystem thường chịu disturbance và change. Dynamic stability không có nghĩa static composition.

## Mental Model

> Behavior là decision/action của individual dưới constraint; population ecology theo dõi number và distribution; community ecology nghiên cứu network interaction giữa species. Khi thêm energy flow và nutrient cycle, ta lên level ecosystem trong [[01_ecosystems_biogeochemical_cycles_and_conservation]].