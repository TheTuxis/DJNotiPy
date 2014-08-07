(function() {
    var app = angular.module('notification', []);

    app.controller('NotificationList', ['$http',  function($http){
        var ntf = this;
        var timer = 60000;
        ntf.notifications = [];
        ntf.see_all = 0;
        $http.get('/ntf/get_new/').success(function(data){
            ntf.notifications = data;
        });

        this.readed = function(id_ntf) {
            event.stopPropagation();
            $http.get('/ntf/readed/'+id_ntf+'/').success(
                function(data){
                    if (ntf.see_all == 0){
                        $http.get('/ntf/get_new/').success(function(data){
                            ntf.notifications = data;
                        });
                    }else{
                        $http.get('/ntf/get_all/').success(function(data){
                            ntf.notifications = data;
                        });
                    }
                }
            ); 
        };


        this.ver_todos = function() {
            event.stopPropagation();
            ntf.see_all = 1;
            $http.get('/ntf/get_all/').success(function(data){
                ntf.notifications = data;
            });
        };

        var tid = setTimeout(update_ntf, timer);
        

        function update_ntf() {
            ntf.see_all = 0;
            $http.get('/ntf/get_new/').success(function(data){
                ntf.notifications = data;
            });
            tid = setTimeout(update_ntf, timer);
        }

        this.update = function() {
            event.stopPropagation();
            ntf.see_all = 0;
            update_ntf()
        };
    }]);

    app.directive('notificationsList', function(){
        return {
            restrict: 'E',
            templateUrl: '/static/html/notifications_list.html'
        }
    });
})();