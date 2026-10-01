# Phiên bản (version / 버전) hóa Dữ liệu và Mô hình

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Phiên bản dữ liệu là gì?** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Dữ liệu có thể thay đổi nguy hiểm ở đâu?** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một hệ thống ML chỉ có thể tái lập tốt khi **dữ liệu, mã nguồn và sản phẩm tạo ra (artifact / 산출물) mô hình đều có danh tính rõ ràng**. Git quản lý mã nguồn rất tốt, nhưng tập dữ liệu lớn, bảng có thể thay đổi và đặc trưng được sinh tự động cần cơ chế versioning và lineage riêng.

## Phiên bản dữ liệu là gì?

Một phiên bản dữ liệu có thể được biểu diễn bằng:

```text
file bất biến + checksum
snapshot của kho dữ liệu theo thời điểm
truy vấn + phiên bản bảng nguồn
snapshot bảng Delta/Iceberg
manifest của các object ID
```

Điểm cốt lõi là phải xác định lại chính xác tập dữ liệu huấn luyện hoặc đánh giá đã được dùng.

> **Chuyển mạch:** Trong **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Phiên bản dữ liệu là gì?** nêu điều cần giải thích; **Dữ liệu có thể thay đổi nguy hiểm ở đâu?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Dòng nguồn gốc của tập dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu có thể thay đổi nguy hiểm ở đâu?

Nếu truy vấn `SELECT * FROM transactions` hôm nay và một tháng sau trả về nội dung khác nhau thì cùng mã nguồn/cấu hình vẫn tạo ra hai run không còn so sánh trực tiếp được.

Cần snapshot hoặc manifest theo thời điểm (point-in-time manifest) để đóng băng danh tính dữ liệu.

> **Chuyển mạch:** Ở chặng này của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Dữ liệu có thể thay đổi nguy hiểm ở đâu?** nêu điều cần giải thích; **Dòng nguồn gốc của tập dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phiên bản (version / 버전) hóa lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dòng nguồn gốc của tập dữ liệu

Lineage cần trả lời được:

```text
nguồn thô nào?
phép biến đổi nào?
bộ lọc nào?
phiên bản logic gán nhãn nào?
mã nguồn đặc trưng nào?
tập dữ liệu đầu ra nào?
mô hình nào dùng tập dữ liệu đó?
```

Lineage hai chiều hỗ trợ phân tích ảnh hưởng (impact analysis): nếu một bảng nguồn thay đổi, những mô hình nào sẽ bị ảnh hưởng?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Dòng nguồn gốc của tập dữ liệu** nêu điều cần giải thích; **Phiên bản (version / 버전) hóa lược đồ (schema / 스키마)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Phiên bản (version / 버전) hóa đặc trưng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên bản (version / 버전) hóa lược đồ (schema / 스키마)

Sự tiến hóa lược đồ (schema / 스키마) cần hợp đồng rõ. Đổi tên cột, đổi đơn vị hoặc đổi ngữ nghĩa (semantics / 의미론) có thể không gây lỗi cú pháp nhưng vẫn phá mô hình một cách âm thầm.

Nên theo dõi cả siêu dữ liệu (metadata / 메타데이터) ngữ nghĩa như đơn vị, múi giờ, encoding và khoảng giá trị hợp lệ.

> **Chuyển mạch:** Trong **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Phiên bản (version / 버전) hóa đặc trưng** tiếp nhận điểm tựa từ **Phiên bản (version / 버전) hóa lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên bản sản phẩm tạo ra (artifact / 산출물) của mô hình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên bản (version / 버전) hóa đặc trưng

Một định nghĩa đặc trưng (feature definition) thực chất gồm mã nguồn, phụ thuộc (dependency / 의존성) dữ liệu và ngữ nghĩa (semantics / 의미론) theo thời gian.

Ví dụ `avg_spend_30d` phải xác định rõ cửa sổ thời gian, múi giờ, loại giao dịch bị loại và thời điểm cutoff.

Tính nhất quán giữa huấn luyện và phục vụ yêu cầu lô-gic (logic / 논리) đặc trưng online tương thích với định nghĩa offline.

> **Chuyển mạch:** Ở chặng này của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Phiên bản sản phẩm tạo ra (artifact / 산출물) của mô hình** tiếp nhận điểm tựa từ **Phiên bản (version / 버전) hóa đặc trưng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phiên bản ngữ nghĩa và ID bất biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên bản sản phẩm tạo ra (artifact / 산출물) của mô hình

Phiên bản mô hình không chỉ là trọng số. Gói sản phẩm tạo ra (artifact / 산출물) nên gắn cùng:

```text
trọng số
cấu hình kiến trúc
tokenizer / preprocessor
ánh xạ nhãn
yêu cầu runtime
signature / schema đầu vào
training run ID
báo cáo đánh giá
```

Với ứng dụng LLM hoặc RAG còn cần phiên bản prompt và cấu hình truy xuất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Phiên bản ngữ nghĩa và ID bất biến** tiếp nhận điểm tựa từ **Phiên bản sản phẩm tạo ra (artifact / 산출물) của mô hình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checksum dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phiên bản ngữ nghĩa và ID bất biến

Băm (hash / 해시) bất biến hoặc run ID phù hợp cho truy vết. Phiên bản phát hành dễ đọc phù hợp cho giao tiếp giữa con người.

Có thể dùng cả hai:

```text
release: fraud-model-3.2
artifact sha: abc123...
```

> **Chuyển mạch:** Trong **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Phiên bản ngữ nghĩa và ID bất biến** nêu điều cần giải thích; **Checksum dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tập dữ liệu lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checksum dữ liệu

Checksum phát hiện thay đổi ở mức byte nhưng không cho biết hai tập dữ liệu có tương đương về ngữ nghĩa hay không. chuỗi xử lý (pipeline / 파이프라인) dữ liệu cần cả băm (hash / 해시) lẫn siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Ở chặng này của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Checksum dữ liệu** nêu điều cần giải thích; **Tập dữ liệu lớn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Quyền riêng tư và xóa dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tập dữ liệu lớn

Không nên sao chép toàn bộ tập dữ liệu cho mỗi thí nghiệm nếu chi phí lưu trữ quá lớn. Snapshot, manifest hoặc lưu trữ theo nội dung (content-addressed storage) có thể tái sử dụng các khối (block / 블록) không đổi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Tập dữ liệu lớn** nêu điều cần giải thích; **Quyền riêng tư và xóa dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đồ thị Mô hình–Dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền riêng tư và xóa dữ liệu

Versioning không có nghĩa giữ mọi dữ liệu vĩnh viễn. Yêu cầu xóa vì quyền riêng tư và chính sách lưu giữ phải được truyền qua snapshot, bộ nhớ đệm (cache / 캐시) và lineage huấn luyện.

Trong một số trường hợp cần biết mô hình nào từng huấn luyện từ dữ liệu phải xóa để đánh giá việc huấn luyện lại hoặc biện pháp khắc phục.

> **Chuyển mạch:** Trong **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Quyền riêng tư và xóa dữ liệu** nêu điều cần giải thích; **Đồ thị Mô hình–Dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị Mô hình–Dữ liệu

Một mô hình tư duy hữu ích:

```text
Dữ liệu nguồn
   ↓
Phiên bản tập dữ liệu
   ↓
Phiên bản đặc trưng
   ↓
Lần huấn luyện
   ↓
Artifact mô hình
   ↓
Đánh giá
   ↓
Triển khai
```

Mỗi cạnh trong đồ thị (graph / 그래프) cần siêu dữ liệu (metadata / 메타데이터) có thể truy vết.

> **Chuyển mạch:** Ở chặng này của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Đồ thị Mô hình–Dữ liệu** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Git LFS là đủ cho phiên bản (version / 버전) hóa dữ liệu”

Có thể đủ với tập dữ liệu nhỏ và ít thay đổi, nhưng snapshot kho dữ liệu hoặc lineage quy mô lớn cần lớp trừu tượng (abstraction / 추상화) khác.

### “Phiên bản mô hình chỉ là tên checkpoint”

Không. Tokenizer, lược đồ (schema / 스키마) và cấu hình cũng là một phần của mô hình có thể thực thi.

### “Càng nhiều snapshot càng tốt”

Không. Chi phí lưu trữ, thời hạn lưu giữ và ràng buộc quyền riêng tư cần được cân bằng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phiên bản (version / 버전) hóa Dữ liệu và Mô hình**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Experiment Tracking](./01_experiment_tracking_and_reproducibility.md), [Data Governance](../14_data_for_ai/08_data_governance.md), [Model Registry](./03_model_registry.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
