function solution(sizes) {
    var answer = 0;
    var max_row = [];
    var min_col = [];
    for(var i=0; i<sizes.length; i++){
        max_row.push(Math.max(sizes[i][0], sizes[i][1]));
        min_col.push(Math.min(sizes[i][0], sizes[i][1]));
    }
    
    answer = Math.max(...max_row) * Math.max(...min_col);
    return answer;
}