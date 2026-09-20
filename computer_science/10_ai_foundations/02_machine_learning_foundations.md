# Machine Learning foundations

Machine Learning (ML / 기계 학습) xây models từ data thay vì hand-code toàn bộ mapping input→output. Nhưng “học từ data” không có nghĩa model tự tìm chân lý. Learning luôn xảy ra trong hypothesis space, objective, data distribution và evaluation protocol do con người/system thiết kế.

## Supervised learning

Ta có examples `(x, y)` và muốn học function `f(x) ≈ y`. Classification dự đoán category; regression dự đoán numeric target.

Training chọn parameters giảm loss trên training data; mục tiêu thật là generalization trên unseen data từ target distribution.

## Unsupervised và self-supervised

Unsupervised learning tìm structure không có explicit labels, như clustering/dimensionality reduction.

Self-supervised learning tạo supervision từ structure của data, ví dụ predict masked token/next token. Labels không cần manual nhưng objective vẫn được designer chọn.

## Features và representation

Traditional ML phụ thuộc feature engineering. Deep learning học representations qua multiple layers từ raw-ish input.

Nhưng representation vẫn quyết định what information available. Timestamp bị bỏ hoặc leakage feature được thêm có thể thay model behavior mạnh.

## Loss function

Loss biến prediction error thành scalar objective optimization. Mean squared error penalize squared residuals; cross-entropy phù hợp probability classification under common assumptions.

Loss không phải business metric. Một model giảm log-loss có thể không tối ưu fraud cost hoặc medical utility nếu threshold/cost asymmetry khác.

## Training, validation và test

Training data fit parameters. Validation data chọn hyperparameters/model decisions. Test data ước lượng final generalization và nên giữ độc lập khỏi tuning.

Repeatedly nhìn test results rồi tune biến test thành validation de facto.

## Overfitting và underfitting

Underfit: model quá hạn chế hoặc training chưa đủ để capture pattern. Overfit: model fit idiosyncrasies/noise của training data và generalize kém.

Bias-variance intuition giúp reasoning: model capacity/regularization/data amount ảnh hưởng trade-off.

## Regularization

L1/L2 penalties, dropout, early stopping, data augmentation và architectural constraints đều hạn chế effective fitting hoặc encode prior assumptions.

Regularization không chỉ “chống overfit”; nó bias learning toward solutions được cho là plausible/simpler theo mechanism.

## Distribution shift

Model trained trên distribution A có thể fail khi production distribution B thay. Covariate shift, label shift, concept drift là các forms khác nhau.

Monitoring cần nhìn input distribution, output confidence, outcome labels nếu có và business metrics.

## Data leakage

Leakage xảy ra khi training features chứa information không available at prediction time hoặc split làm same entity/time leak giữa train/test.

Model metrics có thể cực cao nhưng production fail. Split strategy phải phản ánh deployment timeline/entity structure.

## Common Misconceptions

**“Nhiều data luôn tốt hơn.”** Data sai distribution, noisy labels hoặc leakage có thể làm model tệ/misleading.

**“Accuracy cao nghĩa model tốt.”** Class imbalance/cost asymmetry có thể làm accuracy vô nghĩa.

**“Model học objective chúng ta muốn.”** Nó tối ưu proxy loss trên data; proxy mismatch là nguồn failure lớn.

## Mental Model

> ML là optimization trên data dưới assumptions. Generalization—not training fit—is mục tiêu; evaluation phải mô phỏng deployment reality.

## Kết nối

Xem [statistics/inference](../../mathematics/06_probability_statistics/05_descriptive_and_inferential_statistics.md), [optimization](../../mathematics/08_optimization_numerical/00_optimization.md), [neural networks](./03_neural_networks_and_representation_learning.md) và [AI evaluation](./04_ai_evaluation_data_and_responsibility.md).