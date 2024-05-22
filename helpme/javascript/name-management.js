const nameMap = new Map(JSON.parse(localStorage.getItem('nameMap')) || []);

function saveNameMap() {
    localStorage.setItem('nameMap', JSON.stringify(Array.from(nameMap.entries())));
}

function updateNameList() {
    const nameList = document.getElementById('name-list');
    nameList.innerHTML = '';
    nameMap.forEach((displayName, pronunciation) => {
        const listItem = document.createElement('div');
        listItem.textContent = `${pronunciation} -> ${displayName}`;
        nameList.appendChild(listItem);
    });
}

document.getElementById('add-name-btn').addEventListener('click', function() {
    const pronunciation = document.getElementById('pronunciation').value.trim();
    const displayName = document.getElementById('display-name').value.trim();

    if (pronunciation && displayName) {
        nameMap.set(pronunciation, displayName);
        saveNameMap();
        updateNameList();

        // テキストボックスをクリア
        document.getElementById('pronunciation').value = '';
        document.getElementById('display-name').value = '';
    }
});

window.addEventListener('load', updateNameList);

document.getElementById('back-to-transcription-btn').addEventListener('click', function() {
    window.location.href = 'cheindex.html'; // 文字起こしページへのリンク
});