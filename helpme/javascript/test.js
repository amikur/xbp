const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const resetBtn = document.getElementById('reset-btn');
const copyBtn = document.getElementById('copy-btn');
const gotoNameManagementBtn = document.getElementById('goto-name-management-btn');
const realtimeOutput = document.getElementById('realtime-output');
const savedText = document.getElementById('saved-text');
const pastContents = document.getElementById('past-contents');

const speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new speechRecognition();

recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = 'ja-JP';

let finalTranscript = '';

// ローカルストレージからnameMapを取得
const nameMap = new Map(JSON.parse(localStorage.getItem('nameMap')) || []);
console.log('Loaded nameMap:', nameMap); // nameMapの内容をコンソールにログ出力

recognition.onresult = function(event) {
    let interimTranscript = '';

    for (let i = event.resultIndex; i < event.results.length; ++i) {
        let transcript = event.results[i][0].transcript;

        // 固有名詞の置き換え
        nameMap.forEach((displayName, pronunciation) => {
            // 正規表現で大文字小文字を区別せずに置き換える
            const regex = new RegExp(pronunciation, 'gi');
            transcript = transcript.replace(regex, displayName);
        });

        if (event.results[i].isFinal) {
            finalTranscript += transcript + ' ';
        } else {
            interimTranscript += transcript;
        }
    }
    
    realtimeOutput.value = finalTranscript + interimTranscript;

    // Save the current content to localStorage
    saveToLocalStorage();

    // 2000文字を超えたらsavedTextに移動
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
    savedText.value += realtimeOutput.value; // テキストを移動
    realtimeOutput.value = ''; // リアルタイム音声出力をクリア
    finalTranscript = ''; // 最終結果をリセット
});

recognition.isRecognizing = false;

copyBtn.addEventListener('click', copyAndMoveText);
gotoNameManagementBtn.addEventListener('click', function() {
    window.location.href = 'name-management.html'; // 固有名詞登録ページへのリンク
});

// コピーして過去の内容に移動する関数
function copyAndMoveText() {
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

// テキストボックスの内容をlocalStorageに保存する関数
function saveToLocalStorage() {
    localStorage.setItem('realtimeOutput', realtimeOutput.value);
    localStorage.setItem('savedText', savedText.value);
    localStorage.setItem('pastContents', pastContents.value);
}

resetBtn.addEventListener('click', () => {
    if (confirm('全てのテキストボックスの内容をリセットしますか？')) {
        // localStorageからも削除
        localStorage.removeItem('realtimeOutput');
        localStorage.removeItem('savedText');
        localStorage.removeItem('pastContents');

        // 全てのテキストボックスをクリア
        realtimeOutput.value = '';
        savedText.value = '';
        pastContents.value = '';
    }
});

// テキストボックスの内容が変更されたときにlocalStorageに保存
realtimeOutput.addEventListener('input', saveToLocalStorage);
savedText.addEventListener('input', saveToLocalStorage);
pastContents.addEventListener('input', saveToLocalStorage);

// ページ読み込み時に実行する関数を追加
window.addEventListener('load', function() {
    // 既存のlocalStorageのデータを復元
    realtimeOutput.value = localStorage.getItem('realtimeOutput') || '';
    savedText.value = localStorage.getItem('savedText') || '';
    pastContents.value = localStorage.getItem('pastContents') || '';
});