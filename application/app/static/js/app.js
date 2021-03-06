/* App Module */

angular.module('fileCreator', ['ui.router', 'webui-core', 'ngFileUpload']);

angular.module('fileCreator').config(routes);
routes.$inject = ['$stateProvider', '$urlRouterProvider'];
function routes($stateProvider, $urlRouterProvider) {
    // console.log("routing");
    $urlRouterProvider.otherwise('/');
    $stateProvider.state('part-search', {
        url: '/',
        templateUrl: 'views/part-search.html',
        controller: 'partNumberSearch'
    });
}

angular.module('fileCreator').controller('partNumberSearch', ['$scope', '$timeout', '$http', function ($scope, $timeout, $http) {
    $scope.fields = [
        {name: 'TEST_PO_x', value: ""},
        {name: 'VENDOR_NUMBER', value: ""},
        {name: 'REC_QUAL', value: ""},
        {name: 'REC_ID', value: ""},
        {name: 'JANE SMITH', value: ""},
        {name: '888-739-3232', value: ""},
        {name: 'TEST_PO_x', value: ""},
        {name: 'VENDOR_PART_NUM', value: ""},
        {name: 'UPC_CASE_CODE', value: ""},
        {name: 'ITEM_DESCRIPTION', value: ""}
    ];
    $scope.showList = false;
    $scope.newFields = [];
    $scope.addFields = function () {
        $scope.showList = true;
        $scope.newFields = angular.copy($scope.fields);
    };
    $scope.removePair = function (index) {
        $scope.newFields.splice(index, 1);
    };

    $scope.uploadFiles = function (files, errFiles) {
        // console.log('TESTING');
        $scope.files = files;
        $scope.errFiles = errFiles;
    };

    $scope.submit = function () {
        console.log($scope.newFields);
        console.log($scope.files);
        var jsonData = JSON.stringify({
            regex: $scope.newFields
        });

        var fd = new FormData();
        angular.forEach($scope.files, function (file) {
            fd.append('zip', file);
        });
        fd.append("data", jsonData);

        $http({
            url: "create_test_files",
            method: 'POST',
            responseType: 'arraybuffer',
            cache: false,
            data: fd,
            headers: {
                'Content-Type': undefined
            }
            }).success(function (data) {
                console.log(data);
                var blob = new Blob([data], {type: "application/octet-stream"});
                var fileDownload = angular.element('<a></a>');
                fileDownload.attr('href', window.URL.createObjectURL(blob));
                fileDownload.attr('download', 'testfilecreator.zip');
                fileDownload[0].click();
                console.log('downloaded');

        });

    }
}]);
