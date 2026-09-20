# Quần thể, Quần xã và Hành vi — Population, Community and Behavior (개체군, 군집과 행동)

Sau khi học organismal biology, ta đã có một cá thể có physiology, behavior và reproduction. Nhưng ngoài tự nhiên, không organism nào tồn tại một mình. Cá thể cạnh tranh resource, tìm mate, tránh predator, tương tác mutualist và chịu environmental fluctuation. Vì vậy scale tiếp theo của Sinh học là **quần thể (population)** và **quần xã (community)**.

> **Mental model:** ecology là study của interaction và constraint. Population growth bị giới hạn bởi resource; species interaction thay fitness; behavior nối physiology với environment; community structure xuất hiện từ nhiều interaction đồng thời.

## 1. Population size không chỉ là “đếm số con”

Một population được mô tả bởi size \(N\), density, age structure, sex ratio, spatial distribution và genetic composition.

Hai population cùng N có thể rất khác nếu một population toàn juvenile còn population kia phần lớn old individual. Demography vì vậy cần structure, không chỉ count.

## 2. Exponential growth: baseline khi constraint chưa mạnh

Nếu per-capita growth rate gần constant:

\[
\frac{dN}{dt}=rN
\]

solution là:

\[
N(t)=N_0e^{rt}
\]

Growth càng lớn khi N lớn vì có nhiều individual sinh sản. Đây là positive feedback.

Exponential model có thể phù hợp short-term khi resource dư, như microbial culture early phase hoặc invasive population mới vào habitat thuận lợi.

## 3. Doubling time

Với exponential growth, doubling time xấp xỉ:

\[
t_d=\frac{\ln 2}{r}
\]

Relation này nối ecology với logarithm. Một population có r lớn gấp đôi nhanh hơn không tuyến tính theo trực giác đơn giản.

## 4. Logistic growth và carrying capacity

Resource hữu hạn làm per-capita growth giảm khi N tăng. Model logistic:

\[
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
\]

\(K\) là carrying capacity trong model — population size mà net growth tiến gần zero dưới condition cụ thể.

K không phải hằng số vĩnh viễn của species; climate, resource, predator và habitat làm K thay đổi.

## 5. Density-dependent và density-independent factor

Disease transmission, competition và resource shortage thường mạnh hơn khi density cao: density-dependent.

Storm, fire hoặc sudden freeze có thể ảnh hưởng không trực tiếp theo density: density-independent trong model đơn giản.

Phân loại giúp hiểu feedback population, nhưng real event có thể kết hợp cả hai.

## 6. Life history trade-off

Organism phân resource hữu hạn cho growth, maintenance và reproduction.

Một species có thể sinh nhiều offspring nhỏ với parental care ít; species khác sinh ít offspring nhưng đầu tư nhiều.

Không có “strategy tốt hơn” universal. Fitness phụ thuộc mortality pattern, environment predictability và resource.

## 7. Survivorship curve

Type I: mortality thấp đầu đời, tăng ở tuổi cao. Type II: risk tương đối đều. Type III: mortality rất cao early life nhưng survivor sống lâu hơn.

Đây là simplified pattern, useful để liên hệ life-history strategy với demography.

## 8. Metapopulation

Species trong fragmented habitat có thể tồn tại thành nhiều local population nối bằng migration.

Một patch có thể extinct local rồi recolonize. Persistence toàn hệ phụ thuộc balance extinction–colonization và connectivity.

Conservation corridor có ý nghĩa từ model này.

## 9. Behavior là phenotype dưới selection

**Hành vi (behavior / 행동)** là response/action của organism, được tạo bởi nervous/endocrine system, development, learning và environment.

Behavior có genetic component trong nhiều case nhưng cũng plastic. Natural selection tác động behavior nếu variation heritable ảnh hưởng fitness.

## 10. Innate và learned behavior không phải hai hộp tuyệt đối

Một behavior có thể có predisposition genetic nhưng cần learning để hoàn thiện. Birdsong, navigation hoặc fear response thường là interaction nature–experience.

Learning là phenotypic plasticity cho phép update behavior trong lifetime.

## 11. Optimal foraging và trade-off

Animal phải maximize energy/nutrient gain nhưng cũng chịu search time, handling time và predation risk.

Optimal-foraging model không nói animal “tính calculus”; nó là framework dự đoán strategy được selection favor trong constraint.

Model đơn giản có thể fail nếu social factor hoặc learning quan trọng.

## 12. Territoriality

Defending territory có benefit resource/mate nhưng cost energy/injury/time.

Territorial behavior chỉ evolutionarily favorable khi benefit > cost trong context.

Một lần nữa, behavior là economic trade-off dưới biological constraint.

## 13. Altruism và inclusive fitness

Một behavior làm giảm direct reproduction của actor nhưng tăng relative reproduction của genetic relative có thể được giải thích bằng **kin selection**.

Hamilton’s rule đơn giản:

\[
rB>C
\]

trong đó \(r\) là relatedness, \(B\) benefit recipient và \(C\) cost actor.

Đây không phải law chính xác cho mọi social behavior, nhưng là mental model mạnh cho inclusive fitness.

## 14. Reciprocal cooperation

Cooperation giữa unrelated individual có thể persist nếu interaction lặp lại, cheating bị detect/punish hoặc partner choice tồn tại.

Game theory được dùng model strategy evolution như Prisoner’s Dilemma.

Ecology và economics/computation gặp nhau ở strategic interaction.

## 15. Niche

**Ecological niche (생태적 지위)** không chỉ là “nơi sống”. Nó gồm resource use, environmental tolerance, timing và interaction role.

**Fundamental niche** là range có thể sống khi không bị biotic restriction; **realized niche** là range thực sau competition/predation và interaction khác.

Niche là multidimensional condition/resource space.

## 16. Competition

Species cạnh tranh khi dùng resource giới hạn chung. Competition có thể exploitative (gián tiếp dùng hết resource) hoặc interference (direct exclusion).

Competitive exclusion principle nói hai species có niche hoàn toàn identical khó coexist ổn định lâu dài trong simple constant environment.

Nhưng real community có fluctuation, spatial heterogeneity và resource partitioning giúp coexistence.

## 17. Resource partitioning

Species có thể chia resource theo space, time hoặc type. Bird species ăn ở tầng cây khác nhau; predator săn time khác nhau.

Partitioning giảm niche overlap và competition.

Pattern có thể là nguyên nhân/effect của evolution; cần experiment để tách.

## 18. Predator–prey dynamics

Simple Lotka–Volterra model:

\[
\frac{dN}{dt}=rN-aNP
\]

\[
\frac{dP}{dt}=baNP-mP
\]

Prey growth bị predation giảm; predator growth phụ thuộc encounter prey.

Model có thể tạo oscillation, nhưng real system thêm carrying capacity, refuge, alternative prey và seasonality.

Point không phải thuộc equation mà hiểu feedback coupled population.

## 19. Functional response

Predator consumption không tăng tuyến tính vô hạn với prey density vì handling/satiation.

Holling Type II response saturates; Type III sigmoid có low consumption khi prey rare.

Shape response ảnh hưởng stability prey–predator system.

## 20. Mutualism, commensalism, parasitism

Interaction label dựa sign effect relative fitness/growth:

- mutualism +/+;
- competition -/-;
- predation/parasitism +/-;
- commensalism +/0 trong model ideal.

Nhưng sign có thể change theo context. Mycorrhiza beneficial khi phosphorus low nhưng cost carbon; relationship strength đổi theo nutrient.

## 21. Keystone species

Một species có effect community lớn hơn abundance gợi ý **keystone species**.

Removing predator có thể tạo trophic cascade, làm herbivore tăng và vegetation giảm.

Community network có node influence không tỷ lệ đơn giản biomass.

## 22. Trophic cascade

Predator tác động prey trực tiếp; prey tác động producer; vì vậy predator có indirect effect lên plant.

Ecology cần causal chain nhiều step giống signaling network.

Direct interaction và indirect interaction đôi khi cho outcome ngược trực giác.

## 23. Food web chứ không phải food chain

Real ecosystem có many feeding links. Species có thể ăn ở nhiều trophic level; omnivory và detrital path phổ biến.

Food web được biểu diễn graph: node = species/group; edge = energy/feeding interaction.

Network topology ảnh hưởng stability và disturbance propagation.

## 24. Disease ecology

Pathogen transmission phụ thuộc host density/contact, immunity, vector và environment.

Simple epidemic model như SIR dùng differential equation để track susceptible–infectious–recovered compartment.

Ecology và epidemiology chia cùng population-dynamics language.

## 25. Invasive species

Species tới new habitat có thể expand nếu escape enemy, resource phù hợp hoặc disturbance mở niche.

Không phải mọi introduced species trở thành invasive; invasion là outcome của propagule pressure + trait + ecosystem context.

Management cần hiểu population growth và interaction, không chỉ loại bỏ individual.

## 26. Community succession

Sau disturbance, community composition thay theo time.

Primary succession bắt đầu nơi gần như không có soil; secondary succession ở nơi soil/biological legacy còn.

Succession không phải luôn fixed linear path tới một climax state; disturbance và contingency có thể tạo alternative trajectory.

## 27. Case study: wolf và trophic cascade

Wolf reintroduction thường được dùng ví dụ predator ảnh hưởng herbivore và vegetation. Nhưng real ecosystem effect phức tạp, gồm prey number/behavior, other predator, human management và climate.

Lesson tốt nhất không phải memorize slogan mà học cách tránh oversimplification trong ecological causality.

## 28. Case study: bee pollination

Plant cung cấp nectar/pollen; pollinator giúp pollen transfer. Network pollination ảnh hưởng plant reproduction và crop yield.

Loss pollinator không chỉ tác động một species mà có thể đổi community interaction.

## 29. Common misconceptions

“Population luôn tiến tới K” sai; environment/K thay đổi và dynamics có delay.

“Predator luôn xấu cho ecosystem” sai; predator có thể stabilize community hoặc tạo cascade.

“Niche = habitat” quá hẹp.

“Altruism tiến hóa vì lợi ích của species” thường là explanation yếu; cần individual/kin/multilevel mechanism cụ thể.

“Community cân bằng cố định nếu không có human” sai; natural disturbance và succession liên tục.

## 30. Bridge: từ interaction local tới ecosystem-scale matter và energy

Population/community chapter theo dõi số lượng organism và interaction. Nhưng ecosystem còn phải hỏi: **energy đi qua trophic level thế nào, carbon/nitrogen/phosphorus quay vòng ra sao, disturbance và climate thay process ở scale landscape/global thế nào?**

Đó là nội dung của [[01_ecosystems_biogeochemical_cycles_and_conservation]].

> **Mental model cuối chapter:** population ecology là dynamics của số lượng; community ecology là dynamics của interaction. Behavior nối decision của individual với fitness, còn food web nối nhiều population thành network. Mọi level đều có feedback, trade-off và constraint.