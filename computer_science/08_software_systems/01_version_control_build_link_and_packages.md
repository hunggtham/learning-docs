# Phiên bản (version / 버전) điều khiển (control / 제어), bản dựng (build / 빌드), linking và gói (package / 패키지) phụ thuộc (dependency / 의존성)

> **Mạch đọc:** Đặt **phiên bản (version / 버전) điều khiển (control / 제어), bản dựng (build / 빌드), linking và gói (package / 패키지) phụ thuộc (dependency / 의존성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **phiên bản (version / 버전) điều khiển (control / 제어) as lịch sử (history / 이력) đồ thị (graph / 그래프)** sang **Content addressing**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Mã nguồn (source code / 소스 코드) không trực tiếp trở thành deployable hệ thống (system / 시스템). Reproducible development cần lịch sử (history / 이력), phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), compilation/transformation, linking, packaging và sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자). Git, bản dựng (build / 빌드) tools và gói (package / 패키지) managers giải các parts khác nhau của chuỗi xử lý (pipeline / 파이프라인).

## Phiên bản (version / 버전) điều khiển (control / 제어) as lịch sử (history / 이력) đồ thị (graph / 그래프)

Git mô hình (model / 모델) stores content-addressed objects: blobs, trees, commits. lần ghi nhận (commit / 커밋) points to cây (tree / 트리) snapshot + parent(s) + siêu dữ liệu (metadata / 메타데이터). Branch is movable tham chiếu (reference / 참조) to lần ghi nhận (commit / 커밋); merge lần ghi nhận (commit / 커밋) can have multiple parents.

Lịch sử (history / 이력) therefore is DAG, not folders of diffs. Diff is computed between snapshots/trees. Understanding this explains why rebase creates new commits (new parents → new hashes) rather than “moves same lần ghi nhận (commit / 커밋)”.


> **Chuyển mạch:** Từ **phiên bản (version / 버전) điều khiển (control / 제어) as lịch sử (history / 이력) đồ thị (graph / 그래프)**, ta sang **Content addressing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Content addressing

Đối tượng (object / 객체) identifier derives from content/siêu dữ liệu (metadata / 메타데이터) format băm (hash / 해시). Same content can be deduplicated. băm (hash / 해시) định danh (identity / 식별자) helps integrity but Git băm (hash / 해시) ngữ nghĩa (semantics / 의미론)/phiên bản (version / 버전) depend hiện thực (implementation / 구현) era; don't treat lần ghi nhận (commit / 커밋) IDs as arbitrary crypto authentication without signed trust ngữ cảnh (context / 맥락).


> **Chuyển mạch:** Từ **Content addressing**, ta sang **hệ thống dựng (build system / 빌드 시스템)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hệ thống dựng (build system / 빌드 시스템)

Hệ thống dựng (build system / 빌드 시스템) các mô hình (models / 모델들) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) from sources to outputs. It should rebuild sản phẩm tạo ra (artifact / 산출물) when inputs/commands/môi trường (environment / 환경) affecting kết quả (result / 결과) thay đổi (change / 변경).

Make uses timestamps/rules; hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) may use tường minh (explicit / 명시적) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), content hashes and remote bộ nhớ đệm (cache / 캐시). Incremental bản dựng (build / 빌드) reuses unchanged outputs.

Undeclared phụ thuộc (dependency / 의존성) creates non-reproducible “works on my machine” hành vi (behavior / 동작) because bản dựng (build / 빌드) kết quả (result / 결과) depends hidden trạng thái (state / 상태).


> **Chuyển mạch:** Từ **hệ thống dựng (build system / 빌드 시스템)**, ta sang **Compilation and linking** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Compilation and linking

Compiled languages may go nguồn (source / 소스) → đối tượng (object / 객체) files → linker → executable/thư viện (library / 라이브러리). Linker resolves symbols and relocations. Static link embeds mã (code / 코드); động (dynamic / 동적) link resolves dùng chung (shared / 공유) libraries at tải (load / 로드)/thời gian chạy (runtime / 런타임).

Managed ecosystems gói (package / 패키지) bytecode/classes and thời gian chạy (runtime / 런타임) resolves modules/dependencies differently, but same concept: names/references must resolve to compatible artifacts.


> **Chuyển mạch:** Từ **Compilation and linking**, ta sang **trình quản lý gói (package manager / 패키지 관리자)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trình quản lý gói (package manager / 패키지 관리자)

Trình quản lý gói (package manager / 패키지 관리자) solves phụ thuộc (dependency / 의존성) resolution, phiên bản (version / 버전) các ràng buộc (constraints / 제약조건들), downloading, integrity and installation bố cục (layout / 레이아웃). phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) can contain diamond conflicts: A needs C v1, B needs C v2. Ecosystems handle by single resolution, multiple versions, shading/isolation or thất bại (failure / 실패).

Lockfile records chính xác (exact / 정확한) resolved versions/checksums to improve reproducibility. phiên bản (version / 버전) phạm vi (range / 범위) without khóa (lock / 잠금) means same manifest may install different phụ thuộc (dependency / 의존성) later.


> **Chuyển mạch:** Từ **trình quản lý gói (package manager / 패키지 관리자)**, ta sang **ngữ nghĩa (semantic / 의미적) and nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ngữ nghĩa (semantic / 의미적) and nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)

Upgrade can compile but thất bại (fail / 실패) thời gian chạy (runtime / 런타임) due ngữ nghĩa (semantic / 의미적) changes; bản địa (native / 네이티브) thư viện (library / 라이브러리) may break ABI; Java thư viện (library / 라이브러리) may preserve nhị phân (binary / 이진) linkage but hành vi (behavior / 동작) changes. tính tương thích (compatibility / 호환성) has nguồn (source / 소스), nhị phân (binary / 이진), behavioral and data-format dimensions.


> **Chuyển mạch:** Từ **ngữ nghĩa (semantic / 의미적) and nhị phân (binary / 이진) tính tương thích (compatibility / 호환성)**, ta sang **Reproducible builds** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Reproducible builds

Same declared inputs should create bit-for-bit identical sản phẩm tạo ra (artifact / 산출물). Hidden timestamps, filesystem thứ tự (ordering / 순서), locale, phụ thuộc (dependency / 의존성) fetching and trình biên dịch (compiler / 컴파일러) versions can break. Reproducibility improves supply-chain xác minh (verification / 확인) and debugging.


> **Chuyển mạch:** Từ **Reproducible builds**, ta sang **CI/CD chuỗi xử lý (pipeline / 파이프라인)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CI/CD chuỗi xử lý (pipeline / 파이프라인)

CI automates bản dựng (build / 빌드)/kiểm thử (test / 테스트)/static checks on controlled môi trường (environment / 환경). CD packages and promotes artifacts. Best practice is bản dựng (build / 빌드) once, promote same immutable sản phẩm tạo ra (artifact / 산출물) through environments; rebuilding at môi trường vận hành (production / 운영 환경) can thay đổi (change / 변경) dependencies/toolchain.


> **Chuyển mạch:** Từ **CI/CD chuỗi xử lý (pipeline / 파이프라인)**, ta sang **Supply-chain bảo mật (security / 보안)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Supply-chain bảo mật (security / 보안)

Dependencies/bản dựng (build / 빌드) scripts execute mã (code / 코드) with nhà phát triển (developer / 개발자)/CI privileges. Pin/verify artifacts, protect publishing credentials, rà soát (review / 검토) transitive dependencies, sign/provenance artifacts and minimize untrusted bản dựng (build / 빌드) steps.


> **Chuyển mạch:** Từ **Supply-chain bảo mật (security / 보안)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> nguồn (source / 소스) repository is a **đồ thị (graph / 그래프) of versions**; bản dựng (build / 빌드) is a **đồ thị (graph / 그래프) transformation** from declared inputs to immutable artifacts; trình quản lý gói (package manager / 패키지 관리자) is a **phụ thuộc (dependency / 의존성) solver + sản phẩm tạo ra (artifact / 산출물) fetcher**. Reproducibility requires no hidden inputs.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Git lần ghi nhận (commit / 커밋) is a diff.”** lần ghi nhận (commit / 커밋) references a snapshot cây (tree / 트리) and parent; diff is derived.

**“package-lock only for phụ thuộc (dependency / 의존성) install speed.”** It primarily fixes chính xác (exact / 정확한) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)/integrity for repeatability.

**“CI passing means deploy sản phẩm tạo ra (artifact / 산출물) identical everywhere.”** Only if sản phẩm tạo ra (artifact / 산출물) is preserved/promoted and môi trường (environment / 환경) contracts controlled.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Graph theory](../01_algorithms_data_structures/06_graphs_and_graph_algorithms.md) explains phụ thuộc (dependency / 의존성) DAGs; [compiler/linker](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md) supplies transformation; [security vulnerabilities](../07_security_reliability/03_software_vulnerabilities.md) covers supply-chain rủi ro (risk / 위험).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 abstraction modularity interfaces and apis](./00_abstraction_modularity_interfaces_and_apis.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
