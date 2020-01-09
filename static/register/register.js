$(function () {
    $('#registe-button').click(function () {
            //预先发送csrf值，防止出现403错误
           $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
           $.ajax({
                type: 'POST',
                url: '/register/', //路由加'/'否则会报ssh错误
                data:$('#log_form').serialize(),
                dataType: 'JSON',
                success: function(data){
                    if(data.status ==200){
                        window.location.reload();
                        alert('注册成功')
                    }
                    else if(data.status ==500){
                        window.location.reload();
                        alert('用户名重复')
                    }
            },
        })
    });
});
