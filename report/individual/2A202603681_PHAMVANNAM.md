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
| 5   | Cần đọc, tổng hợp nhiều thông tin | Khi gặp một bug trong đồ án, tôi muốn nhớ lại mình đã thử cách nào rồi, để không sửa lại vòng vo                                                                         | Tôi                  | 3-4 bug/tuần; mỗi bug mất \~20 phút chỉ để dò lại prompt đã đã thử để sửa                                                                                                                                                                                            |
| 6   | Cần đọc, tổng hợp nhiều thông tin | Khi nhận một job freelance mới, tôi muốn ước lượng có đủ thời gian xen với đồ án và shop không, để quyết nhận hay từ chối                                                | Tôi, khách freelance | Tháng trước 1 job vì không khóa scope nên kéo dài hơn tháng, rất mất thời gian                                                                                                                                                                                       |
| 7   | Pain từ người khác                | Khi khách muốn đặt trước một bộ đồ, họ muốn biết ngay bộ đó còn trống ngày họ cần không, để chốt đơn                                                                     | Khách thuê, tôi      | Khách hỏi "Bộ này còn trống không?" tôi phải dò lại danh sách rất mất thời gian                                                                                                                                                                                      |
| 8   | Pain từ người khác                | Khi cộng tác viên freelance nhận task code từ tôi, họ muốn biết ngay tài liệu, code liên quan nằm ở đâu và cần làm đến mức nào, để bắt tay vào làm mà không phải hỏi lại | Cộng tác viên, tôi   | Mỗi lần giao task, CTV hỏi lại 2-3 lượt: “Tài liệu API xem ở đâu?”, “Code từ nhánh nào?”, “File `.env` lấy ở đâu?”, “Sửa ở file nào?”. Mỗi lượt chờ tôi trả lời mất nửa ngày, nên task trễ 1-2 ngày. Có lần CTV đoán sai, code trên nhánh cũ, phải merge lại từ đầu. |


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


| Câu hỏi                                             | Điểm yếu AI chỉ ra                                                                  | Đồng ý?  | Đã sửa gì                                                                                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| Metric có đo được không?                            | "Trả lời nhanh hơn" chung chung, không có baseline/target                           | Có       | Đổi thành đo được: \~4 phút/lần → dưới 1 phút; số lần nhận trùng lịch → 0                                                 |
| Bottleneck có là một bước cụ thể?                   | Việc mất đơn có thể do khâu khách trả đồ không cập nhật lịch, không chỉ do dò tay   | Một phần | Giữ bottleneck chính ở bước dò tay, nhưng ghi thêm rủi ro "lịch không cập nhật khi trả đồ" vào Impact để kiểm chứng ở CP4 |
| Quy trình có thật không?                            | Chưa rõ đang ghi đơn bằng sổ tay hay file — ảnh hưởng tới thời gian dò              | Có       | Ghi rõ hiện ghi bằng sổ/ghi chú rời, dễ sót; đây chính là lý do bước 3 chậm                                               |
| Sửa quy trình/Rule đã đủ chưa? Có nhảy sang AI sớm? | Một bảng lịch tra tay đã giải gần hết; giả thuyết "AI tự trả lời khách" là nhảy sớm | Có       | Hạ "Cảm nhận nhanh" từ Workflow xuống **Rule**, ưu tiên thử phương án không dùng AI (bảng lịch) trước                     |


---

## 4. Tôi đã tham gia phần nào (CP3 → CP7)


| Hoạt động                  | Tôi đã làm gì?                                                                                                                                                                                              | Kết quả / ảnh hưởng tới bài nhóm                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pitch Problem Card         | Pitch 3 card của mình: lịch trống shop thuê đồ, đồng bộ tài liệu đồ án↔code, khóa scope job freelance; chọn card lịch shop để pitch chính                                                                   | Nhóm có thêm góc "tra cứu/lịch" khi gom cluster                                                                                                        |
| Phản biện bài của bạn khác | Câu hỏi tôi đã đặt: với Sơn — "Chênh lệch doanh thu là do phí/hoàn tiền hay do gom sai số liệu?"; với Linh — "Nhóm là SV, có kiểm chứng được với kế toán thật không?"                                       | Giúp nhóm thấy #4 (nhập liệu) khó phỏng vấn đúng người, và #7–#8 của Sơn mới là pain đo được rõ                                                        |
| Nhận phản biện             | Câu hỏi tôi nhận được: "Lịch trống shop chỉ mình bạn gặp hay nhiều người gặp?" (Linh)                                                                                                                       | Tôi đã sửa gì: đồng ý lịch shop phạm vi hẹp một người; bỏ ý đưa nó thành candidate chính, chuyển sang ủng hộ cluster dữ liệu đa nguồn mà cả 3 cùng gặp |
| Gom cluster / cây OST      | Là người chính CP3: gom 9 candidate thành 4 cluster (A gom/đối soát dữ liệu, B yêu cầu mơ hồ, C tổng hợp thông tin, D tra cứu/giao hàng); dựng cây OST 1 outcome + 3 opportunity, gạch các solution đội lốt | Ra được cây OST và bảng cluster ở Mục 2 group\_report                                                                                                  |
| Chọn candidate problem     | Dẫn dắt chấm điểm 7 tiêu chí cho shortlist; chốt cluster A (gom &amp; đối soát dữ liệu đa nguồn) vì phủ cả 3 người và kiểm chứng được                                                                       | Nhóm chốt candidate problem chính thức cho CP4→CP6                                                                                                     |
| Kiểm chứng / research      | Hỗ trợ Linh/Sơn: soạn cùng bộ câu hỏi phỏng vấn theo Mom Test, nhắc tránh câu "Bạn có muốn…"; cùng rà 3 link research cho mở được                                                                           | Phỏng vấn ra số thật, nhóm chỉnh lại baseline thời gian và thu hẹp actor về "người bán ≥2 sàn"                                                         |
| Quy trình nhóm             | Cùng Sơn vẽ quy trình hiện tại/tương lai; đề xuất thêm bước con người duyệt (HITL) và phương án quay về khi AI sai                                                                                          | Quy trình tương lai có boundary + phương án quay về ở Mục 4 group\_report                                                                              |
| Problem Statement          | Người chính viết Problem Statement v0 và v1; nhờ AI chỉ lỗ hổng rồi tự chốt                                                                                                                                 | Ra Problem Statement v0 (Mục 5) và v1 (Mục 7); metric có baseline→target→cách đo                                                                       |
| Mức can thiệp AI           | Dẫn so sánh 4 mức, lập luận chọn Workflow và vì sao không chọn Rule/Agent; điền AI Canvas + 2 câu PAIR                                                                                                      | Mục 6 group\_report: chốt mức Workflow có lý do                                                                                                        |
| Quyết định                 | Cùng Linh chấm 4 rủi ro và đề xuất ngưỡng dừng đo được                                                                                                                                                      | Quyết định "Go, phạm vi nhỏ" + ngưỡng dừng ở Mục 8                                                                                                     |


---

## 5. Dùng AI


| Checkpoint                     | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai hoặc hời hợt ở đâu? | Tôi sửa gì bằng nhận định của mình? |
| ------------------------------ | ---------------------- | ----------------- | -------------------------- | ----------------------------------- |
| CP1 Scan                       | Sau khi tự scan trước, hỏi AI gợi ý thêm góc nhìn cho các lăng kính | Gợi được vài hướng tôi chưa nghĩ tới (theo vết khi fix bug, ước lượng thời gian job) | Gợi ý chung chung, thiếu dấu hiệu thật; có ý là giải pháp trá hình ("làm app quản lý") | Tự viết lại theo trải nghiệm thật, thêm số đo; loại các ý là solution |
| CP2 Problem Card               | Cho AI đóng vai "PM hoài nghi" phản biện card theo 6 câu (actor, quy trình, bottleneck, metric, Rule đủ chưa, nhảy AI sớm) | Chỉ ra metric "nhanh hơn" không đo được, và việc nhảy sang AI quá sớm | Có chỗ phán đoán bottleneck hộ tôi chưa đúng bối cảnh | Sửa metric thành baseline→target đo được; hạ cảm nhận từ Workflow xuống Rule |
| CP4 Research                   | Nhờ AI gợi ý từ khoá và một số công cụ gom/đối soát đa sàn để tự đi tìm | Rút ngắn thời gian tìm, biết tên vài công cụ (Sapo, Pancake) | Có link/thông tin AI đưa không chính xác hoặc đã cũ | Tự mở từng link kiểm lại, bỏ nguồn không mở được; không dùng AI để phỏng vấn người thật |
| CP5 Quy trình                  | Nhờ AI chuyển mô tả các bước thành sơ đồ và phản biện quy trình tương lai | Giúp sắp xếp sơ đồ gọn, nhắc chỗ cần bước con người kiểm tra | Bỏ qua "phương án quay về" khi AI sai nếu tôi không hỏi | Tự thêm boundary + phương án quay về; kiểm lại số phút từng bước theo thực tế |
| CP5–6 Problem Statement        | Nhờ AI chỉ lỗ hổng của Problem Statement v0 (chỉ hỏi lỗ hổng, không để viết lại thay) | Chỉ ra baseline metric chưa rõ cách đo, actor còn rộng | Có đề xuất mở rộng phạm vi làm bài phình ra | Giữ phạm vi hẹp (đối soát tuần); bổ sung cách đo đối chiếu chéo; thu hẹp actor về người bán ≥2 sàn |
| CP6 Mức can thiệp / quyết định | Dùng AI phản biện lựa chọn mức và cách chấm 4 rủi ro | Nhắc tự hỏi "Workflow đã đủ chưa" trước khi chọn Agent | Thiên về gợi mức cao cho "ấn tượng" | Giữ mức Workflow, lập luận vì sao không cần Agent; tự đặt ngưỡng dừng đo được |


---

## 6. Reflection (CP7)

**6.1. Tôi học được gì khi nghe top 3 problems của các bạn khác?**

Khi nghe Linh và Sơn pitch, tôi nhận ra ba đứa sống trong ba thế giới rất khác nhau: tôi thì loay hoay với shop cho thuê đồ và đồ án, Linh thì quen các việc văn phòng như nhập liệu và họp hành, còn Sơn bán sữa online trên nhiều sàn. Điều làm tôi bất ngờ là dù khác domain, có những pattern lặp lại ở cả ba: đều có khâu "gom và xử lý dữ liệu rải rác" và khâu "làm lại vì hiểu sai". Tôi học được rằng một vấn đề mạnh không phải là vấn đề của riêng mình, mà là cái nhiều người cùng gặp và đo được. Ban đầu tôi khá tự tin card lịch shop của mình sẽ được chọn, nhưng nghe xong mới thấy nó hẹp vì chỉ mình tôi gặp. Nhìn vấn đề của Sơn, tôi thấy nó vừa đo được bằng thời gian, vừa có người thật để phỏng vấn ngay. Bài học lớn nhất với tôi là phải tạm bỏ "cái tôi" với vấn đề của mình, nhìn vào tiêu chí khách quan để chọn cái tốt nhất cho cả nhóm.

**6.2. Nhóm có lúc nào bị "solution-first" (nghĩ giải pháp trước khi hiểu vấn đề) không? Lúc đó nhóm nhận ra và xử lý thế nào?**

Có, và khá sớm. Ngay khi chốt hướng của Sơn, cả nhóm lập tức nhảy sang bàn "làm một công cụ tự gom số liệu các sàn" và thậm chí nói tới việc để AI tự đối soát. Lúc gom cây OST, tôi phát hiện mình đang viết "app quản lý bán hàng" vào nhánh opportunity — mà đó là giải pháp, không phải pain. Chúng tôi dừng lại, gạch các ý gọi tên công cụ, và viết lại nhánh theo đúng nỗi đau: "dữ liệu rải rác nhiều định dạng nên phải gom tay và dễ sai". Sau đó khi vẽ quy trình, nhóm cũng suýt gán mức Agent cho đẹp, nhưng khi tự hỏi "Workflow đã đủ chưa" thì thấy quy trình vốn đã cố định, không cần AI tự quyết bước. Cách nhóm xử lý là luôn quay lại hỏi "bottleneck thật nằm ở bước nào" trước khi nói tới AI.

**6.3. Tôi có đổi ý sau khi bị phản biện không? Kể một lần cụ thể.**

Có. Tôi vào buổi hội tụ với ý định pitch mạnh cho card "lịch trống shop cho thuê đồ" của mình và muốn nó thành vấn đề chính của nhóm. Linh phản biện một câu làm tôi khựng lại: "Pain này chỉ mình bạn gặp hay nhiều người gặp?". Tôi thừa nhận là gần như chỉ mình tôi, và nếu phỏng vấn thì cũng chỉ phỏng vấn được chính mình. Lúc đầu tôi hơi tiếc vì đã chuẩn bị kỹ card đó, nhưng khi đặt lên bàn chấm điểm 7 tiêu chí thì rõ ràng vấn đề của Sơn thắng ở "pain có bằng chứng" và "kiểm chứng được với người thật". Tôi đổi ý, chủ động bỏ ý đưa lịch shop làm candidate chính và chuyển sang ủng hộ cluster dữ liệu đa nguồn. Nhờ vậy nhóm hội tụ nhanh hơn.

**6.4. Kết quả kiểm chứng (phỏng vấn/survey/research) có làm tôi bất ngờ không? Điều gì?**

Có hai điều. Thứ nhất, khi research tôi tưởng đây là bài chưa ai giải, nhưng hoá ra đã có công cụ như Sapo hay Pancake POS gom đơn đa sàn khá tốt. Điều này suýt làm tôi nghĩ "thôi khỏi làm". Nhưng khi đọc kỹ thì thấy chúng mạnh ở khâu "gom", còn khâu "đối soát chênh lệch phí/hoàn tiền" — đúng bottleneck của Sơn — thì vẫn bỏ trống hoặc tính phí cao. Thứ hai, khi nghe Sơn kể lần số liệu bị lệch thật, tôi bất ngờ vì hậu quả không chỉ là mất thời gian mà còn ghi sai doanh thu, dẫn tới đánh giá nhầm sản phẩm nào đang lãi. Điều đó làm tôi thấy "bỏ sót" nguy hiểm hơn "báo nhầm", và nó đổi cả cách nhóm thiết kế boundary.

**6.5. Điều khó nhất khi viết Problem Statement là gì?**

Khó nhất với tôi là viết Success Metric cho đo được. Lúc đầu tôi viết "giúp đối soát nhanh và chính xác hơn", nghe thì xuôi tai nhưng không đo được cái gì cả. Phải ngồi lại tách ra baseline (hiện mất khoảng 60 phút/tuần), target (xuống dưới 30 phút) và cách đo (tự bấm giờ ba tuần). Phần "số dòng chênh lệch bị bỏ sót" còn khó hơn vì baseline của nó không có sẵn — nhóm phải nghĩ ra cách đo bằng việc đối chiếu chéo bảng người kiểm với bảng đã chốt. Qua đó tôi hiểu một metric tốt buộc mình phải nói rõ đang đo cái gì, bằng con số nào, chứ không được trốn sau những từ như "nhanh hơn", "tiện hơn".

**6.6. Nếu làm lại, tôi sẽ đổi gì? Tôi sẽ phản biện nhóm mạnh hơn ở điểm nào?**

Nếu làm lại, tôi sẽ đi phỏng vấn người thật sớm hơn, ngay sau khi có shortlist, thay vì gần như chốt vấn đề xong mới kiểm chứng — làm vậy số liệu baseline sẽ chắc hơn. Tôi cũng sẽ ép nhóm phỏng vấn thêm ít nhất một người bán ngoài Sơn để tránh phụ thuộc vào một nguồn duy nhất. Về phản biện, tôi thấy mình còn dễ dãi ở chỗ chấp nhận ngay con số thời gian của một mình Sơn làm baseline; lần sau tôi sẽ phản biện mạnh hơn vào tính đại diện của số liệu, hỏi "con số này đúng với bao nhiêu người", trước khi để nó vào Problem Statement.

**6.7. Hiểu bài:** giải thích bằng 5–8 câu, không nhìn tài liệu, chuỗi *problem → quy trình → metric → boundary → mức can thiệp AI → quyết định* của bài nhóm mình.

Problem của nhóm tôi là người bán online trên nhiều sàn phải gom và đối soát số liệu giao dịch rải rác để ra doanh thu đúng, tốn thời gian và dễ sai. Quy trình hiện tại gồm tải báo cáo từng sàn, chuẩn hoá, gộp vào một bảng, rồi đối chiếu phí và hoàn tiền để tìm chênh lệch — bottleneck nằm ở bước đối chiếu, khoảng 20 phút mỗi lần. Metric là giảm thời gian đối soát từ 60 xuống dưới 30 phút một tuần và giảm ít nhất một nửa số dòng chênh lệch bị bỏ sót, đo bằng bấm giờ và đối chiếu chéo. Boundary là AI chỉ gợi ý dòng nghi ngờ chứ không tự sửa số hay tự chốt doanh thu, và người bán bắt buộc duyệt lại trước khi chốt, có phương án quay về đối chiếu tay. Về mức can thiệp, nhóm chọn Workflow vì quy trình đã cố định nhưng dữ liệu đa định dạng cần AI làm một phần; không cần Agent vì không phải để AI tự quyết bước. Quyết định cuối là Go phạm vi nhỏ, chạy thử ba tuần với một người bán, và ngưỡng dừng là nếu thời gian không giảm xuống dưới 45 phút hoặc AI bỏ sót trên 10% dòng chênh lệch thì quay về cách làm bằng Excel.

---

## 7. Tài liệu tham khảo

**Framework (theo docs/[03-international-frameworks.md](http://03-international-frameworks.md)):**

- Job Story (Jobs-to-be-Done) — Intercom / Alan Klement: [https://www.intercom.com/blog/accidentally-invented-job-stories/](https://www.intercom.com/blog/accidentally-invented-job-stories/)

- Opportunity Solution Tree — Teresa Torres: [https://www.producttalk.org/opportunity-solution-trees/](https://www.producttalk.org/opportunity-solution-trees/)

- The Mom Test — Rob Fitzpatrick: [https://www.momtestbook.com/](https://www.momtestbook.com/)

- Lean UX Problem Statement — Jeff Gothelf: [https://jeffgothelf.com/blog/business-problem-statement-opportunity-statement/](https://jeffgothelf.com/blog/business-problem-statement-opportunity-statement/)

- Google PAIR — User Needs + Defining Success: [https://pair.withgoogle.com/chapter/user-needs/](https://pair.withgoogle.com/chapter/user-needs/)

- Building Effective Agents — Anthropic (No AI/Rule/Workflow/Agent): [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

- AI Canvas — Prediction Machines (HBR): [https://hbr.org/2018/04/a-simple-tool-to-start-making-decisions-with-the-help-of-ai](https://hbr.org/2018/04/a-simple-tool-to-start-making-decisions-with-the-help-of-ai)

- Four Big Risks — Marty Cagan (SVPG): [https://www.svpg.com/four-big-risks/](https://www.svpg.com/four-big-risks/)

**Công cụ tham khảo khi research giải pháp đã có (CP4):**

- Sapo Omnichannel: [https://www.sapo.vn](https://www.sapo.vn)

- Pancake POS: [https://pos.pancake.vn](https://pos.pancake.vn)

- Shopee Seller Center: [https://seller.shopee.vn](https://seller.shopee.vn)

 

