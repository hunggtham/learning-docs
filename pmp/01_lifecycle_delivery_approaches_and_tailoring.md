# 01 — Vòng đời, delivery approach và tailoring

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **01 — Lifecycle, delivery approach và tailoring**. Route đi từ uncertainty/constraint → predictive/agile/hybrid choice → development lifecycle → tailoring decisions → feedback and governance, để cách giao hàng xuất phát từ bối cảnh.

## Không có một tiến trình (process / 프로세스) đúng cho mọi dự án

Một nhà máy, một di chuyển (migration / 마이그레이션) cơ sở dữ liệu (database / 데이터베이스) và một ứng dụng thử nghiệm thị trường đều là dự án (project / 프로젝트), nhưng chi phí (cost / 비용) of thay đổi (change / 변경) và mức bất định khác nhau. Vì vậy việc áp cùng một quy trình cho mọi dự án là lỗi thiết kế. Tailoring (điều chỉnh phương pháp / 테일러링) là quá trình chọn và điều chỉnh approach, practice, sản phẩm tạo ra (artifact / 산출물), quản trị (governance / 거버넌스) và cadence theo ngữ cảnh (context / 맥락) thực tế.

Câu hỏi đầu tiên không nên là “Waterfall hay Agile?”. Câu hỏi tốt hơn là: ta biết rõ bài toán (problem / 문제) và solution đến mức nào, phản hồi (feedback / 피드백) có thể nhận sớm đến đâu, chi phí (cost / 비용) of thay đổi (change / 변경) tăng ra sao theo thời gian, regulatory bằng chứng (evidence / 증거) cần mức nào, phụ thuộc (dependency / 의존성) vật lý/kỹ thuật chặt đến đâu, và stakeholder chấp nhận incremental delivery đến mức nào.

Một delivery approach thực chất là cách dự án (project / 프로젝트) phân phối ba thứ theo thời gian: **commitment**, **phản hồi (feedback / 피드백)** và **điều khiển (control / 제어)**. Predictive đặt nhiều commitment sớm hơn để tăng coordination; adaptive trì hoãn một số commitment để giữ option và học; hybrid đặt commitment ở ranh giới (boundary / 경계) cần ổn định nhưng giữ phản hồi (feedback / 피드백) nhanh ở vùng còn bất định.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Không có một tiến trình (process / 프로세스) đúng cho mọi dự án** xác định đầu vào; **Dự án (project / 프로젝트) vòng đời (lifecycle / 생명주기) và development vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Vòng đời (lifecycle / 생명주기) như một chuỗi commitment tăng dần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dự án (project / 프로젝트) vòng đời (lifecycle / 생명주기) và development vòng đời (lifecycle / 생명주기)

Vòng đời dự án (project life cycle / 프로젝트 생애주기) mô tả dự án (project / 프로젝트) từ khởi đầu đến kết thúc. Development vòng đời (lifecycle / 생명주기) mô tả cách sản phẩm hoặc deliverable được tạo ra. Hai thứ có thể khác nhau. Một dự án (project / 프로젝트) có initiation, planning, delivery, chuyển tiếp (transition / 전이), closure; bên trong delivery có thể dùng iterative software development.

Nhầm hai khái niệm dẫn đến tranh luận vô ích, ví dụ “Agile không cần planning”. Agile vẫn có planning, nhưng planning được phân phối qua nhiều horizon và cập nhật theo phản hồi (feedback / 피드백) thay vì cố định chi tiết xa trong tương lai.

Một cách nhìn tốt hơn là xem vòng đời (lifecycle / 생명주기) như chuỗi thay đổi trạng thái của investment. Lúc đầu tổ chức mới có một hypothesis rằng đầu tư này đáng làm. Sau đó dự án (project / 프로젝트) dần tạo bằng chứng (evidence / 증거), lần ghi nhận (commit / 커밋) nguồn lực, tạo deliverable, chuyển năng lực (capability / 역량) sang thao tác (operation / 연산) và cuối cùng đóng temporary organization. Mỗi phase tồn tại vì loại quyết định (decision / 결정) cần đưa ra thay đổi theo thời gian.

Vòng đời (lifecycle / 생명주기) tốt không chỉ hỏi “đã làm xong phase chưa?” mà hỏi “bằng chứng (evidence / 증거) hiện tại có đủ để chuyển sang mức commitment tiếp theo không?”. Nếu gate chỉ kiểm tra đủ template mà không thay đổi quyết định (decision / 결정) quyền đầu tư, nó trở thành ceremony.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Dự án (project / 프로젝트) vòng đời (lifecycle / 생명주기) và development vòng đời (lifecycle / 생명주기)** xác định đầu vào; **Vòng đời (lifecycle / 생명주기) như một chuỗi commitment tăng dần** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Năm chiều bất định (uncertainty / 불확실성) cần tách riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòng đời (lifecycle / 생명주기) như một chuỗi commitment tăng dần

Mỗi quyết định (decision / 결정) lớn làm giảm option. Ký hợp đồng dài hạn, chốt kiến trúc, đặt thiết bị, migrate môi trường vận hành (production / 운영 환경) dữ liệu (data / 데이터) hoặc công khai (public / 공개) launch đều là những commitment ngày càng khó đảo ngược.

Vì vậy vòng đời (lifecycle / 생명주기) nên đồng bộ **bằng chứng (evidence / 증거) strength** với **commitment irreversibility**. quyết định (decision / 결정) càng khó đảo ngược thì càng cần bằng chứng (evidence / 증거) mạnh, rủi ro (risk / 위험) rà soát (review / 검토) rõ và authority phù hợp.

Một dự án (project / 프로젝트) yếu thường làm ngược: commitment lớn được đưa ra khi bằng chứng (evidence / 증거) còn yếu, rồi sau đó quản trị (governance / 거버넌스) chỉ cố bảo vệ quyết định (decision / 결정) cũ. Khi đó vòng đời (lifecycle / 생명주기) không còn là học tập (learning / 학습) hệ thống (system / 시스템) mà trở thành cơ chế rationalize sunk chi phí (cost / 비용).

Mô hình tư duy (mental model / 사고 모델):

```text
uncertainty cao + commitment dễ đảo ngược
                ↓ learning
uncertainty giảm + evidence tăng
                ↓
commitment lớn hơn / khó đảo ngược hơn
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Vòng đời (lifecycle / 생명주기) như một chuỗi commitment tăng dần** xác định đầu vào; **Năm chiều bất định (uncertainty / 불확실성) cần tách riêng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bất định (uncertainty / 불확실성) profile phải nối với loại phản hồi (feedback / 피드백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năm chiều bất định (uncertainty / 불확실성) cần tách riêng

Không nên gộp mọi bất định thành một từ “uncertain”. yêu cầu (requirement / 요구사항) bất định (uncertainty / 불확실성) là mức chưa rõ về nhu cầu. Solution bất định (uncertainty / 불확실성) là mức chưa rõ về cách xây. thực thi (execution / 실행) bất định (uncertainty / 불확실성) là khả năng kế hoạch bị lệch do phụ thuộc (dependency / 의존성), năng suất hoặc tài nguyên (resource / 자원). bên ngoài (external / 외부) bất định (uncertainty / 불확실성) đến từ regulation, thị trường (market / 시장), vendor hay technology. Adoption bất định (uncertainty / 불확실성) là mức chưa rõ liệu đầu ra (output / 출력) có thực sự được sử dụng để tạo kết quả (outcome / 결과) hay không.

Một dự án có thể yêu cầu (requirement / 요구사항) ổn định nhưng solution bất định (uncertainty / 불확실성) cao, ví dụ di chuyển (migration / 마이그레이션) một hệ thống legacy có phạm vi (scope / 범위) rõ nhưng chưa biết dữ liệu bẩn đến mức nào. Dự án khác có solution technology quen thuộc nhưng yêu cầu (requirement / 요구사항) bất định (uncertainty / 불확실성) cao vì customer chưa biết họ muốn gì. Hai trường hợp này cần vòng phản hồi (feedback loop / 피드백 루프) khác nhau.

Đây là lý do chỉ hỏi “phạm vi (scope / 범위) có rõ không?” là chưa đủ để chọn approach.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Bất định (uncertainty / 불확실성) profile phải nối với loại phản hồi (feedback / 피드백)** tiếp nhận điểm tựa từ **Năm chiều bất định (uncertainty / 불확실성) cần tách riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) of thay đổi (change / 변경) không phải một đường cong cố định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định (uncertainty / 불확실성) profile phải nối với loại phản hồi (feedback / 피드백)

Không phải phản hồi (feedback / 피드백) nào cũng giảm cùng loại bất định (uncertainty / 불확실성). người dùng (user / 사용자) interview có thể giảm yêu cầu (requirement / 요구사항) bất định (uncertainty / 불확실성) nhưng không chứng minh hiệu năng (performance / 성능) ở môi trường vận hành (production / 운영 환경) tải (load / 로드). Technical spike có thể giảm solution bất định (uncertainty / 불확실성) nhưng không chứng minh adoption. đặc tả hợp đồng (contract / 계약) clarification giảm bên ngoài (external / 외부)/commercial bất định (uncertainty / 불확실성) nhưng không giúp customer usability.

Tailoring tốt vì vậy cần hỏi **ta đang cố học điều gì**, rồi chọn phản hồi (feedback / 피드백) cơ chế (mechanism / 메커니즘) tương ứng. Demo không phải phản hồi (feedback / 피드백) đủ cho mọi rủi ro (risk / 위험). Prototype, pilot, simulation, regulatory rà soát (review / 검토), kiểm thử tải (load test / 부하 테스트), vendor proof-of-concept hay operational rehearsal đều là các vòng phản hồi (feedback loop / 피드백 루프) khác nhau.

Một dự án (project / 프로젝트) có nhiều phản hồi (feedback / 피드백) sự kiện (event / 이벤트) nhưng vẫn học rất ít nếu phản hồi (feedback / 피드백) không chạm giả định (assumption / 가정) trọng yếu (critical / 중요).

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Chi phí (cost / 비용) of thay đổi (change / 변경) không phải một đường cong cố định** tiếp nhận điểm tựa từ **Bất định (uncertainty / 불확실성) profile phải nối với loại phản hồi (feedback / 피드백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Predictive: khi việc dự đoán có giá trị cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) of thay đổi (change / 변경) không phải một đường cong cố định

Người học thường nghe “thay đổi (change / 변경) càng muộn càng đắt”. Điều này đúng trong nhiều ngữ cảnh (context / 맥락) nhưng không phải luật tuyệt đối. chi phí (cost / 비용) of thay đổi (change / 변경) phụ thuộc sản phẩm tạo ra (artifact / 산출물) đã lần ghi nhận (commit / 커밋), phụ thuộc (dependency / 의존성) đã phát sinh, đặc tả hợp đồng (contract / 계약) đã khóa, dữ liệu (data / 데이터) đã migrate, huấn luyện (training / 학습) đã rollout và expectation đã được công khai (public / 공개) đến đâu.

Trong software có automated kiểm thử (test / 테스트), modular kiến trúc (architecture / 아키텍처) và cờ tính năng (feature flag / 기능 플래그), một số thay đổi (change / 변경) muộn có thể vẫn rẻ. Trong construction, hardware fabrication hoặc regulated submission, thay đổi (change / 변경) muộn có thể rất đắt.

Delivery approach nên được chọn dựa trên **actual thay đổi (change / 변경) economics**, không dựa vào slogan theo methodology.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Predictive: khi việc dự đoán có giá trị cao** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) of thay đổi (change / 변경) không phải một đường cong cố định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Predictive thất bại (failure / 실패) không phải lúc nào do “Waterfall”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predictive: khi việc dự đoán có giá trị cao

Predictive approach (phương pháp dự đoán / 예측형 접근) phù hợp khi phạm vi (scope / 범위) có thể xác định tương đối sớm, phụ thuộc (dependency / 의존성) rõ, thay đổi muộn đắt, hoặc đặc tả hợp đồng (contract / 계약)/regulation yêu cầu baseline mạnh. Công trình xây dựng là ví dụ trực quan: không thể liên tục đổi vị trí cột chịu lực sau khi đã thi công.

Predictive không có nghĩa “không thay đổi”. Nó làm thay đổi (change / 변경) tường minh (explicit / 명시적) bằng baseline, impact phân tích (analysis / 분석) và thay đổi (change / 변경) điều khiển (control / 제어). Strength của nó là coordination và predictability khi kiến thức (knowledge / 지식) đủ ổn định; weakness là phản hồi (feedback / 피드백) có thể đến muộn nếu ta giả định quá nhiều điều chưa biết.

Điểm sâu hơn là predictive đặt commitment tương đối sớm. Vì vậy nó hiệu quả nhất khi thông tin (information / 정보) lúc commitment đủ tốt. Nếu commitment được đưa ra sớm hơn khả năng hiểu bài toán (problem / 문제), baseline có thể tạo cảm giác chắc chắn giả. Khi đó dự án (project / 프로젝트) không thực sự “có kế hoạch tốt”; nó chỉ có một forecast được trình bày như commitment.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Predictive thất bại (failure / 실패) không phải lúc nào do “Waterfall”** tiếp nhận điểm tựa từ **Predictive: khi việc dự đoán có giá trị cao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adaptive/agile: khi học tập (learning / 학습) có giá trị cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predictive thất bại (failure / 실패) không phải lúc nào do “Waterfall”

Một predictive dự án (project / 프로젝트) có thể thất bại vì yêu cầu (requirement / 요구사항) discovery kém, phụ thuộc (dependency / 의존성) mô hình (model / 모델) sai, quản trị (governance / 거버넌스) độ trễ (latency / 지연 시간) hoặc incentive khiến bad news bị giấu. Chuyển sang sprint không tự sửa những nguyên nhân này.

Cần phân biệt **approach thất bại (failure / 실패)** với **execution-system thất bại (failure / 실패)**. Nếu bất định (uncertainty / 불확실성) thật sự thấp nhưng nhóm (team / 팀) vẫn trễ vì tài nguyên (resource / 자원) contention, vấn đề không phải predictive. Nếu bất định (uncertainty / 불확실성) cao nhưng organization bắt baseline chi tiết quá sớm, lúc đó delivery approach mới là nguyên nhân cấu trúc.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Adaptive/agile: khi học tập (learning / 학습) có giá trị cao** tiếp nhận điểm tựa từ **Predictive thất bại (failure / 실패) không phải lúc nào do “Waterfall”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) quyết định học tập (learning / 학습) speed** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adaptive/agile: khi học tập (learning / 학습) có giá trị cao

Adaptive approach (phương pháp thích ứng / 적응형 접근) phù hợp khi yêu cầu (requirement / 요구사항) hoặc solution bất định (uncertainty / 불확실성) cao và có thể nhận phản hồi (feedback / 피드백) qua increment nhỏ. Thay vì tối ưu khả năng dự đoán toàn bộ phạm vi (scope / 범위), nó tối ưu tốc độ học và khả năng đổi hướng.

Batch nhỏ làm giảm chi phí (cost / 비용) of wrong giả định (assumption / 가정). Nếu một tính năng (feature / 기능) mất hai tuần để thử và bị bác bỏ, tổn thất nhỏ hơn việc dành sáu tháng xây toàn bộ hệ thống (system / 시스템) rồi mới cho người dùng (user / 사용자) xem. Nhưng adaptive không loại bỏ quản trị (governance / 거버넌스), kiến trúc (architecture / 아키텍처), compliance hay long-term thinking. Nó chỉ thay cách và thời điểm ra quyết định.

Adaptive chỉ có giá trị khi phản hồi (feedback / 피드백) có thể thay quyết định (decision / 결정). Nếu nhóm (team / 팀) demo mỗi hai tuần nhưng phạm vi (scope / 범위), priority, ngân sách (budget / 예산) và bản phát hành (release / 릴리스) plan đều không được phép thay, vòng lặp chỉ tạo ceremony chứ không tạo adaptation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) quyết định học tập (learning / 학습) speed** tiếp nhận điểm tựa từ **Adaptive/agile: khi học tập (learning / 학습) có giá trị cao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch kích thước (size / 크기) và rủi ro (risk / 위험) exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) quyết định học tập (learning / 학습) speed

Adaptive delivery không chỉ nói về iteration length. Điều quan trọng hơn là từ lúc một giả định (assumption / 가정) được đưa vào công việc (work / 작업) đến lúc dự án (project / 프로젝트) nhận bằng chứng (evidence / 증거) đủ để giữ hoặc thay quyết định (decision / 결정) mất bao lâu.

Một nhóm (team / 팀) có sprint hai tuần nhưng môi trường vận hành (production / 운영 환경) phản hồi (feedback / 피드백) ba tháng một lần vẫn có học tập (learning / 학습) độ trễ (latency / 지연 시간) dài. Ngược lại, một predictive dự án (project / 프로젝트) có prototype sớm và customer kiểm tra hợp lệ (validation / 검증) mạnh có thể giảm một số bất định (uncertainty / 불확실성) rất nhanh.

Ta có thể nghĩ đơn giản:

```text
learning speed ≈ quality of feedback / feedback latency
```

Đây không phải công thức toán học, mà là mô hình tư duy (mental model / 사고 모델): phản hồi (feedback / 피드백) nhanh nhưng noise cao không giúp nhiều; phản hồi (feedback / 피드백) chất lượng nhưng đến quá muộn cũng làm rework lớn.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Batch kích thước (size / 크기) và rủi ro (risk / 위험) exposure** tiếp nhận điểm tựa từ **Phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간) quyết định học tập (learning / 학습) speed** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hybrid không phải “lấy một nửa mỗi bên”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch kích thước (size / 크기) và rủi ro (risk / 위험) exposure

Batch càng lớn, càng nhiều giả định (assumption / 가정) được đóng gói trước khi nhận phản hồi (feedback / 피드백). Khi batch sai, rework blast radius lớn hơn.

Nhưng batch quá nhỏ cũng có overhead: triển khai (deployment / 배포), approval, setup hoặc kiểm tra hợp lệ (validation / 검증) chi phí (cost / 비용) có thể cao. Tailoring phải tìm economic batch kích thước (size / 크기) hợp lý thay vì mặc định “nhỏ nhất luôn tốt nhất”.

Trong regulated dự án (project / 프로젝트), có thể development batch nhỏ nhưng bằng chứng (evidence / 증거) gói (package / 패키지)/bản phát hành (release / 릴리스) gate lớn hơn vì compliance giao dịch (transaction / 트랜잭션) chi phí (cost / 비용). Hybrid thường xuất hiện chính ở đây.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Hybrid không phải “lấy một nửa mỗi bên”** tiếp nhận điểm tựa từ **Batch kích thước (size / 크기) và rủi ro (risk / 위험) exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hybrid giao diện (interface / 인터페이스) cần đặc tả hợp đồng (contract / 계약) rõ hơn methodology label** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid không phải “lấy một nửa mỗi bên”

Hybrid approach (phương pháp lai / 하이브리드 접근) có ý nghĩa khi các phần của hệ thống (system / 시스템) có bất định (uncertainty / 불확실성)/chi phí (cost / 비용) profile khác nhau. Ví dụ cốt lõi (core / 핵심) tích hợp (integration / 통합) với regulator có giao diện (interface / 인터페이스) cố định và milestone cứng, trong khi UX có thể được phát triển iteratively. Ta có thể baseline bên ngoài (external / 외부) milestones nhưng dùng backlog và sprint cho tương tác (interaction / 상호작용) thiết kế (design / 설계).

Hybrid tệ là giữ toàn bộ bureaucracy của predictive và toàn bộ ceremony của agile cùng lúc. Hybrid tốt chọn cơ chế (mechanism / 메커니즘) theo bài toán (problem / 문제): phần nào cần predictability, phần nào cần phản hồi (feedback / 피드백), và giao diện (interface / 인터페이스) giữa hai phần được quản lý thế nào.

Điểm khó nhất của hybrid thường không nằm trong từng phần mà ở giao diện (interface / 인터페이스). Một vendor predictive có thể yêu cầu specification freeze trong khi sản phẩm (product / 제품) nhóm (team / 팀) adaptive vẫn thay backlog. Nếu không định nghĩa rõ thay đổi (change / 변경) cửa sổ (window / 윈도우), versioning, acceptance và phụ thuộc (dependency / 의존성), mỗi bên đều có thể “làm đúng tiến trình (process / 프로세스)” nhưng toàn hệ thống vẫn trễ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Hybrid không phải “lấy một nửa mỗi bên”** cho ta quy tắc; **Hybrid giao diện (interface / 인터페이스) cần đặc tả hợp đồng (contract / 계약) rõ hơn methodology label** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Tailoring như một bài toán điều khiển (control / 제어) hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid giao diện (interface / 인터페이스) cần đặc tả hợp đồng (contract / 계약) rõ hơn methodology label

Mỗi ranh giới (boundary / 경계) giữa hai delivery chế độ (mode / 모드) nên làm rõ ít nhất: sản phẩm tạo ra (artifact / 산출물) nào là authoritative, phiên bản (version / 버전) nào được dùng, cadence handoff, acceptance quy tắc (rule / 규칙), thay đổi (change / 변경) cửa sổ (window / 윈도우), phụ thuộc (dependency / 의존성) đơn vị sở hữu (owner / 오너) và escalation threshold.

Ví dụ adaptive UX nhóm (team / 팀) bản phát hành (release / 릴리스) mỗi sprint nhưng vendor chỉ nhận API thay đổi (change / 변경) mỗi tháng. Nếu giao diện (interface / 인터페이스) cadence không tường minh (explicit / 명시적), backlog priority nội bộ có thể tạo công việc (work / 작업) không deploy được. Vấn đề ở đây là **coordination kiến trúc (architecture / 아키텍처)**, không phải nhóm (team / 팀) nào “less agile”.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Hybrid giao diện (interface / 인터페이스) cần đặc tả hợp đồng (contract / 계약) rõ hơn methodology label** cho ta quy tắc; **Tailoring như một bài toán điều khiển (control / 제어) hệ thống (system / 시스템)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Điều khiển (control / 제어) strength nên tỷ lệ với consequence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring như một bài toán điều khiển (control / 제어) hệ thống (system / 시스템)

Một tiến trình (process / 프로세스) tạo overhead để đổi lấy visibility, coordination hoặc rủi ro (risk / 위험) reduction. Nếu sản phẩm tạo ra (artifact / 산출물) không thay đổi quyết định (decision / 결정) nào, nó có thể chỉ là waste. Ngược lại, bỏ sản phẩm tạo ra (artifact / 산출물) trọng yếu (critical / 중요) chỉ vì “nhẹ” có thể làm tổ chức mất bằng chứng (evidence / 증거) cần cho compliance hoặc kiểm tra (audit / 감사).

Có thể lập luận (reasoning / 추론) theo chuỗi:

```text
context → uncertainty/risk → information need → control/feedback → artifact/cadence
```

Ví dụ dự án (project / 프로젝트) ít người, low rủi ro (risk / 위험), co-located có thể không cần status report dài. Nhưng dự án (project / 프로젝트) tài chính có vendor, bảo mật (security / 보안) rà soát (review / 검토) và regulator cần traceability mạnh; cùng một report/điều khiển (control / 제어) lúc này có purpose rõ.

Tailoring tốt luôn giữ điều khiển (control / 제어) mục tiêu (objective / 목표) trước rồi mới thay cơ chế (mechanism / 메커니즘). Nếu mục tiêu (objective / 목표) là “không bản phát hành (release / 릴리스) khi privacy bằng chứng (evidence / 증거) chưa đủ”, ta có thể thay manual meeting bằng automated gate, nhưng không được bỏ yêu cầu (requirement / 요구사항) chỉ vì muốn delivery nhanh hơn.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Điều khiển (control / 제어) strength nên tỷ lệ với consequence** tiếp nhận điểm tựa từ **Tailoring như một bài toán điều khiển (control / 제어) hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tailoring economics: điều khiển (control / 제어) cũng có chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều khiển (control / 제어) strength nên tỷ lệ với consequence

Không phải mọi quyết định (decision / 결정) cần cùng quản trị (governance / 거버넌스). Reversible low-impact quyết định (decision / 결정) có thể được decentralize; irreversible high-impact quyết định (decision / 결정) cần bằng chứng (evidence / 증거), rà soát (review / 검토) và authority mạnh hơn.

Một cách nhìn hữu ích là:

```text
control intensity ↑ khi
impact ↑, irreversibility ↑, external obligation ↑, information asymmetry ↑
```

Đây là lý do một CSS thay đổi (change / 변경) không cần CCB nhưng thay data-retention chính sách (policy / 정책) có thể cần legal/compliance approval dù coding effort nhỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Tailoring economics: điều khiển (control / 제어) cũng có chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Điều khiển (control / 제어) strength nên tỷ lệ với consequence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quản trị (governance / 거버넌스) cadence và quyết định (decision / 결정) độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring economics: điều khiển (control / 제어) cũng có chi phí (cost / 비용)

Điều khiển (control / 제어) không miễn phí. Mỗi approval, report, meeting, bằng chứng (evidence / 증거) gói (package / 패키지) hoặc handoff tạo giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và quyết định (decision / 결정) độ trễ (latency / 지연 시간). Thiếu điều khiển (control / 제어) gây thất bại (failure / 실패) rủi ro (risk / 위험); quá nhiều điều khiển (control / 제어) làm luồng (flow / 흐름) chậm và khiến nhóm (team / 팀) tìm đường vòng.

Tailoring maturity nằm ở việc tối ưu **total chi phí (cost / 비용) of quản trị (governance / 거버넌스)**, không phải tối thiểu hóa ceremony.

Nếu rà soát (review / 검토) thêm một ngày nhưng giảm đáng kể rủi ro (risk / 위험) của irreversible bản phát hành (release / 릴리스), chi phí (cost / 비용) hợp lý. Nếu 12 approver cùng ký một low-risk thay đổi (change / 변경) nhưng không ai thực sự thêm thông tin (information / 정보), điều khiển (control / 제어) đó chỉ chuyển trách nhiệm mà không tăng quyết định (decision / 결정) chất lượng (quality / 품질).

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Quản trị (governance / 거버넌스) cadence và quyết định (decision / 결정) độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Tailoring economics: điều khiển (control / 제어) cũng có chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Một khung chọn approach thực tế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quản trị (governance / 거버넌스) cadence và quyết định (decision / 결정) độ trễ (latency / 지연 시간)

Cadence nên match tốc độ thay đổi của thông tin (information / 정보). rủi ro (risk / 위험) rà soát (review / 검토) hàng quý có thể vô nghĩa trong một dự án (project / 프로젝트) bản phát hành (release / 릴리스) hàng tuần. Ngược lại executive steering meeting hàng ngày tạo overhead mà không có new bằng chứng (evidence / 증거) tương xứng.

Quyết định (decision / 결정) độ trễ (latency / 지연 시간) là thời gian từ khi quyết định (decision / 결정) need xuất hiện đến khi authority quyết. Tailoring phải xem độ trễ (latency / 지연 시간) có phù hợp với delivery cadence không. nhóm (team / 팀) sprint hai tuần nhưng procurement approval sáu tuần tạo bottleneck quản trị (governance / 거버넌스), dù development rất nhanh.

Một điều khiển (control / 제어) hệ thống (system / 시스템) tốt không chỉ biết **ai quyết**, mà còn biết **cần quyết trong bao lâu**.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Một khung chọn approach thực tế** tiếp nhận điểm tựa từ **Quản trị (governance / 거버넌스) cadence và quyết định (decision / 결정) độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Delivery approach có thể khác theo tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Một khung chọn approach thực tế

Có thể đánh giá một dự án bằng sáu câu hỏi. yêu cầu (requirement / 요구사항) có ổn định không? Solution có quen thuộc không? phản hồi (feedback / 피드백) có thể lấy sớm không? thay đổi (change / 변경) muộn có đắt không? Compliance/đặc tả hợp đồng (contract / 계약) có yêu cầu bằng chứng (evidence / 증거) cố định không? phụ thuộc (dependency / 의존성) vật lý hoặc bên ngoài (external / 외부) có buộc chuỗi (sequence / 시퀀스) cứng không?

Nếu yêu cầu (requirement / 요구사항) và solution đều ổn định, thay đổi (change / 변경) muộn đắt và bên ngoài (external / 외부) phụ thuộc (dependency / 의존성) chặt, predictive thường có lợi. Nếu yêu cầu (requirement / 요구사항) hoặc solution còn nhiều unknown nhưng có thể kiểm thử (test / 테스트) bằng increment nhỏ, adaptive mạnh hơn. Nếu các subsystem có profile khác nhau, hybrid thường hợp lý hơn một methodology duy nhất.

Khung này không tạo answer tự động. Nó buộc nhóm (team / 팀) giải thích vì sao một practice tồn tại thay vì chọn theo thói quen tổ chức.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Delivery approach có thể khác theo tầng (layer / 계층)** tiếp nhận điểm tựa từ **Một khung chọn approach thực tế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rolling-wave planning và planning horizon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Delivery approach có thể khác theo tầng (layer / 계층)

Không nhất thiết cả dự án (project / 프로젝트) có một approach duy nhất. quản trị (governance / 거버넌스)/funding có thể predictive, sản phẩm (product / 제품) discovery adaptive, procurement milestone-based, hạ tầng (infrastructure / 인프라) di chuyển (migration / 마이그레이션) phased và operations chuyển tiếp (transition / 전이) theo readiness gate.

Điểm quan trọng là các tầng (layer / 계층) phải có giao diện (interface / 인터페이스) rõ. “dự án (project / 프로젝트) này Agile” là mô tả quá thô nếu funding chỉ duyệt theo annual fixed phạm vi (scope / 범위) và vendor đặc tả hợp đồng (contract / 계약) không cho thay đổi (change / 변경).

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Rolling-wave planning và planning horizon** tiếp nhận điểm tựa từ **Delivery approach có thể khác theo tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Planning horizon nên gắn với quyết định (decision / 결정) horizon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rolling-wave planning và planning horizon

Khi thông tin xa tương lai kém tin cậy, ta lập kế hoạch chi tiết cho near term và coarse-grained cho far term. Đây là rolling-wave planning (lập kế hoạch cuốn chiếu / 점진적 상세 계획). Nó không phải thiếu kế hoạch; nó thừa nhận thông tin (information / 정보) chất lượng (quality / 품질) giảm theo thời gian (time / 시간) horizon.

Một roadmap 12 tháng có thể xác định kết quả (outcome / 결과)/milestone, nhưng tác vụ (task / 작업) chi tiết chỉ nên chắc trong vài tuần hoặc vài tháng tùy lĩnh vực (domain / 도메인). Nếu cố chi tiết hóa quá sớm, ta tạo false precision và tốn chi phí cập nhật.

Ngược lại, rolling-wave không được dùng như lý do để bỏ qua phụ thuộc (dependency / 의존성) dài hạn. Procurement lead thời gian (time / 시간) sáu tháng hoặc regulatory approval ba tháng phải được nhìn thấy sớm dù tác vụ (task / 작업) hiện thực (implementation / 구현) chi tiết chưa cần xác định.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Planning horizon nên gắn với quyết định (decision / 결정) horizon** tiếp nhận điểm tựa từ **Rolling-wave planning và planning horizon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stage gate và progressive commitment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Planning horizon nên gắn với quyết định (decision / 결정) horizon

Chi tiết chỉ có giá trị nếu giúp một quyết định (decision / 결정) sắp tới. Nếu nhóm (team / 팀) chưa cần chọn hiện thực (implementation / 구현) option trong sáu tháng nữa và bằng chứng (evidence / 증거) còn thay đổi mạnh, plan chi tiết hôm nay dễ trở thành waste.

Nhưng quyết định (decision / 결정) có lead thời gian (time / 시간) dài phải được kéo về sớm. Đây là khác biệt giữa **công việc (work / 작업) horizon** và **quyết định (decision / 결정) horizon**. Một thiết bị chỉ được lắp sáu tháng sau nhưng procurement quyết định (decision / 결정) có thể cần xảy ra ngay hôm nay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Stage gate và progressive commitment** tiếp nhận điểm tựa từ **Planning horizon nên gắn với quyết định (decision / 결정) horizon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gate phải có exit option thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stage gate và progressive commitment

Stage gate có ý nghĩa khi organization muốn tăng mức commitment theo bằng chứng (evidence / 증거). Ở đầu dự án (project / 프로젝트) có thể chỉ duyệt discovery ngân sách (budget / 예산). Sau prototype và rủi ro (risk / 위험) rà soát (review / 검토) mới duyệt full hiện thực (implementation / 구현). Trước môi trường vận hành (production / 운영 환경) lại có readiness gate.

Mô hình tư duy (mental model / 사고 모델) ở đây là progressive commitment: càng gần irreversible investment, yêu cầu bằng chứng (evidence / 증거) càng mạnh. Đây cũng là cách giảm sunk-cost trap vì dự án (project / 프로젝트) có cơ hội bị dừng hoặc đổi hướng trước khi chi phí lớn hơn.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Gate phải có exit option thật** tiếp nhận điểm tựa từ **Stage gate và progressive commitment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tailoring theo organizational năng lực (capability / 역량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gate phải có exit option thật

Nếu mọi stage gate luôn approve vì “đã đi đến đây rồi”, gate không còn chức năng. Một gate thực sự cần option continue, conditionally continue, pivot, pause hoặc stop.

Criteria nên được xác định trước khi emotion/sunk chi phí (cost / 비용) tăng. Ví dụ pilot chỉ mở rộng nếu adoption > X, lỗi (error / 오류) < Y và operational chi phí (cost / 비용) < Z. Nếu threshold được đổi sau khi thấy kết quả để tránh stop, quản trị (governance / 거버넌스) đã mất integrity.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Tailoring theo organizational năng lực (capability / 역량)** tiếp nhận điểm tựa từ **Gate phải có exit option thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển tiếp (transition / 전이) là phần của vòng đời (lifecycle / 생명주기), không phải hậu sự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring theo organizational năng lực (capability / 역량)

Approach phù hợp trên lý thuyết có thể thất bại nếu organization chưa có năng lực (capability / 역량). Continuous delivery cần automated kiểm thử (test / 테스트), triển khai (deployment / 배포) discipline và sản phẩm (product / 제품) quyết định (decision / 결정) rights. Decentralized quyết định (decision / 결정) cần skill và transparency. Predictive baseline cần estimation/dữ liệu (data / 데이터) chất lượng (quality / 품질) đủ tốt.

Vì vậy tailoring phải xét không chỉ dự án (project / 프로젝트) bất định (uncertainty / 불확실성) mà cả **năng lực (capability / 역량) của hệ thống (system / 시스템) thực thi**. Chọn practice vượt xa năng lực (capability / 역량) hiện tại có thể tạo theater; chọn practice quá thấp so với năng lực (capability / 역량) lại bỏ phí lợi thế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Tailoring theo organizational năng lực (capability / 역량)** xác định đầu vào; **Chuyển tiếp (transition / 전이) là phần của vòng đời (lifecycle / 생명주기), không phải hậu sự** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chuyển tiếp (transition / 전이) readiness là bằng chứng (evidence / 증거), không phải calendar date** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển tiếp (transition / 전이) là phần của vòng đời (lifecycle / 생명주기), không phải hậu sự

Dự án (project / 프로젝트) không tạo giá trị (value / 값) chỉ vì deliverable đã “xong”. Cần chuyển tiếp (transition / 전이) sang thao tác (operation / 연산), sản phẩm (product / 제품) nhóm (team / 팀), customer hoặc nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너). chuyển tiếp (transition / 전이) có thể gồm huấn luyện (training / 학습), hỗ trợ (support / 지원) mô hình (model / 모델), runbook, quyền sở hữu (ownership / 소유권) transfer, dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션), warranty, operational acceptance và benefits tracking.

Nếu chuyển tiếp (transition / 전이) không được thiết kế từ đầu, dự án (project / 프로젝트) có thể đóng hành chính nhưng organization chưa thực sự có năng lực (capability / 역량) bền vững. Điều này đặc biệt quan trọng với hệ thống (system / 시스템) software, nơi môi trường vận hành (production / 운영 환경) quyền sở hữu (ownership / 소유권) và sự cố (incident / 인시던트) responsibility phải rõ trước go-live.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, cơ chế trong **Chuyển tiếp (transition / 전이) là phần của vòng đời (lifecycle / 생명주기), không phải hậu sự** cần được kiểm chứng bằng dấu vết cụ thể; **Chuyển tiếp (transition / 전이) readiness là bằng chứng (evidence / 증거), không phải calendar date** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **Tailoring anti-patterns** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển tiếp (transition / 전이) readiness là bằng chứng (evidence / 증거), không phải calendar date

Go-live date không tự tạo readiness. Readiness cần bằng chứng (evidence / 증거) như thao tác (operation / 연산) đơn vị sở hữu (owner / 오너) rõ, hỗ trợ (support / 지원) coverage, monitoring, quay lui (rollback / 롤백), kiến thức (knowledge / 지식) transfer, truy cập (access / 접근), dữ liệu (data / 데이터) chất lượng (quality / 품질) và sự cố (incident / 인시던트) đường dẫn (path / 경로).

Nếu date đến nhưng readiness bằng chứng (evidence / 증거) thiếu, dự án (project / 프로젝트) phải surface sự đánh đổi (trade-off / 트레이드오프) thay vì gọi “schedule success” rồi đẩy rủi ro (risk / 위험) sang operations.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Chuyển tiếp (transition / 전이) readiness là bằng chứng (evidence / 증거), không phải calendar date** nêu điều cần giải thích; **Tailoring anti-patterns** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tailoring cần rà soát (review / 검토) lại khi ngữ cảnh (context / 맥락) đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring anti-patterns

Một anti-pattern phổ biến là cargo-cult methodology: giữ sản phẩm tạo ra (artifact / 산출물) và ceremony vì “khung phần mềm (framework / 프레임워크) yêu cầu” dù không ai dùng đầu ra (output / 출력) để quyết định. Anti-pattern thứ hai là methodology shopping: đổi khung phần mềm (framework / 프레임워크) mỗi khi dự án (project / 프로젝트) gặp khó thay vì sửa nguyên nhân gốc (root cause / 근본 원인) về authority, năng lực (capability / 역량) hay phụ thuộc (dependency / 의존성). Anti-pattern thứ ba là gọi mọi exception là “hybrid” nhưng không định nghĩa giao diện (interface / 인터페이스) giữa các chế độ (mode / 모드). Anti-pattern cuối cùng là over-tailoring: bỏ quá nhiều điều khiển (control / 제어) đến mức dự án (project / 프로젝트) mất traceability và dùng chung (shared / 공유) understanding.

Một anti-pattern tinh vi hơn là **tailoring theo convenience**: điều khiển (control / 제어) bị bỏ vì nhóm (team / 팀) không thích, không phải vì rủi ro (risk / 위험) đã giảm. Ngược lại **điều khiển (control / 제어) accumulation** xảy ra khi mỗi sự cố (incident / 인시던트) thêm một approval mới nhưng không bao giờ retire điều khiển (control / 제어) cũ, khiến quản trị (governance / 거버넌스) ngày càng chậm.

Tailoring chỉ tốt khi giảm waste mà không làm mất thông tin (information / 정보) cần cho quyết định (decision / 결정).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Tailoring cần rà soát (review / 검토) lại khi ngữ cảnh (context / 맥락) đổi** tiếp nhận điểm tựa từ **Tailoring anti-patterns** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mixed bất định (uncertainty / 불확실성) profile: một dự án (project / 프로젝트) có nhiều lô-gic (logic / 논리) delivery cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring cần rà soát (review / 검토) lại khi ngữ cảnh (context / 맥락) đổi

Tailoring không phải quyết định (decision / 결정) một lần lúc kickoff. Khi nhóm (team / 팀) kích thước (size / 크기) tăng, vendor mới vào, regulation đổi, sự cố (incident / 인시던트) xảy ra hoặc sản phẩm (product / 제품) chuyển từ discovery sang quy mô (scale / 규모), điều khiển (control / 제어) need thay đổi.

Một lightweight dự án (project / 프로젝트) có thể cần formal cấu hình (configuration / 구성) điều khiển (control / 제어) sau khi nhiều nhóm (team / 팀) cùng tích hợp (integration / 통합). Một regulated pilot có thể giảm một số ceremony khi bằng chứng (evidence / 증거)/automation trưởng thành. tiến trình (process / 프로세스) kiến trúc (architecture / 아키텍처) phải tiến hóa cùng rủi ro (risk / 위험) profile.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Mixed bất định (uncertainty / 불확실성) profile: một dự án (project / 프로젝트) có nhiều lô-gic (logic / 논리) delivery cùng lúc** tiếp nhận điểm tựa từ **Tailoring cần rà soát (review / 검토) lại khi ngữ cảnh (context / 맥락) đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhiều vòng phản hồi (feedback loop / 피드백 루프) có cadence khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mixed bất định (uncertainty / 불확실성) profile: một dự án (project / 프로젝트) có nhiều lô-gic (logic / 논리) delivery cùng lúc

Một dự án (project / 프로젝트) hiếm khi có chỉ một loại bất định (uncertainty / 불확실성). Ví dụ eKYC có thể có yêu cầu (requirement / 요구사항) compliance gần như cố định, solution bất định (uncertainty / 불확실성) ở OCR/face matching, thực thi (execution / 실행) bất định (uncertainty / 불확실성) ở tích hợp (integration / 통합) với legacy, bên ngoài (external / 외부) bất định (uncertainty / 불확실성) từ regulator/vendor và adoption bất định (uncertainty / 불확실성) ở customer hành vi (behavior / 동작). Nếu organization chọn một methodology duy nhất cho toàn bộ dự án (project / 프로젝트), ít nhất một loại bất định (uncertainty / 불확실성) thường bị xử lý bằng phản hồi (feedback / 피드백) cơ chế (mechanism / 메커니즘) không phù hợp.

Cách lập luận (reasoning / 추론) tốt hơn là tạo một **bất định (uncertainty / 불확실성) profile** cho từng ranh giới (boundary / 경계) quan trọng. Compliance yêu cầu (requirement / 요구사항) có thể cần baseline và formal bằng chứng (evidence / 증거). mô hình (model / 모델) chất lượng (quality / 품질) cần pilot/segmented evaluation. UX cần người dùng (user / 사용자) phản hồi (feedback / 피드백) ngắn. Legacy tích hợp (integration / 통합) cần early technical spike. Operations readiness cần rehearsal gần chuyển tiếp (transition / 전이). Đây không phải “trộn khung phần mềm (framework / 프레임워크)”; đây là ánh xạ bất định (uncertainty / 불확실성) → bằng chứng (evidence / 증거) cơ chế (mechanism / 메커니즘).

Điểm quan trọng hơn là bất định (uncertainty / 불확실성) profile có thể **di chuyển theo vòng đời (lifecycle / 생명주기)**. Lúc đầu yêu cầu (requirement / 요구사항) bất định (uncertainty / 불확실성) có thể cao; sau discovery nó giảm nhưng thực thi (execution / 실행) bất định (uncertainty / 불확실성) tăng khi nhiều phụ thuộc (dependency / 의존성) bắt đầu tương tác. Gần go-live, technical bất định (uncertainty / 불확실성) có thể giảm trong khi adoption và operational bất định (uncertainty / 불확실성) trở thành dominant. Tailoring trưởng thành phải theo dõi sự dịch chuyển này thay vì giữ nguyên tiến trình (process / 프로세스) vì “đã thống nhất từ đầu”.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Nhiều vòng phản hồi (feedback loop / 피드백 루프) có cadence khác nhau** tiếp nhận điểm tựa từ **Mixed bất định (uncertainty / 불확실성) profile: một dự án (project / 프로젝트) có nhiều lô-gic (logic / 논리) delivery cùng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decision-flip kiểm thử (test / 테스트): variable nào làm approach phải đổi?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhiều vòng phản hồi (feedback loop / 피드백 루프) có cadence khác nhau

Một dự án (project / 프로젝트) có thể có customer phản hồi (feedback / 피드백) mỗi tuần, kiểm thử tích hợp (integration test / 통합 테스트) mỗi hai tuần, vendor đặc tả hợp đồng (contract / 계약) rà soát (review / 검토) mỗi tháng và regulatory gate mỗi quý. Nếu chỉ chọn một cadence chung, hoặc phản hồi (feedback / 피드백) nhanh bị chặn bởi gate chậm, hoặc quản trị (governance / 거버넌스) phải họp quá thường xuyên mà không có bằng chứng (evidence / 증거) mới.

Do đó cần phân biệt **cục bộ (local / 로컬) cadence** và **synchronization điểm (point / 지점)**. nhóm (team / 팀) có thể inspect/adapt nhanh bên trong ranh giới (boundary / 경계) nhưng chỉ synchronize với bên ngoài (external / 외부) authority khi đủ thông tin (information / 정보). Tuy nhiên synchronization quá thưa tạo batch rủi ro (risk / 위험): nhiều quyết định (decision / 결정) nội bộ tích tụ rồi va vào regulatory/vendor ranh giới (boundary / 경계) một lần.

Một thiết kế (design / 설계) tốt giảm khoảng cách giữa các cadence ở những giao diện (interface / 인터페이스) có coupling cao. Nếu sản phẩm (product / 제품) backlog thay đổi hàng tuần nhưng vendor giao diện (interface / 인터페이스) freeze mỗi ba tháng, dự án (project / 프로젝트) cần tính tương thích (compatibility / 호환성)/versioning hoặc thay đổi (change / 변경) cửa sổ (window / 윈도우) rõ; nếu không, cục bộ (local / 로컬) agility tạo downstream rework.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Decision-flip kiểm thử (test / 테스트): variable nào làm approach phải đổi?** tiếp nhận điểm tựa từ **Nhiều vòng phản hồi (feedback loop / 피드백 루프) có cadence khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Methodology inertia và tailoring debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decision-flip kiểm thử (test / 테스트): variable nào làm approach phải đổi?

Một cách kiểm tra tailoring có lô-gic (logic / 논리) hay không là hỏi: **điều gì nếu thay đổi sẽ khiến ta chọn cơ chế (mechanism / 메커니즘) khác?** Nếu câu trả lời là “không gì cả vì công ty luôn làm Scrum/Waterfall”, approach đang dựa trên định danh (identity / 식별자) chứ không dựa trên ngữ cảnh (context / 맥락).

Ví dụ nếu phản hồi (feedback / 피드백) có thể lấy trong hai ngày thay vì ba tháng, adaptive experimentation trở nên đáng giá hơn. Nếu thay đổi (change / 변경) trở nên gần như irreversible sau fabrication, commitment cần sớm và điều khiển (control / 제어) mạnh hơn. Nếu regulation bỏ mandatory gate, quản trị (governance / 거버넌스) có thể nhẹ hơn. Nếu automated testing làm regression chi phí (cost / 비용) giảm mạnh, batch/bản phát hành (release / 릴리스) chiến lược (strategy / 전략) có thể thay đổi. Nếu nhóm (team / 팀) chưa đủ skill để decentralized quyết định (decision / 결정), autonomy ranh giới (boundary / 경계) phải hẹp hơn dù bất định (uncertainty / 불확실성) vẫn cao.

Decision-flip kiểm thử (test / 테스트) buộc nhóm (team / 팀) nêu **nhân quả (causal / 인과적) variable** đứng sau methodology. Nó cũng giúp rà soát (review / 검토) tailoring khi ngữ cảnh (context / 맥락) đổi: ta không hỏi “có nên Agile hơn không?”, mà hỏi “phản hồi (feedback / 피드백) economics, irreversibility, coupling hoặc điều khiển (control / 제어) consequence đã thay đổi chưa?”.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Methodology inertia và tailoring debt** tiếp nhận điểm tựa từ **Decision-flip kiểm thử (test / 테스트): variable nào làm approach phải đổi?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tailoring quyết định (decision / 결정) example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Methodology inertia và tailoring debt

Một tiến trình (process / 프로세스) từng hợp lý có thể trở thành overhead khi ngữ cảnh (context / 맥락) đổi. Pilot nhỏ ban đầu có approval nhẹ; khi quy mô (scale / 규모) sang nhiều country và personal dữ liệu (data / 데이터), điều khiển (control / 제어) cũ có thể quá yếu. Ngược lại, emergency controls thêm sau sự cố (incident / 인시던트) có thể vẫn tồn tại nhiều năm dù automation và năng lực (capability / 역량) đã làm rủi ro (risk / 위험) giảm.

Đây có thể xem như **tailoring debt**: khoảng cách giữa tiến trình (process / 프로세스) hiện tại và điều khiển (control / 제어) kiến trúc (architecture / 아키텍처) mà ngữ cảnh (context / 맥락) bây giờ thực sự cần. Tailoring debt tăng khi organization không retire điều khiển (control / 제어) cũ, không thêm điều khiển (control / 제어) mới khi exposure tăng, hoặc giữ cadence/authority của giai đoạn trước.

Rà soát (review / 검토) vòng đời (lifecycle / 생명주기) nên vì thế hỏi không chỉ “tiến trình (process / 프로세스) có được follow không?” mà còn “tiến trình (process / 프로세스) này còn đúng bài toán (problem / 문제) không?”. Compliance với một tiến trình (process / 프로세스) lỗi thời không phải maturity.

> **Chuyển mạch:** Ở chặng này của **01 — Vòng đời, delivery approach và tailoring**, **Methodology inertia và tailoring debt** cho ta quy tắc; **Tailoring quyết định (decision / 결정) example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Counterexample: Agile không phải lúc nào giảm rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tailoring quyết định (decision / 결정) example

Dự án eKYC phải tích hợp vendor, đáp ứng privacy/bảo mật (security / 보안), vượt UAT với ngân hàng, nhưng UI và luồng (flow / 흐름) onboarding còn cần người dùng (user / 사용자) phản hồi (feedback / 피드백). Approach hợp lý có thể là hybrid: compliance/bảo mật (security / 보안) gates và vendor milestones được quản lý bằng acceptance criteria/baseline rõ; UX được iteratively refined; tích hợp (integration / 통합) rủi ro (risk / 위험) được prototype sớm; triển khai (deployment / 배포) có cutover plan riêng.

Nếu vendor API còn chưa ổn định, tích hợp (integration / 통합) spike nên xảy ra sớm hơn việc hoàn thiện toàn bộ UI. Nếu regulator có deadline cứng, mandatory compliance phạm vi (scope / 범위) phải được phân biệt với optional tính năng (feature / 기능). Nếu người dùng (user / 사용자) phản hồi (feedback / 피드백) chỉ có thể nhận sau pilot, dự án (project / 프로젝트) cần thiết kế pilot như một học tập (learning / 학습) milestone chứ không chỉ là demo.

Điểm quan trọng không phải tên methodology mà là từng cơ chế (mechanism / 메커니즘) đang giải quyết bất định (uncertainty / 불확실성) hoặc ràng buộc (constraint / 제약조건) nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **01 — Vòng đời, delivery approach và tailoring**, **Tailoring quyết định (decision / 결정) example** cho ta quy tắc; **Counterexample: Agile không phải lúc nào giảm rủi ro (risk / 위험)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterexample: Agile không phải lúc nào giảm rủi ro (risk / 위험)

Giả sử hardware cần đặt trước sáu tháng và vendor chỉ chấp nhận một giao diện (interface / 인터페이스) phiên bản (version / 버전) trước fabrication. Nếu nhóm (team / 팀) trì hoãn giao diện (interface / 인터페이스) quyết định (decision / 결정) quá lâu với lý do “giữ option”, họ có thể bỏ lỡ procurement cửa sổ (window / 윈도우). Trong ngữ cảnh (context / 맥락) này, early commitment ở ranh giới (boundary / 경계) hardware lại giảm rủi ro (risk / 위험).

Ngược lại, nếu UI preference chưa rõ mà dự án (project / 프로젝트) freeze toàn bộ tương tác (interaction / 상호작용) thiết kế (design / 설계) cùng lúc với hardware giao diện (interface / 인터페이스), commitment đó không mang thêm coordination giá trị (value / 값). Tailoring tốt tách hai loại bất định (uncertainty / 불확실성) thay vì dùng một ideology cho toàn hệ thống.

> **Chuyển mạch:** Trong **01 — Vòng đời, delivery approach và tailoring**, **Counterexample: Agile không phải lúc nào giảm rủi ro (risk / 위험)** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Chọn delivery approach là chọn vị trí đặt phản hồi (feedback / 피드백), commitment và điều khiển (control / 제어). Tailoring tốt đồng bộ bất định (uncertainty / 불확실성), phản hồi (feedback / 피드백) độ trễ (latency / 지연 시간), reversibility, quản trị (governance / 거버넌스) chi phí (cost / 비용) và organizational năng lực (capability / 역량) để mỗi commitment xảy ra khi bằng chứng (evidence / 증거) đủ mạnh.

Tiếp theo: [People, leadership, team và conflict](./02_people_leadership_team_and_conflict.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
