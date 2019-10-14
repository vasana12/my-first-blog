$(document).ready(function(){

        //---------------Target A--------------------------
        var keywordA = $("#list_keywordA").text();
        keywordA = keywordA.split("'")[1];
        $('#keywordA').html('&emsp;keyword : ' + keywordA);

        var channelA_list= ' ';
        var channelA = $("#list_channelA").text();
        for(var i=0; i<channelA.split("'").length; i++){
            if(i!=channelA.split("'").length-2 &&i%2!=0){
                var channelA_list = channelA_list+channelA.split("'")[i]+',&nbsp;'
            }
            else if(i==channelA.split("'").length-2){
                var channelA_list = channelA_list+channelA.split("'")[i]
            }
        }
        $('#channelA').html('&emsp;channel : ' + channelA_list);


        var periodA = $("#list_periodA").text();
        periodA_start = periodA.split("'")[1];
        periodA_end = periodA.split("'")[3];
        $('#periodA').html('&emsp;period : ' + periodA_start + '~' + periodA_end);
        //-----------------------------------------------------------


        //---------------Target B--------------------------

        var keywordB = $("#list_keywordB").text();
        keywordB = keywordB.split("'")[1];
        $('#keywordB').html('&emsp;keyword : ' + keywordB);

        var channelB_list= ' ';
        var channelB = $("#list_channelB").text();
        for(var i=0; i<channelB.split("'").length; i++){
            if(i!=channelB.split("'").length-2 &&i%2!=0){
                var channelB_list = channelB_list+channelB.split("'")[i]+',&nbsp;'
            }
            else if(i==channelB.split("'").length-2){
                var channelB_list = channelB_list+channelB.split("'")[i]
            }
        }
        $('#channelB').html('&emsp;channel : ' + channelB_list);

        var periodB = $("#list_periodB").text();
        periodB_start = periodB.split("'")[1];
        periodB_end = periodB.split("'")[3];

        $('#periodB').html('&emsp;period : ' + periodB_start + '~' + periodB_end);
        //-----------------------------------------------------------
        $('#targetA').html('&nbsp;TargetA' + '(' + keywordA + '/&nbsp;' + channelA_list + periodA_start + '~' + periodA_end + ')');
        $('#targetB').html('&nbsp;TargetB' + '(' + keywordB + '/&nbsp;' + channelB_list + periodB_start + '~' + periodB_end + ')');
        $('#targetA-B').html('&nbsp;TargetA' + '(' + keywordA + '/&nbsp;' +channelA_list + '/&nbsp;' + periodA_start + '~' + periodA_end + ')' + '<br>' + '-' +
            'TargetB' + '(' + keywordB + '/&nbsp;' + channelB_list + '/&nbsp;' + periodB_start + '~' + periodB_end + ')');
        $('#targetB-A').html('&nbsp;TargetB' + '(' + keywordB + '/&nbsp;' + channelB_list + '/&nbsp;' + periodB_start + '~' + periodB_end + ')' + '<br>' + '-' +
            'TargetA' + '(' + keywordA + '/&nbsp;' + channelA_list + '/&nbsp;' + periodA_start + '~' + periodA_end + ')');


    var strA = $("#outputA").attr("src");
    var strB = $("#outputB").attr("src");
    var strA_B = $("#outputA_B").attr("src");
    var strB_A = $("#outputB_A").attr("src");

    var select_id = $("#select_id").text();

    var locationA =strA.substring(0,21)+select_id+"_"+strA.substring(21,strA.length);
    var locationB =strB.substring(0,21)+select_id+"_"+strB.substring(21,strB.length);
    var locationA_B =strA_B.substring(0,21)+select_id+"_"+strA_B.substring(21,strA_B.length);
    var locationB_A =strB_A.substring(0,21)+select_id+"_"+strB_A.substring(21,strB_A.length);


    $('#outputA').attr("src", locationA);

    $('#outputB').attr("src", locationB);

    $('#outputA_B').attr("src", locationA_B);

    $('#outputB_A').attr("src", locationB_A);

    // var outputB = "static/polls/source/"+select_id+"outputB.png";
    // var outputA_B = "static/polls/source/"+select_id+"outputA_B.png";
    // var outputB_A = "static/polls/source/"+select_id+"outputB_A.png";
    // $("#outputB").attr("src", outputB)
    // $("#outputA_B").attr("src", outputA_B)
    // $("#outputB_A").attr("src", outputB_A)

        // $('.form-check input:checked').each(function(){
        //     selected.push($(this).attr('value'));
        // })

        // var count = $('.form-check input:checked').length;
        // alert(count)
})