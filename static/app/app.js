var chillout = angular.module('chillout', [
	'ngRoute',
    'destegabry.timeline'
])
.config(function ($routeProvider) {
	$routeProvider.
	when('/calendar', {
		templateUrl: 'static/app/components/calendar/calendar.tpl.html',
		controller: 'CalendarCtrl'
	}).
	when('/mapandchart', {
		templateUrl: 'static/app/components/mapandchart/mapandchart.tpl.html'
	}).
	when('/map', {
		templateUrl: 'static/app/components/map/map.tpl.html'
	}).
	when('/timeseries', {
		templateUrl: 'static/app/components/timeseries/timeseries.tpl.html'
	}).
	otherwise({
		redirectTo: '/mapandchart'
	});
})


// run is where we set initial rootscope properties
.run(function ($rootScope) {
	console.log('Running chillout module');
})

.controller('RouteCtrl',function ($scope,$location) {
	$scope.reRoute = function (path) {
		console.log('switching path to:',path);
		$location.path(path);
		$scope.activeBtn = path.slice(1);
	}
});
