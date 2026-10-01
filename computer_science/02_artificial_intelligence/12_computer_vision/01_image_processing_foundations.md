# Xử lý ảnh (image processing / 이미지 처리) Foundations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Xử lý ảnh (image processing / 이미지 처리) Foundations**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Convolution như cục bộ (local / 로컬) filtering** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Padding và ranh giới (boundary / 경계)** để soi ranh giới và điểm dễ nhầm. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Trước Deep học tập (learning / 학습), Computer Vision dựa nhiều vào **xử lý ảnh (image processing / 이미지 처리)**: biến đổi tín hiệu ảnh để làm nổi bật cấu trúc (structure / 구조) hữu ích. Dù hiện đại (modern / 현대적) các mô hình (models / 모델들) học features tự động, các nguyên lý filtering, edges, morphology và frequency vẫn giúp hiểu dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) và thất bại (failure / 실패) modes.

## Convolution như cục bộ (local / 로컬) filtering

Với ảnh (image / 이미지) `I` và kernel `K`, convolution/discrete correlation practical form tính weighted sum neighborhood:

\[
Y(i,j)=\sum_m\sum_n K(m,n)I(i+m,j+n)
\]

Một kernel blur trung bình:

\[
\frac{1}{9}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
\]

làm smooth cục bộ (local / 로컬) variation.

Edge kernel như Sobel approximates spatial derivative. CNN sau này học kernels thay vì hand-design hoàn toàn.

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Convolution như cục bộ (local / 로컬) filtering** đã nêu tiêu chí phân biệt, còn **Padding và ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Blur và Noise Reduction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Padding và ranh giới (boundary / 경계)

Kernel gần border thiếu neighbors. Strategies:

- zero padding;
- reflect;
- replicate;
- valid/no padding.

Ranh giới (boundary / 경계) choice ảnh hưởng đầu ra (output / 출력) dimension và artifacts.

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Padding và ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Blur và Noise Reduction** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Edges và Gradients** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blur và Noise Reduction

Gaussian blur:

\[
G(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/(2\sigma^2)}
\]

ưu tiên center pixels và suppress high-frequency noise.

Nhưng blur cũng xóa edges/fine detail. Denoising luôn là signal-vs-detail sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Edges và Gradients** tiếp nhận điểm tựa từ **Blur và Noise Reduction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Canny Edge Detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Edges và Gradients

Edge là nơi intensity thay đổi nhanh. ảnh (image / 이미지) độ dốc (gradient / 기울기):

\[
\nabla I=(I_x,I_y)
\]

Magnitude:

\[
|\nabla I|=\sqrt{I_x^2+I_y^2}
\]

Direction cho orientation của cục bộ (local / 로컬) thay đổi (change / 변경).

Edges từng là cốt lõi (core / 핵심) thành phần nguyên thủy (primitive / 기본 요소) cho đối tượng (object / 객체) shape detection.

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Canny Edge Detection** tiếp nhận điểm tựa từ **Edges và Gradients** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thresholding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Canny Edge Detection

Canny chuỗi xử lý (pipeline / 파이프라인) classic:

```text
Gaussian smoothing
→ gradient computation
→ non-maximum suppression
→ double threshold
→ hysteresis tracking
```

Điểm đáng học là chuỗi xử lý (pipeline / 파이프라인) separates noise suppression, cục bộ (local / 로컬) bằng chứng (evidence / 증거) và connectivity lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Thresholding** tiếp nhận điểm tựa từ **Canny Edge Detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Morphological Operations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thresholding

Nhị phân (binary / 이진) segmentation đơn giản:

\[
B(x,y)=1[I(x,y)>T]
\]

Toàn cục (global / 전역) threshold thất bại (fail / 실패) nếu illumination nonuniform. Adaptive threshold dùng cục bộ (local / 로컬) statistics.

Otsu phương thức (method / 메서드) chọn threshold để separate classes theo between-class variance giả định (assumption / 가정).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Morphological Operations** tiếp nhận điểm tựa từ **Thresholding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Connected Components** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Morphological Operations

Với nhị phân (binary / 이진) mask và structuring element:

- **erosion (침식)** shrink foreground;
- **dilation (팽창)** expand foreground;
- opening = erosion then dilation;
- closing = dilation then erosion.

Dùng để remove small noise, fill holes, connect components.

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Connected Components** tiếp nhận điểm tựa từ **Morphological Operations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Histograms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Connected Components

Nhị phân (binary / 이진) mask có thể được group thành connected regions. thành phần (component / 컴포넌트) properties như area, centroid, bounding box rất hữu ích cho OCR/inspection pipelines.

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Histograms** tiếp nhận điểm tựa từ **Connected Components** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Geometric Transformations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Histograms

Intensity histogram mô tả frequency của điểm ảnh (pixel / 픽셀) values. Histogram equalization redistribute contrast; CLAHE làm cục bộ (local / 로컬) adaptive enhancement.

Nhưng contrast enhancement có thể amplify noise.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Geometric Transformations** tiếp nhận điểm tựa từ **Histograms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interpolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Geometric Transformations

Affine transform:

\[
\begin{bmatrix}x'\\y'\end{bmatrix}=A\begin{bmatrix}x\\y\end{bmatrix}+b
\]

cover translation, rotation, quy mô (scale / 규모), shear.

Perspective/homography cần projective transform để map planes under viewpoint thay đổi (change / 변경).

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Interpolation** tiếp nhận điểm tựa từ **Geometric Transformations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Frequency lĩnh vực (domain / 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interpolation

Resize/warp cần estimate điểm ảnh (pixel / 픽셀) values at non-integer coordinates:

- nearest neighbor;
- bilinear;
- bicubic.

Nearest preserves labels for masks better; bilinear smoother for images. Dùng interpolation sai cho segmentation mask có thể tạo lớp (class / 클래스) IDs invalid.

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Frequency lĩnh vực (domain / 도메인)** tiếp nhận điểm tựa từ **Interpolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JPEG Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Frequency lĩnh vực (domain / 도메인)

2D Fourier transform decompose ảnh (image / 이미지) into spatial frequencies. Convolution in spatial lĩnh vực (domain / 도메인) corresponds multiplication in frequency lĩnh vực (domain / 도메인).

Low-pass filters smooth; high-pass emphasize edges.

Frequency view giúp hiểu blur, periodic noise và compression.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **JPEG Intuition** tiếp nhận điểm tựa từ **Frequency lĩnh vực (domain / 도메인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Classical chuỗi xử lý (pipeline / 파이프라인) Example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JPEG Intuition

JPEG chia blocks, transform qua DCT, quantize frequency coefficients rồi entropy-code. mất mát (loss / 손실) chủ yếu đến từ quantization; high-frequency details bị bỏ mạnh hơn.

Compression artifacts có thể ảnh hưởng mô hình (model / 모델) nếu train/kiểm thử (test / 테스트) compression khác nhau.

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **JPEG Intuition** cho ta quy tắc; **Classical chuỗi xử lý (pipeline / 파이프라인) Example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **When Classical Processing Still Wins** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Classical chuỗi xử lý (pipeline / 파이프라인) Example

Document scan:

```text
gray
→ denoise
→ deskew
→ adaptive threshold
→ morphology
→ connected components
→ OCR
```

Một deep mô hình (model / 모델) có thể replace vài stage nhưng preprocessing vẫn hữu ích khi acquisition predictable.

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Classical chuỗi xử lý (pipeline / 파이프라인) Example** cho ta quy tắc; **When Classical Processing Still Wins** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Differentiable ảnh (image / 이미지) Operations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## When Classical Processing Still Wins

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- deterministic industrial inspection;
- tiny compute ngân sách (budget / 예산);
- obvious geometric quy tắc (rule / 규칙);
- pre/postprocessing around neural mô hình (model / 모델);
- mask cleanup;
- document normalization.

Không phải mọi vision bài toán (problem / 문제) cần deep mạng (network / 네트워크).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **When Classical Processing Still Wins** xác định đầu vào; **Differentiable ảnh (image / 이미지) Operations** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differentiable ảnh (image / 이미지) Operations

Nhiều processing operations có differentiable equivalents và trở thành layers/augmentations inside neural huấn luyện (training / 학습).

> **Chuyển mạch:** Trong **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Differentiable ảnh (image / 이미지) Operations** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **xử lý ảnh (image processing / 이미지 처리) thay đổi đo lường (measurement / 측정) để cấu trúc (structure / 구조) cần thiết trở nên dễ detect hơn. Deep học tập (learning / 학습) chủ yếu thay hand-designed tính năng (feature / 기능) extraction bằng learned representations, không xóa bỏ signal-processing foundations.**

> **Chuyển mạch:** Ở chặng này của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Deep học tập (learning / 학습) làm xử lý ảnh (image processing / 이미지 처리) lỗi thời”

Không. Resize, normalization, augmentation, filtering và geometric transforms vẫn ở mọi chuỗi xử lý (pipeline / 파이프라인).

### “Sharpen luôn tăng thông tin (information / 정보)”

Sharpen tăng cục bộ (local / 로컬) contrast; không tạo detail thật đã mất.

### “Thresholding là segmentation giống deep segmentation”

Cùng đầu ra (output / 출력) mask nhưng các giả định (assumptions / 가정들)/năng lực (capability / 역량) rất khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Xử lý ảnh (image processing / 이미지 처리) Foundations**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Convolution/filtering là cầu nối (bridge / 브리지) trực tiếp tới CNN; độ dốc (gradient / 기울기)/frequency connect Calculus và tín hiệu (signal / 신호) Processing.

Xem tiếp: [Feature Representation](./02_feature_representation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
