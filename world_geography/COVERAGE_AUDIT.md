# Địa lý thế giới — điểm vào kiểm toán phạm vi

**Ngày rà soát:** 2026-09-29
**Root chuẩn gốc:** `world_geography/`

Bản kiểm toán chi tiết đã tồn tại tại:

- [`CORE_COVERAGE_AUDIT.md`](./CORE_COVERAGE_AUDIT.md)

Tệp root này chỉ là **điểm vào governance ổn định** cho tooling cấp repository; không lặp lại nội dung audit chi tiết.

## Hợp đồng cấp root

Domain cần giữ mô hình trung tâm:

```text
mẫu không gian
+ quá trình
+ mạng / dòng
+ quy mô
+ bằng chứng
```

Chapter vùng/quốc gia phải giải thích cấu trúc nhân quả thay vì trở thành encyclopedia dữ kiện:

```text
ràng buộc vật lý / tài nguyên
→ phân bố dân cư
→ sản xuất / kinh tế
→ hành lang vận chuyển / mạng
→ đô thị / thương mại
→ tương tác với thể chế và lịch sử
→ rủi ro / biến đổi
```

Không dùng địa lý như thuyết định mệnh. Lịch sử, công nghệ và thể chế có thể làm yếu, khuếch đại hoặc đảo chiều tác động của constraint không gian.

## Quy tắc review và bàn giao

Khi trạng thái core coverage thay đổi, cập nhật [`CORE_COVERAGE_AUDIT.md`](./CORE_COVERAGE_AUDIT.md). Chỉ sửa tệp root này nếu vị trí audit hoặc canonical owner thay đổi.
