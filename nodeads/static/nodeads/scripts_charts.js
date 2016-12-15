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
        $("#sort_key").click(function(){
            
            var event = {text: $("#date :selected").text()};
            var str = JSON.stringify(event);

            $.ajax({
                type: "POST",
                url: "/nodeads/ajax/",
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                data: str,
                cache: false,
                success: function(return_data){
                    drawChart(return_data);
                }
            });
        });


        
//Google Charts
        google.charts.load("current", {packages:["corechart"]});
        
        function drawChart(for_temp) {
            
            var data = new google.visualization.DataTable();
            data.addColumn('string', 'Date');
            data.addColumn('number', 'temp');     
            for (var i = 0, n = for_temp.dt_t.length; i < n; i++) {
                myVal = parseFloat($.trim(for_temp.temp[i]));
                data.addRow([for_temp.dt_t[i], {v: myVal, f: myVal.toFixed(3)}]);
            }
            var options = {
                legend: { position: 'none' },
            };
            var chart = new google.visualization.LineChart(document.getElementById('diagram'));
            chart.draw(data, options);
            
                        
            var data2 = new google.visualization.DataTable();
            data2.addColumn('string', 'Date');
            data2.addColumn('number', 'pres');     
            for (var i = 0, n = for_temp.dt_p.length; i < n; i++) {
                myVal = parseFloat($.trim(for_temp.pres[i]));
                data2.addRow([for_temp.dt_p[i], {v: myVal, f: myVal.toFixed(3)}]);
            }
            var chart = new google.visualization.LineChart(document.getElementById('diagram2'));
            chart.draw(data2, options);
        };
    });
});
