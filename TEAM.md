# Team

> Điền file này trên repo chung do nhóm trưởng fork. Nhóm điền phần **Thông tin nhóm** và **Thành viên**. Mỗi người tự điền phần của mình trong **Cá nhân**. Không copy file này sang repo khác.

## Thông tin nhóm

- Tên nhóm: Triple Black
- Candidate problem nhóm chọn (1 câu): Người bán hàng online / người vừa học vừa kinh doanh nhỏ phải gom và đối soát dữ liệu giao dịch phân mảnh từ nhiều nguồn (nhiều sàn TMĐT, nhiều file/chứng từ) thành một báo cáo hoặc con số đúng, tốn thời gian và dễ sai.
- Quyết định cuối (Go / Not Yet / No-Go): *(điền sau khi xong CP6)*

## Thành viên


| STT | Họ và tên           | MSSV        | Vai trò trong nhóm                                | Tài khoản GitHub |
| ---: | ------------------- | ----------- | ------------------------------------------------- | ---------------- |
| 1   | Phạm Văn Nam        | 2A202603681 | Leader, điều phối, viết Problem Statement         | NamPham1012      |
| 2   | Lê Nguyễn Hoàng Sơn | 2A202603686 | Người phản biện chính, vẽ quy trình               | SonLNH19         |
| 3   | Vũ Gia Linh         | 2A202603677 | Phụ trách kiểm chứng (phỏng vấn/survey), research | vugialinh905-wq  |


Không ghi email hay số điện thoại vào bảng này, vì repo có thể để public.

Gợi ý vai trò (một người có thể giữ nhiều vai): điều phối thời gian, ghi chép, người phản biện chính, phụ trách kiểm chứng (phỏng vấn/survey), phụ trách research, vẽ quy trình, viết Problem Statement.

## Phân công theo checkpoint


| Checkpoint                                 | Người chính | Người hỗ trợ | Sản phẩm                                       |
| ------------------------------------------ | ----------- | ------------ | ---------------------------------------------- |
| CP3 — Hội tụ nhóm                          | Nam         | Linh, Sơn    | Cluster, cây OST, bảng chấm điểm               |
| CP4 — Kiểm chứng                           | Linh        | Sơn, Nam     | Assumption map, snapshot hoặc survey           |
| CP4 — Research                             | Sơn         | Linh,Sơn     | Bảng research có link                          |
| CP5 — Quy trình trước/sau                  | Sơn         | Nam,Linh     | Quy trình + bảng before/after                  |
| CP5 — Problem Statement v0                 | Nam         | Linh, Sơn    | Problem Statement v0                           |
| CP6 — Mức can thiệp + Problem Statement v1 | Nam         | Sơn,Linh     | Ma trận, AI Canvas, eval, Problem Statement v1 |
| CP6 — Quyết địn                            | Linh        | Nam,Sơn      | 4 rủi ro + Go/Not Yet/No-Go                    |




### PHẠM VĂN NAM - 2A202603681

**Phần việc phụ trách:**

- Leader, điều phối thời gian nhóm.
- Người chính CP3 (hội tụ nhóm) và CP5 Problem Statement v0; chính CP6 mức can thiệp + Problem Statement v1.
- Viết Problem Statement (v0 → v1), hỗ trợ vẽ quy trình và chấm quyết định.

**Đóng góp cụ thể** (mình đã làm gì, ra sản phẩm gì):

- CP3: gom 9 candidate thành 4 cluster, dựng cây OST (1 outcome + 3 opportunity), dẫn chấm điểm 7 tiêu chí và chốt candidate "gom &amp; đối soát dữ liệu đa nguồn".
- CP5–CP6: viết Problem Statement v0 và v1 (metric có baseline→target→cách đo, boundary + HITL); lập luận chọn mức Workflow và vì sao không chọn Rule/Agent; điền AI Canvas và 2 câu PAIR.
- CP6: cùng nhóm chấm 4 rủi ro và đề xuất ngưỡng dừng đo được.

**Bằng chứng** (phần nào trong `group_report.md`, file nào trong `report/assets/`, commit nào):

- `group_report.md` Mục 2 (toàn bộ CP3), Mục 5 (Problem Statement v0), Mục 6–8 (mức can thiệp, v1, quyết định).
- Báo cáo cá nhân `report/individual/2A202603681_PHAMVANNAM.md` (CP1–CP2, Mục 4–6).
- Commit của tài khoản NamPham: `0ab20f1` (cp01 &amp; cp2), `c980eac` / `89fcf13` (cp3), `a1b5372` (cp5 Problem Statement v0 &amp; CP6 mức can thiệp + v1), `f3103dc` (báo cáo cá nhân CP3→7 &amp; Mục 5 Dùng AI).

**Điều mình học được từ phần nhóm:**

- Vấn đề mạnh nhất của nhóm không phải vấn đề của riêng mình: tôi đã bỏ card lịch shop của mình để chọn vấn đề của Sơn vì nó đo được và kiểm chứng được với người thật.
- Phân biệt opportunity (pain) với solution khi dựng cây OST, và viết Success Metric buộc phải có baseline, target, cách đo thay vì nói "nhanh hơn".



### VŨ GIA LINH - 2A202603677

**Phần việc phụ trách:**

- Người chính CP4 (kiểm chứng) và CP6 (quyết định).
- Hỗ trợ CP4 research và CP5 quy trình.
- Phụ trách phỏng vấn/khảo sát người thật và tổng hợp tín hiệu.

**Đóng góp cụ thể** (mình đã làm gì, ra sản phẩm gì):

- CP4: lập Assumption Map, soạn bộ câu hỏi theo The Mom Test (hỏi hành vi đã xảy ra), phỏng vấn người bán online và ghi thành interview snapshot; tổng hợp tín hiệu xác nhận và phản bác.
- CP4: cùng Sơn rà bảng research, kiểm từng link mở được.
- CP6: chủ trì chấm 4 rủi ro (Value/Usability/Feasibility/Viability) và chốt quyết định Go/Not Yet/No-Go kèm ngưỡng dừng.

**Bằng chứng** (phần nào trong `group_report.md`, file nào trong `report/assets/`, commit nào):

- `group_report.md` Mục 3 (assumption map, interview snapshot, tổng hợp, research), Mục 8 (4 rủi ro + quyết định).
- Interview snapshot trong `report/assets/` (nếu có file: `cp4-interview-snapshot-N.md`).
- Báo cáo cá nhân `report/individual/2A202603677_VuGiaLinh.md`.
- Commit của tài khoản vugialinh905-wq (bổ sung mã commit cụ thể).

**Điều mình học được từ phần nhóm:**

- Phỏng vấn phải hỏi hành vi đã xảy ra, không hỏi "bạn có muốn…"; lời khen không phải bằng chứng, chỉ hành vi và con số mới là bằng chứng.
- # Một quyết định tốt cần soi đủ 4 rủi ro và phải có ngưỡng dừng đo được, thay vì chỉ nói "nên làm".

### LÊ NGUYỄN HOÀNG SƠN - 2A202603686

**Phần việc phụ trách:**

- Người phản biện chính của nhóm; phụ trách chính CP4 – Research và CP5 – Quy trình trước/sau.
- CP4 Research: tìm hiểu giải pháp đang có, lập bảng đối chiếu công cụ, nguồn tham khảo và rút ra khoảng trống của bài toán.
- CP5 Quy trình: mô tả các bước đối soát doanh thu hiện tại và phương án đề xuất, xác định bottleneck, lập bảng Before/After và ranh giới can thiệp AI.

**Đóng góp cụ thể** (mình đã làm gì, ra sản phẩm gì):

- **CP1–CP2 (cá nhân):** scan 6 vấn đề từ hoạt động bán sữa công thức nhập khẩu, chọn 3 Problem Cards gồm đối soát doanh thu tuần (#3), báo cáo kinh doanh tháng (#4) và phản ánh lon sữa bị móp (#6); xây dựng quy trình nháp và đề xuất pitch Card #2 về báo cáo tháng.
- **CP4 – Research:** chuẩn bị bảng so sánh **Sapo Omnichannel, Pancake POS, Google Sheets + Shopee Seller Center** theo các tiêu chí: giải quyết bước nào, điểm mạnh, khoảng trống/rủi ro và bài học cho nhóm. Rút ra hướng nghiên cứu: không làm lại tính năng gom đơn đã có mà tập trung kiểm tra những chênh lệch giữa doanh thu, phí sàn, hoàn tiền và đơn trả.
- **CP5 – Quy trình trước/sau:** xây dựng bản nháp quy trình đối soát đa nguồn gồm 6 bước, bảng **Actor – Input – Output – Thời gian** và bảng so sánh Before/After. Xác định bước đối chiếu phí sàn/hoàn tiền/đơn trả là bottleneck dự kiến (~20 phút/lần); đề xuất dùng Rule cho chuẩn hóa/ghép dữ liệu, AI hỗ trợ gợi ý giao dịch nghi ngờ và **người bán kiểm duyệt (HITL)** trước khi chốt doanh thu.

**Bằng chứng** (phần nào trong `group_[report.md](http://report.md)`, file nào trong `report/assets/`, commit nào):

- `group_[report.md](http://report.md)`: **Mục 3.3** (Research giải pháp đã có) và **Mục 4.1–4.3** (quy trình hiện tại, quy trình tương lai, bảng Before/After), sau khi nhóm đưa nội dung vào báo cáo chung.
- Báo cáo cá nhân: `report/individual/2A202603686_LeNguyenHoangSon.md`(CP1–CP2).
- **Commit của tài khoản** `SonLNH19`**:** `32af6b9` (cp1 & cp2), `30d9eb1` (cp4 & cp5 Hoàng Sơn), `0cc59c5` / `711fb89` (cập nhật báo cáo cá nhân), `f3f8047` (hoàn thiện phần của Sơn).

**Điều mình học được từ phần nhóm**:

- Phân biệt việc gom dữ liệu với việc đối soát chênh lệch: có công cụ hỗ trợ quản lý đa kênh không có nghĩa là mọi khoản phí, hoàn tiền và tiền thực nhận đều được kiểm tra chính xác.
- Khi thiết kế quy trình Trước/Sau,  metric cần có baseline, target, cách đo; AI chỉ nên hỗ trợ phần phù hợp, còn người bán phải kiểm tra và chịu trách nhiệm chốt số liệu cuối cùng.



&nbsp;