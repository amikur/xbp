const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const resetBtn = document.getElementById('reset-btn');
const copyBtn = document.getElementById('copy-btn');
const gotoNameManagementBtn = document.getElementById('goto-name-management-btn');
const langToggleBtn = document.getElementById('lang-toggle-btn'); // 言語切り替えボタン
const realtimeOutput = document.getElementById('realtime-output');
const savedText = document.getElementById('saved-text');
const pastContents = document.getElementById('past-contents');

const speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new speechRecognition();

recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = localStorage.getItem('speechLang') || 'ja-JP'; // 言語の保存・復元

let finalTranscript = '';

// ローカルストレージからnameMapを取得
const nameMap = new Map(JSON.parse(localStorage.getItem('nameMap')) || []);
console.log('Loaded nameMap:', nameMap);

// 言語切り替え機能
langToggleBtn.addEventListener('click', function () {
    if (recognition.lang === 'ja-JP') {
        recognition.lang = 'en-US';
        localStorage.setItem('speechLang', 'en-US');
        langToggleBtn.textContent = 'Switch to Japanese';
    } else {
        recognition.lang = 'ja-JP';
        localStorage.setItem('speechLang', 'ja-JP');
        langToggleBtn.textContent = 'Englishに切り替え';
    }
    alert(`Language changed to: ${recognition.lang}`);
});

recognition.onresult = function (event) {
    let interimTranscript = '';

    for (let i = event.resultIndex; i < event.results.length; ++i) {
        let transcript = event.results[i][0].transcript;

        console.log('Original transcript:', transcript);

        // 各単語に対して置き換えを行う
        let words = transcript.split(' ');
        words = words.map(word => {
            nameMap.forEach((displayName, pronunciation) => {
                const regex = new RegExp(pronunciation, 'gi');
                if (regex.test(word)) {
                    console.log('Applying regex:', regex);
                    word = word.replace(regex, displayName);
                }
            });
            return word;
        });

        transcript = words.join(' ');

        console.log('Replaced transcript:', transcript);

        if (event.results[i].isFinal) {
            finalTranscript += transcript + ' ';
        } else {
            interimTranscript += transcript;
        }
    }

    console.log('Final transcript:', finalTranscript);
    console.log('Interim transcript:', interimTranscript);

    realtimeOutput.value = finalTranscript + interimTranscript;

    saveToLocalStorage();

    if (realtimeOutput.value.length >= 2000) {
        if (savedText.value.length > 0) {
            savedText.value += 'xxxxxxxxxxxx\n';
        }
        savedText.value += realtimeOutput.value;
        realtimeOutput.value = '';
        finalTranscript = '';
    }
};

recognition.onerror = function (event) {
    console.error('Speech recognition error: ' + event.error);
};

recognition.onend = function () {
    if (recognition.isRecognizing) {
        recognition.start();
    }
};

startBtn.addEventListener('click', function () {
    recognition.isRecognizing = true;
    finalTranscript = '';
    realtimeOutput.value = '';
    recognition.start();
});

stopBtn.addEventListener('click', function () {
    recognition.isRecognizing = false;
    recognition.stop();

    if (savedText.value.length > 0) {
        savedText.value += 'xxxxxxxxxxxx\n';
    }
    savedText.value += realtimeOutput.value;
    realtimeOutput.value = '';
    finalTranscript = '';
});

recognition.isRecognizing = false;

copyBtn.addEventListener('click', copyAndMoveText);
gotoNameManagementBtn.addEventListener('click', function () {
    window.location.href = 'name-management.html';
});

function copyAndMoveText() {
    navigator.clipboard.writeText(savedText.value).then(() => {
        pastContents.value += savedText.value + "\n";
        savedText.value = '';
        alert(recognition.lang === 'ja-JP' ? 'テキストが過去の内容に移動されました。' : 'Text has been moved to past contents.');
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

function saveToLocalStorage() {
    localStorage.setItem('realtimeOutput', realtimeOutput.value);
    localStorage.setItem('savedText', savedText.value);
    localStorage.setItem('pastContents', pastContents.value);
}

resetBtn.addEventListener('click', () => {
    if (confirm(recognition.lang === 'ja-JP' ? '全てのテキストボックスの内容をリセットしますか？' : 'Do you want to reset all text boxes?')) {
        localStorage.removeItem('realtimeOutput');
        localStorage.removeItem('savedText');
        localStorage.removeItem('pastContents');

        realtimeOutput.value = '';
        savedText.value = '';
        pastContents.value = '';
    }
});

realtimeOutput.addEventListener('input', saveToLocalStorage);
savedText.addEventListener('input', saveToLocalStorage);
pastContents.addEventListener('input', saveToLocalStorage);

window.addEventListener('load', function () {
    realtimeOutput.value = localStorage.getItem('realtimeOutput') || '';
    savedText.value = localStorage.getItem('savedText') || '';
    pastContents.value = localStorage.getItem('pastContents') || '';

    langToggleBtn.textContent = recognition.lang === 'ja-JP' ? 'Englishに切り替え' : 'Switch to Japanese';
});
