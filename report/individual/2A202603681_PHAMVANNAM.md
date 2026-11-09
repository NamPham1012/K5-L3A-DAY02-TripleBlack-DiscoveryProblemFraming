# Báo cáo cá nhân — 2A202603681_PHAMVANNAM



## 1. Thông tin học viên

- Họ tên: PHAM VĂN NAM 
- MSSV: 2A202603681
- Email trường (không bắt buộc, repo có thể để public):
- Tên nhóm: TRIPLE BLACK
- Link repo nhóm: [https://github.com/NamPham1012/-K5-L3A-DAY02-TripleBlack-DiscoveryProblemFraming](https://github.com/NamPham1012/-K5-L3A-DAY02-TripleBlack-DiscoveryProblemFraming)



---

## 2. Scan problem (CP1)

Lăng kính: **Lặp lại** · **Tốn thời gian** · **Cần đọc, tổng hợp nhiều thông tin** · **Pain từ người khác**.

**Bối cảnh (actor):** Tôi — sinh viên năm 4 đang làm đồ án tốt nghiệp (vừa sửa code vừa viết tài liệu), đồng thời tự quản lý một shop cho thuê đồ (theo dõi lịch thuê/trả, khách hàng, tình trạng đồ) và thỉnh thoảng nhận thêm job freelance bên ngoài. Các problem dưới đây là pain thật trong ba mảng việc này.




| #   | Lăng kính                         | Job Story: Khi… tôi muốn… để…                                                                                                                                            | Ai chịu ảnh hưởng?   | Dấu hiệu thật (thời gian, tần suất, số người, bằng chứng)                                                                                                                                                                                                            |
| ---: | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Lặp lại                           | Khi hết mỗi ngày ở shop, tôi muốn tổng hợp lại ai thuê bộ nào, thuê/trả ngày nào, để không nhầm lịch và không mất dấu đồ                                                 | Tôi, khách thuê      | \~15 phút/ngày ghi tay + chat; tuần trước nhầm 1 đơn trả.                                                                                                                                                                                                            |
| 2   | Lặp lại                           | Khi tới cuối tuần, tôi muốn tổng hợp lại mọi việc đã làm (đồ án, shop, freelance), để biết tuần tới nên ưu tiên gì                                                       | Tôi                  | \~30 phút mỗi Chủ nhật, thông tin rải ở 3–4 chỗ ghi chú khác nhau.                                                                                                                                                                                                   |
| 3   | Tốn thời gian                     | Khi viết tài liệu đồ án, tôi muốn đồng bộ phần mô tả với code vừa sửa, để nộp bản tài liệu đúng với thực tế                                                              | Tôi, GV hướng dẫn    | \~60 phút mỗi lần cập nhật tài liệu sau một đợt sửa code.                                                                                                                                                                                                            |
| 4   | Tốn thời gian                     | Khi một đơn thuê kết thúc, tôi muốn kiểm và ghi lại bộ nào hỏng/thiếu, để trừ cọc và sửa kịp cho khách sau                                                               | Tôi, khách tiếp theo | \~10 phút/đơn; tháng trước 2 lần suýt giao nhầm đồ đang hỏng.                                                                                                                                                                                                        |
| 5   | Cần đọc, tổng hợp nhiều thông tin | Khi gặp một bug trong đồ án, tôi muốn nhớ lại mình đã thử cách nào rồi, để không sửa lại vòng vo                                                                         | Tôi                  | 3–4 bug/tuần; mỗi bug mất \~20 phút chỉ để dò lại prompt đã đã thử để sửa                                                                                                                                                                                            |
| 6   | Cần đọc, tổng hợp nhiều thông tin | Khi nhận một job freelance mới, tôi muốn ước lượng có đủ thời gian xen với đồ án và shop không, để quyết nhận hay từ chối                                                | Tôi, khách freelance | Tháng trước 1 job vì không khóa scope nên kéo dài hơn tháng, rất mất thời gian                                                                                                                                                                                       |
| 7   | Pain từ người khác                | Khi khách muốn đặt trước một bộ đồ, họ muốn biết ngay bộ đó còn trống ngày họ cần không, để chốt đơn                                                                     | Khách thuê, tôi      | Khách hỏi "Bộ này còn trống không?" tôi phải dò lại danh sách rất mất thời gian                                                                                                                                                                                      |
| 8   | Pain từ người khác                | Khi cộng tác viên freelance nhận task code từ tôi, họ muốn biết ngay tài liệu, code liên quan nằm ở đâu và cần làm đến mức nào, để bắt tay vào làm mà không phải hỏi lại | Cộng tác viên, tôi   | Mỗi lần giao task, CTV hỏi lại 2–3 lượt: “Tài liệu API xem ở đâu?”, “Code từ nhánh nào?”, “File `.env` lấy ở đâu?”, “Sửa ở file nào?”. Mỗi lượt chờ tôi trả lời mất nửa ngày, nên task trễ 1–2 ngày. Có lần CTV đoán sai, code trên nhánh cũ, phải merge lại từ đầu. |


---

## 3. Top 3 Problem Cards + quy trình nháp (CP2)

### Bảng chọn top 3


| Rank | Problem                                      | Vì sao chọn                                                                                   | Điều còn chưa chắc                                              |
| ----: | -------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1    | Lịch trống khi khách đặt đồ thuê (#7)        | Actor rõ, lặp mỗi ngày, bottleneck cụ thể (dò lịch tay), impact đo được, vừa sức một buổi lab | "Trả lời đủ nhanh" là bao lâu thì khách thấy ổn?                |
| 2    | Đồng bộ tài liệu đồ án với code (#3)         | Pain thật hằng tuần, quy trình rõ, có baseline thời gian; ảnh hưởng tới điểm bảo vệ           | "Tài liệu đúng với code" đo thế nào cho khách quan?             |
| 3    | Khóa scope trước khi nhận job freelance (#6) | Impact lớn (job kéo dài gấp đôi), liên quan tiền và uy tín                                    | Nguyên nhân là do giao tiếp với khách hay do quy trình của tôi? |


### Problem Card #1 — Lịch trống khi khách đặt đồ thuê


| Trường                                    | Nội dung                                                                                                                                                                                                                   |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Job Story                                 | Khi khách nhắn hỏi thuê một bộ đồ, tôi muốn biết ngay bộ đó còn trống đúng ngày khách cần không, để trả lời và chốt đơn nhanh                                                                                              |
| Actor                                     | Tôi — chủ shop cho thuê đồ, trực tiếp nhận tin nhắn và chốt đơn                                                                                                                                                            |
| Thời điểm / bối cảnh                      | Suốt cả ngày khi khách nhắn qua Zalo/Messenger, cao điểm vào cuối tuần và mùa lễ                                                                                                                                           |
| Quy trình hiện tại (3–7 bước)             | 1. Nhận tin khách hỏi bộ X cho ngày Y · 2. Mở sổ/file ghi đơn · 3. Dò tay xem bộ X đã có ai thuê trùng ngày Y chưa · 4. Nếu trùng, tìm bộ tương tự thay thế · 5. Nhắn lại khách · 6. Nếu khách chốt thì ghi đơn mới vào sổ |
| Bottleneck (bước nào, mất bao nhiêu phút) | Bước 3 — dò tay trong danh sách/sổ xem bộ đó có trùng lịch không: \~3–5 phút/lần, dễ sót khi nhiều đơn                                                                                                                     |
| Impact (nếu không giải thì sao)           | Khách hỏi \~5–7 lần/tuần; trả lời chậm làm mất đơn; đã có lần nhận trùng 1 bộ cho 2 khách cùng ngày phải xin lỗi và hoàn cọc                                                                                               |
| Success metric (baseline → target)        | Thời gian trả lời "còn trống không" từ \~4 phút/lần xuống dưới 1 phút; số lần nhận trùng lịch từ \~1 lần/tháng xuống 0                                                                                                     |
| Phương án không dùng AI                   | Chuyển sổ tay sang một bảng lịch (Google Sheet/Calendar) theo từng bộ đồ, tra trống/bận bằng mắt — giảm thời gian dò và tránh trùng                                                                                        |
| Giả thuyết về AI (nếu có)                 | Sau này có thể để trợ lý tự đọc tin khách và tra bảng lịch trả lời nháp; nhưng chưa chắc cần ở mức này                                                                                                                     |
| Cảm nhận nhanh                            | **Rule**                                                                                                                                                                                                                   |


Quy trình nháp hiện tại:

```text
HIỆN TẠI — ~4 phút/lần khách hỏi

[1 Nhận tin hỏi bộ X ngày Y: 0.5'] → [2 Mở sổ/file: 0.5']
   → [★3 Dò tay bộ X có trùng ngày Y: 3–5'] ← BOTTLENECK
   → [4 Tìm bộ thay thế nếu trùng: 2'] → [5 Nhắn lại khách: 0.5']
   → [6 Ghi đơn mới nếu chốt: 1']
```

### Problem Card #2 — Đồng bộ tài liệu đồ án với code vừa sửa


| Trường                                    | Nội dung                                                                                                                                                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Job Story                                 | Khi vừa sửa xong một đợt code trong đồ án, tôi muốn cập nhật phần tài liệu mô tả cho khớp, để nộp bản tài liệu đúng với hệ thống thực tế                                                                           |
| Actor                                     | Tôi — sinh viên làm đồ án tốt nghiệp, vừa viết code vừa viết tài liệu nộp cho GV hướng dẫn                                                                                                                         |
| Thời điểm / bối cảnh                      | Mỗi khi sửa một chức năng/API xong, hoặc trước các mốc nộp tài liệu cho GV                                                                                                                                         |
| Quy trình hiện tại (3–7 bước)             | 1. Nhớ lại đợt vừa rồi đã sửa những gì · 2. Dò lại code/commit để xác nhận thay đổi · 3. Tìm đúng chỗ trong tài liệu cần sửa · 4. Viết lại mô tả, cập nhật sơ đồ/ảnh chụp màn hình · 5. Đọc soát lại cho khớp code |
| Bottleneck (bước nào, mất bao nhiêu phút) | Bước 1–2 — nhớ và dò lại "đã sửa gì so với tài liệu cũ": \~25 phút, hay sót chi tiết                                                                                                                               |
| Impact (nếu không giải thì sao)           | 60 phút/lần cập nhật; tài liệu lệch với code khiến GV hỏi vặn lúc bảo vệ, ảnh hưởng điểm                                                                                                                           |
| Success metric (baseline → target)        | Thời gian đồng bộ từ 60 phút xuống dưới 30 phút; số mục tài liệu lệch với code khi GV review từ 3–4 xuống ≤1                                                                                                       |
| Phương án không dùng AI                   | Lập checklist "mỗi lần sửa code thì sửa mục tài liệu nào", ghi changelog ngắn ngay sau mỗi đợt sửa — giảm việc phải nhớ lại                                                                                        |
| Giả thuyết về AI (nếu có)                 | AI đọc diff code + tài liệu cũ, gợi ý nháp đoạn tài liệu cần đổi; tôi review và sửa trước khi nộp                                                                                                                  |
| Cảm nhận nhanh                            | **Workflow**                                                                                                                                                                                                       |


Quy trình nháp hiện tại:

```text
HIỆN TẠI — ~60 phút/lần cập nhật

[★1 Nhớ lại đã sửa gì: 10'] → [★2 Dò code/commit xác nhận: 15'] ← BOTTLENECK
   → [3 Tìm chỗ cần sửa trong tài liệu: 10'] → [4 Viết lại mô tả + sơ đồ/ảnh: 15']
   → [5 Đọc soát khớp code: 10']
```

### Problem Card #3 — Khóa scope trước khi nhận job freelance


| Trường                                    | Nội dung                                                                                                                                                                                                                          |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Job Story                                 | Khi một khách freelance mô tả công việc muốn thuê, tôi muốn chốt rõ phạm vi và khối lượng trước khi nhận, để không bị job phình ra và kéo dài                                                                                     |
| Actor                                     | Tôi — sinh viên nhận thêm job code freelance bên ngoài, tự trao đổi và nhận việc                                                                                                                                                  |
| Thời điểm / bối cảnh                      | Lúc trao đổi ban đầu với khách, trước khi báo giá và đồng ý làm                                                                                                                                                                   |
| Quy trình hiện tại (3–7 bước)             | 1. Nghe khách mô tả nhu cầu (thường mơ hồ) · 2. Hỏi lại vài ý cho rõ · 3. Ước lượng thời gian trong đầu · 4. Báo giá và nhận việc · 5. Trong lúc làm, khách thêm yêu cầu mới · 6. Làm cả phần phát sinh vì chưa chốt scope từ đầu |
| Bottleneck (bước nào, mất bao nhiêu phút) | Bước 1–3 — chốt phạm vi "làm đến đâu là xong" không có danh sách hạng mục rõ nên về sau phát sinh; không đo bằng phút mà bằng việc job đội thời gian                                                                              |
| Impact (nếu không giải thì sao)           | Tháng trước 1 job dự kiến \~2 tuần bị kéo dài \~5 tuần vì không khóa scope; mất thời gian cho đồ án và shop, ảnh hưởng thu nhập/uy tín                                                                                            |
| Success metric (baseline → target)        | Tỷ lệ job đội thời gian &gt;50% so với ước lượng: từ \~2/3 job gần đây xuống ≤1/3; mỗi job có bảng hạng mục scope chốt trước khi bắt đầu                                                                                          |
| Phương án không dùng AI                   | Dùng mẫu "bản mô tả công việc" cố định: liệt kê hạng mục làm / không làm, số vòng sửa, mốc nghiệm thu — gửi khách xác nhận trước khi nhận                                                                                         |
| Giả thuyết về AI (nếu có)                 | AI đọc đoạn mô tả của khách, gợi ý các hạng mục và câu hỏi làm rõ còn thiếu; tôi quyết định chốt scope                                                                                                                            |
| Cảm nhận nhanh                            | No AI                                                                                                                                                                                                                             |


Quy trình nháp hiện tại:

```text
HIỆN TẠI — scope không chốt rõ → job đội thời gian

[1 Nghe khách mô tả (mơ hồ)] → [2 Hỏi lại vài ý]
   → [★3 Ước lượng & chốt phạm vi: thiếu danh sách hạng mục] ← BOTTLENECK
   → [4 Báo giá & nhận] → [5 Khách thêm yêu cầu khi đang làm]
   → [6 Làm cả phần phát sinh → đội thời gian]
```

- Card số: **#1 — Lịch trống khi khách đặt đồ thuê**
- Vì sao: Pain lặp lại mỗi ngày, có người ngoài cùng chịu ảnh hưởng (khách), bottleneck rõ (dò lịch tay) và impact đo được (mất đơn, nhận trùng). Đây cũng là card dễ kiểm chứng với người thật ở CP4 (khách thuê) và dễ vẽ quy trình trước/sau ở CP5.
- Câu hỏi muốn nhóm phản biện: Với quy mô một shop nhỏ, chỉ cần sửa cách ghi lịch (Rule / bảng tra tay) là đủ, hay bottleneck thật nằm ở chỗ khác (ví dụ khâu trả lời khách, hay khâu cập nhật khi khách trả đồ)?

### AI đã phản biện card thế nào


Tôi hỏi AI theo 6 câu: actor có cụ thể không, quy trình có thật không, bottleneck có là một bước cụ thể không, metric có đo được không, sửa quy trình/Rule đã đủ chưa, có nhảy sang AI quá sớm không. Dưới đây là các điểm yếu AI chỉ ra cho card pitch (#1):

| Câu hỏi | Điểm yếu AI chỉ ra | Đồng ý? | Đã sửa gì |
| ------- | ------------------ | ------- | --------- |
| Metric có đo được không? | "Trả lời nhanh hơn" chung chung, không có baseline/target | Có | Đổi thành đo được: ~4 phút/lần → dưới 1 phút; số lần nhận trùng lịch → 0 |
| Bottleneck có là một bước cụ thể? | Việc mất đơn có thể do khâu khách trả đồ không cập nhật lịch, không chỉ do dò tay | Một phần | Giữ bottleneck chính ở bước dò tay, nhưng ghi thêm rủi ro "lịch không cập nhật khi trả đồ" vào Impact để kiểm chứng ở CP4 |
| Quy trình có thật không? | Chưa rõ đang ghi đơn bằng sổ tay hay file — ảnh hưởng tới thời gian dò | Có | Ghi rõ hiện ghi bằng sổ/ghi chú rời, dễ sót; đây chính là lý do bước 3 chậm |
| Sửa quy trình/Rule đã đủ chưa? Có nhảy sang AI sớm? | Một bảng lịch tra tay đã giải gần hết; giả thuyết "AI tự trả lời khách" là nhảy sớm | Có | Hạ "Cảm nhận nhanh" từ Workflow xuống **Rule**, ưu tiên thử phương án không dùng AI (bảng lịch) trước |


---

## 4. Tôi đã tham gia phần nào (CP3 → CP7)


| Hoạt động                  | Tôi đã làm gì?         | Kết quả / ảnh hưởng tới bài nhóm |
| -------------------------- | ---------------------- | -------------------------------- |
| Pitch Problem Card         |                        |                                  |
| Phản biện bài của bạn khác | Câu hỏi tôi đã đặt:    |                                  |
| Nhận phản biện             | Câu hỏi tôi nhận được: | Tôi đã sửa gì:                   |
| Gom cluster / cây OST      |                        |                                  |
| Chọn candidate problem     |                        |                                  |
| Kiểm chứng / research      |                        |                                  |
| Quy trình nhóm             |                        |                                  |
| Problem Statement          |                        |                                  |
| Mức can thiệp AI           |                        |                                  |
| Quyết định                 |                        |                                  |


---

## 5. Dùng AI


| Checkpoint                     | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai hoặc hời hợt ở đâu? | Tôi sửa gì bằng nhận định của mình? |
| ------------------------------ | ---------------------- | ----------------- | -------------------------- | ----------------------------------- |
| CP1 Scan                       |                        |                   |                            |                                     |
| CP2 Problem Card               |                        |                   |                            |                                     |
| CP4 Research                   |                        |                   |                            |                                     |
| CP5 Quy trình                  |                        |                   |                            |                                     |
| CP5–6 Problem Statement        |                        |                   |                            |                                     |
| CP6 Mức can thiệp / quyết định |                        |                   |                            |                                     |


---

## 6. Reflection (CP7)

Trả lời bằng trải nghiệm thật của bạn, tối thiểu 200 từ cho các câu 6.1–6.6 (không tính 6.7, câu này được chấm riêng ở tiêu chí C5). **Không dùng AI để viết thay.**

**6.1. Tôi học được gì khi nghe top 3 problems của các bạn khác?**

**6.2. Nhóm có lúc nào bị "solution-first" (nghĩ giải pháp trước khi hiểu vấn đề) không? Lúc đó nhóm nhận ra và xử lý thế nào?**

**6.3. Tôi có đổi ý sau khi bị phản biện không? Kể một lần cụ thể.**

**6.4. Kết quả kiểm chứng (phỏng vấn/survey/research) có làm tôi bất ngờ không? Điều gì?**

**6.5. Điều khó nhất khi viết Problem Statement là gì?**

**6.6. Nếu làm lại, tôi sẽ đổi gì? Tôi sẽ phản biện nhóm mạnh hơn ở điểm nào?**

**6.7. Hiểu bài:** giải thích bằng 5–8 câu, không nhìn tài liệu, chuỗi *problem → quy trình → metric → boundary → mức can thiệp AI → quyết định* của bài nhóm mình.

---

## 7. Tài liệu tham khảo

- 

