chillout.controller('MapCtrl', function ($scope) {
	// $scope.$on('$viewContentLoaded',function () {
	console.log('MapCtrl running');
		var map = L.map('mapcontainer').setView([42.359802,-71.126647], 13);
		// to switch these to other tiles, check out the examples at https://github.com/shramov/leaflet-plugins
		// the google api allows for customizable google maps icons
		L.tileLayer('http://d.www.toolserver.org/tiles/bw-mapnik/{z}/{x}/{y}.png', {
			attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
			maxZoom: 18
		}).addTo(map);
		var marker = L.marker([42.359802,-71.126647]).addTo(map);
		// console.log('mapcontainer',mapcontainer);
	// });
});