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
function hire(scode, sname, stafftype, jobname, staffstatus ){
    var d = dialog({
            width: 300,
            title: '员工姓名修改',
            quickClose: true,
            content: '<label>姓名：</label>' + '<input type="text" id="snamed" placeholder="">' + '<p></p>' +
                '<label>类型：</label>' +  '<select style="height: 20px; width:100px" id="stafftyped">\n' +
                    '<option value="正职">正职</option>\n' +
                    '<option value="实习生">实习生</option>\n' +
                    '<option value="外包">外包</option>\n' +
                    '<option value="内包">内包</option>\n' +
                    '<option value="基地">基地</option>\n' + '</select>' + '<p></p>' +
                '<label>岗位名称：</label>' +'<input type="text" id="job_id" placeholder="">' + '<p></p>' +
                '<label>状态：</label>' + '<select style="height: 20px; width:100px" id="staffstatused">\n' +
                    '<option value="在职">在职</option>\n' +
                    '<option value="offer">offer</option>\n' +
                    '<option value="待招">待招</option>\n' + '</select> ',
            ok: function() {
                    $.post('/staff_hire/', {
                        'scode': scode,
                        'sname': $('#snamed').val(),
                        'stafftype':$('#stafftyped').val(),
                        'jobname_id':$('#job_id').val(),
                        'staffstatus': $('#staffstatused').val(),
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
                $('#stafftyped').val(stafftype);
                $('#job_id').val(jobname);
                $('#staffstatused').val(staffstatus);
                // do something
            }
        });
        d.show();
    }