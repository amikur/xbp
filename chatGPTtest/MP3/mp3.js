document.addEventListener('DOMContentLoaded', function() {
  const fileInput = document.getElementById('audioFile');
  const canvas = document.getElementById('visualizer');
  const ctx = canvas.getContext('2d');
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  let analyser = audioContext.createAnalyser();
  let source;

  fileInput.addEventListener('change', function() {
      const files = this.files;
      if (files.length > 0) {
          const reader = new FileReader();
          reader.onload = function(e) {
              audioContext.decodeAudioData(e.target.result, function(buffer) {
                  if (source) {
                      source.stop();
                  }
                  source = audioContext.createBufferSource();
                  source.buffer = buffer;
                  source.connect(analyser);
                  analyser.connect(audioContext.destination);
                  source.start();
                  visualize();
              });
          };
          reader.readAsArrayBuffer(files[0]);
      }
  });

  function visualize() {
      const WIDTH = canvas.width;
      const HEIGHT = canvas.height;
      const barWidth = (WIDTH / analyser.frequencyBinCount) * 2.5;
      let barHeight;
      const dataArray = new Uint8Array(analyser.frequencyBinCount);

      function draw() {
          requestAnimationFrame(draw);
          analyser.getByteFrequencyData(dataArray);

          ctx.fillStyle = '#000';
          ctx.fillRect(0, 0, WIDTH, HEIGHT);

          let x = 0;

          for (let i = 0; i < analyser.frequencyBinCount; i++) {
              barHeight = dataArray[i];

              const r = barHeight + (25 * (i/analyser.frequencyBinCount));
              const g = 250 * (i/analyser.frequencyBinCount);
              const b = 50;

              ctx.fillStyle = `rgb(${r},${g},${b})`;
              ctx.fillRect(x, HEIGHT - barHeight, barWidth, barHeight);

              x += barWidth + 1;
          }
      }

      draw();
  }
});

// ... 既存のコード ...

let audioBuffer;
let isPlaying = false;

document.getElementById('playButton').addEventListener('click', function() {
    if (!isPlaying) {
        if (audioBuffer) {
            source = audioContext.createBufferSource();
            source.buffer = audioBuffer;
            source.connect(analyser);
            analyser.connect(audioContext.destination);
            source.start(0);
            isPlaying = true;
            visualize();
        }
    }
});

document.getElementById('stopButton').addEventListener('click', function() {
    if (isPlaying) {
        source.stop(0);
        isPlaying = false;
    }
});

// ファイルのアップロードと読み込みの処理に小さな変更を加えます
fileInput.addEventListener('change', function() {
    const files = this.files;
    if (files.length > 0) {
        const reader = new FileReader();
        reader.onload = function(e) {
            audioContext.decodeAudioData(e.target.result, function(buffer) {
                audioBuffer = buffer;
            });
        };
        reader.readAsArrayBuffer(files[0]);
    }
});

// ... 既存の visualize 関数 ...

