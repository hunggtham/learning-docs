# TLB, page walkers, huge pages và virtualization extensions

Virtual memory cho mỗi process một address space riêng, nhưng CPU cuối cùng phải truy cập physical memory. Nếu mỗi load/store đều phải đọc nhiều page-table entries từ RAM trước khi đọc dữ liệu thật, overhead sẽ rất lớn. **TLB — Translation Lookaside Buffer (변환 색인 버퍼)** tồn tại để cache kết quả dịch virtual page sang physical frame.

## Translation nằm trên critical path

Một virtual address thường được tách thành virtual page number và offset. Offset giữ nguyên; page number được dịch qua page table. Multi-level page table tiết kiệm memory cho address space thưa nhưng một TLB miss có thể cần nhiều memory accesses để walk các levels.

Hardware **page walker** thực hiện quá trình này trên nhiều kiến trúc. Các page-table entries mà walker đọc lại có thể được cache bởi CPU caches, nên translation performance liên hệ trực tiếp với cache hierarchy.

## TLB reach

Nếu TLB có `N` entries và page size `P`, lượng memory có thể được cover xấp xỉ `N × P`. Working set lớn hơn TLB reach làm translation miss tăng dù data vẫn vừa LLC.

Đây là lý do workload database, JVM heap lớn và analytics có thể hưởng lợi từ **huge pages**. Page 2 MiB cover memory lớn hơn nhiều so với page 4 KiB với cùng số TLB entries.

## Huge pages không miễn phí

Page lớn giảm TLB pressure nhưng tăng internal fragmentation, làm allocation/compaction khó hơn và tăng lượng memory bị ảnh hưởng khi một page cần copy/migrate. Transparent Huge Pages có thể giúp workload này nhưng gây latency spikes ở workload khác do compaction hoặc collapse.

Do đó huge pages là trade-off giữa translation efficiency và memory-management flexibility.

## TLB shootdown

Khi OS thay đổi mapping đang có thể được cache trên nhiều cores, stale TLB entry phải bị invalidated. **TLB shootdown** thường cần inter-processor interrupts hoặc coordination giữa cores.

Một workload thay đổi mappings thường xuyên có thể chịu cost không chỉ trên core gọi syscall mà trên nhiều cores khác. Đây là ví dụ rõ rằng operation “local” ở API level có thể có coordination cost toàn machine.

## Virtualization thêm tầng translation

Trong VM, guest OS nghĩ nó quản lý guest physical addresses, nhưng hypervisor phải map chúng tới host physical addresses. Hardware virtualization dùng cơ chế như Intel EPT hoặc AMD NPT để hỗ trợ nested translation.

Nếu naive, guest page-table walk kết hợp host translation có thể tạo nhiều accesses. CPU hiện đại có translation caches và page-walk optimizations để giảm cost, nhưng VM vẫn làm translation hierarchy phức tạp hơn bare metal.

## IOMMU

Device DMA cũng cần isolation. **IOMMU** dịch device-visible addresses và ngăn device tùy ý đọc/ghi toàn bộ physical memory. Nó đóng vai trò tương tự MMU nhưng cho I/O devices, quan trọng trong virtualization, PCI passthrough và security boundary.

## Production diagnosis

Nếu application có high CPU nhưng cache miss không quá lớn, TLB misses có thể là phần bị bỏ sót. Random access trên heap lớn, sparse structures và pointer-heavy workload dễ tạo translation pressure.

Measurement nên phân biệt minor/major page fault ở OS với TLB miss ở hardware. Chúng đều chứa từ “page” nhưng là hiện tượng khác tầng.

## Mental Model

> Virtual memory tạo abstraction; TLB làm abstraction đó đủ nhanh. Khi working set, core count hoặc virtualization tăng, translation trở thành một hierarchy riêng có cache, miss, invalidation và locality giống nhiều hệ thống cache khác.