var chillout = angular.module('chillout', [])
.config(function ($routeProvider) {
	$routeProvider.
	when('/calendar', {
		templateUrl: 'components/calendar/calendar.tpl.html',
		controller: 'CalendarCtrl'
	}).
	when('/map', {
		templateUrl: 'components/calendar/map.tpl.html',
		controller: 'MapCtrl'
	}).
	when('/timeseries', {
		templateUrl: 'components/calendar/timesereies.tpl.html',
		controller: 'TimeseriesCtrl'
	}).
	otherwise({
		redirectTo: '/map'
	});
})


// run is where we set initial rootscope properties
.run(function ($rootScope) {
	console.log('Running chillout module');
});
