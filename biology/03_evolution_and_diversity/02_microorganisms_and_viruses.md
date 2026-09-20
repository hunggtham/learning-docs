# Vi sinh vật và virus — Microorganisms and Viruses (미생물과 바이러스)

Phylogeny cho thấy phần lớn diversity của life không nằm ở những organism lớn ta dễ nhìn thấy. Microbial world là nơi nhiều nguyên lý đã học hội tụ: cell nhỏ cần membrane và metabolism; genome nhỏ nhưng rất linh hoạt; population lớn tiến hóa nhanh; gene có thể truyền ngang; và activity của microorganism ảnh hưởng toàn ecosystem.

Vì vậy microbiology không nên học như “một danh sách bacteria và virus”. Nó là case study cực tốt để thấy cell biology, genetics, evolution và ecology hoạt động cùng nhau.

## 1. Microorganism là một category theo scale, không phải một clade duy nhất

**Microorganism (vi sinh vật / 미생물)** là organism quá nhỏ để quan sát rõ bằng mắt thường. Category này có thể gồm bacteria, archaea, nhiều protist, microscopic fungi và một số algae.

Chúng không nhất thiết có common ancestor gần nhau chỉ vì đều nhỏ.

Đây là reminder rằng classification theo appearance và classification theo phylogeny là hai việc khác nhau.

## 2. Bacteria: nhỏ nhưng metabolic diversity rất lớn

Bacteria là prokaryote, không có nucleus membrane-bound. Nhưng chúng có membrane, ribosome, DNA, enzyme và signaling system.

Một số lấy energy từ light; một số oxidize inorganic compound; một số dùng organic carbon; một số sống có oxygen, một số không.

Metabolic diversity của bacteria vượt xa cách chia “có lợi/có hại”.

Nhiều global biogeochemical cycle phụ thuộc microbial metabolism.

## 3. Archaea: nhìn giống bacteria nhưng evolutionary khác

Archaea cũng là prokaryote nhưng membrane lipid chemistry, transcription machinery và nhiều molecular feature khác bacteria.

Một số archaea sống ở extreme environment, nhưng nhiều loài sống ở ocean, soil và microbiome bình thường.

Việc từng gọi chúng là “extremophile đặc biệt” rồi sau đó phát hiện chúng phổ biến hơn là ví dụ cách scientific picture thay đổi khi sampling tốt hơn.

## 4. Growth của bacterial population

Bacteria có thể divide bằng binary fission.

Nếu condition lý tưởng và generation time cố định, population có thể tăng exponential:

\[
N(t)=N_0 2^{t/g}
\]

với \(g\) là generation time.

Nhưng culture thật không tăng exponential mãi. Nutrient cạn, waste tích lũy và space hạn chế, dẫn tới stationary phase rồi decline.

Đây là bridge trực tiếp từ cell metabolism sang population ecology.

## 5. Biofilm: bacteria sống như community

Trong tự nhiên, nhiều bacteria không sống đơn lẻ mà tạo **biofilm (생물막)** trên surface.

Cell tiết extracellular matrix, tạo structure giữ water và molecule, đồng thời tạo microenvironment khác nhau.

Trong biofilm, diffusion limitation làm oxygen/nutrient không phân bố đều. Một số cell grow chậm, làm antibiotic targeting fast-growing cell kém hiệu quả hơn.

Biofilm cho thấy property ở community level không thể suy chỉ từ một bacterium isolated.

## 6. Quorum sensing: population density trở thành signal

Một số bacteria tiết signal molecule. Khi population density tăng, signal concentration tăng. Khi vượt threshold, nhiều cell đồng thời đổi gene expression.

Đây là **quorum sensing (정족수 감지)**.

Logic này nối signaling với population behavior:

```text
individual cells release signal
      ↓
population density rises
      ↓
signal accumulates
      ↓
receptor threshold crossed
      ↓
coordinated gene expression
```

Các behavior như biofilm formation hoặc virulence factor production có thể được coordinate theo cách này.

## 7. Horizontal gene transfer: information không chỉ đi parent → offspring

Bacteria có thể nhận DNA qua ba route kinh điển.

**Transformation**: uptake DNA tự do từ environment.

**Transduction**: bacteriophage mang DNA giữa bacteria.

**Conjugation**: DNA, thường plasmid, được truyền qua cell-cell contact.

Những mechanism này làm gene flow ở microbial world rất nhanh.

Đây là lý do một resistance gene có thể lan giữa lineage mà không chờ mutation độc lập xuất hiện ở từng species.

## 8. Antibiotic resistance như một chain causal đầy đủ

Hãy nối từ molecular đến population scale.

Một mutation đổi target protein hoặc một plasmid mang enzyme phá antibiotic. Cell có resistance phenotype. Khi antibiotic hiện diện, susceptible cell bị inhibited mạnh hơn. Resistant cell có relative fitness cao hơn. Sau nhiều generation, resistance gene frequency tăng.

```text
DNA variant
  ↓
protein / pathway change
  ↓
cell survives drug better
  ↓
differential reproduction
  ↓
population evolves
```

Đây là toàn bộ genetics → phenotype → selection chain trong một example thực tế.

## 9. Microbiome: host là một ecosystem

**Microbiome (마이크로바이옴)** thường dùng để chỉ microbial community cùng genetic material trong một environment như gut, skin hoặc soil.

Host cung cấp habitat và nutrient; microbe có thể metabolize compound host không tự xử lý, cạnh tranh pathogen hoặc tạo metabolite ảnh hưởng host signaling.

Nhưng association microbiome–disease rất dễ bị overinterpreted. Diet, medication và disease state có thể đồng thời đổi microbiome. Do đó correlation không tự động thành causation.

Causal reasoning ở chapter đầu tiếp tục cần thiết ở đây.

## 10. Virus: information system phụ thuộc host

**Virus (바이러스)** thường gồm genome DNA hoặc RNA nằm trong protein coat, đôi khi có lipid envelope.

Virus không có independent metabolism hoàn chỉnh. Nó dùng host machinery để replicate.

Một viral lifecycle có logic:

```text
attachment
 ↓
entry
 ↓
genome replication / expression
 ↓
assembly
 ↓
release
```

Mỗi step có molecular target khác nhau cho antiviral intervention.

## 11. Virus và câu hỏi “có sống không?”

Virus có genome, mutation và evolution nhưng không tự metabolism/reproduction bên ngoài host.

Vì vậy virus nằm ở boundary của definition life.

Case này quan trọng hơn debate semantic: nó cho thấy properties của life có thể modular, không nhất thiết xuất hiện tất cả trong một entity độc lập.

## 12. RNA virus tiến hóa nhanh vì sao?

Nhiều RNA virus dùng polymerase có proofreading kém hơn DNA replication system, nên mutation rate cao hơn.

Population size lớn và generation nhanh làm variation xuất hiện nhanh.

Nhưng mutation rate quá cao cũng có cost vì nhiều genome bị damage.

Evolution luôn cân bằng variation và fidelity.

## 13. Bacteriophage và CRISPR: arms race ở molecular scale

Bacteriophage infect bacteria. Bacteria có defense; phage evolution counter-defense.

CRISPR-Cas system ở nhiều bacteria/archaea lưu fragment từ invader genome như molecular memory, rồi dùng RNA guide để nhận diện sequence tương tự lần sau.

Biotechnology sau này tái sử dụng logic này thành gene-editing tool.

Đây là ví dụ tuyệt vời: một mechanism evolution từ microbial defense trở thành technology của con người.

## 14. Microbe và global nutrient cycle

Nitrogen fixation biến N₂ thành form sinh vật dùng được. Nitrification và denitrification tiếp tục chuyển nitrogen giữa chemical form.

Decomposer phân hủy organic matter, trả carbon và nutrient về environment.

Một microorganism rất nhỏ nhưng collective activity ở planet scale có thể đổi atmospheric composition và soil fertility.

Scale nhỏ không đồng nghĩa impact nhỏ.

## 15. Pathogen, virulence và host không phải quan hệ đơn giản

Pathogen success không nhất thiết tối đa khi gây disease nặng nhất. Nếu host chết quá nhanh hoặc không truyền pathogen, virulence quá cao có thể giảm transmission.

Evolution của virulence phụ thuộc trade-off giữa replication, transmission và host damage.

Điều này nối microbiology với ecology và evolutionary game.

## 16. Từ microbial world sang organism đa bào

Microorganism cho ta một phiên bản rất cô đọng của life: một cell tự làm gần như mọi việc.

Nhưng multicellular organism chọn strategy khác: cell specialization và division of labor. Điều này tạo efficiency nhưng đồng thời tạo bài toán mới — các cell phụ thuộc nhau và cần transport, communication, defense và homeostasis ở scale lớn.

Vì vậy bước tiếp theo là chuyển từ single-cell autonomy sang multicellular coordination.

Ta sẽ bắt đầu với plant như một giải pháp đặc biệt cho bài toán lấy light, water và mineral từ hai môi trường khác nhau, rồi sang animal physiology.

Tiếp tục với [[../04_organismal_biology/00_plant_biology]].