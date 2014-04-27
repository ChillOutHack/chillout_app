chillout.controller('TimeseriesCtrl', function ($scope) {
	console.log('TimeseriesCtrl running');
    
    var graph = null,
        xAxis = null,
        yAxis = null,
        chartElement = document.getElementById("timeseries-chart");

    var fetchData = function (callback) {
        console.log("fetching");
        $.ajax('/api/data', {
            complete: callback
        });
    };

    var time = new Rickshaw.Fixtures.Time();
    var minute = time.unit('minute');

    var prepData = function (data) {
        /**
         * Gets min, max, and prepares the data points
         */
        data = JSON.parse(data.responseText).reverse();

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

        return {
            min: min,
            max: max,
            points: points
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
            width: 1080,
            height: 280,
            series: [{
                color: 'steelblue',
                data: data.points,
                name: "Temperature"
            }],
            min: data.min - 5,
            max: data.max + 5
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

            graph.series[0].data = data.points;
            graph.update();
            console.log("updated");
        });
    }, 3500);
});