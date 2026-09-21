# Động lượng, xung lượng, va chạm và tâm khối

## Tại sao cần động lượng khi đã có động năng?

Động lượng (Momentum / 운동량) mô tả trạng thái chuyển động theo cách gắn trực tiếp với tác dụng của lực:

```math
\vec p=m\vec v
```

Động lượng là một đại lượng vectơ. Trong cơ học Newton, dạng tổng quát của định luật II có thể viết:

```math
\sum\vec F=\frac{d\vec p}{dt}
```

Năng lượng là đại lượng vô hướng nên rất mạnh khi phân tích sự chuyển đổi và bảo toàn năng lượng. Động lượng giữ cả độ lớn lẫn thông tin về hướng, vì vậy đặc biệt hữu ích trong các bài toán va chạm, giật lùi và hệ nhiều vật.

## Xung lượng

Xung lượng (Impulse / 충격량) là tích phân của lực theo thời gian:

```math
\vec J=\int_{t_1}^{t_2}\vec F\,dt
```

Từ định luật II Newton:

```math
\vec J=\Delta\vec p
```

Nếu chỉ biết lực trung bình trong khoảng thời gian `\Delta t`, ta có thể viết gần đúng:

```math
\vec J\approx \vec F_{avg}\Delta t
```

Với cùng một độ biến thiên động lượng `\Delta p`, kéo dài thời gian va chạm sẽ làm giảm độ lớn lực trung bình. Túi khí ô tô, vùng hấp thụ va chạm của thân xe, thảm tập và động tác co tay khi bắt bóng đều khai thác nguyên lý này.

## Bảo toàn động lượng

Với một hệ gồm nhiều vật, tổng động lượng là:

```math
\vec P=\sum_i\vec p_i
```

Các nội lực giữa các phần của hệ triệt tiêu theo cặp trong tổng khi mô hình Newton III áp dụng. Vì vậy:

```math
\frac{d\vec P}{dt}=\vec F_{external}
```

Nếu tổng ngoại lực bằng không:

```math
\vec P=constant
```

Bảo toàn động lượng không phụ thuộc vào việc va chạm có đàn hồi hay không. Ở mức cơ học, nó xuất hiện khi hệ được cô lập khỏi ngoại lực. Ở mức sâu hơn, bảo toàn động lượng liên hệ với đối xứng tịnh tiến (translational symmetry / 병진 대칭) của không gian.

## Va chạm đàn hồi và không đàn hồi

Trong va chạm đàn hồi (Elastic Collision / 탄성 충돌), cả tổng động lượng và tổng động năng đều được bảo toàn.

Trong va chạm không đàn hồi (Inelastic Collision / 비탄성 충돌), động lượng vẫn được bảo toàn nếu hệ cô lập, nhưng động năng cơ học có thể chuyển thành nội năng, biến dạng, nhiệt và âm thanh.

Va chạm hoàn toàn không đàn hồi (Perfectly Inelastic Collision / 완전 비탄성 충돌) là trường hợp các vật dính lại sau va chạm.

### Ví dụ: hai vật dính nhau

Vật `m_1` chuyển động với vận tốc `v_1`, còn `m_2` ban đầu đứng yên. Sau va chạm, hai vật dính nhau và cùng chuyển động với vận tốc `v_f`:

```math
m_1v_1=(m_1+m_2)v_f
```

Suy ra:

```math
v_f=\frac{m_1}{m_1+m_2}v_1
```

Động năng trước và sau nói chung không bằng nhau. Phần động năng giảm đi không biến mất mà chuyển sang các dạng năng lượng khác của hệ.

## Tâm khối

Tâm khối (Center of Mass / 질량중심) là trung bình có trọng số theo khối lượng của vị trí các phần tử trong hệ:

```math
\vec R_{cm}=\frac{\sum_i m_i\vec r_i}{\sum_i m_i}
```

Với phân bố khối lượng liên tục:

```math
\vec R_{cm}=\frac{1}{M}\int \vec r\,dm
```

Khái niệm này mạnh vì chuyển động của tâm khối chỉ phụ thuộc vào tổng ngoại lực:

```math
M\vec A_{cm}=\vec F_{external}
```

Nội lực có thể làm hệ biến dạng, quay hoặc thậm chí nổ thành nhiều phần, nhưng chúng không thể tự làm thay đổi chuyển động của tâm khối của một hệ cô lập.

Nếu một người đứng trên ván trượt ném một quả bóng về phía trước, người và ván trượt lùi lại. Các phần của hệ trao đổi động lượng với nhau, trong khi chuyển động của tâm khối toàn hệ vẫn tuân theo ngoại lực tác dụng lên hệ.

## Tên lửa và hệ có khối lượng thay đổi

Tên lửa là trường hợp cần cẩn thận khi dùng dạng đơn giản `F=ma`, vì khối lượng của tên lửa thay đổi khi nhiên liệu được phụt ra. Bảo toàn động lượng dẫn tới phương trình tên lửa Tsiolkovsky:

```math
\Delta v=v_e\ln\frac{m_0}{m_f}
```

Trong đó `v_e` là tốc độ phụt của khí so với tên lửa, `m_0` là khối lượng ban đầu và `m_f` là khối lượng cuối.

Logarithm xuất hiện vì mỗi phần tăng vận tốc đạt được khi tên lửa mất đi một phần khối lượng đang còn lại. Trong quá trình suy dẫn xuất hiện tích phân:

```math
\int \frac{dm}{m}=\ln m
```

Đây là một ví dụ điển hình cho cấu trúc logarit xuất hiện trong một quá trình có sự thay đổi theo tỉ lệ của đại lượng hiện có.

## Bài toán giật lùi

Một khẩu súng và viên đạn ban đầu đứng yên. Nếu viên đạn khối lượng `m` bay ra với vận tốc `v`, còn súng khối lượng `M` giật lùi với vận tốc `V`, bảo toàn động lượng cho:

```math
0=mv+MV
```

Do đó:

```math
V=-\frac{m}{M}v
```

Dấu âm cho biết súng chuyển động ngược hướng với viên đạn. Vì `M` thường lớn hơn `m` rất nhiều, độ lớn vận tốc giật lùi của súng nhỏ hơn nhiều so với vận tốc viên đạn.

## Bảo toàn như một bất biến của hệ

Có thể liên hệ trực giác với một hệ thống kế toán hoặc một giao dịch cơ sở dữ liệu: một bất biến (invariant) là điều kiện phải được giữ sau mọi thao tác hợp lệ. Trong một hệ cô lập, các tương tác nội bộ có thể chuyển động lượng từ thành phần này sang thành phần khác, nhưng tổng động lượng của toàn hệ không đổi.

Điểm khác biệt quan trọng là định luật bảo toàn trong vật lý không phải quy ước do con người đặt ra. Nó là cấu trúc được kiểm chứng thực nghiệm và, ở mức lý thuyết sâu hơn, liên hệ với đối xứng của tự nhiên.

## Mô hình tư duy (Mental Model)

> Động lượng có thể được hình dung như một “sổ cái chuyển động có hướng”. Ngoại lực tạo dòng động lượng đi vào hoặc đi ra khỏi hệ; các tương tác nội bộ chỉ chuyển động lượng giữa các phần của hệ. Khi chọn đúng ranh giới hệ, nhiều bài toán va chạm phức tạp trở thành bài toán cân bằng một đại lượng vectơ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Động lượng và động năng là cùng một thứ”

Không. `p=mv` là vectơ và tuyến tính theo `v`, còn `K=mv²/2` là vô hướng và phụ thuộc bậc hai vào tốc độ. Một hệ có tổng động lượng bằng không vẫn có thể chứa động năng lớn, chẳng hạn hai vật cùng khối lượng chuyển động với cùng tốc độ theo hai hướng ngược nhau.

### “Động lượng chỉ bảo toàn trong va chạm đàn hồi”

Sai. Động lượng được bảo toàn trong mọi loại va chạm nếu hệ cô lập. Chỉ động năng mới có thêm điều kiện bảo toàn trong va chạm đàn hồi.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md), [Lượng tử](../08_quantum/00_quantum_foundations.md).
