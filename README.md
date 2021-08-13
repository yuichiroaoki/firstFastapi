# Github ActionsでのCI/CDパイプライン構築
![image](https://user-images.githubusercontent.com/45054071/129161150-2a86acfe-7979-4c7f-810f-61e30818db2d.png)
source: https://github.co.jp/features/actions

## Github Actionsとは
Github社が提供するCI/CDツールです。  

### CI/CDとは
ビルド、テスト、デプロイを自動化するシステム  

![image](https://user-images.githubusercontent.com/45054071/129161541-1fa373a6-8c4d-4232-8b3d-75885a6d43d2.png)  
source: NIF CLOUD

利点
* 手動でビルド、テスト、デプロイする手間が省ける
* いち早くバグやmergeコンフリクトを防ぐことができる  
ー＞ 迅速なソフトウェア開発につながる

### Github Actionsの特徴
* 導入の手軽さ
* 安い
* テンプレートが豊富

参考
* https://github.com/marketplace?category=&query=&type=actions&verification=
* https://docs.github.com/ja/actions/guides/building-and-testing-python
* https://github.co.jp/features/actions
* https://github.com/marketplace/circleci/
* https://github.com/marketplace/travis-ci

## Github Actionsの始め方
.github/workflows/ ディレクトリ以下にyamlファイルを配置するのみ

### Pythonワークフローのテンプレート
```yaml
name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [2.7, 3.5, 3.6, 3.7, 3.8]

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint with flake8
        run: |
          # Python 構文エラーまたは未定義の名前がある場合はビルドを停止する
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero はすべてのエラーを警告として扱う。 GitHub エディタの幅は 127 文字
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
      - name: Test with pytest
        run: |
          pytest
 ```
 source: https://docs.github.com/ja/actions/guides/building-and-testing-python#starting-with-the-python-workflow-template
 
 1. GitHubホストランナー上で各バージョンのpythonをセットアップ
 2. requirements.txtからライブラリをインストール
 3. pythonの構文チェック
 4. pytestでコードのテスト
 
 
#### どのように役に立つか
例１. ライブラリのバージョンコンフリクトを検知
 
 ![image](https://user-images.githubusercontent.com/45054071/129168929-2c85cf36-503d-4b00-8342-138ffd97811b.png)　
 
![image](https://user-images.githubusercontent.com/45054071/129169042-6e30c6e8-72d3-4fa4-95c5-a49727fe1aa7.png)


例２．pytestによるエラー

![image](https://user-images.githubusercontent.com/45054071/129169331-4b243712-a805-4ffd-b1ac-8cd77d3ade26.png)


例３．自動でデプロイ

```yaml
      - id: deploy
        uses: google-github-actions/deploy-appengine@main
        with:
          credentials: ${{ secrets.gcp_credentials }}
```
https://github.com/yuichiroaoki/github-actions-example/blob/bb716ae502dee12b9af23a7910eaebc34a5687da/.github/workflows/python.yml#L46-L49

https://github.com/marketplace/actions/deploy-to-app-engine


例４．他のDockerコンテナ（DB、RabbitMQなどのメッセージングサーバーなど）との連携のテストができ

以下のようにポートを指定しmongodbのコンテナを起動させ、データのやり取りができる

```yaml
    services:
      mongodb:
        image: mongo
        ports:
          - 27017:27017
```

![image](https://user-images.githubusercontent.com/45054071/129349975-b090a9fb-df66-4f69-8157-0a6c9960829f.png)



参考
* https://docs.github.com/ja/actions
* https://docs.github.com/ja/actions/guides/building-and-testing-python
* https://docs.github.com/ja/billing/managing-billing-for-github-actions/about-billing-for-github-actions
