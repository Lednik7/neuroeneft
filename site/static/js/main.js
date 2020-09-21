window.onload = function() {
    document.getElementById('click_3day').addEventListener('click', function (e) {
        alert("1")
    });
    document.getElementById('click_week').addEventListener('click', function (e) {
        alert("2")
    });

    document.getElementById('click_month').addEventListener('click', function (e) {
        alert("3")
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
