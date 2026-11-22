# Netheretヘルプデスク ステップ03：データベース

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

授業のための作例です。16のステップで、小さな会社のITを支える架空の会社Netheretのために、ヘルプデスクのWebアプリを作っていきます。 このステップでは、データベースを加えます。ER図のテーブルをPythonのクラスとして書き、サンプルデータを入れるスクリプトを用意します。

## このステップで加わるもの

- `helpdesk/extensions.py`：Flask-SQLAlchemyの `db` オブジェクト。
- `helpdesk/models.py`：6つのテーブル、`Company`、`User`、`Ticket`、
  `TicketUpdate`、`Job`、`Article`。先頭に、許される値のリスト
  （役割、カテゴリー、優先度、ステータスなど）があります。
- `seed.py`：すべてを削除してから、サンプルの会社、ユーザー、サポート依頼、
  タイムラインの更新、訪問作業、ナレッジベースの記事を読み込みます。
- トップページで各テーブルの行数を数えるようになり、すべてが動いていることを確かめられます。

## 動かしてみる

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

`python seed.py` は `instance/helpdesk.db` を作ります。新しいサンプルデータからやり直したいときは、
いつでもまた実行してください。デモ用アカウントが表示されます。どれもデモ用パスワード
`password123` を使います。これはこの作例のためだけのものです。
まだ誰もサインインできません。それは次のステップです。

## 注目するところ

- `models.py`：各列に型があること、どの列が空でもよいか
  （`| None`）、そしてテーブルを結ぶ外部キー。
- `User.set_password`：パスワードは保存する前にWerkzeugでハッシュにするので、
  データベースにパスワードそのものが入ることはありません。
- `Ticket.set_reference`：`NTH-0001` のような参照番号はidから作ります。idは
  行を保存して初めてできるので、`seed.py` は `db.session.flush()` を呼んでいます。
- どのSQLiteビューアーでもデータベースを開いて、行を見ることができます。

## このステップを学ぶ

これは **Task 2. Developing the solution** の16ステップ中のステップ3です。T Level Digital Software Developmentの無料レッスン（英語）のシリーズで、PythonとFlaskを使い、アジャイルのスプリントでNetheretのヘルプデスクを作ります。このステップのレッスンはこちらです：
[Flask-SQLAlchemyによるデータベース](https://mitsurutech.co.uk/resources/t-level/dsd-t2-03-database)。

- 前のステップ：[ステップ02「JinjaテンプレートとCSSによるページレイアウト」](https://github.com/mitsurutech/netheret-helpdesk-02-layout)
- 次のステップ：[ステップ04「サインイン、役割、セッション」](https://github.com/mitsurutech/netheret-helpdesk-04-sign-in)
- [T Level Digitalの無料レッスン一覧](https://mitsurutech.co.uk/resources/t-level)
- [これらのレッスンをMitsuruTechでクラスに教える](https://mitsurutech.co.uk/ja/learning)、[料金を見る](https://mitsurutech.co.uk/ja/pricing)、
  [学校で無料の1年を始める](https://mitsurutech.co.uk/ja/signup)

## この作例について

T Level Digital Software Developmentの授業のための作例として、[Mitsuru Technologies](https://mitsurutech.co.uk/ja)（MitsuruTech）が書きました。
Netheret IT Support Solutionsの課題文はPearsonのサンプル評価資料によるものです。このコードと解説は私たち自身のもので、
PearsonやDepartment for Educationが公開、推奨、承認したものではありません。
「T Level」はDepartment for Educationの登録商標です。
