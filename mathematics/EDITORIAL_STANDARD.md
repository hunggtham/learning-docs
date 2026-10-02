# Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**. Route đi từ chapter objective → explanation flow → mechanism, assumptions và failure modes → examples, evidence và boundary → handoff/cross-links, để mọi chapter toán giữ được chiều sâu và tiếng Việt rõ.

Tài liệu trong `mathematics/` được viết như một **kiến thức (knowledge / 지식) book để học lâu dài**, không phải cheat sheet, collection công thức hay ghi chú (note / 노트) ôn thi. tệp (file / 파일) này là chuẩn biên soạn cho các lần cập nhật (update / 업데이트) tiếp theo, để những chapter được viết ở các thời điểm khác nhau vẫn có cùng chất lượng và cùng cách tư duy.

## 1. Mục tiêu của một chapter

Một chapter tốt phải giúp người đọc xây được một mô hình tư duy (mental model / 사고 모델) đủ mạnh để tự suy luận khi gặp tình huống mới. Sau khi đọc, người học không chỉ trả lời được “công thức là gì?” mà còn phải hiểu:

- đối tượng (object / 객체) hoặc concept đang nói tới là gì;
- vấn đề nào khiến concept đó cần tồn tại;
- concept được xây từ những giả định (assumption / 가정) hoặc idea nào;
- formula xuất hiện từ đâu và từng thành phần có ý nghĩa gì;
- khi nào mô hình (model / 모델) đúng, khi nào bắt đầu sai hoặc thiếu;
- concept liên kết thế nào với các chapter trước và sau;
- cùng cấu trúc (structure / 구조) đó xuất hiện ở đâu trong science, kỹ thuật (engineering / 엔지니어링), software, dữ liệu (data / 데이터), AI hoặc đời sống.

Một chapter không được coi là hoàn thiện chỉ vì đã liệt kê đủ definitions và formulas.

> **Chuyển mạch:** Trong **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **2. Luồng giải thích mặc định** tiếp nhận điểm tựa từ **1. Mục tiêu của một chapter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Viết thành discourse, không viết thành flashcard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Luồng giải thích mặc định

Không ép mọi chapter vào một template cứng, nhưng một luồng tốt thường là:

```text
problem / phenomenon
    ↓
what must be represented or measured?
    ↓
minimal definitions
    ↓
relationship between quantities
    ↓
model / theorem / formula
    ↓
derivation or reasoning
    ↓
worked examples
    ↓
limits and failure modes
    ↓
connections to other knowledge
    ↓
mental model
```

Nếu người đọc cần một prerequisite để hiểu bước hiện tại, hoặc giải thích prerequisite ngay tại chỗ ở mức đủ dùng, hoặc link rõ đến chapter đã giải thích nó. Không dùng câu kiểu “phần này sẽ rõ hơn ở chương nâng cao” để né giải thích bản chất cần thiết.

> **Chuyển mạch:** Ở chặng này của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **3. Viết thành discourse, không viết thành flashcard** tiếp nhận điểm tựa từ **2. Luồng giải thích mặc định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Definition phải đi cùng intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Viết thành discourse, không viết thành flashcard

Phần giải thích chính ưu tiên paragraph có logical luồng (flow / 흐름). Bullet chỉ nên dùng khi bản chất nội dung thực sự là danh sách (list / 목록), ví dụ các giả định (assumptions / 가정들), classification, thuật toán (algorithm / 알고리즘) steps hoặc concise comparison.

Không viết liên tiếp các câu như:

```text
A là ...
B là ...
C dùng để ...
```

nếu giữa A, B và C có nhân quả (causal / 인과적) relationship. Hãy nói vì sao B xuất hiện từ A và vì sao C cần B.

Mỗi section nên có một câu hỏi hoặc idea trung tâm. Heading không nên chia vụn nội dung thành quá nhiều section chỉ có một paragraph ngắn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **4. Definition phải đi cùng intuition** tiếp nhận điểm tựa từ **3. Viết thành discourse, không viết thành flashcard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Công thức phải có provenance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Definition phải đi cùng intuition

Definition chính xác là cần thiết nhưng không đủ. Khi giới thiệu một term mới, dùng format:

```text
Tên tiếng Việt (English term / 한국어 용어)
```

ở mọi lần thuật ngữ xuất hiện trong phần giải thích.

Sau definition, giải thích đối tượng (object / 객체) đó nên được “nhìn” như thế nào. Ví dụ, basis không chỉ là “linearly independent spanning set”; nó là một hệ tọa độ tối thiểu cho một véc-tơ (vector / 벡터) không gian (space / 공간). Derivative không chỉ là limit của difference quotient; nó là cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델) của một hàm (function / 함수).

> **Chuyển mạch:** Trong **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **5. Công thức phải có provenance** tiếp nhận điểm tựa từ **4. Definition phải đi cùng intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Ví dụ phải tạo lập luận (reasoning / 추론) transfer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Công thức phải có provenance

Không để formula đứng một mình. Với formula quan trọng, chapter phải giải thích ít nhất bốn lớp:

1. formula đang mô hình (model / 모델) điều gì;
2. mỗi symbol đại diện cho gì và đơn vị (unit / 단위) nếu có;
3. vì sao các đại lượng liên hệ theo dạng đó;
4. các giả định (assumptions / 가정들) hoặc lĩnh vực (domain / 도메인) validity.

Khi derivation hợp lý trong phạm vi (scope / 범위), derive từng bước. Không dùng “ta dễ dàng suy ra” ở chỗ mà người học mới có thể không thấy dễ.

Ví dụ, thay vì chỉ ghi

```math
A(t)=A_0e^{kt},
```

cần nối nó với cục bộ (local / 로컬) law

```math
\frac{dA}{dt}=kA
```

và giải thích rằng exponential xuất hiện vì tốc độ thay đổi tại mỗi thời điểm tỷ lệ với chính lượng hiện có.

> **Chuyển mạch:** Ở chặng này của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **5. Công thức phải có provenance** cho ta quy tắc; **6. Ví dụ phải tạo lập luận (reasoning / 추론) transfer** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. Liên kết giữa các lĩnh vực phải dựa trên cùng cấu trúc (structure / 구조)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Ví dụ phải tạo lập luận (reasoning / 추론) transfer

Một chapter quan trọng nên cố gắng có nhiều lớp ví dụ khi phù hợp:

**Intuitive example** giúp người đọc hình dung cấu trúc (structure / 구조) trước khi tính toán.

**Numeric example** bắt người đọc đi qua formula với con số cụ thể và kiểm tra đơn vị (unit / 단위)/thứ tự (order / 순서) of magnitude.

**Real-system example** cho thấy mô hình (model / 모델) được sử dụng trong software, physics, finance, statistics hoặc kỹ thuật (engineering / 엔지니어링) như thế nào.

**Counterexample hoặc thất bại (failure / 실패) example** cho biết giả định (assumption / 가정) nào thật sự quan trọng.

Ví dụ không nên chỉ chứng minh rằng formula “chạy được”; nó phải làm rõ một idea.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **6. Ví dụ phải tạo lập luận (reasoning / 추론) transfer** cho ta quy tắc; **7. Liên kết giữa các lĩnh vực phải dựa trên cùng cấu trúc (structure / 구조)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. Phân biệt mô hình (model / 모델), theorem và computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Liên kết giữa các lĩnh vực phải dựa trên cùng cấu trúc (structure / 구조)

Không thêm section “Ứng dụng IT” chỉ để kể tên công nghệ. Chỉ tạo liên kết (connection / 연결) khi có cùng mathematical cấu trúc (structure / 구조).

Ví dụ:

- composition của functions ↔ software chuỗi xử lý (pipeline / 파이프라인) ↔ neural mạng (network / 네트워크) layers;
- projection ↔ least squares ↔ attention similarity ↔ graphics camera coordinates;
- exponential decay ↔ radioactive decay ↔ bộ nhớ đệm (cache / 캐시) TTL probabilistic các mô hình (models / 모델들) ↔ discounting;
- đồ thị (graph / 그래프) reachability ↔ phụ thuộc (dependency / 의존성) resolution ↔ mạng (network / 네트워크) routing ↔ chuyển tiếp trạng thái (state transition / 상태 전이);
- điều kiện (condition / 조건) number ↔ sensitivity of a computational bài toán (problem / 문제).

Khi liên kết (connection / 연결) chỉ là analogy bề mặt, không dùng nó như explanation.

> **Chuyển mạch:** Trong **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **8. Phân biệt mô hình (model / 모델), theorem và computation** tiếp nhận điểm tựa từ **7. Liên kết giữa các lĩnh vực phải dựa trên cùng cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Luôn nói về các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Phân biệt mô hình (model / 모델), theorem và computation

Ba câu hỏi này phải được tách rõ:

**mô hình (model / 모델):** Ta đã chọn biểu diễn (representation / 표현) nào cho reality/bài toán (problem / 문제)?

**Mathematics:** Trong mô hình (model / 모델) đó, điều gì đúng một cách logical?

**Computation:** Máy tính thực sự tính approximation đó thế nào và lỗi (error / 오류) ở đâu?

Ví dụ `Ax=b` có thể có chính xác (exact / 정확한) mathematical solution, nhưng measured `A,b` có noise và numerical thuật toán (algorithm / 알고리즘) lại dùng floating điểm (point / 지점). Đây là ba nguồn bất định (uncertainty / 불확실성) khác nhau.

> **Chuyển mạch:** Ở chặng này của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **9. Luôn nói về các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **8. Phân biệt mô hình (model / 모델), theorem và computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Dùng notation nhất quán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Luôn nói về các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Một formula hữu ích hơn khi người đọc biết lúc nào không nên dùng nó.

Các câu hỏi cần xem xét:

- lĩnh vực (domain / 도메인) có restriction gì?
- theorem cần continuity/differentiability/independence/nonnegative weight... không?
- mô hình (model / 모델) giả định linearity, stationarity, infinite tài nguyên (resource / 자원), Gaussian noise hay independence không?
- nếu giả định (assumption / 가정) hỏng thì kết luận sai theo kiểu nào?
- numerical phương thức (method / 메서드) có stability hoặc conditioning issue không?

Đây là phần giúp kiến thức (knowledge / 지식) chuyển từ “school math” thành kỹ thuật (engineering / 엔지니어링) judgment.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **10. Dùng notation nhất quán** tiếp nhận điểm tựa từ **9. Luôn nói về các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. mô hình tư duy (mental model / 사고 모델) không phải summary** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Dùng notation nhất quán

Ưu tiên notation phổ biến trong textbook và documentation quốc tế. Nếu một symbol có nhiều conventions, nói rõ convention đang dùng.

Không đổi notation vô lý giữa các section. véc-tơ (vector / 벡터) nên được viết nhất quán, ma trận (matrix / 행렬) dimension phải hợp lệ, summation chỉ mục (index / 인덱스) cần có phạm vi (range / 범위) rõ khi cần. xác suất (probability / 확률) phân biệt `P(A)`, density `p(x)` và likelihood `L(θ;x)`.

Formula display dùng fenced `math` khối (block / 블록) theo convention hiện tại của repository.

> **Chuyển mạch:** Trong **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **11. mô hình tư duy (mental model / 사고 모델) không phải summary** gom các mảnh từ **10. Dùng notation nhất quán** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **12. dùng chung (common / 공통) Misconceptions phải giải thích vì sao sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. mô hình tư duy (mental model / 사고 모델) không phải summary

`## Mental Model` phải nén chapter thành một cách nhìn có khả năng tái sử dụng, chứ không lặp lại definition.

Ví dụ tốt:

> Basis là một vocabulary tối thiểu cho véc-tơ (vector / 벡터) không gian (space / 공간): đổi basis giống đổi ngôn ngữ tọa độ, đối tượng (object / 객체) không đổi nhưng description có thể đơn giản hơn rất nhiều.

Mô hình tư duy (mental model / 사고 모델) phải giúp người đọc dự đoán hoặc suy luận, không chỉ ghi nhớ.

> **Chuyển mạch:** Ở chặng này của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **12. dùng chung (common / 공통) Misconceptions phải giải thích vì sao sai** gom các mảnh từ **11. mô hình tư duy (mental model / 사고 모델) không phải summary** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **13. Chất lượng chapter quan trọng hơn độ dài** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. dùng chung (common / 공통) Misconceptions phải giải thích vì sao sai

Không chỉ liệt kê lỗi. Với misconception quan trọng, nói nguyên nhân nó có vẻ hợp lý và điểm lô-gic (logic / 논리) nào bị nhầm.

Ví dụ: “logarithm làm dữ liệu thành tuyến tính” chỉ đúng với một số functional relationships; log-transform không tự động biến arbitrary nonlinear quan hệ (relation / 관계) thành tuyến tính (linear / 선형) quan hệ (relation / 관계) và còn thay đổi interpretation/lỗi (error / 오류) cấu trúc (structure / 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **13. Chất lượng chapter quan trọng hơn độ dài** tiếp nhận điểm tựa từ **12. dùng chung (common / 공통) Misconceptions phải giải thích vì sao sai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Checklist trước khi merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Chất lượng chapter quan trọng hơn độ dài

Không đặt word-count mục tiêu (target / 대상) cứng. Tuy nhiên, chapter nền tảng chỉ vài trăm từ thường là dấu hiệu cần kiểm tra (audit / 감사) nếu concept có nhiều phụ thuộc (dependency / 의존성) và consequences.

Một tệp (file / 파일) dài cũng có thể kém nếu lặp ý. Mục tiêu là **conceptual completeness**, không phải volume.

> **Chuyển mạch:** Trong **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **14. Checklist trước khi merge** tiếp nhận điểm tựa từ **13. Chất lượng chapter quan trọng hơn độ dài** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델) cho toàn bộ thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Checklist trước khi merge

Trước khi coi một chapter là hoàn thiện trong phạm vi (scope / 범위), kiểm tra:

- Có giải thích bài toán (problem / 문제)/need trước definition không?
- Có giải thích bản chất, không chỉ cú pháp (syntax / 문법)/formula không?
- Formula chính có lập luận (reasoning / 추론) hoặc derivation phù hợp không?
- Có example đủ để transfer lập luận (reasoning / 추론) không?
- Có các giả định (assumptions / 가정들), ranh giới (boundary / 경계) cases và thất bại (failure / 실패) modes không?
- Có liên kết với prerequisites và downstream concepts không?
- English/Korean terminology có nhất quán không?
- Có `Mental Model` thật sự hữu ích không?
- `Common Misconceptions` có giải thích lỗi tư duy không?
- Paragraph có luồng (flow / 흐름) hay vẫn giống bullet notes được kéo dài?

> **Chuyển mạch:** Ở chặng này của **Editorial tiêu chuẩn (standard / 표준) — Mathematics thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Mô hình tư duy (mental model / 사고 모델) cho toàn bộ thư viện (library / 라이브러리)** gom các mảnh từ **14. Checklist trước khi merge** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델) cho toàn bộ thư viện (library / 라이브러리)

> Mỗi chapter không phải một hộp kiến thức riêng. Nó là một nút (node / 노드) trong đồ thị (graph / 그래프) của các representations, các ràng buộc (constraints / 제약조건들), transformations, rates, accumulations, symmetries, uncertainties và tối ưu hóa (optimization / 최적화) problems. Viết tốt nghĩa là làm cho các edge giữa những nút (node / 노드) đó trở nên nhìn thấy được.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델) cho toàn bộ thư viện (library / 라이브러리)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
