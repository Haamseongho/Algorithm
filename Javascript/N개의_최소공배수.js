function solution(arr) {
    arr.sort((a, b) => {return a-b});
    var result = arr[0];
    var divisionNumber = 0;
    for(var i=1;i<arr.length;i++){
        divisionNumber = getLargestComDivision(result,  arr[i]); // 최대공약수
        console.log(`최대공약수 : ${divisionNumber}`);
        result = result * arr[i] / divisionNumber;
        console.log(`최소공배수 : ${result}`);
    }
    return result;
}
// a * b / 최대공약수 = 최소공배수
// a % b = r -> b % r = r2 -> r % r2 = r3 ... 나눠지면 그게 최대공약수 (예 : a % b = r, b % r = r2, r % r2 = 0 -> r2가 최대공약수)
function getLargestComDivision(a, b){
    while(a % b !== 0){
        var r = a % b;
        a = b;
        b = r;
    }
    return b;
}
