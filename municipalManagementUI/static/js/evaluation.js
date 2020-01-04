/**/ //函数定义
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
                $("#yearSelector").append("<option value=" +"'" + year + "'" + ">" + year.toString() + "</option>");
            }
            $("#yearSelector").trigger("change");
        },
        error:function (xmlHttpRequest,data,status) {
            console.log("服务器错误!");
        }
    });
};

const checkIfYearsExists = function (yearSelector) {
    let currentYear = yearSelector.options[yearSelector.selectedIndex].value;
    if(currentYear === "没有查询到数据"){
        document.getElementById('evaluateButton').disabled = true;
    }else{
        document.getElementById('evaluateButton').disabled = false;
    }
};

//生成评估
const evaluate = function(){
    let roadSelector = $("#roadSelector")[0];
    let yearSelector = $("#yearSelector")[0];
    //获取道路编号与年份信息
    let roadId = roadSelector.options[roadSelector.selectedIndex].value;
    let year = yearSelector.options[yearSelector.selectedIndex].value;
    if(roadId === undefined || year === undefined){
        return false;
    }
    //从服务器获取评估信息
    $.ajax({
        url:"/municipalManagement/evaluation/evaluate/",
        type:"POST",
        async:true,
        cache:true,
        data:{
            roadId:roadId,
            year:year,
        },
        success:function (data) {
            if (data === '1'){
                alert("评估已存在!");
                return;
            }else if(data === '-1'){
                alert("无记录!");
                return;
            }

            let roadTable = document.getElementById("evaluateTable");
            let newRow = roadTable.insertRow();
            // newRow.setAttribute("onclick","onRoadRowClick(this);");
            for(let i = 0;i<8;i++){
                let newCell = newRow.insertCell();
                newCell.innerHTML="<th>"+data[i]+"</th>";
        }

        },
        error:function () {

        }
    });
};
/**/

//函数调用
$("#evaluateButton").click(evaluate);

