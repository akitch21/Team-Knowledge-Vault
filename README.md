# Team Knowledge Vault
## Overview

Team Knowledge Vault は、チームの技術メモやノウハウを蓄積・検索・共有するためのナレッジ管理アプリです。
散在しがちなナレッジを一箇所に集約し、再利用を促進することを目的としています。

## Features

- 記事の作成・編集・閲覧・削除

- タグ管理によるナレッジの分類

- 状態（draft/published）による記事公開制御

- 今後の予定: 検索機能、AIによる要約・レコメンド、ユーザー権限管理 など

## Technology Stack
| Layer          | Main Tech                   |
| -------------- | --------------------------- |
| Frontend       | Next.js (React, TypeScript) |
| Backend        | FastAPI (Python)            |
| Database       | PostgreSQL                  |
| Infrastructure | Docker / docker-compose     |

## System Architecture

Next.js フロントエンドが FastAPI バックエンドへ REST API を通じてアクセスし、FastAPI が PostgreSQL へデータを保存します。
将来的に全文検索やベクトル検索を導入する場合、別サービス（例: Elasticsearch, Supabaseなど）を追加します。

Directory Structure
Team-Knowledge-Vault/
  ├── frontend/         # Next.js アプリケーション
  ├── backend/          # FastAPI アプリケーション
  │   ├── api/          # ルーター定義
  │   ├── schemas/      # Pydantic スキーマ
  │   ├── models/       # DB モデル定義
  │   ├── services/     # ビジネスロジック
  │   └── db/           # DB 接続設定
  ├── docs/             # 設計資料や仕様書
  └── README.md         # プロジェクト概要

## Getting Started
### Prerequisites

- Node.js と npm

- Python 3.11 以上

- Docker と docker-compose

## Development Setup

1. リポジトリをクローンします。

2. frontend ディレクトリで依存パッケージをインストールし、開発サーバを起動します。

3. backend ディレクトリで仮想環境を作成し、必要なパッケージをインストールして FastAPI サーバを起動します。

4. Docker を使用する場合は、リポジトリルートで docker-compose up を実行して全サービスを起動します。

## API Overview

エンドポイントの詳細は docs/api ディレクトリの OpenAPI ドキュメントを参照してください。
ここでは代表的なエンドポイント例を示します。

```
GET /articles
GET /articles/{id}
POST /articles
PUT /articles/{id}
DELETE /articles/{id}
```

## Database Design

ユーザ (users)・記事 (articles)・タグ (tags) のテーブルを中心としたシンプルな構成です。
詳細な ER 図は docs/er_diagram.png を参照してください。

## Roadmap

- Phase 1: 基本 CRUD 機能と認証

- Phase 2: 検索・タグ管理・外部サービス連携

- Phase 3: AI要約やレコメンド機能の実装

## Contributing

Pull Request や Issue は歓迎します。貢献時は以下に注意してください。

- ブランチは機能ごとに切り、main へは Pull Request でマージ。

- コーディング規約や lint ツールに従う。

- Issue テンプレートを活用し、内容を明確に記述する。
