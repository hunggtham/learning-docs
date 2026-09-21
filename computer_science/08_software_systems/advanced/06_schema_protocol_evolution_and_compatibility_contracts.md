# Tiến hóa schema, protocol và hợp đồng tương thích

Hệ thống production hiếm khi nâng cấp toàn bộ thành phần cùng lúc. Trong vài phút, vài giờ hoặc nhiều tuần, client cũ có thể nói chuyện với server mới; producer mới gửi dữ liệu cho consumer cũ; database schema mới phục vụ application instance chưa restart. Vì vậy **compatibility (tính tương thích)** không phải vấn đề phụ của deployment mà là thuộc tính correctness của hệ thống đang tiến hóa.

Chapter này nối data modeling, API design, event streaming và distributed deployment. Câu hỏi trung tâm là: **làm thế nào thay đổi representation mà các thành phần đang chạy ở nhiều version vẫn hiểu nhau đủ đúng?**

## 1. Schema là contract chứ không chỉ structure

Một field `status` trong JSON không chỉ là chuỗi. Consumer có thể giả định tập giá trị, nullability, ý nghĩa thời gian hoặc quan hệ với field khác.

```json
{
  "orderId": "A-100",
  "status": "PAID"
}
```

Nếu producer thêm `PARTIALLY_REFUNDED`, syntax vẫn hợp lệ nhưng consumer dùng exhaustive switch cũ có thể crash hoặc xử lý sai.

Do đó schema có hai lớp: representation contract và semantic contract.

## 2. Backward và forward compatibility

**Tương thích ngược (backward compatibility)** thường nghĩa reader mới đọc được dữ liệu do writer cũ tạo. **Tương thích xuôi (forward compatibility)** nghĩa reader cũ vẫn xử lý được dữ liệu writer mới trong phạm vi thiết kế.

Trong rolling deployment, thường cần cả hai theo một khoảng thời gian vì version cũ và mới cùng tồn tại.

Không nên dùng hai thuật ngữ này mà không nói rõ ai là reader, ai là writer; documentation giữa các hệ sinh thái đôi khi dùng góc nhìn khác nhau.

## 3. Additive change thường an toàn hơn destructive change

Thêm optional field thường dễ tương thích nếu reader cũ bỏ qua field lạ:

```json
{
  "orderId": "A-100",
  "status": "PAID",
  "paymentMethod": "CARD"
}
```

Nhưng “thêm field” không tự động an toàn. Nếu field mới thay đổi interpretation của field cũ, semantic compatibility vẫn có thể vỡ.

Rename thường thực chất là `add new → dual support → migrate → remove old`, không phải đổi tên nguyên tử.

## 4. Tolerant reader và giới hạn của nó

Tolerant reader bỏ qua thông tin không hiểu, giúp evolution. Nhưng quá tolerant có thể che lỗi. Nếu security-sensitive field bị bỏ qua, hệ thống có thể chấp nhận message mà đáng ra phải reject.

Vì vậy tolerance phải có boundary: unknown metadata có thể bỏ qua, nhưng unknown authorization mode có thể phải fail closed.

## 5. Enum là điểm compatibility dễ vỡ

Developer thường xem enum là closed set:

```text
PENDING | PAID | CANCELLED
```

Distributed protocol nên cân nhắc khả năng writer mới thêm giá trị. Consumer cũ cần chiến lược như `UNKNOWN`, fallback an toàn hoặc explicit rejection.

Đây là trade-off giữa evolvability và khả năng phát hiện dữ liệu bất thường.

## 6. Binary protocols và field identity

Các serialization system như Protocol Buffers không chỉ dựa vào tên field mà dùng numeric field identifier trên wire. Nếu tái sử dụng identifier đã xóa cho nghĩa mới, dữ liệu cũ có thể bị giải mã thành ý nghĩa sai.

Điểm sâu ở đây là **wire identity phải ổn định lâu hơn source-code name**. Rename source field có thể an toàn trong khi reuse wire tag có thể nguy hiểm.

## 7. Database schema trong rolling deployment

Giả sử cần đổi `full_name` thành `display_name`. Nếu migration rename column trước khi application cũ dừng, instance cũ có thể lỗi.

Pattern **expand–migrate–contract** giải quyết bằng các giai đoạn:

```text
expand: thêm representation mới nhưng giữ cũ
migrate: code/data chuyển dần
contract: xóa representation cũ khi không còn reader/writer phụ thuộc
```

Điều này biến migration từ một mutation lớn thành protocol giữa các version.

## 8. Dual write và consistency risk

Trong giai đoạn chuyển tiếp, application đôi khi ghi cả column cũ và mới. Hai write có thể lệch nếu không nằm trong cùng transaction hoặc logic mapping thay đổi.

Nếu dual write sang hai service/database độc lập, ta quay lại distributed dual-write problem. Khi đó outbox/event-driven migration có thể phù hợp hơn.

Xem [distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).

## 9. Backfill là workload production

Backfill hàng triệu row không chỉ là data script. Nó cạnh tranh I/O, buffer pool, WAL bandwidth, replica lag và lock với traffic thật.

Một migration logically correct vẫn có thể gây outage vì resource saturation. Vì vậy cần batch, rate limit, checkpoint, retry và observability.

Đây là connection trực tiếp giữa schema evolution và capacity planning.

## 10. Event schema khó xóa hơn database column

Database row có thể được migration tại chỗ. Event log có thể giữ message nhiều năm và được replay. Consumer mới phải đối mặt historical schema.

Nếu stream được dùng cho replay, compatibility horizon gần bằng retention horizon, không chỉ deployment window.

Schema registry giúp kiểm tra structural compatibility, nhưng không chứng minh semantic compatibility.

## 11. API versioning không phải lựa chọn đầu tiên cho mọi thay đổi

Tạo `/v2` cho mỗi thay đổi nhỏ tạo nhiều version phải duy trì. Additive evolution thường tốt hơn khi semantics cốt lõi không đổi.

Version mới hợp lý khi contract thực sự thay đổi theo cách không thể diễn đạt tương thích, ví dụ meaning của resource hoặc workflow thay đổi lớn.

Versioning không xóa migration; nó chuyển migration sang client ecosystem.

## 12. Capability negotiation

Một số protocol cho phép hai phía thương lượng capability thay vì suy luận từ version number:

```text
client supports: compression=A,B; feature=X
server supports: compression=B,C; feature=X,Y
intersection: compression=B; feature=X
```

Capability negotiation hữu ích khi feature evolution không tuyến tính. Nhưng protocol handshake và fallback trở nên phức tạp hơn.

## 13. Semantic versioning và distributed reality

`major.minor.patch` là communication convention, không phải proof về compatibility. Một “minor” release vẫn có thể phá consumer nếu behavior undocumented đã trở thành dependency thực tế.

Contract tests và traffic evidence quan trọng hơn label version.

## 14. Consumer-driven contract

Provider không luôn biết consumer đang dựa vào field nào. Consumer-driven contract ghi lại expectation của consumer và kiểm tra provider change trước deployment.

Nhưng test chỉ phản ánh consumer đã đăng ký. Shadow consumer, ad-hoc analytics hoặc external integration vẫn có thể tồn tại. Governance và observability vẫn cần thiết.

## 15. Unknown fields, defaults và dữ liệu bị mất

Một proxy đọc message mới bằng schema cũ rồi serialize lại có thể làm mất unknown field nếu serialization library không preserve chúng. Đây là failure mode tinh vi: proxy “không thay đổi gì” về logic nhưng làm hỏng forward compatibility.

Default value cũng nguy hiểm. Missing field có thể có nghĩa “writer cũ không biết field này”, khác với writer mới chủ động gửi `false` hoặc `0`.

## 16. Compatibility matrix

Thay vì hỏi “API có backward compatible không?”, hãy lập matrix:

```text
writer old -> reader old
writer old -> reader new
writer new -> reader old
writer new -> reader new
historical replay -> reader current
```

Sau đó kiểm tra structural parsing, semantic interpretation và side effect của từng ô.

## 17. Failure-safe rollout

Một rollout tốt cần khả năng dừng và rollback. Nhưng rollback binary không luôn rollback data. Nếu version mới đã ghi representation mà version cũ không hiểu, quay application về version cũ có thể thất bại.

Do đó migration cần **rollback compatibility** trong khoảng quan trọng, hoặc forward-fix strategy rõ ràng.

## Common Misconceptions

**“Thêm field luôn backward compatible.”** Chỉ đúng nếu parser và semantics của consumer cho phép.

**“Schema registry đảm bảo hệ thống tương thích.”** Registry thường kiểm structural rules, không hiểu business semantics.

**“Database migration chạy một lần nên performance không quan trọng.”** Migration có thể là workload lớn nhất hệ thống trong thời gian chạy.

**“Rollback application là đủ.”** Data được ghi bởi version mới có thể làm version cũ không chạy được.

## Mental Model

> Schema evolution là một **distributed protocol theo thời gian** giữa các writer và reader không đổi version đồng thời.

Thiết kế change bằng cách xác định ai đang đọc/ghi representation nào, overlap window dài bao lâu, historical data có replay không, rollback cần hiểu dữ liệu mới đến mức nào và migration tiêu thụ tài nguyên gì.

Xem thêm: [Event streams](./04_event_streams_partitions_watermarks_replay_and_state.md), [Capacity planning](./01_capacity_planning_utilization_knee_and_admission_control.md), [Idempotency](./05_idempotency_and_deduplication_at_scale.md).