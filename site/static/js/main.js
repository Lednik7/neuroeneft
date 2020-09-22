window.onload = function() {
    document.getElementById('click_3day').addEventListener('click', function (e) {
        $.ajax({
            url: "http://0.0.0.0:10000/calc/3",
            context: document.body,
            success: function(){
                document.getElementById('img_src').src='../static/media/image/3.png';
            }
        });
    });
    document.getElementById('click_week').addEventListener('click', function (e) {
        $.ajax({
            url: "http://0.0.0.0:10000/calc/7",
            context: document.body,
            success: function(){
                document.getElementById('img_src').src='../static/media/image/7.png';
            }
        });
    });

    document.getElementById('click_month').addEventListener('click', function (e) {
        $.ajax({
            url: "http://0.0.0.0:10000/calc/30",
            context: document.body,
            success: function(){
                document.getElementById('img_src').src='../static/media/image/30.png';
            }
        });
    });

    document.getElementById('predict_date').addEventListener('click', function (e) {
        $.ajax({
            url: "http://0.0.0.0:10000/pred",
            data: {date: document.getElementById('datepicker').value},
            context: document.body,
            success: function(data){
                document.getElementById('price_date').innerText = data['price'];
            }
        });
    });
};

$(function(){
    $("#datepicker").datepicker({
        showOn: "button",
        buttonImage: "https://snipp.ru/demo/437/calendar.gif",
        buttonImageOnly: true,
        buttonText: "Выбрать дату"
    });
});