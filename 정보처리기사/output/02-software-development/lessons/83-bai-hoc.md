# 핵심 110: RAM (Random Access Memory)

## 핵심 110: RAM (Random Access Memory)
Phần “핵심 110: RAM (Random Access Memory)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- 자유롭게 읽고 쓸 수 있는 기억장치로, RWM(Read Write Memory)이라고도 한다. (Bộ nhớ có thể đọc và ghi tự do.)
- RAM에는 현재 사용중인 프로그램이나 데이터가 저장되어 있다. (Lưu trữ chương trình và dữ liệu đang được sử dụng hiện tại.)
- 전원이 꺼지면 기억된 내용이 모두 사라지는 휘발성 메모리이다. (Bộ nhớ dễ bay hơi, mất dữ liệu khi tắt nguồn.)
- 일반적으로 ‘주기억장치’ 또는 ‘메모리’라고 하면 램을 의미한다. (Thường được gọi là bộ nhớ chính hoặc đơn giản là 'bộ nhớ'.)

| 구분 (Phân loại) | DRAM (Dynamic RAM - RAM động) | SRAM (Static RAM - RAM tĩnh) |
|---|---|---|
| 구성소자 (Thành phần) | 콘덴서 (Tụ điện) | 플립플롭 (Flip-Flop) |
| 특징 (Đặc điểm) | 전하가 방전되므로 주기적인 재충전(Refresh)이 필요함 (Cần làm mới định kỳ do tụ điện bị phóng điện) | 전원이 공급되는 동안에는 기억 내용이 유지 (Giữ nội dung miễn là có nguồn) |
| 전력소모 (Tiêu thụ điện) | 적음 (Ít) | 많음 (Nhiều) |
| 접근속도 (Tốc độ) | 느림 (Chậm) | 빠름 (Nhanh) |
| 집적도 (Mật độ) | 높음 (Cao - dung lượng lớn) | 낮음 (Thấp - dung lượng nhỏ) |
| 가격 (Giá) | 저가 (Rẻ) | 고가 (Đắt) |
| 용도 (Sử dụng cho) | 일반적인 주기억장치 (Bộ nhớ chính thông thường) | 캐시 메모리 (Bộ nhớ đệm / Cache) |

- **Vietnamese Explanation:** RAM là bộ nhớ làm việc của máy tính. DRAM rẻ, dung lượng cao nhưng chậm và hay quên (phải refresh liên tục), thường dùng làm thanh RAM máy tính. SRAM đắt, dung lượng nhỏ nhưng cực nhanh, không cần refresh, dùng làm Cache trong CPU.
- **Ví dụ (Example):** SRAM giống như bộ nhớ ngắn hạn của bạn khi tính nhẩm (nhanh nhưng nhớ được ít số). DRAM giống như cuốn sổ nháp (nhớ được nhiều nhưng phải tra cứu chậm hơn, và chốc chốc phải tô lại chữ mờ - refresh).
- 💡 **Mẹo ghi nhớ (Mnemonics):** **S**RAM = **S**iêu tốc (Flip-Flop, Cache). **D**RAM = **D**ump (Đổ liên tục - Refresh, Tụ điện, RAM thường).

---
