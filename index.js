$(document).ready(function(){
  // モーダルウィンドウを表示
  $("#volunteerModal").show();

  // 閉じるボタンのクリックイベント
  $(".close").click(function(){
    $("#volunteerModal").hide();
  });

  // モーダルウィンドウの外側をクリックしても閉じる
  $(window).click(function(event) {
    if (event.target.id == "volunteerModal") {
      $("#volunteerModal").hide();
    }
  });
});
