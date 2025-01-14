<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // メールの内容を作成
    $to = 'あなたのメールアドレス@example.com'; // ここに送信先のメールアドレスを指定
    $subject = 'お問い合わせフォームからのメッセージ';
    $body = "お名前: $name\nメールアドレス: $email\nメッセージ:\n$message";
    $headers = "From: $email";

    // メールの送信
    if (mail($to, $subject, $body, $headers)) {
        echo "メッセージが送信されました。";
    } else {
        echo "メッセージの送信に失敗しました。";
    }
}
?>
