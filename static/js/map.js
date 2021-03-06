var cachedRoadsLatlng={};    //缓存的道路位置信息字典

//oms地图
var oms = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
            minZoom: 14,
            maxZoom: 19,
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            id: 'mapbox.streets'
        });
//地图选择图层
var baseLayers = {
            // "高德地图": Gaode,
            "OMS":oms
        };
//创建地图实例
var map = L.map("rightmap", {
        center: [29.507165702686823, 106.55347824096681],
        zoom: 18,
        layers: [oms],
        scrollWheelZoom: false
    });

//缓存今日巡查任务的道路经纬度信息
var cacheRoadsLatlng = function () {
        $.ajax({
            url:"/patrolManagement/patrolMap/getRoadsLatlng/",
            type:"POST",
            async:true,
            cache:true,
            data:{},
            success:function (data) {
                cachedRoadsLatlng = data;
            }
        })
    };

//道路表点击事件,获取道路信息
    var LocateRoad = function(self){
        var roadId = self.firstElementChild.innerHTML;
        var latlng = cachedRoadsLatlng[roadId];     //根据id获取位置信息
        if(typeof(latlng) == "undefined"){
            cacheRoadsLatlng();
        }
        resetCenterCoordinate(latlng);
    };


    //重设中心点
    var resetCenterCoordinate = function (latlngCoordinate) {
        map.flyTo(latlngCoordinate);
    };

    //初始化地图
    var loadAllRoads = function () {
        //得到经纬度与道路编号
        $.ajax({
            type: "POST",
            url: "/patrolManagement/patrolMap/getTodayRoadsBasicInfo/",
            async: true,
            cache: true,
            data: {},
            success: function (data) {
                for (var i = 0; i < data.length; i++) {
                    roadId = data[i]['roadId'];
                    roadName = data[i]['roadName'];
                    latlng = data[i]['latlng'];
                    roadLevel = data[i]['roadLevel'];
                    //添加道路麻点
                    var marker = addMarker(latlng);
                    ////绑定popup信息框
                    $.ajax({
                        type: "POST",
                        url: "/patrolManagement/patrolMap/getRoadInfoPopup/",
                        async: false,
                        cache: true,
                        data: {
                            roadId: roadId,
                        },
                        success: function (data, status) {
                            marker.bindPopup(data);
                            //更换图标
                            adjustMarkerIcon(marker, roadLevel);
                        },
                        error: function () {
                            console.log("绑定POP失败！");
                        }
                    });
                }
            },
            error: function () {
                console.log("服务器错误!");
            }
        })
    };

    //向地图添加麻点
    var addMarker = function (latlng) {
        return L.marker(latlng).addTo(map);
    };

     //调整道路麻点图标
    var adjustMarkerIcon = function (marker,level) {

      iconUrl = level==='1'?'/static/images/1.png':(level==='2'?'/static/images/2.png':'/static/images/3.png');

      marker.setIcon(L.icon({
        iconUrl: iconUrl,
        iconSize: [16*4, 19*4],
        iconAnchor: [16*4-31,19*4],
        popupAnchor: [0,-19*4],
      }));
    };


//模态框展示函数
$('#myModal').on('show.bs.modal',function(e)
{
    var button=$(e.relatedTarget);
    var roadId=button.data('roadid');
    $("#damageType").empty();
    $("#tabbody").empty();
    $("#describe").val("");
    $("#note").val("");
    $.ajax({
        type: "POST",
        url: "/patrolManagement/patrolMap/setupModalView/",
        async: false,
        cache: true,
        data: {
            roadId: roadId,
        },
        success: function (data, status) {
            $("#roadId").val(data['roadId'])
            $("#roadName").val(data['roadName'])
            $("#roadType").val(data['roadType'])
            var length=Number(data['length'])
            console.log(length)
            console.log(data)
            for(var i=1;i<length;i++)
            {
                $("#damageType").append("<option value="+data[i]+">"+data[i]+"</option>")
            }
            console.log(data['employeeId'])
            console.log(data['employeeName'])
        },
        error: function () {
            console.log("服务器异常");
        }
    });
})

//提交函数
function patrolEnd()
{
	var con;
    //取消回车绑定事件
    document.onkeydown=function(event){
        var e=event||window.event;
        if(e && e.keyCode == 13)
        {
            event.prevent();
        }
    };
	con=confirm("是否提交？"); //在页面上弹出对话框
	if(con==true)
	{
        //将数据写入数据库
        var tab=document.getElementById("mytab");
        //获取道路编号
        var roadId=$("#roadId").val();
        //获取路面类型
        var roadType=$("#roadType").val();
        var length =tab.rows.length;
        console.log(length);
        var info={};
        for(let i=1; i<length; i++)
        {
            let j = i - 1;
            info[j.toString()] = {
                'damageType': tab.rows[i].cells[0].innerHTML,
                'damageDetail' : tab.rows[i].cells[1].innerHTML,
                'note' : tab.rows[i].cells[2].innerHTML,
            };
        }
        info = JSON.stringify(info);
        console.log(info);
        $.ajax({
            type: "POST",
            url: "/patrolManagement/patrolMap/AddDailyPatrolRecord/",
            async: false,
            cache: true,
            data: {
                roadId: roadId,
                roadType:roadType,
                infos:info,
            },
            success: function (data, status) {
                //隐藏模态框
		        $("#myModal").modal('hide');
		        location.reload();
            },
            error: function () {
                console.log("服务器异常");
            }
        });
	}
	else
    {
        document.onkeydown=function(event){
            var e=event||window.event;
            if(e && e.keyCode == 13)
            {
                patrolEnd();
            }
        }
    }
}

//添加巡查信息到表格
function addPatrolInfo() {
    var damageType=$("#damageType").val();
    var damageDetail=$("#damageDetail").val();
    var note=$("#note").val();
    var newRow=$('<tr><td style="text-align: center;vertical-align:middle!important;">'+damageType+'</td>' +
        '<td style="text-align: center;vertical-align:middle!important;">'+damageDetail+'</td>' +
        '<td style="text-align: center;vertical-align:middle!important;">'+note+'</td>' +
        '<td  style="text-align: center;vertical-align:middle!important;">' +
        '<input type="button" value="删除" class="btn btn-primary" onclick="removePatrolInfo(this)" ' +
        ' style="width:100%;" "></td></tr>');
    $("#tabbody").append(newRow);
};

function removePatrolInfo(e){
    if(confirm("是否删除"))
        $(e).parent("td").parent("tr").remove();
}

//函数调用
loadAllRoads();             //初始化地图，显示麻点
cacheRoadsLatlng();         //缓存道路位置信息

