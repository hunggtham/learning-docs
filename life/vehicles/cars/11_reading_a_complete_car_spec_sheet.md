# Reading a Complete Car Spec Sheet — Đọc xe như một hệ thống, không như bảng số quảng cáo

Mười chapter trước đã tách Cars thành powertrain, transmission, drivetrain, tires, brakes, chassis, engine architecture, thermal management và ADAS. Bước tiếp theo không nên là học thêm một danh sách component; ta cần **ghép các owner đó lại để đọc một spec sheet thật mà không bị một con số peak hoặc một badge marketing kéo lệch kết luận**.

Mục tiêu của chapter này là tạo một reusable workflow:

```text
use case
→ vehicle architecture
→ energy / output
→ gearing / driven wheels
→ mass / dimensions
→ tire / brake / chassis
→ thermal / charging
→ ADAS function
→ maintenance / lifecycle
→ unresolved evidence
```

Điểm chốt ngay từ đầu:

> **Spec sheet là tập measurement/label từ nhiều subsystem khác nhau. Nó không tự tạo ra verdict “xe tốt hơn”.**

---

## 1. Bắt đầu từ use case, không bắt đầu từ horsepower

Một spec chỉ có nghĩa khi biết xe phải giải quyết nhiệm vụ gì.

Ví dụ các use case khác nhau:

```text
city commute
family / child seats
long highway trips
winter / mountain driving
towing
track/repeated high load
frequent DC fast charging
rough roads
low operating cost
long ownership / repairability
```

Cùng `250 kW`, `AWD`, `20-inch wheels` có thể là advantage, neutral hoặc cost tùy use case.

Trước khi đọc bảng, ghi:

```text
primary use:
secondary use:
climate:
annual distance:
parking/space constraints:
load/passenger needs:
charging/refueling access:
ownership horizon:
```

Đây là application của Problem Framing; Life không tự quyết định preference cho người đọc.

---

## 2. Xác định architecture trước metric

Đầu tiên phân loại vehicle theo các trục riêng:

```text
body:
sedan / hatch / wagon / SUV / MPV / coupe / pickup ...

energy architecture:
ICE / HEV / PHEV / BEV ...

drivetrain:
FWD / RWD / AWD / 4WD

transmission/reduction:
AT / CVT / DCT / e-CVT / single-speed reduction ...

engine architecture if applicable:
I3 / I4 / I6 / V6 ...
NA / turbo / supercharged ...
```

Không trộn chúng thành một ranking.

Ví dụ:

```text
SUV + AWD + Hybrid + e-CVT
```

là bốn answers cho bốn câu hỏi khác nhau.

Nếu taxonomy sai ở bước này, các comparison sau cũng dễ sai.

---

## 3. Power và torque: đọc curve/context trước peak number

Spec thường cho:

```text
peak power: kW / hp / PS
peak torque: Nm
RPM range if ICE
```

Peak power hữu ích nhưng không cho biết:

- low-speed response;
- gearing;
- vehicle mass;
- traction;
- sustained thermal capability;
- hybrid/motor blending;
- throttle/control tuning.

Với ICE/turbo, đọc:

```text
peak torque @ RPM range
peak power @ RPM
redline / useful RPM band if available
```

Với EV, motor peak torque có thể xuất hiện từ low speed nhưng wheel force vẫn phụ thuộc reduction ratio và traction; torque may fall as speed rises while power behavior changes.

Mental model:

```text
power-unit output
→ gearing
→ wheel torque
→ tire force
→ acceleration
```

Chapter owner: [`03_transmissions_and_reduction_gearing.md`](03_transmissions_and_reduction_gearing.md).

---

## 4. Power-to-weight giúp normalize nhưng không thay acceleration test

Có thể tính:

```text
power-to-weight = power / vehicle mass
```

Ví dụ:

```text
200 kW / 1600 kg
= 0.125 kW/kg
= 125 kW/tonne
```

Metric này tốt hơn peak power alone để có first-pass performance intuition.

Nhưng nó vẫn bỏ qua:

- launch traction;
- gearing;
- torque curve;
- aero drag at high speed;
- battery/thermal limits;
- shift behavior.

Vì vậy:

```text
power-to-weight
→ sanity-check metric
≠ measured acceleration outcome
```

Dùng Thinking/Estimation mindset nếu claim acceleration không khớp mass/output intuition.

---

## 5. Curb weight, gross weight và payload không phải một con số

Vehicle weight specs có nhiều definitions/protocols theo market/manufacturer.

Common conceptual distinctions:

```text
curb/kerb weight
→ vehicle in defined ready-to-drive state

GVWR / maximum permitted mass
→ vehicle + occupants + cargo within rated limit

payload
→ allowable added load under defined assumptions
```

Không subtract hai random weight numbers từ different protocols rồi coi đó là exact payload.

Khi compare:

- check definition;
- same market/specification;
- options can change mass;
- battery/engine/drivetrain variants change mass.

Mass ảnh hưởng:

```text
acceleration
braking energy
corner load transfer
ride
energy consumption
payload margin
```

Nó là cross-subsystem spec, không chỉ efficiency penalty.

---

## 6. Dimensions: length/width/height chưa nói hết usable space

External dimensions:

- length;
- width;
- height;
- wheelbase;
- ground clearance;
- track width where given.

Internal usefulness còn phụ thuộc:

- floor shape;
- roofline;
- seat packaging;
- battery/tunnel placement;
- suspension intrusion;
- tailgate/body shape.

Wheelbase thường cho intuition về axle spacing/packaging nhưng không guarantee rear legroom or ride quality.

Ground clearance không guarantee off-road ability because approach/departure/breakover geometry, tires, drivetrain, protection and control matter.

Thus:

```text
external dimension
→ packaging constraint
≠ interior-use outcome by itself
```

---

## 7. Cargo volume chỉ có nghĩa khi measurement protocol khớp

Cargo capacity can be measured with different standards, seat positions and load boundaries.

Before comparing liters/cubic feet, ask:

```text
same measurement standard?
seats up/down?
measured to parcel shelf or roof?
underfloor storage included?
front trunk included separately?
```

A seemingly larger number can result from protocol difference.

This is direct application of Consumer Literacy:

```text
number
→ definition
→ test boundary
→ comparison validity
```

Do not treat cargo-volume numbers as universal unless measurement context matches.

---

## 8. Tire-size notation encodes geometry, not “sportiness”

Example:

```text
225/45 R18
```

Rough reading:

- `225` → nominal section width in mm;
- `45` → aspect ratio, sidewall height as % of nominal width;
- `R` → radial construction;
- `18` → wheel/rim diameter in inches.

Approx sidewall height:

```text
225 × 0.45 ≈ 101 mm
```

Larger wheel with lower-profile tire can change:

- steering response;
- unsprung mass depending wheel design;
- impact compliance;
- tire cost;
- damage risk;
- aero/rolling resistance;
- available performance-tire choices.

Do not infer:

```text
20 inch > 18 inch
```

without use case/trade-off.

Owner: [`05_tires_traction_and_contact_patch.md`](05_tires_traction_and_contact_patch.md).

---

## 9. Tire load/speed ratings matter more than visual width alone

Complete tire spec may include load index and speed symbol.

Life-level rule:

```text
tire fitment
≠ only width / wheel diameter
```

It also needs compatible:

- load capacity;
- speed capability;
- diameter/circumference;
- wheel width/offset;
- vehicle clearance;
- pressure specification;
- seasonal/use requirement.

Actual replacement must follow vehicle/tire manufacturer guidance; this chapter does not replace fitment standards.

The important mental model is that tire is a **rated load-bearing force interface**, not styling component.

---

## 10. Brake size is mainly a thermal/capacity clue, not direct stopping-distance score

Specs/reviews may mention:

- rotor diameter;
- ventilated discs;
- multi-piston calipers;
- rear drum/disc;
- regenerative braking.

From chapter 06:

```text
larger thermal capacity
→ better repeated-energy handling potential
```

but first-stop dry-road distance may still be limited mainly by:

- tire grip;
- ABS/control;
- speed;
- mass;
- surface.

Thus compare brake hardware to **duty cycle**:

```text
commuting
vs
towing
vs
mountain descent
vs
track repeated stops
```

Big caliper is not a universal safety score.

---

## 11. Suspension label is architecture, not ride-quality verdict

Specs may list:

```text
MacPherson strut
multi-link
double wishbone
torsion beam
air suspension
adaptive damper
```

These labels describe architecture/features but final ride/handling depends on:

- geometry;
- bushing stiffness;
- spring rate;
- damping calibration;
- anti-roll stiffness;
- tire sidewall;
- wheel mass;
- body stiffness;
- vehicle mass distribution;
- control software.

Therefore:

```text
multi-link
≠ automatically better ride/handling than every torsion beam
```

Architecture creates design freedom/trade-offs; tuning realizes outcome.

Owner: [`07_steering_suspension_and_alignment.md`](07_steering_suspension_and_alignment.md).

---

## 12. ICE engine spec: đọc geometry + aspiration + output + fuel requirement

For an ICE vehicle, capture:

```text
displacement
cylinder count/configuration
NA/turbo/supercharged
compression ratio if meaningful
peak torque + RPM range
peak power + RPM
fuel grade requirement/recommendation
```

Then ask:

```text
how is cylinder filled?
what pressure/thermal loading is implied?
what transmission handles torque?
what vehicle mass must it move?
```

A `1.6 turbo` vs `2.5 NA` comparison needs whole system, not liter alone.

Owner: [`08_engine_displacement_cylinders_na_turbo.md`](08_engine_displacement_cylinders_na_turbo.md).

---

## 13. Hybrid spec: engine power + motor power often cannot simply be added

Hybrid spec sheets can show:

- engine output;
- one or more motor outputs;
- system/combined output;
- battery capacity;
- electric mode details.

Naive arithmetic:

```text
engine peak power + motor peak power
= system peak power
```

may be wrong because peaks can occur at different speeds/conditions and power paths share limits.

Prefer manufacturer **system output** where defined, and understand architecture from chapter 02.

Similarly, front/rear motor peak outputs in AWD EV may not sum exactly to advertised system peak due battery/inverter/control constraints.

---

## 14. Battery capacity: gross/total và usable must be separated

BEV/PHEV battery specs may report:

```text
gross / total capacity
usable / net capacity
```

Battery management usually reserves buffers rather than exposing every electrochemical extreme to user.

For range/energy-use reasoning, usable capacity is often the more relevant denominator if reliably specified.

Do not mix gross capacity of one model with usable capacity of another.

Example sanity check:

```text
usable battery ≈ 75 kWh
consumption ≈ 18 kWh / 100 km

idealized energy-only range
≈ 75 / 18 × 100
≈ 417 km
```

This is not certified/real range prediction; it is a consistency check before considering reserve, speed, climate, HVAC, terrain and test protocol.

---

## 15. kW và kWh phải được tách triệt để

```text
kW
→ power / rate

kWh
→ energy capacity/amount
```

Examples:

```text
80 kWh battery
→ energy storage

200 kW motor
→ mechanical/electrical power capability

250 kW DC charging peak
→ charging power rate
```

Question:

```text
how much energy?
→ kWh

how fast is energy transferred/converted?
→ kW
```

Confusing them breaks every EV calculation afterward.

---

## 16. Charging: AC onboard limit, DC peak and charging curve are different specs

Capture separately:

```text
AC charging input limit
DC fast-charge peak
10–80% or comparable charging time under stated conditions
charging curve if available
battery preconditioning capability
```

Peak DC number alone is weak evidence.

Useful real-world quantity:

```text
average power over a useful SOC window
```

Example:

```text
energy added: 50 kWh
elapsed time: 20 min = 1/3 h
average power ≈ 150 kW
```

A vehicle peaking at 250 kW but tapering quickly may have similar trip time to another peaking lower but sustaining power longer.

Thermal owner: [`09_thermal_management_ice_hybrid_bev.md`](09_thermal_management_ice_hybrid_bev.md).

---

## 17. Range/efficiency figures require protocol + environment context

Certified range/consumption values depend on test cycle/protocol and configuration.

Do not compare numbers blindly across different protocols/markets.

Always annotate:

```text
test protocol / market
wheel/tire configuration
battery/vehicle variant
ambient/test conditions if available
```

Real use changes with:

- speed/aero drag;
- temperature;
- HVAC;
- terrain;
- precipitation/wind;
- payload;
- tire/pressure;
- driving pattern.

A range figure is a **standardized comparison measurement under a protocol**, not a promise for every trip.

---

## 18. Aerodynamic drag grows strongly with speed

For intuition, aerodynamic drag force follows approximately:

```text
F_drag ∝ Cd × A × v²
```

Power needed to overcome drag then grows roughly with another factor of speed:

```text
P_drag ∝ v³
```

under simplifying assumptions.

Therefore high-speed cruising disproportionately increases energy demand.

Specs may provide:

- drag coefficient `Cd`;
- frontal area less commonly;
- sometimes combined aero claims.

`Cd` alone is incomplete because actual drag also depends on frontal area.

Thus:

```text
lower Cd
≠ automatically lower total aerodynamic drag if frontal area differs greatly
```

---

## 19. Fuel tank size or battery capacity tells endurance only when paired with consumption

ICE rough reasoning:

```text
tank liters
÷ L/100 km
→ range estimate
```

EV rough reasoning:

```text
usable kWh
÷ kWh/100 km
→ range estimate
```

But reserve, test condition and actual efficiency matter.

Capacity by itself is not efficiency:

```text
large tank / battery
→ potentially longer endurance
but can coexist with poor consumption
```

This distinction matters when comparing ownership cost and vehicle mass.

---

## 20. Towing capacity is a system rating, not engine-strength metric

Towing depends on more than power:

- cooling/thermal capacity;
- transmission/drivetrain rating;
- braking;
- chassis/hitch structure;
- suspension/load;
- tire ratings;
- stability control;
- legal/certification constraints.

Thus a high-power vehicle can have modest tow rating, while a lower-power vehicle engineered for towing can rate higher.

Do not extrapolate towing capacity from torque alone.

Use official vehicle rating for actual operation.

---

## 21. Payload and towing interact

Tongue/hitch load can consume part of vehicle payload/axle capacity.

Passengers/cargo also consume payload.

Therefore:

```text
maximum trailer rating
+ fully loaded cabin/cargo
```

may not always be simultaneously achievable under every configuration.

Actual safe/legal towing requires vehicle-specific weight ratings and regulations, outside this generic chapter.

Consumer lesson: read **constraint set**, not one maximum.

---

## 22. Ground clearance + AWD still does not equal off-road system

Off-road capability can depend on:

```text
tire
traction control / differential
low-range gearing
approach/departure/breakover angles
ground clearance
underbody protection
cooling
water/dust sealing
suspension travel
```

Therefore:

```text
SUV + AWD
≠ serious off-road capability
```

Body/drivetrain badge is only first layer.

---

## 23. Turning circle is a practical packaging/steering metric

Turning diameter/radius influences:

- parking;
- U-turns;
- narrow streets;
- maneuverability.

It depends on:

- wheelbase;
- steering angle;
- track/geometry;
- tire clearance;
- drivetrain/package constraints.

Long vehicle can still have surprisingly good turning circle if steering geometry allows; compact body does not guarantee best result.

For city use, this metric may matter more than peak horsepower.

---

## 24. Acceleration number must include test definition

`0–100 km/h` or `0–60 mph` appears simple but can differ with:

- rollout conventions;
- surface;
- tire condition;
- battery SOC/temperature;
- launch control;
- fuel;
- weather;
- vehicle load.

When comparison is close, protocol matters.

Also one launch does not measure sustained output.

Use chapter 09 for repeated-load thermal reasoning.

---

## 25. Top speed is often control/gearing/aero/tire-limited, not pure power metric

Maximum speed may be limited by:

- electronic governor;
- motor RPM;
- gear ratio;
- tire rating;
- aerodynamic power demand;
- thermal protection.

Therefore a car with more power can have lower limited top speed.

For everyday use, top speed may have low decision relevance; do not weight it just because spec is easy to compare.

---

## 26. ADAS spec must be translated from brand name to function

Instead of writing:

```text
Brand X Safety Pack
Highway Pilot Plus
Smart Drive Pro
```

map each item to:

```text
warning?
AEB/intervention?
ACC longitudinal control?
lane centering sustained steering?
blind-spot intervention?
driver monitoring?
parking assistance?
```

Then ask responsibility/operating conditions.

Owner: [`10_safety_adas_perception_control_and_limits.md`](10_safety_adas_perception_control_and_limits.md).

This prevents marketing names from being compared as if standardized.

---

## 27. SAE Level does not replace feature behavior review

Even when automation taxonomy level is correctly identified, still evaluate:

- control smoothness;
- cut-in response;
- lane geometry handling;
- driver-monitoring behavior;
- HMI clarity;
- limitations;
- fallback expectations.

```text
same level
≠ same system quality
```

Taxonomy answers task allocation, not complete performance.

---

## 28. Safety rating is outcome/protocol evidence, not immutable vehicle essence

Crash/safety ratings come from defined protocols, test configurations and model-year/market context.

When using them:

```text
rating organization
model year
market/spec
protocol year
tested configuration
```

all matter.

Do not combine old/new protocol scores as if scale identical.

Life should link current official rating source when actual model comparison is performed rather than hard-code scores in a general mechanism chapter.

---

## 29. Warranty spec does not equal reliability probability

Long warranty can reflect:

- manufacturer confidence;
- marketing strategy;
- cost allocation;
- exclusions/conditions;
- market competition.

It does not directly measure field failure rate.

Separate:

```text
reliability
→ probability/frequency of failure under conditions

warranty
→ contractual cost/risk allocation when eligible failure occurs
```

Owner: [`../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md`](../../consumer_literacy/03_warranty_lifecycle_and_total_cost.md).

---

## 30. Maintenance interval is not proof of low maintenance cost

A long oil/service interval says little alone about:

- fluid quantity/cost;
- filter cost;
- labor;
- brakes/tires;
- battery/coolant services;
- transmission service;
- regional severe-duty schedule;
- repair parts.

Similarly EV has fewer certain routine engine items but can still incur:

- tires;
- suspension;
- brakes/corrosion service;
- cabin filters;
- coolant depending design;
- HVAC;
- electronics/sensors;
- body/ADAS calibration repairs.

Maintenance must be modeled as system lifecycle, not count of oil changes.

---

## 31. Wheel/tire option can change several published outcomes at once

Larger/heavier wheel package may change:

- vehicle mass;
- rolling resistance;
- aero;
- acceleration;
- certified range/consumption;
- ride;
- tire price;
- damage risk.

Therefore comparing range from base trim to performance trim without noting wheel/tire can be misleading.

Configuration metadata belongs beside the number.

---

## 32. Options can change more than comfort features

Options may alter:

- curb mass;
- wheels/tires;
- suspension;
- brakes;
- battery;
- motor count;
- cooling package;
- ADAS sensors;
- tow package;
- seating/cargo.

A review/test car may not represent base trim.

Record exact configuration whenever outcome evidence is used.

---

## 33. Price must be decomposed before value comparison

Sticker/MSRP/list price may exclude or include different:

- taxes;
- destination/delivery;
- registration;
- options;
- incentives;
- dealer fees.

Market price can move over time.

Life does not own affordability or financing. For financial decision, hand off price/operating inputs to Personal Finance.

Object-side role is to identify what technical/lifecycle differences the price buys.

---

## 34. TCO inputs from Cars hand off to Consumer Literacy/Personal Finance

Cars can identify:

```text
energy consumption
maintenance items
tire/brake usage
insurance-relevant complexity as input only
repair/calibration complexity
depreciation drivers as observed data
charging/fuel needs
```

But full personal affordability depends on household cash flow, debt, opportunity cost and financing.

Boundary:

```text
Cars
→ object-side cost drivers

Consumer Literacy
→ lifecycle/TCO framework

Personal Finance
→ household decision
```

Do not make Cars a loan calculator.

---

## 35. Reliability claim needs evidence hierarchy

Common weak evidence:

```text
one owner's failure
one mechanic's anecdote
forum thread
brand reputation
architecture stereotype
```

Stronger evidence may include:

- large owner datasets with known limitations;
- warranty/recall data where interpretable;
- fleet experience;
- repeated technical failure reports;
- service bulletins/official campaigns;
- component teardown/root-cause evidence.

Architecture can identify possible failure modes but not field probability.

This is where Cars hands off to Critical Thinking/Research Methods if making broad reliability claims.

---

## 36. Recall count is not a simple “bad car score”

Raw recall count can depend on:

- issue severity;
- population size;
- reporting/recall practices;
- model years grouped;
- how quickly manufacturer/regulator acts;
- whether fix is simple software or major hardware.

Thus compare:

```text
what issue?
which vehicles?
how severe?
what remedy?
what rate/evidence?
```

not `brand A has more recall headlines`.

Current recall information is time-sensitive and should be checked at official regulator/manufacturer sources for actual purchase decisions.

---

## 37. A complete spec reading needs three evidence classes

### Type A — architecture/specification

```text
what hardware/system is installed?
```

### Type B — standardized measurement

```text
range / consumption / crash protocol / official rating
```

### Type C — observed behavior

```text
acceleration
braking
charging curve
noise
ride
handling
repeated-load thermal behavior
```

Good comparison triangulates all three.

Spec sheet alone cannot replace behavior evidence; road review alone can miss exact configuration/spec.

---

## 38. Build a subsystem matrix instead of a pros/cons list

Pros/cons lists often mix importance and domains.

Use matrix:

| Layer | Vehicle A | Vehicle B | What it changes | Evidence quality |
|---|---|---|---|---|
| energy architecture | | | | |
| power/output | | | | |
| gearing/drivetrain | | | | |
| mass/dimensions | | | | |
| tires/brakes | | | | |
| suspension/steering | | | | |
| thermal/charging | | | | |
| ADAS | | | | |
| cargo/payload | | | | |
| maintenance/repair | | | | |
| object-side TCO | | | | |

Then apply use-case weights outside the raw facts.

This keeps `what is true?` separate from `what matters to me?`.

---

## 39. Worked example — two fictional compact SUVs

Assume:

```text
Vehicle A
1.6L turbo HEV
FWD
e-CVT
170 kW system output
1650 kg
18-inch tires

Vehicle B
BEV AWD
250 kW
78 kWh usable
2050 kg
20-inch tires
```

Naive conclusion:

```text
B has more power + AWD → B is better
```

System reading:

### Performance

B has higher peak power but also ~400 kg more mass. Need acceleration/traction evidence.

### Energy

A depends on fuel + hybrid efficiency; B on charging access + electricity consumption.

### Tires

20-inch package may affect ride, cost, range and replacement pricing.

### Thermal

B's repeated fast charging/high-power performance depends on battery/motor thermal management; A's sustained load depends on engine/turbo/transmission cooling.

### ADAS

Same advertised feature names do not guarantee same control quality; map functions and reviews.

### Ownership

Need actual energy prices, maintenance, insurance, depreciation and financing separately.

The correct conclusion is not “A or B wins”; it is that **architecture creates a different trade-off vector**.

---

## 40. Worked sanity check — EV charging claim

Suppose spec says:

```text
10–80% in 25 min
usable capacity ≈ 80 kWh
```

Approx energy in that window:

```text
0.70 × 80 = 56 kWh
```

Average battery-side power ignoring losses/details:

```text
56 kWh / (25/60 h)
≈ 134 kW
```

If marketing also says `250 kW peak`, both can be true because peak lasts only part of curve.

This simple estimate catches misconception:

```text
250 kW peak for 25 min
```

would imply far more energy than actual 10–80% window.

Use estimation as a sanity check, not reverse-engineered exact charging curve.

---

## 41. Worked sanity check — fuel consumption/range

Suppose:

```text
tank = 50 L
consumption = 6.5 L/100 km
```

Idealized arithmetic:

```text
50 / 6.5 × 100
≈ 769 km
```

Real usable range can differ because:

- reserve;
- actual consumption;
- temperature;
- traffic;
- speed;
- terrain.

This does not predict exact range; it checks whether a claim of e.g. `1500 km without refuel` is plausible under given numbers.

---

## 42. Worked sanity check — power-to-weight

```text
Car A: 150 kW, 1500 kg → 100 kW/t
Car B: 200 kW, 2200 kg → ~91 kW/t
```

Even though B has more absolute power, A has higher simple power-to-weight.

This still does not prove A accelerates faster because traction/gearing/curve matter, but it prevents peak-power anchoring.

---

## 43. Configuration snapshot is mandatory for time-sensitive comparison

When documenting a real vehicle, write:

```text
model year:
market/country:
trim:
powertrain:
wheel/tire option:
software version if relevant:
source date:
```

This matters because manufacturer offerings, battery size, ADAS hardware/software and pricing change over time.

A general Cars chapter can stay stable; a model-specific comparison should be snapshot-based.

---

## 44. Source hierarchy for an actual vehicle study

Prefer:

```text
1. official owner/manual/spec/homologation/regulator data
2. official standardized test/rating source
3. instrumented independent test
4. high-quality technical review
5. owner/fleet experience
6. forum/social anecdote
```

Not every question has the same best source.

Examples:

- towing rating → official manual/spec;
- 100–0 braking test → instrumented independent test;
- recurring failure experience → larger field evidence + service info;
- current recall → regulator/official source.

Source authority is question-dependent.

---

## 45. Never compare measurements from incompatible protocols silently

Common mistakes:

```text
WLTP vs EPA range as direct same-scale numbers
one publication's 0–100 vs another using different method
cargo volume under different standards
curb weight under different definitions
```

If protocols differ:

- state difference;
- avoid fake precision;
- use same-source/same-protocol comparison where possible.

Consumer Literacy's protocol discipline is essential for Cars.

---

## 46. Complete worksheet — one-page vehicle reading

```text
IDENTITY
- model year / market / trim:
- source snapshot date:

USE CASE
- primary / secondary:
- climate / roads:
- passengers/cargo/towing:
- charging/refueling:

ARCHITECTURE
- body:
- ICE/HEV/PHEV/BEV:
- engine/motor architecture:
- transmission/reduction:
- drivetrain:

OUTPUT
- power:
- torque + RPM range:
- curb mass:
- power-to-weight sanity check:

DIMENSIONS / LOAD
- length/width/height/wheelbase:
- cargo protocol/value:
- payload/GVWR:
- towing rating:

ROAD INTERFACE
- tire size/rating:
- wheel option:
- brake architecture:
- suspension/steering:

ENERGY / THERMAL
- fuel tank or usable battery:
- consumption protocol:
- range protocol:
- AC/DC charging:
- charging curve evidence:
- thermal/preconditioning:

ADAS / SAFETY
- warning features:
- intervention features:
- sustained control:
- driver responsibility:
- operating limitations:
- rating/test snapshot:

LIFECYCLE
- maintenance schedule:
- tire/brake replacement implications:
- warranty boundaries:
- known failures + evidence quality:
- repair/calibration complexity:

OPEN QUESTIONS
- which claims still lack comparable evidence?
```

This worksheet converts spec browsing into system analysis.

---

## 47. Bàn giao sang maintenance / diagnostics

A spec sheet tells us architecture before failure. Ownership eventually asks a different question:

```text
symptom appears
→ which subsystem could produce it?
→ what observation discriminates between hypotheses?
→ which items are normal wear vs abnormal failure?
→ what maintenance prevents avoidable degradation?
```

The next Cars application chapter should therefore use the architecture map for **maintenance and diagnostic reasoning**, not become a repair manual.

Examples:

```text
vibration
→ tire/wheel/alignment/suspension/drivetrain hypotheses

power loss under repeated load
→ thermal/fuel/boost/protection hypotheses

poor fast charging
→ SOC/battery temp/preconditioning/charger hypotheses
```

Point to keep:

> **A complete car spec sheet is not a scoreboard. Read every number by subsystem, definition, protocol, operating condition and lifecycle consequence; then connect subsystems before deciding what the car can actually do for a use case.**
