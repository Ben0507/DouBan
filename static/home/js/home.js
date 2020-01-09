$(function () {
    $("#list").on('click', 'li', function () {
        if (!$(this).attr('s')) {
            $('#select').val(this.innerHTML)
            // 获取list清除下面的li
            var div = document.getElementById("list");
            while (div.hasChildNodes()) //当div下还存在子节点时 循环继续
            {
                div.removeChild(div.firstChild);
            }
        } else {
        }
    })
    $('#search').click(function () {
        window.location.href = "/showsearch/?select=" + $('#select').val()
    })

    $('#select').on('keyup', function () {
        if ($('#select').val() !=""){
        $.ajax({
            type: 'GET',
            url: '/search/', //路由加'/'否则会报ssh错误
            data: {"select": $('#select').val()},
            dataType: 'JSON',
            success: function (data) {
                if (data.status == 200) {
                    list = data.keyword
                    var item=null;
                    for (var i = 0; i < list.length; i++) {
                        // alert(list[i])
                         item = document.createElement('li');
                        item.innerHTML = list[i];
                        document.getElementById('list').appendChild(item)
                    }
                }
            },
        })
            }
    });
    //
    //
    // $('#select').on('compositionend', function () {
    //     $.ajax({
    //         type: 'GET',
    //         url: '/search/', //路由加'/'否则会报ssh错误
    //         data: {"select": $('#select').val()},
    //         dataType: 'JSON',
    //         success: function (data) {
    //             if (data.status == 200) {
    //                 list = data.keyword
    //                 for (var i = 0; i < list.length; i++) {
    //                     // alert(list[i])
    //                     var item = document.createElement('li');
    //                     item.innerHTML = list[i];
    //                     document.getElementById('list').appendChild(item)
    //                 }
    //             }
    //         },
    //     })
    // });



});
