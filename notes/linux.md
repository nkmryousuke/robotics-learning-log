# Linuxの基本

## 覚えるべきコマンド（★：何も見ずに使える／☆：読めればOK）

### ファイルとフォルダ
- ★ `pwd`：print working directory 
- ★ `ls`：
- ★ `cd`（`cd ~`、`cd ..` も）：
- ★ `mkdir -p`（`-p`の意味）：
- ★ `mv`：
- ★ `cp`：
- ★ `rm`（`rm -rf`の意味と危険性）：
- ★ `cat`：
- ★ `tail -n 5`：

### 権限とパッケージ
- ★ `sudo`：
- ★ `apt update`：
- ★ `apt upgrade`：
- ★ `apt install -y`（`-y`の意味）：
- ☆ `dpkg`：
- ☆ `snap`：

### 環境の設定
- ★ `echo`：
- ★ `>` と `>>` の違い：
- ★ `.bashrc`：
- ★ `source`：
- ★ `export`：
- ★ 環境変数とPATH：
- ★ `which`：
- ☆ `sed -i`：
- ☆ `$( )`：
- ☆ `|`（パイプ）：

### 便利な操作
- ★ Tabキー：
- ★ Ctrl+C：
- ★ `history`：
- ★ `&&`：
- ★ `コマンド &`（最後の&）：

### ROS2
- ★ `ros2 run`：
- ★ `ros2 launch`：
- ★ `colcon build --symlink-install`：
- ☆ `rosdep install`：

### GitとSSH
- ★ `git clone`：
- ★ `git add` / `git commit` / `git push`：
- ☆ `git config --global`：
- ☆ `ssh-keygen`：
- ☆ `ssh -T git@github.com`：

---

## 環境構築でやったこと（履歴の番号つき）

### 1. Ubuntuの初期設定（1〜10）
- 何をしたか：
- 9の`sed`は何を書き換えたか：
- 10の`timedatectl`は何をしたか：

### 2. ROS2 Jazzyのインストール（11〜24）
- 12〜15（ロケール設定）は何のためか：
- 16〜20（リポジトリの追加）は何のためか：
- 22で入れたもの：
- 23〜24で何をしたか：

### 3. 動作確認（25、26、51、52）
- talkerとlistenerで確かめたこと：
- turtlesimとteleopで確かめたこと：

### 4. GazeboとTurtleBot3（27〜58）
- 27で入れたもの：
- 28〜32で何をしたか：
- 34〜36（rosdep）は何のためか：
- 37と43（colcon build）は何をしたか：
- 44〜49で何をしたか：
- 57の`LIBGL_ALWAYS_SOFTWARE=1`は何のためか：

### 5. GitHubとの接続（59〜65）
- 何をしたか：
- SSHキーとは何か：

### 6. 作業フォルダの準備（67〜73）
- ワークスペースとは何か、なぜ`src`の中にリポジトリを置いたか：

---

## つまずいたことと解決策
- 1：`upgrade-y`でエラー →
- 3：Firefoxのインストールで止まった →
- 37：TurtleBot3のビルドが失敗した →
- 46：`source ~/.bashrc~`で失敗した →
- 54：Gazeboの画面が灰色だった →
- 71：`gedit`が見つからなかった →

## 自分の言葉で説明する
- なぜ`source ~/.bashrc`が必要だったのか：
- なぜ`apt install`の前に`apt update`をするのか：
- `sudo`をつけるのはどんなときか：
