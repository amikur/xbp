const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const realtimeOutput = document.getElementById('realtime-output');
const savedText = document.getElementById('saved-text');

const speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new speechRecognition();

recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = 'ja-JP';

let finalTranscript = '';

recognition.onresult = function(event) {
    let interimTranscript = '';

    for (let i = event.resultIndex; i < event.results.length; ++i) {
        let transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
            finalTranscript += transcript + ' ';
        } else {
            interimTranscript += transcript;
        }
    }

    realtimeOutput.value = finalTranscript + interimTranscript;

    if (realtimeOutput.value.length >= 2000) {
        savedText.value += realtimeOutput.value;
        realtimeOutput.value = '';
        finalTranscript = '';
    }
};

recognition.onerror = function(event) {
    console.error('音声認識エラー: ' + event.error);
};

recognition.onend = function() {
    if (recognition.isRecognizing) {
        recognition.start();
    }
};

startBtn.addEventListener('click', function() {
    recognition.isRecognizing = true;
    finalTranscript = '';
    realtimeOutput.value = '';
    recognition.start();
});

stopBtn.addEventListener('click', function() {
    recognition.isRecognizing = false;
    recognition.stop();
    savedText.value += realtimeOutput.value;
    realtimeOutput.value = '';
    finalTranscript = '';
});

recognition.isRecognizing = false;

// コピーして過去の内容に移動する関数
function copyAndMoveText() {
    const savedText = document.getElementById('saved-text');
    const pastContents = document.getElementById('past-contents');
    
    // クリップボードにコピー
    navigator.clipboard.writeText(savedText.value).then(() => {
        // コピー成功時に過去の内容にテキストを移動
        pastContents.value += savedText.value + "\n"; // 既存のテキストに新しいテキストを追加
        savedText.value = ''; // 元のテキストボックスをクリア
        alert('テキストが過去の内容に移動されました。');
    }).catch(err => {
        console.error('コピーに失敗しました: ', err);
    });
}

// コピー用ボタンのクリックイベントハンドラを設定
const copyBtn = document.getElementById('copy-btn');
copyBtn.addEventListener('click', copyAndMoveText);