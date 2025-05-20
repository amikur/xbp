const nameMap = new Map(JSON.parse(localStorage.getItem('nameMap')) || []);
let isEditMode = false;

function saveNameMap() {
    localStorage.setItem('nameMap', JSON.stringify(Array.from(nameMap.entries())));
}

function updateNameList() {
    const nameList = document.getElementById('name-list');
    nameList.innerHTML = '';
    nameMap.forEach((displayName, pronunciation) => {
        const listItem = document.createElement('div');
        listItem.classList.add('name-item');

        const textContent = document.createElement('span');
        textContent.textContent = `${pronunciation} -> ${displayName}`;
        listItem.appendChild(textContent);

        if (isEditMode) {
            const buttonContainer = document.createElement('div');
            buttonContainer.classList.add('button-container');

            const editButton = document.createElement('button');
            editButton.textContent = '編集';
            editButton.classList.add('edit-button');
            editButton.addEventListener('click', () => editName(pronunciation, displayName));
            buttonContainer.appendChild(editButton);

            const deleteButton = document.createElement('button');
            deleteButton.textContent = '削除';
            deleteButton.classList.add('delete-button');
            deleteButton.addEventListener('click', () => deleteName(pronunciation));
            buttonContainer.appendChild(deleteButton);

            listItem.appendChild(buttonContainer);
        }

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

document.getElementById('toggle-edit-btn').addEventListener('click', function() {
    isEditMode = !isEditMode;
    this.textContent = isEditMode ? '編集完了' : '編集';
    updateNameList();
});

function editName(pronunciation, displayName) {
    document.getElementById('pronunciation').value = pronunciation;
    document.getElementById('display-name').value = displayName;

    nameMap.delete(pronunciation);
    saveNameMap();
    updateNameList();
}

function deleteName(pronunciation) {
    nameMap.delete(pronunciation);
    saveNameMap();
    updateNameList();
}

window.addEventListener('load', updateNameList);

document.getElementById('back-to-transcription-btn').addEventListener('click', function() {
    window.location.href = 'test.html'; // 文字起こしページへのリンク
});