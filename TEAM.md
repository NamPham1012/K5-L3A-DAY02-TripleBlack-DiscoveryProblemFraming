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
| CP6 — Quyết định                           | Linh        | Nam,Sơn      | 4 rủi ro + Go/Not Yet/No-Go                    |




### PHẠM VĂN NAM - 2A202603681

**Phần việc phụ trách:**

- Leader, điều phối thời gian nhóm.
- Người chính CP3 (hội tụ nhóm) và CP5 Problem Statement v0; chính CP6 mức can thiệp + Problem Statement v1.
- Viết Problem Statement (v0 → v1), hỗ trợ vẽ quy trình và chấm quyết định.

**Đóng góp cụ thể** (mình đã làm gì, ra sản phẩm gì):

- CP3: gom 9 candidate thành 4 cluster, dựng cây OST (1 outcome + 3 opportunity), dẫn chấm điểm 7 tiêu chí và chốt candidate "gom & đối soát dữ liệu đa nguồn".
- CP5–CP6: viết Problem Statement v0 và v1 (metric có baseline→target→cách đo, boundary + HITL); lập luận chọn mức Workflow và vì sao không chọn Rule/Agent; điền AI Canvas và 2 câu PAIR.
- CP6: cùng nhóm chấm 4 rủi ro và đề xuất ngưỡng dừng đo được.

**Bằng chứng** (phần nào trong `group_report.md`, file nào trong `report/assets/`, commit nào):

- `group_report.md` Mục 2 (toàn bộ CP3), Mục 5 (Problem Statement v0), Mục 6–8 (mức can thiệp, v1, quyết định).
- Báo cáo cá nhân `report/individual/2A202603681_PHAMVANNAM.md` (CP1–CP2, Mục 4–6).
- Commit của tài khoản NamPham: `0ab20f1` (cp01 & cp2), `c980eac` / `89fcf13` (cp3), `a1b5372` (cp5 Problem Statement v0 & CP6 mức can thiệp + v1), `f3103dc` (báo cáo cá nhân CP3→7 & Mục 5 Dùng AI).

**Điều mình học được từ phần nhóm:**

- Vấn đề mạnh nhất của nhóm không phải vấn đề của riêng mình: tôi đã bỏ card lịch shop của mình để chọn vấn đề của Sơn vì nó đo được và kiểm chứng được với người thật.
- Phân biệt opportunity (pain) với solution khi dựng cây OST, và viết Success Metric buộc phải có baseline, target, cách đo thay vì nói "nhanh hơn".