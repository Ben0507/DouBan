$(function () {
    $('#login_button').click(function () {

            //预先发送csrf值，防止出现403错误
           $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
           $.ajax({
                type: 'POST',
                url: '/logins/', //路由加'/'否则会报ssh错误
                data:$('#log_form').serialize(),
                dataType: 'JSON',
                success: function(data){
                    if(data.status ==200){
                        alert("登陆成功");
                          window.open("/home/?username="+data.msg);
                    }
                    if(data.status ==500){
                        alert("密码不正确")
                    }
            },
        })
    });
});
