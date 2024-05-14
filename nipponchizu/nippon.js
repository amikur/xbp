document.addEventListener("DOMContentLoaded", function() {
  const prefectures = document.querySelectorAll(".prefecture");
  prefectures.forEach(prefecture => {
    prefecture.addEventListener("mouseover", function() {
      const name = this.getAttribute("data-name");
      console.log(name + "にカーソルが合わせられました");
    });
  });
});
