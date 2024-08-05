const canvas = document.getElementById('background');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const points = [];
const pointCount = 100;

for (let i = 0; i < pointCount; i++) {
    points.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2
    });
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    points.forEach((point, index) => {
        point.x += point.vx;
        point.y += point.vy;

        if (point.x > canvas.width || point.x < 0) point.vx *= -1;
        if (point.y > canvas.height || point.y < 0) point.vy *= -1;

        ctx.fillStyle = '#00c8c8';
        ctx.beginPath();
        ctx.arc(point.x, point.y, 3, 0, Math.PI * 2);
        ctx.fill();

        for (let j = index + 1; j < points.length; j++) {
            const other = points[j];
            const distance = Math.sqrt((point.x - other.x) ** 2 + (point.y - other.y) ** 2);
            if (distance < 100) {
                ctx.strokeStyle = 'rgba(0, 200, 200, 0.3)';
                ctx.beginPath();
                ctx.moveTo(point.x, point.y);
                ctx.lineTo(other.x, other.y);
                ctx.stroke();
            }
        }
    });

    requestAnimationFrame(draw);
}

draw();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
