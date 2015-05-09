var myApp = angular.module('myApp', [ 'ui.bootstrap', 'ngRoute',
		'blogControllers', 'headerController' ]);


myApp.config(['$routeProvider',
                    function($routeProvider) {
                      $routeProvider.
                        when('/blogs', {
                          templateUrl: 'static/partials/blog-list.html',
                          controller: 'BlogListCtrl'
                        }).
                        when('/blogs/:blogId', {
                          templateUrl: 'static/partials/blog-detail.html',
                          controller: 'BlogDetailCtrl'
                        }).
                        when('/', {
                            templateUrl: 'static/partials/home.html',
                            controller: 'HomeCtrl'
                        }).
                        otherwise({
                          redirectTo: '/home'
                        });
                    }]);