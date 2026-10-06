# Machine học tập (learning / 학습) foundations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Machine learning foundations**. Route đi từ supervised/unsupervised objectives → features/representations → loss/training/validation → overfitting/regularization → distribution shift và leakage, để generalization được tách khỏi memorization.

Machine học tập (learning / 학습) xây các mô hình (models / 모델들) từ dữ liệu (data / 데이터) thay vì hand-code toàn bộ ánh xạ (mapping / 매핑) đầu vào (input / 입력)→đầu ra (output / 출력). Nhưng “học từ dữ liệu (data / 데이터)” không có nghĩa mô hình (model / 모델) tự tìm chân lý. học tập (learning / 학습) luôn xảy ra trong hypothesis không gian (space / 공간), mục tiêu (objective / 목표), dữ liệu (data / 데이터) phân phối (distribution / 분포) và evaluation giao thức (protocol / 프로토콜) do con người/hệ thống (system / 시스템) thiết kế.

## Supervised học tập (learning / 학습)

Ta có examples `(x, y)` và muốn học hàm (function / 함수) `f(x) ≈ y`. Classification dự đoán category; regression dự đoán numeric mục tiêu (target / 대상).

Huấn luyện (training / 학습) chọn parameters giảm mất mát (loss / 손실) trên dữ liệu huấn luyện (training data / 학습 데이터); mục tiêu thật là generalization trên unseen dữ liệu (data / 데이터) từ mục tiêu (target / 대상) phân phối (distribution / 분포).

> **Nối mạch:** Supervised learning học từ nhãn; unsupervised tìm cấu trúc không nhãn, còn self-supervised tạo tín hiệu từ chính dữ liệu. Features và representation quyết định mô hình thấy được tín hiệu nào.

## Unsupervised và self-supervised

Unsupervised học tập (learning / 학습) tìm cấu trúc (structure / 구조) không có tường minh (explicit / 명시적) labels, như clustering/dimensionality reduction.

Self-supervised học tập (learning / 학습) tạo supervision từ cấu trúc (structure / 구조) của dữ liệu (data / 데이터), ví dụ predict masked đơn vị từ (token / 토큰)/next đơn vị từ (token / 토큰). Labels không cần manual nhưng mục tiêu (objective / 목표) vẫn được designer chọn.

> **Nối mạch:** **Features và biểu diễn (representation / 표현)** nối từ **Unsupervised và self-supervised** sang **Hàm mất mát (loss function / 손실 함수)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Features và biểu diễn (representation / 표현)

Traditional ML phụ thuộc tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링). Deep học tập (learning / 학습) học representations qua multiple layers từ raw-ish đầu vào (input / 입력).

Nhưng biểu diễn (representation / 표현) vẫn quyết định what thông tin (information / 정보) available. Timestamp bị bỏ hoặc leakage tính năng (feature / 기능) được thêm có thể thay mô hình (model / 모델) hành vi (behavior / 동작) mạnh.

> **Nối mạch:** **Hàm mất mát (loss function / 손실 함수)** nối từ **Features và biểu diễn (representation / 표현)** sang **Huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàm mất mát (loss function / 손실 함수)

Mất mát (loss / 손실) biến prediction lỗi (error / 오류) thành scalar mục tiêu (objective / 목표) tối ưu hóa (optimization / 최적화). Mean squared lỗi (error / 오류) penalize squared residuals; cross-entropy phù hợp xác suất (probability / 확률) classification under dùng chung (common / 공통) các giả định (assumptions / 가정들).

Mất mát (loss / 손실) không phải nghiệp vụ (business / 비즈니스) chỉ số (metric / 지표). Một mô hình (model / 모델) giảm log-loss có thể không tối ưu fraud chi phí (cost / 비용) hoặc medical utility nếu threshold/chi phí (cost / 비용) asymmetry khác.

> **Nối mạch:** **Huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)** nối từ **Hàm mất mát (loss function / 손실 함수)** sang **Overfitting và underfitting**, vì cơ chế trước tạo đầu vào cho bước sau.

## Huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)

Dữ liệu huấn luyện (training data / 학습 데이터) fit parameters. kiểm tra hợp lệ (validation / 검증) dữ liệu (data / 데이터) chọn hyperparameters/mô hình (model / 모델) decisions. kiểm thử (test / 테스트) dữ liệu (data / 데이터) ước lượng final generalization và nên giữ độc lập khỏi tuning.

Repeatedly nhìn kiểm thử (test / 테스트) results rồi tune biến kiểm thử (test / 테스트) thành kiểm tra hợp lệ (validation / 검증) de facto.

> **Nối mạch:** **Overfitting và underfitting** nối từ **Huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) và kiểm thử (test / 테스트)** sang **Regularization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Overfitting và underfitting

Underfit: mô hình (model / 모델) quá hạn chế hoặc huấn luyện (training / 학습) chưa đủ để capture mẫu (pattern / 패턴). Overfit: mô hình (model / 모델) fit idiosyncrasies/noise của dữ liệu huấn luyện (training data / 학습 데이터) và generalize kém.

Bias-variance intuition giúp lập luận (reasoning / 추론): mô hình (model / 모델) sức chứa (capacity / 용량)/regularization/dữ liệu (data / 데이터) amount ảnh hưởng sự đánh đổi (trade-off / 트레이드오프).

> **Nối mạch:** **Regularization** nối từ **Overfitting và underfitting** sang **Phân phối (distribution / 분포) shift**, vì cơ chế trước tạo đầu vào cho bước sau.

## Regularization

L1/L2 penalties, dropout, early stopping, dữ liệu (data / 데이터) augmentation và architectural các ràng buộc (constraints / 제약조건들) đều hạn chế effective fitting hoặc encode prior các giả định (assumptions / 가정들).

Regularization không chỉ “chống overfit”; nó độ lệch (bias / 편향) học tập (learning / 학습) toward solutions được cho là plausible/simpler theo cơ chế (mechanism / 메커니즘).

> **Nối mạch:** **Phân phối (distribution / 분포) shift** nối từ **Regularization** sang **Dữ liệu (data / 데이터) leakage**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phân phối (distribution / 분포) shift

Mô hình (model / 모델) trained trên phân phối (distribution / 분포) A có thể thất bại (fail / 실패) khi môi trường vận hành (production / 운영 환경) phân phối (distribution / 분포) B thay. Covariate shift, label shift, concept drift là các forms khác nhau.

Monitoring cần nhìn đầu vào (input / 입력) phân phối (distribution / 분포), đầu ra (output / 출력) confidence, kết quả (outcome / 결과) labels nếu có và nghiệp vụ (business / 비즈니스) metrics.

> **Nối mạch:** **Phân phối (distribution / 분포) shift** đặt vấn đề; **Dữ liệu (data / 데이터) leakage** kiểm tra bằng chứng, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## Dữ liệu (data / 데이터) leakage

Leakage xảy ra khi huấn luyện (training / 학습) features chứa thông tin (information / 정보) không available at prediction thời gian (time / 시간) hoặc split làm same thực thể (entity / 엔터티)/thời gian (time / 시간) leak giữa train/kiểm thử (test / 테스트).

Mô hình (model / 모델) metrics có thể cực cao nhưng môi trường vận hành (production / 운영 환경) thất bại (fail / 실패). Split chiến lược (strategy / 전략) phải phản ánh triển khai (deployment / 배포) timeline/thực thể (entity / 엔터티) cấu trúc (structure / 구조).

> **Nối mạch:** **Dữ liệu (data / 데이터) leakage** đặt vấn đề; **Dùng chung (common / 공통) Misconceptions** kiểm tra bằng chứng, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Dùng chung (common / 공통) Misconceptions

**“Nhiều dữ liệu (data / 데이터) luôn tốt hơn.”** dữ liệu (data / 데이터) sai phân phối (distribution / 분포), noisy labels hoặc leakage có thể làm mô hình (model / 모델) tệ/misleading.

**“Accuracy cao nghĩa mô hình (model / 모델) tốt.”** lớp (class / 클래스) imbalance/chi phí (cost / 비용) asymmetry có thể làm accuracy vô nghĩa.

**“mô hình (model / 모델) học mục tiêu (objective / 목표) chúng ta muốn.”** Nó tối ưu proxy mất mát (loss / 손실) trên dữ liệu (data / 데이터); proxy mismatch là nguồn thất bại (failure / 실패) lớn.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> ML là tối ưu hóa (optimization / 최적화) trên dữ liệu (data / 데이터) dưới các giả định (assumptions / 가정들). Generalization—not huấn luyện (training / 학습) fit—is mục tiêu; evaluation phải mô phỏng triển khai (deployment / 배포) reality.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Xem [statistics/inference](../../mathematics/06_probability_statistics/05_descriptive_and_inferential_statistics.md), [optimization](../../mathematics/08_optimization_numerical/00_optimization.md), [neural networks](./03_neural_networks_and_representation_learning.md) và [AI evaluation](./04_ai_evaluation_data_and_responsibility.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
