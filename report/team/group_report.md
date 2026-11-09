# Báo cáo nhóm — Day 02 Discovery & Problem Framing

> Bản chung của nhóm, viết trên repo do nhóm trưởng fork. Không copy file này sang repo cá nhân.
> Template chi tiết và prompt mẫu: [docs/01-worksheet.md](../../docs/01-worksheet.md). Bài mẫu: [docs/02-deliverable-example.md](../../docs/02-deliverable-example.md).

## 1. Thông tin nhóm

- Tên nhóm: Triple Black
- Thành viên: xem `TEAM.md`
- Candidate problem được chọn (1 câu): Người bán hàng online / người vừa học vừa kinh doanh nhỏ phải gom và đối soát dữ liệu giao dịch phân mảnh từ nhiều nguồn (nhiều sàn TMĐT, nhiều file/chứng từ) thành một báo cáo hoặc con số đúng, tốn thời gian và dễ sai.
- Quyết định cuối: Go / Not Yet / No-Go

---

## 2. Hội tụ nhóm (CP3)

### 2.1. Pitch

| # | Người đưa ra | Candidate (Job Story ngắn) | Actor | Bottleneck | Câu hỏi phản biện nhận được (ai hỏi) |
|---:|---|---|---|---|---|
| 1 | Nam | Khi khách hỏi thuê một bộ đồ, muốn biết ngay bộ đó còn trống đúng ngày không, để chốt đơn nhanh | Chủ shop cho thuê đồ | Dò lịch bận/trống bằng tay (~4'/lần) | Pain chỉ của riêng shop bạn hay nhiều người gặp? (Linh) |
| 2 | Nam | Khi vừa sửa code đồ án, muốn cập nhật tài liệu cho khớp, để nộp bản đúng thực tế | SV làm đồ án | Nhớ/dò lại "đã sửa gì" (~25') | Có phải gốc là do chưa ghi changelog không? (Sơn) |
| 3 | Nam | Khi khách freelance mô tả việc mơ hồ, muốn chốt rõ phạm vi trước khi nhận, để job không phình ra | SV nhận job freelance | Chốt scope thiếu danh sách hạng mục → phát sinh | Nguyên nhân do khách hay do quy trình của bạn? (Linh) |
| 4 | Linh | Khi nhập dữ liệu từ hóa đơn/email/form, muốn trích xuất tự động, để khỏi gõ tay vào bảng tính | Kế toán, hành chính | Đọc và gõ lại (~3–4'/hóa đơn) | Nhóm là SV, có kiểm chứng được với kế toán thật không? (Nam) |
| 5 | Linh | Khi nhận yêu cầu mơ hồ từ khách/đồng nghiệp, muốn có checklist câu hỏi làm rõ, để tránh làm sai rồi sửa lại | Người thực hiện task | Thiếu bước làm rõ yêu cầu → 1/3 task phải làm lại | Người gửi yêu cầu có chịu trả lời thêm câu hỏi không? (Sơn) |
| 6 | Linh | Khi họp xong, muốn có bảng tóm tắt và việc cần làm, để khỏi mất công viết biên bản | Quản lý, thành viên nhóm | Viết biên bản (~45'/buổi) | Ghi âm/transcript tiếng Việt chồng tiếng có đủ chính xác? (Nam) |
| 7 | Sơn | Khi đến cuối tuần, muốn kiểm các khoản thanh toán, phí sàn, hoàn tiền và đơn trả, để xác định đúng doanh thu thực nhận | Chủ shop TMĐT (sữa) | Đối chiếu giao dịch nhiều khoản (~20'), tổng ~60'/tuần | Chênh lệch là do phí/hoàn tiền hay do gom sai số liệu? (Nam) |
| 8 | Sơn | Khi cuối tháng, muốn tổng hợp doanh thu, chi phí quảng cáo, số đơn, tỷ lệ hoàn trả từ nhiều sàn, để biết sản phẩm nào hiệu quả | Chủ shop TMĐT | Gom 3 báo cáo Shopee/TikTok/FB (~120'/tháng) | Mỗi sàn xuất file khác định dạng, gom thủ công có hay sai không? (Linh) |
| 9 | Sơn | Khi khách đặt sữa, muốn đơn được đóng gói kỹ và giao nguyên vẹn, để khách không khó chịu khi nhận | Khách, nhân viên đóng gói | ~10% đơn sữa bị móp lon | Đây là vấn đề quy trình đóng gói hay vận chuyển của sàn? (Nam) |

### 2.2. Cluster

| Cluster | Các candidate | Pattern chung |
|---|---|---|
| A — Gom & đối soát dữ liệu phân mảnh từ nhiều nguồn | #4 (nhập liệu hóa đơn/form), #7 (đối soát doanh thu tuần), #8 (báo cáo kinh doanh tháng nhiều sàn) | Phải lấy dữ liệu từ nhiều nguồn/định dạng khác nhau rồi gom, đối chiếu thành một bảng/con số đúng; tốn giờ và dễ sai |
| B — Yêu cầu/mô tả việc mơ hồ → làm sai, làm lại | #3 (scope freelance), #5 (checklist làm rõ yêu cầu) | Việc bắt đầu khi yêu cầu chưa rõ → hiểu sai → phải sửa/làm lại |
| C — Tổng hợp & ghi lại thông tin rải rác | #2 (đồng bộ tài liệu đồ án), #6 (biên bản họp) | Phải nhớ lại và viết lại thông tin đã có ở nơi khác |
| D — Tra cứu trạng thái / chất lượng giao hàng | #1 (lịch trống shop), #9 (đơn sữa móp lon) | Tra nhanh một trạng thái, hoặc kiểm soát chất lượng vật lý khi giao |

### 2.3. Opportunity Solution Tree rút gọn

Gốc là **1 outcome**. Nhánh là **opportunity** (nhu cầu, pain), không phải tính năng hay công cụ.

```text
OUTCOME: Giảm thời gian và sai sót khi phải tự xử lý dữ liệu/công việc lặp của người vừa học vừa kinh doanh nhỏ

├── Opportunity A: Dữ liệu cần dùng nằm rải rác ở nhiều nguồn/định dạng, phải gom và đối chiếu tay nên tốn giờ và dễ sai
├── Opportunity B: Yêu cầu công việc không rõ ngay từ đầu nên làm ra kết quả lệch ý, phải làm lại
└── Opportunity C: Phải nhớ lại và viết lại thông tin đã tồn tại ở nơi khác
```

Những ý đã gạch bỏ vì là solution đội lốt opportunity:

- "Làm một chatbot trả lời khách tự động" — là giải pháp, không phải pain.
- "Dùng AI trích xuất hóa đơn", "app quản lý bán hàng tất-cả-trong-một" — gọi tên công cụ/tính năng, bị gạch khỏi cây OST.
- "Xây Agent tự điều khiển xe tự lái" — solution, phạm vi quá rộng (đã loại ở bước scan trước đó).

### 2.4. Chấm điểm shortlist (1–5)

Shortlist 3 candidate đại diện cho 3 cluster A, B, C (cluster D bị loại trước: lịch shop phạm vi hẹp một người, móp lon là vấn đề vật lý/vận chuyển khó giải bằng phần mềm trong buổi lab).

| Candidate | Actor rõ | Quy trình rõ | Pain có bằng chứng | Impact đo được | Vừa sức lab | So sánh được No AI/Rule/Workflow/Agent | Nhóm hiểu domain | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A — Gom & đối soát dữ liệu đa nguồn (#4 + #7 + #8) | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **34** |
| B — Yêu cầu mơ hồ → làm lại (#3 + #5) | 5 | 4 | 4 | 4 | 5 | 5 | 4 | 31 |
| C — Tổng hợp thông tin rải rác (#2 + #6) | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 27 |

**Candidate được chọn:** Cluster A — *Người bán hàng online / người vừa học vừa kinh doanh nhỏ phải gom và đối soát dữ liệu giao dịch phân mảnh từ nhiều nguồn (nhiều sàn TMĐT, nhiều file/chứng từ) thành một báo cáo hoặc con số đúng, tốn thời gian và dễ sai.*

**Vì sao chọn:**
- Pain phủ **cả 3 thành viên**: Sơn (đối soát doanh thu tuần + báo cáo tháng nhiều sàn), Linh (nhập liệu hóa đơn vào bảng tính), Nam (tổng hợp việc/dữ liệu cuối tuần) -&gt; nhóm hiểu domain và cùng gặp thật.
- **Dễ kiểm chứng với người thật** trong buổi lab: Sơn là người bán online thật; có thể phỏng vấn thêm sinh viên/bạn bè đang bán hàng trên sàn - đều là hành vi đã xảy ra (CP4).
- **Impact đo được rõ**: thời gian gom/đối soát (60–120 phút), tần suất (tuần/tháng), tỷ lệ chênh lệch số liệu, số lỗi mỗi kỳ.
- **So sánh được cả 4 mức AI**: No AI/Rule (template, công thức, import file chuẩn) -&gt; Workflow (AI trích xuất từ nhiều định dạng + đối chiếu, người duyệt) -&gt; Agent (ít phù hợp) → rất thuận cho CP6.

**Vì sao loại các candidate còn lại:**
- **Cluster D:** lịch trống shop (#1) chỉ một mình Nam gặp, phạm vi hẹp; đơn sữa móp lon (#9) là vấn đề đóng gói/vận chuyển vật lý, phần mềm khó giải trong một buổi lab → loại.
- **Cluster C (đồng bộ tài liệu đồ án #2, biên bản họp #6):** impact khó đo khách quan ("tài liệu đúng với code" đo thế nào), biên bản họp phụ thuộc chất lượng transcript tiếng Việt khi nhiều người nói chồng -&gt; để làm hướng mở rộng, không chọn lần này.
- **Cluster B (yêu cầu mơ hồ -&gt; làm lại):** candidate mạnh (31đ), nhưng bằng chứng hiện có mỏng hơn A và impact khó quy ra con số bằng A; nhóm giữ B làm phương án dự phòng nếu kiểm chứng A ở CP4 không ra tín hiệu đủ mạnh.

**Xử lý bất đồng (nếu có):** Ban đầu các thành viên có domain rất khác nhau (shop thuê đồ, công việc văn phòng, bán hàng TMĐT). Nhóm thống nhất không chọn theo domain của một người, mà chọn **pattern chung mạnh nhất và kiểm chứng được**; vì vậy hội tụ về "gom & đối soát dữ liệu đa nguồn" - pattern cả ba cùng gặp. Hướng xe tự lái (phiên bản scan cũ của Sơn) đã được thống nhất loại từ trước vì vượt sức và không kiểm chứng được với người thật.

---

## 3. Kiểm chứng + research giải pháp đã có (CP4)

### 3.1. Assumption Map

| # | Giả định | Loại (Value / Usability / Feasibility / Viability) | Quan trọng (1–5) | Đã có bằng chứng (1–5) | Kiểm chứng trước? |
|---:|---|---|---:|---:|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

*Điền 4–6 giả định; xóa dòng thừa.*

Giả định nhóm kiểm chứng trong buổi này:

### 3.2. Kiểm chứng

Cách đã dùng: Phỏng vấn / Survey / Log, ticket, review

Interview snapshot (mỗi buổi phỏng vấn một bảng, hoặc đặt file trong `report/assets/cp4-interview-snapshot-N.md`):

| Trường | Nội dung |
|---|---|
| Người được hỏi (vai trò, không ghi tên thật) | |
| Câu nói đáng nhớ nhất (nguyên văn) | |
| Lần gần nhất gặp vấn đề này: chuyện gì đã xảy ra? | |
| Hiện đang xử lý bằng cách nào (workaround)? | |
| Mất bao lâu, bao lần? | |
| Insight / opportunity rút ra | |

Tổng hợp:

| Nguồn | Số người / số mẫu | Tín hiệu xác nhận | Tín hiệu phản bác |
|---|---:|---|---|
| | | | |

**Nhóm đã sửa problem thế nào sau kiểm chứng:**

### 3.3. Research giải pháp đã có

| Công cụ / case / pattern | Link | Giải bước nào trong quy trình? | Điểm mạnh | Khoảng trống / rủi ro | Bài học cho nhóm |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

---

## 4. Quy trình trước/sau (CP5)

### 4.1. Quy trình hiện tại

Sơ đồ (ASCII, Mermaid hoặc link ảnh trong `report/assets/`):

```text

```

| Bước | Actor | Input | Output | Thời gian / tần suất | Ghi chú |
|---:|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Bottleneck chính:**

### 4.2. Quy trình tương lai

Ghi rõ bước nào **Rule**, bước nào **AI**, bước nào **con người**, **boundary** ở đâu, **phương án quay về** khi AI sai.

```text

```

### 4.3. Before / after

| Chỉ số | Trước | Sau (kỳ vọng) | Ghi chú |
|---|---:|---:|---|
| Số bước | | | |
| Tổng thời gian | | | |
| Số bước thủ công | | | |
| Bottleneck chính | | | |
| Rủi ro mới phát sinh | | | |

---

## 5. Problem Statement v0 (CP5)

| Trường | Nội dung |
|---|---|
| **Actor** | |
| **Quy trình** | |
| **Bottleneck** | |
| **Impact** | |
| **Success Metric** (baseline → target, cách đo) | |
| **Boundary** (AI không được làm gì; khi nào cần con người kiểm tra — HITL) | |

Phản biện nhận được (từ AI hoặc nhóm khác) và nhóm có đồng ý không:

-

---

## 6. Mức can thiệp AI (CP6)

### 6.1. Ma trận độ mơ hồ × độ phức tạp

Bài của nhóm nằm ở ô:

Vì sao:

### 6.2. So sánh 4 mức

| Mức | Phương án cho bài của nhóm | Đủ khi nào | Rủi ro | Chọn? |
|---|---|---|---|---|
| **No AI** (sửa quy trình) | | | | |
| **Rule** | | | | |
| **Workflow** | | | | |
| **Agent** | | | | |

**Mức chọn:**

**Vì sao không chọn mức đơn giản hơn:**

### 6.3. AI Canvas rút gọn

| Thành phần | Nội dung |
|---|---|
| **Prediction** — AI dự đoán / tạo ra gì? | |
| **Judgment** — con người cân nhắc, quyết định gì? | |
| **Action** — hành động cuối cùng là gì, ai làm? | |
| **Outcome** — đo kết quả bằng gì? | |
| **Input** — AI cần dữ liệu đầu vào gì mỗi lần chạy? Có sẵn không? | |
| **Feedback** — lấy phản hồi ở đâu để cải thiện? | |

### 6.4. Hai câu hỏi của Google PAIR

- Người dùng muốn **được hỗ trợ (augment)** hay **giao hẳn việc (automate)**? Bằng chứng:
- AI sai kiểu nào tệ hơn, **báo nhầm** hay **bỏ sót**? Vì sao, và thiết kế đã xử lý thế nào:

---

## 7. Problem Statement v1 + tiêu chí đánh giá (CP6)

| Trường | Nội dung |
|---|---|
| **Actor** | |
| **Quy trình** | |
| **Bottleneck** | |
| **Impact** | |
| **Success Metric** (baseline → target, cách đo) | |
| **Boundary** | |
| **AI intervention point** | |
| **Mức chọn** | No AI / Rule / Workflow / Agent |
| **Rủi ro & người kiểm tra** | |

**Thay đổi so với v0 và lý do:**

| Trường | v0 | v1 | Vì sao đổi |
|---|---|---|---|
| | | | |

**Tiêu chí đánh giá đầu ra của AI (3–5 tiêu chí):**

| # | Tiêu chí | Đạt khi | Không đạt khi |
|---:|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## 8. Quyết định (CP6)

### 8.1. Bốn rủi ro

| Rủi ro | Câu hỏi | Mức độ rủi ro (Thấp = an toàn / TB / Cao = nguy hiểm) | Lý do / bằng chứng |
|---|---|---|---|
| **Value** | Người dùng có thật sự cần và sẽ dùng không? | | |
| **Usability** | Người dùng có dùng được, có hiểu và sửa được đầu ra của AI không? | | |
| **Feasibility** | Có đủ dữ liệu, công cụ, kỹ năng để làm không? | | |
| **Viability** | Có hợp chi phí, pháp lý, quy định tổ chức không? Ai vận hành? | | |

### 8.2. Kết luận

**Quyết định:** Go / Not Yet / No-Go

**Lý do:**

**Nếu Go — pilot nhỏ nhất:**

**Nếu Not Yet — cần kiểm chứng gì trước:**

**Nếu No-Go — nên làm gì thay AI:**

**Ngưỡng dừng** (nếu sau … mà … thì quay về …):

---

## 9. Hạn chế và hướng tiếp theo

-

## 10. Tài liệu tham khảo

-
