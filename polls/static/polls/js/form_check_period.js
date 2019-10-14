$(document).ready(function(){

    $("#periodForm").submit(function(){
        var aday = $('input[name="aday"]').val();
        var bday = $('input[name="bday"]').val();
        var aday = $('input[name="cday"]').val();
        var aday = $('input[name="dday"]').val();

        if (aday==""||bday==""||cday==""||dday=="")
            {
                alert("날짜를 입력해 주세요")
                return false;
            }

        // var keywordA = $('input[name="keywordA"]').val();
        // var keywordB = $('input[name="keywordB"]').val();
        // alert(keywordA);
        // alert(keywordB);
        var keywordA = $('input[name="keywordA"]').val();
        if (keywordA=="")
            {
                alert("keyword를 다시 입력해 주세요!");
                return false;
            }
        var countA = $("input:checkbox[name='channelA']:checked").length
        if(count<1)
            {
                alert("하나 이상의 채널을 선택해 주세요.")
                return false;
            }

    })
})