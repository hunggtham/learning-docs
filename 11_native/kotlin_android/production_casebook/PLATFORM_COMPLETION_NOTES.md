# Platform Completion Notes

Vòng bổ sung này tập trung vào các boundary Android platform còn thiếu sau khi architecture, coroutine/Flow, Compose state, persistence, networking, security, testing, build/release và Kotlin/JVM internals đã được cover.

Các chapter 09–14 không thay thế learning spine hoặc deep dive. Chúng giải thích những failure mode chỉ xuất hiện khi app chạm process/thread/IPC, runtime permission và target-SDK behavior, Compose layout/input/accessibility, camera/media/Bluetooth/location/files, device/OEM matrix và các system entry point ngoài Activity.

Khi đọc, ưu tiên reasoning theo thứ tự: capability có tồn tại không → permission/policy có cho phép không → component/process/thread nào sở hữu operation → resource lifetime bao lâu → state/source of truth ở đâu → failure/recovery thế nào → behavior có đổi theo OS/target SDK không → test matrix nào chứng minh được contract.

Đây cũng là tiêu chí cho các vòng update sau: không thêm API chỉ để tăng coverage danh mục; chỉ thêm khi nó tạo ra mental model mới, platform behavior mới hoặc production failure mode chưa được giải thích.