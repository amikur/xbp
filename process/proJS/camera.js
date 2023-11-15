document.addEventListener("DOMContentLoaded", function() {
  var video = document.getElementById('camera');
  if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
          .then(function (stream) {
              video.srcObject = stream;
          })
          .catch(function (error) {
              console.log("カメラの起動に失敗しました: ", error);
          });
  } else {
      alert("お使いのブラウザはカメラ機能をサポートしていません。");
  }
});
