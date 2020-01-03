//选择道路时更新年份
const updateYearSelector = function (roadSelector) {
    let roadId = roadSelector.options[roadSelector.selectedIndex].value;
    $.ajax({
        url:"/municipalManagement/evaluation/getYearsByRoadId/",
        type:"GET",
        async:true,
        cache:true,
        data:{
            roadId:roadId,
        },
        success:function (data) {
            //清空yearSelector
            $("#yearSelector").empty();
            //添加年份到yearSelector
            let years = data;
            let year;
            for(let i=0;i<years.length;i++){
                year = years[i];
                $("#yearSelector").append("<option>" + year.toString() + "</option>");
            }
        },
        error:function (xmlHttpRequest,data,status) {
            console.log("服务器错误!");
        }
    });
};
