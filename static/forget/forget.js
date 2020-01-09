$(function () {
    $('#forget_button').click(function () {

            //预先发送csrf值，防止出现403错误
           $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
           $.ajax({
                type: 'POST',
                url: '/forget/', //路由加'/'否则会报ssh错误
                data:$('#log_form').serialize(),
                dataType: 'JSON',
                success: function(data){
                    if(data.status ==200){
                        alert("修改成功");
                          window.open("/logins/");
                    }
                    if(data.status ==500){
                        alert("用户或者key错误");
                          window.open("/forget/");
                    }

            },
        })
    });
});
