var headerController = angular.module('headerController', []);

headerController.controller('HeaderCtrl', ['$scope', '$location',
  function ($scope, $location) {
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
}]);

