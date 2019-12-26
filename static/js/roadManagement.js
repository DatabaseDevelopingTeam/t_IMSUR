    /*地图层*/
        //高德地图
        // var Gaode = L.tileLayer.chinaProvider('GaoDe.Normal.Map', {
        //     maxZoom: 18,
        //     minZoom: 12
        // });
        //OMS地图
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
    /*地图图层*/


    /*引入高德api*/

    /*引入高德api*/



    //创建地图实例
    var map = L.map("map", {
        center: [29.507165702686823, 106.55347824096681],
        zoom: 18,
        layers: [oms],
        scrollWheelZoom: false
    });






    /*添加控件*/
        //图层切换控件
        L.control.layers(baseLayers, null).addTo(map);
        //缩放控件
        // L.control.zoom({
        //     zoomInTitle: '放大',
        //     zoomOutTitle: '缩小'
        // }).addTo(map);
    /*添加控件*/

    //初始化地图
    var loadAllRoads = function () {
        //得到经纬度与道路编号
        $.ajax({
          type:"POST",
            url:"/municipalManagement/roadManagement/getAllRoadsLatLng/",
            async:true,
            cache:true,
            data:{

            },
            success:function (data) {
                for(var i =0;i<data.length;i++){
                    roadId = data[i]['roadId'];
                    latlng = data[i]['latlng'];
                    roadLevel = data[i]['roadLevel'];
                    //添加道路麻点
                    var marker = addMarker(latlng);
                    ////绑定popup信息框
                     $.ajax({
                        type:"POST",
                        url:"/municipalManagement/roadManagement/getRoadInfoPopup/",
                         async:false,
                        cache:true,
                        data:{
                            roadId:roadId,
                            },
                        success:function(data,status){
                            marker.bindPopup(data);
                             //更换图标
                           adjustMarkerIcon(marker,roadLevel);
                        },
                        error:function () {

                        }
                    });
                }
            },
            error:function () {
                console.log("服务器错误!");
            }
        })


    };

    loadAllRoads();


    /*事件监听*/
        // map.on('click',function outputLngLat(e){
        //     var gps = [e.latlng.lng,e.latlng.lat];
        //     console.log(gps);
        //     AMap.convertFrom(gps, 'gps', function (status, result) {
        //       console.log(status);
        //       console.log(result);
        //       if (result.info != 'ok') {
        //         var lnglats = result.locations; // Array.<LngLat>
        //         console.log(lnglats);
        //       }
        //     });
        // })

        //添加道路的pop框
    const roadAddPopupContent = '<form "class="container" id="popupForm" style="width: 200px;">\
            <p><input onchange="onCheckIfRoadIdExists()" name = "roadId" id="roadId" type="text" class="form-control" placeholder="道路编号" required autofocus></p>\
            <span style="color: red; margin: 0;padding: 0;" id="wrongInfo"></span>\
            <p><input name = "roadName" id="roadName" type="text" class="form-control" placeholder="道路名称" required autofocus></p>\
            <p>\
                <select class="form-control" id="roadLevel" name="roadLevel" >\
                    <option value="1">一级</option>\
                    <option value="2">二级</option>\
                    <option value="3">三级</option>\
                </select> \
            </p>\
            <p>\
                <select name = "roadType" id="roadType" class="form-control">\
                    <option>沥青路面</option>\
                    <option>混凝土路面</option>\
                </select>\
            </p>\
            <p><input onclick="addRoadBasicInfo();return false;" class="form-control center-block" type="button" value="提交" style="width: 50%;"></p>\
        </form>';

    //显示道路信息的pop框
    var roadInfoPopupContent = '<html>' +
        '<body>' +
        '<p>nothing at all</p>' +
        '</body>' +
        '</html>';

    //异步请求道路编号是否重复
        function onCheckIfRoadIdExists(){
            var roadId = $("[name='roadId']").val();
            // console.log(roadId);
             $.ajax({
                type:"POST",
                url:"/municipalManagement/roadManagement/checkIfRoadIdExists/",
                async:true,
                cache:false,
                data:{
                    roadId:roadId,
                },
                success:function (data) {
                    if (data === '1'){
                        $("#wrongInfo").text('');
                        $("[value='提交']").attr("disabled",false);
                    }
                    else{
                        $("#wrongInfo").text('编号已存在!');
                        $("[value='提交']").attr("disabled",true);
                    }

                },
                error:function () {
                    console.log("服务器错误!");
                }
            });
        }
        //异步添加道路信息到服务器
        function addRoadBasicInfo() {

            //bootstrap自动判空

            $.ajax({
                type:"POST",
                url:"/municipalManagement/roadManagement/addRoadBasicInfo/",
                async:true,
                cache:true,
                data:{
                    roadId:$("#roadId").val(),
                    roadName:$("#roadName").val(),
                    roadLevel:$("#roadLevel option:selected").val(),
                    lng :currentLatLng[1],
                    lat:currentLatLng[0],


                    // roadType:$("#roadType option:selected").val(),
                },
                success:function(data,status){
                    closePopupFlag = false;
                    currentMarker.closePopup();
                    currentMarker.unbindPopup();

                    $.ajax({
                        type:"POST",
                        url:"/municipalManagement/roadManagement/getRoadInfoPopup/",
                         async:true,
                        cache:true,
                        data:{
                            roadId:$("#roadId").val(),
                            },
                        success:function(data,status){
                           currentMarker.bindPopup(data);
                           //更换图标
                           adjustMarkerIcon(currentMarker,$("#roadLevel option:selected").val());
                        },
                        error:function () {

                        }
                    });


                    // addMarker(currentLatLng);
                    // currentPopup.openPopup();
                    // $(".leaflet-popup-close-button").trigger("click");
                },
                error:function (xmlHttpRequest,data,status) {
                    console.log("添加失败!");
                    closePopupFlag = true;
                    currentMarker.remove();
                }
            });
        }

        var addMarker = function (latlng) {
            return L.marker(latlng).addTo(map);
        };

        //调整道路麻点图标
        var adjustMarkerIcon = function (marker,level) {
            var iconOptions = {
                iconUrl: '/static/images/level1.png',
                iconSize: [80, 80],
                iconAnchor: [22, 94],
                popupAnchor: [-3, -76],
            };

          if(level==='1'){

          }else if (level==='2'){
            iconOptions['iconUrl'] = "/static/images/level2.png";
          }else if(level === '3'){
            iconOptions['iconUrl'] = "/static/images/level3.png";
          }
          var myIcon = L.icon(iconOptions);
          marker.setIcon(myIcon);
        };

        var closePopupFlag=true;
        var currentLatLng;
        var currentPopup;
        var currentMarker;
    	var addRoad = function(e){
    		currentLatLng = [e.latlng.lat,e.latlng.lng];
    		// console.log(currentLatLng);
            var popupOptions = {
            	// autoClose:false,
            	// closeOnEscapeKey:false,
            	// closeOnClick:true,
            };

            currentMarker = L.marker([e.latlng.lat,e.latlng.lng]).addTo(map)
                .bindPopup(roadAddPopupContent)
                .openPopup();

            currentMarker.on("popupclose",function () {
                if(closePopupFlag){
                    currentMarker.remove();
                }

            })

            // currentPopup = L.popup(popupOptions)
            // .setLatLng([e.latlng.lat,e.latlng.lng])
            // .setContent(roadAddPopupContent)
            // .openOn(map);


            // $("#addRoadBasicInfoSubmit").click(function () {
            //     $.ajax({
            //         type:"POST",
            //         url:"/municipalManagement/roadManagement/addRoadBasicInfo/",
            //         async:true,
            //         cache:false,
            //         data:{
            //             roadId:$("#roadId").val(),
            //             roadName:$("#roadName").val(),
            //             roadLevel:$("#roadLevel option:selected").val(),
            //         },
            //         success:function (data) {
            //             console.log(data);
            //         },
            //         error:function (xmlhttpRequest,data) {
            //             console.log(data);
            //         }
            //
            //     });
            //
            //
            //  });

            // var popUp = marker.bindPopup()
            // .openPopup();
    	};


        map.on('click',addRoad);

    /*事件监听*/
