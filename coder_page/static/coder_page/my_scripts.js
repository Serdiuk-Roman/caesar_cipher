
$(function() {
    $(document).ready(function() {


        $(function () {
            $.ajaxSetup({
                headers: { "X-CSRFToken": getCookie("csrftoken") }
            });
        });
        
        function getCookie(c_name) {
            if (document.cookie.length > 0) {
                c_start = document.cookie.indexOf(c_name + "=");
                if (c_start != -1) {
                    c_start = c_start + c_name.length + 1;
                    c_end = document.cookie.indexOf(";", c_start);
                    if (c_end == -1) c_end = document.cookie.length;
                    return unescape(document.cookie.substring(c_start,c_end));
                }
            }
            return "";
        }


        $("#encryption_key").click(function(){
            
            var event = {
                text: $("#original_text").val(),
                step: $("#step").val(),
                flag: "0",
            };
            
            var str = JSON.stringify(event);
            
            $.ajax({
                type: "POST",
                url: "/cipher/",
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                data: str,
                cache: false,
                success: function(return_data){
                    $("#cipher_text").text(return_data.cipher_text)
                    $("#advice").text(return_data.advice)
                }
            });
        });


        $("#decryption_key").click(function(){
            
            var event = {
                text: $("#original_text").val(),
                step: -$("#step").val(),
                flag: "1",
            };
            
            var str = JSON.stringify(event);
            
            $.ajax({
                type: "POST",
                url: "/cipher/",
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                data: str,
                cache: false,
                success: function(return_data){
                    $("#cipher_text").text(return_data.cipher_text)
                    $("#advice").text(return_data.advice)
                }
            });
        });


        $("#reset").click(function(){
            $("#cipher_text").text("");
            $("#advice").text("...");
        });


    });
});




















