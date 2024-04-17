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
        if (savedText.value.length > 0) {
            savedText.value += 'xxxxxxxxxxxx\n'; // 既存のテキストと新しいテキストの間に区切りを追加
        }
        savedText.value += realtimeOutput.value; // テキストを移動
        realtimeOutput.value = ''; // リアルタイム音声出力をクリア
        finalTranscript = ''; // 最終結果をリセット
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

    if (savedText.value.length > 0) {
        savedText.value += 'xxxxxxxxxxxx\n'; // 既存のテキストと新しいテキストの間に区切りを追加
    }
    savedText.value += realtimeOutput.value;// テキストを移動
    realtimeOutput.value = '';// リアルタイム音声出力をクリア
    finalTranscript = '';// 最終結果をリセット
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

// テキストボックスの内容をlocalStorageに保存する関数
function saveToLocalStorage() {
    localStorage.setItem('realtimeOutput', document.getElementById('realtime-output').value);
    localStorage.setItem('savedText', document.getElementById('saved-text').value);
    localStorage.setItem('pastContents', document.getElementById('past-contents').value);
    localStorage.setItem('summaryResult', document.getElementById('summary-result').value);
}

// ページ読み込み時にlocalStorageからテキストボックスの内容を復元する
window.onload = function() {
    document.getElementById('realtime-output').value = localStorage.getItem('realtimeOutput') || '';
    document.getElementById('saved-text').value = localStorage.getItem('savedText') || '';
    document.getElementById('past-contents').value = localStorage.getItem('pastContents') || '';
    document.getElementById('summary-result').value = localStorage.getItem('summaryResult') || '';
};

// リセットボタンのクリックイベントハンドラ
const resetBtn = document.getElementById('reset-btn');
resetBtn.addEventListener('click', () => {
    if (confirm('全てのテキストボックスの内容をリセットしますか？')) {
        // localStorageからも削除
        localStorage.removeItem('realtimeOutput');
        localStorage.removeItem('savedText');
        localStorage.removeItem('pastContents');
        localStorage.removeItem('summaryResult');

        // 全てのテキストボックスをクリア
        document.getElementById('realtime-output').value = '';
        document.getElementById('saved-text').value = '';
        document.getElementById('past-contents').value = '';
        document.getElementById('summary-result').value = '';
    }
});

// テキストボックスの内容が変更されたときにlocalStorageに保存
document.getElementById('realtime-output').addEventListener('input', saveToLocalStorage);
document.getElementById('saved-text').addEventListener('input', saveToLocalStorage);
document.getElementById('past-contents').addEventListener('input', saveToLocalStorage);
document.getElementById('summary-result').addEventListener('input', saveToLocalStorage);

// ページ読み込み時に実行する関数を追加
window.addEventListener('load', function() {
    // テキストボックスを取得
    const realtimeOutput = document.getElementById('realtime-output');
    // テキストボックスを編集可能にする
    realtimeOutput.disabled = false;

    // 既存のlocalStorageのデータを復元
    document.getElementById('realtime-output').value = localStorage.getItem('realtimeOutput') || '';
    document.getElementById('saved-text').value = localStorage.getItem('savedText') || '';
    document.getElementById('past-contents').value = localStorage.getItem('pastContents') || '';
    document.getElementById('summary-result').value = localStorage.getItem('summaryResult') || '';
});

// その他の初期化コード
recognition.isRecognizing = false;

// コピーして過去の内容に移動する関数
function copyAndMoveText() {
    const savedText = document.getElementById('saved-text');
    const pastContents = document.getElementById('past-contents');
    
    // クリップボードにコピー
    navigator.clipboard.writeText(savedText.value).then(() => {
        // コピー成功時に過去の内容にテキストを移動
        pastContents.value += savedText.value + "\n";
        savedText.value = ''; // 元のテキストボックスをクリア
        alert('テキストが過去の内容に移動されました。');
    }).catch(err => {
        console.error('コピーに失敗しました: ', err);
    });
}





