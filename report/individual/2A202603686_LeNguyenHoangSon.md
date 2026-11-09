# Báo cáo cá nhân — 2A202603686_LeNguyenHoangSon

> Đổi tên file theo quy tắc `MSSV_HoTen.md`, ví dụ `20241234_NguyenVanAn.md` (MSSV trước, dấu `_`, họ tên viết liền không dấu). Sửa cả dòng tiêu đề phía trên cho khớp.
> Template chi tiết và prompt mẫu cho từng mục: [docs/01-worksheet.md](../../docs/01-worksheet.md).
> Mỗi thành viên một file trong `report/individual/` trên repo nhóm: copy template này thành file mới, điền, rồi commit bằng tài khoản GitHub của bạn. Không viết hộ người khác.

## 1. Thông tin học viên

- Họ tên: Lê Nguyễn Hoàng Sơn
- MSSV:2A202603686
- Email trường (không bắt buộc, repo có thể để public):26ai.sonlnh@vinuni.edu.vn
- Tên nhóm:TripleBlack
- Link repo nhóm: https://github.com/NamPham1012/-K5-L3A-DAY02-TripleBlack-DiscoveryProblemFraming

---
## 2. Scan problem (CP1)

Lăng kính: **Lặp lại** · **Tốn thời gian** · **Cần đọc, tổng hợp nhiều thông tin** · **Pain từ người khác**.

| # | Lăng kính | Job Story: Khi… tôi muốn… để… | Ai chịu ảnh hưởng? | Dấu hiệu thật (thời gian, tần suất, số người, bằng chứng) |
|---:|---|---|---|---|
| 1 |Lặp lại|Khi nhận dữ liệu từ camera và các cảm biến sau mỗi đợt thử nghiệm, tôi muốn kiểm tra chất lượng và định dạng dữ liệu, để đảm bảo dữ liệu đáp ứng định dạng đã được quy định chung để tránh gây xung đột |AI Engineer, Data Engineer|Mỗi đợt kiểm tra dữ liệu mất khoảng 30–45 phút |
| 2 |Lặp lại |Khi cập nhật mô hình nhận diện vật thể xung quanh, tôi muốn đánh giá mô hình mới trên bộ kiểm thử chuẩn để đánh giá chất lượng mô hình sau khi cập nhật |AI Engineer, ML Engineer|Mỗi tuần đánh giá 2–3 lần, khoảng 40 phút/lần.|
| 3 |Tốn thời gian|Khi xử lý đèn giao thông từ camera trên xe tự lái, tôi muốn xác định chính xác trạng thái đèn và thời gian còn lại của đèn trong các điều kiện ánh sáng,thời tiết, lưu lượng các phương tiện xung quanh khác nhau, để phương tiện có thể đưa ra quyết định di chuyển chính xác và an toàn.|Computer Vision, AI Engineer|Mất khoảng 7 giờ để thu nhập dữ liệu, kiểm tra dữ liệu, chạy mô hình, phân tích lỗi, điều chỉnh lại, kiểm thử lại|
| 4 |Tốn thời gian|Khi mô hình nhận diện sai phương tiện hoặc người đi bộ trong tình huống giao thông phức tạp, tôi muốn xác định nguyên nhân lỗi, để cải thiện độ tin cậy của mô hình. |AI Engineer, ML Engineer|Mất 1 ngày để sửa lỗi không nhận diện được người đi bộ qua đường gây nguy hiểm.|
| 5 |Cần đọc, tổng hợp nhiều thông tin|Khi lựa chọn phiên bản mô hình để tích hợp, tôi muốn so sánh độ chính xác, tốc độ xử lý và tài nguyên sử dụng của các phiên bản, để lựa chọn mô hình đáp ứng yêu cầu hệ thống.|Tech Lead, Tester, AI Engineer |Nhiều phiên bản cần so sánh với nhau, tìm ra phiên bản ổn định và an toàn nhất.|
| 6 |Pain từ người khác|Khi kiểm thử chức năng nhận diện đèn giao thông, tôi muốn biết rõ nguyên nhân các trường hợp nhận diện sai đèn giao thông để cải tiển hơn so với lần trước|AI Engineer, Tester|Lỗi xác định sai thời gian đèn xanh còn lại dẫn đến vượt đèn đỏ gây nguy hiểm.|
| 7 |Pain từ người khác|Khi kiểm thử chức năng phanh khẩn cấp khi gặp chướng ngại vật bất ngờ trên cao tốc khi xe đang ở tốc độ cao, tôi muốn biết thời gian tối đa phát hiện vật cản và dừng lại để cải tiến tốc độ nhận diện vật thể |AI Engineer, Tester|Xe phía trước bật đèn cảnh báo và giảm tốc độ nhưng xe tự lái không nhận diện được, người dân chạy qua đường cao tốc từ xa xe không phản ứng kịp yếu tố bất ngờ.|

**Nếu có dùng AI để gợi ý thêm:** ý nào AI gợi ý mà bạn giữ lại, ý nào bỏ và vì sao.

-Giữ lại ý 1 và loại bỏ ý Xây dựng Agent tự động điều khiển xe tự lái vì phạm vi quá rộng, tốn nhiều tài nguyên, độ an toàn thấp và nhiều rủi ro pháp lý khi xe gặp sự cố mà những người làm ra Agent và duyệt phải gánh chịu khi gặp sự cố nghiêm trọng

---

## 3. Top 3 Problem Cards + quy trình nháp (CP2)

### Bảng chọn top 3

| Rank | Problem | Vì sao chọn | Điều còn chưa chắc |
|---:|---|---|---|
 3 |Nhận diện tín hiệu đèn giao thông(#3)|Liên quan trực tiếp đến an toàn xe tự lái, có thể đo tỷ lệ nhận diện sai và phân tích các tình huống khó như thời tiết xấu, ánh sáng yếu.|Chưa xác định điều kiện nào gây lỗi nhiều nhất và thời gian xử lý mỗi lỗi.|
| 6 |Kiểm thử lỗi nhận diện đèn giao thông(#6)|Có tình huống kiểm thử cụ thể, ảnh hưởng đến AI Engineer và Tester; có thể xác định quy trình phát hiện, phân tích và kiểm thử lại lỗi.|Chưa xác định nguyên nhân lỗi chủ yếu và số lần phải kiểm thử lại.|
| 7 |Kiểm thử chức năng phanh khẩn cấp(#7)|Có tác động lớn đến an toàn phương tiện, có thể đánh giá thời gian phát hiện vật cản và phản ứng của hệ thống trong tình huống nguy hiểm.|Chưa có dữ liệu kiểm thử xác nhận nguyên nhân xe không phát hiện vật cản và các ngưỡng an toàn cần đạt.|


### Problem Card #1

| Trường | Nội dung |
|---|---|
| Job Story | Khi xử lý đèn giao thông từ camera trên xe tự lái, tôi muốn xác định chính xác trạng thái đèn và thời gian còn lại của đèn trong các điều kiện ánh sáng, thời tiết và lưu lượng phương tiện xung quanh khác nhau, để phương tiện có thể đưa ra quyết định di chuyển chính xác và an toàn.|
| Actor | Computer Vision Engineer, AI Engineer |
| Thời điểm / bối cảnh |Trong quá trình phát triển và kiểm thử chức năng nhận diện tín hiệu đèn giao thông, đặc biệt với các tình huống ánh sáng yếu, trời mưa hoặc đèn bị che khuất, phương tiện phía trước che khuất đèn giao thông.|
| Quy trình hiện tại (3–7 bước) |1. Thu thập dữ liệu camera → 2. Kiểm tra dữ liệu và nhãn → 3. Chạy mô hình nhận diện → 4. Đối chiếu với kết quả chuẩn → 5. Phân tích lỗi → 6. Điều chỉnh mô hình hoặc dữ liệu → 7. Kiểm thử lại.|
| Bottleneck (bước nào, mất bao nhiêu phút) | Bước 5: Phân tích những trường hợp nhận diện sai để xác định nguyên nhân từ dữ liệu, điều kiện môi trường hoặc mô hình. |
| Impact (nếu không giải thì sao) |Có thể làm tăng thời gian kiểm thử, số lần phải chạy lại mô hình và ảnh hưởng đến độ tin cậy của chức năng nhận diện.|
| Success metric (baseline → target) |Giảm thời gian trung bình phân tích một trường hợp lỗi, không tăng tỷ lệ bỏ sót lỗi nghiêm trọng.|
| Phương án không dùng AI |Sử dụng checklist kiểm tra hình ảnh, phân loại lỗi theo điều kiện môi trường và đối chiếu thủ công với nhãn chuẩn.|
| Giả thuyết về AI (nếu có) |Có thể hỗ trợ phân loại và tổng hợp những trường hợp nhận diện sai để kỹ sư xem xét. Chưa quyết định sử dụng. |
| Cảm nhận nhanh |Agent|

Quy trình nháp hiện tại:

```
1. Thu thập dữ liệu camera 10 phút -> 2. Kiểm tra dữ liệu và nhãn 20 phút -> 3. Chạy mô hình nhận diện 30 phút -> 4. Đối chiếu kết quả 10 phút -> 5. Phân tích nguyên nhân lỗi 3 giờ -> 6. Điều chỉnh mô hình hoặc dữ liệu 2 giờ -> 7. Kiểm thử lại 30 phút
Tổng thời gian: 190 phút (3 giờ 10 phút)
Bottleneck dự kiến: Bước 5 – Phân tích nguyên nhân lỗi (60 phút), do AI Engineer phải đối chiếu dữ liệu kiểm thử, hình ảnh và log hệ thống để xác định nguyên nhân nhận diện sai.
Tổng thời gian: 450 phút (7 giờ 30 phút)
Bottleneck: Bước 5 – Phân tích nguyên nhân lỗi (3 giờ), chiếm 40% tổng thời gian.
```

### Problem Card #2

| Trường | Nội dung |
|---|---|
| Job Story | Khi kiểm thử chức năng nhận diện đèn giao thông, tôi muốn biết rõ nguyên nhân các trường hợp nhận diện sai để cải tiến tốt hơn so với lần trước. |
| Actor |AI Engineer, Tester |
| Thời điểm / bối cảnh |Khi Tester phát hiện hệ thống nhận diện sai tín hiệu đèn và cần phối hợp với AI Engineer để tìm nguyên nhân, xác nhận hướng khắc phục và kiểm thử lại.|
| Quy trình hiện tại (3–7 bước) | 1. Chuẩn bị test case → 2. Chạy kiểm thử → 3. Ghi nhận lỗi → 4. Gửi thông tin cho AI Engineer → 5. Phân tích nguyên nhân → 6. Trao đổi kết quả và kiểm thử lại.|
| Bottleneck (bước nào, mất bao nhiêu phút) | Bước 4–5: Thông tin lỗi có thể chưa đầy đủ khiến Tester và AI Engineer phải trao đổi nhiều lần để xác định nguyên nhân. Cần đo xem bước nào thực sự gây nghẽn.|
| Impact (nếu không giải thì sao) |Có thể kéo dài thời gian xử lý lỗi, trì hoãn kiểm thử lại và tăng khối lượng trao đổi giữa các bộ phận. |
| Success metric (baseline → target) |Giảm tỷ lệ lỗi nhận diện đèn giao thông tái diễn từ 20% xuống 5% sau khi khắc phục.|
| Phương án không dùng AI |Chuẩn hóa mẫu báo cáo lỗi bao gồm ảnh/video, thời điểm, điều kiện kiểm thử, trạng thái đèn thực tế, kết quả nhận diện|
| Giả thuyết về AI (nếu có) | Hỗ trợ tổng hợp thông tin lỗi từ test case và log thành báo cáo để kỹ sư kiểm tra. |
| Cảm nhận nhanh | Chưa biết|

Quy trình nháp hiện tại:

```
1. Chuẩn bị test case 15 phút -> 2. Chạy kiểm thử 60 phút -> 3. Ghi nhận trường hợp lỗi 20 phút -> 4. Chuyển thông tin lỗi 5 phút -> 5. Phân tích nguyên nhân  60 phút - BOTTLENECK dự kiến -> 6. Trao đổi kết quả và kiểm thử lại 30 phút .
```

### Problem Card #3

| Trường | Nội dung |
|---|---|
| Job Story | Khi kiểm thử chức năng nhận diện đèn giao thông, tôi muốn xác định rõ nguyên nhân của các trường hợp nhận diện sai, để khắc phục lỗi và cải thiện độ chính xác của hệ thống trong những lần kiểm thử tiếp theo.|
| Actor |AI Engineer, Tester|
| Thời điểm / bối cảnh |Khi Tester phát hiện hệ thống nhận diện sai tín hiệu đèn giao thông và cần phối hợp với AI Engineer để phân tích nguyên nhân, xác nhận hướng khắc phục và kiểm thử lại. |
| Quy trình hiện tại (3–7 bước) |. Chuẩn bị kịch bản → 2. Thiết lập môi trường mô phỏng → 3. Chạy kiểm thử → 4. Thu thập log → 5. Phân tích thời gian phản ứng → 6. Tổng hợp kết quả và kiểm thử lại. |
| Bottleneck (bước nào, mất bao nhiêu phút) | 	Bước 5: Đối chiếu dữ liệu cảm biến, thời điểm phát hiện vật cản, thời điểm phát lệnh phanh và phản hồi hệ thống để xác định nguyên nhân phản ứng không đạt yêu cầu.|
| Impact (nếu không giải thì sao) |	Có thể kéo dài quá trình xác định lỗi, khiến nhóm khó phân biệt vấn đề của mô hình nhận diện với vấn đề thuộc các bộ phận điều khiển khác. |
| Success metric (baseline → target) | Giảm thời gian phân tích mỗi tình huống kiểm thử từ 60 phút xuống 40 phút, đo bằng log công việc. Các chỉ số phản ứng và an toàn phải đạt tiêu chí kiểm thử đã được phê duyệt.|
| Phương án không dùng AI | Phân tích cốt lõi tốc độ mô hình phản ứng và nâng cấp mô hình |
| Giả thuyết về AI (nếu có) | Hỗ trợ tổng hợp log và làm nổi bật các sự kiện bất thường để kỹ sư phân tích; không đưa ra quyết định phanh thực tế.|
| Cảm nhận nhanh | Rule hoặc Workflow|

Quy trình nháp hiện tại:

```
1. Chuẩn bị test case - 15 phút -> 2. Chạy kiểm thử - 20 phút -> 3. Ghi nhận lỗi - 10 phút -> 4. Chuyển thông tin lỗi - 5phút -> 5. Phân tích nguyên nhân - 60phút -> 6. Trao đổi kết quả và kiểm thử lại - 30 phút
Tổng thời gian ước tính: 140 phút/lần xử lý lỗi.
Bottleneck dự kiến: Bước 5 – Phân tích nguyên nhân, chiếm khoảng 43% tổng thời gian.
```

### Card muốn pitch nhất

- Card số: 3
- Vì sao: 	Đây là vấn đề liên quan trực tiếp đến an toàn của hệ thống xe tự lái.
- Câu hỏi muốn nhóm phản biện: Phạm vi này vượt một buổi lab, có thu hẹp được không?

### AI đã phản biện card thế nào

| Điểm yếu AI chỉ ra | Đồng ý? | Đã sửa gì |
|---|---|---|
| Phạm vi vấn đề quá rộng, liên quan đến cảm biến, nhận diện vật cản và điều khiển phanh.| Cần xác nhận| Đề xuất thu hẹp vào phân tích kết quả kiểm thử và nguyên nhân phản ứng chậm.|
| Chưa chứng minh được rằng cần sử dụng AI để giải quyết vấn đề.|Cần xác nhận | Đề xuất so sánh phương án dùng checklist và công cụ phân tích log với phương án có AI hỗ trợ.|

---

## 4. Tôi đã tham gia phần nào (CP3 → CP7)

| Hoạt động | Tôi đã làm gì? | Kết quả / ảnh hưởng tới bài nhóm |
|---|---|---|
| Pitch Problem Card | | |
| Phản biện bài của bạn khác | Câu hỏi tôi đã đặt: | |
| Nhận phản biện | Câu hỏi tôi nhận được: | Tôi đã sửa gì: |
| Gom cluster / cây OST | | |
| Chọn candidate problem | | |
| Kiểm chứng / research | | |
| Quy trình nhóm | | |
| Problem Statement | | |
| Mức can thiệp AI | | |
| Quyết định | | |

---

## 5. Dùng AI

| Checkpoint | Tôi dùng AI để làm gì? | AI hữu ích ở đâu? | AI sai hoặc hời hợt ở đâu? | Tôi sửa gì bằng nhận định của mình? |
|---|---|---|---|---|
| CP1 Scan | | | | |
| CP2 Problem Card | | | | |
| CP4 Research | | | | |
| CP5 Quy trình | | | | |
| CP5–6 Problem Statement | | | | |
| CP6 Mức can thiệp / quyết định | | | | |

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
