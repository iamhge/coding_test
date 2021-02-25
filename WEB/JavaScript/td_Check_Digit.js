function createCheckDigit(membershipId) {
    // Write the code that goes here.
    var sum = 10
    var _sum = membershipId
    while (sum >= 10) {
        sum = 0
        for (var i = 0; i < _sum.length; i++) {
            sum += Number(_sum[i])
        }
        _sum = String(sum)
    }
    return sum;   
}
  
  console.log(createCheckDigit("55555"));