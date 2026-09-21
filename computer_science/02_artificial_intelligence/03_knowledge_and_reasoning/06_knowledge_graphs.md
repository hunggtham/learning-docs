# Đồ thị tri thức trong Trí tuệ nhân tạo

**Đồ thị tri thức (Knowledge Graph / 지식 그래프)** biểu diễn thực thể và các mối quan hệ giữa chúng bằng một cấu trúc đồ thị có ngữ nghĩa rõ ràng. Dạng đơn giản nhất là một bộ ba:

\[
(subject, predicate, object)
\]

Ví dụ:

```text
(Seoul, capitalOf, SouthKorea)
(Alice, worksAt, CompanyX)
(CompanyX, locatedIn, Seoul)
```

Điểm quan trọng là Knowledge Graph không chỉ đơn giản là một graph database có nhiều cạnh. Giá trị thực sự của nó đến từ định danh thực thể, schema hoặc ontology, nguồn gốc dữ liệu (provenance), phạm vi thời gian, ý nghĩa của quan hệ và khả năng kết nối nhiều sự kiện từ các nguồn khác nhau thành một mô hình có thể truy vấn hoặc suy luận.

Xem trước: [Biểu diễn tri thức](./00_knowledge_representation.md).

## Mô hình dữ liệu đồ thị

Một đồ thị gồm tập node `V` và tập cạnh `E`:

\[
G=(V,E)
\]

Trong Knowledge Graph:

- node thường là thực thể, khái niệm hoặc literal;
- cạnh có loại quan hệ cụ thể;
- node và cạnh có thể mang thuộc tính hoặc metadata.

Mô hình kiểu RDF thường biểu diễn quan hệ bằng bộ ba. Mô hình property graph cho phép gắn thuộc tính trực tiếp lên node và cạnh.

Hai kiểu mô hình này có thể chuyển đổi qua lại trong nhiều trường hợp, nhưng cách truy vấn, công cụ và ngữ nghĩa không hoàn toàn giống nhau.

## Định danh thực thể

Nếu cùng một thực thể ngoài đời được ghi bằng nhiều identifier khác nhau:

```text
Seoul
서울
SEOUL_CITY_001
```

hệ thống cần cơ chế ánh xạ về một định danh chuẩn.

Nếu không, đồ thị sẽ bị chia thành nhiều thực thể trùng lặp. Ngược lại, nếu gộp nhầm hai thực thể khác nhau, dữ liệu cũng bị nhiễm lẫn.

**Đối sánh thực thể (entity resolution / 개체 해결)** vì vậy là thành phần nền tảng chứ không phải công việc dọn dữ liệu phụ.

## Ngữ nghĩa của quan hệ

Một cạnh `worksAt` cần được định nghĩa rõ:

- chủ thể nào được phép xuất hiện;
- đối tượng nào được phép xuất hiện;
- chỉ quan hệ hiện tại hay cả lịch sử;
- nhân viên chính thức và contractor có được xem giống nhau hay không;
- quan hệ có phạm vi thời gian hay không.

Nếu không có ngữ nghĩa, đồ thị có thể kết nối đúng về mặt cú pháp nhưng mơ hồ về ý nghĩa.

## Schema và ontology

Schema có thể mô tả:

```text
Person --worksAt--> Organization
Organization --locatedIn--> Place
```

Ontology có thể bổ sung quan hệ phân cấp:

```text
Doctor subClassOf MedicalProfessional
Hospital subClassOf HealthcareOrganization
```

Bộ suy luận có thể dùng các quy tắc này để suy ra kiểu kế thừa.

Schema cũng giúp kiểm tra tính hợp lệ. Ví dụ cạnh `Person worksAt Date` nhiều khả năng là sai về mặt ngữ nghĩa.

## Mô hình RDF

RDF biểu diễn phát biểu dưới dạng:

```text
subject predicate object
```

Ví dụ kiểu Turtle:

```turtle
:Alice :worksAt :CompanyX .
:CompanyX :locatedIn :Seoul .
```

URI hoặc IRI được dùng để định danh tài nguyên một cách nhất quán theo quy ước.

Một lợi thế lớn của RDF là khả năng hợp nhất dữ liệu từ nhiều nguồn khi identifier và vocabulary được thiết kế tương thích.

## RDFS và OWL

RDFS cung cấp các khái niệm nền như class, subclass, property, domain và range.

OWL bổ sung các khả năng biểu diễn ontology phong phú hơn, chẳng hạn equivalence, cardinality và các biểu thức lớp dựa trên Description Logic.

Mức biểu đạt càng cao thì suy luận có thể càng tốn kém. Vì vậy OWL cung cấp nhiều profile với mức đánh đổi khác nhau giữa khả năng biểu diễn và chi phí suy luận.

## SPARQL

SPARQL truy vấn đồ thị RDF bằng mẫu đồ thị.

Ví dụ:

```sparql
SELECT ?person
WHERE {
  ?person :worksAt :CompanyX .
  ?person :livesIn :Seoul .
}
```

Đây là truy vấn theo cấu trúc quan hệ, không phải tìm kiếm tương đồng ngữ nghĩa.

Bộ máy SPARQL cũng phải tối ưu thứ tự join tương tự query optimizer của cơ sở dữ liệu quan hệ.

## Property Graph và truy vấn kiểu Cypher

Property graph có thể lưu:

```text
(:Person {id: 1})-[:WORKS_AT {since: 2024}]->(:Company)
```

Ngôn ngữ như Cypher biểu diễn mẫu đường đi và quan hệ trực tiếp trên đồ thị.

Property graph thường phổ biến trong ứng dụng vận hành và phân tích quan hệ; hệ RDF/OWL nhấn mạnh hơn vào chuẩn ngữ nghĩa và ontology.

Không có mô hình nào luôn tốt hơn trong mọi trường hợp.

## Quan hệ dạng cạnh và quan hệ dạng sự kiện

Quan hệ nhị phân đơn giản có thể biểu diễn trực tiếp:

```text
Alice --worksAt--> CompanyX
```

Nhưng nếu việc làm cần thêm vai trò, ngày bắt đầu, ngày kết thúc, mức lương và nguồn dữ liệu, một cạnh duy nhất trở nên thiếu thông tin.

Ta có thể chuyển quan hệ thành một node sự kiện:

```text
Alice --participantIn--> Employment123
Employment123 --employer--> CompanyX
Employment123 --role--> Engineer
Employment123 --startDate--> 2025-01-01
```

Cách này phù hợp hơn với quan hệ nhiều ngôi và những quan hệ cần nhiều qualifier.

## Nguồn gốc dữ liệu

Một sự kiện quan trọng thường cần kèm theo thông tin nguồn:

```text
claim: CompanyX locatedIn Seoul
source: registry document
retrievedAt: 2026-09-01
confidence: verified
```

Khi hai nguồn mâu thuẫn, provenance cho phép hệ thống so sánh thay vì âm thầm ghi đè.

Citation trong RAG và provenance trong Knowledge Graph giải quyết cùng một vấn đề cốt lõi: ta biết thông tin này đến từ đâu và đáng tin đến mức nào.

## Knowledge Graph theo thời gian

Quan hệ có thể thay đổi:

```text
(Alice, worksAt, CompanyX, 2025-01..2026-08)
```

Knowledge Graph có yếu tố thời gian cho phép trả lời câu hỏi lịch sử như:

> Ai là CEO tại thời điểm T?

Nếu bỏ qua thời gian, đồ thị có thể chứa hai cạnh nhìn như mâu thuẫn nhưng thực tế đúng ở hai giai đoạn khác nhau.

## Suy luận trên đồ thị

Ví dụ quy tắc:

```text
parentOf(x,y) ∧ parentOf(y,z)
→ grandparentOf(x,z)
```

Hoặc ontology:

```text
Cardiologist subClassOf Doctor
Alice type Cardiologist
→ Alice type Doctor
```

Hệ thống có thể materialize các bộ ba dẫn xuất hoặc tính động khi truy vấn.

Duyệt đồ thị đơn thuần không phải suy luận logic nếu hệ thống chưa định nghĩa ngữ nghĩa cho quan hệ.

## Quan hệ bắc cầu

Nếu quan hệ được khai báo là bắc cầu:

\[
R(a,b)\land R(b,c)\rightarrow R(a,c)
\]

thì ta có thể suy ra quan hệ gián tiếp.

Ví dụ `ancestorOf` thường có tính bắc cầu. Một số quan hệ vị trí như `locatedWithin` cũng có thể bắc cầu nếu định nghĩa cẩn thận.

Không được tự động giả định mọi cạnh đều bắc cầu. `friendOf` hay `parentOf` không có tính chất này.

## Quan hệ đối xứng và quan hệ nghịch đảo

Quan hệ đối xứng:

\[
MarriedTo(a,b)\rightarrow MarriedTo(b,a)
\]

Quan hệ nghịch đảo:

\[
ParentOf(a,b)\leftrightarrow ChildOf(b,a)
\]

Mã hóa những thuộc tính này trong ontology giúp giảm dữ liệu lặp và cải thiện khả năng truy vấn.

## Hoàn thiện Knowledge Graph

Knowledge Graph thường không đầy đủ. Bài toán dự đoán liên kết (link prediction) ước lượng điểm cho bộ ba chưa tồn tại:

\[
score(h,r,t)
\]

Các mô hình embedding biến thực thể và quan hệ thành vector rồi học hàm chấm điểm.

Ví dụ ý tưởng kiểu TransE:

\[
\mathbf{h}+\mathbf{r}\approx\mathbf{t}
\]

với các bộ ba được xem là đúng.

Quan trọng: cạnh được dự đoán chỉ là **giả thuyết**, không phải sự kiện đã được xác minh. Trong hệ thống quan trọng, không nên tự động chuyển score thành fact.

## Embedding thực thể

Graph embedding đưa thực thể vào không gian vector dựa trên topology và quan hệ.

Nhờ đó có thể thực hiện link prediction, tìm thực thể tương tự, clustering hoặc dùng vector làm feature cho Machine Learning.

Tuy nhiên embedding nén nhiều cấu trúc quan hệ vào vector nên có thể làm mất khả năng giải thích tường minh.

Đây lại là sự đánh đổi quen thuộc giữa biểu diễn ký hiệu và biểu diễn phân tán.

## Graph Neural Network

GNN cập nhật biểu diễn của node bằng cách tổng hợp thông tin từ lân cận:

\[
\mathbf{h}_v^{(l+1)}=\phi\left(\mathbf{h}_v^{(l)},\operatorname{AGG}\{\mathbf{h}_u^{(l)}:u\in N(v)\}\right)
\]

GNN có thể học pattern trên cấu trúc đồ thị, nhưng không thay thế vai trò của schema, ontology hay provenance.

Knowledge Graph là cách tổ chức dữ liệu và ngữ nghĩa; GNN là một kiến trúc học có thể sử dụng dữ liệu đồ thị.

## Truy vấn nhiều bước

Ví dụ câu hỏi:

> Những nhà cung cấp nào nằm ở các quốc gia đang bị sự kiện X ảnh hưởng?

có thể cần một đường đi kiểu:

```text
Supplier
→ locatedIn
Country
← affects
Event
```

Đồ thị giúp thể hiện rõ truy vấn nhiều bước.

Tuy nhiên chỉ vì tồn tại một đường đi không có nghĩa câu trả lời luôn đúng về mặt ngữ nghĩa. Loại quan hệ, hướng cạnh và bối cảnh đều phải phù hợp.

## Bùng nổ số đường đi

Nếu bậc trung bình của đồ thị là `b`, số đường đi độ dài `k` có thể tăng gần `b^k`.

Vì vậy truy vấn đồ thị thường cần lọc loại quan hệ, giới hạn hướng cạnh, giới hạn độ dài đường đi, áp dụng schema và xếp hạng.

Đây cũng là một bài toán tìm kiếm.

## Knowledge Graph và cơ sở dữ liệu quan hệ

Cơ sở dữ liệu quan hệ mạnh ở giao dịch dạng bảng, ràng buộc và SQL join.

Graph database mạnh hơn khi cần truy vấn quan hệ nhiều bước, cấu trúc linh hoạt và path traversal.

Nhiều Knowledge Graph vẫn có thể lưu bằng cơ sở dữ liệu quan hệ. “Knowledge Graph” trước hết là một cách mô hình hóa tri thức, không bắt buộc phải dùng một công nghệ lưu trữ cụ thể.

Nên chọn storage theo workload thay vì theo tên công nghệ.

## Knowledge Graph và vector database

Vector database truy xuất theo mức tương đồng trong không gian embedding:

```text
query embedding ≈ document/entity embedding
```

Knowledge Graph truy xuất theo quan hệ được biểu diễn rõ:

```text
entity --relation--> entity
```

Vector search trả lời câu hỏi “thứ gì giống nhau về ngữ nghĩa?”.

Knowledge Graph trả lời câu hỏi “những thực thể nào được kết nối bởi quan hệ cụ thể?”.

Hai cơ chế có thể bổ sung cho nhau.

## Knowledge Graph kết hợp RAG

RAG cơ bản thường có dòng xử lý:

```text
query → embedding retrieval → chunks → LLM
```

Nếu kết hợp Knowledge Graph:

```text
query
 ↓ entity linking
seed entities
 ↓ graph traversal / structured filters
relevant entities + relations + documents
 ↓
LLM grounded generation
```

Cách này hữu ích khi cần cấu trúc quan hệ rõ, truy vấn nhiều bước hoặc provenance.

Đổi lại, chi phí xây và duy trì graph cao hơn đáng kể so với RAG văn bản đơn giản.

## Thuật ngữ GraphRAG

“GraphRAG” hiện được dùng cho nhiều kiến trúc khác nhau, không phải một thuật toán chuẩn duy nhất.

Điểm chung thường là quá trình retrieval hoặc generation được tăng cường bằng thực thể, quan hệ, community hoặc path lấy từ một graph.

Khi đánh giá một hệ GraphRAG, cần hỏi rõ:

- graph được xây bằng cách nào;
- node và edge thực sự đại diện cho điều gì;
- chiến lược truy vấn ra sao;
- graph được dùng để retrieval, summarization hay reasoning;
- fact được xác minh như thế nào.

Tên “GraphRAG” tự nó không bảo đảm chất lượng suy luận tốt hơn.

## Liên kết thực thể từ văn bản

Trước khi truy vấn Knowledge Graph bằng ngôn ngữ tự nhiên, hệ thống phải xác định mention và ánh xạ về đúng entity.

Ví dụ `Apple` có thể là công ty hoặc trái táo.

Entity linking sử dụng ngữ cảnh để giải quyết mơ hồ.

Nếu link sai ngay từ đầu, toàn bộ truy vấn nhiều bước phía sau có thể sai theo. Vì vậy confidence và fallback rất quan trọng.

## Retrieval dựa trên ontology

Nếu truy vấn yêu cầu `medical professional`, ontology có thể mở rộng sang các subclass như:

```text
Doctor
Nurse
Pharmacist
... ⊑ MedicalProfessional
```

Cách này tăng độ bao phủ mà không phụ thuộc hoàn toàn vào từ khóa hoặc embedding similarity.

Tuy nhiên ontology phải phản ánh đúng định nghĩa hiện tại của miền dữ liệu.

## Knowledge Graph trong hệ gợi ý

Có thể mô hình hóa:

```text
User → watched → Movie
Movie → directedBy → Director
Movie → genre → SciFi
```

Các path trên graph có thể trở thành feature hoặc lý do giải thích recommendation.

Embedding hoặc GNN có thể học thêm từ đồ thị dị thể này.

## Knowledge Graph trong phát hiện gian lận

Một graph có thể nối:

```text
Account
Device
IP
Merchant
Phone
Transaction
```

Gian lận thường mang tính quan hệ: nhiều tài khoản dùng chung thiết bị hoặc IP, hoặc có chuỗi tiền quay vòng.

Những pattern này khó nhìn thấy nếu chỉ xem từng dòng giao dịch độc lập.

Khi dùng graph cho fraud cần đặc biệt chú ý thời gian để tránh leakage từ các cạnh xuất hiện sau thời điểm cần dự đoán.

## Chất lượng dữ liệu

Các chiều chất lượng quan trọng gồm:

- độ chính xác của entity resolution;
- độ đúng của quan hệ;
- độ bao phủ;
- độ mới theo thời gian;
- provenance;
- tính nhất quán schema;
- tỷ lệ duplicate và conflict.

Một graph rất lớn nhưng định danh kém có thể tệ hơn một graph nhỏ nhưng đáng tin cậy.

## Cập nhật gia tăng

Knowledge Graph trong production luôn thay đổi. Pipeline có thể gồm:

```text
nguồn mới
→ trích xuất thực thể / quan hệ
→ entity resolution
→ kiểm tra schema
→ lưu provenance
→ hòa giải xung đột
→ cập nhật index / embedding
```

Đây là bài toán kết hợp giữa Data Engineering và Knowledge Engineering, không chỉ là Machine Learning.

## Trích xuất bằng LLM

LLM có thể chuyển văn bản thành các bộ ba ứng viên:

```text
Text → LLM → structured entities/relations
```

Nhưng vẫn phải kiểm tra vì mô hình có thể tự tạo quan hệ không tồn tại, gộp sai entity, bỏ mất qualifier hoặc thời gian, hoặc chuẩn hóa giá trị sai.

Pipeline an toàn hơn:

```text
LLM extraction
→ schema validation
→ entity resolution
→ source-grounded verification
→ human/review rules cho dữ liệu quan trọng
```

## Hỏi đáp trên Knowledge Graph

Có nhiều cách:

- SPARQL hoặc Cypher xác định;
- semantic parsing từ ngôn ngữ tự nhiên sang query;
- embedding-based relation prediction;
- GNN reasoning;
- LLM gọi công cụ truy vấn graph.

Một mẫu đáng tin cậy trong doanh nghiệp là: LLM tạo query có cấu trúc, graph engine thực thi, sau đó LLM diễn đạt kết quả kèm provenance.

## Mô hình tư duy

```text
Entity      = một đối tượng có thể định danh
Relation    = kết nối ngữ nghĩa có kiểu
Triple      = phát biểu nguyên tử trên đồ thị
Ontology    = vocabulary + ràng buộc ngữ nghĩa
Provenance  = nguồn của phát biểu
Time        = bối cảnh hiệu lực
Graph query = truy xuất quan hệ có cấu trúc
Embedding   = lớp tương đồng / chấm điểm học được
Reasoner    = suy ra fact mới từ quy tắc hình thức
```

## Các hiểu lầm thường gặp

### “Knowledge Graph là vector database có thêm quan hệ”

Không. Vector database xoay quanh tương đồng trong embedding space; Knowledge Graph xoay quanh quan hệ có kiểu và ngữ nghĩa tường minh.

### “Nếu có đường đi thì quan hệ đó có ý nghĩa”

Không. Ý nghĩa chỉ đúng khi loại cạnh, hướng và ngữ cảnh của đường đi phù hợp với câu hỏi.

### “Link prediction tạo ra fact còn thiếu”

Không trực tiếp. Nó chỉ tạo ứng viên và điểm số; vẫn có thể cần xác minh ngoài mô hình.

### “GraphRAG luôn tốt hơn RAG thường”

Không. GraphRAG có thêm chi phí xây và truy vấn graph, chỉ đáng giá khi quan hệ hoặc cấu trúc nhiều bước thật sự quan trọng.

## Liên kết kiến thức

Knowledge Graph nằm ở giao điểm của Database, Logic, Graph Algorithms, NLP và Machine Learning. Nó đặc biệt quan trọng với RAG và Agent vì cung cấp tri thức bên ngoài có thể cập nhật và truy vấn rõ ràng, trong khi embedding và LLM đảm nhận phần hiểu ngôn ngữ và khái quát hóa linh hoạt.

Xem tiếp: [AI ký hiệu và AI neuro-symbolic](./07_symbolic_neurosymbolic_ai.md).