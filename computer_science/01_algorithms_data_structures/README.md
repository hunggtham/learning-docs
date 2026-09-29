# Algorithms & dữ liệu (data / 데이터) Structures — lĩnh vực (domain / 도메인) Hub

> **Mạch đọc:** Đọc **Algorithms & dữ liệu (data / 데이터) Structures — lĩnh vực (domain / 도메인) Hub** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.

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

> **Bàn giao:** Sau **Khi nào chuyển từ Basic sang Advanced?**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algorithmic thinking and correctness](./00_algorithmic_thinking_and_correctness.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
