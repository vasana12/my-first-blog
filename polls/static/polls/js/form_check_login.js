$(document).ready(function(){

    $("#loginForm").submit(function(){

        var usr_id = $('input[name="usr_id"]').val();

        var usr_pass = $('input[name="password"]').val();
        if (usr_id=="")
            {
                alert("id를 입력해 주세요");
                return false;
            }

        if (usr_pass=="")
            {
                alert("password를 입력해 주세요");
                return false;
            }

    })
})