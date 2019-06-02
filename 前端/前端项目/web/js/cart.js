$(function () {
    // 总价 总数量
    function sum() {
        var totalPrice = 0;
        var totalNum = 0;
        // 遍历所有选中商品 获取总价
        $("img[check=true]").each(function () {
            var num = Number($(this).parent().siblings(".count").find("input").val());
            var priceStr = $(this).parent().siblings(".sum").html();
            console.log(priceStr);
            var price = Number(priceStr.substring(1));
            console.log(price);
            totalPrice += price;
            totalNum += num;
        });
        // 修改标签
        $(".total-num").html(totalNum);
        $(".total-price").html("¥" + totalPrice);
    }


    // 全选和取消全选
    var checkall = false;
    $("#checkall").click(function () {
        checkall = !checkall;
        if (checkall) {
            $(this).attr("src", "../images/cart/product_true.png");
            $(".choose").attr("src", "../images/cart/product_true.png").attr("check", "true")
        } else {
            $(this).attr("src", "../images/cart/product_normal.png");
            $(".choose").attr("src", "../images/cart/product_normal.png").removeAttr("check")
        }
        sum()
    });

    //  选中 反选
    $(".choose").click(function () {
        if ($(this).attr("check")) {
            $(this).attr("src", "../images/cart/product_normal.png").removeAttr("check")
        } else {
            $(this).attr("src", "../images/cart/product_true.png").attr("check", "true")
        }
        if ($("img[check=true]").length == $(".choose").length) {
            $("#checkall").attr("src", "../images/cart/product_true.png");
            checkall = true;
        } else {
            $("#checkall").attr("src", "../images/cart/product_normal.png");
            checkall = false;
        }
        sum()
    });

    // - 1 价格联动
    $(".decrement").click(function () {
        var count = $(this).next().val();

        if (count > 1) {
            $(this).next().val(--count);
        }
        var priceStr = $(this).parent().prev().find("span").eq(1).html();
        var price = priceStr.substring(1);
        $(this).parent().next().html("¥" + count * price);
        sum()
    });

    // + 1 价格联动
    $(".increment").click(function () {
        var count = $(this).prev().val();
        $(this).prev().val(++count);
        var priceStr = $(this).parent().prev().find("span").eq(1).html();
        var price = priceStr.substring(1);
        $(this).parent().next().html("¥" + count * price);
        sum()
    });

    // 移除
    $(".action a").click(function () {
        $(this).parents(".item").remove();
        sum()
    });


});