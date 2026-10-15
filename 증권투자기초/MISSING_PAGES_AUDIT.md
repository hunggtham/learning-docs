# 증권투자기초 — Audit trang thiếu

Ngày kiểm tra: 2026-10-13  
Phạm vi: đối chiếu PDF nguồn với Markdown hiện tại; không sửa nội dung nguồn trong lần audit này.

## Kết luận nhanh

Không phát hiện khoảng số trang vật lý trong ba PDF nguồn:

| Sách | PDF nguồn | Marker Markdown | Khoảng số trang |
|---|---:|---:|---|
| `sach1` | 168 | Bản hiện tại đã bỏ marker `Page N`; bản page-map trước đó có `1–168` liên tục | Không phát hiện |
| `sach2` | 392 | `Page 1–392` | Không |
| `sach3` | 381 | `Page 1–381` | Không |

Vấn đề thực tế là một số trang trong Markdown bị mất phần OCR/nội dung, không phải mất cả số trang PDF.

## Trang bị thiếu nội dung rõ ràng

Các mục dưới đây thuộc bản [raw_md/sach3.md](./raw_md/sach3.md):

| Sách / trang | Hiện trạng trong Markdown | Đối chiếu nguồn |
|---|---|---|
| `sach3` — trang 8 | Section trống | PDF có trang phân cách chương với chữ `제1장` |
| `sach3` — trang 328 | Chỉ còn số trang `328` | PDF có bảng và phần giải thích về hợp đồng tương lai hàng hóa; bản source còn nội dung tương ứng |
| `sach3` — trang 346 | Chỉ còn số trang `346` | PDF có phần giải thích đầy đủ về sản phẩm/phái sinh; bản source còn nội dung tương ứng |

Bằng chứng trong file hiện tại:

- [raw_md/sach3.md:222](./raw_md/sach3.md#L222) — trang 8 trống.
- [raw_md/sach3.md:7763](./raw_md/sach3.md#L7763) — trang 328 chỉ còn footer.
- [raw_md/sach3.md:8203](./raw_md/sach3.md#L8203) — trang 346 chỉ còn footer.

Bản source có nội dung để đối chiếu:

- [sach3/raw_md/sach3.md:8921](./sach3/raw_md/sach3.md#L8921) — nội dung trang 328.
- [sach3/raw_md/sach3.md:9447](./sach3/raw_md/sach3.md#L9447) — nội dung trang 346.

## Trang bị thiếu một phần OCR / hình / bảng

Đây không phải trang trắng hoàn toàn, nhưng Markdown hiện tại ngắn hoặc thiếu phần hình/bảng/công thức so với PDF. Cần mở PDF để phục hồi thận trọng:

`sach3`: **30, 150, 168, 234, 251, 266, 268, 279, 286, 358**.

Đặc điểm thường gặp:

- trang 30: công thức còn nhưng phần mô tả và hình hồi quy bị thiếu;
- trang 150: sơ đồ học tập chủ yếu chỉ còn OCR rời rạc;
- trang 168: trang câu hỏi bị mất nhiều dòng;
- trang 234, 251, 266, 268, 279, 286, 358: bảng/hình chụp và phần chú thích bị OCR không đầy đủ.

## Các trang không tính là bị thiếu

- `sach1` trang 5: trang trắng trong PDF nguồn.
- `sach3` trang 380: trang trắng trong PDF nguồn.
- `sach2` các trang 1, 9, 10, 215, 216: trang bìa hoặc trang phân cách chương; nội dung tiêu đề vẫn hiện diện trong Markdown.

## Ghi chú về đường dẫn nguồn

- Sách 1: [`raw_md/sach1.md`](./raw_md/sach1.md).
- Sách 2: source authority được ghi trong README là [`raw/sach2.md`](./raw/sach2.md); bản page-structured dùng để kiểm tra marker là [`raw_md/sach2.md`](./raw_md/sach2.md).
- Sách 3: source/audit là [`sach3/raw_md/sach3.md`](./sach3/raw_md/sach3.md); bản page-structured được kiểm tra là [`raw_md/sach3.md`](./raw_md/sach3.md).

## Giới hạn của audit

Audit này xác định được khoảng số trang và các trang bị thiếu nội dung rõ ràng. Nó chưa chứng minh mọi công thức, bảng, hình và từng ký tự OCR đã chính xác 100%; các trang ở mục “thiếu một phần OCR / hình / bảng” vẫn cần đối chiếu trực quan với PDF.
