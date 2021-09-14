//修改密码的函数
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

//editscore的函数
function hire(scode, sname){
    var d = dialog({
            width: 360,
            title: '员工姓名修改',
            quickClose: true,
            content: '<label class="col-sm-3 control-label bk-lh30 pt0">姓名：</label>' +
                '<div class="col-sm-9">' +
                '<input type="text" class="form-control bk-valign-top" id="snamed" placeholder=""> ' +
                '</div>',
            ok: function() {
                    $.post('/staff_hire/', {
                    'scode': scode,
                    'sname': $('#snamed').val(),
                    }, function (res) {
                        if (res.result == 'True') {
                            alert("修改成功");
                            window.location.reload();
                            } else {
                            alert("修改失败");
                            window.location.reload();
                            }
                    }, 'json')
            },
            cancelValue: '取消',
            cancel: function() {
                console.log(this)
                // do something
            },
            onshow: function() {
                $('#snamed').val(sname);
                // do something
            }
        });
        d.show();
    }