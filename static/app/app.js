var chillout = angular.module('chillout', [
	'ngRoute'
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
.run(function ($rootScope,$timeout) {
	console.log('Running chillout module');
	var seconds = 0;
	console.log('storydata',angular.copy(storyData));
	angular.forEach(storyData,function (val,i) {
		// body...
		$timeout(function () {
			$rootScope.$broadcast('tick', val);
		},seconds += 1000);
	});
})

.controller('RouteCtrl',function ($scope,$location) {
	$scope.reRoute = function (path) {
		console.log('switching path to:',path);
		$location.path(path);
		$scope.activeBtn = path.slice(1);
	}
});