# Báo cáo nhóm — Day 02 Discovery &amp; Problem Framing

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


| #   | Người đưa ra | Candidate (Job Story ngắn)                                                                                                     | Actor                     | Bottleneck                                               | Câu hỏi phản biện nhận được (ai hỏi)                                    |
| ---: | ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1   | Nam          | Khi khách hỏi thuê một bộ đồ, muốn biết ngay bộ đó còn trống đúng ngày không, để chốt đơn nhanh                                | Chủ shop cho thuê đồ      | Dò lịch bận/trống bằng tay (\~4'/lần)                    | Pain chỉ của riêng shop bạn hay nhiều người gặp? (Linh)                 |
| 2   | Nam          | Khi vừa sửa code đồ án, muốn cập nhật tài liệu cho khớp, để nộp bản đúng thực tế                                               | SV làm đồ án              | Nhớ/dò lại "đã sửa gì" (\~25')                           | Có phải gốc là do chưa ghi changelog không? (Sơn)                       |
| 3   | Nam          | Khi khách freelance mô tả việc mơ hồ, muốn chốt rõ phạm vi trước khi nhận, để job không phình ra                               | SV nhận job freelance     | Chốt scope thiếu danh sách hạng mục → phát sinh          | Nguyên nhân do khách hay do quy trình của bạn? (Linh)                   |
| 4   | Linh         | Khi nhập dữ liệu từ hóa đơn/email/form, muốn trích xuất tự động, để khỏi gõ tay vào bảng tính                                  | Kế toán, hành chính       | Đọc và gõ lại (\~3–4'/hóa đơn)                           | Nhóm là SV, có kiểm chứng được với kế toán thật không? (Nam)            |
| 5   | Linh         | Khi nhận yêu cầu mơ hồ từ khách/đồng nghiệp, muốn có checklist câu hỏi làm rõ, để tránh làm sai rồi sửa lại                    | Người thực hiện task      | Thiếu bước làm rõ yêu cầu → 1/3 task phải làm lại        | Người gửi yêu cầu có chịu trả lời thêm câu hỏi không? (Sơn)             |
| 6   | Linh         | Khi họp xong, muốn có bảng tóm tắt và việc cần làm, để khỏi mất công viết biên bản                                             | Quản lý, thành viên nhóm  | Viết biên bản (\~45'/buổi)                               | Ghi âm/transcript tiếng Việt chồng tiếng có đủ chính xác? (Nam)         |
| 7   | Sơn          | Khi đến cuối tuần, muốn kiểm các khoản thanh toán, phí sàn, hoàn tiền và đơn trả, để xác định đúng doanh thu thực nhận         | Chủ shop TMĐT (sữa)       | Đối chiếu giao dịch nhiều khoản (\~20'), tổng \~60'/tuần | Chênh lệch là do phí/hoàn tiền hay do gom sai số liệu? (Nam)            |
| 8   | Sơn          | Khi cuối tháng, muốn tổng hợp doanh thu, chi phí quảng cáo, số đơn, tỷ lệ hoàn trả từ nhiều sàn, để biết sản phẩm nào hiệu quả | Chủ shop TMĐT             | Gom 3 báo cáo Shopee/TikTok/FB (\~120'/tháng)            | Mỗi sàn xuất file khác định dạng, gom thủ công có hay sai không? (Linh) |
| 9   | Sơn          | Khi khách đặt sữa, muốn đơn được đóng gói kỹ và giao nguyên vẹn, để khách không khó chịu khi nhận                              | Khách, nhân viên đóng gói | \~10% đơn sữa bị móp lon                                 | Đây là vấn đề quy trình đóng gói hay vận chuyển của sàn? (Nam)          |


### 2.2. Cluster


| Cluster                                                 | Các candidate                                                                                      | Pattern chung                                                                                                        |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| A — Gom &amp; đối soát dữ liệu phân mảnh từ nhiều nguồn | #4 (nhập liệu hóa đơn/form), #7 (đối soát doanh thu tuần), #8 (báo cáo kinh doanh tháng nhiều sàn) | Phải lấy dữ liệu từ nhiều nguồn/định dạng khác nhau rồi gom, đối chiếu thành một bảng/con số đúng; tốn giờ và dễ sai |
| B — Yêu cầu/mô tả việc mơ hồ → làm sai, làm lại         | #3 (scope freelance), #5 (checklist làm rõ yêu cầu)                                                | Việc bắt đầu khi yêu cầu chưa rõ → hiểu sai → phải sửa/làm lại                                                       |
| C — Tổng hợp &amp; ghi lại thông tin rải rác            | #2 (đồng bộ tài liệu đồ án), #6 (biên bản họp)                                                     | Phải nhớ lại và viết lại thông tin đã có ở nơi khác                                                                  |
| D — Tra cứu trạng thái / chất lượng giao hàng           | #1 (lịch trống shop), #9 (đơn sữa móp lon)                                                         | Tra nhanh một trạng thái, hoặc kiểm soát chất lượng vật lý khi giao                                                  |


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


| Candidate                                              | Actor rõ | Quy trình rõ | Pain có bằng chứng | Impact đo được | Vừa sức lab | So sánh được No AI/Rule/Workflow/Agent | Nhóm hiểu domain | Tổng   |
| ------------------------------------------------------ | --------: | ------------: | ------------------: | --------------: | -----------: | --------------------------------------: | ----------------: | ------: |
| A — Gom &amp; đối soát dữ liệu đa nguồn (#4 + #7 + #8) | 5        | 5            | 5                  | 5              | 4           | 5                                      | 5                | **34** |
| B — Yêu cầu mơ hồ → làm lại (#3 + #5)                  | 5        | 4            | 4                  | 4              | 5           | 5                                      | 4                | 31     |
| C — Tổng hợp thông tin rải rác (#2 + #6)               | 4        | 4            | 4                  | 3              | 4           | 4                                      | 4                | 27     |


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

**Xử lý bất đồng (nếu có):** Ban đầu các thành viên có domain rất khác nhau (shop thuê đồ, công việc văn phòng, bán hàng TMĐT). Nhóm thống nhất không chọn theo domain của một người, mà chọn **pattern chung mạnh nhất và kiểm chứng được**; vì vậy hội tụ về "gom &amp; đối soát dữ liệu đa nguồn" - pattern cả ba cùng gặp. Hướng xe tự lái (phiên bản scan cũ của Sơn) đã được thống nhất loại từ trước vì vượt sức và không kiểm chứng được với người thật.

---

## 3. Kiểm chứng + research giải pháp đã có (CP4)

### 3.1. Assumption Map


| # | Giả định | Loại | Quan trọng (1–5) | Đã có bằng chứng (1–5) | Kiểm chứng trước? |
|:-:|---|---|:-:|:-:|:-:|
| 1 | Người bán online thật sự mất nhiều thời gian và hay sai khi gom/đối soát số liệu từ nhiều nguồn | Value | 5 | 3 |  Có |
| 2 | Việc gom/đối soát hiện làm thủ công (Excel/chép tay), chưa dùng công cụ chuyên dụng | Feasibility | 4 | 3 |  Có |
| 3 | Chênh lệch số liệu gây hậu quả thật (ghi sai doanh thu, quyết định sai sản phẩm) | Value | 5 | 2 | Có  |
| 4 | Người bán sẵn sàng đổi cách làm / dùng công cụ mới nếu tiết kiệm thời gian | Usability | 4 | 2 |  Có |
| 5 | Dữ liệu các sàn xuất ra đủ để gom lại mà không cần nhập tay toàn bộ | Feasibility | 3 | 3 | Chưa |
| 6 | Chi phí/công sức duy trì cách làm mới không lớn hơn lợi ích | Viability | 3 | 2 | Chưa |

**Giả định nhóm kiểm chứng trong buổi này:** #1, #3, #4 — đều thuộc nhóm quan trọng nhưng ít bằng chứng. Nhóm sử dụng phỏng vấn định tính để tìm hiểu hành vi thực tế của người bán online.

---

## 3.2. Kiểm chứng

**Cách đã dùng:** Phỏng vấn 2 người bán hàng online.

### Bộ câu hỏi phỏng vấn

1. Gần đây nhất bạn chốt doanh thu / làm báo cáo bán hàng là khi nào? Kể lại hôm đó bạn làm những bước gì?
2. Lúc đó bạn lấy số liệu từ những nguồn nào?
3. Bước nào mất thời gian nhất? Khoảng bao lâu?
4. Đã có lần nào số liệu bị lệch / sai chưa? Lần gần nhất là chuyện gì, hậu quả ra sao?
5. Hiện bạn đang làm việc đó bằng cách gì? (Excel, chép tay, công cụ nào?)
6. Bạn đã từng thử cách nào khác để đỡ mất công chưa? Kết quả thế nào?

### Tổng hợp

| Nguồn | Số người/mẫu | Tín hiệu xác nhận | Tín hiệu phản bác |
|---|:-:|---|---|
| Phỏng vấn người bán online | 2 | Cả 2 đều phải kiểm tra số liệu từ nhiều nguồn; 1 người từng gặp chênh lệch do đơn hoàn và phí sàn. | 1 người cho biết Excel vẫn đáp ứng được nhu cầu vì số lượng đơn chưa nhiều. |

**Nhóm đã sửa problem thế nào sau kiểm chứng:**

Ban đầu, nhóm tập trung vào việc gom dữ liệu từ nhiều sàn. Sau khi xem xét các tình huống, nhóm chuyển trọng tâm sang việc đối soát chênh lệch giữa doanh thu, phí sàn, đơn hoàn và số tiền thực nhận. Đây là vấn đề cụ thể hơn và có thể đo lường được. Nhóm cũng xác định giải pháp cần phù hợp với shop nhỏ, tránh làm quy trình trở nên phức tạp hơn.


### 3.3. Research giải pháp đã có


| Công cụ / case / pattern                                              | Link                                                                                                                | Giải bước nào?                                                              | Điểm mạnh                                                                  | Khoảng trống / rủi ro                                                                                                         | Bài học cho nhóm                                                                                 |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Sapo Omnichannel** (phần mềm quản lý bán hàng đa kênh)              | [sapo.vn/omnichannel.html](https://sapo.vn/omnichannel.html)                                                        | Bước 1 + 3: kết nối nhiều sàn, gom đơn và doanh thu về một nơi              | Đồng bộ đa sàn tự động; có báo cáo bán hàng tập trung; phổ biến ở Việt Nam | Trả phí theo gói; phần đối soát phí sàn / hoàn tiền / đơn trả ở mức chi tiết có thể chưa khớp 100% với số sàn thanh toán thật | Bước “gom” đã có công cụ làm tốt → không nên làm lại; giá trị nằm ở bước **đối soát chênh lệch** |
| **Pancake POS** (quản lý bán hàng đa kênh, mạnh về mạng xã hội)       | [docs.pos.pages.fm — Kết nối Shopee](https://docs.pos.pages.fm/pos/thiet-lap-shop/kenh-ban/ket-noi-kenh-ban/shopee) | Bước 1 + 3: gom đơn từ Facebook, Shopee, TikTok vào một hệ thống            | Mạnh ở kênh Facebook/mạng xã hội; quen thuộc với shop nhỏ                  | Phụ thuộc kết nối API với từng sàn; tính năng đối soát sâu bị giới hạn theo gói                                               | Xác nhận lại: pain thật không phải “gom” mà là **tìm và giải thích chênh lệch**                  |
| **Google Sheets + file xuất từ Shopee Seller Center** (pattern No-AI) | [seller.shopee.vn](https://seller.shopee.vn)                                                                        | Bước 1 → 4: tải file từng sàn rồi dùng công thức / pivot để gộp và đối soát | Miễn phí; linh hoạt; người bán tự kiểm soát số liệu                        | Vẫn tốn công ghép tay; dễ sai khi mỗi sàn đổi định dạng file; dễ bỏ sót dòng chênh                                            | Dùng làm **phương án No AI/Rule** để so sánh ở CP6 và làm phương án quay về                      |


---

## 4. Quy trình trước/sau (CP5)

### 4.1. Quy trình hiện tại

Sơ đồ (ASCII, Mermaid hoặc link ảnh trong `report/assets/`):

```text
HIỆN TẠI — ~60 phút/tuần (đối soát).

[1 Tải báo cáo từng sàn: 10']
   → [2 Chuẩn hoá từng file khác định dạng: 10']
   → [3 Gộp dữ liệu nhiều nguồn vào 1 bảng: 10']
   → [4 Đối chiếu phí sàn / hoàn tiền / đơn trả, tìm chênh lệch: 20']  ← BOTTLENECK
   → [5 Tính doanh thu thực nhận: 5']
   → [6 Lưu/gửi báo cáo: 5']
```


| Bước | Actor     | Input                                | Output                    | Thời gian / tần suất | Ghi chú                      |
| :----: | --------- | ------------------------------------ | ------------------------- | :--------------------: | ---------------------------- |
| 1    | Người bán | Tài khoản các sàn (Shopee/TikTok/FB) | File báo cáo thô từng sàn | 10' / tuần           | Mỗi sàn một nơi tải          |
| 2    | Người bán | File thô mỗi sàn                     | File chuẩn hoá cột        | 10' / tuần           | Mỗi sàn khác định dạng       |
| 3    | Người bán | Các file chuẩn hoá                   | 1 bảng tổng hợp           | 10' / tuần           | Copy–paste tay, dễ lệch dòng |
| 4    | Người bán | Bảng tổng hợp + phí/hoàn tiền        | Danh sách chênh lệch      | 20' / tuần           | **Bottleneck**               |
| 5    | Người bán | Bảng đã đối chiếu                    | Doanh thu thực nhận       | 5' / tuần            |                              |
| 6    | Người bán | Kết quả                              | Báo cáo lưu/gửi           | 5' / tuần            |                              |


Bottleneck chính: Bước 4 — đối chiếu phí sàn / hoàn tiền / đơn trả để tìm chênh lệch (\~20'/lần), chiếm 1/3 tổng thời gian, dễ bỏ sót và khiến doanh thu ghi nhận sai.

### 4.2. Quy trình tương lai



```text
TƯƠNG LAI — kỳ vọng ~30 phút/tuần

[1 Tải báo cáo từng sàn: 10']  (CON NGƯỜI, như cũ)
   → [2 RULE: chuẩn hoá cột theo mẫu cố định mỗi sàn: 3']
   → [3 RULE/AI: gộp & khớp các dòng về 1 bảng chung: 3']
   → [4 AI: phát hiện & phân loại dòng chênh lệch, gợi ý khoản cần xem: 4']
        └─ BOUNDARY: AI chỉ GỢI Ý dòng nghi ngờ, KHÔNG tự sửa số, KHÔNG tự chốt doanh thu
   → [5 CON NGƯỜI (HITL): duyệt dòng AI gắn cờ + đọc lướt toàn bảng: 7']
   → [6 CON NGƯỜI: chốt doanh thu thực nhận & lưu báo cáo: 3']
                                                    Tổng: ~30'/tuần
```

### 4.3. Before / after


| Bước | Ai làm           | Việc                                                                                  | Thời gian |
| :----: | ---------------- | ------------------------------------------------------------------------------------- | :---------: |
| 1    | Con người        | Tải báo cáo từng sàn                                                                  | 10'       |
| 2    | Rule             | Chuẩn hoá cột theo mẫu cố định của mỗi sàn                                            | 3'        |
| 3    | Rule/AI          | Gộp &amp; khớp các dòng về 1 bảng chung                                               | 3'        |
| 4    | **AI**           | Phát hiện &amp; phân loại dòng chênh lệch (phí sàn / hoàn tiền / đơn trả / lệch dòng) | 4'        |
| 5    | Con người (HITL) | Duyệt dòng AI gắn cờ, xác nhận/đính chính; đọc lướt toàn bảng để bắt AI bỏ sót        | 7'        |
| 6    | Con người        | Chốt doanh thu thực nhận &amp; lưu báo cáo                                            | 3'        |


---

## 5. Problem Statement v0 (CP5)


| Trường                                                                     | Nội dung                                                                                                                                                                          |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actor**                                                                  | Người bán hàng online nhỏ (chủ shop / người vừa học vừa kinh doanh) tự đối soát doanh thu và báo cáo bán hàng.                                                                    |
| **Quy trình**                                                              | Cuối tuần/tháng: tải báo cáo từng sàn → chuẩn hoá → gộp vào một bảng → đối chiếu phí/hoàn tiền/đơn trả → tính doanh thu thực nhận → lưu/gửi.                                      |
| **Bottleneck**                                                             | Đối chiếu phí sàn / hoàn tiền / đơn trả để tìm chênh lệch (\~20'/lần), tốn thời gian và dễ bỏ sót.                                                                                |
| **Impact**                                                                 | \~60'/tuần + \~120'/tháng cho một người; chênh lệch bị sót làm ghi nhận sai doanh thu và quyết định sai sản phẩm.                                                                 |
| **Success Metric** (baseline → target, cách đo)                            | Thời gian đối soát tuần: 60' → ≤30' (tự bấm giờ 3 tuần liên tiếp). Số dòng chênh lệch bị bỏ sót: baseline đếm được → giảm ≥50% (đối chiếu chéo bảng người kiểm với bảng đã chốt). |
| **Boundary** (AI không được làm gì; khi nào cần con người kiểm tra — HITL) | AI chỉ gợi ý dòng nghi ngờ; không tự sửa số, không tự chốt doanh thu. HITL bắt buộc: người bán duyệt trước khi chốt. Có phương án quay về đối chiếu tay khi AI gắn cờ sai/thiếu.  |


Phản biện nhận được (từ AI hoặc nhóm khác) và nhóm có đồng ý không:


| #   | Lỗ hổng được chỉ ra                                                                                                          | Đồng ý?   | Nhóm đã xử lý                                                                                                                                      |
| :---: | ---------------------------------------------------------------------------------------------------------------------------- | :---------: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Metric “số dòng chênh lệch bị bỏ sót” chưa rõ baseline đo bằng gì — không có con số gốc thì không chứng minh được cải thiện  | Có        | Bổ sung cách đo: trong 2 kỳ đối soát, một người làm lại độc lập rồi đối chiếu chéo với bảng đã chốt để đếm số dòng sót → lấy đó làm baseline       |
| 2   | Actor “người bán online nhỏ” còn rộng — người bán 1 sàn khác người bán 3–4 sàn; pain đối soát chỉ thật sự nặng khi nhiều sàn | Một phần  | Thu hẹp actor: người bán trên ≥2 sàn TMĐT (đúng trường hợp của Sơn); ghi chú người bán 1 sàn pain nhẹ hơn, để ngoài phạm vi lần này                |
| 3   | Boundary mới nói AI “không tự chốt doanh thu”, nhưng chưa nói khi AI bỏ sót dòng chênh thì ai chịu trách nhiệm phát hiện     | Có        | Thêm vào Boundary: người bán vẫn đọc lướt toàn bảng một lượt ở bước duyệt (không chỉ xem dòng AI gắn cờ), để bắt trường hợp AI bỏ sót              |
| 4   | Success metric thời gian “60' → ≤30'” dựa trên baseline của một người (Sơn) — mẫu quá nhỏ, dễ chủ quan                       | Một phần  | Giữ target nhưng ghi rõ baseline là đo thật từ ≥2 người bán ở CP4; nếu con số thật khác nhiều thì chỉnh lại target theo trung bình                 |
| 5   | Impact đang trộn 2 việc (đối soát tuần + báo cáo tháng) → dễ làm phạm vi phình                                               | Không hẳn | Nhóm giữ cả hai vì cùng một bottleneck (gộp + đối chiếu đa nguồn), nhưng chọn đối soát tuần làm phạm vi chính để vừa sức; báo cáo tháng là mở rộng |


---

## 6. Mức can thiệp AI (CP6)

### 6.1. Ma trận độ mơ hồ × độ phức tạp

Bài của nhóm nằm ở ô: Độ mơ hồ Trung bình – Thấp × Độ phức tạp Trung bình.

Vì sao: Quy trình đã rõ các bước và đầu ra có đáp án đúng/sai (doanh thu thực nhận là con số kiểm được) → không quá mơ hồ. Nhưng dữ liệu đến từ nhiều sàn, nhiều định dạng, phần phát hiện dòng chênh lệch cần nhận dạng mẫu → phức tạp vừa, nhiều hơn mức một công thức Excel đơn thuần.

### 6.2. So sánh 4 mức


| Mức                       | Phương án cho bài của nhóm                                                                                             | Đủ khi nào                                                                               | Rủi ro                                                            | Chọn?                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------- |
| **No AI** (sửa quy trình) | Dùng template chuẩn hoá + pivot/công thức Excel, import file chuẩn                                                     | Khi các sàn xuất file cùng định dạng và ít phát sinh chênh lệch                          | Vẫn tốn công ghép tay, không tự bắt dòng chênh lệch bất thường    | Không                                  |
| **Rule**                  | Macro/công thức cố định: tự gộp cột theo mẫu, đánh dấu dòng theo<br>điều kiện cứng                                     | Khi các loại chênh lệch đều theo quy tắc rõ ràng                                         | Sàn đổi định dạng hoặc chênh lệch kiểu mới → rule bỏ sót          | Một phần (dùng cho bước gộp/chuẩn hoá) |
| **Workflow**              | Các bước định sẵn, AI làm một phần: gộp đa định dạng + phát hiện &amp; phân loại dòng nghi ngờ chênh lệch, người duyệt | Khi dữ liệu đa dạng, chênh lệch không chỉ theo quy tắc cứng, nhưng quy trình vẫn cố định | AI gắn cờ sai/bỏ sót → giảm bằng HITL + phương án quay về         | Có                                     |
| **Agent**                 | AI tự quyết các bước, tự truy vấn sàn, tự chốt doanh thu                                                               | Khi cần tự ra quyết định nhiều bước không định trước                                     | Tự chốt số tài chính rủi ro cao, khó kiểm soát, quá mức cần thiết | Không                                  |


**Mức chọn: Workflow**

**Vì sao không chọn mức đơn giản hơn:**

- Không chọn No AI/Rule đơn thuần vì: mỗi sàn xuất định dạng khác nhau và chênh lệch (phí, hoàn tiền, đơn trả) không phải lúc nào cũng theo quy tắc cứng — rule tĩnh dễ bỏ sót dòng bất thường. Nhưng Rule vẫn được dùng cho bước chuẩn hoá/gộp (phần có quy tắc rõ).
- Không chọn Agent vì: quy trình đã cố định, không cần AI tự quyết bước tiếp theo; để AI tự chốt con số tài chính là rủi ro không đáng.

### 6.3. AI Canvas rút gọn


| Thành phần                                                        | Nội dung                                                                                                         |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Prediction** — AI dự đoán / tạo ra gì?                          | Các dòng giao dịch nghi ngờ chênh lệch và phân loại nguyên nhân (phí sàn, hoàn tiền, đơn trả, lệch dòng khi gộp) |
| **Judgment** — con người cân nhắc, quyết định gì?                 | Người bán xem dòng AI gắn cờ, quyết định đúng/sai, có cần điều chỉnh số không                                    |
| **Action** — hành động cuối cùng là gì, ai làm?                   | Người bán chốt doanh thu thực nhận và lưu/gửi báo cáo (AI không tự chốt)                                         |
| **Outcome** — đo kết quả bằng gì?                                 | Thời gian đối soát/tuần; số dòng chênh lệch bị bỏ sót (đối chiếu chéo)                                           |
| **Input** — AI cần dữ liệu đầu vào gì mỗi lần chạy? Có sẵn không? | File báo cáo xuất từ từng sàn (Shopee/TikTok/FB) — có sẵn, người bán tự tải được                                 |
| **Feedback** — lấy phản hồi ở đâu để cải thiện?                   | Các lần người bán đính chính dòng AI gắn cờ sai → dùng để tinh chỉnh quy tắc/gợi ý                               |


### 6.4. Hai câu hỏi của Google PAIR

- **Augment hay Automate?** → **Augment (hỗ trợ).** Bằng chứng: đây là số liệu tài chính, người bán cần tự kiểm và tự chịu trách nhiệm con số cuối; họ muốn công cụ đỡ việc dò, không muốn giao hẳn việc chốt tiền.
- **Sai kiểu nào tệ hơn — báo nhầm hay bỏ sót?** → **Bỏ sót tệ hơn:** một dòng chênh lệch bị sót làm ghi nhận sai doanh thu thật. Thiết kế xử lý: người duyệt đọc lướt toàn bảng một lượt (không chỉ xem dòng gắn cờ) + AI ưu tiên “thà báo dư còn hơn bỏ sót” (recall cao) ở bước gắn cờ.

---

## 7. Problem Statement v1 + tiêu chí đánh giá (CP6)


| Trường                                          | Nội dung                                                                                                                                                    |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actor**                                       | Người bán hàng online bán trên ≥2 sàn TMĐT (chủ shop nhỏ / người vừa học vừa kinh doanh) tự đối soát doanh thu.                                             |
| **Quy trình**                                   | Cuối tuần: tải báo cáo từng sàn → chuẩn hoá (Rule) → gộp (Rule/AI) → AI gắn cờ dòng nghi ngờ → người duyệt (HITL) → chốt doanh thu → lưu.                   |
| **Bottleneck**                                  | Đối chiếu phí/hoàn tiền/đơn trả để tìm chênh lệch (\~20'/lần), tốn giờ và dễ bỏ sót.                                                                        |
| **Impact**                                      | \~60'/tuần/người; chênh lệch bị sót làm ghi sai doanh thu, quyết định sai sản phẩm.                                                                         |
| **Success Metric** (baseline → target, cách đo) | Thời gian đối soát: 60' → ≤30' (bấm giờ 3 tuần); dòng chênh lệch bỏ sót giảm ≥50% (đối chiếu chéo, baseline đo từ ≥2 người bán).                            |
| **Boundary**                                    | AI chỉ gợi ý; không tự sửa số, không tự chốt doanh thu. HITL bắt buộc; người duyệt đọc lướt toàn bảng để bắt AI bỏ sót; có phương án quay về đối chiếu tay. |
| **AI intervention point**                       | Bước phát hiện &amp; phân loại dòng nghi ngờ chênh lệch sau khi đã gộp dữ liệu.                                                                             |
| **Mức chọn**                                    | Workflow                                                                                                                                                    |
| **Rủi ro &amp; người kiểm tra**                 | Rủi ro: AI bỏ sót/báo nhầm dòng chênh. Người kiểm tra: người bán duyệt trước khi chốt.                                                                      |


**Thay đổi so với v0 và lý do:**


| Trường         | v0                           | v1                                    | Vì sao đổi                                      |
| -------------- | ---------------------------- | ------------------------------------- | ----------------------------------------------- |
| Actor          | Người bán online nhỏ (chung) | Người bán ≥2 sàn                      | Thu hẹp theo phản biện: pain nặng khi nhiều sàn |
| Success Metric | Baseline từ 1 người          | Baseline từ ≥2 người bán              | Phản biện mẫu quá nhỏ → đo thật nhiều người     |
| Boundary       | AI không tự chốt             | Thêm “người duyệt đọc lướt toàn bảng” | Xử lý rủi ro AI bỏ sót (bỏ sót tệ hơn báo nhầm) |


**Tiêu chí đánh giá đầu ra của AI (3–5 tiêu chí):**


| #   | Tiêu chí                          | Đạt khi                                                              | Không đạt khi                                                             |
| :---: | --------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | Độ phủ dòng chênh lệch (recall)   | Gắn cờ đúng ≥90% dòng thực sự có chênh lệch (so với bảng người kiểm) | Bỏ sót &gt;10% dòng chênh lệch                                            |
| 2   | Tỷ lệ báo nhầm (precision) hợp lý | Dòng gắn cờ sai ≤30% (người duyệt chấp nhận được)                    | Quá nhiều báo nhầm làm người duyệt mất lòng tin, duyệt lâu hơn cả làm tay |
| 3   | Phân loại nguyên nhân đúng        | Gán đúng loại (phí/hoàn tiền/đơn trả) ≥80% dòng gắn cờ               | Gán sai loại khiến người duyệt phải tra lại từ đầu                        |
| 4   | Gộp dữ liệu không lệch dòng       | 100% dòng khớp đúng đơn/giao dịch sau khi gộp                        | Có dòng bị lệch/trùng khi gộp đa sàn                                      |
| 5   | Không tự ý thay đổi số gốc        | Giữ nguyên số liệu gốc, chỉ gắn cờ/ghi chú                           | AI chỉnh số gốc của giao dịch                                             |


---

## 8. Quyết định (CP6)

### 8.1. Bốn rủi ro


| Rủi ro          | Câu hỏi                                                           | Mức độ rủi ro (Thấp = an toàn / TB / Cao = nguy hiểm) | Lý do / bằng chứng |
| --------------- | ----------------------------------------------------------------- | ----------------------------------------------------- | ------------------ |
| **Value**       | Người dùng có thật sự cần và sẽ dùng không?                       | Thấp (an toàn) | Pain đo được (~60'/tuần, từng lệch số liệu thật) và phủ nhiều người bán — xác nhận ở CP4. |
| **Usability**   | Người dùng có dùng được, có hiểu và sửa được đầu ra của AI không? | Trung bình | Người bán quen Excel nên tiếp cận được, nhưng cần giao diện duyệt dòng gắn cờ đủ rõ để sửa nhanh. |
| **Feasibility** | Có đủ dữ liệu, công cụ, kỹ năng để làm không?                     | Trung bình | Dữ liệu có sẵn (file xuất từ sàn); nhưng xử lý nhiều định dạng + độ chính xác gắn cờ cần công sức. |
| **Viability**   | Có hợp chi phí, pháp lý, quy định tổ chức không? Ai vận hành?     | Thấp – Trung bình | Chi phí thấp nếu dùng công cụ sẵn; dữ liệu tài chính nội bộ nên cần cẩn trọng bảo mật; người bán tự vận hành. |


### 8.2. Kết luận

**Quyết định:** **Go, phạm vi nhỏ** (pilot ở mức Workflow với một người bán).

**Lý do:** Pain thật và đo được (Value rủi ro thấp), dữ liệu sẵn có, mức Workflow vừa đủ. Các rủi ro còn lại ở mức Trung bình đều kiểm soát được bằng HITL (người bán duyệt trước khi chốt) và phương án quay về đối chiếu tay.

**Nếu Go — pilot nhỏ nhất:** Chạy thử 3 tuần với một người bán (Sơn) trên 2 sàn: Rule gộp dữ liệu + AI gắn cờ dòng nghi ngờ chênh lệch, người bán duyệt và chốt. Đo thời gian đối soát và số dòng bỏ sót theo bộ eval ở Mục 7.

**Nếu Not Yet — cần kiểm chứng gì trước:** Phỏng vấn thêm ≥2 người bán để chắc baseline thời gian và tỷ lệ bỏ sót; kiểm xem file các sàn có đủ trường để gộp mà không nhập tay toàn bộ (giả định #5).

**Nếu No-Go — nên làm gì thay AI:** Dùng phương án No AI/Rule — template chuẩn hoá + pivot/công thức Excel, import file chuẩn — vẫn giảm được phần thời gian gộp.

**Ngưỡng dừng** (nếu sau … mà … thì quay về …): Nếu sau **3 tuần** pilot mà **thời gian đối soát không giảm xuống ≤45'/tuần** hoặc **AI bỏ sót >10% dòng chênh lệch** (eval #1 không đạt), thì **quay về phương án Rule/No AI** (template + pivot Excel) và dừng phần AI.

---

## 9. Hạn chế và hướng tiếp theo

- Baseline hiện chủ yếu từ một người bán (Sơn); cần đo thật từ ≥2 người để số liệu đại diện hơn.
- Chưa kiểm chứng giả định #5 (file các sàn có đủ trường để gộp tự động) và #6 (chi phí duy trì) — để lại cho vòng sau.
- Phạm vi lần này chốt ở khâu đối soát tuần; báo cáo kinh doanh tháng và các pain khác (yêu cầu mơ hồ, tổng hợp thông tin) là hướng mở rộng.
- Hướng tiếp theo: chạy pilot 3 tuần theo bộ eval, thu phản hồi các lần người bán đính chính dòng AI gắn cờ để tinh chỉnh quy tắc.

## 10. Tài liệu tham khảo

- Double Diamond — Design Council (UK): https://www.designcouncil.org.uk/resources/framework-for-innovation/
- Job Story (Jobs-to-be-Done) — Intercom / Alan Klement: https://www.intercom.com/blog/accidentally-invented-job-stories/
- Opportunity Solution Tree — Teresa Torres: https://www.producttalk.org/opportunity-solution-trees/
- Assumptions Mapping — David Bland / Strategyzer: https://www.strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter
- The Mom Test — Rob Fitzpatrick: https://www.momtestbook.com/
- Lean UX Problem Statement — Jeff Gothelf: https://jeffgothelf.com/blog/business-problem-statement-opportunity-statement/
- Google PAIR — User Needs + Defining Success: https://pair.withgoogle.com/chapter/user-needs/
- Building Effective Agents — Anthropic: https://www.anthropic.com/research/building-effective-agents
- AI Canvas — Prediction Machines (HBR): https://hbr.org/2018/04/a-simple-tool-to-start-making-decisions-with-the-help-of-ai
- Four Big Risks — Marty Cagan (SVPG): https://www.svpg.com/four-big-risks/
- Công cụ research CP4: Sapo (https://www.sapo.vn), Pancake POS (https://pos.pancake.vn), Shopee Seller Center (https://seller.shopee.vn)