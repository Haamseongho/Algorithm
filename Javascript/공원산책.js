function solution(park, routes) {
    var answer = [];
    var direction = {
        "N" : [-1, 0],
        "E" : [0, 1],
        "W" : [0, -1],
        "S" : [1, 0]
    }
    // 시작위치
    var x = 0;
    var y = 0;
    for(var i=0;i<park.length;i++){
        for(var j=0;j<park[i].length;j++){
            if(park[i][j] == "S"){
                x = i;
                y = j;
            }
        }
    }
    
    for(var i=0;i<routes.length;i++){
        var dir = routes[i].split(" ")[0];
        var cnt = routes[i].split(" ")[1];
        var move_x = direction[dir][0];
        var move_y = direction[dir][1];
        // 장애물에 걸린 경우 다시 원 상태에서 다음 조건을 접해야하므로 이전 상태값 저장 
        var prev_x = x; 
        var prev_y = y; 
        for(var j=0;j<cnt;j++){
            x += move_x;
            y += move_y;
            if((x >= 0 && x < park.length) && (y >= 0 && y < park[x].length)){
                if(park[x][y] == "X"){
                    x = prev_x;
                    y = prev_y;
                    break;
                }
            } 
            else {
                x = prev_x;
                y = prev_y;
                break;
            }
            
            
        }
   
    }
    return [x,y];
}