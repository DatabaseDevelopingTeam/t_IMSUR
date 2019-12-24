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