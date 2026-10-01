# Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**. Route đi từ mạng tương tác → phương trình động học và tham số → mô hình, dự đoán và kiểm định → thiết kế mạch gene/hệ tổng hợp, để mô hình dẫn tới thí nghiệm thay vì chỉ tạo sơ đồ đẹp.

Khi đã đo hàng nghìn gene, protein và metabolite, một giới hạn mới xuất hiện: **biết danh sách thành phần (component / 컴포넌트) không đồng nghĩa hiểu hành vi (behavior / 동작) của hệ thống (system / 시스템)**. Một signaling mạng (network / 네트워크) có thể tạo công tắc (switch), oscillation hoặc adaptation tùy phản hồi (feedback / 피드백). Hai gene có thể gần như không gây phenotype khi perturb riêng nhưng gây tác động (effect / 효과) rất lớn khi perturb cùng nhau. Một metabolite có concentration gần như không đổi dù dòng chuyển hóa (flux) qua pathway tăng nhiều lần.

**Sinh học hệ thống (systems biology / 시스템 생물학)** tập trung vào tương tác (interaction / 상호작용), dynamics và nổi trội (emergent) hành vi (behavior / 동작). **Sinh học tổng hợp (synthetic biology / 합성생물학)** đi thêm một bước: dùng hiểu biết về hệ thống (system / 시스템) để thiết kế circuit hoặc metabolic trạng thái (state / 상태) mới.

> **mô hình tư duy (mental model / 사고 모델):** sinh học phân tử (molecular biology) hỏi “part này làm gì?”. Sinh học hệ thống hỏi “mạng (network / 네트워크) của nhiều part tạo dynamics gì?”. Sinh học tổng hợp hỏi “nếu thay topology hoặc parameter, ta có tạo hành vi (behavior / 동작) dự đoán được không?”.

## 1. mạng (network / 네트워크) diagram chưa phải mô hình động (dynamic model / 동적 모델)

Một pathway A → B → C chỉ nói direction tương tác. Nó chưa nói tỷ lệ (rate / 비율), delay, bão hòa (saturation), định vị (localization) hay phân giải (degradation).

Nếu A activate B rất chậm còn B degrade rất nhanh, hành vi (behavior / 동작) khác hẳn khi activation nhanh và degradation chậm. Vì vậy topology là skeleton; dynamics cần parameter.

Điểm này rất quan trọng khi đọc pathway figure: arrow là hypothesis về quan hệ (relation / 관계), không phải full prediction.

> **Chuyển mạch:** Network diagram shows topology, not dynamics; rates turn edges into changing biology, while a steady state can persist far from thermodynamic equilibrium.

## 2. tỷ lệ (rate / 비율) of thay đổi (change / 변경) là ngôn ngữ tự nhiên của động (dynamic / 동적) biology

Nếu B được tạo theo A và degraded theo B hiện tại:

\[
\frac{dB}{dt}=k_{on}A-k_{off}B
\]

Equation không chỉ là toán. Nó buộc ta phát biểu rõ: môi trường vận hành (production / 운영 환경) phụ thuộc gì, mất mát (loss / 손실) phụ thuộc gì, variable nào thay đổi theo thời gian (time / 시간).

Khi \(dB/dt=0\), B ở **trạng thái ổn định (steady state)**, nhưng môi trường vận hành (production / 운영 환경) và degradation vẫn có thể diễn ra liên tục.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **3. Trạng thái ổn định không đồng nghĩa cân bằng nhiệt động (thermodynamic equilibrium)** tiếp nhận điểm tựa từ **2. tỷ lệ (rate / 비율) of thay đổi (change / 변경) là ngôn ngữ tự nhiên của động (dynamic / 동적) biology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Sự tạo ra (production)–phân giải mô hình (model / 모델) và hằng số thời gian (time constant)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Trạng thái ổn định không đồng nghĩa cân bằng nhiệt động (thermodynamic equilibrium)

Cell sống thường duy trì **non-equilibrium trạng thái ổn định**. ATP được tạo và tiêu thụ liên tục. Ion được pump ra rồi leak vào. Glucose blood có thể gần ổn định dù uptake và bản phát hành (release / 릴리스) xảy ra liên tục.

Cân bằng nhiệt động thực sự sẽ làm nhiều độ dốc (gradient / 기울기) collapse. Life cần dòng năng lượng (energy flow) để giữ hệ thống (system / 시스템) xa equilibrium.

Đây là liên kết (connection / 연결) trực tiếp giữa thermodynamics và cân bằng nội môi (homeostasis).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **4. Sự tạo ra (production)–phân giải mô hình (model / 모델) và hằng số thời gian (time constant)** tiếp nhận điểm tựa từ **3. Trạng thái ổn định không đồng nghĩa cân bằng nhiệt động (thermodynamic equilibrium)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Saturation làm phản hồi (response / 응답) nonlinear** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Sự tạo ra (production)–phân giải mô hình (model / 모델) và hằng số thời gian (time constant)

Mô hình (model / 모델) đơn giản:

\[
\frac{dX}{dt}=\alpha-\beta X
\]

Trạng thái ổn định:

\[
X^*=\frac{\alpha}{\beta}
\]

Nhưng còn một thông tin (information / 정보) khác: tốc độ hệ thống (system / 시스템) tiến tới trạng thái ổn định phụ thuộc \(\beta\). Molecule degrade nhanh phản ứng nhanh hơn với thay đổi (change / 변경), nhưng phải tốn năng lượng (energy / 에너지) để resynthesize liên tục.

Biology thường sự đánh đổi (trade-off / 트레이드오프) **responsiveness vs tài nguyên (resource / 자원) chi phí (cost / 비용)**.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **5. Saturation làm phản hồi (response / 응답) nonlinear** tiếp nhận điểm tựa từ **4. Sự tạo ra (production)–phân giải mô hình (model / 모델) và hằng số thời gian (time constant)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Phản hồi âm (negative feedback) tạo stability nhưng có thể tạo dao động (oscillation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Saturation làm phản hồi (response / 응답) nonlinear

Enzym (enzyme), receptor và transporter có sức chứa (capacity / 용량) hữu hạn. Michaelis–Menten-like quan hệ (relation / 관계):

\[
v=\frac{V_{max}[S]}{K_m+[S]}
\]

Ở substrate thấp, phản hồi (response / 응답) gần tuyến tính (linear / 선형). Ở cao, hệ thống (system / 시스템) saturate.

Tính phi tuyến (nonlinearity) là nền cho ngưỡng (threshold), ultrasensitivity và công tắc. Nếu cứ giả định quan hệ (relation / 관계) tuyến tính, ta sẽ bỏ lỡ nhiều hành vi (behavior / 동작) quan trọng.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **6. Phản hồi âm (negative feedback) tạo stability nhưng có thể tạo dao động (oscillation)** tiếp nhận điểm tựa từ **5. Saturation làm phản hồi (response / 응답) nonlinear** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Phản hồi dương (positive feedback) tạo bộ nhớ (memory / 메모리) và tính lưỡng ổn (bistability)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Phản hồi âm (negative feedback) tạo stability nhưng có thể tạo dao động (oscillation)

Phản hồi âm làm đầu ra (output / 출력) giảm upstream drive. Metabolic end sản phẩm (product / 제품) inhibit enzyme đầu; glucose–insulin regulation giảm deviation; gene sản phẩm (product / 제품) có thể repress transcription của chính nó.

Phản hồi (feedback / 피드백) giúp disturbance decay nhanh hơn và giảm variation. Nhưng nếu phản hồi (feedback / 피드백) có delay lớn hoặc gain quá mạnh, hệ thống (system / 시스템) có thể overshoot và oscillate.

Lý thuyết điều khiển (control theory) giúp ta thấy stability không chỉ phụ thuộc “có phản hồi hay không” mà cả strength và delay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **7. Phản hồi dương (positive feedback) tạo bộ nhớ (memory / 메모리) và tính lưỡng ổn (bistability)** tiếp nhận điểm tựa từ **6. Phản hồi âm (negative feedback) tạo stability nhưng có thể tạo dao động (oscillation)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Hiện tượng trễ (hysteresis): threshold bật và threshold tắt có thể khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Phản hồi dương (positive feedback) tạo bộ nhớ (memory / 메모리) và tính lưỡng ổn (bistability)

Nếu X kích hoạt môi trường vận hành (production / 운영 환경) của chính nó, hệ thống (system / 시스템) có thể có hai stable trạng thái (state / 상태): low và high.

Một transient tín hiệu (signal / 신호) có thể đẩy hệ thống (system / 시스템) qua ngưỡng, sau đó high trạng thái (state / 상태) tự duy trì. Đây là **tính lưỡng ổn (쌍안정성)**.

Biệt hóa tế bào (cell differentiation) và tế bào (cell)-cycle chuyển tiếp (transition / 전이) thường có công tắc-like motif. Phản hồi dương biến graded đầu vào (input / 입력) thành discrete quyết định (decision / 결정).

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **8. Hiện tượng trễ (hysteresis): threshold bật và threshold tắt có thể khác nhau** tiếp nhận điểm tựa từ **7. Phản hồi dương (positive feedback) tạo bộ nhớ (memory / 메모리) và tính lưỡng ổn (bistability)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Feed-forward vòng lặp (loop / 루프) tạo filter thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Hiện tượng trễ (hysteresis): threshold bật và threshold tắt có thể khác nhau

Trong bistable hệ thống (system / 시스템), đầu vào (input / 입력) cần để bật trạng thái (state / 상태) high có thể cao hơn đầu vào (input / 입력) cần để giữ trạng thái (state / 상태) high. Khi giảm đầu vào (input / 입력), hệ thống (system / 시스템) không quay lại ngay đường cũ.

Đây là **hiện tượng trễ**, cùng concept đã gặp ở ecosystem alternative states. Một motif mathematical có thể xuất hiện từ gene circuit đến lake ecology.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **9. Feed-forward vòng lặp (loop / 루프) tạo filter thời gian** tiếp nhận điểm tựa từ **8. Hiện tượng trễ (hysteresis): threshold bật và threshold tắt có thể khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Oscillator cần phản hồi (feedback / 피드백) + delay + tính phi tuyến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Feed-forward vòng lặp (loop / 루프) tạo filter thời gian

Nếu A activate C trực tiếp và cũng activate B, còn B activate C, C có thể yêu cầu tín hiệu (signal / 신호) A tồn tại đủ lâu để cả hai đường dẫn (path / 경로) cùng active.

Coherent feed-forward vòng lặp (loop / 루프) vì vậy có thể lọc pulse ngắn.

Mạng lưới (network) topology tự thực hiện computation về duration mà không cần central processor.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **10. Oscillator cần phản hồi (feedback / 피드백) + delay + tính phi tuyến** tiếp nhận điểm tựa từ **9. Feed-forward vòng lặp (loop / 루프) tạo filter thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Tính ngẫu nhiên (stochasticity): khi molecule count thấp, average không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Oscillator cần phản hồi (feedback / 피드백) + delay + tính phi tuyến

Nhịp sinh học ngày đêm (circadian rhythm), tế bào-cycle oscillator và many mạch sinh học tổng hợp (synthetic circuit) tạo periodic dynamics.

Phản hồi âm với delay có thể làm đầu ra (output / 출력) lên xuống. Phản hồi dương có thể sharpen chuyển tiếp (transition / 전이). Degradation tỷ lệ (rate / 비율) quyết định period.

Snapshot omics ở một thời gian (time / 시간) điểm (point / 지점) có thể bỏ hoàn toàn phase thông tin (information / 정보); time-series vì vậy quan trọng khi hệ thống (system / 시스템) oscillatory.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **11. Tính ngẫu nhiên (stochasticity): khi molecule count thấp, average không đủ** tiếp nhận điểm tựa từ **10. Oscillator cần phản hồi (feedback / 피드백) + delay + tính phi tuyến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Population average có thể che tính lưỡng ổn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Tính ngẫu nhiên (stochasticity): khi molecule count thấp, average không đủ

Nếu chỉ có vài yếu tố phiên mã (transcription factor) phân tử (molecule), reaction sự kiện (event / 이벤트) riêng lẻ gây fluctuation lớn. Continuous ODE approximation có thể không capture phân phối (distribution / 분포).

**Stochastic mô hình (model / 모델)** mô tả reaction sự kiện (event / 이벤트) probabilistically. Gillespie-style simulation chọn sự kiện (event / 이벤트) và thời gian dựa trên propensity.

Noise có thể làm genetically identical cell vào trạng thái (state / 상태) khác nhau. Trong bacterial persistence hoặc developmental fate, tính ngẫu nhiên có functional consequence.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **12. Population average có thể che tính lưỡng ổn** tiếp nhận điểm tựa từ **11. Tính ngẫu nhiên (stochasticity): khi molecule count thấp, average không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Phân tích độ nhạy (sensitivity analysis): parameter nào thật sự kiểm soát đầu ra (output / 출력)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Population average có thể che tính lưỡng ổn

Nếu nửa cell OFF và nửa ON, bulk đo lường (measurement / 측정) có thể cho average 50%. Nhưng không cell nào thật sự ở 50% trạng thái (state / 상태).

Single-tế bào đo lường (measurement / 측정) vì vậy cần thiết để phân biệt continuous shift với mixture trạng thái (state / 상태).

Đây là cầu nối (bridge / 브리지) giữa sinh học hệ thống và đo tế bào dòng chảy (flow cytometry)/single-cell omics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **13. Phân tích độ nhạy (sensitivity analysis): parameter nào thật sự kiểm soát đầu ra (output / 출력)?** tiếp nhận điểm tựa từ **12. Population average có thể che tính lưỡng ổn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Identifiability: fit tốt không nghĩa parameter đúng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Phân tích độ nhạy (sensitivity analysis): parameter nào thật sự kiểm soát đầu ra (output / 출력)?

Mô hình (model / 모델) có hàng chục parameter. **Phân tích độ nhạy** hỏi đầu ra (output / 출력) thay đổi bao nhiêu khi parameter thay đổi.

Nếu small thay đổi (change / 변경) ở parameter A làm đầu ra (output / 출력) đổi lớn, A là sensitive điều khiển (control / 제어) điểm (point / 지점). Nếu hành vi (behavior / 동작) robust qua phạm vi (range / 범위) rộng, hệ thống (system / 시스템) có tính bền vững (robustness).

Độ nhạy (sensitivity) giúp chọn experiment nào đáng làm và nút (node / 노드) nào có tiềm năng intervention.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **14. Identifiability: fit tốt không nghĩa parameter đúng** tiếp nhận điểm tựa từ **13. Phân tích độ nhạy (sensitivity analysis): parameter nào thật sự kiểm soát đầu ra (output / 출력)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Overfitting cũng tồn tại trong mô hình cơ chế (mechanistic model)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Identifiability: fit tốt không nghĩa parameter đúng

Nhiều combination parameter có thể tạo curve giống nhau. Đây là **khả năng nhận dạng tham số (parameter identifiability) vấn đề (problem) (매개변수 식별성)**.

Mô hình (model / 모델) có thể fit dữ liệu (data / 데이터) đẹp nhưng individual parameter không uniquely determined.

Giải pháp có thể là thêm đo lường (measurement / 측정) intermediate, perturb hệ thống (system / 시스템), dùng prior kiến thức (knowledge / 지식) hoặc simplify mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **14. Identifiability: fit tốt không nghĩa parameter đúng** xác định đầu vào; **15. Overfitting cũng tồn tại trong mô hình cơ chế (mechanistic model)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Perturbation phân biệt correlation với causality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Overfitting cũng tồn tại trong mô hình cơ chế (mechanistic model)

Thêm nhiều parameter gần như luôn giúp fit dữ liệu huấn luyện (training data / 학습 데이터). Nhưng mô hình (model / 모델) phức tạp có thể prediction kém ở điều kiện (condition / 조건) mới.

Mô hình (model / 모델) selection cần balance fit và độ phức tạp (complexity / 복잡도). AIC/BIC, cross-validation và held-out perturbation giúp, nhưng biological plausibility vẫn quan trọng.

Mục tiêu không phải “fit mọi điểm” mà là capture cơ chế (mechanism / 메커니즘) đủ để generalize.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **15. Overfitting cũng tồn tại trong mô hình cơ chế (mechanistic model)** xác định đầu vào; **16. Perturbation phân biệt correlation với causality** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **17. Genetic tương tác (interaction / 상호작용): whole lớn hơn hoặc nhỏ hơn tổng tác động (effect / 효과) riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Perturbation phân biệt correlation với causality

Co-expression A và B không cho biết A→B, B→A hay cả hai cùng do C.

Knockout A rồi đo B tạo nhân quả (causal / 인과적) bằng chứng (evidence / 증거) mạnh hơn. Dose perturbation nhiều mức giúp infer nonlinear phản hồi (response / 응답). Time-resolved perturbation giúp infer direction.

Sinh học hệ thống mạnh nhất khi mô hình (model / 모델) tạo prediction rồi experiment perturb để cố làm prediction sai.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **17. Genetic tương tác (interaction / 상호작용): whole lớn hơn hoặc nhỏ hơn tổng tác động (effect / 효과) riêng** tiếp nhận điểm tựa từ **16. Perturbation phân biệt correlation với causality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Epistasis nối genetics cổ điển với mạng (network / 네트워크) hiện đại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Genetic tương tác (interaction / 상호작용): whole lớn hơn hoặc nhỏ hơn tổng tác động (effect / 효과) riêng

Nếu mutation A làm fitness giảm 10% và B giảm 10%, double mutant có thể không đơn giản giảm 20%.

**Genetic tương tác (interaction / 상호작용)** xảy ra khi double tác động (effect / 효과) khác expectation từ single tác động (effect / 효과).

**Synthetic lethality** là trường hợp A hoặc B riêng vẫn sống nhưng A+B chết. Đây là mạng (network / 네트워크) phụ thuộc (dependency / 의존성) quan trọng trong cancer therapy.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **18. Epistasis nối genetics cổ điển với mạng (network / 네트워크) hiện đại** tiếp nhận điểm tựa từ **17. Genetic tương tác (interaction / 상호작용): whole lớn hơn hoặc nhỏ hơn tổng tác động (effect / 효과) riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Metabolic concentration và flux không giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Epistasis nối genetics cổ điển với mạng (network / 네트워크) hiện đại

Trong classical genetics, **epistasis** mô tả alen (allele) ở gene này che hoặc thay tác động (effect / 효과) gene khác. Sinh học hệ thống diễn giải điều đó bằng pathway cấu trúc liên kết (topology).

Nếu A tạo cơ chất (substrate) cho B, mất mát (loss / 손실) A có thể làm status của B không còn matter. Kiểu hình (phenotype) mẫu (pattern / 패턴) từ cross có thể giúp suy thứ tự (order / 순서) pathway.

Một concept Mendel-era vì vậy nối trực tiếp mạng (network / 네트워크) suy luận (inference / 추론) hiện đại.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **19. Metabolic concentration và flux không giống nhau** tiếp nhận điểm tựa từ **18. Epistasis nối genetics cổ điển với mạng (network / 네트워크) hiện đại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Stoichiometric ma trận (matrix / 행렬) và Phân tích cân bằng dòng chuyển hóa (flux balance analysis)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Metabolic concentration và flux không giống nhau

Một metabolite concentration ổn định có thể có flux rất cao nếu môi trường vận hành (production / 운영 환경) và consumption cùng nhanh.

Ví dụ bathtub giữ water mức (level / 수준) constant dù faucet và drain luồng (flow / 흐름) lớn.

Do đó metabolomics đo concentration chưa đủ để biết metabolic tỷ lệ (rate / 비율). Isotope tracing và dòng chuyển hóa mô hình (model / 모델) cần khi muốn biết material thực sự đi đâu.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **20. Stoichiometric ma trận (matrix / 행렬) và Phân tích cân bằng dòng chuyển hóa (flux balance analysis)** tiếp nhận điểm tựa từ **19. Metabolic concentration và flux không giống nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. điều khiển (control / 제어) coefficient phân bố qua mạng lưới (network)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Stoichiometric ma trận (matrix / 행렬) và Phân tích cân bằng dòng chuyển hóa (flux balance analysis)

Mạng lưới chuyển hóa (metabolic network) có thể biểu diễn bằng stoichiometric ma trận (matrix / 행렬) \(S\) và flux véc-tơ (vector / 벡터) \(v\). Ở steady-state approximation:

\[
Sv=0
\]

Sau đó ràng buộc (constraint / 제약조건) đặt upper/lower bound cho dòng chuyển hóa, và tối ưu hóa (optimization / 최적화) chọn solution theo mục tiêu (objective / 목표) như biomass môi trường vận hành (production / 운영 환경).

**Phân tích cân bằng dòng chuyển hóa, FBA** mạnh vì không cần mọi kinetic parameter, nhưng mục tiêu (objective / 목표) giả định (assumption / 가정) là giới hạn (limitation). Microbe trong natural ecosystem không luôn maximize growth như lab culture.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **21. điều khiển (control / 제어) coefficient phân bố qua mạng lưới (network)** tiếp nhận điểm tựa từ **20. Stoichiometric ma trận (matrix / 행렬) và Phân tích cân bằng dòng chuyển hóa (flux balance analysis)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Multi-scale modeling: molecular trạng thái (state / 상태) phải gặp tissue hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. điều khiển (control / 제어) coefficient phân bố qua mạng lưới (network)

Một misconception cổ điển là “một enzyme rate-limiting duy nhất kiểm soát whole pathway”. Trong mạng (network / 네트워크) thật, điều khiển (control / 제어) thường phân bố.

Tăng enzyme A 10× có thể không tăng flux nếu enzyme B hoặc substrate supply trở thành bottleneck mới.

Kỹ thuật chuyển hóa (metabolic engineering) vì vậy cần các hệ thống (systems / 시스템들) view, không chỉ overexpress một gene.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **22. Multi-scale modeling: molecular trạng thái (state / 상태) phải gặp tissue hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **21. điều khiển (control / 제어) coefficient phân bố qua mạng lưới (network)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Sinh học tổng hợp: xây circuit để kiểm tra principle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Multi-scale modeling: molecular trạng thái (state / 상태) phải gặp tissue hình học (geometry / 기하학)

Tumor growth có molecular signaling trong tế bào, phân chia tế bào (cell division)/sự di chuyển (migration / 마이그레이션) ở mô (tissue), oxy (oxygen) diffusion từ vessel và immune-cell movement.

Mỗi quy mô (scale / 규모) dùng variable/thời gian (time / 시간) step khác nhau. Mô hình đa quy mô (multi-scale model) nối ODE, agent-based mô hình (model / 모델) và diffusion equation.

Khó khăn chính không chỉ computational; nó là quyết định thông tin (information / 정보) nào cần pass giữa quy mô (scale / 규모).

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **23. Sinh học tổng hợp: xây circuit để kiểm tra principle** gom các mảnh từ **22. Multi-scale modeling: molecular trạng thái (state / 상태) phải gặp tissue hình học (geometry / 기하학)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **24. Tính mô-đun (modularity) trong cell không sạch như electronics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Sinh học tổng hợp: xây circuit để kiểm tra principle

Sinh học tổng hợp dùng promoter, repressor, ribosome binding site, enzyme và sensor như mô-đun (module / 모듈).

Nếu hai repressor inhibit nhau, circuit có thể tạo toggle switch. Nếu phản hồi âm có delay, circuit có thể oscillate.

Kỹ thuật (engineering / 엔지니어링) circuit là cách mạnh để kiểm thử (test / 테스트) sufficiency: topology dự đoán có thật sự tạo hành vi (behavior / 동작) không?

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **24. Tính mô-đun (modularity) trong cell không sạch như electronics** gom các mảnh từ **23. Sinh học tổng hợp: xây circuit để kiểm tra principle** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **25. ngữ cảnh (context / 맥락) dependence là challenge central của sinh học tổng hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Tính mô-đun (modularity) trong cell không sạch như electronics

Electronic thành phần (component / 컴포넌트) có giao diện (interface / 인터페이스) khá ổn định. Biological circuit share ribosome, polymerase, ATP, axit amin (amino acid) và membrane không gian (space / 공간).

Khi synthetic construct expression quá mạnh, nó tạo **tài nguyên (resource / 자원) burden**, làm host growth giảm và indirectly thay circuit hành vi (behavior / 동작).

Vì vậy mô-đun (module / 모듈) tương tác (interaction / 상호작용) có thể tồn tại dù diagram không vẽ edge.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **25. ngữ cảnh (context / 맥락) dependence là challenge central của sinh học tổng hợp** gom các mảnh từ **24. Tính mô-đun (modularity) trong cell không sạch như electronics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **26. Kỹ thuật chuyển hóa là tối ưu hóa (optimization / 최적화) dưới ràng buộc (constraint / 제약조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. ngữ cảnh (context / 맥락) dependence là challenge central của sinh học tổng hợp

Cùng promoter có thể hoạt động khác tùy host strain, bản sao (copy / 복사) number, tốc độ tăng trưởng (growth rate) và genomic insertion site.

Biological part có lịch sử (history / 이력) và môi trường (environment / 환경). Standardization hữu ích nhưng không xóa ngữ cảnh (context / 맥락).

Điều này dạy ngược lại về natural biology: hàm (function / 함수) của gene cũng phụ thuộc mạng (network / 네트워크) bối cảnh (context).

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **26. Kỹ thuật chuyển hóa là tối ưu hóa (optimization / 최적화) dưới ràng buộc (constraint / 제약조건)** gom các mảnh từ **25. ngữ cảnh (context / 맥락) dependence là challenge central của sinh học tổng hợp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **27. Biosensor: biology như đo lường (measurement / 측정) thiết bị (device / 장치)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Kỹ thuật chuyển hóa là tối ưu hóa (optimization / 최적화) dưới ràng buộc (constraint / 제약조건)

Muốn cell tạo sản phẩm (product / 제품) P, ta có thể tăng precursor supply, knock out competing pathway, balance redox cofactor, improve transporter hoặc reduce toxicity.

Nhưng mỗi modification có sự đánh đổi (trade-off / 트레이드오프) với growth và stability.

Kỹ thuật (engineering / 엔지니어링) bài toán (problem / 문제) thường multi-objective: maximize sản phẩm (product / 제품) nhưng giữ cell sống đủ lâu và circuit không bị evolution phá nhanh.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **26. Kỹ thuật chuyển hóa là tối ưu hóa (optimization / 최적화) dưới ràng buộc (constraint / 제약조건)** nêu điều cần giải thích; **27. Biosensor: biology như đo lường (measurement / 측정) thiết bị (device / 장치)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. Tế bào-free hệ thống (system / 시스템): giảm ngữ cảnh (context / 맥락) để prototype nhanh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Biosensor: biology như đo lường (measurement / 측정) thiết bị (device / 장치)

Biosensor có đầu vào (input / 입력) mô-đun (module / 모듈) nhận molecule, processing mô-đun (module / 모듈) và đầu ra (output / 출력) như huỳnh quang (fluorescence)/electrical tín hiệu (signal / 신호).

Chỉ số (metric / 지표) gồm sensitivity, độ đặc hiệu (specificity), dải động (dynamic range), phản hồi (response / 응답) thời gian (time / 시간), leak và nhiễu (noise).

Biosensor nối experimental đo lường (measurement / 측정) với synthetic thiết kế (design / 설계): ta dùng biology để đo biology hoặc môi trường (environment / 환경).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **27. Biosensor: biology như đo lường (measurement / 측정) thiết bị (device / 장치)** nêu điều cần giải thích; **28. Tế bào-free hệ thống (system / 시스템): giảm ngữ cảnh (context / 맥락) để prototype nhanh** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **29. Evolution là một “dạng thất bại (failure mode / 실패 모드)” của engineered circuit — và cũng là thiết kế (design / 설계) áp suất (pressure)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Tế bào-free hệ thống (system / 시스템): giảm ngữ cảnh (context / 맥락) để prototype nhanh

Tế bào-free expression dùng extract hoặc purified machinery ngoài living cell. Nó bỏ ràng buộc growth và màng (membrane), dễ điều khiển (control / 제어) reagent.

Nhưng kết quả (result / 결과) không tự translate sang cell vì tài nguyên (resource / 자원) competition, degradation và compartment khác.

Tế bào-free giống simplified mô hình (model / 모델): useful để isolate principle, nhưng phải validate lại in vivo.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **29. Evolution là một “dạng thất bại (failure mode / 실패 모드)” của engineered circuit — và cũng là thiết kế (design / 설계) áp suất (pressure)** tiếp nhận điểm tựa từ **28. Tế bào-free hệ thống (system / 시스템): giảm ngữ cảnh (context / 맥락) để prototype nhanh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Digital twin và predictive biology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Evolution là một “dạng thất bại (failure mode / 실패 모드)” của engineered circuit — và cũng là thiết kế (design / 설계) áp suất (pressure)

Synthetic construct gây burden có thể bị mutation làm mất hàm (function / 함수); mutant grow nhanh hơn và chiếm population.

Do đó engineered biology phải nghĩ đến **độ ổn định tiến hóa (evolutionary stability)**. thiết kế (design / 설계) tốt không chỉ hoạt động ngày đầu mà còn phải giữ chức năng (function) qua generation.

Sinh học tổng hợp vì vậy buộc kỹ thuật (engineering / 엔지니어링) phải học evolution.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **30. Digital twin và predictive biology** tiếp nhận điểm tựa từ **29. Evolution là một “dạng thất bại (failure mode / 실패 모드)” của engineered circuit — và cũng là thiết kế (design / 설계) áp suất (pressure)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. data-driven và mô hình cơ chế bổ sung nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Digital twin và predictive biology

Ý tưởng digital twin là mô hình đủ tốt để predict trạng thái (state / 상태) của cell, tissue hoặc patient dưới intervention.

Nhưng hệ thống sinh học (biological system) high-dimensional, partially observed và history-dependent. Vì vậy hiện tại (current / 현재) “digital twin” nên được hiểu như hierarchy mô hình (model / 모델) với bất định (uncertainty / 불확실성), không phải bản sao hoàn hảo.

Prediction useful vẫn có thể đạt được mà không cần mô hình (model / 모델) mọi molecule.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **30. Digital twin và predictive biology** xác định đầu vào; **31. data-driven và mô hình cơ chế bổ sung nhau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **32. Xác thực mô hình (model validation) phải dựa trên prediction chưa dùng để fit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. data-driven và mô hình cơ chế bổ sung nhau

ML mạnh khi mẫu (pattern / 패턴) phức tạp và dữ liệu (data / 데이터) lớn. Mô hình cơ chế mạnh khi quan hệ (relation / 관계) nhân quả (causal / 인과적)/vật lý (physical / 물리적) đã biết.

Hybrid mô hình (model / 모델) có thể dùng neural mạng (network / 네트워크) estimate unknown hàm (function / 함수) nhưng giữ mass balance hoặc thermodynamic ràng buộc (constraint / 제약조건).

Tương lai quantitative biology nhiều khả năng là tích hợp (integration / 통합), không phải “AI thay thế cơ chế (mechanism / 메커니즘)”.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **31. data-driven và mô hình cơ chế bổ sung nhau** xác định đầu vào; **32. Xác thực mô hình (model validation) phải dựa trên prediction chưa dùng để fit** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **33. bất định (uncertainty / 불확실성) phải đi cùng prediction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Xác thực mô hình (model validation) phải dựa trên prediction chưa dùng để fit

Một mô hình (model / 모델) fit dữ liệu (data / 데이터) dùng để xây nó chỉ chứng minh tính tương thích (compatibility / 호환성). Stronger kiểm thử (test / 테스트) là predict perturbation hoặc điều kiện (condition / 조건) mới.

Ví dụ mô hình signaling predict knockout A sẽ tăng B sau 30 phút. Nếu experiment mới confirm temporal phản hồi (response / 응답), confidence tăng mạnh.

Science tiến bộ bằng cycle prediction → kiểm thử (test / 테스트) → revision.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **33. bất định (uncertainty / 불확실성) phải đi cùng prediction** tiếp nhận điểm tựa từ **32. Xác thực mô hình (model validation) phải dựa trên prediction chưa dùng để fit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Ethics và biosafety không phải appendix ngoài science** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. bất định (uncertainty / 불확실성) phải đi cùng prediction

Mô hình parameter không chắc, đo lường (measurement / 측정) noisy, cấu trúc (structure / 구조) có thể sai. Prediction nên có interval hoặc scenario phạm vi (range / 범위) khi phù hợp.

Một điểm (point / 지점) estimate duy nhất dễ tạo false precision.

Bất định (uncertainty / 불확실성) không làm mô hình (model / 모델) yếu; tường minh (explicit / 명시적) bất định (uncertainty / 불확실성) làm quyết định (decision / 결정) tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **34. Ethics và biosafety không phải appendix ngoài science** tiếp nhận điểm tựa từ **33. bất định (uncertainty / 불확실성) phải đi cùng prediction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Tình huống phân tích (case study): lactose-like genetic switch như exercise tư duy hệ thống (systems thinking)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Ethics và biosafety không phải appendix ngoài science

Gene drive, engineered vi sinh vật (microorganism) và clinical gene editing có benefit nhưng cũng ecological/xã hội (social / 사회적) rủi ro (risk / 위험).

Question cần xem containment, reversibility, off-target, horizontal transfer, informed consent và quản trị (governance / 거버넌스).

Technical feasibility không tự quyết định acceptability. Thiết kế tiến trình (process / 프로세스) cần rủi ro (risk / 위험) mô hình (model / 모델) cùng lúc với hiệu năng (performance / 성능) mô hình.

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **34. Ethics và biosafety không phải appendix ngoài science** cho ta quy tắc; **35. Tình huống phân tích (case study): lactose-like genetic switch như exercise tư duy hệ thống (systems thinking)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **36. Tình huống phân tích: drug combination và mạng (network / 네트워크) redundancy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Tình huống phân tích (case study): lactose-like genetic switch như exercise tư duy hệ thống (systems thinking)

Giả sử nutrient S activate regulator, regulator bật transporter T, transporter làm S đi vào cell nhanh hơn. Đây là positive vòng lặp (loop / 루프). Nhưng khi S được metabolize, intracellular S giảm, tạo negative tác động (effect / 효과).

Chỉ bằng topology, ta đã có thể hỏi: hệ thống (system / 시스템) có threshold không, adaptation không, tính lưỡng ổn không? Sau đó đo lường (measurement / 측정) time-course giúp phân biệt mô hình (model / 모델).

Sinh học hệ thống biến “pathway diagram” thành câu hỏi prediction.

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **35. Tình huống phân tích (case study): lactose-like genetic switch như exercise tư duy hệ thống (systems thinking)** cho ta quy tắc; **36. Tình huống phân tích: drug combination và mạng (network / 네트워크) redundancy** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **37. Các hiểu lầm phổ biến (common misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Tình huống phân tích: drug combination và mạng (network / 네트워크) redundancy

Drug A khối (block / 블록) pathway 1 nhưng cell sống nhờ con đường (pathway) 2. Drug B khối (block / 블록) pathway 2 nhưng pathway 1 đủ bù. Combination A+B gây collapse.

Nếu chỉ study single drug, ta có thể kết luận cả hai mục tiêu (target / 대상) “không quan trọng”. mạng (network / 네트워크) view reveal redundancy.

Đây là lý do combination therapy và genetic tương tác (interaction / 상호작용) map quan trọng trong cancer/infectious disease research.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **36. Tình huống phân tích: drug combination và mạng (network / 네트워크) redundancy** cho ta quy tắc; **37. Các hiểu lầm phổ biến (common misconceptions)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **38. Mô hình tư duy tổng hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Các hiểu lầm phổ biến (common misconceptions)

“Có mạng (network / 네트워크) diagram nghĩa đã hiểu hệ thống (system / 시스템)” là sai; topology không đủ động lực học (dynamics).

“mô hình (model / 모델) fit dữ liệu (data / 데이터) nghĩa cơ chế (mechanism / 메커니즘) đúng” sai; nhiều mô hình (model / 모델) có thể fit cùng đầu ra (output / 출력).

“Sinh học tổng hợp biến cell thành machine deterministic” sai; nhiễu, evolution và ngữ cảnh (context / 맥락) vẫn tồn tại.

“AI càng lớn thì không cần experiment” sai; prediction nhân quả (causal / 인과적) và phân phối (distribution / 분포) shift vẫn cần kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Trong **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **38. Mô hình tư duy tổng hợp** gom các mảnh từ **37. Các hiểu lầm phổ biến (common misconceptions)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **39. Synthesis với toàn thư viện kiến thức (knowledge library / 지식 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Mô hình tư duy tổng hợp

Hiện đại (modern / 현대적) sinh học hệ thống vận hành như vòng lặp:

```text
measure
→ represent network
→ formulate model
→ estimate parameter
→ predict
→ perturb system
→ compare prediction with reality
→ revise model
```

Sinh học tổng hợp thêm một nhánh:

```text
model principle
→ design circuit
→ build
→ test
→ learn context/constraint
→ redesign
```

Đây là biology dưới dạng iterative science + kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Ở chặng này của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **39. Synthesis với toàn thư viện kiến thức (knowledge library / 지식 라이브러리)** gom các mảnh từ **38. Mô hình tư duy tổng hợp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Khả năng quan sát (observability / 관측 가능성) và controllability: biết trạng thái (state / 상태) không đồng nghĩa điều khiển được hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Synthesis với toàn thư viện kiến thức (knowledge library / 지식 라이브러리)

Nhìn lại từ đầu, same motifs xuất hiện ở mọi quy mô (scale / 규모): độ dốc (gradient / 기울기) tạo vận chuyển (transport / 전송); phản hồi (feedback / 피드백) tạo điều khiển (control / 제어); selection tạo thích nghi (adaptation); mạng (network / 네트워크) tạo emergence; ràng buộc (constraint / 제약조건) tạo sự đánh đổi (trade-off / 트레이드오프).

Sinh học hệ thống chỉ làm các motif đó tường minh (explicit / 명시적) bằng equation và thí nghiệm (experiment). Nó không thay thế sinh học tế bào (cell biology), di truyền học (genetics) hay sinh thái học (ecology); nó cung cấp một ngôn ngữ (language / 언어) chung để nối chúng.

Đi tiếp sang [Biology × Mathematics × Computation × Scale](../90_connections/00_biology_math_computation_and_scale.md) và [Sinh học nhìn qua Vật lý, Hóa học và Kỹ thuật](../90_connections/01_biology_physics_chemistry_and_engineering.md) để tổng hợp các mẫu (pattern / 패턴) định lượng xuyên toàn thư viện.

<!-- depth-audit-2026:control-observability-evolution -->

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — các hệ thống (systems / 시스템들) Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)**, **39. Synthesis với toàn thư viện kiến thức (knowledge library / 지식 라이브러리)** cho ta quy tắc; **Khả năng quan sát (observability / 관측 가능성) và controllability: biết trạng thái (state / 상태) không đồng nghĩa điều khiển được hệ thống (system / 시스템)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Khả năng quan sát (observability / 관측 가능성) và controllability: biết trạng thái (state / 상태) không đồng nghĩa điều khiển được hệ thống (system / 시스템)

Trong điều khiển (control / 제어) lý thuyết (theory / 이론), **khả năng quan sát (observability / 관측 가능성)** hỏi trạng thái nội bộ (internal state / 내부 상태) có thể suy ra từ đo lường (measurement / 측정) hay không; **khả năng điều khiển (controllability)** hỏi đầu vào (input / 입력) có thể đưa hệ thống (system / 시스템) tới trạng thái (state / 상태) mong muốn hay không. Biology thường thiếu cả hai: ta chỉ đo một subset molecule, còn intervention tác động nhiều pathway ngoài ý muốn.

Điều này giải thích vì sao mô hình (model / 모델) fit dữ liệu (data / 데이터) tốt chưa chắc useful cho intervention. Hai parameter set có thể tạo đầu ra (output / 출력) giống nhau (**non-identifiability**), nhưng phản ứng khác khi perturb. Experiment tốt phải được thiết kế để phân biệt mô hình (model / 모델), không chỉ thu thêm cùng loại dữ liệu (data / 데이터).

Robustness và evolvability cũng tạo sự đánh đổi (trade-off / 트레이드오프). phản hồi (feedback / 피드백) âm giúp giữ đầu ra (output / 출력) trước disturbance, nhưng redundancy có thể che mutation; modularity hạn chế damage lan rộng nhưng tạo giao diện (interface / 인터페이스) mới cho evolution. Synthetic circuit chạy tốt ngày đầu có thể bị mutation phá nếu circuit gây chi phí (cost / 비용) cho cell; selection ưu tiên host clone tăng trưởng nhanh hơn chứ không ưu tiên mục tiêu engineer.

Vì vậy synthetic biology cần nghĩ theo hai vòng phản hồi (feedback / 피드백): kỹ thuật (engineering / 엔지니어링) điều khiển (control / 제어) trong một cell và evolutionary selection giữa nhiều cell qua generation. thiết kế (design / 설계) bền phải xét cả hai quy mô (scale / 규모).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Bioinformatics, thuật toán và Omics Workflow](02_bioinformatics_algorithms_and_omics_workflows.md) · [Mục lục Biology](../README.md) · [Biology × Mathematics × Computation × Scale →](../90_connections/00_biology_math_computation_and_scale.md)

> **Bàn giao:** Sau **Khả năng quan sát (observability / 관측 가능성) và controllability: biết trạng thái (state / 상태) không đồng nghĩa điều khiển được hệ thống (system / 시스템)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
