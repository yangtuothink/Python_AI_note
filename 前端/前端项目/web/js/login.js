$(function () {
    // 获取输入框, 监听失焦状态
    $("[name=uname]").blur(function () {
        // 判断长度为0 或 空字符串
        if ($(this).val().length == 0 || $(this).val() == " ") {
            $(this).siblings("span").html("用户名不能为空").css("color","red" )
        } else {
            $(this).siblings("span").html("")
        }

    });
});