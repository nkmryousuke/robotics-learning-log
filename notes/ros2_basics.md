## 通信方式
# topic
- 一方向垂れ流し（publisher -> subscriber）
- センサーの値など流しっぱなしで問題ない場合に使う
- ros2 topic pub トピック名 型 YAML 
# service
- 双方向（client >request> server >response> client）
- 短時間で終わる値のリセットなどに使う
- ros2 service call 
# action
- 双方向で途中経過報告ありでキャンセル可能
- 最初にリクエストsend_goalとget_resultをおくり、ゴールが受諾されたらレスポンスが帰ってくる。途中経過をトピックでfeedbackとして受け取り、終わったらレスポンスがかえる。
- 時間のかかる処理で使う