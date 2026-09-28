# Nền tảng (platform / 플랫폼) Completion Notes

> **Mạch đọc:** Đặt **nền tảng (platform / 플랫폼) Completion Notes** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.

Vòng bổ sung này tập trung vào các ranh giới (boundary / 경계) Android nền tảng (platform / 플랫폼) còn thiếu sau khi kiến trúc (architecture / 아키텍처), coroutine/luồng (flow / 흐름), Compose trạng thái (state / 상태), persistence, networking, bảo mật (security / 보안), testing, bản dựng (build / 빌드)/bản phát hành (release / 릴리스) và Kotlin/JVM internals đã được cover.

Các chapter 09–14 không thay thế trục học (learning spine / 학습 축) hoặc deep dive. Chúng giải thích những dạng thất bại (failure mode / 실패 모드) chỉ xuất hiện khi app chạm tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드)/IPC, thời gian chạy (runtime / 런타임) permission và target-SDK hành vi (behavior / 동작), Compose bố cục (layout / 레이아웃)/đầu vào (input / 입력)/khả năng tiếp cận (accessibility / 접근성), camera/media/Bluetooth/location/files, thiết bị (device / 장치)/OEM ma trận (matrix / 행렬) và các hệ thống (system / 시스템) entry điểm (point / 지점) ngoài Activity.

Khi đọc, ưu tiên lập luận (reasoning / 추론) theo thứ tự: năng lực (capability / 역량) có tồn tại không → permission/chính sách (policy / 정책) có cho phép không → thành phần (component / 컴포넌트)/tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) nào sở hữu thao tác (operation / 연산) → tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) bao lâu → trạng thái (state / 상태)/nguồn chuẩn (source of truth / 정본) ở đâu → thất bại (failure / 실패)/khôi phục (recovery / 복구) thế nào → hành vi (behavior / 동작) có đổi theo OS/mục tiêu (target / 대상) SDK không → kiểm thử (test / 테스트) ma trận (matrix / 행렬) nào chứng minh được đặc tả hợp đồng (contract / 계약).

Đây cũng là tiêu chí cho các vòng cập nhật (update / 업데이트) sau: không thêm API chỉ để tăng coverage danh mục; chỉ thêm khi nó tạo ra mô hình tư duy (mental model / 사고 모델) mới, nền tảng (platform / 플랫폼) hành vi (behavior / 동작) mới hoặc môi trường vận hành (production / 운영 환경) dạng thất bại (failure mode / 실패 모드) chưa được giải thích.

> **Bàn giao:** Sau **nền tảng (platform / 플랫폼) Completion Notes**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 architecture end to end](./01_architecture_end_to_end.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
