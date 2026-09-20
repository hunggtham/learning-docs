# Sinh học, Toán học, tính toán và scale — Biology, Mathematics, Computation and Scale (생물학·수학·계산·스케일)

Sinh học thường được dạy như một môn nhiều thuật ngữ, nhưng phần lớn modern biology dựa sâu vào toán học và computation. Khi số lượng molecule, cell, individual hoặc gene tăng lên, intuition thuần verbal không đủ. Ta cần model để mô tả rate, probability, network, feedback và uncertainty.

## Scale quyết định câu hỏi phù hợp

Một protein có thể được mô tả bằng structure và binding energy; một cell bằng network signaling; một organ bằng flow và transport; một population bằng birth–death process; một ecosystem bằng energy và nutrient cycle.

Không có một equation duy nhất nối trực tiếp mọi scale. Scientific reasoning thường cần coarse-graining: giữ variable quan trọng ở scale đang xét và bỏ bớt detail không cần thiết.

> Mental model: model tốt không phải model chứa nhiều detail nhất, mà là model giữ đúng detail để trả lời câu hỏi cụ thể.

## Tỷ lệ diện tích/thể tích

Nhiều constraint sinh học bắt nguồn từ geometry. Surface area tăng theo bình phương kích thước tuyến tính, còn volume tăng theo lập phương. Với sphere:

```math
A=4\pi r^2,\qquad V=\frac{4}{3}\pi r^3,\qquad \frac{A}{V}=\frac{3}{r}
```

Khi organism hoặc cell lớn hơn, exchange surface trên mỗi đơn vị volume giảm. Điều này giải thích microvilli, alveoli, branch của vascular system và giới hạn cell size.

## Exponential growth

Bacteria division, PCR amplification và population growth ban đầu thường gần exponential:

```math
N(t)=N_0e^{rt}
```

Điểm quan trọng là derivative của exponential tỷ lệ với chính số lượng hiện tại:

```math
\frac{dN}{dt}=rN
```

Cùng một mathematical structure xuất hiện ở compound interest, epidemic phase đầu và radioactive decay với dấu rate khác nhau.

## Logistic feedback

Khi resource hạn chế, growth có thể được approximate bằng:

```math
\frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
```

Factor `(1-N/K)` là negative feedback. Khi population tăng gần `K`, growth rate giảm.

Sinh học chứa rất nhiều feedback như vậy: glucose–insulin, hormone axis, gene circuit và predator–prey system.

## Probability trong genetics

Mendelian inheritance dùng multiplication rule và conditional probability. Population genetics dùng sampling distribution để hiểu drift. Medical testing dùng Bayes' theorem để chuyển từ test sensitivity/specificity sang xác suất disease sau khi biết result.

Bayes có dạng:

```math
P(H|D)=\frac{P(D|H)P(H)}{P(D)}
```

Trong screening disease hiếm, base rate `P(H)` có thể nhỏ đến mức nhiều positive result vẫn là false positive. Đây là lý do sensitivity cao không tự động làm positive predictive value cao.

## Statistics và biological variation

Biology hiếm khi cho hai sample giống hệt nhau. Variation có thể đến từ measurement noise, individual difference, batch effect hoặc stochastic process thật.

Mean và standard deviation chỉ mô tả distribution, không thay thế causal explanation. Confidence interval mô tả uncertainty của estimate. p-value không cho xác suất hypothesis đúng; nó đo mức độ dữ liệu tương thích với null model theo procedure cụ thể.

Multiple testing đặc biệt quan trọng trong genomics vì có thể kiểm tra hàng nghìn hoặc hàng triệu hypothesis cùng lúc.

## Differential equation và dynamics

Khi state thay đổi liên tục theo time, differential equation cho phép model rate of change. Enzyme kinetics, membrane voltage, hormone regulation và population dynamics đều có thể dùng dạng:

```math
\frac{dx}{dt}=f(x,t,p)
```

Fixed point là state nơi derivative bằng zero. Stability analysis hỏi system quay lại hay rời xa fixed point sau perturbation.

## Network và graph

Protein interaction, gene regulation, neural connection, food web và phylogenetic relation đều có thể biểu diễn bằng graph.

Node có thể là gene, protein, species hoặc neuron; edge có thể là regulation, binding, predation hoặc connection. Degree, path, community structure và centrality giúp tóm tắt network topology.

Trong bioinformatics, De Bruijn graph còn dùng cho genome assembly. Trong evolutionary analysis, tree là graph không cycle đặc biệt biểu diễn ancestry.

## Information theory

DNA sequence là information theo nghĩa statistical. Shannon entropy đo uncertainty:

```math
H(X)=-\sum_i p_i\log_2 p_i
```

Nếu một nucleotide position luôn là A thì entropy thấp; nếu bốn base xuất hiện gần đều nhau thì entropy cao hơn.

Information theory được dùng trong sequence motif, neural coding và population genetics, nhưng “biological information” rộng hơn Shannon information vì biological function cần context và mechanism.

## Optimization và evolution

Nhiều biological trait trông như optimized solution, nhưng evolution không giải bài toán optimization unconstrained. Selection hoạt động trên historical variation với trade-off và local constraints.

Mathematical optimization vẫn hữu ích để tìm strategy dự đoán, ví dụ optimal foraging, nhưng prediction phải được kiểm tra với ecology và evolutionary history.

## Algorithmic thinking trong biology

Sequence alignment dùng dynamic programming. Phylogenetic inference dùng search trên tree space. Genome assembly dùng graph algorithm. Protein structure prediction dùng optimization và machine learning.

Biology ngày càng trở thành discipline nơi experiment và computation tạo vòng lặp liên tục.

## Machine learning và representation

Biological data thường high-dimensional. Gene-expression vector có thể có hàng nghìn dimension; protein sequence có thể được embedding thành vector; medical image có thể học feature bằng deep neural network.

Nhưng representation không tự động bảo đảm causal understanding. Model có thể exploit confounder hoặc batch artifact. Do đó cross-validation, external validation và perturbation experiment vẫn quan trọng.

## Scale và dimensional analysis

Đơn vị giúp phát hiện equation sai. Concentration thường là mol/L; reaction rate có thể mol/(L·s); diffusion coefficient có đơn vị length²/time.

Nếu hai vế equation không cùng dimension, model chắc chắn có lỗi. Dimensional analysis là một kỹ năng physics–mathematics đặc biệt hữu ích khi đọc physiology và biochemistry.

## Kết nối với Mathematics Knowledge Library

Khi cần đào sâu mathematical foundation, xem các phần tương ứng trong `mathematics/`: functions, calculus, probability/statistics, linear algebra, discrete mathematics và numerical methods.

Biology dùng toán không phải để biến sự sống thành vài equation, mà để làm rõ assumption, prediction và uncertainty.
