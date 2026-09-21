# 09. Xuất nhập cảnh, visa, thường trú và nhập quốc tịch

## 1. Bốn khái niệm phải tách riêng

Người nước ngoài ở Hàn Quốc thường dùng chung từ “visa”, nhưng pháp luật tách nhiều lớp:

```text
사증 (visa) — giấy phép nhập cảnh theo diện nhất định
체류자격 — tư cách lưu trú sau khi nhập cảnh
영주(F-5) — tư cách thường trú
국적 — quốc tịch
```

Một người có thể sống lâu dài ở Hàn Quốc mà không có quốc tịch Hàn. `영주권` và `국적` không phải một khái niệm.

## 2. Luật nền tảng

Các luật quan trọng gồm:

- `출입국관리법` — Luật Quản lý Xuất nhập cảnh;
- `출입국관리법 시행령`;
- `출입국관리법 시행규칙`;
- `국적법` — Luật Quốc tịch;
- `국적법 시행령`;
- `국적법 시행규칙`;
- các `고시`, `지침`, `별표` liên quan.

Tại thời điểm kiểm tra 2026-09-21, `출입국관리법 시행규칙` đã được sửa đổi và có bản hiệu lực từ 2026-09-15. Điều này minh họa vì sao tài liệu visa cũ vài tháng có thể đã không còn chính xác.

## 3. Visa và 체류자격

Khi nghiên cứu một loại visa, không chỉ ghi tên và mã. Nên ghi theo template:

```text
체류자격명 / 코드
→ đối tượng chính
→ hoạt động được phép
→ hoạt động bị hạn chế
→ thời hạn tối đa / kỳ gia hạn
→ điều kiện đổi sang tư cách khác
→ nơi nộp
→ hồ sơ
→ 신고 nghĩa vụ sau khi thay đổi việc làm/địa chỉ
```

Một số thay đổi trong công việc, nơi làm việc, địa chỉ, hôn nhân hoặc tình trạng học tập có thể phải khai báo.

## 4. Hi Korea và Immigration Service

Hai nguồn thực tế quan trọng:

- `Hi Korea (hikorea.go.kr)` — điện tử 민원, 예약, hướng dẫn và dịch vụ;
- `Korea Immigration Service (immigration.go.kr)` — thông báo chính sách, hướng dẫn, statistics, tài liệu visa.

Đường dây 1345 là Immigration Contact Center và đặc biệt hữu ích khi cần xác nhận **thủ tục hiện hành**.

## 5. Gia hạn và thay đổi tư cách lưu trú

Phân biệt:

- `체류기간 연장`: gia hạn thời gian của tư cách hiện tại;
- `체류자격 변경`: đổi sang tư cách khác;
- `체류자격 외 활동허가`: xin phép hoạt động ngoài tư cách trong trường hợp luật cho phép;
- `근무처 변경·추가`: thay đổi/thêm nơi làm việc khi chế độ visa yêu cầu;
- `체류지 변경신고`: khai báo thay đổi địa chỉ cư trú.

Không được dùng một thủ tục như thể thay thế tất cả thủ tục còn lại.

## 6. Thường trú F-5 (영주)

F-5 là **tư cách lưu trú thường trú**, không phải quốc tịch. Hệ thống F-5 có nhiều nhánh khác nhau; điều kiện có thể xét thời gian cư trú, thu nhập/tài sản, phẩm chất, kiến thức xã hội, quan hệ gia đình, đầu tư, nhân tài hoặc tiêu chí đặc biệt tùy diện.

Sai lầm phổ biến là đọc điều kiện của một loại F-5 rồi áp dụng cho tất cả F-5.

Cách nghiên cứu đúng:

```text
Visa Navigator / 공식 안내
→ xác định 정확한 F-5 세부유형
→ 출입국관리법 시행령 별표
→ 시행규칙
→ 최신 제출서류
→ 관할 출입국 확인
```

Không nên hard-code một mức thu nhập hoặc số năm duy nhất trong library vì các ngưỡng và route thay đổi.

## 7. Thường trú không bằng nhập quốc tịch

`영주(F-5)` vẫn là tư cách của người nước ngoài. Người có F-5 có quyền cư trú dài hạn và nhiều quyền rộng hơn một số visa khác, nhưng không tự động trở thành `대한민국 국민`.

`귀화` là một con đường **取得 quốc tịch** theo `국적법`. Luật phân biệt nhiều loại như 일반귀화, 간이귀화, 특별귀화 với điều kiện khác nhau.

## 8. Nhập quốc tịch (귀화)

Theo `국적법`, người chưa từng có quốc tịch Hàn có thể xin `귀화허가`; Bộ Tư pháp xem xét các điều kiện pháp luật. Việc cấp quốc tịch liên quan thủ tục, thẩm tra và trong nhiều trường hợp có `국민선서` và nhận `귀화증서` theo luật.

Đây là khu vực rất nhạy theo thời gian. Ví dụ, Luật Quốc tịch đã có sửa đổi được công bố năm 2026 với thời điểm hiệu lực riêng. Vì vậy phải kiểm tra **phiên bản đang hiệu lực vào ngày nộp**, không chỉ bản “mới nhất được công bố”.

## 9. KIIP và naturalization/permanent residence

`사회통합프로그램 (KIIP)` có thể liên quan một số yêu cầu/đánh giá trong hệ thống cư trú hoặc quốc tịch, nhưng vai trò cụ thể phụ thuộc route. Không nên suy rằng hoàn thành KIIP tự động tạo quyền F-5 hoặc quốc tịch.

Tài liệu KIIP trong repo: [`../korean_culture/kiip/`](../korean_culture/kiip/README.md).

## 10. Nghĩa vụ khai báo

Người nước ngoài cần chú ý các loại `신고의무`, ví dụ thay đổi địa chỉ, hộ chiếu, tình trạng nhất định hoặc thông tin liên quan theo luật. Vi phạm deadline có thể dẫn đến bất lợi hoặc xử lý hành chính.

Hãy xây thói quen:

```text
có thay đổi đời sống lớn?
→ tìm xem có 출입국 신고 nghĩa vụ không
→ kiểm tra deadline
→ nộp online hay 방문
→ giữ 접수증 / 처리결과
```

## 11. Cách đọc hồ sơ visa

Mỗi hồ sơ nên chia thành:

```text
필수서류 — bắt buộc
조건부서류 — chỉ khi thuộc trường hợp
본인서류 — của người nộp
회사서류 — của công ty
재정서류 — tài chính
거주서류 — nơi ở
경력·학력서류 — học vấn/kinh nghiệm
번역·공증·아포스티유 — nếu yêu cầu
```

Không nộp theo một checklist cũ mà không kiểm tra ngày cập nhật.

## 12. Nếu nhận quyết định bất lợi về cư trú

Đọc kỹ:

- tên quyết định (`처분명`);
- cơ sở pháp lý;
- lý do;
- ngày nhận;
- thời hạn rời khỏi Hàn nếu có;
- hướng dẫn phản đối (`불복방법`).

Tình trạng cư trú có deadline nghiêm ngặt. Một 민원 chung không chắc làm dừng thời hạn pháp lý.

## 13. Nguồn chính thức

- Hi Korea: https://www.hikorea.go.kr/
- 출입국·외국인정책본부: https://www.immigration.go.kr/
- 국가법령정보센터: https://www.law.go.kr/
- 사회통합정보망: https://www.socinet.go.kr/
- 1345 Immigration Contact Center

## 14. Nguyên tắc an toàn

Với visa, F-5 và quốc tịch, luôn ghi **mã tư cách cụ thể + loại route + ngày kiểm tra**. Không dùng một ví dụ của người khác làm quy tắc cho hồ sơ của mình.