# 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)

## 198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)
Phần “198. 블랙 박스 테스트 (Black Box Test / Kiểm thử Hộp đen)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

- **기능 검사**라고도 함. 내부 코드를 보지 않고, 소프트웨어의 인터페이스(입·출력)에서 기능이 완전히 작동하는지 입증.
- 테스트 과정 **후반부**에 적용됨.
- 종류:
  - **동치 분할 검사 (Equivalence Partitioning)**: 타당한 입력과 타당하지 않은 입력 자료의 갯수를 균등하게 나눠 테스트. (Ví dụ: Yêu cầu nhập từ 1-100. Test case: 50 (hợp lệ), 150 (không hợp lệ)).
  - **경계값 분석 (Boundary Value Analysis)**: 경계값에서 오류가 발생할 확률이 높음을 이용. (Ví dụ: Test case: 0, 1, 100, 101).
  - **원인-효과 그래프 (Cause-Effect Graphing)**: 입력(원인)과 출력(효과)의 관계 분석.
