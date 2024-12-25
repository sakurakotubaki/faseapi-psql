# FastAPI Authentication System

FastAPIとPostgreSQLを使用した認証システムです。

## 技術スタック

- Python 3.12
- FastAPI
- PostgreSQL 16
- Docker & Docker Compose

## プロジェクト構造

```
faseapi-psql/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   ├── core/
│   ├── api/
│   ├── models/
│   ├── schemas/
│   └── services/
└── migrations/
    └── init.sql
```

## セットアップと実行

### 前提条件

- Docker
- Docker Compose

### 環境構築

1. リポジトリのクローン
```bash
git clone <repository-url>
cd faseapi-psql
```

2. 環境変数の設定（必要な場合）
```bash
cp .env.example .env
```

### Docker操作コマンド

1. コンテナのビルドと起動
```bash
docker-compose up -d --build
```

2. コンテナの状態確認
```bash
docker-compose ps
```

3. アプリケーションログの確認
```bash
docker-compose logs -f
```

4. コンテナの停止
```bash
docker-compose stop
```

5. コンテナとボリュームの削除
```bash
docker-compose down -v
```

### PostgreSQL操作コマンド

1. PostgreSQLコンテナに接続
```bash
docker-compose exec db psql -U wakuwaku -d auth_db
```

2. よく使うPostgreSQLコマンド
```sql
-- データベース一覧表示
\l

-- テーブル一覧表示
\dt

-- テーブルの構造確認
\d users

-- ユーザー一覧表示
SELECT * FROM users;

-- 特定のユーザーを検索
SELECT * FROM users WHERE email = 'tanaka@example.com';

-- 最近登録したユーザーを表示（最新5件）
SELECT id, name, email, created_at 
FROM users 
ORDER BY created_at DESC 
LIMIT 5;

-- ユーザーの総数を表示
SELECT COUNT(*) as total_users FROM users;

-- 特定の日付以降に登録したユーザーを表示
SELECT * FROM users 
WHERE created_at >= '2024-01-01';

-- ユーザー名で部分一致検索
SELECT * FROM users 
WHERE name LIKE '%田中%';

-- メールドメインでユーザーを検索
SELECT * FROM users 
WHERE email LIKE '%@example.com';

-- 登録日ごとのユーザー数を集計
SELECT 
    DATE(created_at) as registration_date,
    COUNT(*) as user_count
FROM users 
GROUP BY DATE(created_at)
ORDER BY registration_date DESC;

-- PostgreSQLシェルを終了
\q
```

3. データベースのバックアップ
```bash
docker-compose exec db pg_dump -U wakuwaku auth_db > backup.sql
```

4. バックアップの復元
```bash
docker-compose exec -T db psql -U wakuwaku -d auth_db < backup.sql
```

5. データベース管理用のSQLコマンド
```sql
-- 新しいユーザーを追加
INSERT INTO users (name, email, hashed_password) 
VALUES ('新規ユーザー', 'new@example.com', 'hashedpassword');

-- ユーザー情報を更新
UPDATE users 
SET name = '新しい名前', 
    updated_at = CURRENT_TIMESTAMP 
WHERE email = 'user@example.com';

-- ユーザーを削除
DELETE FROM users 
WHERE email = 'delete@example.com';

-- テーブルのインデックスを確認
\di users

-- テーブルの権限を確認
\dp users

-- データベースのサイズを確認
SELECT pg_size_pretty(pg_database_size('auth_db'));

-- テーブルのサイズを確認
SELECT pg_size_pretty(pg_total_relation_size('users'));
```

### APIエンドポイント

ベースURL: `http://localhost:8000`

#### 認証エンドポイント

1. ユーザー登録
```bash
curl -X POST http://localhost:8000/api/v1/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "name": "Test User",
    "password": "password123"
  }'
```

2. ログイン
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

### データベース情報

- データベース名: auth_db
- ユーザー名: wakuwaku
- パスワード: 1234qq
- ポート: 5432
- タイムゾーン: Asia/Tokyo

### 初期データ

システムには以下の2つのテストユーザーが初期データとして登録されています：

1. 田中太郎
   - Email: tanaka@example.com
   - Password: password123

2. 山田花子
   - Email: yamada@example.com
   - Password: password123

## APIドキュメント

FastAPIの自動生成されたSwagger UIドキュメントは以下のURLで確認できます：

```
http://localhost:8000/docs
