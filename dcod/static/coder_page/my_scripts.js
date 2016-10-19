
$(function() {
    $(document).ready(function() {

//required for csrf token
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

//handler encrypt key, send post request on server
        $("#encryption_key").click(function(){
            
            var event = {
                text: $("#original_text").val(),
                step: $("#step").val(),
            };
            
            if( event.text != '' && event.step != '') {
            
                var str = JSON.stringify(event);
                
                $.ajax({
                    type: "POST",
                    url: "/lit/cipher/",
                    dataType: "json",
                    contentType: 'application/json; charset=utf-8',
                    data: str,
                    cache: false,
                    success: function(return_data){
                        $("#cipher_text").text(return_data.cipher_text);
                        if(return_data.advice == '26' || return_data.advice == '0') {
                            $("#advice").text('When you click "Decrypt", in this place will show advice :-)');
                        } else {
                            $("#advice").text('May be this text encrypted, try step = ' + return_data.advice + ' and click "Decrypt".');
                        };
                        
                        var data_chart = return_data.counter_list;
                        drawChart(data_chart);
                    }
                });
            } else {
                $("#advice").text("Please enter the text and step.");
            };

        });

//handler decrypt key, send post request on server
        $("#decryption_key").click(function(){
            
            var event = {
                text: $("#original_text").val(),
                step: -$("#step").val(),
            };
            
            if( event.text != '' && event.step != '') {
                
                var str = JSON.stringify(event);
                
                $.ajax({
                    type: "POST",
                    url: "/lit/cipher/",
                    dataType: "json",
                    contentType: 'application/json; charset=utf-8',
                    data: str,
                    cache: false,
                    success: function(return_data){
                        $("#cipher_text").text(return_data.cipher_text)
                        if(return_data.advice == '26' || return_data.advice == '0') {
                            $("#advice").text('May be this text not encrypted.');
                        } else {
                            $("#advice").text("Recommended step = " + return_data.advice);
                        };
                        
                        var data_chart = return_data.counter_list;
                        drawChart(data_chart);
                    }
                });
            } else {
                $("#advice").text("Please enter the text and step.");
            };
        });

//reset form
        $("#reset").click(function(){
            $("#cipher_text").text("");
            $("#advice").text("...");
            $("#diagram").html('');
        });
        
//Google Charts
        google.charts.load("current", {packages:["corechart"]});
        
        function drawChart(data_chart) {
            
            var alphabet = "abcdefghijklmnopqrstuvwxyz";
            
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Letter');
            data.addColumn('number', 'count');
            
            for (var i = 0; i < 26; i++) {
                data.addRow([alphabet[i], data_chart[i]]);
            }

            var options = {
                legend: { position: 'none' },
            };
    
            var chart = new google.visualization.ColumnChart(document.getElementById('diagram'));
            chart.draw(data, options);
        };

    });
});
