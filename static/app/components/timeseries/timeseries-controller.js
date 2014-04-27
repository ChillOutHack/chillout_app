chillout.controller('TimeseriesCtrl', function ($scope) {
	console.log('TimeseriesCtrl running');
    
    var graph = null,
        xAxis = null,
        yAxis = null,
        chartElement = document.getElementById("timeseries-chart"),
        time = new Rickshaw.Fixtures.Time(),
        minute = time.unit('minute');

    var fetchData = function (callback) {
        console.log("fetching");

        $.ajax('/api/data?num_requests=50', {
            type: 'GET',
            complete: callback
        });
    };

    var prepData = function (data) {
        /**
         * Gets min, max, and prepares the data points
         */
        data = JSON.parse(data.responseText);
        data.events.reverse();

        var tempPoints = data.events.map(function (d) {
            return {
                //currently displaying as GMT
                x: Date.parse(d.created)/1000, //wow i can't believe this works!
                y: d.temp
            }
        });

        var peltierPoints = data.events.map(function(d){
            return {
                //currently displaying as GMT
                x: Date.parse(d.created)/1000, //wow i can't believe this works!
                y: d.peltier
            }
        });

        var pentiometerPoints = data.events.map(function(d){
            return {
                //currently displaying as GMT
                x: Date.parse(d.created)/1000, //wow i can't believe this works!
                y: d.pentiometer                
            }
        });

        var max = Math.max(data.max_peltier, data.max_temp),
            min = Math.min(data.max_peltier, data.max_temp);

        return {
            min: min - 20,
            max: max,
            tempPoints: tempPoints,
            peltierPoints: peltierPoints,
            pentiometerPoints: pentiometerPoints
        };
    };

    //more stuff here for reference
    //http://code.shutterstock.com/rickshaw/
	var renderGraph = function (data) {
        /**
         * Renders the graph with data retrieved from the remote service /api/data
         */
        data = prepData(data);

        chartElement.innerHTML = "";
        
        graph = new Rickshaw.Graph( {
            element: chartElement,
            width: 1100,
            height: 480,
            renderer: 'line',
            series: [
                {
                    color: 'steelblue',
                    data: data.tempPoints,
                    name: "Temperature"
                },
                {
                    color: 'lightblue',
                    data: data.peltierPoints,
                    name: "Peltier"
                }],
            min: data.min - 10,
            max: 200,
            interpolation: 'linear'
        });

        var format = function(d) {
            d = new Date(d*1000)
            return d3.time.format('%b %e %X')(d)
        };

        xAxis = new Rickshaw.Graph.Axis.X({
                graph: graph,
                tickFormat: format,
                ticks: 4
        });

        yAxis = new Rickshaw.Graph.Axis.Y({
            graph: graph
        });

        var hoverDetail = new Rickshaw.Graph.HoverDetail ({
            graph: graph,
            xFormatter: function(x) {return new Date(x*1000)}
        });

        graph.render();
        xAxis.render();
        yAxis.render();
	};

    fetchData(renderGraph);

    window.setInterval(function(){
        //update function by polling every 3.5 seconds
        fetchData(function(d){
            data = prepData(d);

            graph.series[0].data = data.tempPoints;
            graph.series[1].data = data.peltierPoints;
            graph.update();
            console.log("updated");
        });
    }, 3500);
});