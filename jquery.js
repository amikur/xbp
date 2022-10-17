// スクロールすると上部にヘッダー固定
    $(function () {
      $(window).on("scroll", function () {
        // 最初のh2を通過したらclassを付与 
        const sliderHeight = $("h2:first").height();
        if (sliderHeight - 30 < $(this).scrollTop()) {
          $(".header").addClass("headerColorScroll");
          $("#logo").addClass("headerColorScroll");
        } else {
          $(".header").removeClass("headerColorScroll");
          $("#logo").removeClass("headerColorScroll");
        }
      });
    });

    $('#animation').css('visibility','hidden');
$(window).scroll(function(){
 var windowHeight = $(window).height(),
     topWindow = $(window).scrollTop();
 $('#animation').each(function(){
  var targetPosition = $(this).offset().top;
  if(topWindow > targetPosition - windowHeight + 100){
   $(this).addClass("fadeInDown");
  }
 });
});


