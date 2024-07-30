document.addEventListener('DOMContentLoaded', function() {
  const areas = document.querySelectorAll('area');
  const infoDiv = document.getElementById('prefecture-info');

  areas.forEach(area => {
      area.addEventListener('click', function(event) {
          event.preventDefault();
          const prefecture = area.alt;
          displayPrefectureInfo(prefecture);
      });
  });

  function displayPrefectureInfo(prefecture) {
      infoDiv.innerHTML = `
          <h2>${prefecture}</h2>
          <p>${prefecture}の観光名所情報をここに表示</p>
          <button onclick="closePrefectureInfo()">閉じる</button>
      `;
      infoDiv.classList.add('active');
  }

  window.closePrefectureInfo = function() {
      infoDiv.classList.remove('active');
  }
});