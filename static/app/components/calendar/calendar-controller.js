chillout.controller('CalendarCtrl', function ($scope) {

    $scope.allData = [];
    $scope.ids = [];

    var options = {
      "width":  "100%",
      "height": "600px",
      "style": "box",
      "editable": true,
        "cluster": true,
        "showNavigation": true
    };

    $scope.options = options;

	var fetchData = function (callback) {
        console.log("fetching");
        $.ajax('/api/data', {
            success: callback
        });
    };

    var renderLine = function(data){
        data = JSON.parse(data);
        data = data.events;
        for(var i = 0; i < data.length; i++){
            if($scope.ids.indexOf(data[i].id) === -1){
                if(data[i].peltier > 30){
                    $scope.allData.push({
                        start: Date.parse(data[i].created),
                        content: data[i].peltier
                    });
                    $scope.ids.push(data[i].id);
                }
            }
        }
    };

    window.setInterval(function(){
        //update function by polling every 3.5 seconds
        fetchData(function(d){
            renderLine(d);
        });
    }, 3500);

});