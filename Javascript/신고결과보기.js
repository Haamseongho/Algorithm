function solution(id_list, report, k) {
    var result = [];
    var count_id_list = {};
    var report_list = {};
    // Key: 범죄자, Value: 신고자 
    id_list.map((user) => {
        report_list[user] = [];
    });
    // 초기화 시켜두기 > id_list에 순서에 맞게 횟수 0으로 모두 초기화 (신고)
    for(var i=0;i<id_list.length;i++)
        result[i] = 0;
  
    // 같은 범죄자의 신고자는 없앨것 (동일한 신고자가 범죄자를 신고할 때 하나로 취급하듯)
    report.map((user) => {
        let [reporter, criminal] = user.split(" ");
        if(!report_list[criminal].includes(reporter)){
            report_list[criminal].push(reporter);
        }
    });
    for(var criminal in report_list){
        // 범죄자 : 신고자 로 매핑된 리스트에서 범죄자에 매핑된 신고자의 갯수가 k만큼 이상인 경우
        if(report_list[criminal].length >= k){
            // 범죄자에 매핑된 신고자를 id_list에서 찾는데, 해당 신고자의 위치를 찾아서 해당 인덱스의 값을 올린다.
            // 올려야 결과값으로 출력해 낼 때 범죄자로 신고한 신고자의 수를 반환할 수 있음
            report_list[criminal].map((user) => {
                result[id_list.indexOf(user)] += 1;
            })
        }
    }
    
    return result;
}