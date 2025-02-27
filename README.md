# Users Management API

這是一個使用 Flask 和 MySQL 建立的簡單使用者管理 API 系統。

## 系統需求

- Python 3.8+
- MySQL 5.7+
- pip (Python 套件管理器)

## 安裝步驟

1. 克隆專案：
```bash
git clone https://github.com/lucashsu95/flask-connect-mysql-demo
cd flask-connect-mysql-demo
```

2. 建立虛擬環境：
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. 安裝相依套件：
```bash
pip install -r requirements.txt
```

4. 設定 MySQL 資料庫：
```sql
CREATE DATABASE web01;
```
或是直接匯入`web01.sql`

5. 啟動應用程式：
```bash
python app.py
```

## API 端點

### 獲取所有使用者
- **URL**: users
- **Method**: `GET`
- **Response**: 200 OK
```json
[
    {
        "id": 1,
        "account": "user1",
        "password": "password1"
    }
]
```

### 新增使用者
- **URL**: users
- **Method**: `POST`
- **Body**:
```json
{
    "account": "user1",
    "password": "password1"
}
```
- **Response**: 201 Created

### 獲取特定使用者
- **URL**: `/users/<user_id>`
- **Method**: `GET`
- **Response**: 200 OK

### 更新使用者
- **URL**: `/users/<user_id>`
- **Method**: `PUT`
- **Body**:
```json
{
    "account": "updated_user",
    "password": "updated_password"
}
```
- **Response**: 200 OK

### 刪除使用者
- **URL**: `/users/<user_id>`
- **Method**: `DELETE`
- **Response**: 200 OK

## 錯誤處理

- 409: 帳號已存在
- 404: 使用者不存在
- 400: 請求格式錯誤

## 環境變數設定

資料庫連線設定在 app.py 中：

```python
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost:3306/web01'
```

請根據您的環境修改以下參數：
- 使用者名稱（root）
- 密碼（password）
- 主機位置（localhost）
- 端口（3306）
- 資料庫名稱（web01）