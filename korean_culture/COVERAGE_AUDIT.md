# Văn hóa Hàn Quốc — điểm vào kiểm toán phạm vi

**Ngày rà soát:** 2026-09-29  
**Root chuẩn gốc:** `korean_culture/`

Bản kiểm toán chi tiết về chất lượng và độ phủ đã tồn tại tại:

- [`coverage_audit.md`](./coverage_audit.md)

Tệp root này chỉ tạo một **điểm vào governance nhất quán** cho tooling cấp repository. Audit chi tiết vẫn là nơi sở hữu đánh giá theo chapter về độ sâu, trùng lặp, chất lượng ngôn ngữ và độ mới của nguồn.

## Hợp đồng cấp root

Korean Culture phải giải thích pattern xã hội/văn hóa qua cơ chế và biến thiên, không qua stereotype:

```text
lịch sử / sinh thái
→ thiết chế
→ ràng buộc vật chất
→ quan hệ + động lực
→ công nghệ / giao diện
→ hành vi quan sát được
→ biến thiên / ngoại lệ
→ phản hồi / thay đổi
```

Không dùng một thế hệ, một công ty, một vùng hoặc một cộng đồng online làm đại diện cho toàn bộ người Hàn. Các thống kê hoặc chi tiết thể chế nhạy theo thời gian cần có nguồn và mốc kiểm tra.

KIIP là subdomain ôn thi riêng tại [`kiip/`](./kiip/README.md); nó không thuộc coverage audit chi tiết của Korean Culture trừ khi tài liệu nói rõ.

## Quy tắc review và bàn giao

Khi coverage hoặc chất lượng của domain thay đổi thực sự, cập nhật [`coverage_audit.md`](./coverage_audit.md). Chỉ sửa tệp root này khi owner hoặc vị trí audit chi tiết thay đổi.