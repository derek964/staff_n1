//修改学生密码的函数
function changepassword() {
    if ($('#oldpassword').val() == '' || $('#newpassword1').val() == '' || $('#newpassword2').val() == '') {
        $("#newpasswordinfo").text("密码不能为空！");
    } else if ($('#newpassword1').val() != $('#newpassword2').val()) {
        $("#newpasswordinfo").text("两次输入的新密码不一致！");
    } else {
        $.post('/changepassword/', {
            'oldpassword': $('#oldpassword').val(),
            'newpassword1': $('#newpassword1').val(),
            'newpassword2': $('#newpassword2').val(),
        }, function (res) {
            if(res.result){
                alert("修改成功！");
                window.location.reload();
            }else{
                alert("旧密码不正确，请重新输入！");
                window.location.reload();
            }
        }, 'json')
    }
};