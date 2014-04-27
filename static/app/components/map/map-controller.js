chillout.controller('MapCtrl', function ($scope,$rootScope) {
	// $scope.$on('$viewContentLoaded',function () {
	console.log('MapCtrl running');

	// set map position
	var map = L.map('mapcontainer').setView([42.356251,-71.095405], 15);
	// draw the map tiles
	L.tileLayer('http://d.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png', {
		attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
		maxZoom: 20
	}).addTo(map);

	// listen to each presentation tick
	$scope.$on('tick',function (event,val) {
		L.marker(val.coordinates).addTo(map);
	});

});