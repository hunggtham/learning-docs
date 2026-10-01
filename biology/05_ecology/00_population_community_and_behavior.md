# Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**. Route đi từ kích thước/cấu trúc quần thể → tăng trưởng và giới hạn → cạnh tranh, cộng sinh, săn mồi → hành vi, mạng tương tác và động lực quần xã, để số lượng luôn được giải thích cùng quan hệ sinh thái.

Sau organismal biology, ta đã có một cá thể có physiology, hành vi (behavior / 동작) và reproduction. Nhưng ngoài tự nhiên, cá thể luôn chịu tài nguyên (resource / 자원) limitation, competition, predator, pathogen, mate choice và variation của môi trường. Vì vậy cấp tổ chức tiếp theo là **quần thể (population)** và **quần xã (community)**.

> **Mô hình tư duy:** ecology nghiên cứu tương tác (interaction / 상호작용) dưới ràng buộc (constraint / 제약조건). Population growth phụ thuộc birth, death, immigration và emigration; community cấu trúc (structure / 구조) xuất hiện từ nhiều tương tác (interaction / 상호작용) đồng thời; hành vi (behavior / 동작) là cầu nối từ physiology của cá thể tới fitness và cuối cùng tới population dynamics.

## 1. Kích thước quần thể không đủ để mô tả quần thể

Một quần thể được mô tả không chỉ bởi số cá thể \(N\), mà còn bởi density, age cấu trúc (structure / 구조), sex ratio, spatial phân phối (distribution / 분포) và genetic composition.

Hai quần thể cùng \(N\) có thể có tương lai rất khác nếu một bên chủ yếu là juvenile còn bên kia chủ yếu là cá thể già. Vì vậy demography luôn cần hỏi **ai đang sống trong quần thể**, không chỉ “có bao nhiêu cá thể”.

> **Chuyển mạch:** Population không chỉ là size mà còn age structure, density và distribution; exponential growth là baseline, rồi doubling time cho biết tốc độ trước khi density dependence giới hạn.

## 2. Tăng trưởng theo hàm mũ: baseline khi giới hạn chưa chi phối mạnh

Nếu tốc độ tăng trưởng bình quân trên mỗi cá thể gần như không đổi:

\[
\frac{dN}{dt}=rN
\]

thì:

\[
N(t)=N_0e^{rt}
\]

Population càng lớn càng tạo nhiều offspring, nên mô hình có phản hồi (feedback / 피드백) dương. Nó có thể phù hợp trong giai đoạn đầu của culture vi sinh hoặc quần thể xâm nhập habitat mới, nhưng không thể kéo dài vô hạn vì tài nguyên (resource / 자원) và không gian (space / 공간) hữu hạn.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **2. Tăng trưởng theo hàm mũ: baseline khi giới hạn chưa chi phối mạnh** đã nêu tiêu chí phân biệt, còn **3. Thời gian nhân đôi** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **4. Logistic growth và sức chứa môi trường** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Thời gian nhân đôi

Với tăng trưởng mũ:

\[
t_d=\frac{\ln 2}{r}
\]

Công thức cho thấy quan hệ (relation / 관계) giữa tỷ lệ (rate / 비율) và thời gian nhân đôi là nghịch đảo theo logarithm, không phải intuition tuyến tính đơn giản.

> **Chuyển mạch:** Doubling time describes early exponential growth; logistic growth adds carrying capacity, then density-dependent and density-independent feedback explain deviations.

## 4. Logistic growth và sức chứa môi trường

Khi density tăng, tài nguyên (resource / 자원) trên mỗi cá thể giảm hoặc competition/pathogen tăng. Mô hình logistic biểu diễn điều đó bằng:

\[
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
\]

\(K\) là **sức chứa môi trường (carrying capacity)** trong điều kiện đang xét, không phải số cố định vĩnh viễn của loài. Climate, habitat, predator và tài nguyên (resource / 자원) có thể làm \(K\) thay đổi theo thời gian.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **5. phản hồi (feedback / 피드백) phụ thuộc mật độ và nhiễu không phụ thuộc mật độ** tiếp nhận điểm tựa từ **4. Logistic growth và sức chứa môi trường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Life-history sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. phản hồi (feedback / 피드백) phụ thuộc mật độ và nhiễu không phụ thuộc mật độ

Competition, disease transmission và tài nguyên (resource / 자원) shortage thường mạnh hơn khi density cao nên tạo **phụ thuộc mật độ (density dependence)**. Storm, fire hoặc freeze có thể gây tác động lớn mà không phụ thuộc trực tiếp vào density ban đầu.

Trong hệ thực, hai loại tác động thường tương tác. Một drought có thể giảm tài nguyên (resource / 자원), rồi density dependence quyết định cá thể nào sống sót tốt hơn sau đó.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **6. Life-history sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **5. phản hồi (feedback / 피드백) phụ thuộc mật độ và nhiễu không phụ thuộc mật độ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Survivorship curve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Life-history sự đánh đổi (trade-off / 트레이드오프)

Sinh vật có tài nguyên (resource / 자원) hữu hạn cho growth, maintenance và reproduction. Đầu tư mạnh vào một chức năng thường làm giảm khả năng đầu tư vào chức năng khác.

Loài sinh nhiều offspring nhỏ với parental care thấp và loài sinh ít offspring nhưng đầu tư cao là hai chiến lược khác nhau dưới mẫu (pattern / 패턴) mortality và môi trường (environment / 환경) khác nhau. Không có một chiến lược (strategy / 전략) tối ưu chung cho mọi hệ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **7. Survivorship curve** tiếp nhận điểm tựa từ **6. Life-history sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Metapopulation: persistence có thể nằm ở mạng patch thay vì một quần thể duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Survivorship curve

Survivorship curve là mô hình tóm tắt cách mortality phân bố theo tuổi. kiểu (type / 타입) I có mortality thấp ở đầu đời và tăng mạnh khi già; kiểu (type / 타입) II gần tương đối đều; kiểu (type / 타입) III có mortality rất cao ở giai đoạn sớm nhưng cá thể sống sót có thể sống lâu.

Các kiểu (type / 타입) là mẫu (pattern / 패턴) lý tưởng hóa, hữu ích khi nối demography với life-history chiến lược (strategy / 전략) chứ không phải nhãn cứng cho mọi species.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **8. Metapopulation: persistence có thể nằm ở mạng patch thay vì một quần thể duy nhất** tiếp nhận điểm tựa từ **7. Survivorship curve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Hành vi nối physiology với fitness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Metapopulation: persistence có thể nằm ở mạng patch thay vì một quần thể duy nhất

Trong habitat phân mảnh, loài có thể tồn tại dưới dạng nhiều cục bộ (local / 로컬) population nối nhau bằng di chuyển (migration / 마이그레이션). Một patch có thể extinction cục bộ rồi được recolonize từ patch khác.

Persistence toàn hệ phụ thuộc balance giữa extinction, colonization và connectivity. Đây là cơ sở sinh học cho việc đánh giá corridor và fragmentation trong conservation.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **9. Hành vi nối physiology với fitness** tiếp nhận điểm tựa từ **8. Metapopulation: persistence có thể nằm ở mạng patch thay vì một quần thể duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Bẩm sinh và học được là hai đầu của một continuum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Hành vi nối physiology với fitness

**Hành vi (behavior / 행동)** là đầu ra (output / 출력) của nervous hệ thống (system / 시스템), endocrine trạng thái (state / 상태), development, học tập (learning / 학습) và môi trường (environment / 환경). hành vi (behavior / 동작) có thể có thành phần di truyền nhưng thường rất plastic.

Selection chỉ tác động lên hành vi (behavior / 동작) qua hậu quả sinh sản của nó. Một phản ứng giúp cá thể kiếm thức ăn tốt hơn, tránh predator hoặc tìm mate có thể tăng fitness; cùng hành vi (behavior / 동작) trong môi trường (environment / 환경) khác có thể trở thành chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **10. Bẩm sinh và học được là hai đầu của một continuum** tiếp nhận điểm tựa từ **9. Hành vi nối physiology với fitness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Kiếm ăn là bài toán năng lượng dưới rủi ro** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Bẩm sinh và học được là hai đầu của một continuum

Birdsong, điều hướng (navigation / 내비게이션) hay fear phản hồi (response / 응답) thường có predisposition di truyền nhưng cần experience để hoàn thiện. học tập (learning / 학습) cho phép cá thể cập nhật chính sách (policy / 정책) trong đời nhanh hơn evolution qua generation.

Plasticity này có chi phí (cost / 비용): nervous hệ thống (system / 시스템), thời gian học và nguy cơ học sai đều tiêu tài nguyên (resource / 자원). Selection vì vậy có thể favor mức linh hoạt khác nhau tùy môi trường (environment / 환경) ổn định hay biến động.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **11. Kiếm ăn là bài toán năng lượng dưới rủi ro** tiếp nhận điểm tựa từ **10. Bẩm sinh và học được là hai đầu của một continuum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Lãnh thổ chỉ có lợi khi lợi ích vượt chi phí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Kiếm ăn là bài toán năng lượng dưới rủi ro

**Mô hình kiếm ăn tối ưu (optimal foraging)** hỏi chiến lược (strategy / 전략) nào cân bằng năng lượng (energy / 에너지)/nutrient gain với thời gian tìm kiếm, xử lý thức ăn và nguy cơ bị săn mồi.

Nó không giả định animal “tính toán calculus” có ý thức. mô hình (model / 모델) dự đoán mẫu (pattern / 패턴) selection có thể favor dưới ràng buộc (constraint / 제약조건). Nếu xã hội (social / 사회적) học tập (learning / 학습), nutrient chất lượng (quality / 품질) hay rủi ro (risk / 위험) thay đổi, prediction của mô hình (model / 모델) đơn giản cũng thay.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **12. Lãnh thổ chỉ có lợi khi lợi ích vượt chi phí** tiếp nhận điểm tựa từ **11. Kiếm ăn là bài toán năng lượng dưới rủi ro** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Hành vi hợp tác cần cơ chế duy trì trước cheating** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Lãnh thổ chỉ có lợi khi lợi ích vượt chi phí

Giữ territory có thể bảo vệ food hoặc mate nhưng tốn năng lượng (energy / 에너지), thời gian và nguy cơ injury. Territoriality vì vậy xuất hiện khi tài nguyên (resource / 자원) đủ quan trọng và đủ “bảo vệ được”.

Đây là cùng lô-gic (logic / 논리) sự đánh đổi (trade-off / 트레이드오프) đã gặp ở physiology: điều khiển (control / 제어) mang lợi ích nhưng luôn có chi phí (cost / 비용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **12. Lãnh thổ chỉ có lợi khi lợi ích vượt chi phí** xác định đầu vào; **13. Hành vi hợp tác cần cơ chế duy trì trước cheating** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. Ổ sinh thái là không gian điều kiện và tài nguyên (resource / 자원), không chỉ là nơi sống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Hành vi hợp tác cần cơ chế duy trì trước cheating

Một hành vi (behavior / 동작) giảm reproduction trực tiếp của actor nhưng tăng reproduction của họ hàng có thể được mô hình hóa bằng **Hamilton’s quy tắc (rule / 규칙)**:

\[
rB>C
\]

trong đó \(r\) là mức relatedness, \(B\) là lợi ích cho recipient và \(C\) là chi phí (cost / 비용) cho actor.

Với cá thể không họ hàng, cooperation có thể được duy trì khi tương tác (interaction / 상호작용) lặp lại, cheating bị phát hiện, partner được lựa chọn hoặc lợi ích tức thời đủ lớn. Game lý thuyết (theory / 이론) giúp mô hình hóa những điều kiện này, nhưng kết quả (outcome / 결과) thật còn phụ thuộc physiology, bộ nhớ (memory / 메모리) và population cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, cơ chế trong **13. Hành vi hợp tác cần cơ chế duy trì trước cheating** cần được kiểm chứng bằng dấu vết cụ thể; **14. Ổ sinh thái là không gian điều kiện và tài nguyên (resource / 자원), không chỉ là nơi sống** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **15. Cạnh tranh và phân chia tài nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Ổ sinh thái là không gian điều kiện và tài nguyên (resource / 자원), không chỉ là nơi sống

**Ổ sinh thái (ecological niche / 생태적 지위)** gồm loại tài nguyên (resource / 자원) dùng, nhiệt độ/độ ẩm chịu được, thời gian hoạt động và quan hệ với species khác.

**Ổ cơ bản (fundamental niche)** là vùng có thể tồn tại nếu bỏ bớt biotic tương tác (interaction / 상호작용); **ổ thực tế (realized niche)** là phần còn lại sau competition, predation, mutualism và dispersal limitation.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **14. Ổ sinh thái là không gian điều kiện và tài nguyên (resource / 자원), không chỉ là nơi sống** nêu điều cần giải thích; **15. Cạnh tranh và phân chia tài nguyên** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Predator–prey là hai phương trình phản hồi (feedback / 피드백) ghép với nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Cạnh tranh và phân chia tài nguyên

Hai species dùng cùng tài nguyên (resource / 자원) giới hạn sẽ ảnh hưởng fitness của nhau. Competition có thể gián tiếp qua khai thác tài nguyên (resource / 자원) hoặc trực tiếp qua interference.

Nếu niche gần như trùng hoàn toàn trong môi trường (environment / 환경) ổn định, coexistence lâu dài khó hơn. Nhưng heterogeneity theo không gian (space / 공간)/thời gian (time / 시간), sự đánh đổi (trade-off / 트레이드오프) và **phân chia tài nguyên (resource partitioning)** có thể tạo coexistence.

Điều quan trọng là mẫu (pattern / 패턴) quan sát không tự nói direction nhân quả: species có thể chia niche vì evolution sau competition, hoặc vốn khác niche từ trước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **16. Predator–prey là hai phương trình phản hồi (feedback / 피드백) ghép với nhau** tiếp nhận điểm tựa từ **15. Cạnh tranh và phân chia tài nguyên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Functional phản hồi (response / 응답) tạo giới hạn cho tốc độ predator ăn prey** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Predator–prey là hai phương trình phản hồi (feedback / 피드백) ghép với nhau

Mô hình Lotka–Volterra cơ bản:

\[
\frac{dN}{dt}=rN-aNP
\]

\[
\frac{dP}{dt}=baNP-mP
\]

Prey làm predator tăng; predator lại làm prey giảm. Delay giữa hai phản hồi (response / 응답) có thể tạo dao động. Hệ thực còn có carrying sức chứa (capacity / 용량), refuge, alternative prey, seasonality và evolution của defense/attack.

Mục tiêu của equation không phải thuộc công thức mà thấy rằng hai population là một **hệ động (dynamic system / 동적 시스템) coupled by tương tác (interaction / 상호작용)**.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **16. Predator–prey là hai phương trình phản hồi (feedback / 피드백) ghép với nhau** đã nêu tiêu chí phân biệt, còn **17. Functional phản hồi (response / 응답) tạo giới hạn cho tốc độ predator ăn prey** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **18. Mutualism, commensalism và parasitism là kết quả (outcome / 결과), không phải bản chất bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Functional phản hồi (response / 응답) tạo giới hạn cho tốc độ predator ăn prey

Predator không thể ăn vô hạn khi prey density tăng vì phải tìm, bắt, xử lý và tiêu hóa. Holling kiểu (type / 타입) II bão hòa khi handling thời gian (time / 시간) trở thành bottleneck; kiểu (type / 타입) III có dạng sigmoid khi prey hiếm khó tìm hoặc predator chuyển sang prey khác.

Hình dạng phản hồi (response / 응답) ảnh hưởng stability của cả hệ. Một chi tiết ở hành vi (behavior / 동작)/physiology của predator vì vậy có thể thay population dynamics.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **17. Functional phản hồi (response / 응답) tạo giới hạn cho tốc độ predator ăn prey** đã nêu tiêu chí phân biệt, còn **18. Mutualism, commensalism và parasitism là kết quả (outcome / 결과), không phải bản chất bất biến** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **19. Loài chủ chốt và thác dinh dưỡng cho thấy tác động (effect / 효과) không tỷ lệ với abundance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Mutualism, commensalism và parasitism là kết quả (outcome / 결과), không phải bản chất bất biến

Dấu +/−/0 là cách tóm tắt tác động (effect / 효과) lên fitness. Nhưng tương tác (interaction / 상호작용) có thể đổi theo môi trường (environment / 환경). Mycorrhiza giúp plant nhận phosphorus nhưng lấy carbon; khi phosphorus dồi dào, lợi ích ròng có thể giảm.

Do đó phải hỏi cơ chế (mechanism / 메커니즘) trao đổi tài nguyên (resource / 자원) và ngữ cảnh (context / 맥락) chứ không chỉ gắn nhãn relationship.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **19. Loài chủ chốt và thác dinh dưỡng cho thấy tác động (effect / 효과) không tỷ lệ với abundance** tiếp nhận điểm tựa từ **18. Mutualism, commensalism và parasitism là kết quả (outcome / 결과), không phải bản chất bất biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Lưới thức ăn là mạng dòng năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Loài chủ chốt và thác dinh dưỡng cho thấy tác động (effect / 효과) không tỷ lệ với abundance

Một **loài chủ chốt (keystone species)** có thể ít biomass nhưng tác động lớn lên community. Predator giảm herbivore; herbivore giảm vegetation; thay predator vì vậy có thể tạo **thác dinh dưỡng (trophic cascade)** qua nhiều edge gián tiếp.

Ecology cần tư duy mạng (network / 네트워크) giống cell signaling: direct tác động (effect / 효과) và indirect tác động (effect / 효과) có thể cộng, triệt tiêu hoặc đảo dấu nhau.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **20. Lưới thức ăn là mạng dòng năng lượng** tiếp nhận điểm tựa từ **19. Loài chủ chốt và thác dinh dưỡng cho thấy tác động (effect / 효과) không tỷ lệ với abundance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Sinh thái bệnh dùng cùng ngôn ngữ population dynamics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Lưới thức ăn là mạng dòng năng lượng

Hệ sinh thái thực tế không phải food chuỗi (chain / 사슬) tuyến tính. Omnivory, detritus và nhiều tuyến (route / 경로) ăn lẫn nhau tạo **lưới thức ăn (food web)**.

Ta có thể biểu diễn species/functional group bằng nút (node / 노드) và quan hệ ăn bằng edge. Topology, strength của tương tác (interaction / 상호작용) và timing phản hồi (response / 응답) quyết định disturbance lan rộng hay bị hấp thụ.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **21. Sinh thái bệnh dùng cùng ngôn ngữ population dynamics** tiếp nhận điểm tựa từ **20. Lưới thức ăn là mạng dòng năng lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Loài xâm lấn: introduction không đồng nghĩa invasion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Sinh thái bệnh dùng cùng ngôn ngữ population dynamics

Transmission phụ thuộc density/contact của host, immunity, véc-tơ (vector / 벡터) và môi trường (environment / 환경). Mô hình SIR chia population thành susceptible–infectious–recovered để theo dõi dòng cá thể giữa các trạng thái.

Một pathogen vì vậy vừa là vấn đề molecular/immune vừa là population tiến trình (process / 프로세스). Biology liên tục đổi quy mô (scale / 규모) nhưng giữ cùng lô-gic (logic / 논리) luồng (flow / 흐름) + chuyển tiếp (transition / 전이) + phản hồi (feedback / 피드백).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **22. Loài xâm lấn: introduction không đồng nghĩa invasion** tiếp nhận điểm tựa từ **21. Sinh thái bệnh dùng cùng ngôn ngữ population dynamics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Diễn thế quần xã là trajectory có lịch sử (history / 이력) dependence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Loài xâm lấn: introduction không đồng nghĩa invasion

Một introduced species chỉ trở thành invasive khi propagule đủ, môi trường (environment / 환경) phù hợp, growth vượt mortality và tương tác (interaction / 상호작용) mới không giữ population dưới ngưỡng.

Management hiệu quả phải nhắm cơ chế (mechanism / 메커니즘): reproduction, dispersal, tài nguyên (resource / 자원) subsidy hoặc disturbance, thay vì chỉ loại từng cá thể mà không đổi tiến trình (process / 프로세스).

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **23. Diễn thế quần xã là trajectory có lịch sử (history / 이력) dependence** tiếp nhận điểm tựa từ **22. Loài xâm lấn: introduction không đồng nghĩa invasion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Độ trễ và hiệu ứng Allee tạo threshold quần thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Diễn thế quần xã là trajectory có lịch sử (history / 이력) dependence

Sau disturbance, composition của community đổi qua thời gian. Primary succession bắt đầu nơi gần như chưa có soil/biological legacy; secondary succession giữ lại nhiều cấu trúc và seed/microbe cũ.

Succession không nhất thiết đi một đường cố định tới một “climax” duy nhất. Priority tác động (effect / 효과), stochastic colonization, disturbance mới và phản hồi (feedback / 피드백) soil–plant có thể tạo trajectory khác nhau.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **24. Độ trễ và hiệu ứng Allee tạo threshold quần thể** tiếp nhận điểm tựa từ **23. Diễn thế quần xã là trajectory có lịch sử (history / 이력) dependence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Quần thể có cấu trúc: cùng N nhưng tương lai khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Độ trễ và hiệu ứng Allee tạo threshold quần thể

Logistic mô hình (model / 모델) giả định density phản hồi (feedback / 피드백) gần tức thời. Trong hệ thật, maturation, reproduction và tài nguyên (resource / 자원) regeneration có delay, nên population có thể overshoot rồi crash hoặc dao động.

Ở density thấp, **hiệu ứng Allee (Allee effect)** có thể làm growth per capita giảm vì khó tìm mate, mất cooperative defense hoặc pollination kém. Dưới một threshold, population có thể tiếp tục suy giảm dù tài nguyên (resource / 자원) còn nhiều.

Đây là lý do conservation không thể chỉ hỏi “còn bao nhiêu cá thể” mà phải hỏi cấu trúc tuổi, connectivity và vị trí so với threshold phục hồi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **25. Quần thể có cấu trúc: cùng N nhưng tương lai khác nhau** tiếp nhận điểm tựa từ **24. Độ trễ và hiệu ứng Allee tạo threshold quần thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Stability là thuộc tính (property / 속성) của mạng (network / 네트워크), không phải chỉ của số species** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Quần thể có cấu trúc: cùng N nhưng tương lai khác nhau

Một population 1.000 cá thể gần hết tuổi sinh sản và một population 1.000 juvenile không có trajectory giống nhau. **Ma trận chiếu quần thể (population projection matrix)** dùng survival, chuyển tiếp (transition / 전이) giữa stage và fecundity để dự đoán trạng thái (state / 상태) tương lai.

Nếu stress chủ yếu làm giảm juvenile survival, tác động (effect / 효과) lên số adult có thể chỉ xuất hiện vài năm sau. Delay giữa cơ chế (mechanism / 메커니즘) và abundance quan sát được là vấn đề lớn trong conservation monitoring.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **26. Stability là thuộc tính (property / 속성) của mạng (network / 네트워크), không phải chỉ của số species** tiếp nhận điểm tựa từ **25. Quần thể có cấu trúc: cùng N nhưng tương lai khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Eco-evolutionary phản hồi (feedback / 피드백): ecology đổi selection, evolution lại đổi ecology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Stability là thuộc tính (property / 속성) của mạng (network / 네트워크), không phải chỉ của số species

Weak tương tác (interaction / 상호작용), refuge, spatial heterogeneity và phản hồi (response / 응답) không đồng bộ có thể làm disturbance khó lan đồng loạt. Ngược lại, tương tác (interaction / 상호작용) mạnh cùng hướng có thể khuếch đại collapse.

Biodiversity có thể tăng functional redundancy trong một số hệ, nhưng “nhiều species = luôn ổn định hơn” là phát biểu quá đơn giản. Cần biết role và liên kết (connection / 연결) của chúng.

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **27. Eco-evolutionary phản hồi (feedback / 피드백): ecology đổi selection, evolution lại đổi ecology** tiếp nhận điểm tựa từ **26. Stability là thuộc tính (property / 속성) của mạng (network / 네트워크), không phải chỉ của số species** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Hai trường hợp (case / 사례) study để tránh nhân quả (causal / 인과적) story quá đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Eco-evolutionary phản hồi (feedback / 피드백): ecology đổi selection, evolution lại đổi ecology

Prey evolve defense → predator intake đổi → predator abundance đổi. Pathogen evolve transmissibility → epidemic dynamics đổi. Plant đổi flowering thời gian (time / 시간) → pollination mạng (network / 네트워크) đổi.

Vòng đầy đủ là:

```text
môi trường
→ interaction sinh thái
→ selection
→ thay đổi trait qua thế hệ
→ interaction sinh thái mới
```

Đây là cầu nối trực tiếp từ population genetics sang ecosystem dynamics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **27. Eco-evolutionary phản hồi (feedback / 피드백): ecology đổi selection, evolution lại đổi ecology** cho ta quy tắc; **28. Hai trường hợp (case / 사례) study để tránh nhân quả (causal / 인과적) story quá đơn giản** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. Các hiểu lầm cần tránh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Hai trường hợp (case / 사례) study để tránh nhân quả (causal / 인과적) story quá đơn giản

**Wolf và trophic cascade:** reintroduction predator có thể ảnh hưởng herbivore abundance/hành vi (behavior / 동작) rồi vegetation, nhưng kết quả (outcome / 결과) còn phụ thuộc climate, human hunting và predator khác. Không nên biến mạng (network / 네트워크) causality thành slogan một chiều.

**Bee pollination:** plant cung cấp nectar/pollen, pollinator hỗ trợ reproduction. Mất một pollinator có thể được species khác bù hoặc không tùy topology mạng (network / 네트워크). Vì vậy cần đo tương tác (interaction / 상호작용) mạng (network / 네트워크) chứ không chỉ đếm một species.

> **Chuyển mạch:** Trong **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **28. Hai trường hợp (case / 사례) study để tránh nhân quả (causal / 인과적) story quá đơn giản** cho ta quy tắc; **29. Các hiểu lầm cần tránh** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **30. cầu nối (bridge / 브리지): từ tương tác (interaction / 상호작용) cục bộ (local / 로컬) tới ecosystem-scale matter và năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Các hiểu lầm cần tránh

“Population luôn tiến tới K” sai; K thay đổi, phản hồi (feedback / 피드백) có delay và threshold.

“Predator luôn xấu cho ecosystem” sai; predator có thể giữ herbivore dưới mức phá hủy vegetation hoặc tạo cascade phức tạp.

“Niche = habitat” quá hẹp; niche gồm tài nguyên (resource / 자원), tolerance, timing và tương tác (interaction / 상호작용).

“Altruism tồn tại vì tốt cho species” thường thiếu cơ chế (mechanism / 메커니즘); phải xét kin selection, repeated tương tác (interaction / 상호작용) hoặc multilevel tiến trình (process / 프로세스) cụ thể.

“Community tự nhiên luôn cân bằng nếu không có người” sai; disturbance và succession là phần bình thường của ecology.

> **Mô hình tư duy:** hành vi (behavior / 동작) biến trạng thái (state / 상태) của individual thành hành động (action / 동작); hành động (action / 동작) đổi fitness và tương tác (interaction / 상호작용); tương tác (interaction / 상호작용) tạo population/community dynamics; mạng (network / 네트워크) dynamics quyết định dòng vật chất và năng lượng sẽ được xử lý thế nào ở ecosystem quy mô (scale / 규모).

> **Chuyển mạch:** Ở chặng này của **Quần thể, Quần xã và Hành vi — Population, Community and hành vi (behavior / 동작)**, **30. cầu nối (bridge / 브리지): từ tương tác (interaction / 상호작용) cục bộ (local / 로컬) tới ecosystem-scale matter và năng lượng** tiếp nhận điểm tựa từ **29. Các hiểu lầm cần tránh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 30. cầu nối (bridge / 브리지): từ tương tác (interaction / 상호작용) cục bộ (local / 로컬) tới ecosystem-scale matter và năng lượng

Quần thể/quần xã chương (chapter) theo dõi số lượng organism và tương tác (interaction / 상호작용). Nhưng ecosystem còn phải hỏi: **năng lượng đi qua bậc dinh dưỡng thế nào, carbon/nitrogen/phosphorus quay vòng ra sao, disturbance và climate thay tiến trình (process / 프로세스) ở quy mô (scale / 규모) landscape/toàn cục (global / 전역) thế nào?**

Đó là nội dung của [Hệ sinh thái, Chu trình vật chất và Bảo tồn](01_ecosystems_biogeochemical_cycles_and_conservation.md).

> **Mô hình tư duy cuối chapter:** sinh thái học quần thể (population ecology) là dynamics của số lượng; sinh thái học quần xã (community ecology) là dynamics của tương tác (interaction / 상호작용). hành vi (behavior / 동작) nối quyết định (decision / 결정) của individual với fitness, còn lưới thức ăn nối nhiều population thành mạng (network / 네트워크). Mọi mức (level / 수준) đều có phản hồi (feedback / 피드백), sự đánh đổi (trade-off / 트레이드오프) và ràng buộc.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Quản lý nguy cơ, phòng bệnh và tự theo dõi sức khỏe](../04_organismal_biology/06_health_risk_prevention_and_self_monitoring.md) · [Mục lục Biology](../README.md) · [Hệ sinh thái, Chu trình vật chất và Bảo tồn →](01_ecosystems_biogeochemical_cycles_and_conservation.md)

> **Bàn giao:** Sau **30. cầu nối (bridge / 브리지): từ tương tác (interaction / 상호작용) cục bộ (local / 로컬) tới ecosystem-scale matter và năng lượng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
