chillout.controller('MapCtrl', function ($scope,$rootScope) {
	// $scope.$on('$viewContentLoaded',function () {
	console.log('MapCtrl running');

	// set map position
	var map = L.map('mapcontainer').setView([42.359802,-71.126647], 13);
	// draw the map tiles
	L.tileLayer('http://d.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png', {
		attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
		maxZoom: 18
	}).addTo(map);

	// listen to each presentation tick
	$scope.$on('tick',function (event,val) {
		L.marker(val.coordinates).addTo(map);
	});

});