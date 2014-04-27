chillout.controller('TimeseriesCtrl', function ($scope) {
	console.log('TimeseriesCtrl running');
    
    var graph = null,
        xAxis = null,
        yAxis = null;

    var fetchData = function () {
        $.ajax('/api/data', {
            complete: renderGraph
        });
    };

    var time = new Rickshaw.Fixtures.Time();
    var minute = time.unit('minute');

    //more stuff here for reference
    //http://code.shutterstock.com/rickshaw/
	var renderGraph = function (data) {
        /**
         * Renders the graph with data retrieved from the remote service /api/data
         */

        data = JSON.parse(data.responseText);

        //this is hacky, but will have to suffice for now
        var min = 100,
            max = 0;

        var points = data.map(function (d) {
            var x_value = d.temp;

            if (x_value > max) {
                max = x_value;
            }
            if (x_value < min) {
                min = x_value;
            }
            return {
                //currently displaying as GMT
                x: Date.parse(d.created)/1000, //wow i can't believe this works!
                y: x_value
            }
        });
        
        graph = new Rickshaw.Graph( {
            element: document.querySelector("#timeseries-chart"),
            width: 800,
            height: 280,
            series: [{
                color: 'steelblue',
                data: points,
                name: "Temperature"
            }],
            min: min - 5,
            max: max + 5
        });

        xAxis = new Rickshaw.Graph.Axis.Time({
            graph: graph,
            timeUnit: minute
        });

        yAxis = new Rickshaw.Graph.Axis.Y({
            graph: graph
        });

        var hoverDetail = new Rickshaw.Graph.HoverDetail ({
            graph: graph,
            // xFormatter: function(x) {return x},
            // yFormatter: function(y) {return "Temp" + y}
        });

        graph.render();
        xAxis.render();
        yAxis.render();
	};


    fetchData();
	//renderGraph();
});