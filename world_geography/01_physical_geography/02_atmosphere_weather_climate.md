# Khí quyển, thời tiết và cơ chế tạo thời tiết

## Weather là trạng thái, climate là phân bố

**Thời tiết (weather / 날씨)** là trạng thái khí quyển trong giờ–ngày: temperature, pressure, humidity, wind, cloud và precipitation. **Khí hậu (climate / 기후)** mô tả phân bố thống kê dài hạn của các biến đó: trung bình, variance, seasonality, extreme và persistence.

Vì vậy một ngày lạnh không bác bỏ warming trend, và một ngày nóng không tự chứng minh climate change. Cần tách **event** khỏi **distribution**.

## Thành phần và cấu trúc thẳng đứng của khí quyển

Khí quyển gần mặt đất chủ yếu gồm nitrogen và oxygen, cùng argon, water vapor và trace gases. Water vapor biến đổi mạnh theo không gian và thời gian, đóng vai trò lớn trong cloud, precipitation và greenhouse effect.

Theo profile nhiệt, khí quyển thường chia thành troposphere, stratosphere, mesosphere và thermosphere. Phần lớn weather xảy ra trong **troposphere** vì ở đây water vapor và vertical mixing tập trung.

Stratosphere có ozone hấp thụ UV, làm temperature tăng theo height trong một phần layer. Cấu trúc này hạn chế vertical mixing khác troposphere.

## Pressure là weight của air column

Atmospheric pressure phản ánh weight của column không khí phía trên. Pressure giảm theo altitude vì lượng air above giảm.

Sự khác nhau pressure theo phương ngang tạo **pressure-gradient force**, làm air accelerate từ high pressure về low pressure theo nghĩa động lực ban đầu.

Wind không chỉ “đi từ cao sang thấp” vì rotation và friction làm quỹ đạo phức tạp.

## Coriolis đổi hướng, không tạo năng lượng cho wind

Do Earth quay, vật chuyển động trong reference frame Trái Đất có apparent deflection. Ở Northern Hemisphere lệch về phải, Southern Hemisphere về trái.

**Coriolis parameter** tăng với latitude và bằng 0 tại Equator. Coriolis không khởi động wind; pressure gradient tạo acceleration, còn Coriolis làm đổi direction.

Ở scale lớn và friction nhỏ, pressure-gradient và Coriolis có thể gần cân bằng, tạo **geostrophic wind** chạy gần song song isobar.

## Friction làm surface wind cắt isobar

Gần surface, friction làm wind chậm lại, Coriolis giảm tương đối và wind có component hướng vào low pressure.

Vì vậy surface convergence quanh low pressure có thể hỗ trợ uplift, còn divergence quanh high pressure hỗ trợ subsidence tùy hemisphere và context.

Topography và roughness đô thị làm boundary layer phức tạp hơn simple textbook model.

## Radiation budget: atmosphere được sưởi cả từ trên và dưới

Solar shortwave đi vào hệ; một phần reflect bởi cloud/surface, phần còn lại absorb. Surface phát longwave và truyền heat bằng sensible/latent flux.

Troposphere được sưởi mạnh từ surface, nhưng greenhouse gases và cloud tương tác longwave. Vì vậy temperature structure là kết quả của radiation + convection + phase change + dynamics.

## Stability và lapse rate

Một air parcel nâng lên gặp pressure thấp hơn, expand và cool **adiabatically**. Nếu parcel dry/unsaturated, cooling rate gần dry adiabatic lapse rate; khi saturated, condensation release latent heat làm cooling chậm hơn.

Atmospheric **stability** phụ thuộc so sánh parcel lapse với environmental lapse rate. Unstable atmosphere hỗ trợ convection; stable layer suppress vertical motion.

Đây là cơ chế nền của thunderstorm, fog, inversion và pollution trapping.

## Temperature inversion và air pollution

Thông thường temperature giảm theo height trong troposphere thấp. Nhưng **inversion** là layer nơi temperature tăng theo height, tạo stability mạnh.

Trong basin city, inversion có thể giữ pollutant gần surface. Seoul và nhiều đô thị bao quanh bởi mountain có thể trải nghiệm ventilation khác open coast.

Pollution episode vì thế là interaction giữa emission + boundary-layer meteorology + topography, không chỉ “thành phố xả nhiều”.

## Water vapor, relative humidity và dew point

**Relative humidity** là ratio giữa vapor hiện tại và mức saturation ở temperature đó. Air ấm có saturation vapor pressure cao hơn, nên RH có thể giảm khi air warms dù absolute moisture không đổi.

**Dew point** phản ánh moisture content trực tiếp hơn trong nhiều context: air phải cool tới temperature nào để saturation đạt được.

Cloud formation cần saturation và thường cần condensation nuclei.

## Bốn cơ chế uplift chính

Air có thể nâng do **convection**, **orographic lifting**, **front**, hoặc **convergence**.

Mỗi cơ chế tạo cloud/precipitation pattern khác nhau. Mountain tạo windward rain và leeward rain shadow; front tạo band precipitation; convection tạo storm cell cục bộ nhưng mạnh.

Khi đọc rainfall map, cần hỏi “air bị nâng bằng mechanism nào?”.

## Cloud không chỉ là indicator; chúng tương tác radiation

Cloud low/thick thường reflect solar mạnh và có cooling effect; high thin cloud có thể cho shortwave đi qua nhưng trap longwave, tạo warming effect tương đối.

Net effect phụ thuộc cloud type, altitude, optical thickness và time of day. Đây là lý do cloud feedback là phần phức tạp trong climate system.

## Air mass và front

**Air mass** là khối air có đặc tính temperature/moisture tương đối đồng nhất do source region và history. Khi air mass khác nhau gặp nhau, **front** hình thành.

Warm front, cold front và occluded front trong textbook là idealized structure của mid-latitude cyclone. Real atmosphere có deformation và fronts phức tạp nhưng model giúp xây causal intuition.

## Mid-latitude cyclone và jet stream

Ở mid-latitude, strong horizontal temperature gradient chứa potential energy. Baroclinic instability có thể phát triển wave và cyclone.

**Jet stream** gắn với strong upper-level wind và temperature gradient. Position/shape của jet ảnh hưởng storm track và blocking.

Không nên giải thích cyclone chỉ bằng “low pressure hút gió”; pressure field là phần của một circulation 3D có conservation of momentum và heat transport.

## Tropical cyclone: heat engine trên ocean ấm

Tropical cyclone phát triển khi ocean đủ ấm, atmosphere moist, vertical wind shear không quá mạnh và disturbance có rotation phù hợp.

Storm lấy energy từ latent heat của water vapor. Low central pressure và organized convection duy trì circulation.

Khi lên land hoặc water lạnh, energy/moisture source suy giảm; nhưng flood risk có thể tiếp tục do rainfall và river response.

Wind category không mô tả đầy đủ storm surge và rain hazard.

## Monsoon là seasonal circulation, không chỉ “mùa mưa”

**Monsoon** mô tả seasonal reorganization của wind và precipitation do land–ocean thermal contrast, migration của tropical circulation, topography và large-scale dynamics.

South Asia và East/Southeast Asia có monsoon regime khác nhau. Mountain như Himalaya–Tibetan Plateau và biển lân cận làm pattern regional phức tạp.

Vietnam và Korea cùng chịu seasonal circulation nhưng rainfall timing, typhoon exposure và winter monsoon influence khác nhau.

## Local wind và terrain

Sea breeze, land breeze, valley wind và mountain wind xuất hiện do differential heating ở scale nhỏ hơn.

Urban heat island cũng tạo circulation cục bộ. Building morphology thay đổi turbulence và ventilation.

Đây là lý do forecast model global phải **parameterize** hoặc downscale nhiều process dưới grid size.

## Numerical Weather Prediction

**Dự báo thời tiết số (Numerical Weather Prediction, NWP)** giải hệ phương trình conservation của momentum, mass, energy và moisture trên grid.

Initial condition đến từ observation: satellite, radar, radiosonde, aircraft, buoy, station. **Data assimilation** kết hợp observation với model forecast để tạo state estimate tốt hơn.

Model không “đọc thời tiết tương lai”; nó tích phân equations từ state ước lượng.

## Chaos và ensemble forecast

Atmosphere nhạy với initial condition. Sai số nhỏ phát triển theo thời gian, nên deterministic forecast giảm skill khi lead time tăng.

**Ensemble forecast** chạy nhiều simulation với initial/model perturbation để ước distribution outcome. Spread không phải lỗi cần giấu; nó là thông tin uncertainty.

Người dùng tốt nên đọc “xác suất mưa 70%” như probability/ensemble evidence, không như model do dự.

## Radar, satellite và observation bias

Weather radar đo backscatter từ precipitation particle; satellite đo radiation ở nhiều wavelength. Cả hai cần algorithm để suy rain rate, cloud top hoặc temperature.

Mountain có thể block radar; satellite IR không “nhìn xuyên” cloud như radar; surface station phân bố không đều. Observation field luôn có sampling bias.

## Mô hình tư duy

Weather tại một nơi là kết quả của **energy gradient + pressure + rotation + moisture + stability + vertical motion + surface/terrain**. Forecast là bài toán ước state rồi mô phỏng evolution dưới uncertainty.

Xem tiếp: [Hệ khí hậu toàn cầu](./03_global_climate_system.md), [Oceans](./05_oceans_coasts.md), [Natural hazards](./07_natural_hazards_risk.md).