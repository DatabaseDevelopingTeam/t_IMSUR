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
        }
    /*地图图层*/


    /*引入高德api*/

    /*引入高德api*/



    //创建地图实例
    var map = L.map("map", {
        center: [29.487967,106.57036],
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

        var popupContent = '<form class="container" id="popupForm" style="width: 200px;">\
        <p><input name = "roadId" type="text" class="form-control" placeholder="道路编号" required autofocus></p>\
        <p><input name = "roadName" type="text" class="form-control" placeholder="道路名称" required autofocus></p>\
        <p>\
            <select class="form-control" name="roadLevel" >\
                <option value="1">一级</option>\
                <option value="2">二级</option>\
                <option value="3">三级</option>\
            </select> \
        </p>\
        <p>\
            <select name = "roadType" class="form-control">\
                <option>沥青路面</option>\
                <option>混凝土路面</option>\
            </select>\
        </p>\
        <p><input id="addRoadBasicInfoSubmit" class="form-control center-block" type="submit" value="提交" style="width: 50%;"></p>\
    </form>';

    	var onPopupSubmit = function () {

    	}

    	var displayMarker = function(e){
    		// var marker = L.marker([e.latlng.lat,e.latlng.lng])
            // .addTo(map);
            var popupOptions = {
            	autoClose:true,
            	closeOnEscapeKey:false,
            	closeOnClick:false,
            }
            L.popup(popupOptions)
            .setLatLng([e.latlng.lat,e.latlng.lng])
            .setContent(popupContent)
            .openOn(map);

            // var popUp = marker.bindPopup()
            // .openPopup();
    	}


        map.on('click',displayMarker);

    /*事件监听*/

    /*道路添加*/
    function createXMLHttpRequest() {
        let xmlHttp;
        try{
            xmlHttp = new XMLHttpRequest();
        }
        catch (e) {
            try {
                // 适用于IE6
                xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
            }catch (e) {
                try {
                    // 适用于IE5.5，以及IE更早版本
                    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                }catch (e) {

                }
            }
        }
        return xmlHttp;
    }
