function checkIfEmployeeIdExists(self) {
    var employee_id=self.value;
    var xmlhttp=createXMLHttpRequest();
    xmlhttp.open("POST","/ajaxEmployeeIdCheck/",true);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send("employee_id="+employee_id);

    xmlhttp.onreadystatechange=function () {
        if(xmlhttp.readyState===4 && xmlhttp.status===200){
            var s=xmlhttp.responseText;
            if (s==="1"){
                document.getElementById("idError").innerHTML="工号不存在!";
                document.getElementById('submitInput').disabled = true
            }else{
                document.getElementById("idError").innerHTML="";
                document.getElementById('submitInput').disabled = false
            }
        }
    }
}

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