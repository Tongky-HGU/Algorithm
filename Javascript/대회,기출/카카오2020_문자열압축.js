function solution(s) {
    var ans = [];
    for(var i = 0; i<s.length/2; i ++){
        var num = i+1; 
        var count = 1;
        var temp = ""
        for (var j=0;j<s.length;j=j+num){
            var a = s.substring(j,j+num);
            var b = s.substring(j+num,j+num+num)
            if (a == b){
                count +=1
            }else{
                if(count != 1){
                    temp = temp+ count + a;
                }else{
                    temp = temp+ a;
                }
                count = 1;
            }
        }
        // console.log(temp)
        ans.push(temp.length)
    }
    return Math.min(...ans);
}