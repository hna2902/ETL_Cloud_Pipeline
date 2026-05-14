# E-Commerce Cloud ETL Pipeline

**Live Dashboard:** [Xem Báo cáo Looker Studio tại đây](Thay_link_Looker_Studio_của_bạn_vào_đây)

## Tổng quan dự án (Overview)
Dự án xây dựng một đường ống dữ liệu (End-to-End Data Pipeline) hoàn chỉnh từ khâu trích xuất, làm sạch đến lưu trữ trên nền tảng điện toán đám mây. Hệ thống xử lý tập dữ liệu hành vi người dùng thương mại điện tử khổng lồ để phục vụ trực quan hóa trên hệ thống Business Intelligence (BI)

## Kiến trúc hệ thống (Data Architecture)
* **Extract:** Đọc dữ liệu thô (Raw Data) từ định dạng CSV cục bộ.
* **Transform:** Sử dụng sức mạnh đa luồng của **Polars** để làm sạch dữ liệu, ép kiểu thời gian (datetime) và bóc tách chuỗi danh mục (category) một cách song song
* **Load:** Nén dữ liệu sang định dạng **Parquet** (Columnar storage) để tối ưu dung lượng/I/O, sau đó đẩy tự động lên **Google BigQuery** (Data Warehouse)
* **Serve:** Kết nối BigQuery với **Looker Studio** để xây dựng Dashboard phân tích tự động

## Công nghệ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python, SQL
* **Thư viện xử lý:** Polars, PyArrow
* **Cloud & Lưu trữ:** Google Cloud Platform (GCP), BigQuery, Parquet
* **BI / Trực quan hóa:** Google Looker Studio
* **Bảo mật:** Application Default Credentials (ADC) / gcloud CLI

## Thành tựu & Hiệu năng (Key Achievements)
* Xử lý thành công **42.38 triệu dòng dữ liệu (~5.6GB)** chỉ trong vòng **~67 giây** bằng Polars trên máy tính cá nhân
* Tối ưu hóa lưu trữ: Giảm đáng kể dung lượng file từ CSV sang Parquet, tăng tốc độ truy vấn trên Cloud
* Triển khai thành công luồng xác thực bảo mật chuẩn Doanh nghiệp (không lộ lọt secret key dưới dạng file JSON)

## Hướng dẫn cài đặt (Cấu trúc thư mục)
Dự án được bảo mật chặt chẽ bằng `.gitignore` để tránh rò rỉ dữ liệu lớn và thông tin xác thực
- `/src`: Chứa mã nguồn Python
- Chạy lệnh `gcloud auth application-default login` trước khi thực thi mã để cấp quyền truy cập BigQuery