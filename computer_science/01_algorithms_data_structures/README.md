# Algorithms & dữ liệu (data / 데이터) Structures — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Algorithms & dữ liệu (data / 데이터) Structures — lĩnh vực (domain / 도메인) Hub**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **Khi nào chuyển từ Basic sang Advanced?** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

Phần nền tảng của lĩnh vực (domain / 도메인) này nằm tại [`../basic/01_algorithms_data_structures/`](../basic/01_algorithms_data_structures/). Đây là nơi xây mô hình tư duy (mental model / 사고 모델) về algorithmic thinking, tính đúng đắn (correctness / 정확성), độ phức tạp (complexity / 복잡도), bộ nhớ (memory / 메모리)/dữ liệu (data / 데이터) bố cục (layout / 레이아웃), array/danh sách (list / 목록)/ngăn xếp (stack / 스택)/hàng đợi (queue / 큐), hashing, trees, graphs, sorting/searching, động (dynamic / 동적) programming, randomized/online algorithms và độ phức tạp (complexity / 복잡도) reductions.

Phần [`advanced/`](./advanced/README.md) là **thư viện kiến thức (knowledge library / 지식 라이브러리) DSA chuyên sâu**, đi sâu vào biểu diễn (representation / 표현), bất biến (invariant / 불변식), proof, hiện thực (implementation / 구현), hành vi thời gian chạy (runtime behavior / 런타임 동작) và edge cases bằng **C, Java và JavaScript**.

```text
computer_science/
├── basic/01_algorithms_data_structures/   # nền tảng
└── 01_algorithms_data_structures/
    ├── README.md                           # domain hub
    └── advanced/                           # DSA chuyên sâu
```

## Khi nào chuyển từ Basic sang Advanced?

Foundation nên đủ để trả lời được vì sao biểu diễn (representation / 표현) quyết định chi phí (cost / 비용), Big-O mô tả growth gì, bất biến (invariant / 불변식) dùng để lập luận (reasoning / 추론) tính đúng đắn (correctness / 정확성) ra sao, và array/băm (hash / 해시)/cây (tree / 트리)/đồ thị (graph / 그래프) khác nhau ở mô hình tư duy (mental model / 사고 모델) nào. Khi các câu hỏi đó đã rõ và bạn muốn đi sâu vào hiện thực (implementation / 구현), proof, specialized structures, bộ nhớ đệm (cache / 캐시)/hành vi thời gian chạy (runtime behavior / 런타임 동작) hoặc language-specific trade-offs, hãy chuyển sang Advanced.

**[Bắt đầu Advanced Data Structures & Algorithms](./advanced/README.md)**

Advanced DSA hiện bao gồm các cấu trúc và thuật toán sâu hơn như balanced/augmented trees, B/B+cây (tree / 트리), skip danh sách (list / 목록), Fenwick/Segment cây (tree / 트리), sparse bảng (table / 테이블), luồng (flow / 흐름)/matching, suffix structures, probabilistic structures, reduction/NP lập luận (reasoning / 추론) và hiện thực (implementation / 구현) tương ứng trong C, Java và JavaScript.

> **Bàn giao:** Sau **Khi nào chuyển từ Basic sang Advanced?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
