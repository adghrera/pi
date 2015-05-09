var blogControllers = angular.module('blogControllers', []);


blogControllers.controller('HomeCtrl', ['$scope', '$http',
  function ($scope, $http) {
}]);



blogControllers.controller('BlogListCtrl', ['$scope', '$http',
  function ($scope, $http) {
    $http.get('api/v1/blogs').success(function(data) {
      $scope.blogs = data;
    });

    $scope.orderProp = 'id';
}]);

blogControllers.controller('BlogDetailCtrl', ['$scope', '$routeParams',
  function($scope, $routeParams) {
    $scope.phoneId = $routeParams.blogId;
}]);