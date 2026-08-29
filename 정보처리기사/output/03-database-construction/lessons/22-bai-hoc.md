# 130-132. 트랜잭션 (Transaction)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **130-132. 트랜잭션 (Transaction)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

트랜잭션

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 130-132. 트랜잭션 (Transaction)
- 데이터베이스 상태를 변환시키는 논리적 작업의 단위.
- **ACID 특성:**
  - **Atomicity (원자성):** 모두 반영되거나(Commit) 전혀 반영되지 않아야 함(Rollback).
  - **Consistency (일관성):** 성공 시 일관성 있는 상태 유지.
  - **Isolation (독립성/격리성):** 다른 트랜잭션의 연산이 끼어들 수 없음.
  - **Durability (영속성):** 성공한 결과는 시스템 고장에도 영구 반영.
- **VI (Vietnamese) (Tiếng Việt):** Giao dịch (Transaction) & Tính chất ACID.
  - Atomicity (Tính nguyên tử): Tất cả hoặc không có gì.
  - Consistency (Tính nhất quán): Giữ trạng thái nhất quán.
  - Isolation (Tính độc lập): Không bị can thiệp bởi giao dịch khác.
  - Durability (Tính bền vững): Lưu trữ vĩnh viễn dù có lỗi hệ thống.
