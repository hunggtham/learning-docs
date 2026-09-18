from pathlib import Path
import re
R=Path('korean_history')

# First important occurrence in each chapter: Vietnamese (Korean / English).
M=[
('Gojoseon (고조선)','Cổ Triều Tiên (고조선 / Gojoseon)'),('Goguryeo (고구려)','Cao Câu Ly (고구려 / Goguryeo)'),
('Baekje (백제)','Bách Tế (백제 / Baekje)'),('Silla (신라)','Tân La (신라 / Silla)'),('Balhae (발해)','Bột Hải (발해 / Balhae)'),
('Goryeo (고려, 918–1392)','Cao Ly (고려 / Goryeo)'),('Goryeo (고려)','Cao Ly (고려 / Goryeo)'),('Joseon (조선)','Triều Tiên (조선 / Joseon)'),
('Korean Empire (대한제국)','Đại Hàn Đế Quốc (대한제국 / Korean Empire)'),('Dangun (단군)','Đàn Quân (단군 / Dangun)'),
('Gyeon Hwon (견훤)','Chân Huyên (견훤 / Gyeon Hwon)'),('Gung Ye (궁예)','Cung Duệ (궁예 / Gung Ye)'),('Wang Geon (왕건)','Vương Kiến (왕건 / Wang Geon)'),
('Yi Seong-gye','Lý Thành Quế (이성계 / Yi Seong-gye)'),('vua Sejong (세종)','Vua Sejong Đại đế (세종대왕 / King Sejong the Great)'),
('Yi Sun-sin (이순신)','Đô đốc Yi Sun-sin (이순신 / Admiral Yi Sun-sin)'),('Choe Je-u','Choe Je-u (최제우 / Choe Je-u)'),
('Gojong','Vua Gojong (고종 / King Gojong)'),('Syngman Rhee','Tổng thống Syngman Rhee (이승만 / Syngman Rhee)'),
('Park Chung-hee','Tổng thống Park Chung-hee (박정희 / Park Chung-hee)'),('Chun Doo-hwan','Chun Doo-hwan (전두환 / Chun Doo-hwan)'),
('Park Jong-chul','Park Jong-chul (박종철 / Park Jong-chul)'),('Hanseong','Hán Thành (한성 / Hanseong)'),
('Gyeongju','Gyeongju (경주 / Gyeongju)'),('Ganghwa Island','đảo Ganghwa (강화도 / Ganghwa Island)'),('Jeju','Jeju (제주 / Jeju)'),
('Incheon','Incheon (인천 / Incheon)'),('Gwangju','Gwangju (광주 / Gwangju)'),('Pyongyang','Bình Nhưỡng (평양 / Pyongyang)'),
('Kaesong','Kaesong (개성 / Kaesong)'),('Han River','sông Hán (한강 / Han River)'),('Korean Peninsula','bán đảo Triều Tiên (한반도 / Korean Peninsula)'),
('Samguk sagi','Tam Quốc Sử Ký (삼국사기 / Samguk Sagi)'),('Bone-rank system (골품제)','chế độ Cốt phẩm (골품제 / Bone-rank System)'),
('Gyeongguk Daejeon (경국대전)','Kinh Quốc Đại Điển (경국대전 / Gyeongguk Daejeon)'),
('Joseon Wangjo Sillok (조선왕조실록)','Triều Tiên Vương Triều Thực Lục (조선왕조실록 / Veritable Records of the Joseon Dynasty)'),
('Hunminjeongeum','Huấn Dân Chính Âm (훈민정음 / Hunminjeongeum, The Proper Sounds for the Instruction of the People)'),
('Imjin War (임진왜란)','Chiến tranh Imjin (임진왜란 / Imjin War)'),('Donghak Peasant Movement (동학농민운동)','Phong trào nông dân Đông Học (동학농민운동 / Donghak Peasant Movement)'),
('Gabo Reforms (갑오개혁)','Cải cách Giáp Ngọ (갑오개혁 / Gabo Reform)'),('Gapsin Coup (1884)','Chính biến Giáp Thân (갑신정변 / Gapsin Coup)'),
('Imo Mutiny (1882)','Binh biến Nhâm Ngọ (임오군란 / Imo Mutiny)'),('Treaty of Ganghwa','Hiệp ước Ganghwa (강화도조약 / Treaty of Ganghwa)'),
('March First Movement','Phong trào 1 tháng 3 (3·1운동 / March First Movement)'),('Korean Provisional Government','Chính phủ Lâm thời Đại Hàn Dân Quốc (대한민국임시정부 / Provisional Government of the Republic of Korea)'),
('Korean Liberation Army','Quang Phục Quân Hàn Quốc (한국광복군 / Korean Liberation Army)'),('April Revolution (4·19 혁명)','Cách mạng 19 tháng 4 (4·19혁명 / April Revolution)'),
('Saemaul Undong','Phong trào Làng mới (새마을운동 / Saemaul Undong, New Village Movement)'),('Gwangju Democratization Movement','Phong trào Dân chủ Gwangju (광주민주화운동 / Gwangju Democratization Movement)'),
('June Democratic Struggle','Đấu tranh Dân chủ Tháng Sáu (6월 민주항쟁 / June Democratic Struggle)'),('Hallyu','Làn sóng Hàn Quốc (한류 / Hallyu, Korean Wave)'),
('Juche','Tư tưởng Chủ thể (주체 / Juche)'),('Arduous March','Cuộc Hành quân Gian khổ (고난의 행군 / Arduous March)'),('Jangmadang','chợ Jangmadang (장마당 / Jangmadang markets)')]
SKIP={'README.md','00_index_and_dependency.md','30_timeline_key_dates.md','31_glossary_and_reference_map.md','32_naming_translation_conventions.md'}
for p in R.glob('*.md'):
    if p.name in SKIP: continue
    lines=p.read_text(encoding='utf-8').splitlines(); out=[]; done=set(); fence=False
    for line in lines:
        if line.strip().startswith('```'): fence=not fence; out.append(line); continue
        if fence or line.lstrip().startswith('#'): out.append(line); continue
        for old,new in M:
            if old in done or new in line: continue
            if old in line: line=line.replace(old,new,1); done.add(old)
        out.append(line)
    p.write_text('\n'.join(out)+'\n',encoding='utf-8')

def edit(f,a,b):
    p=R/f; t=p.read_text(encoding='utf-8').replace(a,b); p.write_text(t,encoding='utf-8')

edit('02_prehistory_and_early_states.md','**Wiman Triều Tiên (조선 / Joseon) (위만조선)**','**Vệ Mãn Cổ Triều Tiên (위만조선 / Wiman Joseon)**')
edit('02_prehistory_and_early_states.md','Khi nhà Hán đánh bại Wiman Joseon năm 108 BCE','Khi nhà Hán đánh bại Vệ Mãn Cổ Triều Tiên năm 108 BCE')
edit('02_prehistory_and_early_states.md','và Gaya dần phát triển.','và Gaya (가야 / Gaya) dần phát triển.')
edit('03_three_kingdoms_and_gaya.md','Gaya (가야) không nên bị xem như footnote.','Gaya (가야 / Gaya) không nên bị xem như footnote.')
edit('08_early_joseon_state_confucian_order.md','Civil service examination (과거) biến classical learning thành gateway tới office.','Khoa cử (과거 / Civil Service Examination) biến classical learning thành gateway tới office.')
edit('29_collective_memory_historiography_public_history.md','Triều Tiên (조선 / Joseon) Wangjo Sillok là một corpus lớn','Triều Tiên Vương Triều Thực Lục (조선왕조실록 / Veritable Records of the Joseon Dynasty) là một corpus lớn')
edit('01_how_to_read_korean_history.md','“Unified Tân La (신라 / Silla)”, “Late Triều Tiên (조선 / Joseon)”','“Tân La Thống nhất (통일신라 / Unified Silla)”, “Triều Tiên hậu kỳ (조선 후기 / Late Joseon)”')
edit('01_how_to_read_korean_history.md',"**bán đảo Triều Tiên (한반도 / Korean Peninsula) (bán đảo Triều Tiên / 한반도)**, **Republic of Korea (Đại Hàn Dân Quốc / 대한민국)** và **Democratic People's Republic of Korea (CHDCND Triều Tiên / 조선민주주의인민공화국)**","**bán đảo Triều Tiên (한반도 / Korean Peninsula)**, **Đại Hàn Dân Quốc/Hàn Quốc (대한민국 / Republic of Korea)** và **Cộng hòa Dân chủ Nhân dân Triều Tiên (조선민주주의인민공화국 / Democratic People's Republic of Korea)**")
edit('15_independence_movements_and_provisional_government.md',' (대한민국임시정부)**','**')
edit('15_independence_movements_and_provisional_government.md',' (한국광복군) thuộc',' thuộc')
edit('19_developmental_state_industrialization_1961_1979.md',' (새마을운동) đầu',' đầu')
edit('24_north_korea_parallel_history.md','**Tư tưởng Chủ thể (주체 / Juche) (주체)**','**Tư tưởng Chủ thể (주체 / Juche)**')
edit('24_north_korea_parallel_history.md','” (고난의 행군),','”,')
edit('24_north_korea_parallel_history.md','markets) (장마당)','markets)')
edit('24_north_korea_parallel_history.md',"Democratic People's Republic of Korea hình thành năm 1948 trên nền Soviet occupation zone, land reform, nationalization và political consolidation dưới Korean Workers' Party.","Cộng hòa Dân chủ Nhân dân Triều Tiên (조선민주주의인민공화국 / Democratic People's Republic of Korea) hình thành năm 1948 trên nền Soviet occupation zone, land reform, nationalization và political consolidation dưới Đảng Lao động Triều Tiên (조선로동당 / Workers' Party of Korea).")
edit('16_liberation_division_state_formation_1945_1950.md',"Republic of Korea được thành lập ở south tháng 8/1948; Democratic People's Republic of Korea được thành lập ở north tháng 9/1948.","Đại Hàn Dân Quốc, tức Hàn Quốc (대한민국 / Republic of Korea), được thành lập ở phía nam tháng 8/1948; Cộng hòa Dân chủ Nhân dân Triều Tiên (조선민주주의인민공화국 / Democratic People's Republic of Korea) được thành lập ở phía bắc tháng 9/1948.")

p=R/'08_early_joseon_state_confucian_order.md'; t=p.read_text(encoding='utf-8')
if 'Cung Cảnh Phúc (경복궁 / Gyeongbokgung Palace)' not in t:
    t=t.replace('## Capital relocation và spatial politics\n\n','## Capital relocation và spatial politics\n\nKhi triều đại mới xây dựng kinh đô Hán Thành (한성 / Hanseong), **Cung Cảnh Phúc (경복궁 / Gyeongbokgung Palace)** trở thành chính cung. `경복궁(景福宮)` có thể hiểu theo Hán–Việt là Cung Cảnh Phúc; cách ghi ba lớp giúp nối nghĩa tiếng Việt, biển tên tiếng Hàn và tài liệu quốc tế.\n\n')
p.write_text(t,encoding='utf-8')

p=R/'17_korean_war_1950_1953.md'; t=p.read_text(encoding='utf-8')
if 'Chiến tranh Triều Tiên (한국전쟁 / Korean War)' not in t:
    t=t.replace('## Chiến tranh bắt đầu như thế nào?\n\n','## Chiến tranh bắt đầu như thế nào?\n\n**Chiến tranh Triều Tiên (한국전쟁 / Korean War)** là cuộc chiến 1950–1953 trên bán đảo Triều Tiên, đồng thời mang tính nội chiến, chiến tranh liên quốc gia và một phần của cấu trúc Chiến tranh Lạnh toàn cầu.\n\n')
t=t.replace('Armistice Agreement được ký ngày 27 July 1953.','**Hiệp định đình chiến Triều Tiên (정전협정 / Korean Armistice Agreement)** được ký ngày 27 July 1953.')
p.write_text(t,encoding='utf-8')

(R/'32_naming_translation_conventions.md').write_text('''# Quy ước tên riêng Việt–Hàn–Anh\n\nTên người, địa điểm, triều đại, sự kiện, văn bản và thiết chế quan trọng được ghi lần đầu theo mẫu:\n\n> **Tên tiếng Việt (한국어 원문 / English name)**\n\nVí dụ: **Cung Cảnh Phúc (경복궁 / Gyeongbokgung Palace)**. Tên có cách Hán–Việt tự nhiên hoặc quen thuộc được dịch, như **Cao Ly (고려 / Goryeo)**, **Bột Hải (발해 / Balhae)**, **Bình Nhưỡng (평양 / Pyongyang)**. Tên hiện đại mà Hán–Việt gây khó nhận diện giữ romanization, như **Seoul (서울 / Seoul)**, **Gwangju (광주 / Gwangju)**, **Park Chung-hee (박정희 / Park Chung-hee)**. Romanization ưu tiên Revised Romanization, trừ conventional English names đã phổ biến.\n\n## Bảng tra nhanh\n\n| Việt | 한국어 | English |\n|---|---|---|\n| Cổ Triều Tiên | 고조선 | Gojoseon |\n| Cao Câu Ly | 고구려 | Goguryeo |\n| Bách Tế | 백제 | Baekje |\n| Tân La | 신라 | Silla |\n| Bột Hải | 발해 | Balhae |\n| Cao Ly | 고려 | Goryeo |\n| Triều Tiên | 조선 | Joseon |\n| Đại Hàn Đế Quốc | 대한제국 | Korean Empire |\n| Hàn Quốc / Đại Hàn Dân Quốc | 대한민국 | Republic of Korea |\n| CHDCND Triều Tiên | 조선민주주의인민공화국 | Democratic People's Republic of Korea |\n| Đàn Quân | 단군 | Dangun |\n| Vương Kiến | 왕건 | Wang Geon |\n| Lý Thành Quế | 이성계 | Yi Seong-gye |\n| Vua Sejong Đại đế | 세종대왕 | King Sejong the Great |\n| Đô đốc Yi Sun-sin | 이순신 | Admiral Yi Sun-sin |\n| bán đảo Triều Tiên | 한반도 | Korean Peninsula |\n| Hán Thành | 한성 | Hanseong |\n| Cung Cảnh Phúc | 경복궁 | Gyeongbokgung Palace |\n| Quang Hóa Môn | 광화문 | Gwanghwamun Gate |\n| Bình Nhưỡng | 평양 | Pyongyang |\n| sông Hán | 한강 | Han River |\n| Tam Quốc Sử Ký | 삼국사기 | Samguk Sagi |\n| Kinh Quốc Đại Điển | 경국대전 | Gyeongguk Daejeon |\n| Triều Tiên Vương Triều Thực Lục | 조선왕조실록 | Veritable Records of the Joseon Dynasty |\n| Huấn Dân Chính Âm | 훈민정음 | Hunminjeongeum |\n| Chiến tranh Imjin | 임진왜란 | Imjin War |\n| Phong trào nông dân Đông Học | 동학농민운동 | Donghak Peasant Movement |\n| Cải cách Giáp Ngọ | 갑오개혁 | Gabo Reform |\n| Phong trào 1 tháng 3 | 3·1운동 | March First Movement |\n| Chiến tranh Triều Tiên | 한국전쟁 | Korean War |\n| Phong trào Dân chủ Gwangju | 광주민주화운동 | Gwangju Democratization Movement |\n| Đấu tranh Dân chủ Tháng Sáu | 6월 민주항쟁 | June Democratic Struggle |\n| Làn sóng Hàn Quốc | 한류 | Hallyu / Korean Wave |\n\n## Mental Model\n\nBa dạng tên là ba key trỏ tới cùng một node trong knowledge graph: tiếng Việt giúp hiểu và nhớ, Hangul giúp nhận diện trong môi trường Hàn Quốc, English giúp tra cứu tài liệu quốc tế.\n''',encoding='utf-8')

p=R/'README.md'; t=p.read_text(encoding='utf-8')
if '## Quy ước tên riêng Việt–Hàn–Anh' not in t:
    i=t.find('\n## '); sec='\n## Quy ước tên riêng Việt–Hàn–Anh\n\nLần đầu xuất hiện, tên quan trọng dùng **Tên tiếng Việt (한국어 원문 / English name)**, ví dụ **Cung Cảnh Phúc (경복궁 / Gyeongbokgung Palace)**. Xem [`32_naming_translation_conventions.md`](32_naming_translation_conventions.md).\n'
    t=t[:i]+sec+t[i:]
t=t.replace('File 30 là chronology để tra nhanh; file 31 là glossary Việt–Anh–Hàn và bản đồ nguồn.','File 30 là chronology để tra nhanh; file 31 là glossary Việt–Anh–Hàn và bản đồ nguồn; file 32 là quy ước tên riêng Việt–Hàn–Anh.')
p.write_text(t,encoding='utf-8')
p=R/'00_index_and_dependency.md'; t=p.read_text(encoding='utf-8')
if '32_naming_translation_conventions.md' not in t: t+='\n- [`32_naming_translation_conventions.md`](32_naming_translation_conventions.md) — quy ước tên riêng Việt–Hàn–Anh.\n'
p.write_text(t,encoding='utf-8')
p=R/'31_glossary_and_reference_map.md'; t=p.read_text(encoding='utf-8')
if 'Proper-name index Việt–Hàn–Anh' not in t: t+='\n## Proper-name index Việt–Hàn–Anh\n\nXem [`32_naming_translation_conventions.md`](32_naming_translation_conventions.md). Quy ước: **Tên tiếng Việt (한국어 원문 / English name)**.\n'
p.write_text(t,encoding='utf-8')

p=R/'30_timeline_key_dates.md'; t=p.read_text(encoding='utf-8')
for a,b in {
'| 108 BCE | Han defeats Wiman Joseon |':'| 108 BCE | Nhà Hán đánh bại Vệ Mãn Cổ Triều Tiên (위만조선 / Wiman Joseon) |',
'| 660 | Baekje falls |':'| 660 | Bách Tế (백제 / Baekje) thất thủ |','| 668 | Goguryeo falls |':'| 668 | Cao Câu Ly (고구려 / Goguryeo) thất thủ |',
'| 918 | Goryeo founded |':'| 918 | Cao Ly (고려 / Goryeo) được thành lập |','| 1392 | Joseon founded |':'| 1392 | Triều Tiên (조선 / Joseon) được thành lập |',
'| 1876 | Treaty of Ganghwa |':'| 1876 | Hiệp ước Ganghwa (강화도조약 / Treaty of Ganghwa) |','| 1897 | Korean Empire proclaimed |':'| 1897 | Đại Hàn Đế Quốc (대한제국 / Korean Empire) được tuyên bố |',
'| 1919-03-01 | March First Movement |':'| 1919-03-01 | Phong trào 1 tháng 3 (3·1운동 / March First Movement) |','| 1950-06-25 | Korean War begins |':'| 1950-06-25 | Chiến tranh Triều Tiên (한국전쟁 / Korean War) bắt đầu |',
'| 1980-05 | Gwangju Democratization Movement |':'| 1980-05 | Phong trào Dân chủ Gwangju (광주민주화운동 / Gwangju Democratization Movement) |','| 1987-06 | June Democratic Struggle |':'| 1987-06 | Đấu tranh Dân chủ Tháng Sáu (6월 민주항쟁 / June Democratic Struggle) |',
}.items(): t=t.replace(a,b)
p.write_text(t,encoding='utf-8')
