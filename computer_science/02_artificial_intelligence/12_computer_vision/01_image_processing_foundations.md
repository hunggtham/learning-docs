# Xử lý ảnh (image processing / 이미지 처리) Foundations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Image processing foundations**. Route đi từ pixel transforms → local convolution/filtering → padding/boundaries → denoising/edges → preprocessing for models, để thao tác ảnh được nối với tín hiệu cần giữ lại.

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

Convolution áp dụng kernel cục bộ; padding quyết định thông tin ở boundary. Từ cách xử lý vùng thiếu hàng xóm này, blur/noise reduction cho thấy filter đánh đổi chi tiết lấy ổn định như thế nào.

## Padding và ranh giới (boundary / 경계)

Kernel gần border thiếu neighbors. Strategies:

- zero padding;
- reflect;
- replicate;
- valid/no padding.

Ranh giới (boundary / 경계) choice ảnh hưởng đầu ra (output / 출력) dimension và artifacts.

Padding và ranh giới đã nêu cách giữ hoặc làm mất thông tin ở mép ảnh; blur và noise reduction cho thấy lựa chọn đó ảnh hưởng đến chi tiết ra sao. Bước kế tiếp dùng edges và gradients để đo những thay đổi còn lại.

## Blur và Noise Reduction

Gaussian blur:

\[
G(x,y)=\frac{1}{2\pi\sigma^2}e^{-(x^2+y^2)/(2\sigma^2)}
\]

ưu tiên center pixels và suppress high-frequency noise.

Nhưng blur cũng xóa edges/fine detail. Denoising luôn là signal-vs-detail sự đánh đổi (trade-off / 트레이드오프).

Blur giảm nhiễu nhưng cũng có thể làm mờ biên; edges và gradients biến sự thay đổi cường độ đó thành tín hiệu có thể đo. Canny Edge Detection tiếp tục tổ chức tín hiệu này thành một chuỗi phát hiện biên có kiểm soát.

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

Canny tách việc làm trơn, đo gradient và nối các biên thành từng bước; thresholding sẽ đặt một tiêu chí rõ ràng để biến tín hiệu liên tục thành vùng nhị phân.

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

Thresholding quyết định điểm ảnh nào thuộc foreground dựa trên mức cường độ; morphology dùng mask đó để sửa nhiễu nhỏ, lấp lỗ và nối các vùng theo hình dạng.

## Thresholding

Nhị phân (binary / 이진) segmentation đơn giản:

\[
B(x,y)=1[I(x,y)>T]
\]

Toàn cục (global / 전역) threshold thất bại (fail / 실패) nếu illumination nonuniform. Adaptive threshold dùng cục bộ (local / 로컬) statistics.

Otsu phương thức (method / 메서드) chọn threshold để separate classes theo between-class variance giả định (assumption / 가정).

Morphological operations thay đổi mask theo structuring element, nhưng chưa nói mỗi vùng thuộc về đối tượng nào. Connected components gắn các điểm ảnh liên thông thành những vùng có thể đo được.

## Morphological Operations

Với nhị phân (binary / 이진) mask và structuring element:

- **erosion (침식)** shrink foreground;
- **dilation (팽창)** expand foreground;
- opening = erosion then dilation;
- closing = dilation then erosion.

Dùng để remove small noise, fill holes, connect components.

Connected components cung cấp area, centroid và bounding box cho từng vùng; histogram bổ sung một góc nhìn khác bằng cách tóm tắt phân bố cường độ của toàn ảnh hoặc một vùng.

## Connected Components

Nhị phân (binary / 이진) mask có thể được group thành connected regions. thành phần (component / 컴포넌트) properties như area, centroid, bounding box rất hữu ích cho OCR/inspection pipelines.

Histogram cho biết phân bố cường độ và giúp đánh giá việc tăng tương phản; khi cần thay đổi vị trí hoặc hình học của ảnh, geometric transformations sẽ mô tả phép biến đổi tọa độ tương ứng.

## Histograms

Intensity histogram mô tả frequency của điểm ảnh (pixel / 픽셀) values. Histogram equalization redistribute contrast; CLAHE làm cục bộ (local / 로컬) adaptive enhancement.

Nhưng contrast enhancement có thể amplify noise.

Geometric transformations di chuyển hoặc chiếu lại tọa độ; interpolation quyết định giá trị nào được gán cho các tọa độ không nguyên sinh ra sau phép biến đổi.

## Geometric Transformations

Affine transform:

\[
\begin{bmatrix}x'\\y'\end{bmatrix}=A\begin{bmatrix}x\\y\end{bmatrix}+b
\]

cover translation, rotation, quy mô (scale / 규모), shear.

Perspective/homography cần projective transform để map planes under viewpoint thay đổi (change / 변경).

Interpolation lấp các giá trị khi resize hoặc warp, đồng thời phải giữ đúng ngữ nghĩa của ảnh và mask. Frequency domain cho phép nhìn các thay đổi đó theo thành phần tần số.

## Interpolation

Resize/warp cần estimate điểm ảnh (pixel / 픽셀) values at non-integer coordinates:

- nearest neighbor;
- bilinear;
- bicubic.

Nearest preserves labels for masks better; bilinear smoother for images. Dùng interpolation sai cho segmentation mask có thể tạo lớp (class / 클래스) IDs invalid.

Interpolation chọn cách lấp giá trị cho tọa độ không nguyên và phải bảo toàn ngữ nghĩa của ảnh hoặc mask. Frequency domain cung cấp một cách nhìn khác để phân tích những biến đổi này theo thành phần tần số.

## Frequency lĩnh vực (domain / 도메인)

2D Fourier transform decompose ảnh (image / 이미지) into spatial frequencies. Convolution in spatial lĩnh vực (domain / 도메인) corresponds multiplication in frequency lĩnh vực (domain / 도메인).

Low-pass filters smooth; high-pass emphasize edges.

Frequency view giúp hiểu blur, periodic noise và compression.

Frequency domain tách biến thiên chậm và nhanh, giúp giải thích blur, noise và cạnh. JPEG intuition dùng chính sự phân tách đó để lý giải việc nén loại bỏ chi tiết như thế nào.

## JPEG Intuition

JPEG chia blocks, transform qua DCT, quantize frequency coefficients rồi entropy-code. mất mát (loss / 손실) chủ yếu đến từ quantization; high-frequency details bị bỏ mạnh hơn.

Compression artifacts có thể ảnh hưởng mô hình (model / 모델) nếu train/kiểm thử (test / 테스트) compression khác nhau.

JPEG minh họa một chuỗi xử lý có chủ đích: giữ thành phần quan trọng và chấp nhận mất mát ở tần số cao. Ví dụ document scan cho thấy các phép xử lý cổ điển phối hợp ra sao trong một pipeline cụ thể.

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

Pipeline document scan cho thấy các phép cổ điển vẫn phù hợp khi đầu vào có cấu trúc và mục tiêu rõ. Khi cần học các phép biến đổi cùng mô hình, differentiable image operations mở rộng cùng nguyên lý đó vào quá trình huấn luyện.

## When Classical Processing Still Wins

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- deterministic industrial inspection;
- tiny compute ngân sách (budget / 예산);
- obvious geometric quy tắc (rule / 규칙);
- pre/postprocessing around neural mô hình (model / 모델);
- mask cleanup;
- document normalization.

Không phải mọi vision bài toán (problem / 문제) cần deep mạng (network / 네트워크).

Classical processing thắng khi quy tắc hình học, ngân sách tính toán hoặc điều kiện thu nhận đã đủ ổn định. Differentiable image operations giữ trực giác này nhưng cho phép gradient đi qua các phép xử lý; mô hình tư duy ở cuối bài sẽ gom lại ranh giới đó.

## Differentiable ảnh (image / 이미지) Operations

Nhiều processing operations có differentiable equivalents và trở thành layers/augmentations inside neural huấn luyện (training / 학습).

Differentiable operations cho thấy xử lý ảnh và học sâu có thể nằm trong cùng một chuỗi tối ưu. Mô hình tư duy dưới đây tóm tắt điều gì được đo, điều gì được học, và những giả định nào vẫn cần kiểm tra trước khi sang các ngộ nhận thường gặp.

## Mô hình tư duy (mental model / 사고 모델)

> **xử lý ảnh (image processing / 이미지 처리) thay đổi đo lường (measurement / 측정) để cấu trúc (structure / 구조) cần thiết trở nên dễ detect hơn. Deep học tập (learning / 학습) chủ yếu thay hand-designed tính năng (feature / 기능) extraction bằng learned representations, không xóa bỏ signal-processing foundations.**

Mô hình tư duy giúp phân biệt thay đổi phép đo với việc học biểu diễn; các ngộ nhận tiếp theo kiểm tra những ranh giới này qua các ví dụ cụ thể. Sau đó, phần liên kết kiến thức sẽ đặt chúng vào lộ trình rộng hơn.

## Dùng chung (common / 공통) Misconceptions

### “Deep học tập (learning / 학습) làm xử lý ảnh (image processing / 이미지 처리) lỗi thời”

Không. Resize, normalization, augmentation, filtering và geometric transforms vẫn ở mọi chuỗi xử lý (pipeline / 파이프라인).

### “Sharpen luôn tăng thông tin (information / 정보)”

Sharpen tăng cục bộ (local / 로컬) contrast; không tạo detail thật đã mất.

### “Thresholding là segmentation giống deep segmentation”

Cùng đầu ra (output / 출력) mask nhưng các giả định (assumptions / 가정들)/năng lực (capability / 역량) rất khác.

Các ngộ nhận cho thấy preprocessing, thresholding và sharpening đều có giả định riêng; vì vậy, phần liên kết kiến thức sẽ chỉ rõ những nền tảng cần quay lại và nhánh học tiếp theo.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Convolution/filtering là cầu nối (bridge / 브리지) trực tiếp tới CNN; độ dốc (gradient / 기울기)/frequency connect Calculus và tín hiệu (signal / 신호) Processing.

Xem tiếp: [Feature Representation](./02_feature_representation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
