# Độ lệch (bias / 편향), Variance và Generalization

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Độ lệch (bias / 편향), Variance và Generalization**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Huấn luyện (training / 학습) lỗi (error / 오류) không phải mục tiêu cuối** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **Độ lệch (bias / 편향) trong độ lệch (bias / 편향)–variance decomposition** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối bias-variance với generalization, noise và model complexity, để chọn độ phức tạp theo sai số ngoài mẫu.

Machine học tập (learning / 학습) không được đánh giá bằng khả năng nhớ dữ liệu huấn luyện (training data / 학습 데이터), mà bằng khả năng **generalize (일반화 / khái quát hóa)** sang những examples chưa thấy nhưng đến từ môi trường (environment / 환경) mục tiêu. Đây là điểm phân biệt học tập (learning / 학습) với memorization.

Ba concept giúp lập luận (reasoning / 추론) về vấn đề này là **độ lệch (bias / 편향)**, **variance** và **irreducible noise**. Chúng không phải chỉ là vocabulary để giải thích overfitting; chúng là khung phần mềm (framework / 프레임워크) để hiểu mô hình (model / 모델) sức chứa (capacity / 용량), regularization, dữ liệu (data / 데이터) kích thước (size / 크기) và ensemble methods.

## Huấn luyện (training / 학습) lỗi (error / 오류) không phải mục tiêu cuối

Một mô hình (model / 모델) có thể đạt gần zero huấn luyện (training / 학습) mất mát (loss / 손실) bằng cách memorize dataset. Nếu future đầu vào (input / 입력) khác huấn luyện (training / 학습) examples, prediction có thể thất bại.

Ta quan tâm expected rủi ro (risk / 위험):

\[
R(f)=\mathbb E_{(X,Y)\sim P}[L(Y,f(X))]
\]

nhưng chỉ quan sát finite mẫu (sample / 표본). kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) thiết kế (design / 설계) cố estimate rủi ro (risk / 위험) này dưới các giả định (assumptions / 가정들) về future phân phối (distribution / 분포).

Generalization gap:

\[
Gap=R_{kiểm thử (test / 테스트)}-R_{train}
\]

là một tín hiệu (signal / 신호), nhưng interpretation phụ thuộc split representativeness.

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **Độ lệch (bias / 편향) trong độ lệch (bias / 편향)–variance decomposition** tiếp nhận điểm tựa từ **Huấn luyện (training / 학습) lỗi (error / 오류) không phải mục tiêu cuối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Underfitting và Overfitting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향) trong độ lệch (bias / 편향)–variance decomposition

Ở đây **độ lệch (bias / 편향)** không phải xã hội (social / 사회적) độ lệch (bias / 편향). Nó là systematic lỗi (error / 오류) do mô hình (model / 모델) lớp (class / 클래스)/học tập (learning / 학습) procedure không thể hoặc không có xu hướng capture true relationship.

Với squared lỗi (error / 오류) regression:

\[
\mathbb E[(Y-\hat f(x))^2]
=độ lệch (bias / 편향)^2+Variance+Noise
\]

một decomposition simplified dưới các giả định (assumptions / 가정들) phù hợp.

Độ lệch (bias / 편향) cao: mô hình (model / 모델) consistently miss cấu trúc (structure / 구조), ví dụ fit straight line cho relationship rất cong.

Variance cao: mô hình (model / 모델) thay đổi mạnh nếu huấn luyện (training / 학습) mẫu (sample / 표본) thay đổi nhẹ.

Noise: bất định (uncertainty / 불확실성) không thể loại hết chỉ bằng mô hình (model / 모델) tốt hơn với observed features.

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, **Underfitting và Overfitting** tiếp nhận điểm tựa từ **Độ lệch (bias / 편향) trong độ lệch (bias / 편향)–variance decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Underfitting và Overfitting

**Underfitting** thường liên quan sức chứa (capacity / 용량) quá thấp, tính năng (feature / 기능) biểu diễn (representation / 표현) nghèo hoặc tối ưu hóa (optimization / 최적화) chưa đủ. huấn luyện (training / 학습) lỗi (error / 오류) và kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) đều cao.

**Overfitting** xảy ra khi mô hình (model / 모델) học details/noise specific huấn luyện (training / 학습) mẫu (sample / 표본) khiến kiểm tra hợp lệ (validation / 검증)/generalization kém. huấn luyện (training / 학습) lỗi (error / 오류) thấp nhưng kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) cao.

Tuy nhiên hiện đại (modern / 현대적) Deep học tập (learning / 학습) làm simple textbook picture phức tạp hơn: overparameterized networks có thể interpolate dữ liệu huấn luyện (training data / 학습 데이터) vẫn generalize tốt nhờ implicit/tường minh (explicit / 명시적) regularization, dữ liệu (data / 데이터) quy mô (scale / 규모) và tối ưu hóa (optimization / 최적화) độ lệch (bias / 편향).

Vì vậy “parameters > samples ⇒ chắc chắn overfit” không phải quy tắc (rule / 규칙) universal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ lệch (bias / 편향), Variance và Generalization**, **Mô hình (model / 모델) sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **Underfitting và Overfitting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inductive độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) sức chứa (capacity / 용량)

Sức chứa (capacity / 용량) mô tả richness của hàm (function / 함수) lớp (class / 클래스) mô hình (model / 모델) có thể represent.

Examples:

- tuyến tính (linear / 선형) regression với vài features: sức chứa (capacity / 용량) thấp;
- deep cây (tree / 트리): sức chứa (capacity / 용량) cao hơn;
- large neural mạng (network / 네트워크): rất cao.

Sức chứa (capacity / 용량) cao giảm approximation độ lệch (bias / 편향) nhưng mở nhiều solutions fit noise. Regularization và dữ liệu (data / 데이터) constrain học tập (learning / 학습) tiến trình (process / 프로세스) để chọn solution có generalization tốt hơn.

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **Inductive độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Mô hình (model / 모델) sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Regularization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inductive độ lệch (bias / 편향)

Không mô hình (model / 모델) nào học từ finite dữ liệu (data / 데이터) mà hoàn toàn không giả định (assumption / 가정).

Mô hình tuyến tính (linear model / 선형 모델) assume useful relationship gần tuyến tính (linear / 선형) trong biểu diễn (representation / 표현). CNN assume locality/translation cấu trúc (structure / 구조). cây (tree / 트리) assume recursive tính năng (feature / 기능) partitions. Transformer attention assume đơn vị từ (token / 토큰) interactions có thể học từ content-dependent weighted mixing.

Inductive độ lệch (bias / 편향) tốt làm sample-efficient hơn nếu phù hợp lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, **Regularization** tiếp nhận điểm tựa từ **Inductive độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **More dữ liệu (data / 데이터) thay đổi sự đánh đổi (trade-off / 트레이드오프) thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regularization

### Tường minh (explicit / 명시적) Regularization

L2:

\[
J=\hat R+\lambda\|\theta\|_2^2
\]

L1, dropout, label smoothing, dữ liệu (data / 데이터) augmentation và early stopping đều có regularization effects khác nhau.

### Early Stopping

Trong iterative huấn luyện (training / 학습), kiểm tra hợp lệ (validation / 검증) hiệu năng (performance / 성능) có thể tốt nhất trước khi huấn luyện (training / 학습) mất mát (loss / 손실) minimum. Stop sớm hạn chế mô hình (model / 모델) tiếp tục fit sample-specific details.

### Dữ liệu (data / 데이터) Augmentation

Ảnh (image / 이미지) flips/crops, audio perturbations hoặc văn bản (text / 텍스트) transformations encode invariances: label nên không đổi dưới những transformations hợp lệ.

Augmentation không chỉ “tạo thêm dữ liệu (data / 데이터)”; nó inject inductive độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ lệch (bias / 편향), Variance và Generalization**, **Regularization** nêu điều cần giải thích; **More dữ liệu (data / 데이터) thay đổi sự đánh đổi (trade-off / 트레이드오프) thế nào?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Học tập (learning / 학습) Curves** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## More dữ liệu (data / 데이터) thay đổi sự đánh đổi (trade-off / 트레이드오프) thế nào?

Với fixed useful mô hình (model / 모델) lớp (class / 클래스), thêm representative dữ liệu (data / 데이터) thường giảm variance và làm estimate stable hơn.

Nhưng thêm dữ liệu (data / 데이터) từ wrong phân phối (distribution / 분포) có thể không giúp. Duplicate, low-quality hoặc biased dữ liệu (data / 데이터) cũng không tương đương independent thông tin (information / 정보) mới.

Dataset kích thước (size / 크기) nên nghĩ theo **effective diversity and coverage**, không chỉ row count.

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **More dữ liệu (data / 데이터) thay đổi sự đánh đổi (trade-off / 트레이드오프) thế nào?** nêu điều cần giải thích; **Học tập (learning / 학습) Curves** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Cross-Validation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Học tập (learning / 학습) Curves

Plot huấn luyện (training / 학습)/kiểm tra hợp lệ (validation / 검증) hiệu năng (performance / 성능) theo training-set kích thước (size / 크기) giúp diagnose:

- cả hai lỗi (error / 오류) cao và gần nhau → possible high độ lệch (bias / 편향);
- huấn luyện (training / 학습) tốt, kiểm tra hợp lệ (validation / 검증) kém với gap lớn → high variance;
- kiểm tra hợp lệ (validation / 검증) tiếp tục improve rõ khi thêm dữ liệu (data / 데이터) → more dữ liệu (data / 데이터) likely useful.

Học tập (learning / 학습) curve thực dụng hơn việc gắn label “overfit” chỉ từ một chỉ số (metric / 지표) snapshot.

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, **Cross-Validation** tiếp nhận điểm tựa từ **Học tập (learning / 학습) Curves** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) Shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Validation

k-fold cross-validation chia dữ liệu (data / 데이터) thành `k` folds; mỗi lần train trên `k-1`, validate fold còn lại.

Nó giảm dependence vào một random split và estimate variability.

Nhưng random k-fold không hợp mọi bài toán (problem / 문제):

- thời gian (time / 시간) series cần forward/thời gian (time / 시간) split;
- multiple rows cùng người dùng (user / 사용자) cần group split;
- spatial dữ liệu (data / 데이터) có autocorrelation cần spatial split.

Kiểm tra hợp lệ (validation / 검증) scheme phải mimic triển khai (deployment / 배포) ranh giới (boundary / 경계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ lệch (bias / 편향), Variance và Generalization**, **Phân phối (distribution / 분포) Shift** tiếp nhận điểm tựa từ **Cross-Validation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Shortcut học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) Shift

Generalization lý thuyết (theory / 이론) thường assume train/kiểm thử (test / 테스트) từ same hoặc related phân phối (distribution / 분포). môi trường vận hành (production / 운영 환경) lại gặp shift.

Các dạng hữu ích:

- **covariate shift**: `P(X)` đổi;
- **label/prior shift**: `P(Y)` đổi;
- **concept shift**: relationship `P(Y|X)` đổi.

Ví dụ fraud hành vi (behavior / 동작) thay vì attacker adapt là concept drift.

Mô hình (model / 모델) có excellent IID kiểm thử (test / 테스트) score vẫn có thể thất bại (fail / 실패) dưới shift.

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **Shortcut học tập (learning / 학습)** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spurious Correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shortcut học tập (learning / 학습)

Mô hình (model / 모델) có thể exploit correlation dễ nhưng không robust.

Ví dụ medical ảnh (image / 이미지) classifier học hospital watermark thay vì pathology. huấn luyện (training / 학습)/kiểm thử (test / 테스트) random split cùng nguồn (source / 소스) có score cao, nhưng bên ngoài (external / 외부) hospital hiệu năng (performance / 성능) collapse.

Đây là generalization thất bại (failure / 실패) do biểu diễn (representation / 표현)/dữ liệu (data / 데이터) thiết kế (design / 설계), không chỉ “overfitting” theo parameter count.

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, **Spurious Correlation** tiếp nhận điểm tựa từ **Shortcut học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Double Descent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spurious Correlation

Nếu tính năng (feature / 기능) tương quan mục tiêu (target / 대상) vì historical accident, mô hình (model / 모델) có thể dùng nó. Khi triển khai (deployment / 배포) ngữ cảnh (context / 맥락) thay, correlation mất.

Lĩnh vực (domain / 도메인) kiến thức (knowledge / 지식) và stress tests cần để detect reliance vào brittle signals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ lệch (bias / 편향), Variance và Generalization**, **Double Descent** tiếp nhận điểm tựa từ **Spurious Correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ensemble và Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Double Descent

Classical intuition nói kiểm thử (test / 테스트) lỗi (error / 오류) giảm rồi tăng khi độ phức tạp (complexity / 복잡도) vượt optimum. hiện đại (modern / 현대적) overparameterized các mô hình (models / 모델들) đôi khi cho **double descent**: lỗi (error / 오류) tăng gần interpolation threshold rồi giảm lại khi mô hình (model / 모델) cực overparameterized.

Điều này nhắc rằng độ lệch (bias / 편향)–variance vẫn là mental khung phần mềm (framework / 프레임워크) hữu ích nhưng simple U-shaped curve không mô tả đầy đủ Deep học tập (learning / 학습).

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **Ensemble và Variance** tiếp nhận điểm tựa từ **Double Descent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Generalization trong LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ensemble và Variance

Bagging/Random Forest giảm variance bằng averaging partially independent các mô hình (models / 모델들).

Boosting thường giảm độ lệch (bias / 편향) qua additive correction nhưng cũng có regularization mechanisms như shrinkage/cây (tree / 트리) độ sâu (depth / 깊이)/subsampling.

Xem: [Ensemble Learning](./09_ensemble_learning.md).

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, **Generalization trong LLM** tiếp nhận điểm tựa từ **Ensemble và Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generalization trong LLM

LLM pretraining không chỉ “memorize internet”; mô hình (model / 모델) học statistical patterns và representations cho phép generalize tới unseen combinations/tasks. Nhưng memorization vẫn tồn tại, đặc biệt rare sequences.

In-context học tập (learning / 학습), lĩnh vực (domain / 도메인) shift, contamination và benchmark leakage làm generalization evaluation phức tạp hơn supervised tabular ML.

Các chapter LLM sau sẽ mở rộng distinction này.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ lệch (bias / 편향), Variance và Generalization**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Generalization trong LLM** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Observed sample
   ↓ learning algorithm + inductive bias
Chosen hypothesis
   ↓
Performance on new distribution
```

Nếu thất bại (fail / 실패), hãy hỏi bốn tầng:

```text
Representation có đủ signal?
Model capacity phù hợp?
Learning/regularization chọn solution nào?
Validation có giống deployment distribution?
```

> **Chuyển mạch:** Trong **Độ lệch (bias / 편향), Variance và Generalization**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Overfitting = mô hình (model / 모델) quá nhiều parameters”

Parameter count chỉ là một factor; dữ liệu (data / 데이터), kiến trúc (architecture / 아키텍처), regularization, tối ưu hóa (optimization / 최적화) và tác vụ (task / 작업) matter.

### “Train và kiểm thử (test / 테스트) đều tốt thì mô hình (model / 모델) đã robust”

Chỉ nếu kiểm thử (test / 테스트) đại diện triển khai (deployment / 배포). IID split có thể bỏ lỡ shift/shortcut.

### “Thêm dữ liệu (data / 데이터) luôn giải quyết overfitting”

Chỉ khi dữ liệu (data / 데이터) mới informative, diverse và relevant.

### “độ lệch (bias / 편향)–variance độ lệch (bias / 편향) là fairness độ lệch (bias / 편향)”

Không. Đây là statistical estimation độ lệch (bias / 편향); fairness độ lệch (bias / 편향) là concept khác.

> **Chuyển mạch:** Ở chặng này của **Độ lệch (bias / 편향), Variance và Generalization**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Generalization nối [Statistics for AI](../01_mathematical_foundations/03_statistics_for_ai.md), [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Ensemble Learning](./09_ensemble_learning.md) và [Model Evaluation](./15_model_evaluation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
